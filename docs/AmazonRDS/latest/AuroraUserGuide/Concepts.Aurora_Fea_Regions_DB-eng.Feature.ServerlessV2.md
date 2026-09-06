

# Supported Regions and Aurora DB engines for Aurora serverless
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2"></a>

Aurora serverless is an on-demand, auto-scaling feature designed to be a cost-effective approach to running intermittent or unpredictable workloads on Amazon Aurora. It automatically scales capacity up or down as needed by your applications. With Aurora serverless, each cluster can contain a writer DB instance and multiple reader DB instances. You can combine Aurora serverless and traditional provisioned DB instances within the same cluster. For more information, see [Using Aurora serverless](aurora-serverless-v2.md).

**Topics**
+ [Aurora serverless with Aurora MySQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy)
+ [Aurora serverless with Aurora PostgreSQL](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg)

## Aurora serverless with Aurora MySQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy"></a>

The following Regions and engine versions are available for Aurora serverless with Aurora MySQL.


| Region | Aurora MySQL version 3 | Aurora MySQL version 8.4 | 
| --- | --- | --- | 
| US East (N. Virginia) | Version 3.02.0 and higher | All available versions | 
| US East (Ohio) | Version 3.02.0 and higher | All available versions | 
| US West (N. California) | Version 3.02.0 and higher | All available versions | 
| US West (Oregon) | Version 3.02.0 and higher | All available versions | 
| Africa (Cape Town) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Hong Kong) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Hyderabad) | Version 3.02.3 and higher | All available versions | 
| Asia Pacific (Jakarta) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Malaysia) | Versions 3.04.3, 3.05.2, 3.06.1, 3.07.1, and higher | Versions 3.04.3, 3.05.2, 3.06.1, 3.07.1, and higher | 
| Asia Pacific (Melbourne) | Version 3.02.3 and higher | All available versions | 
| Asia Pacific (Mumbai) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (New Zealand) | Versions 3.04.3 and higher, 3.08.0 and higher | Versions 3.04.3 and higher, 3.08.0 and higher | 
| Asia Pacific (Osaka) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Seoul) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Singapore) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Sydney) | Version 3.02.0 and higher | All available versions | 
| Asia Pacific (Taipei) | Versions 3.04.3 and higher, 3.08.1 and higher | Versions 3.04.3 and higher, 3.08.1 and higher | 
| Asia Pacific (Thailand) | Versions 3.04.3 and higher, 3.08.0 and higher | Versions 3.04.3 and higher, 3.08.0 and higher | 
| Asia Pacific (Tokyo) | Version 3.02.0 and higher | All available versions | 
| Canada (Central) | Version 3.02.0 and higher | All available versions | 
| Canada West (Calgary) | Version 3.04.0 and higher | All available versions | 
| China (Beijing) | Version 3.02.2 and higher | All available versions | 
| China (Ningxia) | Version 3.02.2 and higher | All available versions | 
| Europe (Frankfurt) | Version 3.02.0 and higher | All available versions | 
| Europe (Ireland) | Version 3.02.0 and higher | All available versions | 
| Europe (London) | Version 3.02.0 and higher | All available versions | 
| Europe (Milan) | Version 3.02.0 and higher | All available versions | 
| Europe (Paris) | Version 3.02.0 and higher | All available versions | 
| Europe (Spain) | Version 3.02.3 and higher | All available versions | 
| Europe (Stockholm) | Version 3.02.0 and higher | All available versions | 
| Europe (Zurich) | Version 3.02.3 and higher | All available versions | 
| Israel (Tel Aviv) | Versions 3.02.3 and higher, 3.03.1 and higher | Versions 3.02.3 and higher, 3.03.1 and higher | 
| Mexico (Central) | Versions 3.04.3 and higher, 3.08.0 and higher | Versions 3.04.3 and higher, 3.08.0 and higher | 
| Middle East (Bahrain) | Version 3.02.0 and higher | All available versions | 
| Middle East (UAE) | Version 3.02.3 and higher | All available versions | 
| South America (São Paulo) | Version 3.02.0 and higher | All available versions | 
| AWS GovCloud (US-East) | Version 3.02.2 and higher | All available versions | 
| AWS GovCloud (US-West) | Version 3.02.2 and higher | All available versions | 

 The upper and lower ACU limits for Aurora serverless capacity might vary depending on your engine version. For details, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity). 

