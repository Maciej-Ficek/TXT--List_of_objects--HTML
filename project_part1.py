def produce_html(list_of_objects, filename):
    """
    That function takes as input list of html objects (Headings,
    Paragraphs and Charts) and creates html file from them.

    :param list_of_objects - list of headings, paragraphs and charts
    :param filename - name of html file which will be our final result
    """
    with open(filename + ".html", "w") as result:
        result.write(
            """<!doctype html>
    <html>

    <head>
    <title>Output HTML</title>
    </head>

    <body>
        <div class="markdown-body">
            """
                    )
        # we need to embed objects into html file
        for element in list_of_objects:
            result.write(element.print_to_html())

        result.write(
            """</div>
            </body>
            </html>
            """
        )
