# Checking Aurora MySQL version numbers

Although Aurora MySQL-Compatible Edition is compatible with the MySQL database engines, Aurora MySQL includes features and bug
fixes that are specific to particular Aurora MySQL versions. Application developers can check the Aurora MySQL
version in their applications by using SQL. Database administrators can check and specify Aurora MySQL versions
when creating or upgrading Aurora MySQL DB clusters and DB instances.

###### Topics

- [Checking or specifying Aurora MySQL engine versions through AWS](#AuroraMySQL.Updates.EngineVersions "#AuroraMySQL.Updates.EngineVersions")
- [Checking Aurora MySQL versions using SQL](#AuroraMySQL.Updates.DBVersions "#AuroraMySQL.Updates.DBVersions")

## Checking or specifying Aurora MySQL engine versions through AWS

When you perform administrative tasks using the AWS Management Console, AWS CLI, or RDS API, you specify the Aurora MySQL
version in a descriptive alphanumeric format.

Starting with Aurora MySQL version 2, Aurora engine versions have the following syntax.

```
`mysql-major-version`.mysql_aurora.`aurora-mysql-version`
```

The `mysql-major-version-` portion is `5.7` or `8.0`. This value
represents the version of the client protocol and general level of MySQL feature support for the corresponding Aurora MySQL
version.

The `aurora-mysql-version` is a dotted value with three parts: the Aurora MySQL major
version, the Aurora MySQL minor version, and the patch level. The major version is `2` or `3`. Those values
represent Aurora MySQL compatible with MySQL 5.7 or 8.0, respectively. The minor version represents the feature release within the
2.x or 3.x series. The patch level begins at `0` for each minor version, and represents the set of subsequent bug
fixes that apply to the minor version. Occasionally, a new feature is incorporated into a minor version but not made visible
immediately. In these cases, the feature undergoes fine-tuning and is made public in a later patch level.

All 2.x Aurora MySQL engine versions are wire-compatible with Community MySQL 5.7.12 or higher. All 3.x Aurora MySQL engine versions are wire-compatible
with MySQL 8.0.23 or higher. You can refer to release notes of the specific 3.x version to find the corresponding MySQL compatible version.

For example, the engine versions for Aurora MySQL 3.04.0 and 2.11.2 are the following.

```
8.0.mysql_aurora.3.04.0
5.7.mysql_aurora.2.11.2
```

###### Note

There isn't a one-to-one correspondence between community MySQL versions and the Aurora MySQL 2.x versions. For Aurora MySQL
version 3, there is a more direct mapping. To check which bug fixes and new features are in a particular Aurora MySQL release,
see [Database
engine updates for Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") and [Database engine updates for
Amazon Aurora MySQL version 2](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_. For a chronological list of new features
and releases, see [Document history](WhatsNew.md "WhatsNew.md"). To check the minimum version required for a
security-related fix, see [Security vulnerabilities fixed in
Aurora MySQL](../AuroraMySQLReleaseNotes/AuroraMySQL.md "../AuroraMySQLReleaseNotes/AuroraMySQL.md")in the _Release Notes for Aurora MySQL_.

You specify the Aurora MySQL engine version in some AWS CLI commands and RDS API operations. For example, you specify the
`--engine-version` option when you run the AWS CLI commands [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") and [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md"). You specify
the `EngineVersion` parameter when you run the RDS API operations [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") and [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md").

In Aurora MySQL version 2 and higher, the engine version in the AWS Management Console also includes the Aurora version. Upgrading the cluster
changes the displayed value. This change helps you to specify and check the precise Aurora MySQL versions, without the need to
connect to the cluster or run any SQL commands.

###### Tip

For Aurora clusters managed through AWS CloudFormation, this change in the `EngineVersion` setting can trigger actions by AWS CloudFormation.
For information about how AWS CloudFormation treats changes to the `EngineVersion` setting, see [the AWS CloudFormation documentation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md").

## Checking Aurora MySQL versions using SQL

The Aurora version numbers that you can retrieve in your application using SQL queries use the format
``<major version>`.`<minor
 version>`.`<patch version>``. You can get this version
number for any DB instance in your Aurora MySQL cluster by querying the `AURORA_VERSION` system
variable. To get this version number, use one of the following queries.

```
select aurora_version();
select @@aurora_version;

```

Those queries produce output similar to the following.

```
`mysql>` select aurora_version(), @@aurora_version;
`+------------------+------------------+
| aurora_version() | @@aurora_version |
+------------------+------------------+
| 3.05.2 | 3.05.2 |
+------------------+------------------+`

```

The version numbers that the console, CLI, and RDS API return by using the techniques described in [Checking or specifying Aurora MySQL engine versions through AWS](#AuroraMySQL.Updates.EngineVersions "#AuroraMySQL.Updates.EngineVersions") are typically more
descriptive.
