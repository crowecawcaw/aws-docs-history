# Resource considerations for AWS Control Tower Account Factory for

Terraform

When you set up your landing zone using AWS Control Tower Account Factory for Terraform, several
types of AWS resources are created within your AWS accounts.

###### Search for resources

- You can use tags to search for the most updated list of AFT resources. The
  key-value pair for your search is:

```
Key: managed_by | Value: AFT
```

- For component services that do not support tags, you can locate resources with a
  search for `aft` in the resource names.

###### Note

AFT does not create any AWS Backup resources in the management account.

**Tables of resources initially created, by account**

| AWS Control Tower Account Factory for Terraform management account | **AWS service**       | **Resource type**                                                                                                                                                    | **Resource name** |
| ------------------------------------------------------------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| AWS Identity and Access Management                                 | Roles                 | AWSAFTAdmin<br>AWSAFTExecution<br>AWSAFTService<br>ct-aft-\*<br>aft-\*<br>codebuild_trigger_role<br>python-layer-builder-aft-common-\*                               |
| AWS Identity and Access Management                                 | Policies              | aft-\*                                                                                                                                                               |
| CodeCommit                                                         | Repositories          | aft-\*                                                                                                                                                               |
| CodeBuild                                                          | Build Projects        | aft-\*<br>ct-aft-\*<br>python-layer-builder-aft-common-\*                                                                                                            |
| Code Pipeline                                                      | Pipelines             | YourAccountId-customizations-pipeline                                                                                                                                |
| Amazon S3                                                          | Buckets               | aft-\*                                                                                                                                                               |
| Lambda                                                             | Functions             | aft-\*                                                                                                                                                               |
| Lambda                                                             | Layers                | aft-common-\*                                                                                                                                                        |
| DynamoDB                                                           | Tables                | aft-request<br>aft-request-audit<br>aft-request-metadata<br>aft-controltower-events                                                                                  |
| Step Functions                                                     | State Machines        | aft-account-provisioning-customizations<br>aft-account-provisioning-framework<br>aft-feature-options<br>aft-invoke-customizations                                    |
| VPC                                                                | VPC                   | aft-management-vpc                                                                                                                                                   |
| Amazon SNS                                                         | Topics                | aft-notifications<br>aft-failure-notifications                                                                                                                       |
| Amazon EventBridge                                                 | Event buses           | aft-events-from-ct-management                                                                                                                                        |
| Amazon EventBridge                                                 | Event rules           | aft-account-provisioning-customizations-trigger<br>aft-account-request-codepipeline-trigger<br>aft-lambda-account-request-processor<br>aft-controltower-event-logger |
| Key Management Service (KMS)                                       | Customer Managed Keys | aft-backend-\*-kms-key<br>aft                                                                                                                                        |
| AWS Systems Manager                                                | Parameter store       | /aft/\*                                                                                                                                                              |
| Amazon SQS                                                         | Queues                | aft-account-request.fifo<br>aft-account-request-dlg.fifo                                                                                                             |
| CloudWatch                                                         | Log groups            | /aws/\*/ct-aft-\*<br>/aws/\*/aft-\*<br>/aws/codebuild/python-layer-builder-aft-common-\*                                                                             |
| AWS Backup                                                         | Vaults                | aft-controltower-backup-vault                                                                                                                                        |
| AWS Backup                                                         | Plans                 | aft-controltower-backup-plan                                                                                                                                         |
| AWS Support Center (Optional)                                      | Support plans         | Enterprise                                                                                                                                                           |

| AWS accounts provisioned through AWS Control Tower Account Factory for Terraform | **AWS service** | **Resource type** | **Resource name** |
| -------------------------------------------------------------------------------- | --------------- | ----------------- | ----------------- |
| AWS Identity and Access Management                                               | Roles           | AWSAFTExecution   |
| AWS Support Center (Optional)                                                    | Support plans   | Enterprise        |

| AWS Control Tower management account | **AWS service** | **Resource type**                                                | **Resource name** |
| ------------------------------------ | --------------- | ---------------------------------------------------------------- | ----------------- |
| AWS Identity and Access Management   | Roles           | AWSAFTExecution<br>AWSAFTService<br>aft-controltower-events-rule |
| AWS Systems Manager                  | Parameter store | /aft/\*                                                          |
| EventBridge                          | Event rules     | aft-capture-ct-events                                            |
| CloudTrail (Optional)                | Trails          | aws-aft-CustomizationsCloudTrail                                 |
| AWS Support Center (Optional)        | Support plans   | Enterprise                                                       |

| AWS Control Tower log archive account | **AWS service**       | **Resource type**                            | **Resource name** |
| ------------------------------------- | --------------------- | -------------------------------------------- | ----------------- |
| AWS Identity and Access Management    | Roles                 | AWSAFTExecution<br>AWSAFTService             |
| Key Management Service (KMS)          | Customer Managed Keys | aft                                          |
| Amazon S3                             | Buckets               | aws-aft-logs-\*<br>aws-aft-s3-access-logs-\* |
| AWS Support Center (Optional)         | Support plans         | Enterprise                                   |

| AWS Control Tower audit account    | **AWS service** | **Resource type**                | **Resource name** |
| ---------------------------------- | --------------- | -------------------------------- | ----------------- |
| AWS Identity and Access Management | Roles           | AWSAFTExecution<br>AWSAFTService |
| AWS Support Center (Optional)      | Support plans   | Enterprise                       |
