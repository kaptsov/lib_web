import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server


def rebuild():

    with open("library/library.json", "r") as my_file:
        library_json = my_file.read()

    cards = json.loads(library_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(cards=cards)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("Site rebuilt")


def main():

    rebuild()
    server = Server()
    server.watch('index.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
