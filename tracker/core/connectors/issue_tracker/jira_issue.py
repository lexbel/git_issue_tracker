import logging
import re

from tracker.core import RefChangeRequest
from tracker.core.connectors.issue_handler import IssueHandler
from tracker.env import RELEASE_NUMBER_BRANCH_PATTERN

logger = logging.getLogger("issue:handler")


class JiraIssueHandler(IssueHandler):

    def handle(self, issues, request: RefChangeRequest):
        search = re.search(RELEASE_NUMBER_BRANCH_PATTERN, request.ref_id)

        if len(issues) > 0:
            # do anything you want with found issues
            pass
        else:
            logger.info("issues not found")

