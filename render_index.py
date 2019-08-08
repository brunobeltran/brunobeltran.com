"""A simple script to

    1) compile my blog posts from markdown to html
    2) gather metadata on my coding projects
    3) gather metadata on my scientific projects
    4) insert (1-3) into a simple jinja2 template
"""
import markdown2
from jinja2 import FileSystemLoader, Environment, select_autoescape

from pathlib import Path
from dataclasses import dataclass

blog_posts = [Path('./content/posts') / Path(p) for p in
                    # ['physics-vs-biology.md',
                    #  'defining-science.md',
                     ['weinstein-thiel.md']]
blog_posts = [markdown2.markdown_path(f) for f in
              blog_posts]

page_summary = {f.stem: f.read_text() for f in
                Path('./content/summaries').iterdir()}

@dataclass
class Project:
    title: str
    image: str
    url: str = None
    description: str = None
    full_size_image: str = None

    @classmethod
    def from_file(cls, file_name):
        p = cls(*Path(file_name).read_text().split('\n\n'))
        if p.description:
            p.description = markdown2.markdown(p.description)
        return p

science_projects = [Path('./content/science') / Path(p) for p in
                    ['nucleosome-heterogeneity.txt',
                     'meier-kaplan.txt',
                     'parabs-transport.txt',
                     'bacterial-adder.txt']]
science_projects = [Project.from_file(f) for f in
                    science_projects]
                    # Path('./content/science').iterdir()]

coding_projects = [Path('./content/coding') / Path(p) for p in
                   ['python_tooling_example.txt',
                    'multi_locus_analysis.txt',
                    'nuc_chain.txt']]
coding_projects = [Project.from_file(f) for f in
                   coding_projects]
                    # Path('./content/coding').iterdir()]


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('./content/templates'),
                      autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('index.jinja2')
    with open('index.html', 'w') as f:
        f.write(template.render(page_summary=page_summary,
                               coding_projects=coding_projects,
                               science_projects=science_projects,
                               blog_posts=blog_posts))

