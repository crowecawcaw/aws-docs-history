

# Supported Regions and Aurora DB engines for Kerberos authentication
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication"></a>

By using Kerberos authentication with Aurora, you can support external authentication of database users using Kerberos and Microsoft Active Directory. Using Kerberos and Active Directory provides the benefits of single sign-on and centralized authentication of database users. Kerberos and Active Directory are available with AWS Directory Service for Microsoft Active Directory, a feature of Directory Service. For more information, see [Kerberos authentication](database-authentication.md#kerberos-authentication).

**Topics**
+ [Kerberos authentication with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication.amy)
+ [Kerberos authentication with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication.apg)
+ [Active Directory(AD) security groups with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ActiveDirectory.apg)

## Kerberos authentication with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication.amy"></a>

The following Regions and engine versions are available for Kerberos Authentication with Aurora MySQL.


| Region | Aurora MySQL version 3 | Aurora MySQL version 8.4 | 
| --- | --- | --- | 
| US East (N. Virginia) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| US East (Ohio) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| US West (N. California) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| US West (Oregon) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Africa (Cape Town) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Hong Kong) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Jakarta) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Malaysia) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Melbourne) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Mumbai) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (New Zealand) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Osaka) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Seoul) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Singapore) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Sydney) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Taipei) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Thailand) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Asia Pacific (Tokyo) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Canada (Central) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Canada West (Calgary) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| China (Beijing) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| China (Ningxia) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Frankfurt) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Ireland) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (London) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Milan) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Paris) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Spain) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Stockholm) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Europe (Zurich) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Israel (Tel Aviv) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Mexico (Central) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Middle East (Bahrain) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| Middle East (UAE) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| South America (São Paulo) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| AWS GovCloud (US-East) | Version 3.03.0 and higher | Version 8.4.7 and higher | 
| AWS GovCloud (US-West) | Version 3.03.0 and higher | Version 8.4.7 and higher | 

## Kerberos authentication with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication.apg"></a>

The following Regions and engine versions are available for Kerberos Authentication with Aurora PostgreSQL.


| Region | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | Aurora PostgreSQL 12 | Aurora PostgreSQL 11 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| US East (N. Virginia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US East (Ohio) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (N. California) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (Oregon) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Africa (Cape Town) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hong Kong) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hyderabad) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Jakarta) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Malaysia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Melbourne) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Mumbai) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (New Zealand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Osaka) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Seoul) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Singapore) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Sydney) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Taipei) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Thailand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Tokyo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada West (Calgary) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Beijing) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Ningxia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Frankfurt) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Ireland) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (London) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Milan) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Paris) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Spain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Stockholm) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Zurich) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Israel (Tel Aviv) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Mexico (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (Bahrain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (UAE) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| South America (São Paulo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-East) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-West) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 

## Active Directory(AD) security groups with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ActiveDirectory.apg"></a>

The following Regions and engine versions are available for ActiveDirectory with Aurora PostgreSQL.


| Region | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | Aurora PostgreSQL 12 | Aurora PostgreSQL 11 | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| US East (N. Virginia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US East (Ohio) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (N. California) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| US West (Oregon) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Africa (Cape Town) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hong Kong) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Hyderabad) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Jakarta) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Malaysia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Melbourne) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Mumbai) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (New Zealand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Osaka) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Seoul) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Singapore) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Sydney) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Taipei) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Thailand) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Asia Pacific (Tokyo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Canada West (Calgary) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Beijing) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| China (Ningxia) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Frankfurt) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Ireland) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (London) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Milan) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Paris) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Spain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Stockholm) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Europe (Zurich) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Israel (Tel Aviv) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Mexico (Central) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (Bahrain) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| Middle East (UAE) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| South America (São Paulo) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-East) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 
| AWS GovCloud (US-West) | All versions | All versions | All versions | All versions | All versions | All versions | All versions | 