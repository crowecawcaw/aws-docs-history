# Supported

Regions and Aurora DB engines for Aurora Serverless v2

Aurora Serverless v2 is an on-demand, auto-scaling feature designed to be a
cost-effective approach to running intermittent or unpredictable workloads on Amazon Aurora.
It automatically scales capacity up or down as needed by your applications. The scaling
is faster and more granular than with Aurora Serverless v1. With Aurora Serverless v2, each
cluster can contain a writer DB instance and multiple reader DB instances. You can
combine Aurora Serverless v2 and traditional provisioned DB instances within the same
cluster. For more information, see [Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

###### Topics

- [Aurora Serverless v2 with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy")
- [Aurora Serverless v2 with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg")

## Aurora Serverless v2 with Aurora MySQL

The following Regions and engine versions are available for Aurora Serverless v2
with Aurora MySQL.

| Region                     | Aurora MySQL version 3                              |
| -------------------------- | --------------------------------------------------- |
| US East (N. Virginia)      | Version 3.02.0 and higher                           |
| US East (Ohio)             | Version 3.02.0 and higher                           |
| US West (N. California)    | Version 3.02.0 and higher                           |
| US West (Oregon)           | Version 3.02.0 and higher                           |
| Africa (Cape Town)         | Version 3.02.0 and higher                           |
| Asia Pacific (Hong Kong)   | Version 3.02.0 and higher                           |
| Asia Pacific (Hyderabad)   | Version 3.02.3 and higher                           |
| Asia Pacific (Jakarta)     | Version 3.02.0 and higher                           |
| Asia Pacific (Malaysia)    | Versions 3.04.3, 3.05.2, 3.06.1, 3.07.1, and higher |
| Asia Pacific (Melbourne)   | Version 3.02.3 and higher                           |
| Asia Pacific (Mumbai)      | Version 3.02.0 and higher                           |
| Asia Pacific (New Zealand) | Not available                                       |
| Asia Pacific (Osaka)       | Version 3.02.0 and higher                           |
| Asia Pacific (Seoul)       | Version 3.02.0 and higher                           |
| Asia Pacific (Singapore)   | Version 3.02.0 and higher                           |
| Asia Pacific (Sydney)      | Version 3.02.0 and higher                           |
| Asia Pacific (Taipei)      | Not available                                       |
| Asia Pacific (Thailand)    | Versions 3.04.3 and higher, 3.08.0 and higher       |
| Asia Pacific (Tokyo)       | Version 3.02.0 and higher                           |
| Canada (Central)           | Version 3.02.0 and higher                           |
| Canada West (Calgary)      | Version 3.04.0 and higher                           |
| China (Beijing)            | Version 3.02.2 and higher                           |
| China (Ningxia)            | Version 3.02.2 and higher                           |
| Europe (Frankfurt)         | Version 3.02.0 and higher                           |
| Europe (Ireland)           | Version 3.02.0 and higher                           |
| Europe (London)            | Version 3.02.0 and higher                           |
| Europe (Milan)             | Version 3.02.0 and higher                           |
| Europe (Paris)             | Version 3.02.0 and higher                           |
| Europe (Spain)             | Version 3.02.3 and higher                           |
| Europe (Stockholm)         | Version 3.02.0 and higher                           |
| Europe (Zurich)            | Version 3.02.3 and higher                           |
| Israel (Tel Aviv)          | Versions 3.02.3 and higher, 3.03.1 and higher       |
| Mexico (Central)           | Not available                                       |
| Middle East (Bahrain)      | Version 3.02.0 and higher                           |
| Middle East (UAE)          | Version 3.02.3 and higher                           |
| South America (São Paulo)  | Version 3.02.0 and higher                           |
| AWS GovCloud (US-East)     | Version 3.02.2 and higher                           |
| AWS GovCloud (US-West)     | Version 3.02.2 and higher                           |

The upper and lower ACU limits for Aurora Serverless v2 capacity might vary
depending on your engine version. For details, see [Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity").

## Aurora Serverless v2 with Aurora PostgreSQL

The following Regions and engine versions are available for Aurora Serverless v2
with Aurora PostgreSQL.

| Region                     | Aurora PostgreSQL 17    | Aurora PostgreSQL 16    | Aurora PostgreSQL 15    | Aurora PostgreSQL 14          | Aurora PostgreSQL 13           |
| -------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------------- | ------------------------------ |
| US East (N. Virginia)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| US East (Ohio)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| US West (N. California)    | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| US West (Oregon)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Africa (Cape Town)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Hong Kong)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Hyderabad)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| Asia Pacific (Jakarta)     | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Malaysia)    | Version 17.4 and higher | Version 16.1 and higher | Version 15.4 and higher | Version 14.6, 14.9 and higher | Version 13.9, 13.12 and higher |
| Asia Pacific (Melbourne)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| Asia Pacific (Mumbai)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (New Zealand) | Not available           | Not available           | Not available           | Not available                 | Not available                  |
| Asia Pacific (Osaka)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Seoul)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Singapore)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Taipei)      | Not available           | Not available           | Not available           | Not available                 | Not available                  |
| Asia Pacific (Sydney)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Asia Pacific (Thailand)    | Version 17.4 and higher | Version 16.4 and higher | Version 15.8 and higher | Version 14.13 and higher      | Not available                  |
| Asia Pacific (Tokyo)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Canada (Central)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Canada West (Calgary)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.6, 14.8 and higher | Version 13.9, 13.11 and higher |
| China (Beijing)            | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| China (Ningxia)            | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Frankfurt)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Ireland)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (London)            | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Milan)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Paris)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Spain)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| Europe (Stockholm)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Europe (Zurich)            | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| Israel (Tel Aviv)          | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| Mexico (Central)           | Not available           | Not available           | Not available           | Not available                 | Not available                  |
| Middle East (Bahrain)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| Middle East (UAE)          | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher       | Version 13.9 and higher        |
| South America (São Paulo)  | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| AWS GovCloud (US-East)     | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |
| AWS GovCloud (US-West)     | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher       | Version 13.6 and higher        |

The upper and lower ACU limits for Aurora Serverless v2 capacity might vary
depending on your engine version. For details, see [Aurora Serverless v2 capacity](aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity "aurora-serverless-v2.md#aurora-serverless-v2.how-it-works.capacity").
