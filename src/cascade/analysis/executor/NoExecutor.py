import json
import subprocess

from cascade.analysis.executor.AnalysisExecutor import AnalysisExecutor, succeeded, failed, errored
from cascade.utils.DockerizedWrapper import DockerizedWrapper

import os
import tempfile
import shutil


class NoExecutor(AnalysisExecutor):
    def __init__(self, debug=False, builder=None):
        super().__init__()
        self.debug = debug
        self.builder = builder

    def execute(self, code: str, tests: str, context: dict) -> (succeeded, failed, errored):
        result = ([], [], [])
        return result

    def set_up(self, data):
        pass

    def tear_down(self, data):
        pass

