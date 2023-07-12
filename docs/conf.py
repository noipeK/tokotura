"""Configuration file for the Sphinx documentation builder."""
from __future__ import annotations

# -- Project information -----------------------------------------------------

project = "tokotura"

# -- General configuration ---------------------------------------------------

extensions = [
    # Sphinx own extensions
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    # Docs generation
    "autoapi.extension",
    "numpydoc",
    "myst_parser",
]

default_role = "py:obj"

# -- HTML output --------------------------------------------------------------

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/noipeK/tokotura",
    "source_branch": "master",
}
html_show_sourcelink = False


# -- AutoAPI options ----------------------------------------------------------

autoapi_root = "reference"
autoapi_dirs = ["../tokotura"]
autoapi_ignore = ["__main__.py"]

autoapi_options = ["members", "special-members"]

autoapi_add_toctree_entry = False
autoapi_keep_files = True

# -- AutoDoc options ----------------------------------------------------------

autodoc_typehints = "signature"
autodoc_class_signature = "separated"
autodoc_preserve_defaults = True
autoclass_content = "both"

# -- Intersphinx options ------------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
