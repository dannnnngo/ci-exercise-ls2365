"""Nox sessions."""

import nox

nox.options.default_venv_backend = "uv|virtualenv"

PYPROJECT = nox.project.load_toml()


@nox.session
def tests(session: nox.Session) -> None:
    """Run the unit tests."""
    test_deps = nox.project.dependency_groups(PYPROJECT, "test")
    session.install(".", *test_deps)
    session.run("pytest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """Build the documentation."""
    docs_deps = nox.project.dependency_groups(PYPROJECT, "docs")
    session.install(".", *docs_deps)
    session.run("sphinx-build", "-M", "html", "docs", "docs/_build")
