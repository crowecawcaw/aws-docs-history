# Deleting a project

You can delete a project by using the Rekognition console or by calling the [DeleteProject](../APIReference/API_DeleteProject.md "../APIReference/API_DeleteProject.md") API.
To delete a project, you must first delete each of the associated adapters. A deleted project or model can't be undeleted.

To delete a project with the AWS console:

- Sign into the Rekognition Console.
- Click on **Custom Moderation**.
- You must delete each adapter associated with your project before you can
  delete the project itself. Delete any adapters associated with the project
  by selecting the adapter and then selecting **Delete**.
- Select the project and then select the **Delete** button.
  To delete a project with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and the AWS SDKs. For
   more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to delete a project:

CLI

```

aws rekognition delete-project
  --project-arn `project_arn` \
  --profile `profile-name`

```
