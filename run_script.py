import project_part1 as pp1
import project_part2 as pp2
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Type an input file:')
    parser.add_argument('filename', type = str, help = 'Name of an input file:', default = "input.md")
    args = parser.parse_args()
    pp1.produce_html(pp2.html_to_list_of_objects(args.filename), args.filename)
    

