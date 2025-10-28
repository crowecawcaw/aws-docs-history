# Using service-linked roles for

AWS End User Messaging SMS

AWS End User Messaging SMS uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts"). A service-linked role is a unique type of IAM role that is
linked directly to AWS End User Messaging SMS. Service-linked roles are predefined by AWS End User Messaging SMS and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS End User Messaging SMS easier because you don’t have to
manually add the necessary permissions. AWS End User Messaging SMS defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS End User Messaging SMS can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your AWS End User Messaging SMS resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for AWS End User Messaging SMS

AWS End User Messaging SMS uses the service-linked role named **AWSServiceRoleForSMSVoice** –
Allows SMSVoice to publish metrics to CloudWatch on your behalf.

The AWSServiceRoleForSMSVoice service-linked role trusts the following services to assume the
role:

- `sms-voice.amazonaws.com`

The role permissions policy named SMSVoiceServiceRolePolicy allows AWS End User Messaging SMS to complete the
following actions on the specified resources:

- Action: `cloudwatch:PutMetricData` on
  `any metric in the `AWS/SMSVoice` namespace`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for AWS End User Messaging SMS

You don't need to manually create a service-linked role. When you
use any of the following actions `CreateConfigurationSet`, `CreateOptOutList`, `CreatePool`, `CreateProtectConfiguration`, `CreateRegistration`, `CreateRegistrationAttachment`, `CreateVerifiedDestinationNumber`, `RequestPhoneNumber`, or `RequestSenderId` in the AWS Management Console, the AWS CLI, or the AWS API, AWS End User Messaging SMS creates
the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you use any of the following actions `CreateConfigurationSet`, `CreateOptOutList`, `CreatePool`, `CreateProtectConfiguration`, `CreateRegistration`, `CreateRegistrationAttachment`, `CreateVerifiedDestinationNumber`, `RequestPhoneNumber`, or `RequestSenderId`,
AWS End User Messaging SMS creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**AWSEndUserMessagingSMS - Metrics** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `sms-voice.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for AWS End User Messaging SMS

AWS End User Messaging SMS does not allow you to edit the AWSServiceRoleForSMSVoice service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#edit-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for AWS End User Messaging SMS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS End User Messaging SMS service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete AWS End User Messaging SMS resources used by the AWSServiceRoleForSMSVoice

1. Verify you have no configuration sets, registrations, protect configurations, sender IDs, pools, long codes, and that you have not used AWS End User Messaging SMS in
   the last 30 days.
2. Call the iam DeleteServiceLinkedRole api to remove the role, for more information see [Deleting a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForSMSVoice service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS End User Messaging SMS service-linked roles

AWS End User Messaging SMS supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS End User Messaging endpoints and quotas](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
