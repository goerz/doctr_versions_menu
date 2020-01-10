"""Test for the doctr_versions_menu Sphinx extension."""
from pathlib import Path

import pytest
from sphinx.testing.path import path as sphinx_path


@pytest.fixture
def rootdir():
    """The directory in which to search for testroots.

    This is used by any test using the pytest.mark.sphinx decorator. For a
    `testroot` specified in the decorator, the rootdir will be
    "./test_extension/roots/test-<testroot>".

    The rootdir must contain a conf.py file. All of the rootdir's content will
    be copied to a temporary folder, and the Sphinx builder will be invoked
    inside that folder.
    """
    return sphinx_path(str(Path(__file__).with_suffix('') / 'roots'))


@pytest.mark.sphinx('html', testroot='basic')
def test_sphinx_build(app, status, warning):
    """Test building documentation with the doctr_versions_menu extension.

    This tests the default configuration in ./test_extension/roots/test-basic/
    """
    app.build()
    _build = Path(app.outdir)
    assert (_build / 'index.html').is_file()
    assert (_build / '_static' / 'doctr-versions-menu.js').is_file()
    assert (_build / '_static' / 'badge_only.css').is_file()
    html = (_build / 'index.html').read_text()
    script_inclusion = (
        '<script type="text/javascript" src="_static/doctr-versions-menu.js">'
        '</script>'
    )
    assert script_inclusion in html
