# Set up policies and permissions for

Studio

You will need to install the proper policies and permissions before you schedule your first
notebook run. The following provides instructions on setting up the following permissions:

- Job execution role trust relationships
- Additional IAM permissions attached to the job execution role
- (optional) The AWS KMS permission policy to use a custom KMS key

###### Important

If your AWS account belongs to an organization with service control policies (SCP)
in place, your effective permissions are the logical intersection between what is allowed
by the SCPs and what is allowed by your IAM role and user policies. For example, if your
organization’s SCP specifies that you can only access resources in `us-east-1`
and `us-west-1`, and your policies only allow you to access resources in
`us-west-1` and `us-west-2`, then ultimately you can only access
resources in `us-west-1`. If you want to exercise all the permissions allowed
in your role and user policies, your organization’s SCPs should grant the same set of
permissions as your own IAM user and role policies. For details about how to determine
your allowed requests, see [Determining whether a request is allowed or denied within an account](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow").

**Trust relationships**

To modify the trust relationships, complete the following steps:

1. Open the [IAM
   console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Select **Roles** in the left panel.
3. Find the job execution role for your notebook job and choose the role name.
4. Choose the **Trust relationships** tab.
5. Choose **Edit trust policy**.
6. Copy and paste the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "sagemaker.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

7. Choose **Update Policy**.

## Additional IAM permissions

You might need to include additional IAM permissions in the following
situations:

- Your Studio execution and notebook job roles differ
- You need to access Amazon S3 resources through a S3 VPC endpoint
- You want to use a custom KMS key to encrypt your input and output
  Amazon S3 buckets

The following discussion provides the policies you need for each case.

### Permissions needed if your

Studio execution and notebook job roles differ

The following JSON snippet is an example policy that you should add to the
Studio execution and notebook job roles if you don’t use the Studio execution
role as the notebook job role. Review and modify this policy if you need to further
restrict privileges.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"iam:PassRole",
 "Resource":"arn:aws:iam::*:role/*",
 "Condition":{
 "StringLike":{
 "iam:PassedToService":[
 "sagemaker.amazonaws.com",
 "events.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect":"Allow",
 "Action":[
 "events:TagResource",
 "events:DeleteRule",
 "events:PutTargets",
 "events:DescribeRule",
 "events:PutRule",
 "events:RemoveTargets",
 "events:DisableRule",
 "events:EnableRule"
 ],
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "aws:ResourceTag/sagemaker:is-scheduling-notebook-job":"true"
 }
 }
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:CreateBucket",
 "s3:PutBucketVersioning",
 "s3:PutEncryptionConfiguration"
 ],
 "Resource":"arn:aws:s3:::sagemaker-automated-execution-*"
 },
 {
 "Sid": "S3DriverAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetObject",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::sagemakerheadlessexecution-*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "sagemaker:ListTags"
 ],
 "Resource":[
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:space/*",
 "arn:aws:sagemaker:*:*:training-job/*",
 "arn:aws:sagemaker:*:*:pipeline/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "sagemaker:AddTags"
 ],
 "Resource":[
 "arn:aws:sagemaker:*:*:training-job/*",
 "arn:aws:sagemaker:*:*:pipeline/*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcEndpoints",
 "ec2:DescribeVpcs",
 "ecr:BatchCheckLayerAvailability",
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetAuthorizationToken",
 "s3:ListBucket",
 "s3:GetBucketLocation",
 "s3:GetEncryptionConfiguration",
 "s3:PutObject",
 "s3:DeleteObject",
 "s3:GetObject",
 "sagemaker:DescribeApp",
 "sagemaker:DescribeDomain",
 "sagemaker:DescribeUserProfile",
 "sagemaker:DescribeSpace",
 "sagemaker:DescribeStudioLifecycleConfig",
 "sagemaker:DescribeImageVersion",
 "sagemaker:DescribeAppImageConfig",
 "sagemaker:CreateTrainingJob",
 "sagemaker:DescribeTrainingJob",
 "sagemaker:StopTrainingJob",
 "sagemaker:Search",
 "sagemaker:CreatePipeline",
 "sagemaker:DescribePipeline",
 "sagemaker:DeletePipeline",
 "sagemaker:StartPipelineExecution"
 ],
 "Resource":"*"
 }
 ]
}`

```

### Permissions needed to access Amazon S3

resources through a S3 VPC endpoint

If you run SageMaker Studio in private VPC mode and access S3 through the S3 VPC
endpoint, you can add permissions to the VPC endpoint policy to control which S3
resources are accessible through the VPC endpoint. Add the following permissions to your
VPC endpoint policy. You can modify the policy if you need to further restrict
permissions—for example, you can provide a more narrow specification for the
`Principal` field.

```
{
    "Sid": "S3DriverAccess",
    "Effect": "Allow",
    "Principal": "*",
    "Action": [
        "s3:GetBucketLocation",
        "s3:GetObject",
        "s3:ListBucket"
    ],
    "Resource": "arn:aws:s3:::sagemakerheadlessexecution-*"
}
```

For details about how to set up a S3 VPC endpoint policy, see [Edit
the VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-s3.md#edit-vpc-endpoint-policy-s3 "../../../vpc/latest/privatelink/vpc-endpoints-s3.md#edit-vpc-endpoint-policy-s3").

### Permissions needed to use a custom

KMS key (optional)

By default, the input and output Amazon S3 buckets are encrypted using
server side encryption, but you can specify a custom KMS key to encrypt your data in
the output Amazon S3 bucket and the storage volume attached to the notebook job.

If you want to use a custom KMS key, attach the following policy and supply your
own KMS key ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect":"Allow",
 "Action":[
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*",
 "kms:DescribeKey",
 "kms:CreateGrant"
 ],
 "Resource":"arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 }
 ]
}`

```
