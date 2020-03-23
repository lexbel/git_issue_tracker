from abc import abstractmethod, ABC
from tracker.core import RefChangeRequest


class IssueHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def handle(self, issues, request: RefChangeRequest):
        pass


