AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Before You Begin

Be sure you've completed the following steps.

- Complete the tasks in [Setting up for AWS Data Pipeline](dp-get-setup.md "dp-get-setup.md").
- (Optional) Set up a VPC for the instance and a security group for the VPC.
- Create an Amazon S3 bucket as a data source.

For more information, see [Create a
Bucket](../../../AmazonS3/latest/gsg/CreatingABucket.md "../../../AmazonS3/latest/gsg/CreatingABucket.md") in the _Amazon Simple Storage Service User Guide_.

- Upload your data to your Amazon S3 bucket.

For more information, see [Add an
Object to a Bucket](../../../AmazonS3/latest/gsg/PuttingAnObjectInABucket.md "../../../AmazonS3/latest/gsg/PuttingAnObjectInABucket.md") in the
_Amazon Simple Storage Service User Guide_.

- Create another Amazon S3 bucket as a data target
- Create a topic for sending email notification and make a note of the
  topic Amazon Resource Name (ARN). For more information, see [Create a Topic](../../../sns/latest/gsg/CreateTopic.md "../../../sns/latest/gsg/CreateTopic.md") in
  the _Amazon Simple Notification Service Getting Started Guide_.
- (Optional) This tutorial uses the default IAM role policies created by
  AWS Data Pipeline. If you would rather create and configure your own IAM role policy and
  trust relationships, follow the instructions described in [IAM Roles for AWS Data Pipeline](dp-iam-roles.md "dp-iam-roles.md").
