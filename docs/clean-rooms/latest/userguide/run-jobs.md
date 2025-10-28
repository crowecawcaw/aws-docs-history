# Running PySpark jobs

As the [member who can query](glossary.md#glossary-member-who-can-query "glossary.md#glossary-member-who-can-query"), you can run a
PySpark job on a configured table by using an approved PySpark [analysis
template](create-analysis-template.md "create-analysis-template.md").

**Prerequisites**

Before you run a PySpark job, you must have:

- An active membership in AWS Clean Rooms collaboration
- Access to at least one analysis template in the collaboration
- Access to at least one configured table in the collaboration
- Permissions to write the results of a PySpark job to a specified S3 bucket

For information about creating the required service role, see [Create a service role to write results of
a PySpark job](setting-up-roles.md#create-role-pyspark-job "setting-up-roles.md#create-role-pyspark-job").

- The member who is responsible to pay for compute costs has joined the collaboration as
  an active member
  For information about how to query data or view queries by calling the AWS Clean Rooms
  `StartProtectedJob` API operation directly or by using the AWS SDKs, see the
  [AWS Clean Rooms API
  Reference](../apireference/Welcome.md "../apireference/Welcome.md").

For information about job logging, see [Analysis logging in AWS Clean Rooms](query-logs.md "query-logs.md").

For information about receiving job results, see [Receiving and using analysis results](receive-query-results.md "receive-query-results.md").

The following topics explain how to run a PySpark job on a configured table in a
collaboration using the AWS Clean Rooms console.

###### Topics

- [Running a PySpark job on a configured
  table using a PySpark analysis template](run-jobs-with-analysis-template.md "run-jobs-with-analysis-template.md")
- [Viewing recent jobs](view-recent-jobs.md "view-recent-jobs.md")
- [Viewing job details](view-job-details.md "view-job-details.md")
