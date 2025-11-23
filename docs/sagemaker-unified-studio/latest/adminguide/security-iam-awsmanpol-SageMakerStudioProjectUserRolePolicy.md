# AWS

policy: SageMakerStudioProjectUserRolePolicy

Amazon SageMaker Unified Studio creates IAM roles for projects users to perform data analytics, artificial
intelligence, and machine learning actions, and uses this policy when creating these
roles to define the permissions.

This is the main policy for the SageMakerUnifiedStudioProjectRole role. The
SageMakerStudioProjectUserRolePolicy policy is created as part of the Tooling
environment blueprint. This policy grants read and write access for Amazon SageMaker Unified Studio users to
services such as Amazon SageMaker, AWS Glue, Amazon S3, AWS Lake Formation, Amazon
Redshift, Amazon Athena, Amazon Q, Amazon EMR. The policy also gives read and write
permissions to some infrastructure resources that are required to use these services
such as network interfaces, AWS KMS keys, AWS CodeCommit, and AWS Secrets Manager.

An administrator can disable certain permissions in this policy by tagging the role to
which the policy is attached to. The tag EnableGlueSparkWorkloads=false disables all
Glue Spark workloads related permissions. The tag EnableGenAIStudio=false disables all
Generative AI Studio related permissions.

###### Note

You can't create new projects with AWS CodeCommit. Existing projects that were
created using CodeCommit will continue to work.

- Amazon SageMaker permissions are required for users to use the Amazon
  SageMaker Domain and Spaces provisioned by default by the Tooling
  blueprint.
- AWS Glue permissions are required for users to use the default AWS Glue
  Connection and create AWS Glue Sessions.
- Amazon S3 permissions are required for users to access the project's Amazon S3
  bucket.
- AWS Lake Formation permissions are required for users to access underlying
  data in Amazon S3.
- Amazon Redshift permissions are required for users to perform SQL queries
  against Amazon Redshift, and to allow access to the project's Amazon Redshift
  clusters.
- Amazon Athena permissions are required for users to use the provisioned Amazon
  Athena workgroup and to perform SQL queries.
- Amazon Q permissions are required for users to interact with Amazon Q within
  Amazon SageMaker Unified Studio.
- Amazon EMR permissions are required for users to create and access Amazon EMR
  clusters.
- AWS CodeCommit permissions are required for users to use the default Git
  repository, and perform operations such as committing changes.
- AWS Secrets Manager permissions are required for accessing the secret for
  various services, such as Amazon Redshift, AWS Glue federated data
  connections, and Amazon Bedrock.
- Amazon Bedrock permissions are required to allow users access to Amazon
  Bedrock IDE, a development experience in Amazon SageMaker Unified Studio that
  lets you easily discover Amazon Bedrock models and build generative AI apps that
  use Amazon Bedrock models and features.
- AWS KMS permissions are required to support customer managed keys. Resources provisioned
  by Amazon SageMaker Unified Studio can be encrypted with your customer managed key.
  To view the permissions for this policy, see [SageMakerStudioProjectUserRolePolicy](../../../aws-managed-policy/latest/reference/SageMakerStudioProjectUserRolePolicy.md "../../../aws-managed-policy/latest/reference/SageMakerStudioProjectUserRolePolicy.md") in the _AWS
  Managed Policy Reference_.

###### Note

Amazon SageMaker Unified Studio creates IAM roles for project users to perform data analytics, AI, and
ML actions. You can attach the SageMakerStudioProjectUserRolePolicy managed policy as
your user role policy or you can create and attach your own user role policy. Using
your own policy provides more granular control over permissions but requires
knowledge of IAM policy configuration. The IAM policy must include all necessary
permissions required for the service to function properly.
