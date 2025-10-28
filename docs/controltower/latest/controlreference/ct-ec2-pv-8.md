# [CT.EC2.PV.8] Disallow inbound and outbound internet connections to your VPCs through an internet gateway (IGW) or egress-only internet gateway (EIGW)

This control blocks direct ingress and egress traffic from the internet to your VPCs through an IGW
or EIGW, by configuring block public access for VPCs (VPC BPA) at an account level. This control also disallows configuration
of any VPC BPA exclusions, which means that if you enable it, you cannot exclude VPCs or subnets from the effects of this control.

This is a preventive control with elective guidance, based on declarative policies. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Declarative policy for EC2
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control does not block traffic to your VPC when the traffic originates
  from locations other than an internet gateway or an egress-only internet
  gateway, such as traffic from a peered VPC or other VPC attached gateway (for
  example, an AWS Transit Gateway network gateway or virtual private gateway).
  Traffic from these locations may have a public network origin; therefore,
  AWS Control Tower recommends using EC2 security groups to set least-privilege network
  access controls, and to ensure that only the required network connections are
  allowed.
- This control does not affect inbound traffic from serverless services, such as
  API Gateway and Lambda, in your VPCs (for example, traffic that arrives by means
  of Elastic network interfaces or API Gateway private integration). However, VPC
  BPA will block traffic to or from these services, if that traffic occurs through
  an IGW or EIGW, in a governed VPC.
- This control governs Amazon EC2 VPC block public access settings that are
  configured by means of EC2 `ModifyVpcBlockPublicAccessOptions`,
  `CreateVpcBlockPublicAccessExclusion`, and `ModifyVpcBlockPublicAccessExclusion`
  operations. If you apply this control, you cannot use these operations to modify
  these settings within an enrolled AWS account.
- For an overview of VPC connectivity options and recommendations for creating
  scalable and secure network architectures, see [Building a Scalable and Secure Multi-VPC AWS Network
  Infrastructure](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md") in the _Building a Scalable and Secure
  Multi-VPC AWS Network Infrastructure - AWS Whitepaper_.
- This control includes an AWS Organizations inheritance operator for each policy setting that applies to child policies (`@@operators_allowed_for_child_policies` with a value of `@@all`). This operator allows you to add to, negate, or override each policy setting in this control, when it is applied to child OUs and accounts, by using the AWS Organizations declarative policy syntax. For more information on policy inheritance for AWS Organizations policies, see [Inheritance operators](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") in the _AWS Organizations User Guide_.
  The artifact for this control is the following declarative policy.

```

{
    "ec2_attributes": {
        "vpc_block_public_access": {
            "internet_gateway_block": {
                "mode": {
                    "@@assign": "block_bidirectional",
                    "@@operators_allowed_for_child_policies": ["@@all"]
                },
                "exclusions_allowed": {
                    "@@assign": "disabled",
                    "@@operators_allowed_for_child_policies": ["@@all"]
                }
            }
        }
    }
}

```
