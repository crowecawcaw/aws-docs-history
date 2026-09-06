

# Edit project configuration
<a name="edit-project-configuration-iam-based"></a>

You can edit the project name and description, or modify the project members to reflect changes in business context or project scope.

## Edit project details
<a name="edit-project-iam-based"></a>

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name that you want to edit from the Projects list.

1. On the project details page, choose **Edit**.

1. In the **Edit Project** dialog, modify the **Project name** and **Description**.

1. Choose **Save** to apply your changes.

## Edit project members
<a name="edit-project-members-iam-based"></a>

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name that you want to edit from the Projects list.

1. On the project details page, choose the **Members** tab.

1. Choose **Add members**.

1. For **Type**, select IAM or SSO.

1. For **Members**, select the user to add. If you are adding IAM roles or users, the role or user must have the [SageMakerStudioUserIAMConsolePolicy](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.html) managed policy attached.

1. Choose **Add** to apply your changes.

Your changes are applied immediately. If you added project members, the new members have access to the project.