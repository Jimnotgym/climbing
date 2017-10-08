from jinja2 import Environment, FileSystemLoader


def RenderWebsite(data):
    """ Renders template using current data
    """
    ENV = Environment(loader=FileSystemLoader('./templates'))
    file_name = 'index.html'
    template = ENV.get_template(file_name)
    html = template.render( kioskData=data)

        # Write output in the corresponding HTML file

    with open('./html/index.html', 'w',encoding='utf-8') as out_file:
        out_file.write(html)
    return
