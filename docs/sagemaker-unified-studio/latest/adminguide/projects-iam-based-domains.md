# Projects in IAM-based domains

Projects in IAM-based domains provide isolated environments for data analytics and AI/ML
development work. Each project has one IAM role for login, one IAM role for accessing data
and resources, and storage configurations that determine what resources and data project
members can access from within the project. All members for a project within an IAM-based
domain have the same access to data and compute, this is managed through the execution IAM
role for the project.

Projects can be created in the following ways:

1. The Amazon SageMaker Unified Studio admin creates the project on behalf of users from the Domain
   administration page.
2. The Amazon SageMaker Unified Studio admin prepares IAM roles for self-setup of projects created
   directly from AWS services - Amazon Athena, Amazon S3 Tables, and
   Amazon Redshift.
   Projects within IAM-based domains require two IAM roles:

- **Member IAM role or user** – Authenticates users and
  provides access to the Amazon SageMaker Unified Studio project. This role or user must have the
  SageMakerStudioUserIAMConsolePolicy managed policy attached, or equivalent permissions
  through another policy. Use this role to access your assigned project from the
  Amazon SageMaker Unified Studio interface.
- **Execution IAM role** – Defines which AWS analytics,
  AI, and ML service data the project can access. This role determines available data and
  resources in the portal. Amazon SageMaker Unified Studio assumes this role to make service calls on behalf
  of project users. The execution IAM role requires the
  SageMakerStudioUserIAMDefaultExecutionPolicy managed policy (or equivalent permissions)
  and a trust policy that allows Amazon SageMaker Unified Studio and related AWS services to assume the
  role.

###### Note

The Execution IAM role can be the same IAM role as the Member IAM role. Both roles
require specific policy attachments and trust relationships to function correctly within
the IAM-based domain architecture. The system validates these permissions during setup and
provides guidance for any missing configurations.
