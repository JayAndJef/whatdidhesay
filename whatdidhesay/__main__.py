from pathlib import Path
from typing import Annotated
import typer

from PIL import Image, ImageDraw


def main(
    filepath: Path,
    bubble_height: Annotated[int, typer.Option(help="height of speech bubble in fraction of img height")] = 5,
    arrow_position: Annotated[str, typer.Option(help="alignment of arrow relative to screen")] = "right",
    arrow_width: Annotated[int, typer.Option(help="width of arrow as fraction of img width")] = 5,
    arrow_height: Annotated[int, typer.Option(help="height of arrow as fraction of img height")] = 3,
):
    """
    Generate a discord imagequote from a given image.
    """
    if not filepath.exists:
        raise typer.Exit(1)

    with Image.open(filepath).convert("RGBA") as base:
        img_width, img_height = base.size
        canvas = ImageDraw.Draw(base)

        canvas.ellipse(
            [(0, -(img_height / bubble_height)), (img_width, img_height / bubble_height)],
            fill=(255, 255, 255, 0),
        )
        
        if arrow_position == "left":
            arrow_start = (0, 0)
            arrow_end = (1 / arrow_width * img_width, 0)
            arrow_tip = (img_width / 3, 1 / arrow_height * img_height)
        elif arrow_position == "right":
            arrow_start = (img_width, 0)
            arrow_end = (img_width - (1 / arrow_width * img_width), 0)
            arrow_tip = (2 / 3 * img_width, 1 / arrow_height * img_height)
        
        canvas.polygon(
            [
                arrow_start,
                arrow_end,
                arrow_tip,
            ],
            fill=(255, 255, 255, 0),
        )

        base.save(filepath)


if __name__ == "__main__":
    typer.run(main)
