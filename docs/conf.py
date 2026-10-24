"""Sphinx configuration."""

project = "unc"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_markdown_builder",
]

source_suffix = [".rst", ".md"]

html_theme = "furo"

exclude_patterns = ["_build"]
