

# Running jobs and reading results

This section describes how to process documents with Amazon Textract Insights and find the results. You start a job with `StartDocumentInsights`, which runs asynchronously, and then poll `GetDocumentInsights` until the job succeeds or fails.

The start-and-poll workflow comes with examples in the AWS CLI and the AWS SDK for Python (Boto) (Boto3), along with job statuses, idempotent retries, and error fields. A job organizes its output in Amazon S3, starting from the `job_metadata.json` file that lists the location of every result. To start a job, you need a project or inline blueprints.