from jinja2 import Environment, FileSystemLoader
import json
from climbing.crag import Crag


def renderWebsite(crag):
    """ Renders template using current data
    """
    ENV = Environment(loader=FileSystemLoader('./templates'))
    file_name = 'crag.html'
    template = ENV.get_template(file_name)
    nareas=len(crag.areas)
    html = template.render( crag=crag, nareas=nareas)

        # Write output in the corresponding HTML file

    with open('./html/grinshill.html', 'w',encoding='utf-8') as out_file:
        out_file.write(html)
    return

def renderHome():
    """ Renders template using current data
    """
    ENV = Environment(loader=FileSystemLoader('./templates'))
    file_name = 'index.html'
    template = ENV.get_template(file_name)
    html = template.render()

        # Write output in the corresponding HTML file

    with open('./html/index.html', 'w',encoding='utf-8') as out_file:
        out_file.write(html)
    return


def renderAbout():
    """ Renders template using current data
    """
    ENV = Environment(loader=FileSystemLoader('./templates'))
    file_name = 'about.html'
    template = ENV.get_template(file_name)
    html = template.render()

        # Write output in the corresponding HTML file

    with open('./html/about.html', 'w',encoding='utf-8') as out_file:
        out_file.write(html)
    return


def readJSON(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

filename='crags/grinshill/crag.json'

cragdata=readJSON(filename)

crag = Crag(name=cragdata["name"],path='grinshill',description=cragdata["description"],access=cragdata["access"],\
    mapsrc=cragdata["mapsrc"],maphref=cragdata["maphref"],osgrid=cragdata["osgrid"])

renderWebsite(crag)
renderHome()
renderAbout()
