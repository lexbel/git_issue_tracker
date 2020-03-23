import logging
import re
from abc import abstractmethod

from tracker.core.connectors.issue_handler import IssueHandler
from tracker.core.connectors.webhook_parser import RefChangeRequest

logger = logging.getLogger("issue:handler")


class JiraIssueHandler(IssueHandler):

    def handle(self, issues, request: RefChangeRequest):
        if len(issues) > 0:
            self.process(issues, request)
        else:
            logger.info("issues not found")

    @abstractmethod
    def process(self, issues, request: RefChangeRequest):
        pass
