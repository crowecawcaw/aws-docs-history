AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure access to utilities for managed

applications

When you refactor a mainframe application with AWS Blu Age, you might need to provide support for
various legacy platform utility programs, such as IDCAMS, INFUTILB, SORT, and so on, if your
application depends on them. AWS Blu Age refactoring provides this access with a dedicated web
application that is deployed alongside modernized applications. This web application requires a
configuration file, `application-utility-pgm.yml`, that you must provide. If
you don't provide this configuration file, the web application can't deploy alongside your
application and won't be available.

###### Topics

- [Configuration properties](#applications-m2-ba-utilities-props "#applications-m2-ba-utilities-props")
  This topic describes all the possible properties that you can specify in the
  `application-utility-pgm.yml` configuration file, along with their defaults.
  The topic describes both required and optional properties. The following example is a complete
  configuration file. It lists properties in the order that we recommend. You can use this example
  as a starting point for your own configuration file.

```
# If the datasource support mode is not static-xa, spring JTA transactions autoconfiguration must be disabled
 spring.jta.enabled: false
 logging.config: 'classpath:logback-utility.xml'

 # Encoding
 encoding: cp1047

 # Encoding to be used by INFUTILB and DSNUTILB to generate and read SYSPUNCH files
 sysPunchEncoding: cp1047

 # Utility database access
 spring.aws.client.datasources.primary.secret: `arn:aws:secretsmanager:us-west-2:111122223333:secret:business-FfmXLG`

 treatLargeNumberAsInteger: false

 # Zoned mode : valid values = EBCDIC_STRICT, EBCDIC_MODIFIED, AS400
 zonedMode: EBCDIC_STRICT

 jcl.type: mvs

 # Unload properties
 # For date/time: if use database configuration is enabled, formats are ignored
 # For nbi; use hexadecimal syntaxe to specify the byte value
 unload:
  sqlCodePointShift: 384
  nbi:
    whenNull: "6F"
    whenNotNull: "00"
  useDatabaseConfiguration: false
  format:
    date: MM/dd/yyyy
    time: HH.mm.ss
    timestamp: yyyy-MM-dd-HH.mm.ss.SSSSSS
  chunkSize:500
  fetchSize: 500
  varCharIsNull: false
  columnFiller: space

 # Load properties
 # Batch size for DSNUTILB Load Task
 load:
  sqlCodePointShift: 384
  batchSize: 500
  format:
    localDate: dd.MM.yyyy|dd/MM/yyyy|yyyy-MM-dd
    dbDate: yyyy-MM-dd
    localTime: 'HH:mm:ss|HH.mm.ss'
    dbTime: 'HH:mm:ss'

 table-mappings:
  TABLE_1_NAME : LEGACY_TABLE_1_NAME
  TABLE_2_NAME : LEGACY_TABLE_2_NAME
```

## Configuration properties

You can specify the following properties in your configuration file.

**spring.jta.enabled**

(Optional) Controls whether JTA support is enabled. For utilities, we recommend that you
set this value to `false`.

```
spring.jta.enabled : false
```

**logging.config**

(Required) Specifies the path to the dedicated logger configuration file. We recommend
that you use the name `logback-utility.xml` and provide this file as part
of the modernized application. The common way to organize these files is to put all logger
configuration files in the same place, usually in the subfolder
`/config/logback` where `/config` is the folder that
contains YAML configuration files. For more information, see [Chapter 3: Logback
configuration](https://logback.qos.ch/manual/configuration.html "https://logback.qos.ch/manual/configuration.html") in the Logback documentation.

```
logging.config : classpath:logback-utility.xml
```

**encoding**

(Required) Specifies the character set that the utility program uses. For most cases,
when you migrate from z/OS platforms, this character set is an EBCDIC variant, and should
match the character set that is configured for the modernized applications. Default if not set
is `ASCII`.

```
encoding : cp1047
```

**sysPunchEncoding**

(Optional) Specifies the character set that INFUTILB and DSNUTILB use to generate and
read SYSPUNCH files. If you use the SYSPUNCH files from the legacy platform as they are, this
value should be an EBCDIC variant. Default if not set is `ASCII`.

```
sysPunchEncoding : cp1047
```

### Data source configuration

Some database-related utilities, such as LOAD and UNLOAD, require access to a target
database through a data source. Like other data source definitions within AWS Mainframe Modernization, this access
requires that you use AWS Secrets Manager. The properties that point to the proper secrets in Secrets Manager are as
follows:

#### Primary data source

This is the primary business application database.

**spring.aws.client.datasources.primary.secret**

(Optional) Specifies the secret in Secrets Manager that contains the data source
properties.

```
spring.aws.client.datasources.primary.secret: `datasource-secret-ARN`
```

**spring.aws.client.datasources.primary.dbname**

(Optional) Specifies the target database name if the database name isn't provided
directly in the database secret, with the `dbname` property.

```
spring.aws.client.datasources.primary.dbname: `target-database-name`
```

**spring.aws.client.datasources.primary.type**

(Optional) Specifies the fully qualified name of the connection pool implementation to
use. The default value is `com.zaxxer.hikari.HikariDataSource`.

```
spring.aws.client.datasources.primary.type: target-datasource-type
```

If the type of the primary data source is
`com.zaxxer.hikari.HikariDataSource`, you can specify additional properties as
follows:

**spring.datasource.primary.[property\_name]**

(Optional) You can use this format to specify extra properties for configuring a
primary data source connection pool implementation.

The following is an example for a primary data source of type
`com.zaxxer.hikari.HikariDataSource`.

```
spring:
   datasource:
       primary:
         autoCommit: XXXX
         maximumPoolSize: XXXX
         keepaliveTime: XXXX
         minimumIdle: XXXX
         idleTimeout: XXXX
         connectionTimeout: XXXX
         maxLifetime: XXXX
```

#### Other utility data

sources

In addition to the primary data source, you can provide other utility data sources.

**spring.aws.client.utility.pgm.datasources.names**

(Optional) Specifies the list of utility data source names.

```
spring.aws.client.utility.pgm.datasources.names: dsname1, dsname2, dsname3
```

**spring.aws.client.utility.pgm.datasources.[dsname].secret**

(Optional) Specifies the secret ARN in SSM that hosts the data source properties.
Provide [dsname] in the list of names specified in
`spring.aws.client.utility.pgm.datasources.names`.

```
spring.aws.client.utility.pgm.datasources.dsname1.secret: datasource-secret-ARN
```

**spring.aws.client.utility.pgm.datasources.[dsname].dbname**

(Optional) Specifies the target database name if the database name isn't provided
directly in the database secret by using the `dbname` property. Provide [dsname]
in the list of names specified in
`spring.aws.client.utility.pgm.datasources.names`.

```
spring.aws.client.utility.pgm.datasources.dsname1.dbname: target-database-name
```

**spring.aws.client.utility.pgm.datasources.[dsname].type**

(Optional) Specifies the fully qualified name of the connection pool implementation to
use. The default value is `com.zaxxer.hikari.HikariDataSource`. Provide [dsname]
in the list of names specified in
`spring.aws.client.utility.pgm.datasources.names`.

```
spring.aws.client.utility.pgm.datasources.dsname1.type: target-datasource-type
```

If the utility data source type is `com.zaxxer.hikari.HikariDataSource`, you
can provide additional properties as follows:

**spring.datasource.[dsname].[property\_name]**

(Optional) Specifies a collection of extra properties to configure a utility data
source connection pool implementation. Provide [dsname] in the list of names specified in
`spring.aws.client.utility.pgm.datasources.names`. Specify the properties in the
following format: `property_name : value`

The following is an example for additional utility data sources of type
`com.zaxxer.hikari.HikariDataSource`:

```
spring:
   datasource:
       dsname1:
         connectionTimeout: XXXX
         maxLifetime: XXXX
       dsname2:
         connectionTimeout: XXXX
         maxLifetime: XXXX
       dsname3:
         connectionTimeout: XXXX
         maxLifetime: XXXX
```

**treatLargeNumberAsInteger**

(Optional) Related to Oracle database engine specifics and DSNTEP2/DSNTEP4 utilities
usage. If you set this flag to true, large numbers coming from the Oracle database (NUMBER
(38,0)) are treated as integers. Default: `false`

```
treatLargeNumberAsInteger : false
```

**zonedMode**

(Optional) Sets the zoned mode to encode or decode zoned data types. This setting
influences the way sign digits are represented. The following values are valid:

- _EBCDIC_STRICT_: Default. Use strict definition for signs
  handling. Depending on whether the character set is EBCDIC or ASCII, the sign digit
  representation uses the following characters:
  - EBCDIC characters that correspond to bytes (`Cn+Dn`) to represent
    positive and negative digit ranges (`+0` to `+9`, `-0`
    to `-9`). The characters are displayed as `{`,`A` to
    `I`, `}`, `J` to `R`
  - ASCII characters that correspond to bytes (`3n+7n`) to represent
    positive and negative digit ranges (`+0` to `+9`, `-0`
    to `-9`). The characters are displayed as `0` to `9`,
    `p` to `y`

- _EBCDIC_MODIFIED_: Use a modified definition for signs handling.
  For both EBDIC and ASCII, the same list of characters represent the sign digits, that is,
  `+0` to `+9` mapped to `{` + `A` to
  `I` and `-0` to `-9` mapped to `}` +
  `J` to `R`. \
- _AS400_: Use for modernized legacy assets that come from iSeries
  (AS400) platforms.

```
zonedMode:EBCDIC_STRICT
```

**jcl.type**

(Optional) Indicates the legacy type of modernized JCL scripts. The IDCAMS utility
uses this setting to tailor the return code if the invoking JCL is of type `vse`.
Valid values are as follows:

- `mvs` (Default)
- `vse`

```
jcl.type : mvs
```

### Database Unload utilities related

properties

Use these properties to configure utilities that unload database tables to data sets. All
of the following properties are optional.

This example shows all the possible unload properties.

```
# Unload properties
 # For date/time: if use database configuration is enabled, formats are ignored
 # For nbi; use hexadecimal syntaxe to specify the byte value
 unload:
 sqlCodePointShift: 0
 nbi:
 whenNull: "6F"
 whenNotNull: "00"
 useDatabaseConfiguration: false
 format:
 date: MM/dd/yyyy
 time: HH.mm.ss
 timestamp: yyyy-MM-dd-HH.mm.ss.SSSSSS
 chunkSize: 0
 fetchSize: 0
 varCharIsNull: false
 columnFiller: space
```

**sqlCodePointShift**

(Optional) Specifies an integer value that represents the SQL code point shift used on
data. The default is 0. This means that no code point shifting is made. Align this setting
with the SQL code point shift parameter used for modernized applications. When code point
shifting is in use, the most common value for this parameter is 384.

```
unload.sqlCodePointShift: 0
```

**nbi**

(Optional) Specifies a null indicator byte. This is a hexadecimal value (as a string)
added to the right of the data value. The two possible values are as follows:

- _whenNull_: Add the hexadecimal value when the data value is null.
  Default is `6``. Sometimes the high value `FF` is used
  instead.

```
unload.nbi.whenNull: "6F"
```

- _whenNotNull_: Add the hexadecimal value when the data value is not
  null, but the column is nullable. Default is `00` (low value).

```
unload.nbi.whenNotNull: "00"
```

**useDatabaseConfiguration**

(Optional) Specifies date and time formatting properties. This is used to deal with
date/time objects in UNLOAD queries. Default is `false`.

- If set to `true`, uses the `pgmDateFormat`,
  `pgmTimeFormat`, and `pgmTimestampFormat` properties from the main
  configuration file (`application-main.yml`).
- If set to `false`, uses the following date and time formatting
  properties:
  - `unload.format.date`: Specifies a date formatting pattern. Default is
    `MM/dd/yyyy`.
  - `unload.format.time`: Specifies a time formatting pattern. Default is
    `HH.mm.ss`.
  - `unload.format.timestamp`: Specifies a timestamp formatting pattern.
    Default is `yyyy-MM-dd-HH.mm.ss.SSSSSS`.

**chunkSize**

(Optional) Specifies the size of data chunks used to create SYSREC data sets. These
data sets are the target of the data set unload operation, with parallel operations. Default
is `0` (no chunks).

```
unload.chunkSize:0
```

**fetchSize**

(Optional) Specifies the data fetch size. The value is the number of records to fetch
at one time when a data chunks strategy is used. Default: `0`.

```
unload.fetchSize:0
```

**varCharIsNull**

(Optional) Specifies how to handle a non nullable varchar column with blank content.
Default is `false`.

If you set this value to `true`, the column content is treated as an empty
string for unload purposes, instead of a single space string. Set this flag to
`true` for the Oracle database engine case only.

```
unload.varCharIsNull: false
```

**columnFiller**

(Optional) Specifies the value to use for padding unloaded columns in varchar columns.
Possible values are space or low values. Default is space.

```
unload.columnFiller: space
```

### Database Load related

properties

Use these properties to configure utilities that load data set records into a target
database, for example, DSNUTILB. All of the following properties are optional.

This example shows all of the possible load properties.

```
# Load properties
 # Batch size for DSNUTILB Load Task
 load:
 sqlCodePointShift: 384
 batchSize: 500
 format:
 localDate: dd.MM.yyyy|dd/MM/yyyy|yyyy-MM-dd
 dbDate: yyyy-MM-dd
 localTime: HH:mm:ss|HH.mm.ss
 dbTime: HH:mm:ss

 table-mappings:
 TABLE_1_NAME : LEGACY_TABLE_1_NAME
 TABLE_2_NAME : LEGACY_TABLE_2_NAME
```

**sqlCodePointShift**

(Optional) Specifies an integer value that represents the SQL code point shift that is
used on data. Defaults to 0, which means that applications make no code point shifting. Align
this setting with the SQL code point shift parameter used for modernized applications. When
you use code point shifts, the most common value for this parameter is 384.

```
load.sqlCodePointShift : 384
```

**batchSize**

(Optional) Specifies an integer value that represents the number of records to treat
before you send an actual batch statement to the database. Defaults to 0.

```
load.batchSize: 500
```

**format**

(Optional) Specifies the date and time formatting patterns to use for date/time
conversions during the database load operations.

- `load.format.localDate`: Local date formatting pattern. This defaults to
  `dd.MM.yyyy|dd/MM/yyyy|yyyy-MM-dd`.
- `load.format.dbDate`: Database date formatting pattern. This defaults to
  `yyyy-MM-dd`.
- `load.format.localTime`: Local time formatting pattern. This defaults to
  `HH:mm:ss|HH.mm.ss`.
- `load.format.dbTime`: Database time formatting pattern. This defaults to
  `HH:mm:ss`.

**table-mappings**

(Optional) Specifies a collection of customer-provided mappings between legacy and
modern table names. The DSNUTILB utility program consumes these mappings.

Specify the values in the following format: _MODERN_TABLE_NAME :
LEGACY_TABLE_NAME_

Here is an example:

```
table-mappings:
 TABLE_1_NAME : LEGACY_TABLE_1_NAME
 TABLE_2_NAME : LEGACY_TABLE_2_NAME
 ...
 TABLE_*N*_NAME : LEGACY_TABLE_*N*_NAME
```

###### Note

When the utility application starts, it explicitly logs all provided mappings.
