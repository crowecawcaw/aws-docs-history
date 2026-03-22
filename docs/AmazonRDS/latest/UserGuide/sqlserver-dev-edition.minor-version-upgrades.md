# Applying database minor version upgrades

RDS for SQL Server Developer Edition requires creating a new custom engine version (CEV) with latest cumulative update to apply database minor version upgrade. Database minor version upgrades for SQL Server Developer Edition involve the following steps:

1. Before upgrading, verify current engine version on the instance, identify the target database engine version from Amazon RDS supported versions. For information about what SQL Server versions are available on Amazon RDS, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md "sqlserver-dev-edition.md").
2. Obtain and upload installation media (ISO and CU), then [create a new custom engine version](sqlserver-dev-edition.creating-cev.md "sqlserver-dev-edition.creating-cev.md").
3. Apply database minor version upgrade by using Amazon RDS [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") with the new CEV.

```
aws rds modify-db-instance \
--db-instance-identifier <instance-id> \
--engine-version <new-cev-version> \
--no-apply-immediately ## use --apply-immediately for immediate update
```

###### Note

`--no-apply-immediately` (the default) to apply the changes during the next maintenance window.
