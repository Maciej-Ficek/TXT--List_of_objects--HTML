import html_classes


def html_to_list_of_objects(data):
    """
    That function takes as input a markdown file
    and returns a list of its classes: Headings, Paragraphs
    and Plots/Charts
    """
    with open(str(data), 'r') as Data:
        file = Data.read()
        file_objects = file.split("\n\n")
        list_of_objects = [distinct_object(object) for object in file_objects]

    return list_of_objects

def distinct_object(object):
    """
    That function checks if given object is heading, paragraph or chart

    :param object - object to check
    """
    # checking if object is a heading
    if object.startswith('#'):
        h = 1
        while True:
            if object.startswith('#'*(h+1)):
                h += 1
            else:
                actual_object = html_classes.Heading(object[h+1:], h)
                break
    # if object is not a heading, maybe it is a chart
    elif object.startswith("@BarPlot"):
        rest_of_object = object[9:].split(",")
        new_rest_of_object = [x.replace(' ', '') for x in rest_of_object]
        actual_object = html_classes.BarChart(
            new_rest_of_object[0], new_rest_of_object[1], new_rest_of_object[2], new_rest_of_object[3]
            )
    elif object.startswith("@ScatterPlot"):
        rest_of_object = object[13:].split(",")
        new_rest_of_object = [x.replace(' ', '') for x in rest_of_object]
        actual_object = html_classes.ScatterPlot(
        new_rest_of_object[0], new_rest_of_object[1], new_rest_of_object[2], new_rest_of_object[3]
        )
    elif object.startswith("@LineChart"):
        rest_of_object = object[11:].split(",")
        new_rest_of_object = [x.replace(' ', '') for x in rest_of_object]
        actual_object= html_classes.LineChart(
            new_rest_of_object[0], new_rest_of_object[1], new_rest_of_object[2], new_rest_of_object[3]
        )
    # we know that if object is nor heading neither chart, it is paragraph
    else:
        actual_object = html_classes.Paragraph(object)

    return actual_object
