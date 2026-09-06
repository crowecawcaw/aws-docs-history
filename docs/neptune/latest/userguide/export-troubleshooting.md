

# Troubleshooting the Neptune export process
<a name="export-troubleshooting"></a>

The Amazon Neptune export process uses [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/) to provision the compute and storage resources necessary to export your Neptune data. When an export is running, you can use the link in the `logs` field to access the CloudWatch logs for the export job.

However, the CloudWatch logs for the AWS Batch job that performs the export are only available when the AWS Batch job is running. If Neptune export reports that an export is in a pending state, there won’t be a logs link through which you can access CloudWatch logs. If an export job remains in the `pending` state for more than a few minutes, there may be a problem provisioning the underlying AWS Batch resources.

When the export job leaves the pending state, you can check its status as follows:

**To check the status of a AWS Batch job**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. Select the neptune-export job queue.

1. Look for the job whose name matches the `jobName` returned by Neptune export when you started the export.

![Screenshot of the AWS Batch console when checking for status](http://docs.aws.amazon.com/neptune/latest/userguide/images/batch-console-checking-export.png)


If the job remains stuck in a `RUNNABLE` state, it may be because networking or security issues are preventing the container instance from joining the underlying Amazon Elastic Container Service (Amazon ECS) cluster. See the section about verifying network and security settings of the compute environment in [this support article](https://aws.amazon.com/premiumsupport/knowledge-center/batch-job-stuck-runnable-status/).

Another thing you can check is for problems with auto-scaling:

**To check the Amazon EC2 auto-scaling group for the AWS Batch compute environment**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Select the **Auto Scaling** group for the neptune-export compute environment.

1. Open the **Activity** tab and check the activity history for unsuccessful events.

![Screenshot of the Amazon EC2 console when checking for Auto Scaling problems](http://docs.aws.amazon.com/neptune/latest/userguide/images/ec2-console-checking-auto-scaling.png)


## Neptune Export common errors
<a name="export-troubleshooting-errors"></a>

### `org.eclipse.rdf4j.query.QueryEvaluationException: Tag mismatch!`
<a name="export-troubleshooting-errors-tag-mismatch"></a>

If an `export-rdf` job is regularly failing with a `Tag mismatch!` `QueryEvaluationException`, the Neptune instance is undersized for the large, long-running queries used by Neptune Export.

You can avoid getting this error by scaling up to a larger Neptune instance or by configuring the job to export from a large cloned cluster, like this:

```
'{
  "command": "export-rdf",
  "outputS3Path": "s3://{{(your Amazon S3 bucket)}}/neptune-export",
  "params": {
    "endpoint": "{{(your Neptune endpoint DNS name)}}",
    "cloneCluster": True,
    "cloneClusterInstanceType" : "r5.24xlarge"
  }
}'
```