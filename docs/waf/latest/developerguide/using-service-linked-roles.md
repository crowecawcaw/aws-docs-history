**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Using service-linked roles for AWS WAF

This section explains how to use service-linked roles to give AWS WAF access to resources in your AWS
account.

AWS WAF uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS WAF. Service-linked roles are predefined by AWS WAF and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS WAF easier because you don’t have to
manually add the necessary permissions. AWS WAF defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS WAF can assume its roles.
The defined permissions include the trust policy and the permissions policy. That
permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting the role's related resources.
This protects your AWS WAF resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS WAF

AWS WAF uses the service-linked role `AWSServiceRoleForWAFV2Logging` to write logs to Amazon Data Firehose. This role is used only if you enable logging in AWS WAF. For information about logging, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").

This service-linked role is attached to the AWS managed policy `WAFV2LoggingServiceRolePolicy`. For more information about the managed policy, see [AWS managed policy: WAFV2LoggingServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-WAFV2LoggingServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-WAFV2LoggingServiceRolePolicy").

The `AWSServiceRoleForWAFV2Logging` service-linked role trusts the service to assume the role `wafv2.amazonaws.com`.

The permissions policies of the role allow AWS WAF to complete the following actions on the specified resources:

- Amazon Data Firehose actions: `PutRecord` and `PutRecordBatch` on Firehose data stream resources with a name that
  starts with `aws-waf-logs-`. For example, `aws-waf-logs-us-east-2-analytics`.
- AWS Organizations action: `DescribeOrganization` on Organizations organizations resources.

See the full service-linked role in the IAM console:
[AWSServiceRoleForWAFV2Logging](https://console.aws.amazon.com/iam/home#/roles/details/AWSServiceRoleForWAFV2Logging "https://console.aws.amazon.com/iam/home#/roles/details/AWSServiceRoleForWAFV2Logging").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Creating a service-linked role for

AWS WAF

You don't need to manually create a service-linked role. When you enable AWS WAF logging on the AWS Management Console, or you make a `PutLoggingConfiguration` request in the
AWS WAF CLI or the AWS WAF API, AWS WAF creates the service-linked role for you.

You must have the `iam:CreateServiceLinkedRole` permission to enable logging.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you enable AWS WAF logging,
AWS WAF creates the service-linked role for you again.

## Editing a service-linked role for

AWS WAF

AWS WAF doesn't allow you to edit the `AWSServiceRoleForWAFV2Logging` service-linked role. After you
create a service-linked role, you can't change the name of the role because various
entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing
a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for

AWS WAF

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS WAF service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete AWS WAF resources used by the `AWSServiceRoleForWAFV2Logging`

1. On the AWS WAF console, remove logging from every web ACL. For more information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").
2. Using the API or CLI, submit a `DeleteLoggingConfiguration` request for each web ACL that has logging enabled. For more information, see [AWS WAF API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the `AWSServiceRoleForWAFV2Logging`
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for

AWS WAF service-linked roles

AWS WAF supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS WAF endpoints and quotas](../../../general/latest/gr/waf.md "../../../general/latest/gr/waf.md").
