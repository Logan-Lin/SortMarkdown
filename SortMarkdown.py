import sys


def direct_sort(markdown_strings, output_filename):
    output_file = open(output_filename + ".md", "w")
    lines = markdown_strings.split('\n')
    header_indexes = find_all(lines, '###')
    output_file.write(lines[0] + '\n' + lines[1])
    i = 0
    while i < len(header_indexes):



def file_sort(input_filename, output_filename):
    file = open(input_filename + ".md", "r")
    strings = ''
    line = file.readline()
    while line != '':
        strings += line
        line = file.readline()
    direct_sort(strings, output_filename)


def find_all(string_array, sub_string):
    result = []
    i = 0
    while i < len(string_array):
        if string_array[i].find(sub_string) != -1:
            result.append(i)
        i = i + 1
    return result


file_sort("test_file", "output")
