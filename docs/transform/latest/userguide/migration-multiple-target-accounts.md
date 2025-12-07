# Migration to multiple target accounts

AWS Transform supports migrating VMware workloads to multiple AWS accounts simultaneously. This capability enables you to migrate workloads directly to their intended target accounts while maintaining your organization's security boundaries and governance structures.

## Benefits

Multi-account migration provides the following benefits:

- _Maintain security boundaries_ - Migrate workloads directly to accounts that align with your business units and security requirements
- _Unified management_ - Control the entire migration process from a single management interface

## Limitations

Multi-account migration has the following limitations:

- _Single region only_ - You can migrate to multiple accounts within a single AWS Region. For multi-region migrations, you must create separate projects for each target region
- _One account per wave_ - Each migration wave can target only one account. Applications requiring different target accounts must be placed in separate waves
- _AWS Organizations required_ - All target accounts must be part of an AWS Organization

## Prerequisites

Before you begin a multi-account migration, ensure you have the following:

- An AWS Organization containing all target accounts for your
  migration
- A designated Management Account with [Delegated administrator](../../../organizations/latest/userguide/orgs_delegate_policies.md "../../../organizations/latest/userguide/orgs_delegate_policies.md") or an account with _Manager_
  permissions in the AWS Organization.
- Appropriate permissions initialized across all target accounts. Set up these roles using the link to the Application Migration Service console, provided to you by AWS Transform when it requests that you set up these permissions.
  1.  If you're using Delegated administrator permissions, you can select delegated administrators.
  2.  You can **View Roles** to learn about the permissions.
  3.  Select **Initialize Multi Account Network Migration**. Return to AWS Transform and report that you successfully initialized multi account network migration.

## Implementation overview

Multi-account migration follows this high-level process:

1. After you've kicked off migration and connected your discovery account tell AWS Transform that you want to start network migration.
2. AWS Transform asks if you want to deploy to **Single Account** or **Multi Account**
3. Create or select a target connector. Learn more in [Connect target
   account](transform-vmware-connect-target-account.md "transform-vmware-connect-target-account.md"). The target account must be an account in your Organizations with Delegated administrator or Manager permissions.
4. Provide your source network file.
5. _Review network translation_ - AWS Transform displays
   the target network configuration, including which resources deploy to which
   accounts. After your VPC networks are generated you can modify CIDR ranges
   and select targets across multiple accounts in the table provided in the
   human-in-the-loop (HITL) pane.
6. Generate Infrastructure as code (IaC) files - The IaC files (CDK, CFT, Terraform and
   LZA-compatible yaml) that AWS Transform generates include any changes you make to
   the target accounts and CIDR ranges.
7. _Deploy network infrastructure_ - Choose to deploy the network yourself or have AWS Transform deploy it across your target accounts.
8. _Execute server migration_ - AWS Transform migrates
   servers to their assigned target accounts (using Application Migration Service global view).

###### Note

The inventory file that you provide to AWS Transform should include the target account configuration.
The workloads, and the subnets they use, should go to the same target
account.
