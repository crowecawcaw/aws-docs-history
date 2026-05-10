# Edit project configuration

You can edit the project name and description, or modify the project members to
reflect changes in business context or project scope.

## Edit project details

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. Choose the project name that you want to edit from the Projects list.
3. On the project details page, choose **Edit**.
4. In the **Edit Project** dialog, modify the
   **Project name** and
   **Description**.
5. Choose **Save** to apply your changes.

## Edit project members

1. From the domain administration page, choose **Projects** in the
   left navigation pane.
2. Choose the project name that you want to edit from the Projects list.
3. On the project details page, choose the **Members** tab.
4. Choose **Add members**.
5. For **Type**, select IAM or SSO.
6. For **Members**, select the user to add. If you are adding IAM
   roles or users, the role or user must have the [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") managed policy attached.
7. Choose **Add** to apply your changes.

Your changes are applied immediately. If you added project members, the new members
have access to the project.
