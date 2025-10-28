# Use IPAM with a single account

If you choose not to [Integrate IPAM with accounts in an AWS Organization](enable-integ-ipam.md "enable-integ-ipam.md"), you can use IPAM with a single AWS account.

When you create an IPAM in the next section, a service-linked role is automatically
created for the Amazon VPC IPAM service in AWS Identity and Access Management (IAM).

Service-linked roles are a type of IAM role that allows AWS services to access other AWS
services on your behalf. They simplify the permission management process by automatically
creating and managing the necessary permissions for specific AWS services to perform their
required actions, streamlining the setup and administration of these services.

IPAM uses the service-linked role to monitor and store metrics for CIDRs associated with
EC2 networking resources. For more information on the service-linked role and how IPAM uses
it, see [Service-linked roles for IPAM](iam-ipam-slr.md "iam-ipam-slr.md").

###### Important

If you use IPAM with a single AWS account, you must ensure that the AWS account
you use to create the IPAM uses a IAM role with a policy attached to it that permits the
`iam:CreateServiceLinkedRole` action. When you create the IPAM, you
automatically create the AWSServiceRoleForIPAM service-linked role. For more information
on managing IAM policies, see [Editing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in
the _IAM User Guide_.

Once the single AWS account has permission to create the IPAM service-linked role, go to [Create an IPAM](create-ipam.md "create-ipam.md").
