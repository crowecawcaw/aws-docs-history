# Upgrade rollout policies

AWS Organizations upgrade rollout policies allow you to centrally manage and stagger automatic
upgrades across multiple AWS resources and accounts in your organization. With these
policies, you can define the order in which resources receive upgrades, ensuring changes are
validated in less critical environments before reaching production.

In today's complex cloud environments, managing upgrades across numerous resources and
accounts can be challenging. Upgrade rollout policies address this challenge by providing a
systematic approach to implementing upgrades. By using these policies, you can align your
upgrade process with your organization's change management practices, reducing risk and
improving operational efficiency.

Upgrade rollout policies leverage the hierarchical structure of AWS Organizations to apply policies
across your entire organization or specific organizational units (OUs). This integration
allows you to manage upgrades at scale, eliminating the need for manual coordination or
custom automation scripts.

## Key features and

benefits

Upgrade rollout policies provide comprehensive capabilities for managing upgrades
while offering significant advantages for organizations managing resources across
multiple accounts and environments. The following table outlines the key features and
their associated benefits:

| Features and benefits of upgrade rollout policies | Feature                                                             | Description                                    | Key Benefits |
| ------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------- | ------------ |
| Upgrade ordering system                           | Three-tier system (First, Second, Last) with<br>configurable timing | • Test upgrades in pre-production environments |
| • Minimize risk to production workloads           |
| Policy-based management                           | Centralized control through AWS Organizations                       | • Manage multiple accounts from a single point |
| • Reduce administrative overhead                  |
| Resource targeting                                | Tag-based and OU-based targeting options                            | • Target specific resource groups              |
| • Apply policies at scale                         |
| Automated scheduling                              | Works with existing maintenance windows                             | • Eliminate manual coordination                |
| • Maintain consistent upgrade patterns            |
| Service integration                               | Works with AWS service upgrade mechanisms                           | • Monitor events with Amazon EventBridge       |
| Compliance controls                               | Policy inheritance and enforcement                                  | • Enforce organizational standards             |
| • Meet compliance requirements                    |

For more information about policy inheritance, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md").

## What are upgrade rollout

policies?

Upgrade rollout policies are a set of rules that determine how and when automatic
upgrades are applied to your AWS resources. These policies allow you to designate
different upgrade orders for your resources, typically aligning with your development,
testing, and production environments. By doing so, you can ensure that upgrades are
first applied to less critical systems, allowing you to identify and address any issues
before they affect your production workloads.

The policies support three upgrade orders: First, Second, and Last. These orders
create a staged approach to upgrades, with resources designated as "First" receiving
upgrades initially, followed by "Second" after a waiting period, and finally "Last"
after another waiting period. This staggered approach gives you time to validate
upgrades at each stage before they progress to more critical systems.

Upgrade rollout policies are particularly valuable for organizations with complex,
multi-account structures or those with strict change management requirements. They
provide a balance between maintaining up-to-date systems and minimizing the risk of
upgrade-related disruptions to critical services.

## How upgrade rollout

policies work

Upgrade rollout policies integrate seamlessly with your existing AWS infrastructure
and processes. When you create and attach an upgrade rollout policy to an organizational
unit, it applies to all accounts within that OU. You can then use resource tags or patch
orders to specify which resources should be upgraded in which order.

When a supported AWS service releases an upgrade, it consults the upgrade rollout
policies to determine the order in which resources should receive the upgrade. The
service first applies the upgrade to resources marked as "First" during their configured
maintenance windows. After a service-specific waiting period, typically around one week,
resources marked as "Second" become eligible for the upgrade. Finally, after another
waiting period, resources marked as "Last" receive the upgrade.

This process ensures that upgrades are applied in a controlled, predictable manner
across your organization. It allows you to monitor the impact of upgrades at each stage
and take corrective action if needed before the changes reach your most critical
environments. The automated nature of this process reduces the operational overhead of
managing upgrades, while still providing you with the control and visibility you need to
maintain the stability and security of your AWS resources.

## Terminology

Here are the key terms you should understand when working with upgrade rollout
policies:

