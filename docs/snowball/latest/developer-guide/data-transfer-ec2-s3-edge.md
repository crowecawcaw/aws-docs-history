AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Transferring data from EC2-compatible compute instances

to S3 buckets on the same Snowball Edge

You can transfer data between compute instances and Amazon S3 buckets on the same
Snowball Edge device. You do this by using the supported AWS CLI commands and the
appropriate endpoints. For example, assume that you want to move data from a directory
in my `sbe1.xlarge` instance into the Amazon S3 bucket, `amzn-s3-demo-bucket` on
the same device. Assume that you're using the Amazon S3 compatible storage on Snowball Edge endpoint `https://S3-object-API-endpoint:443`. You use the following procedure.

###### To transfer data between a compute instance and a bucket on the same Snowball

Edge

1. Use SSH to connect to your compute instance.
2. Download and install the AWS CLI. If your instance doesn't already have the
   AWS CLI, download and install it. For more information, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md").
3. Configure the AWS CLI on your compute instance to work with the Amazon S3 endpoint on
   the Snowball Edge. For more information, see [Getting and using local Amazon S3 credentials on Snowball Edge](using-adapter.md#adapter-credentials "using-adapter.md#adapter-credentials").
4. Use the supported Amazon S3 compatible storage on Snowball Edge commands to transfer data. For example:

```
aws s3 cp ~/june2018/results s3://amzn-s3-demo-bucket/june2018/results --recursive --endpoint https://S3-object-API-endpoint:443
```
