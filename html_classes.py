import matplotlib.pyplot as plt
import csv

class Heading:
    def __init__(self, text, size):
        self.text = text
        self.size = size
    def print_to_html(self):
        return f"<h{self.size}>{self.text}</h{self.size}>\n"
    
class Paragraph:
    def __init__(self, text):
        self.text = text
    def print_to_html(self):
        return f"<p>{self.text}</p>\n"

class BarChart:
    def __init__(self, filename, axis_x, axis_y, title):
        self.filename = filename
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.title = title
    def print_to_html(self):
        return print_into_html(self.filename, self.axis_x, self.axis_y, self.title, 'B')

class ScatterPlot:
    def __init__(self, filename, axis_x, axis_y, title):
        self.filename = filename
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.title = title
    def print_to_html(self):
        return print_into_html(self.filename, self.axis_x, self.axis_y, self.title, 'S')

class LineChart:
    def __init__(self, filename, axis_x, axis_y, title):
        self.filename = filename
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.title = title
    def print_to_html(self):
        return print_into_html(self.filename, self.axis_x, self.axis_y, self.title, 'L')

def print_into_html(data = None, xlabel = None, ylabel = None, title = None, type = None):
    """
    Function which prints any object of any chart class.
    Argument 'type' is used to distinct classes:
    'B' -> BarChart
    'S' -> ScatterPlot
    'L' -> LineChart
    """
    labels, values = [], []
    #checking to which class our object belongs using 'type' parameter
    if type == 'B':
        # if type is 'B', we print BarPlot
        with open(data, newline="") as f:
            for lab, val in csv.reader(f):
                labels.append(lab)
                values.append(float(val))
            fig, ax = plt.subplots()
            ax.set_facecolor("white")

            ax.bar(list(range(len(labels))), values)

            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            ax.set_xticks(list(range(len(labels))))
            ax.set_xticklabels(labels)
            fig.tight_layout()
            fig.savefig("bar_chart.png", dpi=80)
            result = "<img src=\'bar_chart.png\' alt=\'Bar Plot\' width=\'500\' height=\'600\'>"
            f.close()
    # if our plot is not BarChart type, we start printing ScatterPlot or LineChart,
    # which share most of code needed to print them
    else:
        X, Y = [], []
        with open(data, newline="") as f:
            for x, y in csv.reader(f):
                X.append(float(x))
                Y.append(float(y))
            fig, ax = plt.subplots()
            ax.set_facecolor("white")
            if type == 'S':
                ax.scatter(X, Y)
            elif type == 'L':
                ax.plot(X, Y)

            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)

            fig.tight_layout()
        if type == 'S':
            fig.savefig("scatter_plot.png", dpi=80)
            f.close()
            result = "<img src=\'scatter_plot.png\' alt=\'Scatter Plot\' width=\'500\' height=\'600\'>"
        else:
            fig.savefig("line_chart.png", dpi=80)
            f.close()
            result = "<img src=\'line_chart.png\' alt=\'Line Chart\'>"
    return result
                