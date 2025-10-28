Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Blocking public access to VPCs and subnets

VPC Block Public Access (BPA) is a centralized security feature that you can use to
block resources in VPCs and subnets that you own in an AWS Region from reaching the
internet or being reached from the internet through internet gateways and egress-only
internet gateways. If you turn this feature on in an AWS account, it will, by default,
impact any VPC or subnet that Amazon Redshift uses. This means that Amazon Redshift blocks all operations to
the public.

When you have VPC BPA turned on and want to use Amazon Redshift APIs over the public internet,
you must add an exclusion for using Amazon EC2 APIs for your VPC or subnet. Exclusions can
have either of the following modes:

- **Bidirectional**: All internet traffic to and from the
  excluded VPCs and subnets is allowed.
- **Egress-only**: Outbound internet traffic from the excluded
  VPCs and subnets is allowed. Inbound internet traffic to the excluded VPCs and
  subnets is blocked. This only applies when BPA is set to bidirectional.
  VPC BPA exclusions designate an entire VPC or specific subnet within a VPC as
  public-access capable. Network interfaces within that boundary respect the regular VPC
  networking controls, such as security groups, route tables, and network ACLs, with
  regard to whether that interface has a route and access to the public internet. For more
  information about adding exclusions, see [Create
  and delete exclusions](../../../vpc/latest/userguide/security-vpc-bpa.md#security-vpc-bpa-exclusions "../../../vpc/latest/userguide/security-vpc-bpa.md#security-vpc-bpa-exclusions") in the _Amazon VPC User Guide_.

**Provisioned clusters**

A subnet group is a combination of subnets from the same VPC. If a subnet group for a
provisioned cluster is in an account with VPC BPA turned on, the following capabilities
are blocked:

- Creating a public cluster
- Restoring a public cluster
- Modifying a private cluster to be public
- Adding a subnet with VPC BPA turned on to the subnet group when there's at
  least one public cluster within the group

**Serverless clusters**

Redshift Serverless doesn't use subnet groups. Instead, each cluster has its own set of subnets. If
a workgroup is in an account with VPC BPA turned on, the following capabilities are
blocked:

- Creating a public access workgroup
- Modifying a private workgroup to public
- Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is
  public
