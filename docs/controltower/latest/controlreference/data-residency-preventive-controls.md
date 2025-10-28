# Data residency controls with preventive behavior

The following data residency controls have preventive behavior.

###### Topics

- [Disallow internet access for an Amazon
  VPC instance managed by a customer](#disallow-vpc-internet-access "#disallow-vpc-internet-access")
- [Disallow Amazon Virtual Private Network (VPN)
  connections](#prevent-vpn-connection "#prevent-vpn-connection")
- [Disallow cross-region networking for
  Amazon EC2, Amazon CloudFront, and AWS Global Accelerator](#prevent-cross-region-networking "#prevent-cross-region-networking")

## Disallow internet access for an Amazon

VPC instance managed by a customer

This control disallows internet access for an Amazon Virtual Private Cloud (VPC)
instance managed by a customer, rather than by an AWS service.

###### Important

If you provision Account Factory accounts with VPC internet access settings
enabled, that Account Factory setting overrides this control. To avoid enabling
internet access for newly provisioned accounts, you must change the setting in
Account Factory. For more information, see [Configure AWS Control Tower Without a VPC](../userguide/configure-without-vpc.md "../userguide/configure-without-vpc.md").

- This control does not apply to VPCs managed by AWS services.
- Existing VPCs that have internet access retain their internet access. It
  applies to new instances only. After this control is applied, access cannot be
  changed.

This is a preventive control with elective guidance. By default, this control
isn't enabled on any OUs.

The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRDISALLOWVPCINTERNETACCESS",
 "Effect": "Deny",
 "Action": [
 "ec2:CreateInternetGateway",
 "ec2:AttachInternetGateway",
 "ec2:CreateEgressOnlyInternetGateway",
 "ec2:CreateDefaultVpc",
 "ec2:CreateDefaultSubnet",
 "ec2:CreateCarrierGateway"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "ArnNotLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::*:role/AWSControlTowerExecution"
 ]
 }
 }
 }
 ]
}`

```

## Disallow Amazon Virtual Private Network (VPN)

connections

This control prevents Virtual Private Network (VPN) connections (Site-to-Site VPN
and Client VPN) to an Amazon Virtual Private Cloud (VPC).

###### Note

Existing VPCs that have internet access retain their internet access.

This is a preventive control with elective guidance. By default, this control
isn't enabled on any OUs.

The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRDISALLOWVPNCONNECTIONS",
 "Effect": "Deny",
 "Action": [
 "ec2:CreateVPNGateway",
 "ec2:AttachVPNGateway",
 "ec2:CreateCustomerGateway",
 "ec2:CreateVpnConnection",
 "ec2:ModifyVpnConnection",
 "ec2:CreateClientVpnEndpoint",
 "ec2:ModifyClientVpnEndpoint",
 "ec2:AssociateClientVpnTargetNetwork",
 "ec2:AuthorizeClientVpnIngress"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Disallow cross-region networking for

Amazon EC2, Amazon CloudFront, and AWS Global Accelerator

This control prevents configuring cross-region networking connections from Amazon
EC2, Amazon CloudFront, and AWS Global Accelerator services. It prevents VPC peering and
transit gateway peering.

###### Note

This control prevents Amazon EC2 VPC peering and Amazon EC2 transit gateway
peering within a single Region, as well as across Regions. For this reason, this
control may affect certain workloads in addition to your data residency
posture.

This is a preventive control with elective guidance. By default, this control
isn't enabled on any OUs.

The artifact for this control is the following service control policy (SCP).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GRDISALLOWCROSSREGIONNETWORKING",
 "Effect": "Deny",
 "Action": [
 "ec2:CreateVpcPeeringConnection",
 "ec2:AcceptVpcPeeringConnection",
 "ec2:CreateTransitGatewayPeeringAttachment",
 "ec2:AcceptTransitGatewayPeeringAttachment",
 "cloudfront:CreateDistribution",
 "cloudfront:UpdateDistribution",
 "globalaccelerator:Create*",
 "globalaccelerator:Update*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
