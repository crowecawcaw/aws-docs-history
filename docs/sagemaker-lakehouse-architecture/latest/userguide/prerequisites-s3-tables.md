# Prerequisites for onboarding data to the lakehouse architecture of Amazon SageMaker

Before onboarding data into the lakehouse architecture, ensure you have completed the initial setup. For detailed setup instructions, see [Getting started with the lakehouse architecture of Amazon SageMaker](lakehouse-get-started.md "lakehouse-get-started.md").

- AWS account with access to the following AWS services:
  - Amazon S3 including S3 Tables
  - IAM
  - Amazon SageMaker Unified Studio
  - AWS Lake Formation and AWS Glue Data Catalog
  - AWS Glue

- [Create a user with administrative access](../../../sagemaker-unified-studio/latest/adminguide/setting-up.md#create-an-admin "../../../sagemaker-unified-studio/latest/adminguide/setting-up.md#create-an-admin").
- Have access to an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that is a Lake Formation data lake administrator.
  For instructions, refer to [Create a data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin").
- [Enable IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the same AWS Region where you want
  to create your Amazon SageMaker Unified Studio domain. Set up your identity provider (IdP) and synchronize identities and groups with [IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/").
  For more information, refer to [IAM Identity Center Identity source tutorials](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").
