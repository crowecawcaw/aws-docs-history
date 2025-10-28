# VPC permissions

VPC permissions use Identity and Access management (IAM) policy condition to allow you to
set granular permissions for VPCs when using [AssociateVPCWithHostedZone](../APIReference/API_AssociateVPCWithHostedZone.md "../APIReference/API_AssociateVPCWithHostedZone.md"), [DisassociateVPCFromHostedZone](../APIReference/API_DisassociateVPCFromHostedZone.md "../APIReference/API_DisassociateVPCFromHostedZone.md"), [CreateVPCAssociationAuthorization](../APIReference/API_CreateVPCAssociationAuthorization.md "../APIReference/API_CreateVPCAssociationAuthorization.md"), [DeleteVPCAssociationAuthorization](../APIReference/API_DeleteVPCAssociationAuthorization.md "../APIReference/API_DeleteVPCAssociationAuthorization.md"), [CreateHostedZone](../APIReference/API_CreateHostedZone.md "../APIReference/API_CreateHostedZone.md"), and [ListHostedZonesByVPC](../APIReference/API_ListHostedZonesByVPC.md "../APIReference/API_ListHostedZonesByVPC.md") APIs.

With the IAM policy condition, `route53:VPCs`, you can grant granular
administrative rights to other AWS users. This allows you
to grant someone permissions to associate hosted zone with, disassociate hosted zone
from, create VPC association authorization for, delete VPC association authorization
for, create hosted zone with or list hosted zones for:

- A single VPC.
- Any VPCs within the same Region.
- Multiple VPCs.
  For more information about VPC permissions, see
  [Using IAM policy conditions for
  fine-grained access control](specifying-conditions-route53.md "specifying-conditions-route53.md").

To learn how to authenticate AWS users, see [Authenticating with identities](auth-and-access-control.md#security_iam_authentication "auth-and-access-control.md#security_iam_authentication") and to learn how to control access to Route 53
resources, see [Access control](auth-and-access-control.md#access-control "auth-and-access-control.md#access-control").
