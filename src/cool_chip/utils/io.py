from os import path
from pathlib import Path


def curr_file_path() -> Path:
    """Get cuurent file path."""
    return Path(__file__).absolute()


def out_folder_path() -> Path:
    """Get output folder path."""
    return curr_file_path().parents[3].joinpath("out").absolute()


def out_geom_path() -> Path:
    """Get output geometry folder path."""
    return path.abspath(out_folder_path().joinpath("geometry").absolute())
