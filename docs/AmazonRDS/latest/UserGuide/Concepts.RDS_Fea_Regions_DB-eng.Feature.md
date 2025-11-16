# Supported

Regions and DB engines for Kerberos authentication in Amazon RDS

By using Kerberos authentication in Amazon RDS, you can support external authentication of
database users using Kerberos and Microsoft Active Directory. Using Kerberos and Active
Directory provides the benefits of single sign-on and centralized authentication of database
users.

Kerberos authentication isn't available with the following engines:

- RDS for MariaDB
  Although most AWS Regions are active by default for your AWS account, certain Regions
  are activated only when you manually select them. These Regions are referred to as
  _opt-in Regions_. In contrast, Regions that are active by default, as soon
  as your AWS account is created, are referred to as _commercial
  Regions_, or simply, _Regions_. For opt-in Regions,
  you must use a regionalized service principal of the form
  `directoryservice.rds.`region_name`.amazonaws.com`. For
  example, for Africa (Cape Town), you must add service principal
  `directoryservice.rds.af-south-1.amazonaws.com` to your trust policy. For
  more information, see [Kerberos authentication](database-authentication.md#kerberos-authentication "database-authentication.md#kerberos-authentication").

###### Topics

- [Kerberos
  authentication with RDS for Db2](#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.db2 "#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.db2")
- [Kerberos
  authentication with RDS for MySQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.my "#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.my")
- [Kerberos
  authentication with RDS for Oracle](#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.ora "#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.ora")
- [Kerberos
  authentication with RDS for PostgreSQL](#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.pg "#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.pg")
- [Kerberos
  authentication with RDS for SQL Server](#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.sq "#Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.sq")

## Kerberos

authentication with RDS for Db2

The following Regions and engine versions are available for Kerberos authentication with
RDS for Db2.

| Region                     | RDS for Db2 11.5 |
| -------------------------- | ---------------- |
| US East (N. Virginia)      | All versions     |
| US East (Ohio)             | All versions     |
| US West (N. California)    | All versions     |
| US West (Oregon)           | All versions     |
| Africa (Cape Town)         | All versions     |
| Asia Pacific (Hong Kong)   | Not available    |
| Asia Pacific (Hyderabad)   | All versions     |
| Asia Pacific (Jakarta)     | All versions     |
| Asia Pacific (Malaysia)    | Not available    |
| Asia Pacific (Melbourne)   | All versions     |
| Asia Pacific (Mumbai)      | All versions     |
| Asia Pacific (New Zealand) | Not available    |
| Asia Pacific (Osaka)       | Not available    |
| Asia Pacific (Seoul)       | All versions     |
| Asia Pacific (Singapore)   | All versions     |
| Asia Pacific (Sydney)      | All versions     |
| Asia Pacific (Taipei)      | Not available    |
| Asia Pacific (Thailand)    | Not available    |
| Asia Pacific (Tokyo)       | All versions     |
| Canada (Central)           | All versions     |
| Canada West (Calgary)      | Not available    |
| China (Beijing)            | Not available    |
| China (Ningxia)            | Not available    |
| Europe (Frankfurt)         | All versions     |
| Europe (Ireland)           | All versions     |
| Europe (London)            | All versions     |
| Europe (Milan)             | All versions     |
| Europe (Paris)             | Not available    |
| Europe (Spain)             | All versions     |
| Europe (Stockholm)         | All versions     |
| Europe (Zurich)            | All versions     |
| Israel (Tel Aviv)          | All versions     |
| Mexico (Central)           | Not available    |
| Middle East (Bahrain)      | All versions     |
| Middle East (UAE)          | All versions     |
| South America (São Paulo)  | All versions     |
| AWS GovCloud (US-East)     | Not available    |
| AWS GovCloud (US-West)     | Not available    |

## Kerberos

authentication with RDS for MySQL

The following Regions and engine versions are available for Kerberos authentication with
RDS for MySQL.

| Region                     | RDS for MySQL 8.4 | RDS for MySQL 8.0 | RDS for MySQL 5.7 (under RDS Extended Support) |
| -------------------------- | ----------------- | ----------------- | ---------------------------------------------- |
| US East (N. Virginia)      | All versions      | All versions      | All versions                                   |
| US East (Ohio)             | All versions      | All versions      | All versions                                   |
| US West (N. California)    | All versions      | All versions      | All versions                                   |
| US West (Oregon)           | All versions      | All versions      | All versions                                   |
| Africa (Cape Town)         | All versions      | All versions      | All versions                                   |
| Asia Pacific (Hong Kong)   | All versions      | All versions      | All versions                                   |
| Asia Pacific (Hyderabad)   | All versions      | All versions      | All versions                                   |
| Asia Pacific (Jakarta)     | All versions      | All versions      | All versions                                   |
| Asia Pacific (Malaysia)    | Not available     | Not available     | Not available                                  |
| Asia Pacific (Melbourne)   | All versions      | All versions      | All versions                                   |
| Asia Pacific (Mumbai)      | All versions      | All versions      | All versions                                   |
| Asia Pacific (New Zealand) | Not available     | Not available     | Not available                                  |
| Asia Pacific (Osaka)       | All versions      | All versions      | All versions                                   |
| Asia Pacific (Seoul)       | All versions      | All versions      | All versions                                   |
| Asia Pacific (Singapore)   | All versions      | All versions      | All versions                                   |
| Asia Pacific (Sydney)      | All versions      | All versions      | All versions                                   |
| Asia Pacific (Taipei)      | Not available     | Not available     | Not available                                  |
| Asia Pacific (Thailand)    | Not available     | Not available     | Not available                                  |
| Asia Pacific (Tokyo)       | All versions      | All versions      | All versions                                   |
| Canada (Central)           | All versions      | All versions      | All versions                                   |
| Canada West (Calgary)      | Not available     | Not available     | Not available                                  |
| China (Beijing)            | All versions      | All versions      | All versions                                   |
| China (Ningxia)            | All versions      | All versions      | All versions                                   |
| Europe (Frankfurt)         | All versions      | All versions      | All versions                                   |
| Europe (Ireland)           | All versions      | All versions      | All versions                                   |
| Europe (London)            | All versions      | All versions      | All versions                                   |
| Europe (Milan)             | All versions      | All versions      | All versions                                   |
| Europe (Paris)             | All versions      | All versions      | All versions                                   |
| Europe (Spain)             | All versions      | All versions      | All versions                                   |
| Europe (Stockholm)         | All versions      | All versions      | All versions                                   |
| Europe (Zurich)            | All versions      | All versions      | All versions                                   |
| Israel (Tel Aviv)          | All versions      | All versions      | All versions                                   |
| Mexico (Central)           | Not available     | Not available     | Not available                                  |
| Middle East (Bahrain)      | All versions      | All versions      | All versions                                   |
| Middle East (UAE)          | All versions      | All versions      | All versions                                   |
| South America (São Paulo)  | All versions      | All versions      | All versions                                   |
| AWS GovCloud (US-East)     | All versions      | All versions      | All versions                                   |
| AWS GovCloud (US-West)     | All versions      | All versions      | All versions                                   |

## Kerberos

authentication with RDS for Oracle

The following Regions and engine versions are available for Kerberos authentication with
RDS for Oracle.

| Region                                   | RDS for Oracle 21c | RDS for Oracle 19c |
| ---------------------------------------- | ------------------ | ------------------ |
| US East (N. Virginia)                    | All versions       | All versions       |
| US East (Ohio)                           | All versions       | All versions       |
| US West (N. California)                  | All versions       | All versions       |
| US West (Oregon)                         | All versions       | All versions       |
| Africa (Cape Town) (opt-in Region)       | All versions       | All versions       |
| Asia Pacific (Hong Kong) (opt-in Region) | All versions       | All versions       |
| Asia Pacific (Hyderabad) (opt-in Region) | All versions       | All versions       |
| Asia Pacific (Jakarta) (opt-in Region)   | All versions       | All versions       |
| Asia Pacific (Malaysia)                  | Not available      | Not available      |
| Asia Pacific (Melbourne) (opt-in Region) | All versions       | All versions       |
| Asia Pacific (Mumbai)                    | All versions       | All versions       |
| Asia Pacific (New Zealand)               | Not available      | Not available      |
| Asia Pacific (Osaka)                     | Not available      | Not available      |
| Asia Pacific (Seoul)                     | All versions       | All versions       |
| Asia Pacific (Singapore)                 | All versions       | All versions       |
| Asia Pacific (Sydney)                    | All versions       | All versions       |
| Asia Pacific (Taipei)                    | Not available      | Not available      |
| Asia Pacific (Thailand)                  | Not available      | Not available      |
| Asia Pacific (Tokyo)                     | All versions       | All versions       |
| Canada (Central)                         | All versions       | All versions       |
| Canada West (Calgary)                    | Not available      | Not available      |
| China (Beijing)                          | Not available      | Not available      |
| China (Ningxia)                          | Not available      | Not available      |
| Europe (Frankfurt)                       | All versions       | All versions       |
| Europe (Ireland)                         | All versions       | All versions       |
| Europe (London)                          | All versions       | All versions       |
| Europe (Milan) (opt-in Region)           | All versions       | All versions       |
| Europe (Paris)                           | Not available      | Not available      |
| Europe (Spain) (opt-in Region)           | All versions       | All versions       |
| Europe (Stockholm)                       | All versions       | All versions       |
| Europe (Zurich) (opt-in Region)          | All versions       | All versions       |
| Israel (Tel Aviv) (opt-in Region)        | All versions       | All versions       |
| Mexico (Central)                         | Not available      | Not available      |
| Middle East (Bahrain) (opt-in Region)    | All versions       | All versions       |
| Middle East (UAE) (opt-in Region)        | All versions       | All versions       |
| South America (São Paulo)                | All versions       | All versions       |
| AWS GovCloud (US-East)                   | All versions       | All versions       |
| AWS GovCloud (US-West)                   | All versions       | All versions       |

## Kerberos

authentication with RDS for PostgreSQL

The following Regions and engine versions are available for Kerberos authentication with
RDS for PostgreSQL.

| Region                     | RDS for PostgreSQL 17 | RDS for PostgreSQL 16 | RDS for PostgreSQL 15 | RDS for PostgreSQL 14 | RDS for PostgreSQL 13 | RDS for PostgreSQL 12 | RDS for PostgreSQL 11 | RDS for PostgreSQL 10 |
| -------------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- | --------------------- |
| US East (N. Virginia)      | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| US East (Ohio)             | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| US West (N. California)    | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| US West (Oregon)           | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Africa (Cape Town)         | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Hong Kong)   | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Hyderabad)   | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Jakarta)     | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Malaysia)    | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Asia Pacific (Melbourne)   | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Mumbai)      | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (New Zealand) | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Asia Pacific (Osaka)       | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Asia Pacific (Seoul)       | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Singapore)   | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Sydney)      | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Asia Pacific (Taipei)      | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Asia Pacific (Thailand)    | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Asia Pacific (Tokyo)       | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Canada (Central)           | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Canada West (Calgary)      | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| China (Beijing)            | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| China (Ningxia)            | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Frankfurt)         | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Ireland)           | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (London)            | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Milan)             | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Paris)             | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Spain)             | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Stockholm)         | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Europe (Zurich)            | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Israel (Tel Aviv)          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Mexico (Central)           | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         | Not available         |
| Middle East (Bahrain)      | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| Middle East (UAE)          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| South America (São Paulo)  | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| AWS GovCloud (US-East)     | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |
| AWS GovCloud (US-West)     | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          | All versions          |

