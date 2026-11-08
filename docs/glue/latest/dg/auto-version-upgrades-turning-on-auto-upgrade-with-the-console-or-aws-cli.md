

# Turning on auto upgrade with the console or AWS CLI
<a name="auto-version-upgrades-turning-on-auto-upgrade-with-the-console-or-aws-cli"></a>

This section describes how to turn on auto upgrade for a new job or an existing job. The `GlueVersion` value is case sensitive. Use lowercase `auto`.

## To create a new job with auto upgrade (console)
<a name="auto-version-upgrades-to-create-a-new-job-with-auto-upgrade-console"></a>

1. Open the [AWS Glue console](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **ETL jobs**.

1. Create a Spark job, and then choose the **Job details** tab.

1. For **Glue version**, choose **Auto**.

1. For **Number of retries**, enter 1 or higher.

1. Choose **Save**.

## To create a new job with auto upgrade (AWS CLI)
<a name="auto-version-upgrades-to-create-a-new-job-with-auto-upgrade-aws-cli"></a>

The following command creates a job with auto upgrade turned on.

```
aws glue create-job \
  --name my-etl-job \
  --role arn:aws:iam::111122223333:role/MyGlueJobRole \
  --command '{"Name": "glueetl", "ScriptLocation": "s3://amzn-s3-demo-bucket/scripts/my-etl-job.py"}' \
  --glue-version auto \
  --max-retries 1
```

## To turn on auto upgrade for an existing job (console)
<a name="auto-version-upgrades-to-turn-on-auto-upgrade-for-an-existing-job-console"></a>

1. Open the [AWS Glue console](https://console.aws.amazon.com/glue/).

1. In the navigation pane, choose **ETL jobs**.

1. Choose the job, and then choose the **Job details** tab.

1. For **Glue version**, choose **Auto**.

1. For **Number of retries**, enter 1 or higher.

1. Choose **Save**.

## To turn on auto upgrade for an existing job (AWS CLI)
<a name="auto-version-upgrades-to-turn-on-auto-upgrade-for-an-existing-job-aws-cli"></a>

Set `GlueVersion` to `auto` and `MaxRetries` to 1 or higher. `update-job` replaces the whole job definition, so include every setting that you want to keep.

```
aws glue update-job \
  --job-name my-etl-job \
  --job-update '{
    "Role": "arn:aws:iam::111122223333:role/MyGlueJobRole",
    "Command": {"Name": "glueetl", "ScriptLocation": "s3://amzn-s3-demo-bucket/scripts/my-etl-job.py"},
    "GlueVersion": "auto",
    "MaxRetries": 1
  }'
```

If the job doesn't meet the prerequisites, the command fails with `InvalidInputException` and a message that names the problem.

## Jobs that aren't safe to retry
<a name="auto-version-upgrades-jobs-that-arent-safe-to-retry"></a>

Some jobs append to their targets and have no way to clean up a failed run. For these jobs, consider following best practices for safe retries, such as writing output to separate partitions. For more information, see [From failed jobs to reliable pipelines](https://builder.aws.com/content/3IgXAgTx0mCVh5wyniqyCnK0USS/from-failed-jobs-to-reliable-pipelines-a-practical-guide-to-aws-data-engineering) on the AWS Builder Center website.

Alternatively, consider Upgrade with AI. For more information, see [Generative AI upgrades for Apache Spark in AWS Glue](upgrade-analysis.md).

## Cleaning up
<a name="auto-version-upgrades-cleaning-up"></a>

To stop using auto upgrade on a job, set `GlueVersion` to a specific version. For more information, see [Disabling auto upgrade](auto-version-upgrades-managing-auto-upgrade.md#auto-version-upgrades-disabling-auto-upgrade).

To remove a job that you created only to try auto upgrade, delete the job. For example, run the following command.

```
aws glue delete-job --job-name my-etl-job
```