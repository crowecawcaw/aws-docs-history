

# Add an Amazon S3 bucket
<a name="S3-buckets-add"></a>

**To add an S3 bucket to your RES environment:**

1. Choose **Add bucket**.

1. Enter the bucket details such as bucket name, ARN, and mount point.
**Important**  
The S3 bucket must be in the same AWS Region as the RES environment. Cross-region S3 bucket mounting is not supported.
The bucket ARN, mount point, and mode provided cannot be changed after creation. 
The bucket ARN can contain a prefix which will isolate the onboarded S3 bucket to that prefix.

1. Select a mode in which to onboard your bucket.
**Important**  
See [Data Isolation](S3-buckets-data-isolation.md) for more information related to data isolation with specific modes.

1. Under **Advanced Options**, you may provide an IAM role ARN to mount the buckets for cross account access. Follow the steps in [Cross account bucket access](S3-buckets-cross-account-access.md) to create the required IAM role for cross account access.

1. (Optional) Associate the bucket with projects, which can be changed later. However, an S3 bucket cannot be mounted to a project's existing VDI sessions. Only sessions launched after the project has been associated with the bucket will mount the bucket.

1. Choose **Submit**.  
![Add bucket page showing available bucket setup fields and submit button](http://docs.aws.amazon.com/res/latest/ug/images/docs-add-bucket.png)