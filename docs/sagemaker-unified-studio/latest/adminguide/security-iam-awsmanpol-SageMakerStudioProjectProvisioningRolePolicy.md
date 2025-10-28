# AWS policy: SageMakerStudioProjectProvisioningRolePolicy

Amazon SageMaker Unified Studio uses this policy to provision and manage resources in your account.

This is the default policy for the AmazonSageMakerProvisioning-<domainAccountId>
service role. This role is used by Amazon SageMaker Unified Studio to manage resources in your account created
as part of projects lifecycle. This role provides access to manage resources for all
services used in Amazon SageMaker Unified Studio, including Amazon SageMaker, AWS Glue, Amazon S3, AWS
Lake Formation, Amazon Redshift, Amazon Athena, Amazon Q, Amazon EMR, Amazon Bedrock,
AWS CodeCommit, and AWS IAM.

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

- Amazon SageMaker permissions are required to manage the SageMaker Domain and
  Spaces provisioned by default by the Tooling blueprint.
- AWS Glue permissions are required to manage AWS Glue Connections, AWS
  Glue Catalog, and AWS Glue Databases.
- Amazon S3 permissions are required to access S3 objects to provision Amazon
  Bedrock resources, federated AWS Glue connection, and to create the staging
  bucket for Amazon Redshift.
- AWS Lake Formation permissions are required to manage grants on AWS Glue
  Data Catalog.
- Amazon Redshift permissions are required to provision Amazon Redshift
  Serverless workgroup and namespace.
- Amazon Athena permissions are required to provision Amazon Athena workgroup
  and Amazon Athena data catalog for federated connection.
- Amazon EMR permissions are required to provision Amazon EMR on EC2
  clusters.
- AWS KMS permissions are required to use CMK in the various services
  integrated with Amazon SageMaker Unified Studio.
- AWS CodeCommit permissions are required to provision the default Git
  repository.
- AWS Secrets Manager permissions are required to provision the secret for
  various services, such as Amazon Redshift, AWS Glue federated data
  connections, and Amazon Bedrock.
- AWS IAM permissions are required to provision the roles that will be used by
  users of Amazon SageMaker Unified Studio.
- Amazon Bedrock permissions are required to provision Amazon Bedrock IDE
  related resources to enable discovery of Amazon Bedrock models and build
  generative AI apps that use Amazon Bedrock models and features.
  To view the permissions for this policy, see [SageMakerStudioProjectProvisioningRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioProjectProvisioningRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioProjectProvisioningRolePolicy.md") in the _AWS Managed Policy Reference_.
