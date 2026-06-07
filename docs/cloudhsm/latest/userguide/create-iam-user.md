# Create IAM administrative groups for AWS CloudHSM

The first step to getting started with AWS CloudHSM is to set up IAM permissions.

As a [best
practice](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users"), don't use your AWS account root user to interact with AWS, including AWS CloudHSM.
Instead, use AWS Identity and Access Management (IAM) to create an IAM user, IAM role, or federated user.
Follow the steps in the section [Create an IAM user and administrator group](#create-iam-admin "#create-iam-admin")
to create an administrator group and attach the
**AdministratorAccess** policy to it. Then create a new administrator
user and add the user to the group. Add additional users to the group as needed. Each user
you add inherits the **AdministratorAccess** policy from the group.

Another best practice is to create an AWS CloudHSM administrator group that has only the
permissions required to run AWS CloudHSM. Add individual users to this group as needed. Each user
inherits the limited permissions that are attached to the group rather than full AWS
access. The [Customer managed policies for AWS CloudHSM](identity-access-management.md#permissions-for-cloudhsm "identity-access-management.md#permissions-for-cloudhsm") section that follows contains the policy that
you should attach to your AWS CloudHSM administrator group.

AWS CloudHSM defines a [service–linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") for your AWS account. The service–linked role
currently defines permissions that allow your account to log AWS CloudHSM events. The role can be
created automatically by AWS CloudHSM or manually by you. You cannot edit the role, but you can
delete it. For more information, see [Service-linked roles for AWS CloudHSM](service-linked-roles.md "service-linked-roles.md").

## Create an IAM user and administrator group

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

For example policies for AWS CloudHSM that you can attach to your IAM user group, see [Identity and access management for AWS CloudHSM](identity-access-management.md "identity-access-management.md").
