#!/usr/bin/env python3
"""三页确定性烟测：页序、真实图标、禁图、后处理与原生 DrawingML 导出必须可用。"""

import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

def main() -> int:
    scripts_dir = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory(prefix="ppt-smoke-") as raw_dir:
        project = Path(raw_dir)
        for name in ("svg_output", "svg_final", "notes", "exports"):
            (project / name).mkdir()

        pages = {
            "01.svg": (
                '<use data-icon="tabler-filled/bulb" x="80" y="80" width="48" height="48" fill="#315B7D"/>'
                '<text x="150" y="118" font-family="Microsoft YaHei, Arial, sans-serif" '
                'font-size="36" fill="#24313A">01-confirmed-cover</text>'
            ),
            "02.svg": (
                '<circle cx="300" cy="340" r="120" fill="#E8EEF3"/>'
                '<path d="M 470 340 L 850 340" stroke="#315B7D" stroke-width="8"/>'
                '<text x="80" y="110" font-family="Microsoft YaHei, Arial, sans-serif" '
                'font-size="36" fill="#24313A">02-confirmed-concept</text>'
            ),
            "03.svg": (
                '<rect x="80" y="170" width="1120" height="260" fill="#E8EEF3"/>'
                '<text x="80" y="110" font-family="Microsoft YaHei, Arial, sans-serif" '
                'font-size="36" fill="#24313A">03-confirmed-summary</text>'
            ),
        }
        for filename, body in pages.items():
            (project / "svg_output" / filename).write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720">'
                '<rect width="1280" height="720" fill="#FFFFFF"/>'
                f'{body}</svg>',
                encoding="utf-8",
            )
        subprocess.run(
            [sys.executable, str(scripts_dir / "finalize_svg.py"), str(project)],
            check=True,
            timeout=60,
        )
        previews = [
            (project / "svg_final" / filename).read_text(encoding="utf-8")
            for filename in pages
        ]
        if "data-icon=" in previews[0]:
            raise RuntimeError("svg_final 仍含未展开图标")
        if any("<image" in preview or "data:image/" in preview for preview in previews):
            raise RuntimeError("svg_final 意外包含图片")
        pptx = project / "exports" / "smoke.pptx"
        subprocess.run(
            [
                sys.executable,
                str(scripts_dir / "svg_to_pptx.py"),
                str(project),
                "-o",
                str(pptx),
                "--only",
                "native",
                "--no-notes",
                "-t",
                "none",
            ],
            check=True,
            timeout=60,
        )
        with zipfile.ZipFile(pptx) as package:
            slide_names = [f"ppt/slides/slide{index}.xml" for index in range(1, 4)]
            slides = [package.read(name).decode("utf-8") for name in slide_names]
            expected = ["01-confirmed-cover", "02-confirmed-concept", "03-confirmed-summary"]
            if any(title not in slide for title, slide in zip(expected, slides)):
                raise RuntimeError("PPTX 页序或确认标题不一致")
            if "<p:sp>" not in slides[0] or "data-icon" in slides[0]:
                raise RuntimeError("PPTX 未生成可编辑 DrawingML 图标和文字")
            if any("<p:pic>" in slide for slide in slides) or any(name.startswith("ppt/media/") for name in package.namelist()):
                raise RuntimeError("PPTX 意外包含图片资源")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
