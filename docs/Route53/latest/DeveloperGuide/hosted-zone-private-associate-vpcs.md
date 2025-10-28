# Associating more VPCs with a private hosted zone

You can use the Amazon Route 53 console to associate more VPCs with a private hosted zone if you created the hosted zone and the
VPCs by using the same AWS account.

###### Important

If you want to associate VPCs that you created by using one account with a private hosted zone that you
created by using a different account, you first must authorize the association. In addition, you can't use the
AWS console either to authorize the association or associate the VPCs with the hosted zone. For more information, see
[Associating an Amazon VPC and a private hosted zone
that you created with different AWS accounts](hosted-zone-private-associate-vpcs-different-accounts.md "hosted-zone-private-associate-vpcs-different-accounts.md").

For information about how to associate more VPCs with a private hosted zone using the Route 53 API, see
[AssociateVPCWithHostedZone](../APIReference/API_AssociateVPCWithHostedZone.md "../APIReference/API_AssociateVPCWithHostedZone.md") in the
_Amazon Route 53 API Reference_.

###### To associate additional VPCs with a private hosted zone using the Route 53 console

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the radio button for the private hosted zone that you want to associate more VPCs with.
4. Choose **Edit**.
5. Choose **Add VPC**.
6. Choose the Region and the ID of the VPC that you want to associate with this hosted zone.
7. To associate more VPCs with this hosted zone, repeat steps 5 and 6.
8. Choose **Save changes**.
