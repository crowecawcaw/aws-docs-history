# About AWS CodeBuild log file

entries

A trail is a configuration that enables delivery of events as log files to an S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
are not an ordered stack trace of the public API calls, so they do not appear in any
specific order.

###### Note

To protect sensitive information, the following are hidden in CodeBuild logs:

- AWS access key IDs. For more information, see
  [Managing Access Keys for IAM Users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _AWS Identity and Access Management User Guide_.
- Strings specified using the Parameter Store. For more information, see [Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-paramstore.md "../../../systems-manager/latest/userguide/systems-manager-paramstore.md") and
  [Systems Manager Parameter Store Console Walkthrough](../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console "../../../systems-manager/latest/userguide/sysman-paramstore-walk.md#sysman-paramstore-console") in the
  _Amazon EC2 Systems Manager User Guide_.
- Strings specified using AWS Secrets Manager. For more information, see
  [Key management](security-key-management.md "security-key-management.md").
  The following example shows a CloudTrail log entry that demonstrates creating a build
  project in CodeBuild.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "FederatedUser",
    "principalId": "`account-ID`:`user-name`",
    "arn": "arn:aws:sts::`account-ID`:federated-user/`user-name`",
    "accountId": "`account-ID`",
    "accessKeyId": "`access-key-ID`",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2016-09-06T17:59:10Z"
      },
      "sessionIssuer": {
        "type": "IAMUser",
        "principalId": "`access-key-ID`",
        "arn": "arn:aws:iam::`account-ID`:user/`user-name`",
        "accountId": "`account-ID`",
        "userName": "`user-name`"
      }
    }
  },
  "eventTime": "2016-09-06T17:59:11Z",
  "eventSource": "codebuild.amazonaws.com",
  "eventName": "CreateProject",
  "awsRegion": "`region-ID`",
  "sourceIPAddress": "127.0.0.1",
  "userAgent": "`user-agent`",
  "requestParameters": {
    "awsActId": "`account-ID`"
  },
  "responseElements": {
    "project": {
      "environment": {
        "image": "image-ID",
        "computeType": "BUILD_GENERAL1_SMALL",
        "type": "LINUX_CONTAINER",
        "environmentVariables": []
      },
      "name": "codebuild-demo-project",
      "description": "This is my demo project",
      "arn": "arn:aws:codebuild:`region-ID`:`account-ID`:project/codebuild-demo-project:`project-ID`",
      "encryptionKey": "arn:aws:kms:`region-ID`:`key-ID`",
      "timeoutInMinutes": 10,
      "artifacts": {
        "location": "arn:aws:s3:::codebuild-`region-ID`-`account-ID`-output-bucket",
        "type": "S3",
        "packaging": "ZIP",
        "outputName": "MyOutputArtifact.zip"
      },
      "serviceRole": "arn:aws:iam::`account-ID`:role/CodeBuildServiceRole",
      "lastModified": "Sep 6, 2016 10:59:11 AM",
      "source": {
        "type": "GITHUB",
        "location": "https://github.com/my-repo.git"
      },
      "created": "Sep 6, 2016 10:59:11 AM"
    }
  },
  "requestID": "9d32b228-745b-11e6-98bb-23b67EXAMPLE",
  "eventID": "581f7dd1-8d2e-40b0-aeee-0dbf7EXAMPLE",
  "eventType": "AwsApiCall",
  "recipientAccountId": "`account-ID`"
}

```
