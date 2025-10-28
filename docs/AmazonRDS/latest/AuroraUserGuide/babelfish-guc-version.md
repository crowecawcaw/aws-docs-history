# Using Babelfish product version

parameter

A new Grand Unified Configuration (GUC) parameter called
`babelfishpg_tds.product_version` is introduced from Babelfish
2.4.0 and 3.1.0 versions. This parameter allows you to set the SQL Server product
version number as the output of Babelfish.

The parameter is a 4-part version ID string, and each part should be separated by “.”.

Syntax

```
*Major.Minor.Build.Revision*
```

- Major Version: A number between 11 and 16.
- Minor Version: A number between 0 and 255.
- Build Version: A number between 0 and 65535.
- Revision: 0 and any positive number.

## Configuring Babelfish product

version parameter

You must use the cluster parameter group to set the
babelfishpg_tds.product_version parameter in the console. For more information on
how to modify the DB cluster parameter, see [Modifying parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

When you set the product version parameter to an invalid value, the change will
not take effect. Although the console might show you the new value, the parameter
retains the previous value. Check the engine log file for details about the error
messages.

For Linux, macOS, or Unix:

```

aws rds modify-db-cluster-parameter-group \
--db-cluster-parameter-group-name mydbparametergroup \
--parameters "ParameterName=babelfishpg_tds.product_version,ParameterValue=15.2.4000.1,ApplyMethod=immediate"
```

For Windows:

```

aws rds modify-db-cluster-parameter-group ^
--db-cluster-parameter-group-name mydbparametergroup ^
--parameters "ParameterName=babelfishpg_tds.product_version,ParameterValue=15.2.4000.1,ApplyMethod=immediate"

```

## Affected queries and

parameter

| Query/Parameter                              | Result                                                                               | Effective time                                 |
| -------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SELECT @@VERSION                             | Returns user defined SQL Server version (babelfishpg_tsql.version value = Default)   | Immediately                                    |
| SELECT SERVERPROPERTY('ProductVersion')      | Returns user defined SQL Server version                                              | Immediately                                    |
| SELECT SERVERPROPERTY('ProductMajorVersion') | Returns Major Version of the user defined SQL Server version                         | Immediately                                    |
| VERSION tokens in PRELOGIN Response Message  | Server returns PRELOGIN messages with user defined SQL Server version                | Takes effect when a user creates a new session |
| SQLServerVersion in LoginAck when using JDBC | DatabaseMetaData.getDatabaseProductVersion() returns user defined SQL Server version | Takes effect when a user creates a new session | ## Interface with babelfishpg_tsql.version parameter You can set the output of the @@VERSION using the parameters babelfishpg_tsql.version and babelfishpg_tds.product_version. The following examples show how these two parameters interface. <br>• When babelfishpg_tsql.version parameter is "default" and babelfishpg_tds.product_version is 15.0.2000.8. + Output of @@version – 15.0.2000.8. <br>• When babelfishpg_tsql.version parameter is set to 13.0.2000.8 and babelfishpg_tds.product_version parameter is 15.0.2000.8. + Output of @@version – 13.0.2000.8. |
