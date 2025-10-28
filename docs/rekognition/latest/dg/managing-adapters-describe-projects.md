# Describing projects

You can use the [DescribeProjects](../APIReference/API_DescribeProjects.md "../APIReference/API_DescribeProjects.md") API to get information about your projects,
including information about all the adapters associated with a project.

To describe projects with the AWS CLI and SDK:

1. If you haven't already done so, install and configure the AWS CLI and
   the AWS SDKs. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md") .
2. Use the following code to describe a project:

CLI

```

# Request
# Getting CONTENT_MODERATION project details
aws rekognition describe-projects \
    --features CONTENT_MODERATION
    --profile `profile-name`

```
