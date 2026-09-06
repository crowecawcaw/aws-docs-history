

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Using service-linked roles for Systems Manager
<a name="using-service-linked-roles"></a>

AWS Systems Manager uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Systems Manager. Service-linked roles are predefined by Systems Manager and include all the permissions that the service requires to call other AWS services on your behalf.

**Note**  
A *service role* role differs from a service-linked role. A service role is a type of AWS Identity and Access Management (IAM) role that grants permissions to an AWS service so that the service can access AWS resources. Only a few Systems Manager scenarios require a service role. When you create a service role for Systems Manager, you choose the permissions to grant so that it can access or interact with other AWS resources.

A service-linked role makes setting up Systems Manager easier because you don’t have to manually add the necessary permissions. Systems Manager defines the permissions of its service-linked roles, and unless defined otherwise, only Systems Manager can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Systems Manager resources because you can't inadvertently remove permission to access the resources.

**Note**  
For non-EC2 nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environment , you need an additional IAM role that allows those machines to communicate with the Systems Manager service. This is the IAM service role for Systems Manager. This role grants AWS Security Token Service (AWS STS) *AssumeRole* trust to the Systems Manager service. The `AssumeRole` action returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token). You use these temporary credentials to access AWS resources that you might not normally have access to. For more information, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md) and [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *[AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/)*. 

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Note**  
Systems Manager Automation no longer uses the service-linked role for CloudWatch alarm monitoring. This operation now uses your runbook execution identity. Make sure your execution identity has the required permissions. For more information, see [Configuring Automations to monitor CloudWatch Alarms](automation-cw-alarm-monitoring.md).

**Topics**
+ [Using roles to collect inventory and view OpsData](using-service-linked-roles-service-action-1.md)
+ [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md)
+ [Using roles to create OpsData and OpsItems for Explorer](using-service-linked-roles-service-action-3.md)
+ [Using roles to create operational insight OpsItems in Systems Manager OpsCenter](using-service-linked-roles-service-action-4.md)
+ [Using roles to maintain Quick Setup-provisioned resource health and consistency](using-service-linked-roles-service-action-5.md)
+ [Using roles to export Explorer OpsData](using-service-linked-roles-service-action-6.md)
+ [Using roles to enable just-in-time node access](using-service-linked-roles-service-action-8.md)
+ [Using roles to send just-in-time node access request notifications](using-service-linked-roles-service-action-9.md)