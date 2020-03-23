# Git issue tracker

This app track changes in git by receiving web hook from BitBucket and synchronize found issues
with Jira in terms of fix version. So it gives 100% guarantee that fix version is set correctly.

BitBucket or Jira could be changed to any other Git or Bug tracker system (should be written by your own). 


## Workflow

User pushes changes into `Git`, in it's turn send web hook to 
 
## Environment variables used

- `JIRA_USERNAME` :  Jira account id
- `JIRA_USER_PASSWORD` :  Jira account password
- `LOG_CFG` : Path to external logging configuration file, yaml format, if you want to override


