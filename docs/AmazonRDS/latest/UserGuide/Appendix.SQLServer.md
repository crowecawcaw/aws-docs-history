# Options for the Microsoft SQL Server database engine

In this section, you can find descriptions for options that are
available for Amazon RDS instances running the Microsoft SQL Server DB engine. To enable these
options, you add them to an option group, and then associate the option group with your DB
instance. For more information, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

If you're looking for optional features that aren't added through RDS option groups (such as SSL, Microsoft Windows Authentication, and Amazon S3 integration),
see [Additional features for Microsoft SQL Server on Amazon RDS](User.SQLServer.md "User.SQLServer.md").

Amazon RDS supports the following options for Microsoft SQL Server DB instances.

| Option                                                                                                         | Option ID                                                                  | Engine editions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Linked Servers with Oracle OLEDB](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")              | `OLEDB_ORACLE`                                                             | SQL Server Enterprise Edition<br>SQL Server Standard Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Native backup and restore](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                     | `SQLSERVER_BACKUP_RESTORE`                                                 | SQL Server Enterprise Edition<br>SQL Server Standard Edition<br>SQL Server Web Edition<br>SQL Server Express Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Transparent Data Encryption](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                   | `TRANSPARENT_DATA_ENCRYPTION` (RDS console)<br>`TDE` (AWS CLI and RDS API) | SQL Server 2016–2022 Enterprise Edition<br>SQL Server 2022 Standard Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [SQL Server Audit](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                              | `SQLSERVER_AUDIT`                                                          | In RDS, starting with SQL Server 2016, all editions of SQL Server support server-level<br>audits, and Enterprise Edition also supports database-level<br>audits.<br>Starting with SQL Server SQL Server 2016 (13.x) SP1, all editions support both server-level and database-level audits.<br>For more information, see [SQL Server Audit (database engine)](https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-2017 "https://docs.microsoft.com/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-2017") in the SQL Server documentation. |
| [SQL Server Analysis Services](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                  | `SSAS`                                                                     | SQL Server Enterprise Edition<br>SQL Server Standard Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [SQL Server Integration Services](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")               | `SSIS`                                                                     | SQL Server Enterprise Edition<br>SQL Server Standard Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [SQL Server Reporting Services](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                 | `SSRS`                                                                     | SQL Server Enterprise Edition<br>SQL Server Standard Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Microsoft Distributed Transaction Coordinator](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md") | `MSDTC`                                                                    | In RDS, starting with SQL Server 2016, all editions of SQL Server support distributed<br>transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [SQL Server resource governor](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md")                  | `RESOURCE_GOVERNOR`                                                        | SQL Server Enterprise Edition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## Listing the available options for SQL Server versions and editions

You can use the `describe-option-group-options` AWS CLI command to list the available options for SQL Server versions
and editions, and the settings for those options.

The following example shows the options and option settings for SQL Server 2019 Enterprise Edition. The
`--engine-name` option is required.

```
aws rds describe-option-group-options --engine-name sqlserver-ee --major-engine-version 15.00
```

The output resembles the following:

```
{
    "OptionGroupOptions": [
        {
            "Name": "MSDTC",
            "Description": "Microsoft Distributed Transaction Coordinator",
            "EngineName": "sqlserver-ee",
            "MajorEngineVersion": "15.00",
            "MinimumRequiredMinorEngineVersion": "4043.16.v1",
            "PortRequired": true,
            "DefaultPort": 5000,
            "OptionsDependedOn": [],
            "OptionsConflictsWith": [],
            "Persistent": false,
            "Permanent": false,
            "RequiresAutoMinorEngineVersionUpgrade": false,
            "VpcOnly": false,
            "OptionGroupOptionSettings": [
                {
                    "SettingName": "ENABLE_SNA_LU",
                    "SettingDescription": "Enable support for SNA LU protocol",
                    "DefaultValue": "true",
                    "ApplyType": "DYNAMIC",
                    "AllowedValues": "true,false",
                    "IsModifiable": true,
                    "IsRequired": false,
                    "MinimumEngineVersionPerAllowedValue": []
                },
        ...

        {
            "Name": "TDE",
            "Description": "SQL Server - Transparent Data Encryption",
            "EngineName": "sqlserver-ee",
            "MajorEngineVersion": "15.00",
            "MinimumRequiredMinorEngineVersion": "4043.16.v1",
            "PortRequired": false,
            "OptionsDependedOn": [],
            "OptionsConflictsWith": [],
            "Persistent": true,
            "Permanent": false,
            "RequiresAutoMinorEngineVersionUpgrade": false,
            "VpcOnly": false,
            "OptionGroupOptionSettings": []
        }
    ]
}
```
