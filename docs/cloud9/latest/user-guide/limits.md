

 AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)

# Service quotas for AWS Cloud9
<a name="limits"></a>

The following tables list quotas in AWS Cloud9 and related AWS services.
+  [AWS Cloud9 service quotas](#limits-core) 
+  [Related AWS Service quotas](#limits-related) 

## AWS Cloud9 quotas
<a name="limits-core"></a>

The following table provides the default quotas for AWS Cloud9 for an AWS account. Unless otherwise noted, each limit is Region-specific. You can request an increase using the AWS Management Console or AWS CLI. To request a quota increase, see [ Requesting a quota increase ](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

These increases are not granted immediately, so it might take a couple of days for your increase to become effective.



| Resource | Default Limit | Adjustable | 
| --- | --- | --- | 
| Maximum number of AWS Cloud9 EC2 development environments |  +  100 per user <br />+  200 per account   | Yes | 
| Maximum number of SSH environments |  +  100 per user <br />+  200 per account   | Yes | 
| Maximum number of members in an environment | The default maximum number of members is equal to the memory of the instance for that environment divided by 60 MB, with results rounded down. For example, an instance with 1 GiB of memory can have a maximum of 17 members (which is 1 GiB divided by 60 MB, rounded down).<br />If AWS Cloud9 cannot determine the memory of an instance, it defaults to a maximum of 8 users for each environment associated with that instance.<br />The absolute maximum number of members for an environment is 25. | No1 | 
| Maximum editable file size | 8 MB | No | 

1 You can [move an environment](move-environment.md#move-environment-move) to attempt to increase the default maximum number of members. However, the absolute maximum number of members for an environment is still 25.

### AWS Cloud9 IDE Download quotas
<a name="limits-related-ide"></a>

When you download files from the AWS Cloud9 IDE to the local file system the speed of transfer will be limited to a speed of 0.1 megabyte/second. To increase the speed of transferring files, use the CLI in AWS Cloud9 IDE to upload files to Amazon S3, and then use Amazon S3 to download the files from there.

## Related AWS Service quotas
<a name="limits-related"></a>



|  |  | 
| --- |--- |
| Maximum number of Amazon Elastic Block Store (Amazon EBS) volumes | 5,000<br />For more information, see [Amazon Elastic Block Store endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ebs-service.html) in the *Amazon Web Services General Reference*. | 
| Maximum number of CloudFormation stacks | 200<br />For more information, see [Understand CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*. | 
| Amazon EC2 quotas | See [Amazon EC2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html#limits_ec2) in the *Amazon Web Services General Reference*. | 