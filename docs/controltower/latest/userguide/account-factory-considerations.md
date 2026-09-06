

# Resource Considerations for Account Factory
<a name="account-factory-considerations"></a>

When an account is provisioned with Account Factory, the following AWS resources are created within the account.


| AWS service | Resource type | Resource name | 
| --- | --- | --- | 
| AWS CloudFormation | Stacks | StackSet-AWSControlTowerBP-BASELINE-CLOUDTRAIL-\* (Not deployed in landing zone version 3.0 and later)<br />StackSet-AWSControlTowerBP-BASELINE-CLOUDWATCH-\*<br />StackSet-AWSControlTowerBP-BASELINE-CONFIG-\*<br />StackSet-AWSControlTowerBP-BASELINE-ROLES-\*<br />StackSet-AWSControlTowerBP-BASELINE-SERVICE-ROLES-\* | 
| AWS CloudTrail | Trail | aws-controltower-BaselineCloudTrail | 
| AWS Config | Delivery channel | aws-controltower-BaselineConfigDeliveryChannel | 
| AWS Config | Recorder | aws-controltower-BaselineConfigRecorder | 
| Amazon CloudWatch | CloudWatch Logs | /aws/lambda/aws-controltower-NotificationForwarder | 
| AWS Identity and Access Management | Roles | aws-controltower-AdministratorExecutionRole<br />aws-controltower-CloudWatchLogsRole (Not deployed in landing zone version 3.0 and later)<br />aws-controltower-ConfigRecorderRole (Not deployed in landing zone version 2.8 and later)<br />aws-controltower-ForwardSnsNotificationRole<br />aws-controltower-ReadOnlyExecutionRole<br /> AWSControlTowerExecution | 
| AWS Identity and Access Management | Policies | AWSControlTowerServiceRolePolicy | 
| Amazon Simple Notification Service | Topics | aws-controltower-SecurityNotifications | 
| AWS Lambda | Applications | StackSet-AWSControlTowerBP-BASELINE-CLOUDWATCH-\* | 
| AWS Lambda | Functions | aws-controltower-NotificationForwarder | 
| Amazon EventBridge | Rule | AWSControlTowerManagedRule | 
| Amazon EventBridge | Rule | aws-controltower-ConfigComplianceChangeEventRule | 