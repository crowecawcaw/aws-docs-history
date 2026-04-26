# Workflow environments in Amazon SageMaker Unified Studio

Use a shared workflow environment to share workflows with other project members.
Workflow environments must be created by project owners.
To update or delete a workflow environment, you must be an owner of the project that the workflow environment is in.
After a workflow environment has been created by a project owner, any project member can sync their files to share them in the environment.

Only one workflow environment can exist in a project at a time.

- [Create a workflow environment](#create-workflow-environment "#create-workflow-environment")
- [Update a workflow environment](#update-workflow-environment "#update-workflow-environment")
- [Delete a workflow environment](#delete-workflow-environment "#delete-workflow-environment")

## Create a workflow environment

To create a workflow environment, you must be an owner of the project that you want to create a workflow environment in.

To create a workflow environment, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that was created with the **Data analytics and AI-ML model development** project profile.
   To do this, choose a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Compute**.
4. On the **Workflow environments** tab, confirm that there are no workflow environments in the project yet. Then choose **Create**.
5. In the **Create workflow environment** window, review the parameters of the workflow environment. These are determined by your admin. If you want any of these parameters to change, contact your admin.
6. Choose **Create workflow environment**.

###### Note

Workflow environment creation takes several minutes to complete.

## Update a workflow environment

To update a workflow environment, you must be an owner of the project that you want to update a workflow environment in.

To update a workflow environment, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the workflow environment that you want to update.
   To do this, choose a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Compute**.
4. On the **Workflow environments** tab, expand the **Actions** menu and choose **Update**.
5. Choose **Update workflow environment**.

###### Note

Updating a workflow environment takes several minutes to complete.

## Delete a workflow environment

To delete a workflow environment, you must be an owner of the project that contains the workflow environment that you want to delete.

To delete a workflow environment, complete the following steps:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the workflow environment that you want to delete.
   To do this, choose a project from the project selector dropdown at the top of the page.
3. In the left navigation pane, choose **Compute**.
4. On the **Workflow environments** tab, expand the **Actions** menu and choose **Delete**.
5. Confirm the action by typing `confirm`, then choose **Delete workflow environment**.

###### Note

Deleting a workflow environment takes several minutes to complete.
