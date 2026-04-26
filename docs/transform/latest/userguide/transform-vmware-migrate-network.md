# Migrate network

AWS Transform migrates VMware networks to AWS by translating your source environment configuration into AWS-equivalent network resources. AWS Transform
analyzes your source network data and creates VPCs, subnets, security groups, NAT gateways, transit gateways, elastic IPs, routes, and route tables as needed. You can review and modify the generated network configuration before deployment. For deployment, you can either have AWS Transform deploy the configuration for you and analyze deployed network connectivity, or choose self-deployment—in which case AWS Transform generates Infrastructure as Code (IaC) in your preferred format: AWS Cloud Development Kit (AWS CDK) (AWS CDK), Landing Zone Accelerator (LZA), or HashiCorp Terraform.

To migrate your network, follow these steps:

1. Upload your source network file
2. Upload additional configuration files (optional, for RVTools environments)
3. Select a network topology
4. Select a security groups mapping strategy
5. Review the generated VPC configurations
6. Generate a network diagram (optional)
7. Configure resource tagging
8. Deploy your network

###### Note

For multi-account deployments, you must configure cross-account IAM roles and trusted access for AWS Organizations before starting the network migration. For more information, see [Step 1: Migration type selection](transform-vmware-connect-target-account.md#transform-vmware-cta-migration-type "transform-vmware-connect-target-account.md#transform-vmware-cta-migration-type").

## Step 1: Source network mapping

The network mapping process requires uploading a configuration file from your source environment. The tool you choose depends on your source network type:

- **Software Defined Networks (SDN):** Import/Export for VMware NSX network virtualization or Cisco ACI config for Cisco Application Centric Infrastructure.
- **VMware vSphere networks:** [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools"). When using RVTools files, AWS Transform generates Amazon VPC configurations only. Security group configurations require additional input from firewall or software-defined network files. See [Additional configuration files](#transform-vmware-firewall-and-sdn-config-files "#transform-vmware-firewall-and-sdn-config-files") for more details.
- **Networks based on firewall configuration data:** Export files from Palo Alto Networks Firewall, Fortinet FortiGate Firewall, or Cisco ACI. For supported versions and extraction instructions, see [Configuration file extraction](#transform-vmware-config-file-extraction "#transform-vmware-config-file-extraction").
- **Hybrid networks running both VMware and non-VMware workloads:** Application mapping tools - modelizeIT.
- **Other file types:** If your configuration file is not one of the supported formats listed above, AWS Transform will attempt to automatically convert it to a format that can be processed by the service. This conversion can take up to two hours depending on the file size and complexity.

###### Warning

The official RVTools site is [https://www.dell.com/en-us/shop/vmware/sl/rvtools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools"), which is the site that this guide links to in steps that mention RVTools. Beware of the scam site (rvtools)(dot)(org).

AWS Transform creates VPCs from all source network segments, with each detected segment becoming its own distinct VPC. Network segmentation varies by source type:

- **vNetwork:** AWS Transform groups VMs by vSwitch and VLAN. VLANs can appear under multiple vSwitches (except VLAN 0).
- **NSX networks:** AWS Transform segments the network based on Tier-1 routers, grouping the routers and collecting their segments.

## Step 2: Additional configuration files

For RVTools source environments, you can optionally upload additional configuration files to enable security group generation. Without additional configuration, no security groups will be generated for RVTools-based migrations.

AWS Transform supports the following additional configuration file types. Only one configuration file from one platform can be uploaded.

- Cisco Application Centric Infrastructure (ACI): Network policy configurations
- Palo Alto Networks: Firewall security policies
- Fortinet FortiGate: Firewall security policies

When you upload a firewall or Cisco ACI file, AWS Transform generates network infrastructure and security groups. When you upload an RVTools file alone, AWS Transform generates network infrastructure only.

For supported versions and extraction instructions, see [Configuration file extraction](#transform-vmware-config-file-extraction "#transform-vmware-config-file-extraction").

## Step 3: Network topologies

During the network definition step, you select a network topology. You can choose the **Isolated VPCs** topology or the **Hub and Spoke** topology.

### Isolated VPCs

These are independent network environments that operate as separate units within AWS. VPCs maintain complete network isolation, with no built-in communication pathways between them. This separation provides the highest level of network boundary protection. You can connect the VPCs through specific networking configurations if needed.

###### Important

No internet connectivity is configured for Isolated VPCs. You must set up internet gateways, NAT gateways, and routing manually.

### Hub and Spoke

In this model, an [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") acts as the central hub that connects multiple workload VPCs (the spokes). AWS Transform creates a spoke VPC for each detected source network segment and connects them through the Transit Gateway.

**Appliance VPCs**

AWS Transform creates three specialized appliance VPCs to manage traffic flow and security:

- **Inspection VPC:** Hosts your firewall appliance for traffic inspection. All cross-VPC traffic is routed through this VPC. You must deploy a firewall (such as [AWS Network Firewall](../../../network-firewall/latest/developerguide/getting-started.md "../../../network-firewall/latest/developerguide/getting-started.md") or a third-party appliance) in this VPC. The Transit Gateway attachment uses [appliance mode](../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md "../../../vpc/latest/tgw/transit-gateway-appliance-scenario.md") to ensure symmetric routing.
- **Inbound VPC:** Handles traffic from the public internet (north-south inbound). Includes an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") and public subnets across multiple Availability Zones.
- **Outbound VPC:** Handles traffic to the public internet (north-south outbound). Includes an internet gateway, [NAT gateways](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") with [elastic IP addresses](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") in each Availability Zone for high availability, and private subnets for the Transit Gateway attachment.

**Transit Gateway route tables**

AWS Transform creates two Transit Gateway route tables to steer traffic through the Inspection VPC:

- **Uninspected:** Associated with spoke VPCs, Inbound VPC, and Outbound VPC. Routes all traffic (0.0.0.0/0) to the Inspection VPC attachment. This is the default association route table — new VPC attachments are automatically associated with it.
- **Inspected:** Associated with the Inspection VPC. Contains propagated routes from all spoke VPCs, so inspected traffic can reach its destination. This is the default propagation route table — spoke VPC routes are automatically propagated to it.

**Traffic flow**

All cross-VPC traffic follows this path:

1. Traffic from a spoke VPC is sent to the Transit Gateway (default route 0.0.0.0/0).
2. The Uninspected route table routes the traffic to the Inspection VPC.
3. Your firewall in the Inspection VPC inspects the traffic and forwards it back to the Transit Gateway.
4. The Inspected route table routes the traffic to the destination spoke VPC using propagated routes.

For outbound internet traffic, the Inspected route table routes traffic to the Outbound VPC, where NAT gateways translate private IP addresses before forwarding to the internet gateway. The Outbound VPC public route table includes specific routes for each spoke VPC CIDR back to the Transit Gateway, enabling return traffic to reach the correct spoke VPC. Inbound internet traffic enters through the Inbound VPC's internet gateway and follows the same inspection path to reach spoke VPCs.

For multi-account deployments, AWS Transform shares the Transit Gateway across accounts using [AWS Resource Access Manager (RAM)](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

###### Note

By default, cross-VPC traffic passes through the Inspection VPC without inspection. To inspect traffic, deploy a firewall appliance (such as [AWS Network Firewall](../../../network-firewall/latest/developerguide/getting-started.md "../../../network-firewall/latest/developerguide/getting-started.md")) in the Inspection VPC.

To deploy a firewall, create additional subnets in the Inspection VPC for the firewall endpoints. AWS Transform creates subnets for the Transit Gateway attachment only. Route traffic from the TGW attachment subnets to the firewall endpoints, and from the firewall subnets back to the Transit Gateway. For more information, see [Creating a firewall with a Transit Gateway](../../../network-firewall/latest/developerguide/create-tgw-firewall.md "../../../network-firewall/latest/developerguide/create-tgw-firewall.md").

If you want fine-grained control over the communication between the VPCs, choose the **Isolated VPCs** option and modify the generated network to create the specific communication paths you require.

## Step 4: Security groups mapping

AWS Transform creates security groups based on your source environment configurations. AWS Transform converts security policies, security policy rules, gateway policies, and gateway policy rules to security groups.

###### Important

AWS Transform makes a best effort to create security groups that match your source environment. Review and modify the generated security groups to ensure that they meet your company's needs and security policies.

**Security group referencing**

When generating security groups, AWS Transform uses security group referencing where supported. Security group referencing sets security rules based on another security group ID rather than specific IP address ranges (CIDR blocks). This approach provides more flexible and maintainable security configurations.

In AWS, security group rules can only reference other security groups within the same VPC, or in a connected VPC within the same Region, including across accounts. You cannot reference a security group in a non-connected VPC or across Regions. For connected VPCs, only inbound rules support cross-VPC security group references — outbound rules must use CIDR-based rules. How AWS Transform creates security group rules depends on your chosen network topology:

- **Hub and Spoke:** Transit Gateway provides network connectivity between VPCs. AWS Transform creates security groups using referencing for both within-VPC and cross-VPC/cross-account ingress rules. Cross-VPC/cross-account egress (outbound) rules use CIDR-based rules.
- **Isolated VPCs:** There is no network connectivity between VPCs. AWS Transform creates security groups using referencing for within-VPC rules only. All cross-VPC and cross-account rules use CIDR-based rules.

CIDR-based rules are also used when source configurations are not symmetric.

Choose one of the following security group mapping strategies:

- **MAP:** Translates security rules from your source environment to AWS security groups and rules. Use this option for migrations using static IP addressing.
- **MAP_DHCP (Translate with DHCP support):** Translates security rules from your source environment with DHCP compatibility. Because DHCP assigns IP addresses dynamically from the subnet's CIDR range, cross-VPC egress rules are widened to match the full destination subnet CIDR. A narrower CIDR would block DHCP-assigned IPs that fall outside that range — review these rules post-migration. Use this option for DHCP support with cross-VPC Transit Gateway communication. Also works with static IPs, but may produce broader rules than MAP.
- **SKIP:** Does not translate security rules. Configure AWS security groups manually post-migration. Works with both static IP and DHCP environments. For RVTools source environments without additional configuration files, AWS Transform automatically uses SKIP.

###### Note

Your mapping strategy determines your IP assignment options. MAP supports static IP only. MAP_DHCP and SKIP support both static and DHCP.

**IP migration approaches**

The system offers two key network configuration choices for your migration:

**Network range selection:**

- **Keep Existing Ranges (IP Address Ranges Retention):** Keep original IP address ranges during migration. Ideal for lift-and-shift scenarios with legacy applications that have hard-coded IP dependencies or existing firewall rules.
- **Update to new IP ranges (CIDR update):** You can modify each VPC CIDR range during migration, and AWS Transform automatically propagates changes to subnets, route tables, and security groups.

**IP addresses assignment:**

- **Fixed IP addresses (Static):** The system assigns static IPs based on the CIDR. This is best for applications requiring predictable network behavior, DNS management, or IP-based access control. IPs persist across instance restarts using Elastic Network Interfaces (ENIs).
- **Dynamic IP assignment (AWS DHCP):** Automatically assign IPs from subnet pools at instance launch. Optimal for cloud-native applications and auto-scaling workloads. Reduces operational overhead but requires applications to use DNS or service discovery.

You can combine either range selection with either IP assignment method.

###### Note

IP addresses assignment strategy is set at the wave level. You can assign different strategies to specific servers by customizing the wave file. For example, if you chose a static IP address approach for the wave but want to assign a dynamic approach to a specific server, you would use `[RESET_VALUE]` as described in [Editing your configuration](../../../mgn/latest/ug/configuration-editing.md "../../../mgn/latest/ug/configuration-editing.md") in the _Application Migration Service user guide_.

## Step 5: Review VPC configurations

After AWS Transform generates Amazon VPC configurations, it displays the generated VPC networks. You can either use the current configuration or modify VPC CIDRs.

For single-account deployments, you can edit VPC CIDRs only. For multi-account deployments, you can also edit the target accounts for each VPC network.

###### Note

You cannot modify the prefix length (the value after the "/").

To modify VPC CIDRs:

1. In the Generated VPCs list, provide your modified CIDRs.
2. Choose **Submit** to apply the changes and rerun the mapping process.
3. Review the results, then either continue or repeat the modification steps.

## Step 6: Network diagram

After reviewing the generated VPC configurations, you can optionally generate a network diagram to visualize your network topology. AWS Transform supports the following diagram formats:

- **Mermaid code (.mmd):** A text-based diagram definition file that can be rendered using Mermaid-compatible tools.
- **Image (.png):** A rendered image of your network topology.

## Step 7: Configure resource tagging

AWS Transform tags your network resources for launch and replication, and supports custom tags and AWS Migration Acceleration Program (MAP) tags.

### Automatic tags for launch and replication

AWS Transform automatically tags migrated network resources (VPCs, subnets, security groups, and route tables) with the following tags:

- **Key:** `CreatedBy` **Value:** `AWSApplicationMigrationService`
- **Key:** `ATWorkspace` **Value:** `workspace-id`

These tags allow using the VPC and subnet for launching test and cutover instances in AWS.

###### Note

Network migration generates network segments without internet connectivity, so migrated VPCs and subnets are not suitable as staging areas for replication by default.

To also use the VPC and subnet as a staging area (replication), manually add the following tags:

- **Key:** `CreatedFor` **Value:** `AWSTransform`
- **Key:** `ATWorkspace` **Value:** `workspace-id`

You can also apply these tags to any existing AWS network resource to make it available for replication.

Find your workspace ID in the AWS Transform web app URL: https://... /workspace/`workspace-id`/job/job-id

### Custom tags

In addition to the tags applied automatically by AWS Transform, you can add custom tags to organize, track costs, and manage compliance for your migrated network resources. You can apply custom tags at two levels:

- **Job-level tags:** Apply to all resources created by this job, including all VPCs, subnets, security groups, and route tables.
- **VPC-level tags:** Apply to a specific VPC and automatically cascade to all its associated resources (subnets, security groups, route tables).

###### Note

Maximum 40 tags per request. Each tag requires a key and value. AWS tagging conventions apply.

AWS Transform applies these tags when generating the Infrastructure as Code templates.

### AWS Migration Acceleration Program

If your migration is part of the **AWS Migration Acceleration Program (MAP 2.0)**, AWS Transform applies a MAP tag to your resources. If you provided your MPE ID earlier in the migration process, the tag is applied automatically. Otherwise, after you finish reviewing the generated VPC configurations, AWS Transform asks whether you have a MAP agreement and prompts you to provide your MPE ID — a 10-character code using uppercase letters and digits (for example, ABCDE12345). The applied tag uses the format:

- **Key:** `map-migrated` **Value:** `mig`MPE_ID``

## Step 8: Deploy network

After tagging, select your deployment strategy:

- **AWS Transform-managed deployment:** AWS Transform uses CloudFormation templates to deploy your network and runs Reachability Analyzer to check connectivity between subnets across multiple VPCs and within the same VPC.

###### Note

Network deployment requests require explicit approval before execution. See the deployment approvals process below.

- **Self-deployment:** AWS Transform generates Infrastructure as Code (IaC) templates. CloudFormation templates are generated by default. You can also select additional output formats:
  - AWS CDK: TypeScript project for programmatic infrastructure deployment
  - HashiCorp Terraform: HCL templates for managing network resources
  - Landing Zone Accelerator (LZA): A network-config.yaml file for LZA network configuration

###### Note

When deploying via the Landing Zone Accelerator (LZA) pipeline, ensure that your AWS Transform account and LZA installation are in the same AWS Organization. Deployment will fail if there is a mismatch between the Organizations IDs.

For self-deployment, use the link provided to download a zip file containing the generated templates. The zip folder includes a README.md file that explains how to use the generated templates.

To verify the downloaded file hasn't been corrupted or tampered with, generate and download a checksum, then compare it to a locally generated hash using `openssl dgst -sha256 -binary <file.zip> | base64` command.

**Deployment approvals process**

Network deployment requests require explicit approval before execution. When you submit a deployment request, it automatically routes to authorized approvers through the AWS Transform Approvals tab. Approvers validate both CloudFormation templates and network configurations to ensure compliance with security standards and architectural requirements. Each submission triggers a new review cycle, and deployments proceed only after receiving confirmation. If an approver denies your request, contact them directly to discuss necessary modifications. The system tracks all approval decisions for audit purposes and maintains deployment history.

## Network deletion

After deployment, you can delete the deployed network resources. Deletion is available immediately after deployment completes. If you modify the deployed network resources after deployment, AWS Transform cannot delete them.

- **AWS Transform-managed deployments:** AWS Transform removes all CloudFormation stacks that were created during deployment. This action requires approval through the AWS Transform Approvals tab.
- **Self-deployments:** You must manually delete the deployed resources through the AWS Management Console or AWS CLI.

## Configuration file extraction

You can use Cisco ACI, Palo Alto Networks, and Fortinet FortiGate configuration files as standalone source files to generate network infrastructure and security groups, or as complementary files alongside an RVTools upload to add security group generation. The extraction process is the same in both cases.

To extract configuration files from your firewall and network environments, follow these procedures. Consult vendor documentation for the latest information.

### Fortinet FortiGate

- Firmware: v7.0 and up
- Requirements: `super_admin` or `super_admin_readonly` privileges on global level
- Steps:
  1.  Connect to the firewall via SSH or built-in CLI client
  2.  Run: `show | grep ""` (`| grep ""` disables pagination)
  3.  Save all output to a file starting from the `show` command

### Palo Alto Networks

- Firmware: 10.1 and up
- Requirements: superadmin role
- Steps: Connect via SSH, run the commands below, and save the outputs:

```
set cli pager off
set cli config-output-format set
configure
show              # Save as palo-conf.txt
show predefined   # Save as palo-default.txt
```

### Cisco ACI

- Firmware: 6.0 and up
- Requirements: Admin role with all privileges; SCP/SFTP/FTP destination configured
- Steps:
  1.  Connect to APIC controller via browser
  2.  Go to Admin >> Config Rollbacks
  3.  In "Take a snapshot" select remote location and choose "Create a snapshot now"
  4.  After receiving "Transfer successful" message, connect to the remote location server and retrieve the latest snapshot file (.gz file)
