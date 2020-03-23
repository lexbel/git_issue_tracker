from injector import singleton

from tracker.core.connectors.issue_handler import IssueHandler, JiraIssueHandler
from tracker.core.connectors.webhook_parser import BitBucketHookParser, WebHookDataParser


def configure(binder):
    binder.bind(WebHookDataParser, to=BitBucketHookParser, scope=singleton)
    binder.bind(IssueHandler, to=JiraIssueHandler, scope=singleton)

