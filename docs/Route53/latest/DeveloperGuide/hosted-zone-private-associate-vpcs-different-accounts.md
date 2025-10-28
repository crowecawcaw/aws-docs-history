# Associating an Amazon VPC and a private hosted zone

that you created with different AWS accounts

If you want to associate a VPC that you created with one AWS account with a private hosted zone that you created
with a different account, perform the following procedure:

###### To associate an Amazon VPC and a private hosted zone that you created with different AWS accounts

1.  Using the account that created the hosted zone, authorize the association of the VPC with the private hosted zone
    by using one of the following methods:

        * **AWS CLI** –
         See [create-vpc-association-authorization](../../../cli/latest/reference/route53/create-vpc-association-authorization.md "../../../cli/latest/reference/route53/create-vpc-association-authorization.md") in the
         *AWS CLI Command Reference*
        * **AWSSDK** or **AWS Tools for Windows PowerShell** –
         See the applicable documentation on the
         [AWSDocumentation](../../../index.md "../../../index.md") page
        * **Amazon Route 53 API** –
         See [CreateVPCAssociationAuthorization](../APIReference/API_CreateVPCAssociationAuthorization.md "../APIReference/API_CreateVPCAssociationAuthorization.md")
         in the *Amazon Route 53 API Reference*

    Note the following:

        * If you want to associate multiple VPCs that you created with one account with a hosted zone that you created
         with a different account, you must submit one authorization request for each VPC.
        * When you authorize the association, you must specify the hosted zone ID, so the private hosted zone
         must already exist.
        * You can't use the Route 53 console either to authorize the association of a VPC with a private hosted zone or to
         make the association.

2.  Using the account that created the VPC, associate the VPC with the hosted zone. As with authorizing the association,
    you can use the AWS SDK, Tools for Windows PowerShell, the AWS CLI, or the Route 53 API. If you're using the API, use the
    [AssociateVPCWithHostedZone](../APIReference/API_AssociateVPCWithHostedZone.md "../APIReference/API_AssociateVPCWithHostedZone.md") action.
3.  _Recommended_ – Delete the authorization to associate the VPC with the
    hosted zone. Deleting the authorization does not affect the association, it just prevents you from reassociating the VPC with
    the hosted zone in the future. If you want to reassociate the VPC with the hosted zone, you'll need to repeat steps 1 and 2
    of this procedure.

###### Important

The `ListHostedZonesByVPC` returns the hosted zones given a VPC and `GetHostedZone` API returns the VPCs associated to the hosted zone.
These APIs only consider the hosted zone to VPC association that are created by `AssociateVPCWithHostedZone` API or when the private hosted zone is created.
If you want a complete list of hosted zone associations to a VPC, also call [ListProfileResourceAssociations](../APIReference/API_route53profiles_ListProfileResourceAssociations.md "../APIReference/API_route53profiles_ListProfileResourceAssociations.md").

###### Note

For the maximum number of authorizations that you can create, see
[Quotas on entities](DNSLimitations.md#limits-api-entities "DNSLimitations.md#limits-api-entities").
