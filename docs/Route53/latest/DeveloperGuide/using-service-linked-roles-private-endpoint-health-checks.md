

# Using service-linked roles for Amazon Route 53 Private endpoint health checks

Amazon Route 53 Private endpoint health checks uses an AWS Identity and Access Management (IAM) [ service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Route 53. Service-linked roles are predefined by Route 53 and include all the permissions that the service requires to call other AWS services on your behalf.

With a service-linked role, you can set up private endpoint health checks without manually adding the necessary permissions. Route 53 defines the permissions of its service-linked roles, and unless defined otherwise, only Route 53 can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting the related resources. This protects your Route 53 resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services that Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes **in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**Topics**
+ [Understanding service-linked role permissions for Private endpoint health checks](#pehc-slr-permissions)
+ [Creating a service-linked role for Private endpoint health checks](#pehc-create-slr)
+ [Editing a service-linked role for Private endpoint health checks](#pehc-edit-slr)
+ [Deleting a service-linked role for Private endpoint health checks](#pehc-delete-slr)
+ [Identifying supported Regions for Private endpoint health checks service-linked roles](#pehc-slr-regions)

## Understanding service-linked role permissions for Private endpoint health checks
<a name="pehc-slr-permissions"></a>

Route 53 uses the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role to create and manage the network interfaces that connect Route 53 health checkers to the private endpoints in your VPCs. The role trusts the `route53healthchecks.amazonaws.com` service to assume the role.

The role uses the AWS managed policy `Route53PrivateHealthChecksServiceRolePolicy`. For information about the policy's permissions, see [Route53PrivateHealthChecksServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/Route53PrivateHealthChecksServiceRolePolicy.html) in the *AWS Managed Policy Reference*. Route 53 uses this policy to complete the following actions on your resources:


| Action | Description | 
| --- | --- | 
| ec2:CreateNetworkInterface | Create network interfaces in your subnets and security groups. Route 53 gives each new network interface a Name tag that starts with healthchecksource-, and no other tags. | 
| ec2:CreateTags | Add the Name tag to a network interface only while Route 53 creates it. Route 53 sets the tag value to start with healthchecksource-. | 
| ec2:DeleteNetworkInterface | Delete network interfaces that have a Name tag that starts with healthchecksource-. | 
| ec2:DescribeNetworkInterfaces | Read the network interfaces in your account. | 
| ec2:DescribeSecurityGroups | Read the security groups in your account. | 
| ec2:DescribeVpcs | Read the VPCs in your account. | 
| ec2:DescribeSubnets | Read the subnets in your account. | 

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Private endpoint health checks
<a name="pehc-create-slr"></a>

You don't need to manually create a service-linked role. When you create a health check source in the Amazon Route 53 console, the AWS CLI, or the AWS API (`CreateHealthCheckSource`), Route 53 creates the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role for you. Route 53 also makes sure that the role exists when you delete a health check source (`DeleteHealthCheckSource`), because it uses the role to delete the network interfaces. The IAM entity that creates or deletes a health check source must have permission for `iam:CreateServiceLinkedRole` for the `route53healthchecks.amazonaws.com` service. The [AWS managed policy: AmazonRoute53FullAccess](security-iam-awsmanpol-route53.md#security-iam-awsmanpol-AmazonRoute53FullAccess) includes this permission.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a new health check source, Route 53 creates the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role for you again.

## Editing a service-linked role for Private endpoint health checks
<a name="pehc-edit-slr"></a>

Route 53 does not allow you to edit the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a Service-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Private endpoint health checks
<a name="pehc-delete-slr"></a>

If you no longer need private endpoint health checks, delete the `AWSServiceRoleForRoute53PrivateHealthChecks` role. That way you don't have an unused role that nobody actively monitors or maintains. However, you must clean up the resources for your service-linked role before you can manually delete it. IAM doesn't delete the role while your account has any health check sources.

To delete the role, you need the `iam:DeleteServiceLinkedRole` permission. If you don't have this permission, ask an administrator to delete the role for you.

**Note**  
If Route 53 is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again. If the deletion still fails with an access denied error, make sure that you have the required IAM permissions, or ask an administrator to complete the steps.

**To delete Route 53 resources used by the service-linked role**

1. Update or delete the records that use the health checks. Route 53 doesn't prevent you from deleting a health check that records still reference, and routing for those records might be unpredictable. For more information, see [Updating or deleting health checks when DNS failover is configured](health-checks-updating-deleting-tasks.md).

1. Delete the health checks that use your health check sources.

1. Delete your health check sources by using the Amazon Route 53 console, the AWS CLI, or the AWS API (`DeleteHealthCheckSource`). Route 53 deletes the network interfaces that it created for each health check source.

After you delete the resources, use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Identifying supported Regions for Private endpoint health checks service-linked roles
<a name="pehc-slr-regions"></a>

Route 53 supports using the `AWSServiceRoleForRoute53PrivateHealthChecks` service-linked role in all of the AWS Regions where private endpoint health checks are available.