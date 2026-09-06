

# Integrate VPC IPAM with Infoblox infrastructure
<a name="integrate-infoblox-ipam"></a>

Amazon VPC IPAM and Infoblox integration connects your AWS VPC IP Address Manager (IPAM) with [Infoblox](https://www.infoblox.com/), enabling you to manage AWS IP addresses through your existing Infoblox workflows while gaining cloud-native AWS capabilities.

This integration solves a common enterprise challenge: avoiding duplicate IP management systems. Instead of learning new tools and maintaining separate processes for AWS and on-premises networks, you can designate Infoblox as the management authority for VPC IPAM scopes and continue using your familiar Infoblox interface for all IP address operations.

## Integration process overview
<a name="integration-process-overview"></a>

The following steps provide an overview of the complete integration process:

1. **Configure IPAM scope** (described in this document): Amazon VPC IPAM delegated admin creates a new scope or modifies an existing scope to use Infoblox as its external authority.

1. **Configure Infoblox** (described outside of this document): See [Next steps](#infoblox-next-steps).

1. **Create top-level pool**: Amazon VPC IPAM delegated admin creates a pool in the scope that's linked to Infoblox. The pool starts with no CIDR assigned.

1. **Provision CIDR from external authority**: Amazon VPC IPAM delegated admin provisions a CIDR for the pool. You can request any available CIDR (Infoblox chooses from allowed range) or request a specific CIDR (Infoblox accepts or rejects based on availability). IPAM automatically coordinates with Infoblox to obtain and provision the approved CIDR.

1. **Continue with standard IPAM operations**: Create child pools and VPCs from the allocated CIDR using standard Amazon VPC IPAM procedures.

## When to use this integration
<a name="when-to-use-this-integration"></a>

Use this integration if you already use or plan to use Infoblox for on-premises network management and want to extend your existing IP management practices to AWS without maintaining separate systems.

## Prerequisites
<a name="prerequisites"></a>

Before configuring this integration, ensure you have:
+ **VPC IPAM Advanced Tier**: enabled in your AWS account. For more information, see [VPC IPAM Advanced Tier](https://docs.aws.amazon.com/vpc/latest/ipam/mod-ipam-tier.html).
+ **Required IAM permissions**: listed below
+ **Infoblox resource identifier**: from your Infoblox administrator

## IAM role for Infoblox
<a name="required-iam-permissions"></a>

Create an IAM role for the Infoblox principal to assume, or use an existing role. The role needs these permissions:
+ `ec2:DescribeIpamPools`
+ `ec2:DescribeIpams`
+ `ec2:DescribeIpamScopes`
+ `ec2:GetIpamPoolAllocations`
+ `ec2:GetIpamPoolCidrs`
+ `ec2:GetIpamResourceCidrs`

For instructions on how to add these permissions to an IAM role or policy, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

**Note**  
Infoblox may require permissions for VPC IPAM discovery in addition to these permissions required to enable this integration. 

## Configure Infoblox integration in the VPC IPAM
<a name="configure-infoblox-integration-in-the-vpc-ipam-console"></a>

You can enable Infoblox integration when you create or modify scopes in the AWS VPC IPAM console or AWS CLI.

**Important**  
Infoblox integration is available only for private scopes, not public scopes.

### Creating a new scope with Infoblox integration
<a name="creating-a-new-scope-with-infoblox-integration"></a>

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **IPAM**, and then choose **Scopes**.

1. Choose **Create scope**.

1. For **Scope settings**, do the following:
   + **IPAM ID** is automatically populated.
   + (Optional) For **Name tag**, enter a name for the scope.
   + (Optional) For **Description**, enter a description for the scope.

1. For **Scope Authority**, choose **Infoblox IPAM**.

1. For **Infoblox resource identifier**, enter the Infoblox resource identifier in the format `<version>.identity.account.<entity_realm>.<entity_id>`.

1. Verify that you have the required IAM permissions as displayed in the information box.

1. Choose **Create scope**.

The related AWS CLI command for this is [create-ipam-scope](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-scope.html).

### Modifying existing scopes
<a name="modifying-existing-scopes"></a>

To change the scope authority from **Amazon VPC IPAM** to **Infoblox IPAM** for an existing scope, edit the scope settings and follow the same configuration steps in the previous procedure.

The related AWS CLI command for this is [modify-ipam-scope](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-scope.html).

## Next steps
<a name="infoblox-next-steps"></a>

This completes the Amazon VPC IPAM configuration needed for the integration. After configuring the scope authority, you can create a top-level IPAM pool within the scope. For more information, see [Create a top-level IPv4 pool](create-top-ipam.md).

The integration also requires configuring an Infoblox source pool, verifying discovery job status, setting up the private scope to be managed by Infoblox, enabling Infoblox management for Amazon VPC IPAM, and creating pools either from the Infoblox integration or directly from the Infoblox portal.

For information about the Infoblox side of the integration, see the *AWS IPAM Integration User Guide* in the Infoblox documentation.