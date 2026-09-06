

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring AWS for AWS Systems Manager Change Manager in ServiceNow
<a name="sn-config-change-mgr-integ"></a>

AWS Systems Manager uses the service-linked role named `AWSServiceRoleForAmazonSSM.` AWS Systems Manager uses this IAM service role to manage AWS resources on your behalf. For more information, see [Using service-linked roles for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html).

**To create a service-linked role for AWS Systems Manager**

1. Follow the instructions in [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#create-service-linked-role) (console) to create the role.

1. Choose **AWS Service as Systems Manager** and the use case as** Systems Manager – Inventory and Maintenance Window**.

1. Review the details and be sure to attach `AmazonSSMServiceRolePolicy`. Then choose **Create Role**.

**To create AutomationAssumeRole**

1. Follow the instructions in [Creating an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in your AWS account to create a role, `ServiceNowChangeManagerRole.` 

1. Add permissions for `ServiceNowChangeManagerRole.` Choose the use case as Systems Manager and choose `AmazonSSMAutomationRole` (AWS managed policy).

**Note**  
You can use baseline CloudFormation tempates to create the `ServiceNowChangeManagerRole` role. For more information, see [Setting baseline permissions for AWS Service Management Connector for ServiceNow](sn-base-perms.md). 

**Note**  
`ServiceNowChangeManagerRole` contains the minimum baseline permissions to execute change templates that contain automation runbooks on EC2 instances. To invoke automation runbooks on other services, you need to attach additional policies. For more information, see [Create a service role for Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup-iam.html#automation-role).

**To create an event data store (optional)**

To create AWS CloudTrail Lake, follow the instructions outlined in [Create an event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html) in your AWS account to create the event data store.