

# VPC permissions
<a name="hosted-zone-private-vpc-permissions"></a>

VPC permissions use Identity and Access management (IAM) policy condition to allow you to set granular permissions for VPCs when using [AssociateVPCWithHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AssociateVPCWithHostedZone.html), [DisassociateVPCFromHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DisassociateVPCFromHostedZone.html), [CreateVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateVPCAssociationAuthorization.html), [DeleteVPCAssociationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteVPCAssociationAuthorization.html), [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html), and [ListHostedZonesByVPC](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html) APIs.

With the IAM policy condition, `route53:VPCs`, you can grant granular administrative rights to other AWS users. This allows you to grant someone permissions to associate hosted zone with, disassociate hosted zone from, create VPC association authorization for, delete VPC association authorization for, create hosted zone with or list hosted zones for:
+ A single VPC.
+ Any VPCs within the same Region.
+ Multiple VPCs.

For more information about VPC permissions, see [Using IAM policy conditions for fine-grained access control](specifying-conditions-route53.md).

To learn how to authenticate AWS users, see [Authenticating with identities](security-iam.md#security_iam_authentication) and to learn how to control access to Route 53 resources, see [Access control](security-iam.md#access-control).