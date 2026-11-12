import os
import sys

sys.path.insert(
    0,
    os.path.abspath('../../src')
)

project = 'Demo project'
copyright = '2026, dsadsdsa'
author = 'dsadsdsa'


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]
templates_path = ["_templates"]
exclude_patterns = []
autosummary_generate = True
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_show_sourcelink = False
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "titles_only": True,
}
