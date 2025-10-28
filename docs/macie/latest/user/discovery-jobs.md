# Running sensitive data discovery jobs

With Amazon Macie, you can create and run sensitive data discovery jobs to automate discovery, logging, and
reporting of sensitive data in Amazon Simple Storage Service (Amazon S3) general purpose buckets. A _sensitive data discovery job_ is a series of automated
processing and analysis tasks that Macie performs to detect and report sensitive data in
Amazon S3 objects. Each job provides detailed reports of the sensitive data that Macie finds and
the analysis that Macie performs. By creating and running jobs, you can build and maintain a
comprehensive view of the data that your organization stores in Amazon S3 and any security or
compliance risks for that data.

To help you meet and maintain compliance with your data security and privacy requirements,
Macie provides several options for scheduling and defining the scope of a job. You can
configure a job to run only once for on-demand analysis and assessment, or on a recurring
basis for periodic analysis, assessment, and monitoring. You also define the breadth and
depth of a job's analysis—specific S3 buckets that you select or buckets that match
specific criteria. You can optionally refine the scope of that analysis by choosing
additional options. The options include custom criteria that derive from properties of S3
objects, such as tags, prefixes, and when an object was last modified.

For each job, you also specify the types of sensitive data that you want Macie to detect and
report. You can configure a job to use [managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md") that Macie provides, [custom
data identifiers](custom-data-identifiers.md "custom-data-identifiers.md") that you define, or a combination of the two. By selecting
specific managed and custom data identifiers for a job, you can tailor the analysis to focus
on specific types of sensitive data. To fine tune the analysis, you can also configure a job
to use [allow lists](allow-lists.md "allow-lists.md"). Allow lists specify text and text
patterns that you want Macie to ignore, typically sensitive data exceptions for your
organization's particular scenarios or environment.

Each job produces records of the sensitive data that Macie finds and the analysis that Macie
performs—_sensitive data findings_ and _sensitive data discovery results_. A _sensitive data
finding_ is a detailed report of sensitive data that Macie found in an S3
object. A _sensitive data discovery result_ is a record that logs details about the
analysis of an S3 object. Macie creates a sensitive data discovery result for each object that you configure a job to
analyze. This includes objects that Macie doesn’t find sensitive data in, and therefore
don't produce sensitive data findings, and objects that Macie can't analyze due to errors or
issues. Each type of record adheres to a standardized schema, which can help you query,
monitor, and process the records to meet your security and compliance requirements.

###### Topics

- [Scope options for jobs](discovery-jobs-scope.md "discovery-jobs-scope.md")
- [Creating a job](discovery-jobs-create.md "discovery-jobs-create.md")
- [Reviewing job
  results](discovery-jobs-manage-results.md "discovery-jobs-manage-results.md")
- [Managing jobs](discovery-jobs-manage.md "discovery-jobs-manage.md")
- [Monitoring jobs with
  CloudWatch Logs](discovery-jobs-monitor-cw-logs.md "discovery-jobs-monitor-cw-logs.md")
- [Forecasting and monitoring job
  costs](discovery-jobs-costs.md "discovery-jobs-costs.md")
- [Managed data identifiers recommended
  for jobs](discovery-jobs-mdis-recommended.md "discovery-jobs-mdis-recommended.md")
