# AWS policy:

SageMakerStudioProjectUserRolePermissionsBoundary

Amazon SageMaker Unified Studio creates IAM roles for Projects users to perform data analytics, artificial
intelligence, and machine learning actions, and uses this policy when creating these
roles to define the boundary of their permissions.

This policy is a permissions boundary. A permissions boundary sets the maximum
permissions that an identity-based policy can grant to an IAM entity. You should not use
and attach Amazon SageMaker Unified Studio permissions boundary policies on your own. Amazon SageMaker Unified Studio permissions
boundary policies should only be attached to Amazon SageMaker Unified Studio managed roles.

When you create a project via the Amazon SageMaker Unified Studio, it applies this permissions boundary to
the IAM roles that are provisioned during project creation. The permissions boundary
limits the scope of the roles that Amazon SageMaker Unified Studio creates and any roles that you add.

Amazon SageMaker Unified Studio uses the SageMakerStudioProjectUserRolePermissionsBoundary managed policy to
limit the provisioned IAM principal to which it is attached. The principals might take
the form of the user roles that Amazon SageMaker Unified Studiocan assume on behalf of interactive enterprise
users or analytic services (AWS Glue, for example), and then conduct actions to
process data such as reading and writing from Amazon S3 or running AWS Glue
crawler.

The SageMakerStudioProjectUserRolePermissionsBoundary policy grants read and write
access for Amazon SageMaker Unified Studioto services such as Amazon SageMaker, AWS Glue, Amazon S3, AWS
Lake Formation, Amazon Redshift, Amazon Athena, Amazon Q, Amazon EMR. The policy also
gives read and write permissions to some infrastructure resources that are required to
use these services such as network interfaces, AWS KMS keys, AWS CodeCommit, and
AWS Secrets Manager.

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
- Amazon EMR permissions are required for users to create and access EMR
  clusters. AWS KMS permissions are required to use CMK in the various services
  integrated with Amazon SageMaker Unified Studio.
- AWS CodeCommit permissions are required for users to use the default Git
  repository, and perform operations such as committing changes.
- AWS Secrets Manager permissions are required for accessing the secret for
  various services, such as Amazon Redshift, AWS Glue federated data
  connections, and Amazon Bedrock.
- Amazon Bedrock permissions are required to allow users access to Amazon
  Bedrock IDE, a development experience in Amazon SageMaker Unified Studio that
  lets you easily discover Amazon Bedrock models and build generative AI apps that
  use Amazon Bedrock models and features.
  To view the permissions for this policy, see [SageMakerStudioProjectUserRolePermissionsBoundary](../../../aws-managed-policy/latest/reference/SageMakerStudioProjectUserRolePermissionsBoundary.md "../../../aws-managed-policy/latest/reference/SageMakerStudioProjectUserRolePermissionsBoundary.md") in the _AWS Managed Policy Reference_.
