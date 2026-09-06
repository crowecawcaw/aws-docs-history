

# Set up projects within an Identity Center-based domain
<a name="setup-projects-idc-based-domains"></a>

Projects in IAM-based domains provide isolated environments for data analytics and AI/ML development work. Each project has one IAM role for accessing data and resources, IAM and SSO credentials for login, and storage configurations. These configurations determine what resources and data project members can access from within the project. All members of a project within an IAM-based domain have the same access to data and compute. This access is managed through the execution IAM role for the project.

Projects within IAM-based domains require a project member and an Execution IAM role:
+ **Project member** — An IAM role or user that provides access to the Amazon SageMaker Unified Studio project. For IAM, the role or user must have the [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) managed policy attached, or equivalent permissions through another policy. Log in to Amazon SageMaker Unified Studio to view the projects that you have access to.
+ **Execution IAM role** — Defines which AWS analytics, AI, and ML service data the project can access. This role determines available data and resources in the portal. Amazon SageMaker Unified Studio assumes this role to make service calls on behalf of project users. The execution IAM role requires the [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html) managed policy (or equivalent permissions) and a trust policy that allows Amazon SageMaker Unified Studio and related AWS services to assume the role.

## Preparing IAM roles
<a name="preparing-iam-roles-idc"></a>

**Project Members**
+ For IAM role or user project members, [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) must be attached or have the same permissions added through another policy.

**Execution IAM role**
+ When Amazon SageMaker Unified Studio creates this role for you, this policy will be attached, [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html).
+ When you provide your own role, [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) must be attached. An inline policy is needed to allow this role to pass itself to other services. A trust policy is needed to allow Amazon SageMaker Unified Studio and related services to assume this execution IAM role.
+ During project creation, the Amazon SageMaker Unified Studio service creates the project IAM role as a group profile and adds the group as a project member. An IAM role session user profile is created for the project IAM role. Any logic that depends on the project role being present as a user profile must be updated to handle its presence as a group profile. For more information about user profiles, see [Managing users in Amazon SageMaker Unified Studio](user-management.md).

![Create a project in Amazon SageMaker Unified Studio](http://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/images/AdminPortal/ProjectDetail.png)


To create a project, complete the following procedure:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose **Create project**.

1. Enter a project name and description, and then choose **Next**.

1. Select the Region.

1. For **Execution role**, choose either **Auto-create a new role with permissions** or **Use an existing role**.

1. For **Storage**, choose either to create a new Amazon S3 bucket or use an existing Amazon S3 bucket, and then choose **Next**.

1. Add members to your project. Choose IAM or single sign-on users to add as members. You can assign up to 8 members at a time. You can add more members after the project is created.

1. For each member, assign a **Designation**.

1. Choose **Create**.

**Note**  
Projects created through the domain administration portal for Identity Center-based domains do not allow you to specify a project profile. The default project profile will be used with access to Notebooks, Data Analytics and AI/ML capabilities.