End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Using roles for CodeBuild-based provisioning

AWS Proton uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Proton. Service-linked roles are predefined by AWS Proton and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Proton easier because you don’t have to
manually add the necessary permissions. AWS Proton defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Proton can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your AWS Proton resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for AWS Proton

AWS Proton uses the service-linked role named **AWSServiceRoleForProtonCodeBuildProvisioning**
– A Service Linked Role for AWS Proton CodeBuild provisioning.

The **AWSServiceRoleForProtonCodeBuildProvisioning** service-linked role trusts the following
services to assume the role:

- `codebuild.proton.amazonaws.com`

The role permissions policy named `AWSProtonCodeBuildProvisioningServiceRolePolicy` allows
AWS Proton to complete the following actions on the specified resources:

- Action: _create, manage, and read_ on
  _AWS CloudFormation stacks and transforms_
- Action: _create, manage, and read_ on
  _CodeBuild projects and builds_

For more information about this policy, see [AWS
managed policy: AWSProtonCodeBuildProvisioningServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSProtonCodeBuildProvisioningServiceRolePolicy").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

AWS Proton

You don't need to manually create a service-linked role. When you
create an environment that uses CodeBuild-based provisioning in AWS Proton in the AWS Management Console, the AWS CLI, or the AWS API, AWS Proton
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create an environment that uses CodeBuild-based provisioning in AWS Proton, AWS Proton creates the service-linked role for you again.

## Editing a service-linked role for

AWS Proton

AWS Proton does not allow you to edit the **AWSServiceRoleForProtonCodeBuildProvisioning**
service-linked role. After you create a service-linked role, you cannot change the name of
the role because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

AWS Proton

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must
delete all environments and services (instances and pipelines) that use CodeBuild-based provisioning in AWS Proton before you can manually delete it.

### Manually delete the service-linked

role

Use the IAM console, the AWS CLI, or the AWS API to delete the
**AWSServiceRoleForProtonCodeBuildProvisioning** service-linked role. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported regions for AWS Proton

service-linked roles

AWS Proton supports using service-linked roles in all of the AWS Regions where the
service is available. For more information, see [AWS Proton endpoints and quotas](../../../general/latest/gr/proton.md "../../../general/latest/gr/proton.md") in the _AWS General Reference_.