## Kerberos

authentication with RDS for SQL Server

The following Regions and engine versions are available for Kerberos authentication with
RDS for SQL Server.

| Region                     | RDS for SQL Server 2022 | RDS for SQL Server 2019 | RDS for SQL Server 2017 | RDS for SQL Server 2016 |
| -------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| US East (N. Virginia)      | All versions            | All versions            | All versions            | All versions            |
| US East (Ohio)             | All versions            | All versions            | All versions            | All versions            |
| US West (N. California)    | All versions            | All versions            | All versions            | All versions            |
| US West (Oregon)           | All versions            | All versions            | All versions            | All versions            |
| Africa (Cape Town)         | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Hong Kong)   | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Hyderabad)   | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Malaysia)    | Not available           | Not available           | Not available           | Not available           |
| Asia Pacific (Melbourne)   | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Mumbai)      | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (New Zealand) | Not available           | Not available           | Not available           | Not available           |
| Asia Pacific (Osaka)       | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Seoul)       | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Singapore)   | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Sydney)      | All versions            | All versions            | All versions            | All versions            |
| Asia Pacific (Taipei)      | Not available           | Not available           | Not available           | Not available           |
| Asia Pacific (Thailand)    | Not available           | Not available           | Not available           | Not available           |
| Asia Pacific (Tokyo)       | All versions            | All versions            | All versions            | All versions            |
| Canada (Central)           | All versions            | All versions            | All versions            | All versions            |
| Canada West (Calgary)      | Not available           | Not available           | Not available           | Not available           |
| China (Beijing)            | All versions            | All versions            | All versions            | All versions            |
| China (Ningxia)            | All versions            | All versions            | All versions            | All versions            |
| Europe (Frankfurt)         | All versions            | All versions            | All versions            | All versions            |
| Europe (Ireland)           | All versions            | All versions            | All versions            | All versions            |
| Europe (London)            | All versions            | All versions            | All versions            | All versions            |
| Europe (Milan)             | All versions            | All versions            | All versions            | All versions            |
| Europe (Paris)             | All versions            | All versions            | All versions            | All versions            |
| Europe (Spain)             | All versions            | All versions            | All versions            | All versions            |
| Europe (Stockholm)         | All versions            | All versions            | All versions            | All versions            |
| Europe (Zurich)            | All versions            | All versions            | All versions            | All versions            |
| Israel (Tel Aviv)          | Not available           | Not available           | Not available           | Not available           |
| Mexico (Central)           | Not available           | Not available           | Not available           | Not available           |
| Middle East (Bahrain)      | All versions            | All versions            | All versions            | All versions            |
| Middle East (UAE)          | All versions            | All versions            | All versions            | All versions            |
| South America (São Paulo)  | All versions            | All versions            | All versions            | All versions            |
| AWS GovCloud (US-East)     | All versions            | All versions            | All versions            | All versions            |
| AWS GovCloud (US-West)     | All versions            | All versions            | All versions            | All versions            |
