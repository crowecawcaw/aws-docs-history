# Set up projects within an IAM-based domain

To create a project within an IAM-based domain, you assign project members (IAM or
single sign-on) and an Execution IAM role, configure execution permissions, and set up
storage options. By default, projects can access resources within the domain's AWS
account. You can configure the project execution IAM role to access data and resources
across AWS accounts and Regions.

## Preparing IAM roles

**Project Members**

- For IAM role or user project members, [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") must be attached or have the same
  permissions added through another policy.

**Execution IAM role:**

- When Amazon SageMaker Unified Studio creates this role for you, this policy will be attached,
  [SageMakerStudioUserIAMDefaultExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md").
- When you provide your own role, [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") must be
  attached. An inline policy is needed to allow this role to pass itself to other
  services. A trust policy is needed to allow Amazon SageMaker Unified Studio and related services to
  assume this execution IAM role.

## Create a project from the domain administration page

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. Choose **Create project**.
3. Enter a project name and description, and then choose
   **Next**.
4. For **Execution role**, choose either **Auto-create a
   new role with permissions** or **Use an existing
   role**.
5. For **Storage**, choose either to create a new Amazon S3 bucket
   or use an existing Amazon S3 bucket, and then choose
   **Next**.
6. Add members to your project. Choose IAM or single sign-on users to add as
   members. You can assign up to 8 members at a time. You can add more members after
   the project is created.
7. For each member, assign a **Designation**.
8. Choose **Create**.

## Prepare IAM roles and users for self-service project setup

You can configure IAM roles and users in your account to set up their own
Amazon SageMaker Unified Studio project within your IAM-based domain. You must add permissions and
policies to the existing IAM roles and users to allow them to set up their own project
using the project member for login and the execution IAM role for accessing data and
resources within the project. This configuration enables users to create projects from
the AWS Management Console using these roles and users, or from AWS services such as
Amazon Athena, Amazon S3 Tables, and Amazon Redshift.

**Project member IAM role and user:**

1. Login to the IAM role (defined in [Overview of IAM-based domains](iam-based-domains-overview.md "iam-based-domains-overview.md") ) with AWS IAM administrator
   privileges defined in the pre-requisites.
2. Navigate to the IAM console.
3. Choose Add permission followed by Attach policy and search for the managed
   policy [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md"). Select it to add it to your existing
   role.

**Execution IAM role:**

1. Login to the IAM role with AWS IAM administrator privileges defined in the
   pre-requisites.
2. Navigate to the IAM console.
3. Choose Add permission followed by Attach policy and search for the managed
   policy [SageMakerStudioUserIAMDefaultExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md"). Select it to add it to your
   existing role.
4. Add the inline policy to allow this role to pass itself to other
   services.
5. Add a trust policy: Allow Amazon SageMaker Unified Studio and related services to assume this
   Execution IAM role.
