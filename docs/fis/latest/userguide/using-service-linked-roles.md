# Use service-linked roles for AWS Fault Injection Service

AWS Fault Injection Service uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to AWS FIS. Service-linked roles are predefined by
AWS FIS and include all of the permissions that the service requires to call other
AWS services on your behalf.

A service-linked role makes setting up AWS FIS easier because you don’t have to
manually add the necessary permissions to manage monitoring and resource selection for experiments. AWS FIS defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS FIS can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

In addition to the service-linked role, you must also specify an IAM role that grants
permission to modify the resources that you specify as targets in an experiment template.
For more information, see [IAM roles for AWS FIS experiments](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

You can delete a service-linked role only after first deleting the related resources. This
protects your AWS FIS resources because you can't inadvertently remove permission to
access the resources.

## Service-linked role permissions for AWS FIS

AWS FIS uses the service-linked role named \***\*AWSServiceRoleForFIS\*\*** to enable it to manage monitoring and resource selection for experiments.

The **AWSServiceRoleForFIS** service-linked role trusts the following services to assume the
role:

- `fis.amazonaws.com`

The **AWSServiceRoleForFIS** service-linked role uses the managed policy **AmazonFISServiceRolePolicy**.
This policy enables AWS FIS to manage monitoring and resource selection for experiments.
For more information, see [AmazonFISServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonFISServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonFISServiceRolePolicy.md")
in the _AWS Managed Policy Reference_.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For the \***\*AWSServiceRoleForFIS\*\***
service-linked role to be successfully created, the IAM identity that you use AWS FIS
with must have the required permissions. To grant the required permissions, attach the following
policy to the IAM identity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "fis.amazonaws.com"
 }
 }
 }
 ]
}`

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.

## Create a service-linked role for AWS FIS

You don't need to manually create a service-linked role. When you
start an AWS FIS experiment in the AWS Management Console, the AWS CLI, or the AWS API, AWS FIS
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you start an AWS FIS experiment,
AWS FIS creates the service-linked role for you again.

## Edit a service-linked role for AWS FIS

AWS FIS does not allow you to edit the **AWSServiceRoleForFIS** service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Delete a service-linked role for AWS FIS

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS FIS service is using the role when you try to clean up the resources,
then the cleanup might fail. If that happens, wait for a few minutes and try the
operation again.

###### To clean up AWS FIS resources used by the **AWSServiceRoleForFIS**

Make sure that none of your experiments are currently running. If necessary, stop your experiments.
For more information, see [Stop an experiment](stop-experiment.md "stop-experiment.md").

###### To manually delete the service-linked role using IAM

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForFIS**
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for AWS FIS service-linked roles

AWS FIS supports using service-linked roles in all of the Regions where the service is available.
For more information, see [AWS Fault Injection Service endpoints and quotas](../../../general/latest/gr/fis.md "../../../general/latest/gr/fis.md").
