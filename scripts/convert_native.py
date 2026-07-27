#!/usr/bin/env python3
"""把若干 SVG 转成「原生可编辑」pptx(DrawingML 形状/文本,无需 PowerPoint 的 Convert to Shape)。

用法:  python convert_native.py <out.pptx> <slide1.svg> <slide2.svg> ...
基于 ppt-master v2.9 的 svg_to_pptx 包,use_native_shapes=True。需 Python 3.10+ 与 python-pptx。
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg_to_pptx import create_pptx_with_native_svg  # noqa: E402


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: convert_native.py <out.pptx> <svg...>", file=sys.stderr)
        return 2
    out = Path(sys.argv[1])
    svgs = [Path(p) for p in sys.argv[2:]]
    create_pptx_with_native_svg(
        svgs,
        out,
        use_native_shapes=True,   # 关键:出原生形状而非嵌图
        use_compat_mode=False,    # 不要 PNG 双格式
        enable_notes=False,
        transition="fade",
        verbose=False,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
