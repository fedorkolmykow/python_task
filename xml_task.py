import xml.etree.ElementTree as et
import sys


def get_depth_rec(el: et.Element, depth: int) -> int:
    if len(el) or el.attrib:
        dep = depth + 1
    for child in el:
        if isinstance(child, et.Element) and child.attrib:
            d = get_depth_rec(child, depth + 1)
            if d > dep:
                dep = d
    return dep


def get_depth(path):
    root = et.parse(path).getroot()
    return get_depth_rec(root, 0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(get_depth(sys.argv[1]))
    else:
        print("Pass the path to *.xml as the first parameter")