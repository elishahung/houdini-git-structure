import re
from pathlib import Path


class HIPStructureGenerator:
    def __init__(self, hip_path, target_path):
        self._hip_path = hip_path
        self._target_path = target_path
        self._temp_file = None

    def generate(self):
        with open(self._hip_path) as f:
            for line in f.readlines()[4:]:
                if line.startswith('Content-Disposition'):
                    result = re.findall(r'filename=\"(.+)\"', line)
                    if len(result) == 0:
                        raise ValueError('No boundary found.')
                    self._create_file(result[0])
                elif line.startswith('Content-Type'):
                    continue
                elif line.startswith('--'):
                    self._close_file()
                elif line == '':
                    continue
                else:
                    self._write_file(line)

    def _create_file(self, file_path):
        file_path = Path(self._target_path).joinpath(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        self._temp_file = file_path.open('w')

    def _write_file(self, content):
        self._temp_file.write(content)

    def _close_file(self):
        if self._temp_file is not None:
            self._temp_file.close()