## Aurora serverless with Aurora PostgreSQL
<a name="Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg"></a>

The following Regions and engine versions are available for Aurora serverless with Aurora PostgreSQL.


| Region | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 | 
| --- | --- | --- | --- | --- | --- | 
| <a name="asv2-apg-us-east-1"></a>US East (N. Virginia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-us-east-2"></a>US East (Ohio) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-us-west-1"></a>US West (N. California) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-us-west-2"></a>US West (Oregon) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-af-south-1"></a>Africa (Cape Town) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ap-east-1"></a>Asia Pacific (Hong Kong) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ap-south-2"></a>Asia Pacific (Hyderabad) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| <a name="asv2-apg-ap-southeast-3"></a>Asia Pacific (Jakarta) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| Asia Pacific (Malaysia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.4 and higher | Version 14.6, 14.9 and higher | Version 13.9, 13.12 and higher | 
| <a name="asv2-apg-ap-southeast-4"></a>Asia Pacific (Melbourne) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| <a name="asv2-apg-ap-south-1"></a>Asia Pacific (Mumbai) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| Asia Pacific (New Zealand) | Version 17.4 and higher | Version 16.8 and higher | Version 15.12 and higher | Version 14.17 and higher | Version 13.20 and higher | 
| <a name="asv2-apg-ap-northeast-3"></a>Asia Pacific (Osaka) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ap-northeast-2"></a>Asia Pacific (Seoul) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ap-southeast-1"></a>Asia Pacific (Singapore) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| Asia Pacific (Taipei) | Version 17.4 and higher | Version 16.6 and higher | Version 15.10 and higher | Version 14.15 and higher | Not available | 
| <a name="asv2-apg-ap-southeast-2"></a>Asia Pacific (Sydney) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ap-southeast-7"></a>Asia Pacific (Thailand) | Version 17.4 and higher | Version 16.4 and higher | Version 15.8 and higher | Version 14.13 and higher | Not available | 
| <a name="asv2-apg-ap-northeast-1"></a>Asia Pacific (Tokyo) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ca-central-1"></a>Canada (Central) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-ca-west-1"></a>Canada West (Calgary) | Version 17.4 and higher | Version 16.1 and higher | Version 15.3 and higher | Version 14.6, 14.8 and higher | Version 13.9, 13.11 and higher | 
| <a name="asv2-apg-cn-north-1"></a>China (Beijing) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-cn-northwest-1"></a>China (Ningxia) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-central-1"></a>Europe (Frankfurt) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-west-1"></a>Europe (Ireland) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-west-2"></a>Europe (London) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-south-1"></a>Europe (Milan) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-west-3"></a>Europe (Paris) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-south-2"></a>Europe (Spain) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| <a name="asv2-apg-eu-north-1"></a>Europe (Stockholm) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-eu-central-2"></a>Europe (Zurich) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| <a name="asv2-apg-il-central-1"></a>Israel (Tel Aviv) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| Mexico (Central) | Version 17.4 and higher | Version 16.4 and higher | Version 15.8 and higher | Version 14.13 and higher | Not available | 
| <a name="asv2-apg-me-south-1"></a>Middle East (Bahrain) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-me-central-1"></a>Middle East (UAE) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.6 and higher | Version 13.9 and higher | 
| <a name="asv2-apg-sa-east-1"></a>South America (São Paulo) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-gov-us-east-1"></a>AWS GovCloud (US-East) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 
| <a name="asv2-apg-gov-us-west-1"></a>AWS GovCloud (US-West) | Version 17.4 and higher | Version 16.1 and higher | Version 15.2 and higher | Version 14.3 and higher | Version 13.6 and higher | 

 The upper and lower ACU limits for Aurora serverless capacity might vary depending on your engine version. For details, see [Aurora serverless capacity](aurora-serverless-v2.how-it-works.md#aurora-serverless-v2.how-it-works.capacity). 