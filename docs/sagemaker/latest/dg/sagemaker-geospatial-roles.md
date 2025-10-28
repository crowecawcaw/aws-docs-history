# SageMaker geospatial capabilities roles

As a managed service, Amazon SageMaker geospatial capabilities performs operations on your behalf on the
AWS hardware that is managed by SageMaker AI. Use AWS Identity and Access Management to grant users, groups, and roles
access to SageMaker geospatial.

An

IAM Administrator can grant these permissions to user, group, or role
using the AWS Management Console, AWS CLI, or one of the AWS SDKs.

###### To use SageMaker geospatial you need the following IAM permissions.

1. **An SageMaker AI execution role.**

To use the SageMaker geospatial specific API operations your SageMaker AI execution
role
must include the SageMaker geospatial
service
principal, `sagemaker-geospatial.amazonaws.com` in the execution role's
trust policy. This allows the SageMaker AI
execution role to perform actions in your AWS account on your behalf. 2. **A user, group, or role that has access Amazon SageMaker Studio Classic and SageMaker geospatial**

To get started with SageMaker geospatial you can use the AWS managed policy:
`AmazonSageMakerGeospatialFullAccess`. This grants will grant a user, group,
or role full access to SageMaker geospatial. To see the policy and learn more about which actions,
resources, and conditions are available, see [AWS managed policy:
AmazonSageMakerFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSageMakerFullAccess").

To get started with Studio Classic and creating a Amazon SageMaker AI domain, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
Use the following topics to create a new SageMaker AI execution role, update an existing SageMaker AI
execution role, and learn how to manage permissions using SageMaker geospatial specific IAM actions,
resources, and conditions.

###### Topics

- [Creating an new SageMaker AI
  execution role](sagemaker-geospatial-roles-create-execution-role.md "sagemaker-geospatial-roles-create-execution-role.md")
- [Adding

the SageMaker geospatial service principal to an existing SageMaker AI execution
role](sagemaker-geospatial-roles-pass-role.md "sagemaker-geospatial-roles-pass-role.md")

- [StartEarthObservationJob
  API: Execution role permissions](sagemaker-roles-start-eoj-perms.md "sagemaker-roles-start-eoj-perms.md")
- [StartVectorEnrichmentJob
  API: Execution role permissions](sagemaker-roles-start-vej-perms.md "sagemaker-roles-start-vej-perms.md")
- [ExportEarthObservationJob API: Execution role permissions](sagemaker-roles-export-eoj-perms.md "sagemaker-roles-export-eoj-perms.md")
- [ExportVectorEnrichmentJob
  API: Execution Role Permissions](sagemaker-roles-export-vej-perms.md "sagemaker-roles-export-vej-perms.md")
