import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from os import makedirs
from more_itertools import chunked


def rebuild():

    with open("library/library.json", "r") as my_file:
        library_json = my_file.read()

    cards = json.loads(library_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    makedirs('pages')
    template = env.get_template('template.html')

    for i, cards_chunk in enumerate(chunked(cards, 20)):

        rendered_page = template.render(cards=cards_chunk, num=i)

        with open(f'pages/index{i}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
    print("Site rebuilt")


def main():

    rebuild()
    server = Server()
    server.watch('index.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
