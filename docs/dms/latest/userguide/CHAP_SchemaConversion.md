# Converting database schemas using DMS Schema Conversion

DMS Schema Conversion is a feature of AWS Database Migration Service (AWS DMS) that converts your source database schemas to a
format compatible with your target database on Aurora, Amazon RDS, or Amazon Redshift.

To convert a database, you create a migration project for your source and target
databases. If you don't have a target database yet, you can use a virtual target and add a
real one before you apply your code. DMS Schema Conversion reads your source metadata, and you
can run an assessment to see what converts automatically and what needs manual work. You
then convert the schema, review the results, and either apply the converted code to your
target database or export it as SQL scripts.

###### Note

DMS Schema Conversion converts your database schema, not your data. To migrate your data, use the
data migration features of AWS DMS.

You can use DMS Schema Conversion in the AWS Management Console, with the AWS CLI and SDKs, or with
an AI agent that drives it through the AWS API. For more information about using an AI
agent, see [Using AI agents with DMS Schema Conversion](sc-genai-agents.md "sc-genai-agents.md").

Use the following topics to learn how to use DMS Schema Conversion.

###### Topics

- [How DMS Schema Conversion works](#how-schema-conversion-works "#how-schema-conversion-works")
- [Key capabilities](#schema-conversion-features "#schema-conversion-features")
- [Supported conversion paths](#schema-conversion-supported-paths "#schema-conversion-supported-paths")
- [Supported AWS Regions](#schema-conversion-supported-regions "#schema-conversion-supported-regions")
- [Getting started with DMS Schema Conversion](getting-started.md "getting-started.md")
- [DMS Schema Conversion concepts](sc-concepts.md "sc-concepts.md")
- [Setting up a network for DMS Schema Conversion](instance-profiles-network.md "instance-profiles-network.md")
- [Creating source data providers in DMS Schema Conversion](data-providers-source.md "data-providers-source.md")
- [Creating and setting target data providers in DMS Schema Conversion](data-providers-target.md "data-providers-target.md")
- [Virtual mode for offline source and virtual target](virtual-data-provider.md "virtual-data-provider.md")
- [Managing migration projects in DMS Schema Conversion](sc-migration-projects.md "sc-migration-projects.md")
- [Conversion assessment reports with DMS Schema Conversion](assessment-reports.md "assessment-reports.md")
- [Using DMS Schema Conversion](schema-conversion.md "schema-conversion.md")
- [Using AI agents with DMS Schema Conversion](sc-genai-agents.md "sc-genai-agents.md")
- [Using extension packs in DMS Schema Conversion](extension-pack.md "extension-pack.md")

## How DMS Schema Conversion works

DMS Schema Conversion converts your schema with a rules-based engine. The rules produce consistent,
repeatable results, so you can rely on them across a large schema without checking every
object by hand. When the rules can't fully convert an object, DMS Schema Conversion can use
generative AI to convert more of it, so you have less to finish manually.

###### Note

DMS Schema Conversion is a fully managed, web-based feature that builds on the AWS Schema Conversion Tool
(AWS SCT) conversion engine.

DMS Schema Conversion uses three resources to work with your databases:

Instance profile

Specifies the network and security settings DMS Schema Conversion uses to connect to
your source and target databases and to encrypt your conversion data.

Data provider

Stores the connection details for a source or target database, such as its
type, server name, and port.

Migration project

Brings together a source data provider, a target data provider, and an
instance profile, along with the AWS Secrets Manager secrets that hold your database
credentials.

The following diagram shows how these resources fit together. Each of your source and
target databases is represented by a data provider. The migration project uses both data
providers and the instance profile, and it's where DMS Schema Conversion converts your schema.

![Source and target databases each connect through a data provider to a migration project, where the schema is converted.](images/dms-schema-conversion-diagram.png)

## Key capabilities

Assess your migration

DMS Schema Conversion reads your source metadata and creates a conversion assessment
report that shows what it can convert automatically and what needs manual
work. Use the report to estimate the effort of a migration before you commit
to it. For more information, see [Conversion assessment reports with DMS Schema Conversion](assessment-reports.md "assessment-reports.md").

Convert your schema

DMS Schema Conversion converts tables, views, stored procedures, functions, and other
objects. You can customize the results with transformation rules, which
change object names and data types, and with conversion settings for each
conversion path. For objects that the rules can't fully convert, generative
AI conversion can convert more of them for you to review. For more
information, see [Using DMS Schema Conversion](schema-conversion.md "schema-conversion.md").

Apply or export your converted code

You can compare the source and converted code, and edit the converted SQL.
When you're ready, apply the converted code to your target database, or
export it as SQL scripts to an Amazon S3 bucket. If your source database uses
features that the target database doesn't have, DMS Schema Conversion adds an extension
pack that emulates some of them. For more information, see [Saving and applying your converted code in DMS Schema Conversion](schema-conversion-save-apply.md "schema-conversion-save-apply.md") and [Using extension packs in DMS Schema Conversion](extension-pack.md "extension-pack.md").

## Supported conversion paths

The following table lists the conversion paths that DMS Schema Conversion supports, including
which paths support generative AI conversion.

| Source database  | Target database                         | Generative AI conversion |
| ---------------- | --------------------------------------- | ------------------------ |
| Oracle           | Aurora PostgreSQL or RDS for PostgreSQL | Yes                      |
| Oracle           | Aurora MySQL or RDS for MySQL           | No                       |
| Oracle           | Amazon Redshift                         | No                       |
| SQL Server       | Aurora PostgreSQL or RDS for PostgreSQL | Yes                      |
| SQL Server       | Aurora MySQL or RDS for MySQL           | No                       |
| PostgreSQL       | Aurora MySQL or RDS for MySQL           | No                       |
| MySQL            | Aurora PostgreSQL or RDS for PostgreSQL | No                       |
| IBM Db2 for LUW  | Aurora PostgreSQL or RDS for PostgreSQL | Yes                      |
| IBM Db2 for z/OS | Aurora PostgreSQL or RDS for PostgreSQL | Yes                      |
| IBM Db2 for z/OS | Amazon RDS for Db2                      | No                       |
| SAP ASE          | Aurora PostgreSQL or RDS for PostgreSQL | Yes                      |

###### Note

IBM Db2 for z/OS conversion paths are not available in the
AWS Management Console. To use these conversion paths, use the AWS DMS API or AWS CLI.

For the supported versions of each database, see [Sources for DMS Schema Conversion](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion "CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.SchemaConversion") and [Targets for DMS Schema Conversion](CHAP_Introduction.Targets.md#CHAP_Introduction.Targets.SchemaConversion "CHAP_Introduction.Targets.md#CHAP_Introduction.Targets.SchemaConversion"). For more
information about generative AI conversion, including how it uses cross-Region inference,
see [Converting database objects with generative AI](schema-conversion-convert.databaseobjects.md "schema-conversion-convert.databaseobjects.md").

## Supported AWS Regions

The following table lists the AWS Regions where you can create a DMS Schema Conversion migration
project, including where generative AI conversion is available.

| Region name                | Region         | Generative AI conversion |
| -------------------------- | -------------- | ------------------------ |
| Africa (Cape Town)         | af-south-1     | No                       |
| Asia Pacific (Hong Kong)   | ap-east-1      | No                       |
| Asia Pacific (Taipei)      | ap-east-2      | No                       |
| Asia Pacific (Tokyo)       | ap-northeast-1 | Yes                      |
| Asia Pacific (Seoul)       | ap-northeast-2 | No                       |
| Asia Pacific (Osaka)       | ap-northeast-3 | Yes                      |
| Asia Pacific (Mumbai)      | ap-south-1     | No                       |
| Asia Pacific (Hyderabad)   | ap-south-2     | No                       |
| Asia Pacific (Singapore)   | ap-southeast-1 | No                       |
| Asia Pacific (Sydney)      | ap-southeast-2 | Yes                      |
| Asia Pacific (Jakarta)     | ap-southeast-3 | No                       |
| Asia Pacific (Melbourne)   | ap-southeast-4 | No                       |
| Asia Pacific (Malaysia)    | ap-southeast-5 | No                       |
| Asia Pacific (New Zealand) | ap-southeast-6 | No                       |
| Asia Pacific (Thailand)    | ap-southeast-7 | No                       |
| Canada (Central)           | ca-central-1   | Yes                      |
| Canada West (Calgary)      | ca-west-1      | No                       |
| Europe (Frankfurt)         | eu-central-1   | Yes                      |
| Europe (Zurich)            | eu-central-2   | Yes                      |
| Europe (Stockholm)         | eu-north-1     | Yes                      |
| Europe (Milan)             | eu-south-1     | Yes                      |
| Europe (Spain)             | eu-south-2     | Yes                      |
| Europe (Ireland)           | eu-west-1      | Yes                      |
| Europe (London)            | eu-west-2      | Yes                      |
| Europe (Paris)             | eu-west-3      | Yes                      |
| Israel (Tel Aviv)          | il-central-1   | No                       |
| Middle East (UAE)          | me-central-1   | No                       |
| Middle East (Bahrain)      | me-south-1     | No                       |
| Mexico (Central)           | mx-central-1   | No                       |
| South America (São Paulo)  | sa-east-1      | No                       |
| US East (N. Virginia)      | us-east-1      | Yes                      |
| US East (Ohio)             | us-east-2      | Yes                      |
| US West (N. California)    | us-west-1      | No                       |
| US West (Oregon)           | us-west-2      | Yes                      |

To convert a database that runs in a Region that isn't listed, create your migration
project in a supported Region. Then set up cross-Region connectivity between the VPC in
that Region and the VPC where your database runs. For more information, see [Setting up a network for DMS Schema Conversion](instance-profiles-network.md "instance-profiles-network.md").
