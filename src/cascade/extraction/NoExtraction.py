from cascade.extraction.Extraction import Extraction
from typing import List, Dict
from cascade.utils.Utils import load_json_from_path
import os


class NoExtraction(Extraction):
    def __init__(self):
        super().__init__()
    """
    This is a basic extraction module
    """
    def extract(self, input_path, output_path) -> List[Dict[str, any]]:
        return []

