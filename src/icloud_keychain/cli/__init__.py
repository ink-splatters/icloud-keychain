"""CLI interface."""

import click

from .. import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=False)
@click.version_option(__version__, "--version", "-v")
def ikc() -> None:
    """
    iCloud Keychain Utility
    """
