

# Map source network to new VPCs
<a name="transform-vmware-migrate-network-new-vpcs"></a>

Get a complete, production-ready target network generated from your source configuration in a fraction of the time. AWS Transform translates your source environment into AWS network resources, including VPCs, subnets, security groups, NAT gateways, transit gateways, elastic IPs, routes, and route tables, which you review and adjust before deployment. You can deploy directly with AWS Transform or choose self-deployment and receive Infrastructure as Code (IaC) in your preferred format: AWS Cloud Development Kit (AWS CDK), Landing Zone Accelerator (LZA), or HashiCorp Terraform.

Choose **Map source network to new VPCs** when you are provisioning your AWS network as part of the migration.

The AWS Transform agent guides you through the following steps, handling the analysis and generation while you make the decisions:

1. Upload your source network file.

1. Upload additional configuration files (optional, for RVTools environments).

1. Select a network topology.

1. Select a security groups mapping strategy.

1. Review and optimize your network.

1. Generate a network diagram (optional).

1. Configure resource tagging.

1. Deploy your network.

**Note**  
For multi-account deployments, you must configure cross-account IAM roles and trusted access for AWS Organizations before you start the network migration. For more information about migration types, see [Step 1: Migration type selection](transform-vmware-connect-target-account.md#transform-vmware-cta-migration-type).

## Step 1: Source network mapping
<a name="transform-vmware-source-network-mapping"></a>

AWS Transform generates target network infrastructure from a wide variety of source network configuration files. Upload one or more configuration files from your source environment, and AWS Transform uses them to generate target networks, including Amazon VPCs, subnets, and security groups. AWS Transform does not generate firewall or load balancer resources. However, it can use configuration from these network elements as input to generate target networks.

AWS Transform accepts configuration files from the following source types:
+ **Software Defined Networks (SDN):** Import/Export for VMware NSX network virtualization or Cisco ACI config for Cisco Application Centric Infrastructure.
+ **VMware vSphere networks:** [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools). When you use RVTools files, AWS Transform generates Amazon VPC configurations only. Security group configurations require additional input from firewall or software-defined network files. For more information about security group generation from additional files, see [Additional configuration files](#transform-vmware-firewall-and-sdn-config-files).
+ **Networks based on firewall configuration data:** Export files from Palo Alto Networks Firewall, Fortinet FortiGate Firewall, or Cisco ACI. For more information about supported versions and extraction instructions, see [Configuration file extraction](#transform-vmware-config-file-extraction).
+ **Hybrid networks that run both VMware and non-VMware workloads:** [AWS Transform discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html) or modelizeIT.
+ **Other file types:** AWS Transform also accepts other network configuration files, such as Checkpoint and F5 configurations. If your configuration file is not one of the formats listed above, AWS Transform converts it automatically and uses it to generate target networks. This conversion can take up to two hours based on the file size and complexity.

**Note**  
The maximum supported source network file size is 70 MB.

**Note**  
To enable stale security group rule removal during network review, submit observed network traffic data from the [AWS Transform discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html) or modelizeIT alongside your source network configuration. For more information, see [Guided network recommendations](#transform-vmware-guided-recommendations).

**Warning**  
Download RVTools only from the official Dell site at [https://www.dell.com/en-us/shop/vmware/sl/rvtools](https://www.dell.com/en-us/shop/vmware/sl/rvtools). Do not download RVTools from unofficial sources.

Each source network segment is mapped to its own distinct VPC. Network segmentation varies by source type:
+ **vNetwork:** AWS Transform groups VMs by vSwitch and virtual LAN (VLAN). VLANs can appear under multiple vSwitches (except VLAN 0).
+ **NSX networks:** AWS Transform segments the network based on Tier-1 routers, grouping the routers and collecting their segments.

## Step 2: Additional configuration files
<a name="transform-vmware-firewall-and-sdn-config-files"></a>

For RVTools source environments, you can optionally upload additional configuration files to enable security group generation. If you don't upload additional configuration files, no security groups are generated for your RVTools-based migration.

AWS Transform supports the following additional configuration file types. You can upload only one configuration file from one platform.
+ Cisco Application Centric Infrastructure (ACI) provides network policy configurations.
+ Palo Alto Networks provides firewall security policies.
+ Fortinet FortiGate provides firewall security policies.

When you upload a firewall or Cisco ACI file, AWS Transform generates network infrastructure and security groups. When you upload an RVTools file alone, AWS Transform generates network infrastructure only.

For more information about supported versions and extraction instructions, see [Configuration file extraction](#transform-vmware-config-file-extraction).

## Step 3: Network topologies
<a name="network-topologies"></a>

During the network definition step, you select a network topology. You can choose the **Isolated VPCs** topology or the **Hub and Spoke** topology.

### Isolated VPCs
<a name="isolated-vpcs"></a>

#### What is deployed
<a name="isolated-vpcs-deployed"></a>

Isolated VPCs are independent network environments that operate as separate units within AWS. Your VPCs are completely isolated, with no built-in communication pathways between them. This separation provides the highest level of network boundary protection.

AWS Transform creates the following resources:
+ A dedicated VPC for each detected source network segment.
+ Private subnets based on your source network configuration.
+ Security groups (if you provided firewall or SDN configuration files).

#### Complete your setup
<a name="isolated-vpcs-complete-setup"></a>

AWS Transform deploys the core network infrastructure for you. You complete the final connectivity and security configuration to match your organization's requirements.

To enable internet access for an Isolated VPC, complete the following steps:

1. Create an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) and attach it to the VPC.

1. Create public subnets in each Availability Zone where you need internet access. Add a route for `0.0.0.0/0` pointing to the internet gateway. For more information about subnet configuration, see [Subnets for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html).

1. Create [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the public subnets (one per AZ for high availability). Allocate an Elastic IP for each NAT gateway.

1. Update your private subnet [route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html). Add a route for `0.0.0.0/0` pointing to the NAT gateway in the same AZ.

1. Review your [security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html). Ensure outbound rules allow the traffic your workloads need (for example, HTTPS and DNS).

For VPC-to-VPC communication, set up [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) or a [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) and update route tables in each VPC to route traffic to the peering connection or TGW attachment.

### Hub and Spoke
<a name="hub-and-spoke"></a>

In this model, an [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) acts as the central hub that connects multiple workload VPCs (the spokes).

#### What is deployed
<a name="hub-and-spoke-deployed"></a>

AWS Transform creates the following resources:
+ **Spoke VPCs:** One VPC per detected source network segment, with private subnets and a Transit Gateway attachment.
+ **Inspection VPC:** Hosts your firewall appliance for traffic inspection. All cross-VPC traffic is routed through this VPC. The Transit Gateway attachment uses [appliance mode](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html), which ensures traffic flows symmetrically through the same appliance in both directions of a connection.
+ **Inbound VPC:** Handles traffic entering your network from the public internet (north-south inbound). Includes an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) and public subnets across multiple Availability Zones.
+ **Outbound VPC:** Handles traffic leaving your network to the public internet (north-south outbound). Includes an internet gateway, [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) with [elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in each Availability Zone for high availability, and private subnets for the Transit Gateway attachment.
+ **Transit Gateway route tables:** Two route tables steer traffic through the Inspection VPC:
  + The *Uninspected* table is associated with spoke VPCs, Inbound VPC, and Outbound VPC. It routes all traffic (0.0.0.0/0) to the Inspection VPC attachment and is the default association route table.
  + The *Inspected* table is associated with the Inspection VPC. It contains propagated routes from all spoke VPCs and is the default propagation route table.

For multi-account deployments, the Transit Gateway is shared across accounts through [AWS Resource Access Manager (RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).

#### Traffic flow
<a name="hub-and-spoke-traffic-flow"></a>

All cross-VPC traffic follows this path:

1. Traffic from a spoke VPC is sent to the Transit Gateway (default route 0.0.0.0/0).

1. The Uninspected route table routes the traffic to the Inspection VPC.

1. Your firewall in the Inspection VPC inspects the traffic and forwards it back to the Transit Gateway.

1. The Inspected route table routes the traffic to the destination spoke VPC using propagated routes.

For outbound internet traffic, the Inspected route table routes traffic to the Outbound VPC. NAT gateways translate private IP addresses before the traffic is forwarded to the internet gateway. The Outbound VPC public route table includes specific routes for each spoke VPC Classless Inter-Domain Routing (CIDR) range back to the Transit Gateway. These routes enable return traffic to reach the correct spoke VPC.

Inbound internet traffic enters through the Inbound VPC's internet gateway and follows the same inspection path to reach spoke VPCs.

#### Complete your setup
<a name="hub-and-spoke-complete-setup"></a>

AWS Transform deploys the core network infrastructure for you, including the Transit Gateway, spoke VPCs, and traffic routing. You complete the firewall configuration and inbound service setup to match your organization's security requirements.

**Note**  
By default, cross-VPC traffic passes through the Inspection VPC without inspection. You must deploy a firewall to enable traffic inspection.

**Deploy a firewall:** Create additional subnets in the Inspection VPC for the firewall endpoints. AWS Transform creates subnets for the Transit Gateway attachment only. Route traffic from the TGW attachment subnets to the firewall endpoints, and from the firewall subnets back to the Transit Gateway. You can deploy [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html) or a third-party appliance. For more information about deploying a firewall with a Transit Gateway, see [Creating a firewall with a Transit Gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/create-tgw-firewall.html).

**Verify connectivity:** After you deploy the firewall, test outbound internet access from a spoke VPC instance (for example, `curl https://aws.amazon.com`). You can use [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to troubleshoot connectivity issues.

**Set up inbound services:** To host public-facing services, deploy an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) or [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) in the Inbound VPC public subnets. Configure target groups that point to instances in your spoke VPCs through the Transit Gateway, and verify that the Inspected route table has return routes to the Inbound VPC.

If you want fine-grained control over the communication between the VPCs, choose the **Isolated VPCs** option and modify the generated network to create the specific communication paths you require.

## Step 4: Security groups mapping
<a name="transform-vmware-security-group-association"></a>

Choose how your source security policies translate to AWS security groups. AWS Transform creates security groups based on your source environment configurations. Security policies, security policy rules, gateway policies, and gateway policy rules are converted to security groups.

**Important**  
AWS Transform creates security groups on a best-effort basis to match your source environment. Review and modify the generated security groups to ensure that they meet your company's needs and security policies.

### Security group referencing
<a name="security-group-referencing"></a>

When security groups are generated, AWS Transform uses security group referencing where supported. Security group referencing sets security rules based on another security group ID rather than specific IP address ranges (CIDR blocks). This approach provides more flexible and maintainable security configurations.

Security group referencing follows these rules:
+ Rules can reference other security groups within the same VPC, or in a VPC that is connected within the same Region.
+ Cross-account references are supported.
+ You cannot reference a security group in a non-connected VPC or across Regions.
+ For connected VPCs, only inbound rules support cross-VPC security group references. Outbound rules must use CIDR-based rules.

How AWS Transform creates security group rules depends on your chosen network topology:
+ **Hub and Spoke:** Transit Gateway provides network connectivity between VPCs. AWS Transform uses referencing for both within-VPC and cross-VPC/cross-account ingress rules. Cross-VPC/cross-account egress (outbound) rules use CIDR-based rules.
+ **Isolated VPCs:** Your VPCs have no network connectivity between them. AWS Transform uses referencing for within-VPC rules only. All cross-VPC and cross-account rules use CIDR-based rules.

CIDR-based rules are also used when source configurations are not symmetric.

Choose one of the following security group mapping strategies:
+ **MAP:** Translates security rules from your source environment to AWS security groups and rules. Use this option for migrations using static IP addressing.
+ **MAP\_DHCP (Translate with DHCP support):** Translates security rules from your source environment with DHCP compatibility. DHCP assigns IP addresses dynamically from the subnet's CIDR range. As a result, cross-VPC egress rules are widened to match the full destination subnet CIDR. A narrower CIDR would block DHCP-assigned IPs that fall outside that range. Review these rules post-migration.

  Use this option for DHCP support with cross-VPC Transit Gateway communication. Also works with static IPs, but might produce broader rules than MAP.
+ **SKIP:** Does not translate security rules. Configure AWS security groups manually post-migration. Works with both static IP and DHCP environments. For RVTools source environments without additional configuration files, AWS Transform automatically uses SKIP.

**Note**  
Your mapping strategy determines your IP assignment options. MAP supports static IP only. MAP\_DHCP and SKIP support both static and DHCP.

### IP migration approaches
<a name="ip-migration-approaches"></a>

You have two network configuration choices for your migration:

**Network range selection**
+ **Keep Existing Ranges (IP Address Ranges Retention):** Keep original IP address ranges during migration. Ideal for migrations where you move applications to AWS without modification (lift-and-shift), especially with legacy applications that have hard-coded IP dependencies or existing firewall rules.
+ **Update to new IP ranges (CIDR update):** You can modify each VPC CIDR range during migration, and AWS Transform automatically propagates changes to subnets, route tables, and security groups.

**IP address assignment**
+ **Fixed IP addresses (Static):** AWS Transform assigns static IPs based on the CIDR. This is best for applications that require predictable network behavior, DNS management, or IP-based access control. IPs persist across instance restarts through Elastic Network Interfaces (ENIs), which are virtual network cards attached to your instances.
+ **Dynamic IP assignment (AWS DHCP):** Automatically assign IPs from subnet pools at instance launch. Optimal for applications that are designed to run in the cloud and auto-scaling workloads. Reduces operational overhead but requires applications to use DNS or service discovery.

You can combine either range selection with either IP assignment method.

**Note**  
The IP address assignment strategy is set at the wave level. You can assign different strategies to specific servers by customizing the wave file. For example, if you chose a static IP address approach for the wave but want to assign a dynamic approach to a specific server, you would use `[RESET_VALUE]` as described in [Editing your configuration](https://docs.aws.amazon.com/mgn/latest/ug/configuration-editing.html) in the *MGN user guide*.

## Step 5: Review and optimize your network
<a name="transform-vmware-review-vpc-configs"></a>

After AWS Transform generates your target network configuration, you can review the on-premises network segments converged to AWS infrastructure. Use the visual interface to review your network, and the chat interface to make changes and receive guided recommendations. AWS Transform performs cascading impact analysis and implements the required changes to maintain network consistency and compliance with best practices. You can also ask AWS Transform to analyze your network and suggest optimizations. For more information, see [Guided recommendations](#transform-vmware-guided-recommendations).

### Existing VPCs in your target account
<a name="transform-vmware-brownfield-network"></a>

If your target account already contains VPCs, from previous migration phases or parallel infrastructure projects, AWS Transform automatically detects them and displays them alongside your mapped VPCs during the review process. For multi-account migrations, AWS Transform detects existing VPCs across all accounts in your AWS Organization.

This visibility helps you understand how your planned network relates to your existing infrastructure, identify potential CIDR conflicts, and make informed decisions before deployment.

**Note**  
AWS Transform detects existing VPCs only (not subnets or other resources). Detection is read-only. AWS Transform does not modify your existing VPCs.

### Optimize your network
<a name="transform-vmware-optimization-operations"></a>

**Note**  
These operations apply to workload VPCs only. For appliance VPCs in the Hub and Spoke topology (Inspection, Inbound, Outbound), only Change IP address is supported.  
You can't undo Delete, Merge, and Split operations. Review your configuration carefully before you apply these changes.

The following operations are available for VPCs:
+ **Delete:** Permanently remove a VPC from the configuration. Use this for obsolete network segments that should not migrate to AWS.
+ **Exclude:** Temporarily remove a VPC from the migration for phased migration strategies. Excluded VPCs are not deployed but can be re-included later.
+ **Include:** Add a previously excluded VPC back into the migration.
+ **Merge:** Combine two VPCs into one. The first VPC keeps its identity and absorbs all subnets from the second VPC. Security groups are moved to the merged VPC and their associations are rebuilt accordingly. The first VPC's CIDR expands to the smallest CIDR range that contains both original CIDRs, and routing is updated automatically. The second VPC is removed from the configuration.

  Merge requirements:
  + Subnet CIDRs must not overlap between the two VPCs.
  + The merged CIDR must not exceed /16.
  + For multi-account deployments, both VPCs must be assigned to the same account.
+ **Change IP address:** Change the base IP address of a VPC CIDR while keeping the same prefix length. AWS Transform automatically translates all subnet CIDRs by the same offset. For example, changing a VPC from `10.0.0.0/16` to `10.20.0.0/16` shifts a subnet from `10.0.1.0/24` to `10.20.1.0/24`.

  Security group rules that exactly match the old VPC CIDR are updated automatically. Rules that partially overlap or don't match the old CIDR are not changed. Review these rules after the change.
+ **Rename:** Change the name of a VPC to align with your organization's naming conventions for cost allocation, compliance tracking, and operational standards.
+ **Resize:** Change the prefix length of a VPC CIDR to expand or reduce the IP address range.
  + **Prefix length decrease** (more IPs, for example /20 to /16): Subnets still fit within the larger range. No subnet changes needed.
  + **Prefix length increase** (fewer IPs, for example /16 to /20): Subnets that fall outside the new range must be resized first using the subnet resize operation.

  Security group rules that exactly match the old VPC CIDR are updated automatically. Rules that partially overlap or don't match the old CIDR are not changed. Review these rules after resizing.

  Resize requirements:
  + The new CIDR must be between /16 and /28.
  + The new CIDR must not overlap with other VPCs in the network (Hub and Spoke topology).
  + When reducing the CIDR, all existing subnets must fit within the new CIDR. Resize subnets first if needed.
+ **Split:** Divide a VPC into two VPCs based on CIDR boundaries you provide. Subnets are assigned to the new VPC whose CIDR contains them. Security groups are cloned to both new VPCs, but security group rule CIDRs are not automatically updated. Review your rules after splitting to ensure cross-VPC communication works as expected. The original VPC is replaced by the two new VPCs.

  Split requirements:
  + You must provide exactly two CIDR ranges.
  + The two CIDRs must not overlap.
  + Each CIDR must be between /16 and /28.
  + Every subnet must fit in exactly one of the two CIDRs. If any subnet does not fit, the operation is rejected.

The following operations are available for subnets:
+ **Change IP address:** Change the base IP address of a subnet CIDR while keeping the same prefix length.
+ **Delete:** Permanently remove a subnet from the configuration without affecting the parent VPC.
+ **Resize:** Change the prefix length of a subnet CIDR to expand or reduce the IP address range.

  Subnet resize requirements:
  + The new CIDR must be between /16 and /28.
  + The new CIDR must not overlap with other subnets in the same VPC.
  + The new CIDR must be within the parent VPC CIDR.

After each operation, AWS Transform re-evaluates security group referencing, which might convert CIDR-based rules to security group references or vice versa. Review your security group rules after you make changes to verify they meet your requirements.

### Guided network recommendations
<a name="transform-vmware-guided-recommendations"></a>

AWS Transform automatically analyzes your mapped network and surfaces prioritized recommendations through the chat interface, identifying optimizations that would typically require manual review by network architects. Recommendations are based on your network data and require your confirmation before any changes are applied.

AWS Transform might recommend the following optimizations:
+ **CIDR conflict resolution:** Flags overlapping CIDR ranges between your mapped VPCs and existing VPCs across all accounts in your AWS Organization. Conflicting VPCs are shown first. You can resolve conflicts by re-addressing the mapped VPC, excluding or deleting it, or acknowledging the conflict and resolving it yourself after deployment.
+ **Naming standardization:** Flags VPC names that don't follow a consistent pattern (for example, names containing hardware references). AWS Transform asks for your cloud naming convention before proposing replacements.
+ **Scope review:** Identifies network segments that might not need to migrate to AWS, such as legacy systems or constructs pending decommission. AWS Transform asks for your confirmation before excluding any construct.
+ **VPC capacity right-sizing:** Surfaces VPCs where the CIDR appears oversized or undersized for the subnets it contains. AWS Transform presents the current capacity data and lets you decide whether to resize.
+ **Security review:** Flags security group rules that allow unrestricted inbound traffic (0.0.0.0/0) for your review.
+ **Stale security group rule removal:** Identifies unused inbound firewall rules migrated from your on-premises environment and suggests removing them, so you don't carry forward security exposure that no longer serves a purpose. This recommendation works as follows:
  + To identify unused rules, AWS Transform uses observed network traffic data collected by the [AWS Transform discovery tool](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html) or modelizeIT. You must submit this traffic data alongside your source network input.
  + AWS Transform compares your migrated firewall rules against the observed traffic over the observation window captured in that data. It flags a rule as unused when no inbound traffic matches it. The absence of observed inbound traffic is a reliable signal that a rule is unused.
  + Without traffic data, AWS Transform cannot determine which rules are unused and does not suggest removals.
  + AWS Transform removes only unused ingress (inbound) rules.

  Review the suggested removals before you apply them to confirm that they align with your security policies.
+ **VPC consolidation:** Identifies fragmented VPCs that appear separated by physical infrastructure limits rather than logical isolation requirements, and suggests merging them.
+ **Application alignment:** Identifies VPCs that host applications from multiple environments, such as development and production workloads that share a single VPC. When the environments can be cleanly separated along subnet boundaries, so that no environment has workloads on both sides of the proposed split, AWS Transform suggests splitting the VPC along that boundary. Subnets and server IP addresses remain unchanged. Separating environments into dedicated VPCs follows AWS best practices for workload isolation and environment-specific access control.

  This recommendation requires the application and environment data from your migration plan, so it is available only after migration planning.

**Note**  
All recommendations require your explicit confirmation before AWS Transform applies any changes. AWS Transform presents trade-offs when a recommendation affects multiple aspects of your network.

## Step 6: Network diagram
<a name="transform-vmware-network-diagram"></a>

After reviewing the generated VPC configurations, you can optionally generate a network diagram to visualize your network topology. AWS Transform supports the following diagram formats:
+ **Mermaid code (.mmd):** This format produces a text-based diagram definition file that you can render with Mermaid-compatible tools.
+ **Image (.png):** This format produces a rendered image of your network topology.

## Step 7: Configure resource tagging
<a name="transform-vmware-tag-network-resources"></a>

Your network resources are tagged for launch and replication. You can also add custom tags and AWS Migration Acceleration Program (MAP) tags.

### Automatic tags for launch and replication
<a name="transform-vmware-tag-replication-launch"></a>

AWS Transform automatically tags your migrated network resources (VPCs, subnets, security groups, and route tables) with the following tags:
+ **Key:** `CreatedBy` **Value:** `AWSApplicationMigrationService`
+ **Key:** `ATWorkspace` **Value:** `{{workspace-id}}`

These tags allow you to use the VPC and subnet to launch test and cutover instances in AWS.

**Note**  
Your migrated VPCs and subnets don't include internet connectivity by default, so they aren't suitable as staging areas for replication.

To also use the VPC and subnet as a staging area (replication), manually add the following tags:
+ **Key:** `CreatedFor` **Value:** `AWSTransform`
+ **Key:** `ATWorkspace` **Value:** `{{workspace-id}}`

You can also apply these tags to any existing AWS network resource to make it available for replication.

Find your workspace ID in the AWS Transform web app URL: https://... /workspace/{{workspace-id}}/job/job-id

### Custom tags
<a name="transform-vmware-tag-custom"></a>

In addition to the tags applied automatically by AWS Transform, you can optionally add custom tags to organize, track costs, and manage compliance for your migrated network resources. You can apply custom tags at two levels:
+ **Job-level tags:** Apply to all resources created by this job, including all VPCs, subnets, security groups, and route tables.
+ **VPC-level tags:** Apply to a specific VPC and automatically cascade to all its associated resources (subnets, security groups, route tables).

**Note**  
Maximum 40 tags per request. Each tag requires a key and value. AWS tagging conventions apply.

AWS Transform applies these tags when it generates the Infrastructure as Code templates.

### AWS Migration Acceleration Program
<a name="transform-vmware-tag-map"></a>

If your migration is part of the **AWS Migration Acceleration Program (MAP 2.0)**, AWS Transform applies a MAP tag to your resources. If you provided your MPE ID earlier in the migration process, the tag is applied automatically. Otherwise, after you finish reviewing the generated VPC configurations, AWS Transform asks whether you have a MAP agreement and prompts you to provide your MPE ID. The MPE ID is a 10-character code using uppercase letters and digits (for example, ABCDE12345). The applied tag uses the format:
+ **Key:** `map-migrated` **Value:** `mig{{MPE_ID}}`

## Step 8: Deploy your network
<a name="transform-vmware-deploy-network"></a>

After tagging, select your deployment strategy:
+ **AWS Transform-managed deployment:** AWS Transform uses CloudFormation templates to deploy your network and runs Reachability Analyzer to check connectivity between subnets across multiple VPCs and within the same VPC.
**Note**  
You must get explicit approval before your network deployment request runs. See [Deployment approvals process](#deployment-approvals-process).
+ **Self-deployment:** AWS Transform generates Infrastructure as Code (IaC) templates. CloudFormation templates are generated by default. You can also select additional output formats:
  + AWS CDK generates a TypeScript project for programmatic infrastructure deployment.
  + HashiCorp Terraform generates HashiCorp Configuration Language (HCL) templates for managing network resources.
  + Landing Zone Accelerator (LZA) generates a network-config.yaml file for LZA network configuration.

**Note**  
When you deploy through the Landing Zone Accelerator (LZA) pipeline, your AWS Transform account and LZA installation must be in the same AWS Organization. Deployment fails if the Organization IDs don't match.

For self-deployment, use the link provided to download a zip file containing the generated templates. The zip folder includes a README.md file that explains how to use the generated templates.

To verify the downloaded file hasn't been corrupted or tampered with, generate and download a checksum, then compare it to a locally generated hash using `openssl dgst -sha256 -binary <file.zip> | base64` command.

### Deployment approvals process
<a name="deployment-approvals-process"></a>

To ensure that network changes comply with your organization's security standards and architectural requirements, all deployment requests go through an approval workflow. You must get explicit approval before your network deployment request runs.

When you submit a deployment request, it automatically routes to authorized approvers through the AWS Transform Approvals tab. Approvers validate both CloudFormation templates and network configurations. Each submission triggers a new review cycle, and deployments proceed only after receiving confirmation. If an approver denies your request, contact them directly to discuss necessary modifications. AWS Transform tracks all approval decisions for audit purposes and maintains deployment history.

## Delete deployed network resources
<a name="transform-vmware-network-deletion"></a>

If you need to roll back a deployment, you can delete the network resources that AWS Transform deployed. You can delete resources immediately after deployment completes. If you modify the deployed network resources after deployment, the resources can't be deleted automatically.
+ **AWS Transform-managed deployments:** AWS Transform removes all CloudFormation stacks that were created during deployment. This action requires approval through the AWS Transform Approvals tab.
+ **Self-deployments:** You must manually delete the deployed resources through the AWS Management Console or AWS CLI.

## Configuration file extraction
<a name="transform-vmware-config-file-extraction"></a>

If your source environment uses Cisco ACI, Palo Alto Networks, or Fortinet FortiGate, you need to extract a configuration file to provide to AWS Transform. You can use these files as standalone source files to generate network infrastructure and security groups, or as complementary files alongside an RVTools upload to add security group generation. The extraction process is the same in both cases.

To extract configuration files from your firewall and network environments, follow these procedures. Consult vendor documentation for the latest information.

### Fortinet FortiGate
<a name="fortinet-fortigate-extraction"></a>
+ The firmware version must be v7.0 or later.
+ You need `super_admin` or `super_admin_readonly` privileges at the global level.
+ Steps:

  1. Connect to the firewall by using SSH or built-in CLI client

  1. Run: `show | grep ""` (`| grep ""` disables pagination)

  1. Save all output to a file starting from the `show` command

### Palo Alto Networks
<a name="palo-alto-extraction"></a>
+ The firmware version must be 10.1 or later.
+ You need the superadmin role.
+ Connect to the firewall through SSH, run the following commands to disable pagination, set the output format, enter configuration mode, and export the configuration and predefined objects. Save the outputs:

  ```
  set cli pager off
  set cli config-output-format set
  configure
  show              # Save as palo-conf.txt
  show predefined   # Save as palo-default.txt
  ```

### Cisco ACI
<a name="cisco-aci-extraction"></a>
+ The firmware version must be 6.0 or later.
+ You need the Admin role with all privileges and a configured Secure Copy Protocol (SCP), SSH File Transfer Protocol (SFTP), or File Transfer Protocol (FTP) destination.
+ Steps:

  1. Connect to the Application Policy Infrastructure Controller (APIC) through your browser

  1. Open the **Admin** menu and choose **Config Rollbacks**

  1. In the **Take a snapshot** dialog, select the remote location option and choose **Create a snapshot now**.

  1. After receiving "Transfer successful" message, connect to the remote location server and retrieve the latest snapshot file (.gz file)