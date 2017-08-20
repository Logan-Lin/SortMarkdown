import sys


def direct_sort(markdown_strings, output_filename):
    output_file = open(output_filename + ".md", "w")
    lines = markdown_strings.split('\n')
    header_indexes = find_all(lines, '###')
    headers = []
    output_file.write(lines[0] + '\n' + lines[1])
    for i in range(len(header_indexes)):
        headers.append(lines[header_indexes[i]][4:])
    sorted_headers = sorted(headers)
    for header in sorted_headers:
        index = headers.index(header)
        start = header_indexes[index]
        if index == len(header_indexes) - 1:
            end = len(lines)
        else:
            end = header_indexes[index + 1]
        for i in range(start, end):
            output_file.write('\n' + lines[i])
    output_file.close()


def file_sort(input_filename, output_filename):
    file = open(input_filename + ".md", "r")
    if file is None:
        return False
    strings = ''
    line = file.readline()
    while line != '':
        strings += line
        line = file.readline()
    direct_sort(strings, output_filename)
    file.close()
    return True


def find_all(string_array, sub_string):
    indexes = []
    for i in range(len(string_array)):
        if string_array[i].find(sub_string) != -1:
            indexes.append(i)
    return indexes


output_name = 'output'
input_name = sys.argv[1]
if len(sys.argv) > 2:
    output_name = sys.argv[2]
result = file_sort(input_name, output_name)
if result is True:
    print("Sort success! Sorted markdown file is saved to " + output_name + ".md")
else:
    print("Sort failed.")
