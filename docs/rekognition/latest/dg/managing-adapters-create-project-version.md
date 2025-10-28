# Creating a project

version

You can train an adapter for deployment by using the [CreateProjectVersion](../APIReference/API_CreateProjectVersion.md "../APIReference/API_CreateProjectVersion.md") operation.
CreateProjectVersion first creates a new version of an adapter associated with a project and
then begins training the adapter. The response from CreateProjectVersion is an
Amazon Resource Name (ARN) for the version of the model. Training takes a while to complete. You
can get the current status by calling DescribeProjectVersions. When training a model,
Rekognition uses the training and test datasets associated with the project.
You create datasets using the console. For more information, see the section on datasets.

To create a project version with the Rekognition console:

- Sign into the AWS Rekognition Console
- Click on Custom Moderation
- Select a project.
- On the “Project detail” page, choose
  **Create adapter**
- On the “Create a project" page, fill in the required details
  for Project Details, Training images, and Testing images, then
  select
  **Create project**
  .
- On the “Assign labels to images” page, add labels to your
  images and when finished select
  **Start training**
  To create a project version with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and
   the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to create a project version:

CLI

```

# Request
aws rekognition create-project-version \
 --project-arn `project-arn` \
 --training-data '{Assets=[GroundTruthManifest={S3Object="`amzn-s3-demo-source-bucket`",Name="`manifest.json`"}]}' \
 --output-config S3Bucket=`amzn-s3-demo-destination-bucket`,S3KeyPrefix=`my-results` \
 --feature-config "ContentModeration={ConfidenceThreshold=70}"
 --profile `profile-name`

```
