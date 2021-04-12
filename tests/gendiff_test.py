from gendiff.scripts.generate_diff import generate_diff


file_open = open('tests/fixtures/test.txt', 'r')
result = file_open.read()


def test_diff():
    assert result == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
