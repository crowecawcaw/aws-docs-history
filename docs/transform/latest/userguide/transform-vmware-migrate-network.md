# Migrate network

AWS Transform can migrate your VMware networks to AWS. The migration process
translates your source environment configuration to an AWS-equivalent network.
AWS Transform analyzes your source network data and translates your source network to
these AWS networking resources as needed: VPCs, subnets, security groups, NAT
gateways, transit gateways, elastic IPs, routes, and route tables. AWS Transform then
creates AWS CloudFormation templates, AWS Cloud Development Kit (AWS CDK) templates, and and Hashicorp Terraform templates. You'll be able to review the
generated network configuration, and then either deploy it on your own or ask
AWS Transform to deploy it for you.

The translation process
requires you to upload a configuration file from your source environment. You can use [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools"), [Export for vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter"),
or [Import/Export for
NSX](https://github.com/awslabs/import-export-for-nsx/ "https://github.com/awslabs/import-export-for-nsx/") to capture on-premises-network data, and then import that file to AWS Transform. The
choice of tool depends on the type of source network that you have:

- If you have an NSX-defined network, upload an NSX configuration file using Import/Export for
  NSX.
- If you have a vSphere-constructs-defined network, you can upload an [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") file. AWS Transform will use
  that data to generate Amazon VPC configurations for you to review and deploy in
  your target AWS account. If you upload an [RVTools](https://www.dell.com/en-us/shop/vmware/sl/rvtools "https://www.dell.com/en-us/shop/vmware/sl/rvtools") file, AWS Transform won't

create security groups because **RVTools**
files don't include the information required to generate security
groups.
If your administrative workstation does not run Windows, RVTools is not approved in your
organization, or you want more granular control over the export file's
contents, use an [Export for vCenter](https://github.com/awslabs/export-for-vcenter "https://github.com/awslabs/export-for-vcenter") file, which generates a file in the same
format as RVTools.

Ensure that the target account has the required quotas.

###### Warning

The official RVTools site is [https://www.dell.com/en-us/shop/vmware/sl/rvtools](https://www.dell.com/en-us/shop/vmware/sl/rvtools " https://www.dell.com/en-us/shop/vmware/sl/rvtools"), which
is the site that this guide links to in steps that mention RVTools. Beware of
the scam site (rvtools)(dot)(org).

AWS Transform analyzes your source network data and translates your source
network to these AWS networking resources as needed: VPCs, subnets, security groups,
NAT gateways, transit gateways, internet
gateways, elastic IPs, routes, and route tables.

If you want the target network to contain different IP ranges than your source
network you can modify your VPC CIDR ranges during migration. AWS Transform
automatically propagates changes to subnets, route tables, and security groups, and
then assigns static IPs based on the CIDR. This is best for applications requiring
predictable network behavior, DNS management, or IP-based access control. IP
addresses persist across instance restarts using Elastic Network Interfaces
(ENIs).

For NSX environments, you can choose to have AWS Transform automatically convert security
policies and gateway policies to Security Groups, associating them with network
interfaces based on VM external IDs and IP addresses. In this case you will not have the option to use dynamic IP assignment (DHCP)
for your target instances because IP
addresses aren't known until instance launch.

AWS Transform then creates CloudFormation templates and AWS Cloud Development Kit (AWS CDK) templates.

Once the target network is generated, review the generated network configuration.
You can either deploy it on your own or ask AWS Transform to deploy it for you. If
you choose to let AWS Transform deploy the network for you, it also uses tools
such as [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to run an analysis to check connectivity
between subnets across multiple VPCs and under the same VPC. If you choose to make
changes to the generated configuration, you must deploy the modified configuration
yourself.

## Source Network Convergence

During end-to-end migration or network-only migration jobs, AWS Transform
creates AWS Virtual Private Clouds (VPCs) from all source network segments in
the **Generate VPC Configuration** stage. Each
detected network segment becomes its own distinct VPC.

Network segmentation by source type:

- For vNetwork: AWS Transform groups VMs by vSwitch and VLAN, with VLAN presented under multiple vSwitches (except for VLAN 0).
- For NSX networks: AWS Transform segments the network based on Tier-1 routers by grouping the routers and collecting the segments.

## Network Topologies

During the migration to the target network you can choose the Isolated VPCs topology or the Hub and Spoke topology.

###### Important

For both topologies, AWS Transform does not open the communication to the internet. You must open it manually after taking appropriate security precautions.

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

## Network configuration generators

AWS Transform provides multiple generators for creating network infrastructure
code from your migrated network configuration. These are available to you in the
**Migrate Network** task, after you **Generate VPC
configuration** and **Review generated VPC
configuration**. When you choose the **Deploy on my
own** option AWS Transform for VMware gives you the option to generate Infrastructure-as-Code (IaC) templates in four formats:

- **CloudFormation** templates that you can use to provision your network
  resources.
- **CDK project** - AWS Cloud Development Kit (AWS CDK) templates generated in TypeScript for programmatic infrastructure deployment
- **HashiCorp Terraform** - Infrastructure as Code (IaC) templates generated in HashiCorp Configuration Language (HCL) for managing network resources
- **Landing Zone Accelerator by AWS** - A
  `network-config.yaml` file that works with LZA network
  configuration. Learn more about the Landing Zone Accelerator solution
  and how to deploy the network configuration YAML in [Using configuration files](../../../solutions/latest/landing-zone-accelerator-on-aws/using-configuration-files.md "../../../solutions/latest/landing-zone-accelerator-on-aws/using-configuration-files.md") in the _Landing Zone
  Accelerator on AWS Implementation Guide_.

###### Note

When deploying this network configuration via the Landing Zone Accelerator (LZA) pipeline,
ensure that your AWS Transform account and LZA installation are in the same AWS Organization. Deployment will fail if there is a mismatch between the Organizations IDs
used in AWS Transform and LZA. To learn how to set up your LZA installation
using Organizations see [AWS Organizations based installation (without AWS Control Tower)](../../../solutions/latest/landing-zone-accelerator-on-aws/prerequisites.md#for-aws-organizations-based-installation-without-aws-control-tower "../../../solutions/latest/landing-zone-accelerator-on-aws/prerequisites.md#for-aws-organizations-based-installation-without-aws-control-tower").

After you select a network configuration format, use the link provided on the
**Download and deploy networks** -
**Collaboration** tab to download a zip file containing the
generated templates. The zip folder includes a README.md file that explains how
to use the generated templates.

###### Note

To ensure that the downloaded file hasn’t been corrupted or tampered with during transfer,
generate and download a checksum from **Optional tasks**
and compare the hash to a locally generated hash. Generate the local hash
using the `openssl dgst -sha256 -binary <file.zip> |
 base64` command.

The network configuration generators generate these key components:

### Hub and Spoke Network Architecture

For details see [Hub and spoke](#hub-and-spoke "#hub-and-spoke") in
the [Network topologies](#network-topologies "#network-topologies")
section.

### Network Segments Configuration

The infrastructure creates VPC segments for organizing workloads and managing network traffic flow.

### Security Configuration

- **Comprehensive Security Groups:** Pre-configured rules for different network segments
- **Network Definitions:** CIDR block definitions for consistent referencing
- **Rule Templates:** Modular security rules supporting ingress/egress traffic control

### Application Migration Service Integration

- **Automatic Tagging:** All resources tagged with MGN definition and execution IDs
- **Migration Tracking:** Resources tagged for Application Migration Service tracking
- **Execution Context:** Unique execution ID for deployment correlation

### Reusable Modules

The generated configuration includes a modular structure for
maintainability and reusability

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

IP strategy is set at the wave level. You can assign different strategies to specific servers
by customizing the wave file. For example if you chose a static IP address
approach for the wave, but want to assign a dynamic approach to a specific
server, you would use `[RESET_VALUE]` as described in [Editing your configuration](../../../mgn/latest/ug/configuration-editing.md "../../../mgn/latest/ug/configuration-editing.md") In the _Application Migration Service user
guide_.

## Generate VPC configuration

###### To import network data

1. In the **Job Plan** pane, choose **Migrate
   network**.
2. Expand **Generate VPC configuration**.
3. Choose **Import network data**.
4. In the **Network source data** section, either select
   an existing import, or choose **Upload file** to
   import a new file to add to the list, and then select the file that you
   uploaded.
5. In the **Network topology** section, the topology
   that you want AWS Transform to generate.
6. Choose **Generate VPC configuration**.
7. After AWS Transform generates a Amazon VPC configuration, choose
   **Review generated VPC configuration**.

In this step you can choose to either
**use the current configuation** or **Modify your VPC CIDRs**. You cannot
modify the prefix length, which comes after the "/".

To modify your VPC CIDRs:

    1. In the **Generated VPCs** list provide your modified CIDRs.
    2. Choose the **Regenerate network** button.


    Review the results and then choose to continue with network
     deployment or to repeat the **Modify your VPC CIDRs** and **Regenerate network** steps.

8. Review the generated
   network configuration, and then choose **Deploy using AWS Transform** or **Deploy on my own**. If you make changes to the generated configuration
   you have to deploy the modified configuration yourself. If you choose to let
   AWS Transform deploy the network for you, it uses tools such as
   [Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") to run an analysis
   to check connectivity between subnets across multiple VPCs and under the same VPC.

## Tag network resources

For AWS Transform to launch Amazon EC2 instances within your existing AWS network
resources which were not created by AWS Transform, the target network resources, including VPCs and subnets, must
be tagged. You can ask AWS Transform to do the tagging for you, in which case it
tags **all** network resources that it finds in
the target AWS account and AWS Region. You can also manually tag target
network resources that you’ve created on your own with the following tags:

Key: `CreatedFor` Value: `AWSTransform`

Key: `ATWorkspace` Value: `workspace ID`

Find your workspace ID in the AWS Transform web app URL, https:// ... /workspace/`workspace-id`/job/job-id

Learn more about how to tag network resources in [Tag your VPCs and subnets](transform-vmware-migrate-waves.md#transform-tag-vpc-subnets "transform-vmware-migrate-waves.md#transform-tag-vpc-subnets") .

## Security group

association

When you migrate networks from an NSX source environment, AWS Transform creates
security groups based on your source environment configurations.

###### Important

AWS Transform makes a best effort to create security groups that match
your source environment. It is your responsibility to review and, if necessary, modify the security
groups to ensure that they meet your company's needs and security policies.

AWS Transform converts the following NSX configurations to security groups:

- Security policies and security policy rules
- Gateway policies and gateway policy rules

The association is based on the `source_groups` for outbound
communication, and on the `destination_groups` for inbound
communication. During server migration (import inventory), AWS Transform uses the
following logic to associate these security groups with the appropriate network
interfaces:

- Rules associated to a VM external ID are attached to all of the
  elastic network interfaces of the given VM.
- Rules associated to an IP are attached to the network interface with
  the specific IP.
- _Exclude_ rules are ignored. However, you can
  manually create replacements for them.

The association maintains the security rules specified in the inventory
import. The migration process creates encoded mapping files, one per VPC in your
Amazon S3 bucket, that link VM external identifiers and IP addresses to the security
groups they should be bound to. Follow AWS best practices to secure these
files because they contain sensitive information about mappings. For guidance,
see [Data protection in AWS Transform](data-protection.md "data-protection.md").

###### Important

Do not modify these mapping files, as they are essential for proper
security group association. Modifying these files will cause a failure
during the import inventory phase.

Security groups removed from the VPC after network deployment will not be
associated with migrated servers.

During import, AWS Transform automatically deduplicates security groups based on
their ID so as to remove redundant assignments.
