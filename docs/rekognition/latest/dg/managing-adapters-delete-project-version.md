# Deleting a project

version

You can delete an Rekognition adapter associated with a project using the [DeleteProjectVersion](../APIReference/API_DeleteProjectVersion.md "../APIReference/API_DeleteProjectVersion.md") operation. You can't delete an adapter if it's
running or if it's training. To check the status of an adapter, call the
DescribeProjectVersions operation and check the Status field returned by it. To
stop a running adapter call StopProjectVersion. If the model is training, wait
until it finishes training to delete it. You must delete each adapter associated
with your project before you can delete the project itself.

To delete a project version with the Rekognition console:

- Sign into the Rekognition Console
- Click on Custom Moderation
- From the Projects tab you can see all your projects and associated
  adapters. Select an adapter and then select **Delete**.
  To delete a project version with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and
   the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to delete a project version:

CLI

```

# Request
aws rekognition delete-project-version
  --project-version-arn `model_arn` \
  --profile `profile-name`

```
