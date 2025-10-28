# The managed-updates service-linked role

AWS Elastic Beanstalk uses AWS Identity and Access Management (IAM) [service-linked
roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is linked directly to Elastic Beanstalk. Service-linked roles are predefined by
Elastic Beanstalk and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Elastic Beanstalk easier because you don’t have to manually add the necessary permissions. Elastic Beanstalk defines
the permissions of its service-linked roles, and unless defined otherwise, only Elastic Beanstalk can assume its roles. The defined permissions include the
trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Elastic Beanstalk resources because you can't
inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for Elastic Beanstalk

Elastic Beanstalk uses the service-linked role named **AWSServiceRoleForElasticBeanstalkManagedUpdates** – Allows Elastic Beanstalk to perform scheduled platform updates of your running environments.

The AWSServiceRoleForElasticBeanstalkManagedUpdates service-linked role trusts the following services to assume the role:

- `managedupdates.elasticbeanstalk.amazonaws.com`

The managed policy **AWSElasticBeanstalkManagedUpdatesServiceRolePolicy** allows the AWSServiceRoleForElasticBeanstalkManagedUpdates service-linked role
all of the permissions that Elastic Beanstalk needs to complete managed update actions on your behalf. To view the managed policy content, see the [AWSElasticBeanstalkManagedUpdatesServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticBeanstalkManagedUpdatesServiceRolePolicy.md") page in the _AWS Managed Policy Reference Guide_.

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in
the _IAM User Guide_.

Alternatively, you can use an AWS managed policy to [provide full access](AWSHowTo.iam.md "AWSHowTo.iam.md") to
Elastic Beanstalk.

## Creating a service-linked role for Elastic Beanstalk

You don't need to manually create a service-linked role. When you create an Elastic Beanstalk environment using the Elastic Beanstalk API, enable managed updates, and specify
`AWSServiceRoleForElasticBeanstalkManagedUpdates` as the value for the `ServiceRoleForManagedUpdates` option of the
`aws:elasticbeanstalk:managedactions` namespace, Elastic Beanstalk creates the service-linked role for
you.

When Elastic Beanstalk tries to create the AWSServiceRoleForElasticBeanstalkManagedUpdates service-linked role for your account when you create an environment, you must have the
`iam:CreateServiceLinkedRole` permission. If you don't have this permission, environment creation fails, and you see a message explaining
the issue.

As an alternative, another user with permission to create service-linked roles can use IAM to pre-create the service linked-role in advance. You
can then create your environment even without having the `iam:CreateServiceLinkedRole` permission.

You (or another user) can use the IAM console to create a service-linked role with the **Elastic Beanstalk Managed Updates** use case. In
the IAM CLI or the IAM API, create a service-linked role with the `managedupdates.elasticbeanstalk.amazonaws.com` service name. For more information, see
[Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_. If you delete this service-linked role, you can use this same process to create the role again.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When
you create an Elastic Beanstalk environment using the Elastic Beanstalk API, enable managed updates, and specify
`AWSServiceRoleForElasticBeanstalkManagedUpdates` as the value for the `ServiceRoleForManagedUpdates` option of the
`aws:elasticbeanstalk:managedactions` namespace, Elastic Beanstalk creates the service-linked role for you again.

## Editing a service-linked role for Elastic Beanstalk

Elastic Beanstalk does not allow you to edit the AWSServiceRoleForElasticBeanstalkManagedUpdates service-linked role. After you create a service-linked role, you cannot change the name
of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see
[Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for Elastic Beanstalk

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can
manually delete it.

### Cleaning up a service-linked role

Before you can use IAM to delete a service-linked role, you must first be sure that Elastic Beanstalk environments with managed updates enabled are either
using a different service role or are terminated.

###### Note

If the Elastic Beanstalk service is using the service-linked role when you try to terminate the environments, then the termination might fail. If
that happens, wait for a few minutes and try the operation again.

###### To terminate an Elastic Beanstalk environment that uses the AWSServiceRoleForElasticBeanstalkManagedUpdates (console)

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. Choose **Actions**, and then choose **Terminate Environment**.
4. Use the on-screen dialog box to confirm environment termination.

See [eb terminate](eb3-terminate.md "eb3-terminate.md") for details about terminating an Elastic Beanstalk environment using the EB CLI.

See [TerminateEnvironment](../api/API_TerminateEnvironment.md "../api/API_TerminateEnvironment.md") for details about terminating an Elastic Beanstalk environment using
the API.

### Manually delete the service-linked role

Use the IAM console, the IAM CLI, or the IAM API to delete the AWSServiceRoleForElasticBeanstalkManagedUpdates service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Elastic Beanstalk service-linked roles

Elastic Beanstalk supports using service-linked roles in all of the regions where the service is available. For more information, see
[AWS Elastic Beanstalk Endpoints and Quotas](../../../general/latest/gr/elasticbeanstalk.md "../../../general/latest/gr/elasticbeanstalk.md").
