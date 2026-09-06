

# Database engine updates for Amazon Aurora PostgreSQL
<a name="AuroraPostgreSQL.Updates"></a><a name="pgsql_relnotes"></a>

Following, you can find information about Amazon Aurora PostgreSQL engine version releases and updates. You can also find information about how to upgrade your Aurora PostgreSQL engine. For more information about Aurora releases in general, see [Amazon Aurora versions](Aurora.VersionPolicy.md).

**Tip**  
You can minimize the downtime required for a DB cluster upgrade by using a blue/green deployment. For more information, see [Using Amazon Aurora Blue/Green Deployments for database updates](blue-green-deployments.md).

**Topics**
+ [Identifying versions of Amazon Aurora PostgreSQL](#AuroraPostgreSQL.Updates.Versions)
+ [Amazon Aurora PostgreSQL releases and engine versions](AuroraPostgreSQL.Updates.20180305.md)
+ [Extension versions for Amazon Aurora PostgreSQL](AuroraPostgreSQL.Extensions.md)
+ [Upgrading Amazon Aurora PostgreSQL DB clusters](USER_UpgradeDBInstance.PostgreSQL.md)
+ [Using an Aurora PostgreSQL long-term support (LTS) release](AuroraPostgreSQL.Updates.LTS.md)

## Identifying versions of Amazon Aurora PostgreSQL
<a name="AuroraPostgreSQL.Updates.Versions"></a>

Amazon Aurora includes certain features that are general to Aurora and available to all Aurora DB clusters. Aurora includes other features that are specific to a particular database engine that Aurora supports. These features are available only to those Aurora DB clusters that use that database engine, such as Aurora PostgreSQL.

An Aurora database release typically has two version numbers, the database engine version number and the Aurora version number. If an Aurora PostgreSQL release has an Aurora version number, it's included after the engine version number in the [Amazon Aurora PostgreSQL releases and engine versions](AuroraPostgreSQL.Updates.20180305.md) listing. 

**Topics**
+ [Aurora version number](#AuroraPostgreSQL.Updates.Versions.AuroraNumber)
+ [PostgreSQL engine version numbers](#AuroraPostgreSQL.Updates.Versions.EngineNumber)

### Aurora version number
<a name="AuroraPostgreSQL.Updates.Versions.AuroraNumber"></a>

Aurora version numbers use the {{major}}.{{minor}}.{{patch}} naming scheme. An Aurora patch version includes important bug fixes added to a minor version after its release. To learn more about Amazon Aurora major, minor, and patch releases, see [Amazon Aurora major versions](Aurora.VersionPolicy.Versioning.md#Aurora.VersionPolicy.MajorVersions), [Amazon Aurora minor versions](Aurora.VersionPolicy.Versioning.md#Aurora.VersionPolicy.MinorVersions), and [Amazon Aurora patch versions](Aurora.VersionPolicy.Versioning.md#Aurora.VersionPolicy.PatchVersions). 

You can find out the Aurora version number of your Aurora PostgreSQL DB instance with the following SQL query:

```
postgres=> SELECT aurora_version();
```

Starting with the release of PostgreSQL versions 13.3, 12.8, 11.13, 10.18, and for all other later versions, Aurora version numbers align more closely to the PostgreSQL engine version. For example, querying an Aurora PostgreSQL 13.3 DB cluster returns the following:

```
aurora_version
----------------
 13.3.1
(1 row)
```

Prior releases, such as Aurora PostgreSQL 10.14 DB cluster, return version numbers similar to the following:

```
aurora_version
----------------
 2.7.3
(1 row)
```

### PostgreSQL engine version numbers
<a name="AuroraPostgreSQL.Updates.Versions.EngineNumber"></a>

Starting with PostgreSQL 10, PostgreSQL database engine versions use a {{major}}.{{minor}} numbering scheme for all releases. Some examples include PostgreSQL 10.18, PostgreSQL 12.7, and PostgreSQL 13.3. 

Releases prior to PostgreSQL 10 used a {{major}}.{{major}}.{{minor}} numbering scheme in which the first two digits make up the major version number and a third digit denotes a minor version. For example, PostgreSQL 9.6 was a major version, with minor versions 9.6.21 or 9.6.22 indicated by the third digit.

**Note**  
The PostgreSQL engine version 9.6 is no longer supported. To upgrade, see [Upgrading Amazon Aurora PostgreSQL DB clusters](USER_UpgradeDBInstance.PostgreSQL.md). For version policies and release timelines, see [How long Amazon Aurora major versions remain available](Aurora.VersionPolicy.Versioning.md#Aurora.VersionPolicy.MajorVersionLifetime).

You can find out the PostgreSQL database engine version number with the following SQL query:

```
postgres=> SELECT version();
```

For an Aurora PostgreSQL 13.3 DB cluster, the results are as follows:

```
version
-------------------------------------------------------------------------------------------------
 PostgreSQL 13.3 on x86_64-pc-linux-gnu, compiled by x86_64-pc-linux-gnu-gcc (GCC) 7.4.0, 64-bit
(1 row)
```