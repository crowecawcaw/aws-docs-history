# Aurora Serverless v1

###### Important

AWS has announced the end-of-life date for Aurora Serverless v1: March 31st, 2025. We strongly recommend upgrading any Aurora Serverless v1 DB clusters to
Aurora Serverless v2 before that date. The upgrade can involve a change in the major
version number of the database engine. Thus, it's important to plan, test, and
implement this switchover before the end-of-life date. Starting January 8th, 2025,
customers will no longer be able to create new Aurora Serverless v1 clusters or
instances with either the AWS Management Console or the CLI. For information about the migration
process, see [Upgrading from an Aurora Serverless v1 cluster to Aurora Serverless v2](aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure "aurora-serverless-v2.md#aurora-serverless-v2.upgrade-from-serverless-v1-procedure").

Aurora Serverless v2 scales more quickly and in a more granular way.
Aurora Serverless v2 also has more compatibility with other Aurora features such as
reader DB instances. You can learn about Aurora Serverless v2 in [Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

Aurora Serverless v1 is an on-demand, auto-scaling feature designed to be a
cost-effective approach to running intermittent or unpredictable workloads on Amazon Aurora.
It automatically starts up, shuts down, and scales capacity up or down, as needed by
your applications, using a single DB instance in each cluster. For more information, see
[Using Amazon Aurora Serverless v1](aurora-serverless.md "aurora-serverless.md").

###### Topics

- [Aurora Serverless v1 with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy")
- [Aurora Serverless v1 with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg")

## Aurora Serverless v1 with Aurora MySQL

The following Regions and engine versions are available for Aurora Serverless v1
with Aurora MySQL.

| Region                    | Aurora MySQL version 3 | Aurora MySQL version 2 |
| ------------------------- | ---------------------- | ---------------------- |
| US East (N. Virginia)     | Not available          | Version 2.11.4         |
| US East (Ohio)            | Not available          | Version 2.11.4         |
| US West (N. California)   | Not available          | Version 2.11.4         |
| US West (Oregon)          | Not available          | Version 2.11.4         |
| Africa (Cape Town)        | Not available          | Not available          |
| Asia Pacific (Hong Kong)  | Not available          | Not available          |
| Asia Pacific (Hyderabad)  | Not available          | Not available          |
| Asia Pacific (Jakarta)    | Not available          | Not available          |
| Asia Pacific (Malaysia)   | Not available          | Not available          |
| Asia Pacific (Melbourne)  | Not available          | Not available          |
| Asia Pacific (Mumbai)     | Not available          | Version 2.11.4         |
| Asia Pacific (Osaka)      | Not available          | Not available          |
| Asia Pacific (Seoul)      | Not available          | Version 2.11.4         |
| Asia Pacific (Singapore)  | Not available          | Version 2.11.4         |
| Asia Pacific (Sydney)     | Not available          | Version 2.11.4         |
| Asia Pacific (Thailand)   | Not available          | Not available          |
| Asia Pacific (Tokyo)      | Not available          | Version 2.11.4         |
| Canada (Central)          | Not available          | Version 2.11.4         |
| Canada West (Calgary)     | Not available          | Not available          |
| China (Beijing)           | Not available          | Not available          |
| China (Ningxia)           | Not available          | Version 2.11.4         |
| Europe (Frankfurt)        | Not available          | Version 2.11.4         |
| Europe (Ireland)          | Not available          | Version 2.11.4         |
| Europe (London)           | Not available          | Version 2.11.4         |
| Europe (Milan)            | Not available          | Not available          |
| Europe (Paris)            | Not available          | Version 2.11.4         |
| Europe (Spain)            | Not available          | Not available          |
| Europe (Stockholm)        | Not available          | Not available          |
| Europe (Zurich)           | Not available          | Not available          |
| Israel (Tel Aviv)         | Not available          | Not available          |
| Middle East (Bahrain)     | Not available          | Not available          |
| Middle East (UAE)         | Not available          | Not available          |
| South America (São Paulo) | Not available          | Not available          |
| AWS GovCloud (US-East)    | Not available          | Not available          |
| AWS GovCloud (US-West)    | Not available          | Not available          |

## Aurora Serverless v1 with Aurora PostgreSQL

The following Regions and engine versions are available for Aurora Serverless v1
with Aurora PostgreSQL.

| Region                    | Aurora PostgreSQL 13 |
| ------------------------- | -------------------- |
| US East (N. Virginia)     | Version 13.12        |
| US East (Ohio)            | Version 13.12        |
| US West (N. California)   | Version 13.12        |
| US West (Oregon)          | Version 13.12        |
| Africa (Cape Town)        | Not available        |
| Asia Pacific (Hong Kong)  | Not available        |
| Asia Pacific (Hyderabad)  | Not available        |
| Asia Pacific (Jakarta)    | Not available        |
| Asia Pacific (Malaysia)   | Not available        |
| Asia Pacific (Melbourne)  | Not available        |
| Asia Pacific (Mumbai)     | Version 13.12        |
| Asia Pacific (Osaka)      | Not available        |
| Asia Pacific (Seoul)      | Version 13.12        |
| Asia Pacific (Singapore)  | Version 13.12        |
| Asia Pacific (Sydney)     | Version 13.12        |
| Asia Pacific (Thailand)   | Not available        |
| Asia Pacific (Tokyo)      | Version 13.12        |
| Canada (Central)          | Version 13.12        |
| Canada West (Calgary)     | Not available        |
| China (Beijing)           | Not available        |
| China (Ningxia)           | Not available        |
| Europe (Frankfurt)        | Version 13.12        |
| Europe (Ireland)          | Version 13.12        |
| Europe (London)           | Version 13.12        |
| Europe (Milan)            | Not available        |
| Europe (Paris)            | Version 13.12        |
| Europe (Spain)            | Not available        |
| Europe (Stockholm)        | Not available        |
| Europe (Zurich)           | Not available        |
| Israel (Tel Aviv)         | Not available        |
| Middle East (Bahrain)     | Not available        |
| Middle East (UAE)         | Not available        |
| South America (São Paulo) | Not available        |
| AWS GovCloud (US-East)    | Not available        |
| AWS GovCloud (US-West)    | Not available        |
