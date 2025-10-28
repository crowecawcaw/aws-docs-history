# Describing a project

version

You can list and describe adapters associated with a project by using the [DescribeProjectVersions](../APIReference/API_DescribeProjectVersions.md "../APIReference/API_DescribeProjectVersions.md") operation.
You can specify up to 10 model versions in ProjectVersionArns. If you don't specify a value, descriptions
for all model versions in the project are returned.

To describe a project version with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and
   the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to describe a project version:

CLI

```

aws rekognition describe-project-versions
  --project-arn `project_arn` \
  --version-names `[versions]`

```
