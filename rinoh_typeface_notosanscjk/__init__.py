from os import path

from rinoh.font import Typeface
from rinoh.font.style import REGULAR, BOLD
from rinoh.font.opentype import OpenTypeFont


__all__ = ['typeface']


def otf(style):
    filename = 'notosanscjkjp-{}.otf'.format(style)
    return path.join(path.dirname(__file__), filename)


typeface = Typeface('Noto Sans CJK JP',
                    OpenTypeFont(otf('regular'), weight=REGULAR),
                    OpenTypeFont(otf('bold'), weight=BOLD))
