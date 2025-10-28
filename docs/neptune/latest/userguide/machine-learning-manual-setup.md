# Setting up Neptune ML without using the quick-start AWS CloudFormation template

This guide provides step-by-step instructions for setting up Amazon Neptune ML without using the AWS AWS CloudFormation quick-start
template. It assumes you already have a working Neptune DB cluster and covers the necessary setup, including installing
the Neptune-Export service, creating custom IAM roles, and configuring your DB cluster to enable Neptune ML.
The guide also explains how to create two SageMaker AI endpoints in your Neptune VPC to give the Neptune engine access to
the necessary SageMaker AI management APIs. By following these instructions, you can set up Neptune ML on your existing Neptune
infrastructure without relying on the AWS CloudFormation template.

## Start with a working Neptune DB cluster

If you don't use the AWS CloudFormation quick-start template to set up Neptune ML, you will
need an existing Neptune DB cluster to work with. If you want, you can use one you
already have, or clone one that you are already using, or you can create a new one
(see [Create Neptune cluster](get-started-create-cluster.md "get-started-create-cluster.md")).

## Install the Neptune-Export service

If you haven't already done so, install the Neptune-Export service, as explained
in [Using the Neptune-Export service to export Neptune data](export-service.md "export-service.md").

Add an inbound rule to the `NeptuneExportSecurityGroup` security group
that the install creates, with the following settings:

- _Type_: `Custom TCP`
- _Protocol_: `TCP`
- _Port range_: `80 - 443`
- _Source_: `(Neptune DB cluster security group ID)`

## Create a custom NeptuneLoadFromS3 IAM role

If you have not already done so, create a custom `NeptuneLoadFromS3` IAM
role, as explained in [Creating an IAM role to access Amazon S3](bulk-load-tutorial-IAM-CreateRole.md "bulk-load-tutorial-IAM-CreateRole.md").

## Create a custom NeptuneSageMakerIAMRole role

Use the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") to create a custom
`NeptuneSageMakerIAMRole`, using the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:CreateVpcEndpoint",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker.amazonaws.com"
 ]
 }
 },
 "Effect": "Allow"
 },
 {
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "arn:aws:kms:*:*:key/*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/sagemaker/*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "sagemaker:AddTags",
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateHyperParameterTuningJob",
 "sagemaker:CreateModel",
 "sagemaker:CreateProcessingJob",
 "sagemaker:CreateTrainingJob",
 "sagemaker:CreateTransformJob",
 "sagemaker:DeleteEndpoint",
 "sagemaker:DeleteEndpointConfig",
 "sagemaker:DeleteModel",
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeHyperParameterTuningJob",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeProcessingJob",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:DescribeTransformJob",
 "sagemaker:InvokeEndpoint",
 "sagemaker:ListTags",
 "sagemaker:ListTrainingJobsForHyperParameterTuningJob",
 "sagemaker:StopHyperParameterTuningJob",
 "sagemaker:StopProcessingJob",
 "sagemaker:StopTrainingJob",
 "sagemaker:StopTransformJob",
 "sagemaker:UpdateEndpoint",
 "sagemaker:UpdateEndpointWeightsAndCapacities"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:*"
 ],
 "Effect": "Allow"
 },
 {
 "Action": [
 "sagemaker:ListEndpointConfigs",
 "sagemaker:ListEndpoints",
 "sagemaker:ListHyperParameterTuningJobs",
 "sagemaker:ListModels",
 "sagemaker:ListProcessingJobs",
 "sagemaker:ListTrainingJobs",
 "sagemaker:ListTransformJobs"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:AbortMultipartUpload",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

While creating this role, edit the trust relationship
so that it reads as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "ec2.amazonaws.com",
 "rds.amazonaws.com",
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Finally, copy the ARN assigned to this new `NeptuneSageMakerIAMRole` role.

###### Important

- Be sure that the Amazon S3 permissions in the `NeptuneSageMakerIAMRole`
  match those above.
- The universal ARN, `arn:aws:s3:::*` is used for the Amazon S3 resource
  in the policy above. If for some reason the universal ARN cannot be used, then
  `arn:aws:s3:::graphlytics*` and the ARN for any other customer Amazon S3
  resource that NeptuneML commands will use must be added to the resource section.

## Configure your DB cluster to enable Neptune ML

###### To set up your DB cluster for Neptune ML

1. In the [Neptune console](https://console.aws.amazon.com/neptune "https://console.aws.amazon.com/neptune"), navigate to **Parameter Groups**
   and then to the DB cluster parameter group associated with the DB cluster you will be
   using. Set the `neptune_ml_iam_role` parameter to the ARN assigned
   to the `NeptuneSageMakerIAMRole` role that you just created.
2. Navigate to Databases, then select the DB cluster you will be using for
   Neptune ML. Select **Actions** then **Manage IAM roles**.
3. On the **Manage IAM roles** page, select **Add role**
   and add the `NeptuneSageMakerIAMRole`. Then add the `NeptuneLoadFromS3` role.
4. Reboot the writer instance of your DB cluster.

## Create two SageMaker AI endpoints in your Neptune VPC

Finally, to give the Neptune engine access the necessary SageMaker AI management APIs,
you need to create two SageMaker AI endpoints in your Neptune VPC, as explained in
[Create two endpoints for SageMaker AI in your Neptune VPC](machine-learning-cluster-setup.md#machine-learning-sm-endpoints "machine-learning-cluster-setup.md#machine-learning-sm-endpoints").
