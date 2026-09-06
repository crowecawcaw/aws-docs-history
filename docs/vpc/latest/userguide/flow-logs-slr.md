

# Using service-linked roles for VPC Flow Logs
<a name="flow-logs-slr"></a>

VPC Flow Logs uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to VPC Flow Logs. Service-linked roles are predefined by VPC Flow Logs and include all the permissions that the service requires to call other AWS services on your behalf. 

A service-linked role makes setting up VPC Flow Logs easier because you don't have to manually add the necessary permissions. VPC Flow Logs defines the permissions of its service-linked roles, and unless defined otherwise, only VPC Flow Logs can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your VPC Flow Logs resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for VPC Flow Logs
<a name="slr-permissions"></a>

VPC Flow Logs uses the service-linked role named **AWSServiceRoleForVPCFlowLogs** – This service-linked role enables VPC Flow Logs to create and manage EventBridge Managed Rules and call DescribeTag APIs on your behalf to automatically track updates to EC2 Tag values associated with resources under Flow Logs subscriptions that include tag fields..

The AWSServiceRoleForVPCFlowLogs service-linked role trusts the following services to assume the role:
+ `vpc-flow-logs.amazonaws.com`

The role permissions policy named AWSVPCFlowLogsServiceRolePolicy allows VPC Flow Logs to complete the following actions on the specified resources:
+ Action: `autoscaling:DescribeTags` on EC2 Autoscaling Groups to validate tag values.

  Action: `tag:GetResources` on EC2 instances and ElasticNetworkInterfaces to validate tag values.

  Action: `events:PutRule` on new Managed Rules from sources `aws.tag` and `aws.autoscaling` for detail-types related to tag change events.

  Action: `events:DeleteRule` on Managed Rules created by VPC Flow Logs named `VPCFlowLogsEC2TagsManagedRule` and/or `VPCFlowLogsASGTagsManagedRule`.

  Action: `events:DescribeRule` on Managed Rules created by VPC Flow Logs named `VPCFlowLogsEC2TagsManagedRule` and/or `VPCFlowLogsASGTagsManagedRule`.

  Action: `events:PutTargets` on Managed Rules created by VPC Flow Logs named `VPCFlowLogsEC2TagsManagedRule` and/or `VPCFlowLogsASGTagsManagedRule`.

  Action: `events:RemoveTargets` on Managed Rules created by VPC Flow Logs named `VPCFlowLogsEC2TagsManagedRule` and/or `VPCFlowLogsASGTagsManagedRule`.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for VPC Flow Logs
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you CreateFlowLogs with tag fields in your log format and the associated TagFieldSpecifications parameter in the AWS Management Console, the AWS CLI, or the AWS API, VPC Flow Logs creates the service-linked role for you. 

**Important**  
This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. To learn more, see [A new role appeared in my AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you CreateFlowLogs with tag fields in your log format and the associated TagFieldSpecifications parameter, VPC Flow Logs creates the service-linked role for you again. 

You can also use the IAM console to create a service-linked role with the **AWSServiceRoleForVPCFlowLogs** use case. In the AWS CLI or the AWS API, create a service-linked role with the `vpc-flow-logs.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for VPC Flow Logs
<a name="edit-slr"></a>

VPC Flow Logs does not allow you to edit the AWSServiceRoleForVPCFlowLogs service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for VPC Flow Logs
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

**Note**  
If the VPC Flow Logs service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete VPC Flow Logs resources used by the AWSServiceRoleForVPCFlowLogs**

1. Delete all VPC Flow Logs subscriptions that use tag fields in the log format.

1. Wait at least one hour for VPC Flow Logs to process that all tag subscriptions for your account have been deleted and automatically clean up EventBridge Managed Rules created to support log enrichment.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForVPCFlowLogs service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for VPC Flow Logs service-linked roles
<a name="slr-regions"></a>

VPC Flow Logs does not support using service-linked roles in every Region where the service is available. You can use the AWSServiceRoleForVPCFlowLogs role in the following Regions.


| Region name | Region identity | Support in VPC Flow Logs | 
| --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | Yes | 
| US East (Ohio) | us-east-2 | Yes | 
| US West (N. California) | us-west-1 | Yes | 
| US West (Oregon) | us-west-2 | Yes | 
| Africa (Cape Town) | af-south-1 | Yes | 
| Asia Pacific (Hong Kong) | ap-east-1 | Yes | 
| Asia Pacific (Jakarta) | ap-southeast-3 | Yes | 
| Asia Pacific (Mumbai) | ap-south-1 | Yes | 
| Asia Pacific (Osaka) | ap-northeast-3 | Yes | 
| Asia Pacific (Seoul) | ap-northeast-2 | Yes | 
| Asia Pacific (Singapore) | ap-southeast-1 | Yes | 
| Asia Pacific (Sydney) | ap-southeast-2 | Yes | 
| Asia Pacific (Tokyo) | ap-northeast-1 | Yes | 
| Canada (Central) | ca-central-1 | Yes | 
| Europe (Frankfurt) | eu-central-1 | Yes | 
| Europe (Ireland) | eu-west-1 | Yes | 
| Europe (London) | eu-west-2 | Yes | 
| Europe (Milan) | eu-south-1 | Yes | 
| Europe (Paris) | eu-west-3 | Yes | 
| Europe (Stockholm) | eu-north-1 | Yes | 
| Middle East (Bahrain) | me-south-1 | Yes | 
| Middle East (UAE) | me-central-1 | Yes | 
| South America (São Paulo) | sa-east-1 | Yes | 
| AWS GovCloud (US-East) | us-gov-east-1 | Yes | 
| AWS GovCloud (US-West) | us-gov-west-1 | Yes | 