AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Service quotas for AWS Cloud9

The following tables list quotas in AWS Cloud9 and related AWS services.

- [AWS Cloud9 service quotas](#limits-core "#limits-core")
- [Related AWS Service quotas](#limits-related "#limits-related")

## AWS Cloud9 quotas

The following table provides the default quotas for AWS Cloud9 for an AWS account. Unless
otherwise noted, each limit is Region-specific. You can request an increase using the AWS
Management Console or AWS CLI. To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User
Guide_.

These increases are not granted immediately, so it might take a couple of days for your increase to become effective.

| Resource                                                  | Default Limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Adjustable |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Maximum number of AWS Cloud9 EC2 development environments | • 100 per user<br>• 200 per account                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes        |
| Maximum number of SSH environments                        | • 100 per user<br>• 200 per account                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes        |
| Maximum number of members in an environment               | The default maximum number of members is equal to the memory of the<br>instance for that environment divided by 60 MB, with results rounded down. For<br>example, an instance with 1 GiB of memory can have a maximum of 17 members<br>(which is 1 GiB divided by 60 MB, rounded down).<br>If AWS Cloud9 cannot determine the memory of an instance, it defaults to a<br>maximum of 8 users for each environment associated with that instance.<br>The absolute maximum number of members for an environment is 25. | No1        |
| Maximum editable file size                                | 8 MB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No         |

1 You can [move an
environment](move-environment.md#move-environment-move "move-environment.md#move-environment-move") to attempt to increase the default maximum number of members. However, the
absolute maximum number of members for an environment is still 25.

### AWS Cloud9 IDE Download quotas

When you download files from the AWS Cloud9 IDE to the local file system the speed of
transfer will be limited to a speed of 0.1 megabyte/second. To increase the speed of transferring files, use the CLI in AWS Cloud9 IDE to
upload files to Amazon S3, and then use Amazon S3 to download the files from there.

## Related AWS Service quotas

|                                                                   |                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum number of Amazon Elastic Block Store (Amazon EBS) volumes | 5,000<br>For more information, see [Amazon Elastic Block Store<br>endpoints and quotas](../../../general/latest/gr/ebs-service.md "../../../general/latest/gr/ebs-service.md") in the<br>_Amazon Web Services General Reference_.                           |
| Maximum number of CloudFormation stacks                           | 200<br>For more information, see [Understand CloudFormation quotas](../../../AWSCloudFormation/latest/UserGuide/cloudformation-limits.md "../../../AWSCloudFormation/latest/UserGuide/cloudformation-limits.md") in the<br>_AWS CloudFormation User Guide_. |
| Amazon EC2 quotas                                                 | See [Amazon EC2<br>endpoints and quotas](../../../general/latest/gr/ec2-service.md#limits_ec2 "../../../general/latest/gr/ec2-service.md#limits_ec2") in the<br>_Amazon Web Services General Reference_.                                                    |
