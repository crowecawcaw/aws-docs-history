# Service-linked roles for IPAM

IPAM uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique
type of IAM role. Service-linked roles are predefined by IPAM and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up IPAM easier because you don’t have to
manually add the necessary permissions. IPAM defines the permissions of its
service-linked roles, and unless defined otherwise, only IPAM can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

## Service-linked role permissions

IPAM uses the **AWSServiceRoleForIPAM** service-linked role to call
the actions in the attached **AWSIPAMServiceRolePolicy** managed
policy. For more information on the allowed actions in that policy, see [AWS managed policies for IPAM](iam-ipam-managed-pol.md "iam-ipam-managed-pol.md").

Also attached to the service-linked role is an [IAM trust policy](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")
that allows the `ipam.amazonaws.com`
service to assume the service-linked role.

## Create the service-linked role

IPAM monitors the IP address usage in one or more accounts by assuming the service-linked role in an account, discovering the resources and their CIDRs, and integrating the resources with IPAM.

The service-linked role is created in one of two ways:

- **When you integrate with AWS
  Organizations**

If you [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md") using the IPAM console or using
the `enable-ipam-organization-admin-account` AWS CLI command, the
**AWSServiceRoleForIPAM** service-linked role
is automatically created in each of your AWS Organizations member accounts. As
a result, the resources within all member accounts are discoverable by
IPAM.

###### Important

For IPAM to create the service-linked role on your
behalf:

    + The AWS Organizations management account that enables IPAM integration with AWS Organizations must have an IAM policy attached to it that permits the
     following actions:




    	- `ec2:EnableIpamOrganizationAdminAccount`
    	- `organizations:EnableAwsServiceAccess`
    	- `organizations:RegisterDelegatedAdministrator`
    	- `iam:CreateServiceLinkedRole`
    + The IPAM account must have an IAM policy attached to it that permits the
     `iam:CreateServiceLinkedRole` action.

- **When you create an IPAM using a single AWS
  account**

If you [Use IPAM with a single account](enable-single-user-ipam.md "enable-single-user-ipam.md"), the **AWSServiceRoleForIPAM** service-linked role is automatically
created when you create an IPAM as that account.

###### Important

If you use IPAM with a single AWS account, before you create an IPAM,
you must ensure that the AWS account you are using has an IAM policy
attached to it that permits the `iam:CreateServiceLinkedRole`
action. When you create the IPAM, you automatically create the
**AWSServiceRoleForIPAM** service-linked role. For more information on managing
IAM policies, see [Editing a service-linked role description](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md#edit-service-linked-role-iam-console") in the _IAM User Guide_.

## Edit the service-linked role

You can't edit the **AWSServiceRoleForIPAM** service-linked
role.

## Delete the service-linked role

If you no longer need to use IPAM, we recommend that you delete the
**AWSServiceRoleForIPAM** service-linked role.

###### Note

You can delete the service-linked role only after you delete all IPAM resources in your AWS
account. This ensures that you can't inadvertently remove the monitoring capability of
IPAM.

Follow these steps
to delete the service-linked role using the AWS CLI:

1. Delete your IPAM resources using [deprovision-ipam-pool-cidr](../../../cli/latest/reference/ec2/deprovision-ipam-pool-cidr.md "../../../cli/latest/reference/ec2/deprovision-ipam-pool-cidr.md") and [delete-ipam](../../../cli/latest/reference/ec2/delete-ipam.md "../../../cli/latest/reference/ec2/delete-ipam.md"). For
   more information, see [Deprovision CIDRs from a pool](depro-pool-cidr-ipam.md "depro-pool-cidr-ipam.md") and
   [Delete an IPAM](delete-ipam.md "delete-ipam.md").
2. Disable the IPAM account with [disable-ipam-organization-admin-account](../../../cli/latest/reference/ec2/disable-ipam-organization-admin-account.md "../../../cli/latest/reference/ec2/disable-ipam-organization-admin-account.md").
3. Disable the IPAM service with [disable-aws-service-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disable-aws-organizations-access.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disable-aws-organizations-access.html") using the `--service-principal
ipam.amazonaws.com` option.
4. Delete the service-linked role: [delete-service-linked-role](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html"). When you delete the service-linked role, the IPAM managed policy is also deleted. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
   _IAM User Guide_.
