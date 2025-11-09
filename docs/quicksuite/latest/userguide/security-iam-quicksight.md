# AWS managed policies for

Amazon Quick Suite

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and resources.
For a list and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed
  policy: AWSQuickSightElasticsearchPolicy](#security-iam-quicksight-AWSQuickSightElasticsearchPolicy "#security-iam-quicksight-AWSQuickSightElasticsearchPolicy")
- [AWS managed
  policy: AWSQuickSightOpenSearchPolicy](#security-iam-quicksight-AWSQuickSightOpenSearchPolicy "#security-iam-quicksight-AWSQuickSightOpenSearchPolicy")
- [AWS managed
  policy: AWSQuickSightSageMakerPolicy](#security-iam-quicksight-AWSQuickSightSageMakerPolicy "#security-iam-quicksight-AWSQuickSightSageMakerPolicy")
- [AWS
  managed policy: AWSQuickSightAssetBundleExportPolicy](#security-iam-quicksight-AWSQuickSightAssetBundleExportPolicy "#security-iam-quicksight-AWSQuickSightAssetBundleExportPolicy")
- [AWS
  managed policy: AWSQuickSightAssetBundleImportPolicy](#security-iam-quicksight-AWSQuickSightAssetBundleImportPolicy "#security-iam-quicksight-AWSQuickSightAssetBundleImportPolicy")
- [Amazon Quick Suite updates to AWS managed
  policies](#security-iam-quicksight-updates "#security-iam-quicksight-updates")

## AWS managed

policy: AWSQuickSightElasticsearchPolicy

This information is provided for backward compatibility only. The
`AWSQuickSightOpenSearchPolicy` AWS managed policy replaces the
`AWSQuickSightElasticsearchPolicy` AWS managed policy.

Previously, you used the `AWSQuickSightElasticsearchPolicy` AWS managed
policy to provide access to Amazon Elasticsearch Service resources from
Amazon Quick Suite. Starting on or after September 7, 2021, Amazon Elasticsearch Service
is renamed to Amazon OpenSearch Service.

Wherever you are using `AWSQuickSightElasticsearchPolicy`, you can update
to the new AWS managed policy that's called
`AWSQuickSightOpenSearchPolicy`. You can attach the policy to your IAM
entities. Amazon Quick Suite also attaches the policy to a service role that allows
Amazon Quick Suite to perform actions on your behalf.
`AWSQuickSightElasticsearchPolicy` is still available and as of August
31, 2021, had the same permissions as the new policy. However,
`AWSQuickSightElasticsearchPolicy` is no longer kept up-to-date with
latest changes.

This policy grants read-only permissions that allow access to OpenSearch (previously
known as Elasticsearch) resources from Amazon Quick Suite.

**Permissions details**

This policy includes the following permissions:

- `es` – Allows principals to use `es:ESHttpGet` to
  access your OpenSearch (previously known as Elasticsearch) domains,
  cluster settings, and indices. This is required to use
  the
  search service from Amazon Quick Suite.
- `es` – Allows principals to use
  `es:ListDomainNames` to list your OpenSearch (previously known
  as Elasticsearch) domains. This is required to initiate access of
  the
  search service from Amazon Quick Suite.
- `es` – Allows principals to use
  `es:DescribeElasticsearchDomain` to search your OpenSearch
  (previously known as Elasticsearch) domains. This is required to use
  the
  search service from Amazon Quick Suite.
- `es` – Allows principals to use `es:ESHttpPost`
  and `es:ESHttpGet` with your OpenSearch (previously known as
  Elasticsearch) domains. This is required to use a SQL plugin with
  read-only access to
  the
  search service domains from Amazon Quick Suite.

For information on the contents of this IAM policy, see [AWSQuickSightElasticsearchPolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSQuickSightElasticsearchPolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSQuickSightElasticsearchPolicy$jsonEditor") in the IAM console.

## AWS managed

policy: AWSQuickSightOpenSearchPolicy

Use the `AWSQuickSightOpenSearchPolicy` AWS managed policy to provide
access to Amazon OpenSearch Service resources from Amazon Quick Suite.
`AWSQuickSightOpenSearchPolicy` replaces
`AWSQuickSightElasticsearchPolicy`. As of August 31, 2021, this policy
had the same permissions as the legacy policy,
`AWSQuickSightElasticsearchPolicy`. For now, you can use them
interchangeably. For the long term, we recommend updating your policy usage to
`AWSQuickSightOpenSearchPolicy`.

You can attach `AWSQuickSightOpenSearchPolicy` to your IAM entities.
Amazon Quick Suite also attaches this policy to a service role that allows Amazon Quick Suite to
perform actions on your behalf.

This policy grants read-only permissions that allow access to
OpenSearch resources from Amazon Quick Suite.

**Permissions details**

This policy includes the following permissions:

- `es` – Allows principals to use `es:ESHttpGet` to
  access your OpenSearch domains, cluster settings, and indices. This is
  required to use Amazon OpenSearch Service from Amazon Quick Suite.
- `es` – Allows principals to use
  `es:ListDomainNames` to list your OpenSearch domains. This is
  required to initiate access of Amazon OpenSearch Service from Amazon Quick Suite.
- `es` – Allows principals to use
  `es:DescribeElasticsearchDomain` and
  `es:DescribeDomain` to search your OpenSearch domains. This is
  required to use Amazon OpenSearch Service from Amazon Quick Suite.
- `es` – Allows principals to use `es:ESHttpPost`
  and `es:ESHttpGet` with your OpenSearch domains. This is required
  to use a SQL plugin with read-only access to Amazon OpenSearch Service domains from
  Amazon Quick Suite.

For information on the contents of this IAM policy, see [AWSQuickSightOpenSearchPolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSQuickSightOpenSearchPolicy$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSQuickSightOpenSearchPolicy$jsonEditor") in the IAM console.

## AWS managed

policy: AWSQuickSightSageMakerPolicy

Use the `AWSQuickSightSageMakerPolicy` AWS managed policy to provide
access to Amazon SageMaker AI resources from Amazon Quick Suite.

You can attach `AWSQuickSightSageMakerPolicy` to your IAM entities.
Amazon Quick Suite also attaches this policy to a service role that allows Amazon Quick Suite to
perform actions on your behalf.

This policy grants read-only permissions that allow access to
Amazon SageMaker AI resources from Amazon Quick Suite.

To view the `AWSQuickSightSageMakerPolicy`, see [AWSQuickSightSageMakerPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSightSageMakerPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSightSageMakerPolicy.md") in the [AWS
Managed Policy reference](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

**Permissions details**

This policy includes the following permissions:

- `sagemaker` – .
- `s3` – Allows principals to use `s3:GetObject` on
  all Amazon S3 buckets that start with the prefix
  `arn:aws:s3:::sagemaker.*` to access data stored in SageMaker AI
  default buckets. This is required to load models shared from Amazon SageMaker AI Canvas to
  the default Amazon SageMaker AI Canvas Amazon S3 bucket.
- `s3` – Allows principals to use `s3:PutObject` to
  export objects into an Amazon S3 bucket. This is required to support existing
  datasets from Amazon Quick Suite to Amazon SageMaker AI Canvas to build predictive models.
- `s3` – Allows principals to use `s3:ListBucket`
  to allow Amazon Quick Suite to validate an existing Amazon SageMaker AI Canvas bucket in Amazon S3.
  This is required to allow the export of data from Amazon Quick Suite to Amazon SageMaker AI
  Canvas to build predictive models.
- `s3` – Allows principals to use `s3:GetObject` on
  all Amazon Quick Suite– owned Amazon S3 buckets that start with the prefix
  `arn:aws:s3:::quicksight-ml`. This is required to allow
  Amazon Quick Suite to access the predictions that are generated by Amazon SageMaker AI Canvas.
  The generated predictions can be appended to a Amazon Quick Suite dataset.
- `sagemaker` – Allows principals to use
  `sagemaker:CreateTransformJob`,
  `sagemaker:DescribeTransformJob`, and
  `sagemaker:StopTransformJob` to perform SageMaker AI transform jobs on
  your behalf. This is required for Amazon Quick Suite to request predictions from SageMaker AI
  models that can be appended to a Amazon Quick Suite dataset.
- `sagemaker` – Allows principals to use
  `sagemaker:ListModels` to list your SageMaker AI models. This is required
  to allow generated SageMaker AI models to appear in Amazon Quick Suite.

## AWS

managed policy: AWSQuickSightAssetBundleExportPolicy

Use the `AWSQuickSightAssetBundleExportPolicy` AWS managed policy to
perform asset bundle export operations. You can attach
`AWSQuickSightAssetBundleExportPolicy` to your IAM entities.

This policy grants read-only permissions that allow access to Amazon Quick Suite asset
resources. To view the details of this policy, see [AWSQuickSightAssetBundleExportPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSightAssetBundleExportPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSightAssetBundleExportPolicy.md") in the AWS Managed Policy
reference.

This policy includes the following permissions:

- `quicksight` – Allows principals to use
  `quicksight:Describe*` and `quicksight:List*` to find
  and fetch Amazon Quick Suite assets and their corresponding permissions.
- `quicksight` – Allows principals to use
  `quicksight:ListTagsForResource` to fetch tags of Amazon Quick Suite
  assets.
- `quicksight` – Allows principals to list, execute, and get
  the status of an Asset bundle export job. This policy uses the
  `quicksight:ListAssetBundleExportJob`,
  `StartAssetBundleExportJob`, and
  `quicksight:DescribeAssetBundleExportJob` permissions.

## AWS

managed policy: AWSQuickSightAssetBundleImportPolicy

Use the `AWSQuickSightAssetBundleImportPolicy` AWS managed policy to
perform asset bundle import operations. This managed policy does not grant permissions
for any run-as-role functionality with the `iam:passrole` that is required
for some VPC connection and DataSource operations. This policy also does not grant
access to retrieve objects from a users Amazon S3 bucket.

You can attach the `AWSQuickSightAssetBundleImportPolicy` to your IAM
entities. This policy grants read and write permissions that allow access to
Amazon Quick Suite resources. To view the details of this policy, see [AWSQuickSightAssetBundleImportPolicy](../../../aws-managed-policy/latest/reference/AWSQuickSightAssetBundleImportPolicy.md "../../../aws-managed-policy/latest/reference/AWSQuickSightAssetBundleImportPolicy.md") in the AWS Managed Policy
reference.

This policy includes the following permissions:

- `quicksight` – Allows principals to use
  `quicksight:Describe*` and `quicksight:List*` to
  detect changes in the Amazon Quick Suite assets and their permissions.
- `quicksight` – Allows principals to use
  `quicksight:Create*` and `quicksight:Update*` to make
  changes to the Amazon Quick Suite assets and permissions from the supplied asset
  bundle.
- `quicksight` – Allows principals to use
  `quicksight:ListTagsForResource`,
  `quicksight:TagResource`, and
  `quicksight:UntagResource` to update the tags of Amazon Quick Suite
  assets.
- `quicksight` – Allows principals to list, execute, and get
  the status of an Asset bundle import job. This policy uses the
  `quicksight:ListAssetBundleImportJob`,
  `quicksight:StartAssetBundleImportJob`, and
  `quicksight:DescribeAssetBundleImportJob` permissions.

## Amazon Quick Suite updates to AWS managed

policies

View details about updates to AWS managed policies for Amazon Quick Suite since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Amazon Quick Suite Document
History](doc-history.md "doc-history.md") page.

| Change                                                               | Description                                                                                                       | Date               |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------ |
| `AWSQuickSightAssetBundleExportPolicy` – New<br>policy               | Amazon Quick Suite added new permissions to simplify Asset bundle export<br>operations.                           | March 27, 2024     |
| `AWSQuickSightAssetBundleImportPolicy` – New<br>policy               | Amazon Quick Suite added new permissions to simplify Asset bundle import<br>operations.                           | March 27, 2024     |
| `AWSQuickSageMakerPolicy` – Update to an<br>existing policy          | Amazon Quick Suite added new permissions to allow integration with<br>Amazon SageMaker AI Canvas.                 | July 25, 2023      |
| `AWSQuickSightElasticsearchPolicy` – Update to<br>an existing policy | Amazon Quick Suite added new permissions to provide access to Amazon OpenSearch Service<br>resources.             | September 08, 2021 |
| `AWSQuickSightOpenSearchPolicy` – New<br>policy                      | Amazon Quick Suite added a new policy to allow access to Amazon OpenSearch Service<br>resources from Quick Suite. | September 08, 2021 |
| Amazon Quick Suite started tracking<br>changes                       | Amazon Quick Suite started tracking changes for its AWS managed<br>policies.                                      | August 2, 2021     |
