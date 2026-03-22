# Aurora MySQL database engine updates 2021-11-18 (version 3.01.0) (Deprecated)

**Version:** 3.01.0

Aurora MySQL 3.01.0 is generally available. Aurora MySQL 3.01 versions are compatible with MySQL 8.0.23, Aurora MySQL
2.x versions are compatible with MySQL 5.7, and Aurora MySQL 1.x versions are compatible with MySQL 5.6.

For details of new features in Aurora MySQL version 3 and differences between Aurora MySQL version 3 and Aurora MySQL
version 2 or community MySQL 8.0, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.Compare-v2-v3 "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.Compare-v2-v3") in the _Amazon Aurora User Guide_.

Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*.

You can restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.01.0.

For information on planning an upgrade to Aurora MySQL version 3, see
[Upgrade planning for Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-planning "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-planning") in the _Amazon Aurora User Guide_.
For the upgrade procedure itself, see
[Upgrading to Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-procedure "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-procedure") in the _Amazon Aurora User Guide_.
For general information about Aurora MySQL upgrades, see [Upgrading Amazon Aurora MySQL DB clusters](../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md "../AuroraUserGuide/AuroraMySQL.Updates.Upgrading.md") in the _Amazon Aurora User Guide_.

For troubleshooting information, see [Troubleshooting upgrade issues with Aurora MySQL version 3](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-troubleshooting "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.mysql80-upgrade-troubleshooting").

If you have any questions or concerns, AWS Support is available on the community forums and through
[AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support"). For more information, see
[Maintaining an Amazon Aurora DB cluster](../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md "../AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.md") in the _Amazon Aurora User Guide_.

## Improvements

Aurora MySQL version 3.01.0 is generally compatible with community MySQL 8.0.23. This version includes the security fixes for Common
Vulnerabilities and Exposures (CVE) issues as of community MySQL 8.0.23.

Aurora MySQL version 3.01.0 contains all the Aurora-specific bug fixes through Aurora MySQL version 2.10.0.

For details of new features in Aurora MySQL version 3, see [Features from community
MySQL 8.0](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.8.0-features-community "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.8.0-features-community") and [New parallel query
optimizations](../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.8.0-features-pq "../AuroraUserGuide/AuroraMySQL.MySQL80.md#AuroraMySQL.8.0-features-pq") in the _Amazon Aurora User Guide_.

**Availability improvements:**

- Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running
  queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast
  insert optimization, see [Amazon Aurora MySQL performance enhancements](../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance "../AuroraUserGuide/Aurora.AuroraMySQL.Overview.md#Aurora.AuroraMySQL.Performance").
