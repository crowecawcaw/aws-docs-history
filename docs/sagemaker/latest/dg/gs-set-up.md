# Complete Amazon SageMaker AI prerequisites

Before you can set up Amazon SageMaker AI, you must complete the following prerequisites.

- **Required**: You will need to create an Amazon Web Services
  (AWS) account to get access to all of the AWS services and resources for the
  account.
- **Highly recommended**: We highly recommend that you
  create an administrative user to manage AWS resources for the account, to adhere
  to the [Security best practices in
  IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"). It is assumed that you have an administrative user for many of
  the administrative tasks throughout the SageMaker AI developer guide.
- **Optional**: Configure the AWS Command Line Interface (AWS CLI) if you
  intend to manage your AWS services and resources for the account using the
  AWS CLI.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [(Optional) Configure the AWS CLI](#gs-cli-prereq "#gs-cli-prereq")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

When you create an administrative user to set up SageMaker AI, the administrative user should
include specific permissions to create SageMaker AI resources. To view the permissions, expand the
following administrator permissions section.

When you create your administrative user using the preceding instructions, your
administrative user should already include the permissions contained in the [AmazonSageMakerFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonSageMakerFullAccess") policy, as well as the following permissions.
These policies are needed to create a SageMaker AI domain among other tasks.

If you intend to create your own custom policy, these permissions are required to
create a domain and get set up with SageMaker AI. For information about adding policies,
see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _AWS Identity and Access Management User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:*"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:domain/*",
 "arn:aws:sagemaker:*:*:user-profile/*",
 "arn:aws:sagemaker:*:*:app/*",
 "arn:aws:sagemaker:*:*:flow-definition/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetRole",
 "servicecatalog:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

**Optional**: If you intend to manage your AWS services and
resources for the account using the AWS CLI, proceed to the following instructions ([(Optional) Configure the AWS CLI](#gs-cli-prereq "#gs-cli-prereq")).

**After you have completed your prerequisites**, continue on
to the setup instructions. You can continue on to your setup instructions by choosing one of
the following options.

- **[Use quick setup](onboard-quick-start.md "onboard-quick-start.md")**: Fastest setup for
  individual users with default settings.
- **[Use custom setup](onboard-custom.md "onboard-custom.md")**: Advanced setup for
  enterprise Machine Learning (ML) administrators. Ideal option for ML administrators
  setting up SageMaker AI for many users or an organization.

## (Optional) Configure the AWS CLI

To manage your domain and other AWS services and resources using the AWS CLI,
complete the setup in [Set up the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in
the _AWS Command Line Interface User Guide for Version 2_.

**After you have completed your prerequisites**, continue
on to the setup instructions. You can continue on to your setup instructions by choosing
one of the following options.

- **[Use quick setup](onboard-quick-start.md "onboard-quick-start.md")**: Fastest setup
  for individual users with default settings.
- **[Use custom setup](onboard-custom.md "onboard-custom.md")**: Advanced setup for
  enterprise Machine Learning (ML) administrators. Ideal option for ML
  administrators setting up SageMaker AI for many users or an organization.
