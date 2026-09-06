

# Set up projects within an IAM-based domain
<a name="setup-projects-iam-based-domains"></a>

To create a project within an IAM-based domain, you assign project members (IAM or single sign-on) and an Execution IAM role, configure execution permissions, and set up storage options. By default, projects can access resources within the domain's AWS account. You can configure the project execution IAM role to access data and resources across AWS accounts and Regions.

## Preparing IAM roles
<a name="preparing-iam-roles-projects"></a>

**Project Members**
+ For IAM role or user project members, [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) must be attached or have the same permissions added through another policy.

**Execution IAM role:**
+ When Amazon SageMaker Unified Studio creates this role for you, this policy will be attached, [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html).
+ When you provide your own role, [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) must be attached. An inline policy is needed to allow this role to pass itself to other services. A trust policy is needed to allow Amazon SageMaker Unified Studio and related services to assume this execution IAM role.
+ During project creation, the Amazon SageMaker Unified Studio service creates the project IAM role as a group profile and adds the group as a project member. An IAM role session user profile is created for the project IAM role. Any logic that depends on the project role being present as a user profile must be updated to handle its presence as a group profile. For more information about user profiles, see [Managing users in Amazon SageMaker Unified Studio](user-management.md).

## Create a project from the domain administration page
<a name="create-project-domain-admin"></a>

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose **Create project**.

1. Enter a project name and description, and then choose **Next**.

1. For **Execution role**, choose either **Auto-create a new role with permissions** or **Use an existing role**.

1. For **Storage**, choose either to create a new Amazon S3 bucket or use an existing Amazon S3 bucket, and then choose **Next**.

1. Add members to your project. Choose IAM or single sign-on users to add as members. You can assign up to 8 members at a time. You can add more members after the project is created.

1. For each member, assign a **Designation**.

1. Choose **Create**.

## Prepare IAM roles and users for self-service project setup
<a name="prepare-iam-roles-self-service"></a>

You can configure IAM roles and users in your account to set up their own Amazon SageMaker Unified Studio project within your IAM-based domain. You must add permissions and policies to the existing IAM roles and users to allow them to set up their own project using the project member for login and the execution IAM role for accessing data and resources within the project. This configuration enables users to create projects from the AWS Management Console using these roles and users, or from AWS services such as Amazon Athena, Amazon S3 Tables, and Amazon Redshift.

**Project member IAM role and user:**

1. Login to the IAM role (defined in [Overview of IAM-based domains](iam-based-domains-overview.md) ) with AWS IAM administrator privileges defined in the pre-requisites.

1. Navigate to the IAM console.

1. Choose Add permission followed by Attach policy and search for the managed policy [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html). Select it to add it to your existing role.

**Execution IAM role:**

1. Login to the IAM role with AWS IAM administrator privileges defined in the pre-requisites.

1. Navigate to the IAM console.

1. Choose Add permission followed by Attach policy and search for the managed policy [SageMakerStudioUserIAMDefaultExecutionPolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.html). Select it to add it to your existing role.

1. Add the inline policy to allow this role to pass itself to other services.

1. Add a trust policy: Allow Amazon SageMaker Unified Studio and related services to assume this Execution IAM role.