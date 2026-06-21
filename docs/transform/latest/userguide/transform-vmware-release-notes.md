# Release notes

The following release notes cover the latest changes to [VMware migration](transform-app-vmware.md "transform-app-vmware.md").
For supported AWS Transform regions, see [Supported Regions](regions.md "regions.md"). For supported target
regions, see the [account
connector setup page](transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions "transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions").

## June 2026

- AWS Transform now allows you to configure your replication settings and launch settings for
  your migration. You can set the configuration per your target account or across specific
  source servers. [Learn
  more about replication and launch settings](transform-vmware-migrate-servers.md#transform-vmware-ms-prereqs-and-defaults "transform-vmware-migrate-servers.md#transform-vmware-ms-prereqs-and-defaults").
- AWS Transform now allows you to attach existing Elastic Network Interfaces (ENIs) to your
  launch template for your migration. AWS Transform displays all existing ENIs found in your target
  account, and you can tag them so that they are available for use through the launch
  configuration when instances are launched. [Learn
  more about network resource tagging](transform-vmware-migrate-servers.md#transform-vmware-ms-resource-tagging "transform-vmware-migrate-servers.md#transform-vmware-ms-resource-tagging").
- AWS Transform for VMware migrations now supports all AWS commercial regions as migration
  targets, excluding Middle East (Bahrain) and Middle East (UAE). A migration target region
  is the AWS Region where migrated resources are deployed, including landing zones, network
  infrastructure, and server rehosting. [Learn
  more about supported target regions](transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions "transform-vmware-connect-target-account.md#transform-vmware-cta-supported-regions").

## May 2026

- AWS Transform now detects existing VPCs in your target account during network migration review.
  You can see existing VPCs alongside your mapped VPCs, identify CIDR conflicts, and resolve
  them before deployment. [Learn
  more about existing VPC detection](transform-vmware-migrate-network.md#transform-vmware-brownfield-network "transform-vmware-migrate-network.md#transform-vmware-brownfield-network").
- AWS Transform supports replatforming source code repositories to containers during migration
  to AWS. [Learn more about
  containerization](transform-containers.md "transform-containers.md").

## April 2026

- Added landing zone creation directly within migration workflows. AWS Transform checks for an
  existing foundation, recommends Organizational Unit (OU) structures and target accounts, and
  offers fully automated deployment or Infrastructure as Code (IaC) output (CloudFormation, AWS CDK, or
  Landing Zone Accelerator (LZA) formats). [Learn more about landing
  zone creation](transform-vmware-landing-zone.md "transform-vmware-landing-zone.md").
- Added support for DHCP with security group mapping during network migration. If you have
  DHCP-enabled migration workloads, you can now ensure your security rules remain valid after
  migration. This applies to both in-VPC security group referencing and cross-VPC and
  cross-account outbound rules via Transit Gateway. [Learn
  more about security group creation](transform-vmware-migrate-network.md#transform-vmware-security-group-association "transform-vmware-migrate-network.md#transform-vmware-security-group-association").

## March 2026

- Added public APIs for network migration, enabling partner and programmatic access to network
  migration capabilities. See the [network
  migration API reference](../../../mgn/latest/APIReference.md "../../../mgn/latest/APIReference.md").

## February 2026

- Network migration now supports ingesting [firewall
  or Software-Defined Networking (SDN) configuration files](transform-vmware-migrate-network.md#transform-vmware-firewall-and-sdn-config-files "transform-vmware-migrate-network.md#transform-vmware-firewall-and-sdn-config-files") without requiring [RVTools discovery
  data](transform-vmware-discover-source-data.md "transform-vmware-discover-source-data.md"). You can use firewall or SDN configuration files independently, or combine
  them with RVTools exports.

## January 2026

- Added support for [Migration
  Acceleration Program (MAP) tagging and user-defined tagging](transform-vmware-setup-service-permissions.md "transform-vmware-setup-service-permissions.md") on network migration
  elements, enabling you to track migration resources for MAP credit and organizational
  purposes.

## December 2025

- Added a new [VMware migration experience](vmware-jobs.md "vmware-jobs.md") with
  redesigned workflow and improved usability. For more information, see [Accelerating
  VMware migration: AWS Transform's new experience](https://aws.amazon.com/blogs/migration-and-modernization/accelerating-vmware-migration-aws-transforms-new-experience/ "https://aws.amazon.com/blogs/migration-and-modernization/accelerating-vmware-migration-aws-transforms-new-experience/").
- Added [Landing
  Zone Accelerator (LZA) network configuration](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-transform-landing-zone-accelerator-network-configuration/ "https://aws.amazon.com/about-aws/whats-new/2025/11/aws-transform-landing-zone-accelerator-network-configuration/") for automated landing zone
  setup.
- Added support for [multiple target
  AWS accounts](migration-multiple-target-accounts.md "migration-multiple-target-accounts.md") in migration execution, enabling you to migrate workloads across
  accounts.
- Added network migration support for [Cisco
  ACI, Palo Alto, FortiGate, and ModelizeIT source formats](transform-vmware-migrate-network.md#transform-vmware-source-network-mapping "transform-vmware-migrate-network.md#transform-vmware-source-network-mapping").

## October 2025

- Expanded migration execution to [16 target
  regions](transform-app-vmware-acct-connections.md "transform-app-vmware-acct-connections.md") with the addition of Asia Pacific (Osaka).

## September 2025

- Added support for licensing configuration in [rehost waves](transform-vmware-migrate-waves.md "transform-vmware-migrate-waves.md"),
  enabling you to specify Bring Your Own License (BYOL) or license-included options per
  wave.
- Added support for [Terraform
  in network migration](transform-vmware-migrate-network.md#transform-vmware-deploy-network "transform-vmware-migrate-network.md#transform-vmware-deploy-network"), enabling you to deploy network infrastructure using
  Terraform templates.
- Added support for updating replication subnet configuration, removing the requirement for a
  default VPC in the target account.

## August 2025

- Expanded migration execution (network migration and rehost) to [15 target
  regions](transform-app-vmware-acct-connections.md "transform-app-vmware-acct-connections.md") with the addition of US East (Ohio), Europe (Stockholm), and Europe
  (Ireland).
- Added [flexible
  CIDR range capabilities](transform-vmware-migrate-network.md#vmware-migration-ip "transform-vmware-migrate-network.md#vmware-migration-ip") for network migration, enabling you to customize IP
  address ranges during network deployment.

## May 2025

- Initial service launch of [VMware migration](transform-app-vmware.md "transform-app-vmware.md"), providing end-to-end
  VMware to AWS migration capabilities including [discovery](transform-vmware-discover-source-data.md "transform-vmware-discover-source-data.md"),
  assessment, [migration
  planning](transform-vmware-review-groupings-and-waves.md "transform-vmware-review-groupings-and-waves.md"), network migration, and server rehost.
- Supported migration execution in 12 [target
  regions](transform-app-vmware-acct-connections.md "transform-app-vmware-acct-connections.md"): US East (N. Virginia), US West (Oregon), Canada (Central), South America
  (São Paulo), Europe (Frankfurt), Europe (London), Europe (Paris), Asia Pacific (Mumbai), Asia
  Pacific (Seoul), Asia Pacific (Tokyo), Asia Pacific (Singapore), and Asia Pacific
  (Sydney).
