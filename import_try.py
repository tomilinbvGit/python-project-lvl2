from gendiff.scripts.generate_diff import generate_diff

def some_name(file1, file2):
    return generate_diff(file1, file2)

print(some_name('file1.json', 'file2.json'))
