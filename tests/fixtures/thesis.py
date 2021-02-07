import pytest
import pyexlatex as pl
from pyexlatex.models.section.sections import Chapter

from plufthesis.thesis import UFThesis

EXAMPLE_BODY = [
    Chapter(
        [
            'Some content',
            pl.UnorderedList(['a', 'b', 'c']),
        ],
        title='First'
    ),
    Chapter(
        [
            'Chapter content',
            pl.Section(
                [
                    'Section content',
                    pl.SubSection(
                        [
                            'Subsection content',
                            pl.SubSubSection(
                                [
                                    'Subsubsubsection content'
                                ],
                                title='First sub sub'
                            )
                        ],
                        title='First sub'
                    )
                ],
                title='First section'
            )
        ],
        title='Second'
    )
]
TITLE = 'Insert Title Here'
AUTHOR = 'Nick DeRobertis'
MAJOR = 'Insert Major Here'
CHAIR = 'Insert Chair Here'
ABSTRACT = "Insert abstract here"
BIBLIOGRAPHY = pl.Bibliography([pl.BibTexArticle('person', 'Last, First', 'An article title', 'Journal of Journals', '2021', '10', '1', '255-256')])

@pytest.fixture(scope='session')
def thesis():
    return UFThesis(
        EXAMPLE_BODY,
        TITLE,
        AUTHOR,
        MAJOR,
        CHAIR,
        ABSTRACT,
        BIBLIOGRAPHY
    )