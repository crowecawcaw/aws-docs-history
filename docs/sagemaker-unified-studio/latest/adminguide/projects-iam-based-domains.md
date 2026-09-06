

# Projects in IAM-based domains
<a name="projects-iam-based-domains"></a>

Projects in IAM-based domains provide isolated environments for data analytics and AI/ML development work. Each project has one IAM role for accessing data and resources, IAM and SSO credentials for login, and storage configurations. These configurations determine what resources and data project members can access from within the project. All members of a project within an IAM-based domain have the same access to data and compute. This access is managed through the execution IAM role for the project.

Projects can be created in the following ways:

1. The Amazon SageMaker Unified Studio admin creates the project on behalf of users from the Domain administration page.

1. The Amazon SageMaker Unified Studio admin prepares IAM roles for self-setup of projects created directly from AWS services - Amazon Athena, Amazon S3 Tables, and Amazon Redshift.

Projects within IAM-based domains require a project member and an Execution IAM role:
+ **Project member** – An IAM role or user that provides access to the Amazon SageMaker Unified Studio project. For IAM, the role or user must have the SageMakerStudioUserIAMConsolePolicy managed policy attached, or equivalent permissions through another policy. Log in to Amazon SageMaker Unified Studio to view the projects that you have access to.
+ **Execution IAM role** – Defines which AWS analytics, AI, and ML service data the project can access. This role determines available data and resources in the portal. Amazon SageMaker Unified Studio assumes this role to make service calls on behalf of project users. The execution IAM role requires the SageMakerStudioUserIAMDefaultExecutionPolicy managed policy (or equivalent permissions) and a trust policy that allows Amazon SageMaker Unified Studio and related AWS services to assume the role.

**Note**  
The Execution IAM role can be the same IAM role as the Member IAM role. Both roles require specific policy attachments and trust relationships to function correctly within the IAM-based domain architecture. The system validates these permissions during setup and provides guidance for any missing configurations.