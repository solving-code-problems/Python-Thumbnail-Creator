from PIL import Image, ImageFont, ImageDraw

import argparse


def main(text, pos, size, output, input):
    img = Image.open(input)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("cool-font.ttf", size=size)
    draw.text(text=text, xy=pos, font=font, fill=(0, 0, 0))
    img.save(output, "PNG")


parser = argparse.ArgumentParser()
parser.add_argument('--text', required=True)
parser.add_argument('--pos', default="150,150")
parser.add_argument('--size', type=int, default=25)
parser.add_argument('--out', default="result.png")
parser.add_argument('--input', required=True)

args = parser.parse_args()
x, y = args.pos.split(",")
main(args.text, (int(x), int(y)), args.size, args.out, args.input)
