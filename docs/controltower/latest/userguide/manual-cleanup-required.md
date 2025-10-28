# Manual cleanup tasks required after decommissioning

This section lists manual cleanup tasks you must perform after the initial decommissioning step.

- You must specify different email addresses for the Log archive and Audit
  accounts if you create a new landing zone after decommissioning one, or follow
  the procedure for bringing your own existing Log archive or Audit
  accounts.
- The CloudWatch Logs log group, `aws-controltower/CloudTrailLogs`, must be
  deleted manually before you set up another landing zone.
- The two Amazon S3 buckets with reserved names for logs must be removed, or renamed,
  manually.
- You must delete, or rename, the existing **Security** and
  **Sandbox** organizational units manually.

###### Note

Before you can delete the AWS Control Tower **Security OU**
organization, you must first delete the logging and audit accounts, but not
the management account. To delete these accounts, you must [When to sign in as a root user](root-login.md "root-login.md") to the audit account
and to the logging account and delete them individually.

- You may wish to delete the AWS IAM Identity Center (IAM Identity Center) configuration for AWS Control Tower
  manually, but you can proceed with the existing IAM Identity Center configuration.
- You may wish to remove the VPC created by AWS Control Tower, and remove the associated
  AWS CloudFormation stack set.
- Before you can set up a new landing zone in a new AWS Region, you must
  follow these additional steps.
  - Enter the following command through the CLI:

  ```
  aws organizations disable-aws-service-access --service-principal controltower.amazonaws.com

  ```

  - Delete the remaining managed rule, called
    `AWSControlTowerManagedRule`, from the shared and member
    accounts for all governed Regions.
    `AWSControlTowerManagedRule` is an Amazon EventBridge rule.
