# Managing sensitive data discovery jobs

To help you manage your sensitive data discovery jobs, Amazon Macie maintains a complete
inventory of your jobs in each AWS Region. With this inventory, you can manage your jobs
as a single collection, and access configuration settings, processing statistics, and the
status of individual jobs.

For example, you can identify all the jobs that you configured to run on a recurring basis
for periodic analysis, assessment, and monitoring. You can also review a breakdown of the
configuration settings for a job. This includes settings that define the scope of the
analysis. It also includes settings that specify the types of sensitive data that you want
Macie to detect and report when the job runs. If you use the Amazon Macie console to manage
your jobs, each job's details also provide direct access to [sensitive data findings and other results](discovery-jobs-manage-results.md "discovery-jobs-manage-results.md")
that the job produced.

In addition to these tasks, you can create custom variations of individual jobs. You can
copy an existing job, adjust the settings for the copy, and then save the copy as a new job.
This can be helpful for cases where you want to analyze different sets of data in the same
way, or the same set of data in different ways. It can also be helpful if you want to adjust
the configuration settings for an existing job—cancel the existing job, copy it, and
then adjust and save the copy as a new job.

###### Topics

- [Reviewing your job
  inventory](discovery-jobs-manage-view.md "discovery-jobs-manage-view.md")
- [Reviewing configuration settings for
  a job](discovery-jobs-manage-settings.md "discovery-jobs-manage-settings.md")
- [Checking the status of a
  job](discovery-jobs-status-check.md "discovery-jobs-status-check.md")
- [Changing the status of a
  job](discovery-jobs-status-change.md "discovery-jobs-status-change.md")
- [Copying a job](discovery-jobs-manage-copy.md "discovery-jobs-manage-copy.md")
