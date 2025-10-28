# Setting up permissions

To prepare data with Data Wrangler, you must set up the following permissions:

- **Create a service role for Amazon Personalize:** If you haven't already, complete the instructions in [Setting up Amazon Personalize](setup.md "setup.md") to create an
  IAM service role for Amazon Personalize. This role must have `GetObject` and `ListBucket` permissions for
  the Amazon S3 buckets that store your processed data. And it must have
  permission to use any AWS KMS keys.

For information about granting Amazon Personalize access to your Amazon S3 buckets, see [Giving Amazon Personalize access to Amazon S3 resources](granting-personalize-s3-access.md "granting-personalize-s3-access.md").
For information about granting Amazon Personalize access to your AWS KMS keys, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

- **Create an administrative user with SageMaker AI permissions:**
  Your administrator must have full access to SageMaker AI and must be able to create a SageMaker AI domain.
  For more information, see [Create an Administrative User and Group](../../../sagemaker/latest/dg/gs-set-up.md#gs-account-user "../../../sagemaker/latest/dg/gs-set-up.md#gs-account-user")
  in the _Amazon SageMaker AI Developer Guide_.
- **Create a SageMaker AI execution role:** Create a SageMaker AI execution role with access to SageMaker AI resources and Amazon Personalize data import operations.
  The SageMaker AI execution role must have the [`AmazonSageMakerFullAccess`](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy attached. If you require more granular Data Wrangler permissions, see
  [Data Wrangler Security and Permissions](../../../sagemaker/latest/dg/data-wrangler-security.md#data-wrangler-security-iam-policy "../../../sagemaker/latest/dg/data-wrangler-security.md#data-wrangler-security-iam-policy") in the _Amazon SageMaker AI Developer Guide_.
  For more information on SageMaker AI roles, see [SageMaker AI Roles](../../../sagemaker/latest/dg/sagemaker-roles.md "../../../sagemaker/latest/dg/sagemaker-roles.md").

To grant access to Amazon Personalize data import operations, attach the following IAM policy to the SageMaker AI execution role.
This policy grants the permissions required to import data into Amazon Personalize and attach a policy to your Amazon S3 bucket.
And it grants `PassRole` permissions when the service is Amazon Personalize. Update the Amazon S3 `amzn-s3-demo-bucket` to the name
of the Amazon S3 bucket you want to use as the destination for your formatted data after you prepare it with Data Wrangler.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "personalize:Create*",
 "personalize:List*",
 "personalize:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutBucketPolicy"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "personalize.amazonaws.com"
 }
 }
 }
 ]
}`

```

For information on creating an IAM policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_. For information on attaching an IAM policy to
role, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.
