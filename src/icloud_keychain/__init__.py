from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("icloud-keychain")
except PackageNotFoundError:
    from typing import Final

    __version__: Final[str] = "dev"


__all__ = ["__version__"]
