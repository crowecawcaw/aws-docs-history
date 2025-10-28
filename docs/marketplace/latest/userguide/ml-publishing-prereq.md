# Prerequisites

Before you can publish your model package or algorithm in AWS Marketplace, you must have the following:

- An AWS account that is registered as an AWS Marketplace seller. You can do this in the
  [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/").
- A completed seller profile under the [Settings](https://aws.amazon.com/marketplace/management/seller-settings "https://aws.amazon.com/marketplace/management/seller-settings") page in the AWS Marketplace Management Portal.
- For publishing paid products, you must complete the tax interview and bank forms. This
  is not required for publishing free products. For more information, see [Seller registration process](registration-process.md "registration-process.md").
- You must have permissions to access the AWS Marketplace Management Portal and Amazon SageMaker AI. For more information,
  see [Required permissions](#ml-permissions-required "#ml-permissions-required").

## Required permissions

To publish an Amazon SageMaker AI product, you must specify a valid IAM role ARN that has a trust
relationship with the AWS Marketplace service principal. Additionally, the IAM user or role you are
signed in as requires the necessary permissions.

###### Setting sign-in permissions

- Add the following permissions to the IAM role:
  1.  **sagemaker:DescribeModelPackage** — For
      listing a model package
  2.  **sagemaker:DescribeAlgorithm** — For listing
      an algorithm

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Action": [
   "sagemaker:DescribeModelPackage",
   "sagemaker:DescribeAlgorithm"
   ],
   "Resource": "*"
   }
   ]
  }`

  ```

###### Setting the IAM role AddVersion/Create product

1. Follow the steps to create a role with a custom trust policy. For more information,
   see [Creating an IAM role using a custom trust policy (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").
2. Enter the following for the custom trust policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "Service": "assets.marketplace.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. Enter the following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeModelPackage",
 "sagemaker:DescribeAlgorithm"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. Provide the role ARN when requested. The role should follow the format:
   `arn:aws:iam::`<account-id>`:role/`<role-name>``.

For the AWS Marketplace permissions needed, or for managing your seller account, see [Policies
and permissions for AWS Marketplace sellers](detailed-management-portal-permissions.md "detailed-management-portal-permissions.md").

## Required assets

Before creating a machine learning product listing, ensure that you have the following
required assets:

- **Amazon Resource Name (ARN)** — Provide the ARN
  of the model package or algorithm resource in the AWS Region that you are publishing
  from (see [Supported AWS Regions for
  publishing](ml-service-restrictions-and-limits.md#ml-supported-aws-regions-for-publishing "ml-service-restrictions-and-limits.md#ml-supported-aws-regions-for-publishing")).
  - An ARN for a model package has this form:
    `arn:aws:sagemaker:<region>:<account-id>:model-package/<model-package-name>`

  To find your model package ARN, see [My marketplace model packages](https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources "https://console.aws.amazon.com/sagemaker/home#/model-packages/my-resources").
  - An ARN for an algorithm has this form:
    `arn:aws:sagemaker:<region>:<account-id>:algorithm/<algorithm-name>`

  To find your algorithm resource ARN, see [My algorithms](https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources "https://console.aws.amazon.com/sagemaker/home#/algorithms/my-resources").

- [Requirements for usage
  information](ml-listing-requirements-and-best-practices.md#ml-requirements-for-usage-information "ml-listing-requirements-and-best-practices.md#ml-requirements-for-usage-information") — Provide details about
  inputs, outputs, and code examples.
- [Requirements for inputs and
  outputs](ml-listing-requirements-and-best-practices.md#ml-requirements-for-inputs-and-outputs "ml-listing-requirements-and-best-practices.md#ml-requirements-for-inputs-and-outputs") — Provide either files or
  text.
- [Requirements for Jupyter
  notebook](ml-listing-requirements-and-best-practices.md#ml-requirements-for-jupyter-notebook "ml-listing-requirements-and-best-practices.md#ml-requirements-for-jupyter-notebook") — Demonstrate complete
  product usage.
