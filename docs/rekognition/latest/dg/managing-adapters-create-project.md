# Creating a project

With the [CreateProject](../APIReference/API_CreateProject.md "../APIReference/API_CreateProject.md") operation you can create a project that will hold an adapter
for Rekognition’s label detection operations. A project is a group of resources and
in the case of label detection operations like DetectModerationLabels, a project
allows you to store adapters that you can use to customize the base Rekognition model.
When invoking CreateProject, you provide the name of the project you want to create to the
ProjectName argument.

To create a project with the AWS console:

- Sign into the Rekognition Console
- Click on **Custom Moderation**
- Choose **Create Project**
- Select either **Create a New Project** or
  **Add to an existing project**
- Add a **Project name**
- Add an **Adapter name**
- Add a description if desired
- Choose how you want to import your training images: Manifest file,
  from S3 bucket, or from your computer
- Choose if you want to Autosplit your training data or import a
  manifest file
- Select whether or not you want the project to automatically
  update
- Click **Create project**
  To create a project with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the
   AWS CLI and the AWS SDKs. For more information,
   see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to create a project:

CLI

```

# Request
# Creating Content Moderation Project
aws rekognition create-project \
    --project-name "`project-name`" \
    --feature CONTENT_MODERATION \
    --auto-update ENABLED
    --profile `profile-name`

```
