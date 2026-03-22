# Supported Regions and Aurora DB engines for RDS Data API

RDS Data API (Data API) provides a web-services interface to an Amazon Aurora DB cluster.
Instead of managing database connections from client applications, you can run SQL
commands against an HTTPS endpoint. For more information, see [Using the Amazon RDS Data API](data-api.md "data-api.md").

###### Topics

- [Data API with Aurora PostgreSQL Serverless v2 and provisioned](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.apg "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.apg")
- [Data API with Aurora MySQL Serverless v2 and provisioned](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.ams "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.ams")
- [Data API with Aurora PostgreSQL Serverless v1](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.apg-sv1 "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.apg-sv1")
- [Data API with Aurora MySQL Serverless v1](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.amy "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.amy")

## Data API with Aurora PostgreSQL Serverless v2 and provisioned

The following Regions and engine versions are available for Data API with
Aurora PostgreSQL Serverless v2 and provisioned DB clusters.

| Region                     | Aurora PostgreSQL 17    | Aurora PostgreSQL 16    | Aurora PostgreSQL 15    | Aurora PostgreSQL 14    | Aurora PostgreSQL 13     |
| -------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ |
| US East (N. Virginia)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| US East (Ohio)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| US West (N. California)    | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| US West (Oregon)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Africa (Cape Town)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Hong Kong)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Hyderabad)   | Not available           | Not available           | Not available           | Not available           | Not available            |
| Asia Pacific (Jakarta)     | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Malaysia)    | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Melbourne)   | Not available           | Not available           | Not available           | Not available           | Not available            |
| Asia Pacific (Mumbai)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (New Zealand) | Not available           | Not available           | Not available           | Not available           | Not available            |
| Asia Pacific (Osaka)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Seoul)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Singapore)   | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Sydney)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Taipei)      | Not available           | Not available           | Not available           | Not available           | Not available            |
| Asia Pacific (Thailand)    | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Asia Pacific (Tokyo)       | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Canada (Central)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Canada West (Calgary)      | Not available           | Not available           | Not available           | Not available           | Not available            |
| China (Beijing)            | Not available           | Not available           | Not available           | Not available           | Not available            |
| China (Ningxia)            | Not available           | Not available           | Not available           | Not available           | Not available            |
| Europe (Frankfurt)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Ireland)           | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (London)            | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Milan)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Paris)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Spain)             | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Stockholm)         | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Europe (Zurich)            | Not available           | Not available           | Not available           | Not available           | Not available            |
| Israel (Tel Aviv)          | Not available           | Not available           | Not available           | Not available           | Not available            |
| Middle East (Bahrain)      | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| Mexico (Central)           | Not available           | Not available           | Not available           | Not available           | Not available            |
| Middle East (UAE)          | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| South America (São Paulo)  | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.8 and higher | Version 13.11 and higher |
| AWS GovCloud (US-East)     | Not available           | Not available           | Not available           | Not available           | Not available            |
| AWS GovCloud (US-West)     | Not available           | Not available           | Not available           | Not available           | Not available            |

## Data API with Aurora MySQL Serverless v2 and provisioned

The following Regions and engine versions are available for Data API with
Aurora MySQL Serverless v2 and provisioned DB clusters.

| Region                     | Aurora MySQL version 3  |
| -------------------------- | ----------------------- |
| US East (Ohio)             | Version 3.07 and higher |
| US East (N. Virginia)      | Version 3.07 and higher |
| US West (N. California)    | Version 3.07 and higher |
| US West (Oregon)           | Version 3.07 and higher |
| Africa (Cape Town)         | Version 3.07 and higher |
| Asia Pacific (Hong Kong)   | Version 3.07 and higher |
| Asia Pacific (Hyderabad)   | Not available           |
| Asia Pacific (Jakarta)     | Version 3.07 and higher |
| Asia Pacific (Malaysia)    | Version 3.07 and higher |
| Asia Pacific (Melbourne)   | Not available           |
| Asia Pacific (Mumbai)      | Version 3.07 and higher |
| Asia Pacific (New Zealand) | Not available           |
| Asia Pacific (Osaka)       | Version 3.07 and higher |
| Asia Pacific (Seoul)       | Version 3.07 and higher |
| Asia Pacific (Singapore)   | Version 3.07 and higher |
| Asia Pacific (Sydney)      | Version 3.07 and higher |
| Asia Pacific (Taipei)      | Not available           |
| Asia Pacific (Thailand)    | Version 3.07 and higher |
| Asia Pacific (Tokyo)       | Version 3.07 and higher |
| Canada (Central)           | Version 3.07 and higher |
| Canada West (Calgary)      | Not available           |
| China (Beijing)            | Not available           |
| China (Ningxia)            | Not available           |
| Europe (Frankfurt)         | Version 3.07 and higher |
| Europe (Ireland)           | Version 3.07 and higher |
| Europe (London)            | Version 3.07 and higher |
| Europe (Milan)             | Version 3.07 and higher |
| Europe (Paris)             | Version 3.07 and higher |
| Europe (Spain)             | Version 3.07 and higher |
| Europe (Stockholm)         | Version 3.07 and higher |
| Europe (Zurich)            | Not available           |
| Israel (Tel Aviv)          | Not available           |
| Mexico (Central)           | Not available           |
| Middle East (Bahrain)      | Version 3.07 and higher |
| Middle East (UAE)          | Version 3.07 and higher |
| South America (São Paulo)  | Version 3.07 and higher |
| AWS GovCloud (US-East)     | Not available           |
| AWS GovCloud (US-West)     | Not available           |

