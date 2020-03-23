import os


GIT_USER_PASS = {
    "username": os.environ["GIT_USERNAME"],
    "token": os.environ["GIT_TOKEN"]
}

# Git properties
TRACKED_BRANCH_REGEXP = os.getenv("TRACKED_BRANCH_REGEXP", "(release/.*|hotfix/.*|support/.*|develop|dev)")
MERGE_PATTERN_SEARCH_TO_SKIP = os.getenv("MERGE_PATTERN_SEARCH_TO_SKIP", "Merge.*((release\/|support\/|hotfix\/)[0-9]{1}\.[0-9]{2,3}\.x|(tag .*)).*(develop|dev).*")
WHITE_LISTED_REPOS = os.getenv("WHITE_LISTED_REPOS", "*".split(','))

RELEASE_NUMBER_BRANCH_PATTERN = os.getenv("RELEASE_NUMBER_BRANCH_PATTERN", ".*(1\\.[0-9]{2,3}).*")

# Issue tracker properties
ISSUE_TRACKER_PATTERN = os.getenv("ISSUE_TRACKER_PATTERN")
ISSUE_TRACKER_PROJECT_NAME = os.getenv("ISSUE_TRACKER_PROJECT_NAME")




