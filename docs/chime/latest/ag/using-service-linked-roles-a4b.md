**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Using roles with shared Alexa for Business

devices

The information in the following sections explains how to use service-linked roles and grant Amazon Chime access to the Alexa for Business resources in your AWS account.

###### Topics

- [Service-linked role permissions for
  Amazon Chime](#service-linked-role-permissions-a4b "#service-linked-role-permissions-a4b")
- [Creating a service-linked role for
  Amazon Chime](#create-service-linked-role-a4b "#create-service-linked-role-a4b")
- [Editing a service-linked role for
  Amazon Chime](#edit-service-linked-role-a4b "#edit-service-linked-role-a4b")
- [Deleting a service-linked role for
  Amazon Chime](#delete-service-linked-role-a4b "#delete-service-linked-role-a4b")
- [Supported Regions for Amazon Chime service-linked roles](#slr-regions-a4b "#slr-regions-a4b")

## Service-linked role permissions for

Amazon Chime

Amazon Chime uses the service-linked role named **AWSServiceRoleForAmazonChime** –
Allows access to AWS services and resources used or managed by Amazon Chime, such as Alexa for Business shared devices.

The AWSServiceRoleForAmazonChime service-linked role trusts the following services to assume the
role:

- `chime.amazonaws.com`

The role permissions policy allows Amazon Chime to complete the following action on the
specified resource:

- Action: `iam:CreateServiceLinkedRole` on
  `arn:aws:iam::*:role/aws-service-role/chime.amazonaws.com/AWSServiceRoleForAmazonChime`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon Chime

You don't need to manually create a service-linked role. When you
turn on Alexa for Business for a shared device in Amazon Chime in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Chime creates
the service-linked role for you.

You can also use the IAM console to create a service-linked role with the
**Amazon Chime** use case. In the AWS CLI or the AWS API,
create a service-linked role with the `chime.amazonaws.com` service name.
For more information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If
you delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for

Amazon Chime

Amazon Chime does not allow you to edit the AWSServiceRoleForAmazonChime service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon Chime

If you no longer require a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can manually delete it.

### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any
resources used by the role.

###### Note

If Amazon Chime is using the role when you try to delete the resources, then the deletion
might fail. If that happens, wait for a few minutes and try the operation again.

###### To delete Amazon Chime resources used by the AWSServiceRoleForAmazonChime (console)

- Turn off Alexa for Business for all shared devices in your Amazon Chime account.
  1.  Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com "https://chime.aws.amazon.com").
  2.  Choose **Users**, **Shared devices**.
  3.  Select a device.
  4.  Choose **Actions**.
  5.  Choose **Disable Alexa for Business.**

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonChime
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Amazon Chime service-linked roles

Amazon Chime supports using service-linked roles in all of the regions where the service is
available. For more information, see [Amazon Chime endpoints and quotas](../../../general/latest/gr/chime.md#chime_region "../../../general/latest/gr/chime.md#chime_region").
