# Major version upgrades for RDS for SQL Server

Amazon RDS currently supports the following major version upgrades to a Microsoft SQL Server DB instance.

You can upgrade your existing DB instance to SQL Server 2017 or 2019 from any version except SQL Server 2008. To upgrade from SQL
Server 2008, first upgrade to one of the other versions.

| Current version | Supported upgrade versions                            |
| --------------- | ----------------------------------------------------- |
| SQL Server 2019 | SQL Server 2022                                       |
| SQL Server 2017 | SQL Server 2022<br>SQL Server 2019                    |
| SQL Server 2016 | SQL Server 2022<br>SQL Server 2019<br>SQL Server 2017 |

You can use an AWS CLI query, such as the following example, to find the available upgrades for a particular database engine
version.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --engine sqlserver-se \
    --engine-version 14.00.3281.6.v1 \
    --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" \
    --output table
```

For Windows:

```
aws rds describe-db-engine-versions ^
    --engine sqlserver-se ^
    --engine-version 14.00.3281.6.v1 ^
    --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" ^
    --output table
```

The output shows that you can upgrade version 14.00.3281.6 to the latest available SQL Server 2017 or 2019 versions.

```
--------------------------
|DescribeDBEngineVersions|
+------------------------+
|      EngineVersion     |
+------------------------+
|  14.00.3294.2.v1       |
|  14.00.3356.20.v1      |
|  14.00.3381.3.v1       |
|  14.00.3401.7.v1       |
|  14.00.3421.10.v1      |
|  14.00.3451.2.v1       |
|  15.00.4043.16.v1      |
|  15.00.4073.23.v1      |
|  15.00.4153.1.v1       |
|  15.00.4198.2.v1       |
|  15.00.4236.7.v1       |
+------------------------+
```

## Database compatibility level

You can use Microsoft SQL Server database compatibility levels to adjust some
database behaviors to mimic previous versions of SQL Server. For more information,
see [Compatibility level](https://msdn.microsoft.com/en-us/library/bb510680.aspx "https://msdn.microsoft.com/en-us/library/bb510680.aspx") in the Microsoft documentation. When you upgrade
your DB instance, all existing databases remain at their original compatibility
level.

You can change the compatibility level of a database by using the ALTER DATABASE
command. For example, to change a database named `customeracct` to be
compatible with SQL Server 2016, issue the following command:

```
ALTER DATABASE customeracct SET COMPATIBILITY_LEVEL = 130

```
