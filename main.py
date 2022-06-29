import json

from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from os import makedirs
from more_itertools import chunked
from math import ceil


def rebuild():

    with open("library/library.json", "r") as my_file:
        library_json = my_file.read()

    cards = json.loads(library_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    makedirs('pages', exist_ok=True)
    template = env.get_template('template.html')
    chunk_size = 100

    pages_count = ceil(len(cards) / chunk_size)

    for i, cards_chunk in enumerate(chunked(cards, chunk_size)):

        rendered_page = template.render(cards=cards_chunk, num=i, pages_count=pages_count)
        with open(f'pages/index{i}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

    print("Site rebuilt")


def main():

    rebuild()
    server = Server()
    server.watch('index0.html', rebuild)
    server.serve(root='.')


if __name__ == '__main__':
    main()
