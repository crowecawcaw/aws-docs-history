# Using service-linked roles for Amazon Inspector

Amazon Inspector uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") named `AWSServiceRoleForAmazonInspector2`. This service-linked role is an
IAM role that is linked directly to Amazon Inspector. It is predefined by Amazon Inspector and it
includes all the permissions that Amazon Inspector requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon Inspector easier because you don’t have to
manually add the necessary permissions. Amazon Inspector defines the permissions of its
service-linked role and, unless defined otherwise, only Amazon Inspector can assume the role. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You must configure permissions to allow an IAM entity (such as a group or role) to create,
edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_. You can
delete a service-linked role only after deleting its related resources. This protects your
Amazon Inspector resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to review the service-linked
role documentation for that service.

## Creating a service-linked role for Amazon Inspector

You don't need to manually create a service-linked role. When you activate Amazon Inspector in
the AWS Management Console, the AWS CLI, or the AWS API, Amazon Inspector creates the service-linked role for
you.

## Editing a service-linked role for Amazon Inspector

Amazon Inspector does not allow you to edit the `AWSServiceRoleForAmazonInspector2` service-linked role.
After a service-linked role is created, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role by using
IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon Inspector

If you no longer need to use Amazon Inspector, we recommend that you delete the
`AWSServiceRoleForAmazonInspector2` service-linked role. Before you can delete the role, you must
deactivate Amazon Inspector in each AWS Region where it's activated. When you deactivate Amazon Inspector, it
doesn't delete the role for you. Therefore, if you activate Amazon Inspector again, it can use the
existing role. That way you can avoid having an unused entity that's not actively monitored or
maintained. However, you must clean up the resources for your service-linked role before you
can manually delete it.

If you delete this service-linked role and then need to create it again, you can use the
same process to re-create the role in your account. When you activate Amazon Inspector, Amazon Inspector re-creates
the service-linked role for you.

###### Note

If the Amazon Inspector service is using the role when you try to delete the resources, the
deletion might fail. If that happens, wait a few minutes and then try the operation
again.

You can use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForAmazonInspector2` service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Creating a service-linked role for agentless scanning

You don't need to manually create a service-linked role. When you activate Amazon Inspector in
the AWS Management Console, the AWS CLI, or the AWS API, Amazon Inspector creates the service-linked role for
you.

## Editing a service-linked role for agentless scanning

Amazon Inspector does not allow you to edit the `AWSServiceRoleForAmazonInspector2Agentless` service-linked role.
After a service-linked role is created, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role by using
IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for agentless scanning

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that isn't actively monitored or maintained.

###### Important

In order to delete the `AWSServiceRoleForAmazonInspector2Agentless` role, you must set your scan mode to agent-based in all Regions where agentless scanning is available.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonInspector2Agentless service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