## Data API with Aurora PostgreSQL Serverless v1

The following Regions and engine versions are available for Data API with
Aurora PostgreSQL Serverless v1.

| Region                    | Aurora PostgreSQL 13 | Aurora PostgreSQL 11 |
| ------------------------- | -------------------- | -------------------- |
| US East (N. Virginia)     | Version 13.9         | Version 11.18        |
| US East (Ohio)            | Version 13.9         | Version 11.18        |
| US West (N. California)   | Version 13.9         | Version 11.18        |
| US West (Oregon)          | Version 13.9         | Version 11.18        |
| Africa (Cape Town)        | Not available        | Not available        |
| Asia Pacific (Hong Kong)  | Not available        | Not available        |
| Asia Pacific (Hyderabad)  | Not available        | Not available        |
| Asia Pacific (Jakarta)    | Not available        | Not available        |
| Asia Pacific (Malaysia)   | Not available        | Not available        |
| Asia Pacific (Melbourne)  | Not available        | Not available        |
| Asia Pacific (Mumbai)     | Version 13.9         | Version 11.18        |
| Asia Pacific (Osaka)      | Not available        | Not available        |
| Asia Pacific (Seoul)      | Version 13.9         | Version 11.18        |
| Asia Pacific (Singapore)  | Version 13.9         | Version 11.18        |
| Asia Pacific (Sydney)     | Version 13.9         | Version 11.18        |
| Asia Pacific (Thailand)   | Not available        | Not available        |
| Asia Pacific (Tokyo)      | Version 13.9         | Version 11.18        |
| Canada (Central)          | Version 13.9         | Version 11.18        |
| China (Beijing)           | Not available        | Not available        |
| China (Ningxia)           | Not available        | Not available        |
| Europe (Frankfurt)        | Version 13.9         | Version 11.18        |
| Europe (Ireland)          | Version 13.9         | Version 11.18        |
| Europe (London)           | Version 13.9         | Version 11.18        |
| Europe (Milan)            | Not available        | Not available        |
| Europe (Paris)            | Version 13.9         | Version 11.18        |
| Europe (Spain)            | Version 13.9         | Version 11.18        |
| Europe (Stockholm)        | Not available        | Not available        |
| Europe (Zurich)           | Not available        | Not available        |
| Israel (Tel Aviv)         | Not available        | Not available        |
| Middle East (Bahrain)     | Not available        | Not available        |
| Middle East (UAE)         | Not available        | Not available        |
| South America (São Paulo) | Not available        | Not available        |
| AWS GovCloud (US-East)    | Not available        | Not available        |
| AWS GovCloud (US-West)    | Not available        | Not available        |

## Data API with Aurora MySQL Serverless v1

The following Regions and engine versions are available for Data API with
Aurora MySQL Serverless v1.

| Region                    | Aurora MySQL version 2 |
| ------------------------- | ---------------------- |
| US East (N. Virginia)     | Version 2.11.3         |
| US East (Ohio)            | Version 2.11.3         |
| US West (N. California)   | Version 2.11.3         |
| US West (Oregon)          | Version 2.11.3         |
| Africa (Cape Town)        | Not available          |
| Asia Pacific (Hong Kong)  | Not available          |
| Asia Pacific (Hyderabad)  | Not available          |
| Asia Pacific (Jakarta)    | Not available          |
| Asia Pacific (Malaysia)   | Not available          |
| Asia Pacific (Melbourne)  | Not available          |
| Asia Pacific (Mumbai)     | Version 2.11.3         |
| Asia Pacific (Osaka)      | Not available          |
| Asia Pacific (Seoul)      | Version 2.11.3         |
| Asia Pacific (Singapore)  | Version 2.11.3         |
| Asia Pacific (Sydney)     | Version 2.11.3         |
| Asia Pacific (Thailand)   | Not available          |
| Asia Pacific (Tokyo)      | Version 2.11.3         |
| Canada (Central)          | Version 2.11.3         |
| Canada West (Calgary)     | Not available          |
| China (Beijing)           | Not available          |
| China (Ningxia)           | Version 2.11.3         |
| Europe (Frankfurt)        | Version 2.11.3         |
| Europe (Ireland)          | Version 2.11.3         |
| Europe (London)           | Version 2.11.3         |
| Europe (Milan)            | Not available          |
| Europe (Paris)            | Version 2.11.3         |
| Europe (Spain)            | Version 2.11.3         |
| Europe (Stockholm)        | Not available          |
| Europe (Zurich)           | Not available          |
| Israel (Tel Aviv)         | Not available          |
| Middle East (Bahrain)     | Not available          |
| Middle East (UAE)         | Not available          |
| South America (São Paulo) | Not available          |
| AWS GovCloud (US-East)    | Not available          |
| AWS GovCloud (US-West)    | Not available          |
