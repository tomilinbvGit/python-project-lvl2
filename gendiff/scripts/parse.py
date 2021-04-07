from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.generate_diff import gendiff


def main():
    file1, file2 = gendiff()
    return generate_diff(file1, file2)


print(main())
