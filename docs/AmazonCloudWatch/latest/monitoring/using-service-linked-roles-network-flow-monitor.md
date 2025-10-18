# Service-linked roles for Network Flow Monitor

Network Flow Monitor uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
 linked directly to Network Flow Monitor. The service-linked role is predefined by Network Flow Monitor and includes all the permissions 
 that the service requires to call other AWS services on your behalf. 

Network Flow Monitor defines the permissions of the
 service-linked roles, and unless defined otherwise, only Network Flow Monitor can assume the roles. The
 defined permissions include the trust policies and the permissions policies, and the permissions
 policies cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This restriction
 protects your Network Flow Monitor resources because you can't inadvertently remove permissions
 to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with
 IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html") and look for the services that have **Yes** in the
 **Service-linked role** column. Choose a 
 **Yes** with a link to view the service-linked role documentation for that
 service.


## Service-linked role permissions for
 Network Flow Monitor


Network Flow Monitor uses the following service-linked roles: 



* **AWSServiceRoleForNetworkFlowMonitor**
* **AWSServiceRoleForNetworkFlowMonitor\_Topology**

### Service-linked role permissions for
 AWSServiceRoleForNetworkFlowMonitor


Network Flow Monitor uses the service-linked role named **AWSServiceRoleForNetworkFlowMonitor**.
 This role allows Network Flow Monitor to publish CloudWatch aggregated telemetry metrics gathered for network
 traffic between instances, and between instances and AWS locations. It also allows the service to use AWS Organizations
 to get information for multi-account scenarios.


This service-linked role uses the managed policy `CloudWatchNetworkFlowMonitorServiceRolePolicy`. 


To view the permissions for this policy, see [CloudWatchNetworkFlowMonitorServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorServiceRolePolicy.html") in the *AWS Managed Policy Reference*.


The **AWSServiceRoleForNetworkFlowMonitor** service-linked role trusts the following service to assume the
 role:



* `networkflowmonitor.amazonaws.com`

### Service-linked role permissions for
 AWSServiceRoleForNetworkFlowMonitor\_Topology


Network Flow Monitor uses the service-linked role named **AWSServiceRoleForNetworkFlowMonitor\_Topology**.
 This role allows Network Flow Monitor to generate a topology snapshot of the resources that you use with Network Flow Monitor.


This service-linked role uses the managed policy `CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy`. 


To view the permissions for this policy, see [CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy.html") in the *AWS Managed Policy Reference*.


The **AWSServiceRoleForNetworkFlowMonitor\_Topology** service-linked role trusts the following service to assume the
 role:



* `topology.networkflowmonitor.amazonaws.com`

## Creating a service-linked role for Network Flow Monitor


You do not need to manually create the service-linked roles for Network Flow Monitor. The first time that you initialize
 Network Flow Monitor, Network Flow Monitor creates **AWSServiceRoleForNetworkFlowMonitor** and **AWSServiceRoleForNetworkFlowMonitor\_Topology** for you.


For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role") in the *IAM User Guide*.


## Editing a service-linked role for Network Flow Monitor


After Network Flow Monitor creates a service-linked role in your account, you cannot change the name of the role because 
 various entities might reference the role. You can edit the description of the role using IAM. For
 more information, see [Editing a
 service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role") in the *IAM User Guide*.


## Deleting a service-linked role for Network Flow Monitor


If you no longer need to use a feature or service that requires a service-linked role, we
 recommend that you delete the role. That way you don’t have an unused entity that is not
 actively monitored or maintained. However, you must clean up the resources for the
 service-linked role before you can manually delete it.


###### Note

If the Network Flow Monitor service is using the role when you try to delete it,
 then the deletion might fail. If that happens, wait for a few minutes and then try again.


**To manually delete the service-linked role using IAM**


Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForNetworkFlowMonitor**
 or the **AWSServiceRoleForNetworkFlowMonitor\_Topology**
 service-linked role. For more information, see [Deleting a
 service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role") in the *IAM User Guide*.


## Updates to the Network Flow Monitor service-linked role


For updates to `CloudWatchNetworkFlowMonitorServiceRolePolicy` or
 `CloudWatchNetworkFlowMonitorTopologyServiceRolePolicy`, the AWS managed policies for the Network Flow Monitor service-linked roles,
 see [CloudWatch updates to AWS managed policies](managed-policies-cloudwatch.md#security-iam-awsmanpol-updates "managed-policies-cloudwatch.md#security-iam-awsmanpol-updates").
 For automatic alerts about managed policy changes in CloudWatch, subscribe to the RSS feed on the CloudWatch 
 [Document history](DocumentHistory.md "DocumentHistory.md") page.
