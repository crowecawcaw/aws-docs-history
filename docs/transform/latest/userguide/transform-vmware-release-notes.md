

# Release notes
<a name="transform-vmware-release-notes"></a>

The following release notes cover the latest changes to [Migrations (including VMware)](transform-app-vmware.md). For a list of changes across the full AWS Transform service, see the [changelog](https://docs.aws.amazon.com/transform/latest/userguide/change-log.html).

For supported AWS Transform regions, see [Supported Regions](https://docs.aws.amazon.com/transform/latest/userguide/regions.html). For supported target regions, see the [account connector setup page](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-connect-target-account.html#transform-vmware-cta-supported-regions).

## August 2026
<a name="transform-vmware-release-notes-august-2026"></a>
+ AWS Transform for migrations now lets you apply your source security posture to VPCs you have already provisioned in AWS, instead of creating new VPCs. You upload a source network file that contains firewall rules, tag the existing VPCs you want in scope, and AWS Transform matches your source subnets to those VPCs by CIDR and generates the corresponding security groups. [Learn more about applying security posture to existing VPCs](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-apply-security-posture.html).
+ AWS Transform for migrations now identifies unused inbound firewall rules migrated from your on-premises environment and suggests removing them as part of guided network recommendations. This helps you avoid carrying forward security exposure, such as open inbound access, that no longer serves a purpose. Removal is limited to unused ingress rules. [Learn more about guided network recommendations](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-guided-recommendations).
+ AWS Transform for migrations now flags VPCs that host applications from multiple environments, such as development and production, as part of guided network recommendations. When the environments can be cleanly separated, AWS Transform suggests splitting the VPC to isolate them. [Learn more about guided network recommendations](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-guided-recommendations).

## July 2026
<a name="transform-vmware-release-notes-july-2026"></a>
+ AWS Transform for migrations now supports migrating virtual and bare metal server environments from virtually any source, including VMware, Hyper-V, and other platforms. Migration capabilities, including discovery, migration planning, landing zone creation, network migration, and server rehost, are available regardless of your source infrastructure. The web application workflow has been renamed from "VMware Migrations" to "Migrations (including VMware)". [Learn more about migrations](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html).
+ AWS Transform now lets you generate a workspace summary report as a downloadable PDF. The report consolidates data from all migration jobs in your workspace, including job statuses, workflow step progress, wave planning, network migration, landing zone configuration, rehost progress, and artifacts produced. [Learn more about workspace summary reports](https://docs.aws.amazon.com/transform/latest/userguide/vmware-jobs.html#transform-app-vmware-workspace-summary-report).
+ The AWS Transform discovery tool now collects detailed Oracle metadata directly from your databases across VMware, Hyper-V, and bare metal servers. You can discover Oracle instances through direct SQL connections. The tool collects Container Database/Pluggable Database (CDB/PDB) enumeration, component inventory, and datafile sizing. [Learn more about Oracle Database discovery](https://docs.aws.amazon.com/transform/latest/userguide/discovery-tool.html).
+ AWS Transform for migrations now provides enhanced capabilities for post-launch actions. You can now define post-launch actions at the account level and apply them to all source servers automatically, or customize them per source server during inventory validation. Post-launch actions automate modernization and validation tasks on each source server immediately after it launches as a test or cutover instance. [Learn more about post-launch actions](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html#transform-vmware-ms-post-launch-actions).

## June 2026
<a name="transform-vmware-release-notes-june-2026"></a>
+ AWS Transform for migrations now supports localization. You can change the display language of the web application when working with migration workflows. [Learn more about language settings](https://docs.aws.amazon.com/transform/latest/userguide/transform-environment.html#transform-environment-language).
+ AWS Transform now allows you to configure your replication settings and launch settings for your migration. You can set the configuration per your target account or across specific source servers. [Learn more about replication and launch settings](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html#transform-vmware-ms-prereqs-and-defaults).
+ AWS Transform now allows you to attach existing Elastic Network Interfaces (ENIs) to your launch template. You can tag ENIs in your target account so they are available for use when instances are launched. [Learn more about network resource tagging](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-servers.html#transform-vmware-ms-resource-tagging).
+ AWS Transform for migrations now supports all AWS commercial regions as migration targets, excluding Middle East (Bahrain) and Middle East (UAE). [Learn more about supported target regions](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-connect-target-account.html#transform-vmware-cta-supported-regions).
+ You can now use the AWS Transform discovery tool as a source for network migration alongside modelizeIT, enabling hybrid network migrations for environments running both VMware and non-VMware workloads. [Learn more about network migration input sources](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network.html).

## May 2026
<a name="transform-vmware-release-notes-may-2026"></a>
+ AWS Transform now detects existing VPCs in your target account during network migration review. You can see existing VPCs alongside your mapped VPCs, identify CIDR conflicts, and resolve them before deployment. [Learn more about existing VPC detection](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-brownfield-network).
+ AWS Transform supports replatforming source code repositories to containers during migration to AWS. [Learn more about containerization](https://docs.aws.amazon.com/transform/latest/userguide/transform-containers.html).
+ AWS Transform can now analyze your discovered inventory and provide a migration strategy recommendation for every server and application. Recommendations follow the industry-standard seven migration strategies (7Rs). Each recommendation includes a suggested AWS target service, a confidence score, and the reasoning behind it. [Learn more about 7Rs recommendations](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-r-strategy-report.html).

## April 2026
<a name="transform-vmware-release-notes-april-2026"></a>
+ Added landing zone creation directly within migration workflows. AWS Transform checks for an existing foundation, recommends Organizational Unit (OU) structures and target accounts, and offers automated deployment or Infrastructure as Code (IaC) output (CloudFormation, AWS CDK, or Landing Zone Accelerator (LZA) formats). [Learn more about landing zone creation](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-landing-zone.html).
+ Added support for DHCP with security group mapping during network migration. [Learn more about security group creation](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-security-group-association).
+ You can now generate interactive diagrams and analytical reports during migration planning. Diagram types include network topology maps, application dependency graphs, wave Gantt charts, and general charts. Report types include risk assessments, 7Rs recommendations, and custom analytical reports. Outputs are available as interactive HTML, PDF, or Microsoft PowerPoint (.pptx) files. [Learn more about migration-planning diagrams and reports](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-diagrams-and-reports.html).

## March 2026
<a name="transform-vmware-release-notes-march-2026"></a>
+ Added public APIs for network migration, enabling partner and programmatic access to network migration capabilities. See the [network migration API reference](https://docs.aws.amazon.com/mgn/latest/APIReference/).

## February 2026
<a name="transform-vmware-release-notes-february-2026"></a>
+ Network migration now supports ingesting [firewall or Software-Defined Networking (SDN) configuration files](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-firewall-and-sdn-config-files) without requiring [RVTools discovery data](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-discover-source-data.html). You can use firewall or SDN configuration files independently, or combine them with RVTools exports.

## January 2026
<a name="transform-vmware-release-notes-january-2026"></a>
+ Added support for [Migration Acceleration Program (MAP) tagging and user-defined tagging](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-setup-service-permissions.html) on network migration elements, enabling you to track migration resources for MAP credit and organizational purposes.

## December 2025
<a name="transform-vmware-release-notes-december-2025"></a>
+ Added a new [migration experience](https://docs.aws.amazon.com/transform/latest/userguide/vmware-jobs.html) with redesigned workflow and improved usability. For more information, see [Accelerating VMware migration: AWS Transform's new experience](https://aws.amazon.com/blogs/migration-and-modernization/accelerating-vmware-migration-aws-transforms-new-experience/).
+ Added [Landing Zone Accelerator (LZA) network configuration](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-transform-landing-zone-accelerator-network-configuration/) for automated landing zone setup.
+ Added support for [multiple target AWS accounts](https://docs.aws.amazon.com/transform/latest/userguide/migration-multiple-target-accounts.html) in migration execution, enabling you to migrate workloads across accounts.
+ Added network migration support for [Cisco ACI, Palo Alto, FortiGate, and ModelizeIT source formats](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-source-network-mapping).

## October 2025
<a name="transform-vmware-release-notes-october-2025"></a>
+ Expanded migration execution to [16 target regions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware-acct-connections.html) with the addition of Asia Pacific (Osaka).

## September 2025
<a name="transform-vmware-release-notes-september-2025"></a>
+ Added support for licensing configuration in [rehost waves](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-waves.html), enabling you to specify Bring Your Own License (BYOL) or license-included options per wave.
+ Added support for [Terraform in network migration](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#transform-vmware-deploy-network), enabling you to deploy network infrastructure using Terraform templates.
+ Added support for updating replication subnet configuration, removing the requirement for a default VPC in the target account.

## August 2025
<a name="transform-vmware-release-notes-august-2025"></a>
+ Expanded migration execution (network migration and rehost) to [15 target regions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware-acct-connections.html) with the addition of US East (Ohio), Europe (Stockholm), and Europe (Ireland).
+ Added [flexible CIDR range capabilities](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-migrate-network-new-vpcs.html#ip-migration-approaches) for network migration, enabling you to customize IP address ranges during network deployment.

## May 2025
<a name="transform-vmware-release-notes-may-2025"></a>
+ Initial service launch of [Migrations (including VMware)](transform-app-vmware.md), providing end-to-end migration capabilities including [discovery](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-discover-source-data.html), assessment, [migration planning](https://docs.aws.amazon.com/transform/latest/userguide/transform-vmware-review-groupings-and-waves.html), network migration, and server rehost.
+ Supported migration execution in 12 [target regions](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware-acct-connections.html): US East (N. Virginia), US West (Oregon), Canada (Central), South America (São Paulo), Europe (Frankfurt), Europe (London), Europe (Paris), Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Tokyo), Asia Pacific (Singapore), and Asia Pacific (Sydney).