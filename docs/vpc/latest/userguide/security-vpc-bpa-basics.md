# VPC BPA basics

This section covers important details about VPC BPA, including which services support
it and how you can work with it.

###### Contents

- [Regional availability](#security-vpc-bpa-reg-avail "#security-vpc-bpa-reg-avail")
- [AWS service impact and support](#security-vpc-bpa-service-support "#security-vpc-bpa-service-support")
- [VPC BPA limitations](#security-vpc-bpa-limits "#security-vpc-bpa-limits")
- [Control access to VPC BPA with an IAM
  policy](#security-vpc-bpa-iam-example "#security-vpc-bpa-iam-example")
- [Enable VPC BPA bidirectional mode
  for your account](#security-vpc-bpa-enable-bidir "#security-vpc-bpa-enable-bidir")
- [Change VPC BPA mode to
  ingress-only](#security-vpc-bpa-ingress-only "#security-vpc-bpa-ingress-only")
- [Create and delete exclusions](#security-vpc-bpa-exclusions "#security-vpc-bpa-exclusions")
- [Enable VPC BPA at the Organization level](#security-vpc-bpa-exclusions-orgs "#security-vpc-bpa-exclusions-orgs")

## Regional availability

VPC BPA is available in all commercial [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") including GovCloud and China Regions.

In this guide, you'll also find information about using Network Access Analyzer and Reachability Analyzer with VPC
BPA. Note that Network Access Analyzer and Reachability Analyzer are not available in all commercial Regions. For
information about the regional availability of Network Access Analyzer and Reachability Analyzer, see [Limitations](../network-access-analyzer/how-network-access-analyzer-works.md#analyzer-limitations "../network-access-analyzer/how-network-access-analyzer-works.md#analyzer-limitations") in the _Network Access Analyzer Guide_ and [Considerations](../reachability/how-reachability-analyzer-works.md#considerations "../reachability/how-reachability-analyzer-works.md#considerations") in the _Reachability Analyzer Guide_.

## AWS service impact and support

The following resources and services support VPC BPA and traffic to these services
and resources is impacted by VPC BPA:

- **Internet gateway**: All inbound and outbound traffic is
  blocked.
- **Egress-only internet gateway**: All outbound traffic is
  blocked. Egress-only internet gateways do not allow inbound traffic.
- **Gateway Load Balancer (GWLB)**: All inbound
  and outbound traffic is blocked even if the subnet containing GWLB endpoints
  is excluded.
- **NAT gateway**: All inbound and outbound traffic is blocked. NAT
  gateways require an internet gateway for internet connectivity.
- **Internet-facing Network Load Balancer**: All inbound and
  outbound traffic is blocked. Internet-facing Network Load Balancers require an
  internet gateway for internet connectivity.
- **Internet-facing Application Load Balancer**: All inbound and
  outbound traffic is blocked. Internet-facing Application Load Balancers require
  an internet gateway for internet connectivity.
- **Amazon CloudFront VPC Origins**:
  All inbound and outbound traffic is blocked.
- **AWS Direct Connect**: All inbound and outbound traffic that uses public
  virtual interfaces (public IPv4 or global unicast IPv6 addresses) is
  blocked. This traffic uses the internet gateway (or egress-only
  internet-gateway) for connectivity.
- **AWS Global Accelerator**: Inbound traffic to VPCs is blocked, whether or not the target is otherwise accessible from the internet.
- **AWS Network Firewall**: All inbound and outbound
  traffic is blocked even if the subnet containing firewall endpoints is
  excluded.
- **AWS Wavelength carrier gateway**: All inbound and outbound traffic
  is blocked.

Traffic related to private connectivity, such as traffic for the following
services and resources, is not blocked or impacted by VPC BPA:

- AWS Client VPN
- AWS CloudWAN
- AWS Outposts local gateway
- AWS Site-to-Site VPN
- Transit gateway
- AWS Verified Access

###### Important

- If you are routing incoming and outgoing traffic through an appliance (such as a 3rd-party
  security or monitoring tool) running on an EC2 instance in a subnet,
  when using VPC BPA, that subnet needs to be an exclusion for traffic to
  flow in and out of it. Other subnets sending traffic to the appliance
  subnet and not to the internet gateway do not need to be added as
  exclusions.
- Traffic sent privately from resources in your VPC to other services
  running in your VPC, such as the Route 53 Resolver, is allowed
  even when VPC BPA is turned on because it does not pass through an
  internet gateway in your VPC. It is possible that these services may
  make requests to resources outside of the VPC on your behalf, for
  example, in order to resolve a DNS query, and may expose information
  about the activity of resources within your VPC if not mitigated through
  other security controls.

## VPC BPA limitations

VPC BPA ingress-only mode is not supported in Local Zones (LZs) where NAT
gateways and egress-only internet gateways are not allowed.

## Control access to VPC BPA with an IAM

policy

For examples of IAM policies that allow/deny access to the VPC BPA feature, see [Block public access to VPCs and subnets](vpc-policy-examples.md#vpc-bpa-example-iam "vpc-policy-examples.md#vpc-bpa-example-iam").

## Enable VPC BPA bidirectional mode

for your account

VPC BPA bidirectional mode blocks all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets). For more information about exclusions, see [Create and delete exclusions](#security-vpc-bpa-exclusions "#security-vpc-bpa-exclusions").

###### Important

We strongly recommend that you thoroughly review the workloads that require Internet access prior to enabling VPC BPA in your production accounts.

###### Note

- To enable VPC BPA on the VPCs and subnets in your account, you must own the VPCs and subnets.
- If you are currently sharing VPC subnets with other accounts, the VPC BPA mode
  enforced by the subnet owner applies to participant traffic as well, but participants
  can't control the VPC BPA settings that impact the shared subnet.

AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose
   **Settings**.
3. Choose **Edit public access settings**.
4. Choose **Turn on block public access** and
   **Bidirectional**, then choose **Save
   changes**.
5. Wait for the **Status** to change to
   **On**. It may take a few minutes for VPC
   BPA settings to take effect and the status to be updated.

VPC BPA Bidirectional mode is now on.

AWS CLI

1. Turn on VPC BPA:

```
aws ec2 --region `us-east-2` modify-vpc-block-public-access-options --internet-gateway-block-mode block-bidirectional
```

It may take a few minutes for VPC BPA settings to take effect
and the status to be updated. 2. View the status of VPC BPA:

```
aws ec2 --region `us-east-2` describe-vpc-block-public-access-options
```

## Change VPC BPA mode to

ingress-only

VPC BPA ingress-only mode blocks all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.

AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose
   **Settings**.
3. Choose **Edit public access
   settings**.
4. Change the direction to
   **Ingress-only**.
5. Save the changes and wait for the status to be updated. It may
   take a few minutes for VPC BPA settings to take effect and the
   status to be updated.

AWS CLI

1. Modify the VPC BPA block direction:

```
aws ec2 --region `us-east-2` modify-vpc-block-public-access-options --internet-gateway-block-mode block-ingress
```

It may take a few minutes for VPC BPA settings to take effect
and the status to be updated. 2. View the status of VPC BPA:

```
aws ec2 --region `us-east-2` describe-vpc-block-public-access-options
```

## Create and delete exclusions

A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s VPC BPA mode and will allow bidirectional or egress-only access. You can create VPC BPA exclusions for VPCs and subnets even when VPC BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. An exclusion for a VPC automatically applies to all subnets in the VPC.

You can create a maximum of 50 exclusions. For information about requesting a limit
increase, see _VPC BPA exclusions per account_ in [Amazon VPC quotas](amazon-vpc-limits.md "amazon-vpc-limits.md").

AWS Management Console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose
   **Settings**.
3. In the **Block public access** tab, under
   **Exclusions**, do one of the
   following:
   - To delete an exclusion, select the exclusion and then choose
     **Actions** > **Delete
     exclusions**.
   - To create an exclusion, choose **Create exclusions** and continue with the
     next steps.

4. Choose a block direction:
   - **Bidirectional**: Allows all internet traffic to
     and from the excluded VPCs and subnets.
   - **Egress-only**: Allows
     outbound internet traffic from the excluded VPCs and
     subnets. Blocks inbound internet traffic to the excluded
     VPCs and subnets. This setting applies when VPC BPA is
     set to **Bidirectional**.

5. Choose a VPC or subnet.
6. Choose **Create
   exclusions**.
7. Wait for the **Exclusion status** to change to **Active**. You may need to refresh the exclusion table to see the change.

The exclusion has been created.

AWS CLI

1. Modify the exclusion allow direction:

```
aws ec2 --region `us-east-2` create-vpc-block-public-access-exclusion --subnet-id `subnet-id` --internet-gateway-exclusion-mode allow-bidirectional
```

2. It can take time for the exclusion status to update. To view the status of the exclusion:

```
aws ec2 --region `us-east-2` describe-vpc-block-public-access-exclusions --exclusion-ids `exclusion-id`
```

## Enable VPC BPA at the Organization level

If you are using AWS Organizations to manage accounts in your organization, you can use an [AWS Organizations declarative policy](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") to enforce VPC BPA on the accounts in the organization. For more information about the VPC BPA declarative policy, see
[Supported
declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-block-public-access "../../../organizations/latest/userguide/orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-block-public-access") in the _AWS Organizations User
Guide_.

###### Note

- You can use the VPC BPA declarative policy to configure if exclusions are allowed, but you
  cannot create exclusions with the policy. To create exclusions, you
  still have to create them in the account that owns the VPC. For more
  information about creating VPC BPA exclusions, see [Create and delete exclusions](#security-vpc-bpa-exclusions "#security-vpc-bpa-exclusions").
- If the VPC BPA declarative policy is enabled, in **Block public access** settings, you'll see **Managed by Declarative Policy** and you won't be able to modify VPC BPA settings at the account level.
