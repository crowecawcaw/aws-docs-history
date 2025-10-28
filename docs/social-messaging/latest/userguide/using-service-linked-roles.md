# Using service-linked roles for

AWS End User Messaging Social

AWS End User Messaging Social uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS End User Messaging Social. Service-linked roles are predefined by AWS End User Messaging Social and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS End User Messaging Social easier because you don’t have to
manually add the necessary permissions. AWS End User Messaging Social defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS End User Messaging Social can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS End User Messaging Social resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS End User Messaging Social

AWS End User Messaging Social uses the service-linked role named **AWSServiceRoleForSocialMessaging** –
To publish metrics and provide insights for your social message sending.

The AWSServiceRoleForSocialMessaging service-linked role trusts the following services to assume the
role:

- `social-messaging.amazonaws.com`

The role permissions policy named AWSSocialMessagingServiceRolePolicy allows AWS End User Messaging Social to complete the
following actions on the specified resources:

- Action: `"cloudwatch:PutMetricData"` on
  `all AWS resources in the AWS/SocialMessaging namespace.`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

For updates to the policy, see [AWS End User Messaging Social updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

## Creating a service-linked role for AWS End User Messaging Social

You can use the IAM console to create a service-linked role with the
**AWSEndUserMessagingSocial - Metrics** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `social-messaging.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

You can create the service-linked role for AWS End User Messaging Social with the following AWS CLI command:

```
aws iam create-service-linked-role --aws-service-name social-messaging.amazonaws.com
```

## Editing a service-linked role for AWS End User Messaging Social

AWS End User Messaging Social does not allow you to edit the AWSServiceRoleForSocialMessaging service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS End User Messaging Social

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS End User Messaging Social service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To remove AWS End User Messaging Social resources used by the AWSServiceRoleForSocialMessaging

1. Call `list-linked-whatsapp-business-accounts` API to see the resources you have.
2. For each linked Whats App Business Account, call the `disassociate-whatsapp-business-account` API to remove the resource from SocialMessaging service.
3. Verify no resources are returned by calling the `list-linked-whatsapp-business-accounts` API again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForSocialMessaging service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS End User Messaging Social service-linked roles

AWS End User Messaging Social supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