| Upgrade rollout policy terms      | Term                                                                                                                                                                   | Definition |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Active Date                       | The date when the AmVU becomes visible in the Describe Pending<br>Maintenance Actions API and available for application.                                               |
| AmVU (Auto minor version upgrade) | The automatic upgrade process for minor versions of database<br>engines.                                                                                               |
| Effective policy                  | The final set of rules that apply to an account or resource after<br>considering all inherited and directly attached policies.                                         |
| Maintenance window                | A recurring time period during which automatic upgrades can be<br>applied to a resource. Upgrade rollout policies work within these<br>configured maintenance windows. |
| Organizational unit (OU)          | A container for AWS accounts in your organization. Upgrade rollout<br>policies can be attached at the OU level to affect all accounts within<br>it.                    |
| Patch order                       | The sequence in which resources receive upgrades (First, Second,<br>Last).                                                                                             |
| Policy target                     | The scope to which an upgrade rollout policy applies, which can be an<br>entire organization, specific OUs, or individual accounts.                                    |
| Resource tags                     | Key-value pairs that can be used to identify which resources should<br>follow specific upgrade orders within a policy.                                                 |
| Scheduling window                 | The time frame during which resources of a specific patch order<br>receive upgrades.                                                                                   |
| Service-specific waiting period   | The designated time interval between upgrading resources of different<br>upgrade orders. This period varies by AWS service and upgrade<br>type.                        |
| Upgrade order                     | A designation that determines when a resource receives upgrades<br>relative to other resources. Can be set to First, Second, or<br>Last.                               |
| Upgrade rollout policy            | The AWS Organizations policy type used to manage upgrade schedules<br>across resources.                                                                                |

## Use cases for upgrade

rollout policies

Organizations of different sizes and industries can benefit from upgrade rollout
policies. The following fictitious scenarios demonstrate common upgrade management
challenges and how upgrade rollout policies provide efficient solutions. These examples
are based on typical customer experiences but have been simplified to highlight key
benefits and implementation patterns.

Many organizations face similar challenges: they need to keep their resources
up-to-date with the latest versions while minimizing risk to their production
environments. Without a centralized policy-based approach, teams often resort to manual
processes or complex automation scripts. The following examples demonstrate how two
different organizations might solve similar challenges using upgrade rollout
policies:

### Example

use case: Global Financial Services Company

A financial services company operates hundreds of Aurora PostgreSQL databases
across multiple AWS accounts. Before upgrade rollout policies, their DevOps team
spent several days each month manually coordinating database upgrades, ensuring
changes were tested in development environments before reaching production systems.
By implementing upgrade rollout policies, they:

- Tagged development databases with upgrade order "First"
- Assigned QA databases to upgrade order "Second"
- Designated production databases as upgrade order "Last"
- Reduced upgrade coordination from days to minutes
- Automatically validated changes in lower environments first
- Maintained compliance with their change management requirements

### Example use

case: IoT Device Platform Provider

An IoT company processes millions of device events daily using multiple Amazon RDS
databases. They needed to ensure automatic minor version upgrades wouldn't disrupt
their production services. Using upgrade rollout policies, they:

- Created a policy that applies across their organizational structure
- Configured canary environments to receive upgrades first
- Set up monitoring in early-upgrade environments
- Gained time to detect and respond to any issues before production
  upgrades
- Replaced complex custom upgrade automation with a simple policy
- Maintained high availability for their production workloads while staying
  current with database versions

## Supported AWS services

Upgrade rollout policies integrate with the following AWS services while supporting
automatic minor version upgrades:

| Supported services for upgrade rollout policies   | Service name                                                                                                                                                                                                                                                  | Purpose |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Amazon Aurora PostgreSQL-Compatible Edition       | [Automatic minor version upgrades](../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU")                                 |
| Amazon Aurora MySQL-Compatible Edition            | [Automatic minor version upgrades](../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU "../../../AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.md#Aurora.Maintenance.AMVU")                                 |
| Amazon Relational Database Service for PostgreSQL | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.md")                                                                       |
| Amazon Relational Database Service for SQL Server | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.md")                                                                                             |
| Amazon Relational Database Service for Oracle     | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.md#oracle-minor-version-upgrade-tuning-on "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.md#oracle-minor-version-upgrade-tuning-on") |
| Amazon Relational Database Service for MariaDB    | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.md")                                                                             |
| Amazon Relational Database Service for MySQL      | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md "../../../AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.md")                                                                                 |
| Amazon Relational Database Service for Db2        | [Automatic minor version upgrades](../../../AmazonRDS/latest/UserGuide/Db2.Concepts.md "../../../AmazonRDS/latest/UserGuide/Db2.Concepts.md")                                                                                                                 |

## Prerequisites

The following are prerequisites and required permissions necessary for managing
upgrade rollout policies in AWS Organizations:

- AWS Organizations management account or delegated administrator access
- Resources in supported services (currently Amazon Aurora and Amazon Relational Database Service database
  engines)
- Proper IAM permissions to manage upgrade rollout policies

## Next steps

To begin using upgrade rollout policies:

1. Review the [Getting started with upgrade
   rollout policies](orgs_manage_policies_upgrade_getting_started.md "orgs_manage_policies_upgrade_getting_started.md") to learn how
   to create and manage policies
2. Explore [Best practices for using
   upgrade rollout policies](orgs_manage_policies_upgrade_best_practices.md "orgs_manage_policies_upgrade_best_practices.md") for
   implementing upgrade rollout policies
3. Understand [Upgrade rollout policy syntax and
   examples](orgs_manage_policies_upgrade_syntax.md "orgs_manage_policies_upgrade_syntax.md")
