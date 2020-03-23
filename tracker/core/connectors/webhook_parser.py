from abc import abstractmethod, ABC

from tracker.core.fix_version_detection import RefChangeRequest


class WebHookDataParser(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def parse(self, request) -> RefChangeRequest:
        pass


class ParseError(Exception):
    pass