# Understanding the

RDS for PostgreSQL incremental release process

RDS for PostgreSQL delivers security fixes, performance improvements, and new features
through incremental releases while maintaining minor version compatibility. These
releases are labeled as R1, R2, R3, and so on.

###### Release version naming convention

- R1 is the initial release of a minor version. It occasionally includes new
  features, extensions, or upgrades to existing extensions.
- Subsequent release versions (R2, R3, and later) include:
  - Security updates
  - Performance improvements
  - Bug fixes
  - Extension updates

## Advantages of

RDS for PostgreSQL incremental release process

The incremental release process provides the following advantages:

- Quick adoption of new PostgreSQL community releases while separately
  managing RDS-specific enhancements through subsequent releases. This
  streamlines the release process and ensures faster delivery of critical
  updates.
- Access to bug fixes, new features, security updates, and extension updates
  while maintaining compatibility with the PostgreSQL minor version.

## Managing release

updates

Amazon RDS notifies you about new incremental releases through pending maintenance
actions in the AWS Management Console. You can update your database using one of these
methods:

- Enable automatic updates during scheduled maintenance windows.
- Apply updates manually through pending maintenance actions.
- Use Blue/Green deployments with physical replication to minimize downtime.
  For more information, see [Blue/Green Deployments support minor version upgrade for
  RDS for PostgreSQL](https://aws.amazon.com/about-aws/whats-new/2024/11/rds-blue-green-deployments-upgrade-rds-postgresql/ "https://aws.amazon.com/about-aws/whats-new/2024/11/rds-blue-green-deployments-upgrade-rds-postgresql/").

Before updating your database, consider the following key points:

- Database reboots are required for updates unless you use Blue/Green
  deployments with physical replication.
- Some incremental releases are mandatory, particularly those that include
  security fixes.

For more information about updating your Amazon RDS DB instance instance, see [PostgreSQL trusted
extensions](PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.Extensions.Trusted "PostgreSQL.Concepts.General.FeatureSupport.md#PostgreSQL.Concepts.General.Extensions.Trusted") and [apply-pending-maintenance-action](../../../cli/latest/reference/rds/apply-pending-maintenance-action.md "../../../cli/latest/reference/rds/apply-pending-maintenance-action.md").
