# Set up projects within an IAM-based

domain

To create a project within an IAM-based domain you assign Member IAM role or user and
Execution IAM role, configure execution permissions for the execution role, and set up
storage options. By default, projects can access resources within the domain's AWS
account. You can configure the project execution IAM role to access data and resources
across AWS accounts and regions.

## Preparing IAM roles

**Member IAM role:**

- [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") must be attached or have the same
  permissions added via another policy.

**Execution IAM role:**

- When Amazon SageMaker Unified Studio creates this role for you, this policy will be attached,
  [SageMakerStudioUserIAMDefaultExecutionPolicy](security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMDefaultExecutionPolicy.md").
- When you provide your own role, [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") must be
  attached. An inline policy is needed to allow this role to pass itself to other
  services. A trust policy is needed to allow Amazon SageMaker Unified Studio and related services to
  assume this execution IAM role.

## Create new project from domain

administration page

1. From the domain administration page, choose Projects in the left navigation
   pane.
2. Choose Create project. This will open up the create project panel.
3. Give the project a name and choose Next.
4. Select a Member role or user.
5. Select an Execution role, choose either to Auto-create a new role with
   permissions or Use an existing role.
6. Choose Create.
7. You should see a Creating project notification.
8. Once the project is successfully created, you should see an entry in the
   projects table with the project name.

## Prepare other IAM roles for other users

to self-service setup projects

You can configure other IAM roles in your account to self-setup their Amazon SageMaker Unified Studio
project within your IAM-based domain. You must add additional permissions and policies
to the existing IAM roles to allow them to setup their own project using the Member IAM
role for login and Execution IAM role for accessing data and resources within the
project. This enables users from AWS console to create projects using these roles from
AWS Services - Amazon Athena, Amazon S3 Tables, and Amazon
Redshift.

**Member IAM role:**

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
