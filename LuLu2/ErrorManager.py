

class ErrorManager:
    _error_count_ = 0
    _path_: str = ""

    def print_error(self, line, col, text):
        self._error_count_ = self._error_count_ + 1
        print(self._path_+":"+str(line)+":"+str(col+1)+": error: "+str(text))

    @property
    def error_count(self) -> int:
        return self._error_count_

    @property
    def path(self):
        return self._path_

    @path.setter
    def path(self, path: str):
        self._path_ = path


errorManager = ErrorManager()