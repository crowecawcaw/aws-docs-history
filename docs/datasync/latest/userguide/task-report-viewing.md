# Viewing your DataSync task reports

DataSync creates task reports for every task execution. When your execution completes,
you can find the related task reports in your S3 bucket. Task reports are organized
under prefixes that include the IDs of your tasks and their executions.

To help locate task reports in your S3 bucket, use these examples:

- **Summary only task report** –
  ``reports-prefix`/Summary-Reports/`task-id-folder`/`task-execution-id-folder``
- **Standard task report** –
  ``reports-prefix`/Detailed-Reports/`task-id-folder`/`task-execution-id-folder``
  Because task reports are in JSON format, you have several options for viewing your
  reports:

- View a report by using [Amazon S3
  Select](../../../AmazonS3/latest/userguide/selecting-content-from-objects.md "../../../AmazonS3/latest/userguide/selecting-content-from-objects.md").
- Visualize reports by using AWS services such as AWS Glue, Amazon Athena, and
  Amazon Quick Suite. For more information about visualizing your task reports, see the
  [AWS Storage Blog](https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/").
