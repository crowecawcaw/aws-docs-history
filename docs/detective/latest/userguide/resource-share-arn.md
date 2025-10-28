# Step 3: Accepting the Resource Share ARN invitation

This topic explains the steps to accept the Resource Share ARN invitation using a AWS CloudFormation template, which is a required step before you enable Detective integration with Security Lake.

To access raw data logs from Security Lake, you must accept a Resource Share invitation from
the Security Lake account that was created by the Security Lake administrator. You also need AWS Lake Formation
permissions to set up cross-account table sharing. In addition, you must create an
Amazon Simple Storage Service (Amazon S3) bucket that can receive raw query logs.

In this next step, you’ll use an AWS CloudFormation template to create a stack for: accepting the Resource Share ARN invitation, create required AWS Glue crawler resources, and grant AWS Lake Formation administrator permissions.

###### To accept the Resource Share ARN invitation and enable the integration

1. Create a new CloudFormation stack using the CloudFormation template. For more details,
   see [Creating a stack using the AWS CloudFormation
   template](#cloud-formation-template "#cloud-formation-template").
2. After you finish creating the stack, choose **Enable integration** to enable Detective integration with Security Lake.

## Creating a stack using the AWS CloudFormation

template

Detective provides an AWS CloudFormation template, which you can use to set up the parameters required to create and manage query access for Security Lake subscribers.

###### Step 1: Create an AWS CloudFormation service role

You must create an AWS CloudFormation service role to create a stack using the AWS CloudFormation template.
If you do not have the required permissions to create a service role, contact the
administrator of the Detective administrator account. For more information about the
AWS CloudFormation service role, see [AWS CloudFormation
service role](../../../AWSCloudFormation/latest/UserGuide/using-iam-servicerole.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-servicerole.md").

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**, and
   then choose **Create role**.
3. For **Select trusted entity**, choose **AWS
   service**.
4. Choose **AWS CloudFormation**. Then, choose
   **Next**.
5. Enter a name for the role. For example,
   `CFN-DetectiveSecurityLakeIntegration`.
6. Attach the following inline policies to the role. Replace `<Account ID>` with your AWS Account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudFormationPermission",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateChangeSet"
 ],
 "Resource": [
 "arn:aws:cloudformation:*:aws:transform/*"
 ]
 },
 {
 "Sid": "IamPermissions",
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:AttachRolePolicy",
 "iam:DetachRolePolicy",
 "iam:UpdateAssumeRolePolicy",
 "iam:PutRolePolicy",
 "iam:DeleteRolePolicy",
 "iam:CreatePolicy",
 "iam:DeletePolicy",
 "iam:PassRole",
 "iam:GetRole",
 "iam:GetRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/*-ResourceShareAcceptorLamb-*",
 "arn:aws:iam::`111122223333`:role/*-SsmParametersLambdaRole-*",
 "arn:aws:iam::`111122223333`:role/*-GlueDatabaseLambdaRole-*",
 "arn:aws:iam::`111122223333`:role/*-GlueTablesLambdaRole-*",
 "arn:aws:iam::`111122223333`:policy/*"
 ]
 },
 {
 "Sid": "S3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucket*",
 "s3:PutBucket*",
 "s3:GetBucket*",
 "s3:GetObject",
 "s3:PutEncryptionConfiguration",
 "s3:GetEncryptionConfiguration"
 ],
 "Resource": [
 "arn:aws:s3:::*"
 ]
 },
 {
 "Sid": "LambdaPermissions",
 "Effect": "Allow",
 "Action": [
 "lambda:CreateFunction",
 "lambda:DeleteFunction",
 "lambda:GetFunction",
 "lambda:TagResource",
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:*:`111122223333`:function:*"
 ]
 },
 {
 "Sid": "CloudwatchPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:DeleteLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource": "arn:aws:logs:*:`111122223333`:log-group:*"
 },
 {
 "Sid": "KmsPermission",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:*:`111122223333`:key/*"
 }
 ]
}`

```

[Show moreShow less](# "#")
**Step 2: Adding permissions to your IAM
principal**.

You’ll need the following permissions to create a stack using the CloudFormation service
role that you created in the preceding step. Add the following IAM policy to the IAM
principal that you plan to use to pass the CloudFormation service role. You will assume this
IAM principal to create the stack. If you do not have the required permissions to add
the IAM policy, contact the administrator of the Detective administrator account.

###### Note

In the following policy, `CFN-DetectiveSecurityLakeIntegration` used in this policy
refers to the role that you created in the previous `Creating an
 AWS CloudFormation` service role step. Change it to the role name that you entered in the preceding step if it’s different.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PassRole",
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/CFN-DetectiveSecurityLakeIntegration"
 },
 {
 "Sid": "RestrictCloudFormationAccess",
 "Effect": "Allow",
 "Action": [
 "cloudformation:CreateStack",
 "cloudformation:DeleteStack",
 "cloudformation:UpdateStack"
 ],
 "Resource": "arn:aws:cloudformation:*:`111122223333`:stack/*",
 "Condition": {
 "StringEquals": {
 "cloudformation:RoleArn": [
 "arn:aws:iam::`111122223333`:role/CFN-DetectiveSecurityLakeIntegration"
 ]
 }
 }
 },
 {
 "Sid": "CloudformationDescribeStack",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStacks",
 "cloudformation:DescribeStackEvents",
 "cloudformation:GetStackPolicy"
 ],
 "Resource": "arn:aws:cloudformation:*:`111122223333`:stack/*"
 },
 {
 "Sid": "CloudformationListStacks",
 "Effect": "Allow",
 "Action": [
 "cloudformation:ListStacks"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:GetLogEvents"
 ],
 "Resource": "arn:aws:logs:*:`111122223333`:log-group:*"
 }
 ]
}`

```

[Show moreShow less](# "#")

###### Step 3: Specifying custom values in the AWS CloudFormation console

1. Go to the AWS CloudFormation console from Detective.
2. (Optional) Enter a **Stack name**. The stack name is
   auto-filled. You can change the stack name to a name that does not conflict with
   existing stack names.
3. Enter the following **Parameters**.
   - **AthenaResultsBucket** – If you don't enter
     values, this template generates an Amazon S3 bucket. If you want to use your
     own bucket, enter a bucket name to store the Athena query results. If you
     use your own bucket, make sure that the bucket is in the same Region as
     the Resource Share ARN. If you use your own bucket, make sure the
     `LakeFormationPrincipals` you choose have permissions to
     write objects to and read objects from the bucket. For more details
     about bucket permissions, see [Query results and recent
     queries](../../../athena/latest/ug/querying.md "../../../athena/latest/ug/querying.md") in the Amazon Athena User Guide.
   - **DTRegion** – This field is pre-filled. Do not change the values in this field.
   - **LakeFormationPrincipals** – Enter the ARN of the IAM principals
     (for example, IAM role ARN) that you want to grant access to use the
     Security Lake integration, separated by commas. These could be your security
     analysts and security engineers that use Detective.

   You can only use the IAM principals that you previously attached the
   IAM permissions to in step [`Step 2: Add the required IAM
   permissions to your account]`.
   - **ResourceShareARN** – This field is pre-filled. Do not change the values in this field.

4. **Permissions**

**IAM role** – Select the role that you created in the
`Creating an AWS CloudFormation Service Role` step. Optionally, you can
keep it blank if your current IAM role has all the required permissions in the
`Creating an AWS CloudFormation Service Role` step. 5. Review and check all the **I Acknowledge** boxes and
then click the **Create stack** button. For more details, review the following IAM resources that will be created.

```
* ResourceShareAcceptorCustomResourceFunction
    - ResourceShareAcceptorLambdaRole
    - ResourceShareAcceptorLogsAccessPolicy
* SsmParametersCustomResourceFunction
    - SsmParametersLambdaRole
    - SsmParametersLogsAccessPolicy
* GlueDatabaseCustomResourceFunction
    - GlueDatabaseLambdaRole
    - GlueDatabaseLogsAccessPolicy
* GlueTablesCustomResourceFunction
    - GlueTablesLambdaRole
    - GlueTablesLogsAccessPolicy
```

**Step 4: Adding Amazon S3 bucket policy to IAM principals in `LakeFormationPrincipals`**

(Optional) If you let this template generate an `AthenaResultsBucket` for
you, you must attach the following policy to the IAM principals in
`LakeFormationPrincipals`.

```
{
  "Sid": "S3ObjectPermissions",
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject"
  ],
  "Resource": [
    "arn:aws:s3:::<athena-results-bucket>",
    "arn:aws:s3:::<athena-results-bucket>/*"
  ]
}
```

Replace `athena-results-bucket` with
the `AthenaResultsBucket` name. The `AthenaResultsBucket`
can be found on the AWS CloudFormation console:

1. Open the AWS CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Click on your Stack.
3. Click the **Resources** tab.
4. Search for the logical ID `AthenaResultsBucket` and copy its physical ID.
