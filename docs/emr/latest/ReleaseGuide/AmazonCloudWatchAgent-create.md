# Create an EMR cluster that uses

Amazon CloudWatch agent

The procedures in this section describe the steps to create a cluster in Amazon EMR with
Amazon CloudWatch agent from the AWS Management Console and the AWS CLI.

###### Topics

- [Required IAM permissions for
  CloudWatch agent](#AmazonCloudWatchAgent-permissions "#AmazonCloudWatchAgent-permissions")
- [Required CloudWatch agent endpoint](#AmazonCloudWatchAgent-endpoints "#AmazonCloudWatchAgent-endpoints")
- [Create an EMR cluster](#AmazonCloudWatchAgent-create-cluster "#AmazonCloudWatchAgent-create-cluster")

## Required IAM permissions for

CloudWatch agent

The CloudWatch agent requires the AWS Identity and Access Management (IAM) `cloudwatch:PutMetricData`
permission in the Amazon EC2 instance profile for Amazon EMR. The Amazon EMR default role already
has this permission. You can create the default role from the AWS CLI with `aws
 emr create-default-roles`. For more information, see [Service role for cluster EC2 instances (EC2 instance profile)](../ManagementGuide/emr-iam-role-for-ec2.md "../ManagementGuide/emr-iam-role-for-ec2.md") in the
_Amazon EMR Management Guide_.

The following example IAM policy includes the
`cloudwatch:PutMetricData` permission:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowCLOUDWATCHPutmetricdata"
 }
 ]
}`

```

## Required CloudWatch agent endpoint

To publish metrics to CloudWatch for an EMR cluster in a private subnet, create a
CloudWatch agent endpoint and associate with the VPC that the private subnet is in.

For more information about the CloudWatch endpoints for each AWS Region, see [Amazon CloudWatch endpoints
and quotas](../../../general/latest/gr/cw_region.md "../../../general/latest/gr/cw_region.md") in the _AWS General Reference
Guide_.

## Create an EMR cluster

Once you have set up the required permissions and endpoint for use with the
CloudWatch agent, use the AWS Management Console or the AWS CLI to create a new cluster with the agent
installed.

Console

###### To create a cluster with Amazon CloudWatch agent from the console

1. Navigate to the Amazon EMR console.
2. Choose **Create cluster**.
3. Under **Name and applications**, choose an
   Amazon EMR release of 7.0.0 or higher.
4. Under **Application bundle**, select the
   bundle or apps that you want to install to your cluster, and
   include **CloudWatch agent** with your
   selections.
5. Proceed to create the cluster to serve your use case
   needs.

AWS CLI
In the AWS CLI, you can add Amazon CloudWatch agent to a cluster with the
`--applications` parameter for
`create-cluster`.

###### To create a cluster with Amazon CloudWatch agent from the AWS CLI

- When you create a cluster, use a command similar to the
  following to include the Amazon CloudWatch agent. Replace
  `myKey` with the
  name of your EC2 key pair.

```
aws emr create-cluster --name "`Spark cluster with CloudWatch agent`" \
--release-label emr-7.0.0 \
--applications Name=Spark Name=AmazonCloudWatchAgent \
--ec2-attributes KeyName=`myKey` --instance-type m7g.2xlarge \
--instance-count 3 --use-default-roles
```

For more details on how to use Amazon EMR with the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html").
