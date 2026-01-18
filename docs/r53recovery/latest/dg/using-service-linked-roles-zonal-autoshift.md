# Using the service-linked role for zonal autoshift in ARC

Zonal autoshift in Amazon Application Recovery Controller uses a AWS Identity and Access Management (IAM)[service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to a service— in this case, ARC. The service-linked role is predefined by ARC and
includes all the permissions that the service requires to call other AWS services on your behalf for specific
purposes.

A service-linked role makes setting up ARC easier because you don’t have to
manually add the necessary permissions. ARC defines the permissions for the
service-linked role, and unless defined otherwise, only ARC can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your ARC zonal autoshift resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS Services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-linked role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun

ARC uses the service-linked role named **AWSServiceRoleForZonalAutoshiftPracticeRun** to
do the following:

- Monitor customer-provided Amazon CloudWatch alarms and customer Health Dashboard events for practice runs
- Manage practice runs (practice zonal shifts)

This section describes the permissions
for the service-linked role, and information about creating, editing, and deleting the role.

### Service-linked role permissions for AWSServiceRoleForZonalAutoshiftPracticeRun

This service-linked role uses the managed policy `AWSZonalAutoshiftPracticeRunSLRPolicy`.

The **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role trusts the following service to assume the role:

- `practice-run.arc-zonal-shift.amazonaws.com`

To view the permissions for this policy, see [AWSZonalAutoshiftPracticeRunSLRPolicy](../../../aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.md "../../../aws-managed-policy/latest/reference/AWSZonalAutoshiftPracticeRunSLRPolicy.md") in the _AWS Managed Policy Reference_.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions")
in the _IAM User Guide_.

### Creating the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC

You don't need to manually create the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role. When you
create the first practice run configuration in the AWS Management Console, the AWS CLI, or an AWS SDK, ARC
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you create the first practice run configuration,
ARC creates the service-linked role for you again.

### Editing the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC

ARC does not allow you to edit the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role. After you
create the service-linked role, you cannot change the name of the role because other entities
might reference it. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

### Deleting the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role for ARC

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for a
service-linked role before you can manually delete it.

After you have disabled autoshift, then you can delete the **AWSServiceRoleForZonalAutoshiftPracticeRun** service-linked role.
For more information about the autoshift capability, see [Zonal shift in ARC](arc-zonal-shift.md "arc-zonal-shift.md").

###### Note

If the ARC service is using the role when you try to delete the resources,
then the service role deletion might fail. If that happens, wait for a few minutes and try the
again to delete the role.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForZonalAutoshiftPracticeRun
service-linked role. For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Updates to the ARC service-linked role for zonal autoshift

For updates to the AWS managed policies for the ARC service-linked roles,
see the [AWS managed policies updates table](security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-arc-updates") for ARC.
You can also subscribe to automatic RSS alerts on the ARC [Document history page](doc-history.md "doc-history.md").
