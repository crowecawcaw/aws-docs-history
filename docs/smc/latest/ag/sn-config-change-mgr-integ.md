# Configuring AWS for AWS Systems Manager Change Manager in ServiceNow

AWS Systems Manager uses the service-linked role named `AWSServiceRoleForAmazonSSM.`
AWS Systems Manager uses this IAM service role to manage AWS resources on your behalf. For more
information, see [Using service-linked roles for AWS Systems Manager](../../../systems-manager/latest/userguide/using-service-linked-roles.md "../../../systems-manager/latest/userguide/using-service-linked-roles.md").

###### To create a service-linked role for AWS Systems Manager

1. Follow the instructions in [Creating a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role") (console) to create the
   role.
2. Choose **AWS Service as Systems Manager** and
   the use case as **Systems Manager – Inventory and
   Maintenance Window**.
3. Review the details and be sure to attach
   `AmazonSSMServiceRolePolicy`. Then choose **Create Role**.

###### To create AutomationAssumeRole

1. Follow the instructions in [Creating an IAM role](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md") in your AWS account to create a role,
   `ServiceNowChangeManagerRole.`
2. Add permissions for `ServiceNowChangeManagerRole.` Choose the
   use case as Systems Manager and choose `AmazonSSMAutomationRole`
   (AWS managed policy).

###### Note

You can use baseline CloudFormation tempates to create the `ServiceNowChangeManagerRole` role.
For more information, see [Setting baseline
permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md "sn-base-perms.md").

###### Note

`ServiceNowChangeManagerRole` contains the minimum baseline
permissions to execute change templates that contain automation runbooks on EC2
instances. To invoke automation runbooks on other services, you need to attach
additional policies. For more information, see [Create a service role for Automation](../../../systems-manager/latest/userguide/automation-setup-iam.md#automation-role "../../../systems-manager/latest/userguide/automation-setup-iam.md#automation-role").

**To create an event data store (optional)**

To create AWS CloudTrail Lake, follow the instructions outlined in [Create
an event data store](../../../awscloudtrail/latest/userguide/query-event-data-store.md "../../../awscloudtrail/latest/userguide/query-event-data-store.md") in your AWS account to create the event data
store.
