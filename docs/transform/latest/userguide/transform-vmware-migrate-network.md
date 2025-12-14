# Migrate network

AWS Transform migrates VMware networks to AWS by translating your source environment configuration into AWS-equivalent network resources. AWS Transform
analyzes your source network data and creates VPCs, subnets, security groups, NAT gateways, transit gateways, elastic IPs, routes, and route tables as needed. You can review and modify the generated network configuration before deployment. For deployment, you can either have AWS Transform deploy the configuration for you and analyze deployed network connectivity, or choose self-deployment—in which case AWS Transform generates Infrastructure as Code (IaC) in your preferred format: AWS Cloud Development Kit (AWS CDK) (AWS CDK), Landing Zone Accelerator (LZA), or HashiCorp Terraform.

## Source Network Mapping

The network mapping process requires uploading a configuration file from your source environment. You can use RVTools, Export for vCenter, or Import/Export for NSX to capture on-premises network data and import it to AWS Transform. The tool you choose depends on your source network type:

- **NSX-defined network:** Upload an NSX configuration file using Import/Export for NSX.
- **vSphere-defined network:** Upload an RVTools file or Export for vCenter file. When using RVTools files, AWS Transform will focus on generate Amazon VPC configurations,
  while security group configurations require additional input. For network security settings, you may upload configuration files from additional sources like firewalls and software-defined networks. See [Additional Configuration Files](#transform-vmware-additional-config-files "#transform-vmware-additional-config-files") for more details.
- **Non-Windows workstation or need granular control:** Use Export for vCenter, which generates files in the same format as RVTools.

###### Warning

The official RVTools site is [https://www.dell.com/en-us/shop/vmware/sl/rvtools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools"), which is the site that this guide links to in steps that mention RVTools. Beware of the scam site (rvtools)(dot)(org).

AWS Transform creates VPCs from all source network segments, with each detected segment becoming its own distinct VPC. Network segmentation varies by source type:

- **vNetwork:** AWS Transform groups VMs by vSwitch and VLAN. VLANs can appear under multiple vSwitches (except VLAN 0).
- **NSX networks:** AWS Transform segments the network based on Tier-1 routers, grouping the routers and collecting their segments.

The network mapping process generates these key resources:

- **Network topology:** Network deployment best practice for implementation. See the Network topologies section for more details.
- **Workload segment configuration:** Amazon VPC segments with CIDR block definitions for organizing workloads and managing network traffic flow.
- **Security configuration:** Pre-configured access rules for different network segments, supporting ingress and egress traffic control.

###### Note

AWS Transform tags all generated resources with "CreatedBy": "AWSTransform" along with definition and execution IDs for tracking and management purposes.

## Additional Configuration Files

AWS Transform supports additional configuration files that enable automated security group generation when combined with RVTools files. You can upload configuration files from the following enterprise solutions:

- Cisco Application Centric Infrastructure (ACI): Network policy configurations
- Palo Alto Networks: Firewall security policies
- Fortinet FortiGate: Firewall security policies

When you upload a combination of RVTools and one or more of these configuration files, AWS Transform generates both the target VPC network infrastructure and corresponding security groups based on your existing security policies. This preserves your security investments and ensures consistent policy enforcement in AWS.

To extract configuration files from firewall and network environments, follow these procedures. Consult vendor documentation for the latest information.

### Fortinet FortiGate

- Firmware: 7.0 - 7.6
- Requirements: super_admin or super_admin_readonly privileges
- Steps: Connect via SSH, run `show | grep ""` (| grep "", save output to file

### Palo Alto Networks

- Firmware: 10.1.X
- Requirements: superadmin role
- Steps: Connect via SSH, run commands below, save outputs to palo-conf.txt and palo-default.txt:
  - `set cli pager off`
  - `set cli config-output-format set`
  - `configure`
  - `show` # Save as palo-conf.txt
  - `show predefined` # Save as palo-default.txt

### Cisco ACI

- Firmware: 6.3+
- Requirements: Admin role with all privileges; SCP/SFTP/FTP destination configured
- Steps:
  - Connect to APIC controller via browser
  - Go to Admin and Config Rollbacks
  - Select remote location and select "Create a snapshot now" option
  - Retrieve .gz file after "Transfer successful" message.

## Network Topologies

During the migration to the target network you can choose the **Isolated VPCs** topology or the **Hub and Spoke** topology.

###### Important

For both topologies AWS Transform does not open the communication to the internet.
You must open it manually after taking appropriate security
precautions.

### Isolated VPCs

These are independent network environments that operate as separate units within AWS . VPCs maintain complete network isolation, with no built-in communication pathways between them. This separation provides the highest level of network boundary protection. You can connect the VPCs through specific networking configurations if needed.

### Hub and Spoke

In this model, an AWS Transit Gateway created by AWS Transform acts as the hub that connects to multiple workload VPCs (the spokes). During network convergence, AWS Transform creates a spoke VPC for each detected source network segment.

AWS Transform creates three specialized VPCs for traffic management and security:

- Inspection VPC: Where you establish the firewall that inspects the traffic. You can create firewall rule configurations here to modify VPC connections.
- Inbound VPC: For all traffic from the public internet (north-south). Includes an internet gateway.
- Outbound VPC: For all traffic to the public internet. Has an internet gateway, a Network Address Translation (NAT) gateway and an [elastic IP address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md").

AWS Transform automatically associates all spoke VPCs with the default association route table and propagates routes from all spoke VPCs to the default propagation route table. This automation creates routing paths without manual configuration, though traffic flow remains subject to security group permissions.

If you want fine-grained control over the communication between the VPCs, choose the
**Isolated VPCs** option and modify the generated network to create the specific communication
paths your require.

## IP migration approaches

The system offers two key network configuration choices for your migration

**Network range selection:**

- **Keep Existing Ranges (IP Address Ranges
  Retention):** Keep original IP address ranges during
  migration. Ideal for lift-and-shift scenarios with legacy applications
  that have hard-coded IP dependencies or existing firewall rules.
- **Update to new IP ranges (CIDR update):**
  You can modify each VPC CIDR range during migration, and AWS Transform
  automatically propagates changes to subnets, route tables, and security
  groups.

**IP addresses assignment:**

- **Fixed IP addresses (Static):** the system
  assigns static IPs based on the CIDR. This is best for applications
  requiring predictable network behavior, DNS management, or IP-based
  access control. IPs persist across instance restarts using Elastic
  Network Interfaces (ENIs).
- **Dynamic IP assignment (AWS DHCP):**
  Automatically assign IPs from subnet pools at instance launch. Optimal
  for cloud-native applications and auto-scaling workloads. Reduces
  operational overhead but requires applications to use DNS or service
  discovery.

You can combine either range selection with either IP assignment method.

###### Note

IP addresses assignment strategy is set at the wave level. You can assign different strategies to specific servers
by customizing the wave file. For example if you chose a static IP address
approach for the wave, but want to assign a dynamic approach to a specific
server, you would use `[RESET_VALUE]` as described in [Editing your configuration](../../../mgn/latest/ug/configuration-editing.md "../../../mgn/latest/ug/configuration-editing.md") In the _Application Migration Service user
guide_.

###### Important

When you choose to create security groups, you cannot use Dynamic Host Configuration Protocol (DHCP) for server migrations.
Security groups use Classless Inter-Domain Routing (CIDR) configurations, and enabling DHCP could compromise your network's security posture.

## Review VPC Configurations

After AWS Transform generates Amazon VPC configurations, it displays the generated VPC networks. You can either use the current configuration or modify VPC CIDRs. Note: You cannot modify the prefix length (the value after the "/") or any other resources.

To modify VPC CIDRs:

1. In the Generated VPCs list, provide your modified CIDRs.
2. Choose **Submit** to apply the changes
   and rerun the mapping process.
3. Review the results, then either continue with network deployment or repeat the modification steps.

## Deploy Network

After reviewing and approving the generated network configuration, choose to deploy using AWS Transform or on your own.

###### Note

Ensure your target account has the required quotas before beginning deployment.

Deployment Options:

- **AWS Transform-managed deployment:** AWS Transform uses CloudFormation templates to deploy your network and runs Reachability Analyzer to check connectivity between subnets across multiple VPCs and within the same VPC.

###### Note

Network deployment requests require explicit approval before execution. See [Deployment approvals process](#transform-vmware-deployment-approvals "#transform-vmware-deployment-approvals") for more details.

- **Self-deployment:** AWS Transform generates Infrastructure as Code (IaC) templates in the following formats:
  - CloudFormation: Templates for provisioning network resources
  - AWS CDK: TypeScript project for programmatic infrastructure deployment
  - HashiCorp Terraform: HCL templates for managing network resources
  - Landing Zone Accelerator (LZA): A network-config.yaml file for LZA network configuration. See Using configuration files in the Landing Zone Accelerator on AWS Implementation Guide.

###### Note

When deploying this network configuration via the Landing Zone Accelerator (LZA) pipeline, ensure that your AWS Transform account and LZA installation are in the same AWS Organization. Deployment will fail if there is a mismatch between the Organizations IDs used in AWS Transform and LZA. To learn how to set up your LZA installation using Organizations see AWS Organizations based installation (without AWS CloudTrail).

After you select a network configuration format, use the link provided to download a zip file containing the generated templates. The zip folder includes a README.md file that explains how to use the generated templates.

To verify the downloaded file hasn't been corrupted or tampered with, generate and download a checksum, then compare it to a locally generated hash using `openssl dgst -sha256 -binary <file.zip> | base64` command.

## Deployment approvals process

Network deployment requests require explicit approval before execution. When you submit a deployment request, it automatically routes to authorized approvers through the AWS Transform Approvals tab. Approvers validate both CloudFormation templates and network configurations to ensure compliance with security standards and architectural requirements. Each submission triggers a new review cycle, and deployments proceed only after receiving confirmation. If an approver denies your request, contact them directly to discuss necessary modifications. The system tracks all approval decisions for audit purposes and maintains deployment history.

## Security group association

AWS Transform creates security groups based on your source environment configurations when migrating from NSX environments. AWS Transform can generate security groups from RVTools files when combined with Additional configuration files from sources such as firewalls and software-defined networks.

###### Important

AWS Transform makes a best effort to create security groups that match your source environment. It is your responsibility to review and, if necessary, modify the security groups to ensure that they meet your company's needs and security policies.

AWS Transform converts the following configurations to security groups:

- Security policies and security policy rules
- Gateway policies and gateway policy rules

## Tag network resources

To use existing AWS network resources not created by AWS Transform, you must tag the resources (including VPCs and subnets). AWS Transform can tag resources during migration wave execution—it will tag all network resources in the target AWS account and Region. Alternatively, you can manually tag network resources you've created with the following tags:

- **Key:** CreatedFor **Value:** AWSTransform
- **Key:** ATWorkspace **Value:** workspace ID

Find your workspace ID in the AWS Transform web app URL, https:// ... /workspace/`workspace-id`/job/job-id

Learn more about how to tag network resources in [VPC and subnet tags](transform-vmware-migrate-waves.md#transform-tag-vpc-subnets "transform-vmware-migrate-waves.md#transform-tag-vpc-subnets").
