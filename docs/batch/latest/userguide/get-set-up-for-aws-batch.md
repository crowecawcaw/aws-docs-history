

# Setting up AWS Batch
<a name="get-set-up-for-aws-batch"></a>

If you've already signed up for Amazon Web Services (AWS) and are using Amazon Elastic Compute Cloud (Amazon EC2) or Amazon Elastic Container Service (Amazon ECS), you can soon use AWS Batch. The setup process for these services is similar. This is because AWS Batch uses Amazon ECS container instances in its compute environments. To use the AWS CLI with AWS Batch, you must use a version of the AWS CLI that supports the latest AWS Batch features. If you don't see support for an AWS Batch feature in the AWS CLI, upgrade to the latest version. For more information, see [http://aws.amazon.com/cli/](http://aws.amazon.com/cli/).

**Note**  
Because AWS Batch uses components of Amazon EC2, you use the Amazon EC2 console for many of these steps.

Complete the following tasks to get set up for AWS Batch.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Create IAM roles for your compute environments and container instances](create-an-iam-role.md)
+ [Create a key pair for your instances](create-a-key-pair.md)
+ [Create a VPC](create-a-vpc.md)
+ [Create a security group](create-a-base-security-group.md)
+ [Install the AWS CLI](install_aws_cli.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.