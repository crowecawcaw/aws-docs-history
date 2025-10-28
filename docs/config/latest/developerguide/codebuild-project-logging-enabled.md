# codebuild-project-logging-enabled

Checks if an AWS CodeBuild project environment has at least one log option enabled. The rule is NON_COMPLIANT if the status of all present log configurations is set to 'DISABLED'.

**Identifier:** CODEBUILD_PROJECT_LOGGING_ENABLED

**Resource Types:** AWS::CodeBuild::Project

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

s3BucketNames (Optional)
Type: String

Comma-separated list of Amazon S3 bucket names that logs should be sent to if S3 logs are configured.

cloudWatchGroupNames (Optional)
Type: String

Comma-separated list of Amazon CloudWatch log group names that logs should be be sent to if CloudWatch logs are configured.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
