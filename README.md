# TXT--List_of_objects--HTML
That project takes as input special TXT File, divides its content into lsit of HTML objects and then creates HTML file from them.

Specification of files:
- bar.csv, line.csv, scatter.csv - files containing data to plot chartss
- input.md - input file. Rules of transforming it to list of html objects:
-- if line stats with 1-6 copies of '#', it is a heading
-- if line starts with @, it is a plot
- if ts is nor heading neither plot, it is a paragraph.

- html_classes.py - file containing python classes being implementations of html objects
- project_part1.py - file containing list of html objects to html file
- project_part2.py - file transforming input to list of objects from html_classes.py file
- run_script.py is a short file You use to run whole project.

Thank You for checking my weak project. 
