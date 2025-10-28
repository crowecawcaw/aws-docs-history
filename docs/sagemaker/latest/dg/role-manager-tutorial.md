# Using the role manager (console)

You can use the Amazon SageMaker Role Manager from the following locations on the left-hand navigation of the Amazon SageMaker AI console:

- **Getting started** – Quickly add permissions policies for your users.
- **domains** – Add permissions policies for users within a Amazon SageMaker AI domain.
- **Notebooks** – Add least permissions for users who create and run notebooks.
- **Training** – Add least permissions for users who create and manage training jobs.
- **Inference** – Add least permissions for users who deploy and manage models for inference.
  You can use the following are procedures to start the process of creating a role from different locations in the SageMaker AI console.

If you're using SageMaker AI for the first time, we recommend creating a role from the **Getting started** section.

To create a role using Amazon SageMaker Role Manager, do the following.

1. Open the Amazon SageMaker AI console.
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **Role manager**.
4. Choose **Create a role**.
   You can create a role using Amazon SageMaker Role Manager when you start the process of creating a Amazon SageMaker AI domain.

To create a role using Amazon SageMaker Role Manager, do the following.

1. Open the Amazon SageMaker AI console.
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. Choose **Create domain**.
5. Choose **Create role using the role creation wizard**.
   You can create a role using Amazon SageMaker Role Manager when you start the process of creating a notebook.

To create a role using Amazon SageMaker Role Manager, do the following.

1. Open the Amazon SageMaker AI console.
2. On the left-hand navigation, select **Notebook**.
3. Choose **Notebook instances**.
4. Choose **Create notebook instance**.
5. Choose **Create role using the role creation wizard**.
   You can create a role using Amazon SageMaker Role Manager when you start the process of creating a training job.

To create a role using Amazon SageMaker Role Manager, do the following.

1. Open the Amazon SageMaker AI console.
2. On the left-hand navigation, choose **Training**.
3. Select **Training jobs**.
4. Choose **Create training job**.
5. Choose **Create role using the role creation wizard**.
   You can create a role using Amazon SageMaker Role Manager when you start the process of deploying a model for inference.

To create a role using Amazon SageMaker Role Manager, do the following.

1. Open the Amazon SageMaker AI console.
2. On the left-hand navigation, choose **Inference**.
3. Select **Models**.
4. Choose **Create model**.
5. Choose **Create role using the role creation wizard**.
   After you've completed one of the preceding procedures, use the information in the following sections to help you create the role.

## Prerequisites

To use Amazon SageMaker Role Manager, you must have permission to create an IAM
role. This permission is usually available to ML administrators and roles with
least-privilege permissions for ML practitioners.

You can temporarily assume an IAM role in the AWS Management Console by [switching roles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md"). For more information about methods for using roles,
see [Using IAM roles](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md") in the _IAM User
Guide_.

## Step 1. Enter role information

Provide a name to use as the unique suffix of your new SageMaker AI role. By default, the
prefix `"sagemaker-"` is added to every role name for easier search in
the IAM console. For example, if you name your role `test-123` during
role creation, your role shows up as `sagemaker-test-123` in the IAM
console. You can optionally add a description of your role to provide additional
details.

Then, choose from one of the available personas to get suggested permissions for
personas such as data scientists, data engineers, or machine learning operations
(MLOps) engineers. For information on available personas and their suggested
permissions, see [Persona reference](role-manager-personas.md "role-manager-personas.md"). To create a role without any suggested
permissions to guide you, choose **Custom Role Settings**.

###### Note

We recommend that you first use the role manager to create a SageMaker AI Compute
Role so that SageMaker AI compute resources have the ability to perform tasks such
as training and inference. Use the SageMaker AI Compute Role persona to create this
role with the role manager. After creating a SageMaker AI Compute Role, take note
of its ARN for future use.

### Network and encryption conditions

We recommend that you activate VPC customization to use VPC configurations,
subnets, and security groups with IAM policies associated with your new role.
When VPC customization is activated, IAM policies for ML activities that
interact with VPC resources are scoped down for least-privilege access. VPC
customization is not activated by default. For more details on recommended
networking architecture, see [Networking architecture](../../../whitepapers/latest/build-secure-enterprise-ml-platform/networking-architecture.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/networking-architecture.md") in the _AWS
Technical Guide_.

You can also use a KMS key to encrypt, decrypt, and re-encrypt data for
regulated workloads with highly sensitive data. When AWS KMS customization is
activated, IAM policies for ML activities that support custom encryption keys
are scoped down for least-privilege access. For more information, see [Encryption with AWS KMS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/encryption-with-kms.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/encryption-with-kms.md") in the _AWS
Technical Guide_.

## Step 2. Configure ML activities

Each Amazon SageMaker Role Manager ML activity includes suggested IAM permissions
to provide access to relevant AWS resources. Some ML activities require that you add
service role ARNs to complete setup. For information on predefined ML
activities and their permissions, see [ML activity reference](role-manager-ml-activities.md "role-manager-ml-activities.md"). For information on adding service roles, see [Service roles](#role-manager-tutorial-configure-ml-activities-service-roles "#role-manager-tutorial-configure-ml-activities-service-roles").

Based on the chosen persona, certain ML activities are already selected. You can
deselect any suggested ML activities or select additional activities to create your
own role. If you selected the Custom Role Settings persona, then no ML activities
are preselected in this step.

You can add any additional AWS or customer-managed IAM policies to your role in
[Step 3: Add additional policies and tags](#role-manager-tutorial-add-policies-and-tags "#role-manager-tutorial-add-policies-and-tags").

### Service roles

Some AWS services require a service role to perform actions on your behalf. If
the ML activity that you selected requires you to pass a service role, then you
must provide the ARN for that service role.

You can either create a new service role or use an existing one, such as a
service role created with the SageMaker AI Compute Role persona. You can find the
ARN of an existing role by selecting the role name in the Roles section of the
[IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/"). To learn more about service
roles, see [Creating a role for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

## Step 3: Add additional policies and tags

You can add any existing AWS or customer-managed IAM policies to your new
role. For information on existing SageMaker AI policies, see [AWS Managed Policies for
Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md"). You can also check your existing policies in the
**Roles** section of the [IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/").

Optionally, use tag-based policy conditions to assign metadata information to
categorize and manage AWS resources. Each tag is represented by a key-value pair.
For more information, see [Controlling access to AWS
resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

## Review role

Take the time to review all of the information associated with your new role.
Choose **Previous** to go back and edit any of the information.
When you are ready to create your role, choose **Create role**.
This generates a role with permissions for your selected ML activities. You can view
your new role in the **Roles** section of the [IAM console](https://console.aws.amazon.com/iamv2/ "https://console.aws.amazon.com/iamv2/").
