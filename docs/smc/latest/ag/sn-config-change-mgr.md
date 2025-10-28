# AWS Systems Manager Change Manager in ServiceNow

AWS Service Management Connector includes a curated version of the Change
Manager integration. To allow the Connector to synchronize change templates, the change
templates should be:

- An Approved status in AWS
- At least one Automation Runbook associated with it
- Enabled as auto-approval
  For more information, see [AWS Systems Manager Change Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md").

You can also view resources affected by the changes that were executed on their AWS
accounts from the AWS CloudTrail events available on the AWS change request.

###### Note

Currently, only the first level events that occurred in the execution of an automation
document will be tracked and synched. Steps which have nested automations will not have
the events synced. This can however be traced separately in the AWS CloudTrail console using
Lake feature by their unique automation execution ID.

## Fields mapped from AWS Change Request

Ops Item records to ServiceNow Change Request records

This table shows how AWS Change Request Ops items map to ServiceNow Change
Request.

| AWS Change Request Ops Item | ServiceNow Change Request    |
| --------------------------- | ---------------------------- |
| AWS Account                 | x_126749_aws_sc_awsaccount   |
| AWS Request ID              | x_126749_aws_sc_awsrequestid |
| AWS Region                  | x_126749_aws_sc_awsregion    |
| AWS Status                  | x_126749_aws_sc_awsstatus    |
