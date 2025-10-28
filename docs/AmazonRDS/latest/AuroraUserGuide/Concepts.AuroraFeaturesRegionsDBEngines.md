# Supported features in

Amazon Aurora by AWS Region and Aurora DB engine

Aurora MySQL- and PostgreSQL-compatible database engines support several Amazon Aurora and
Amazon RDS features and options. The support varies across specific versions of each database
engine, and across AWS Regions. To identify Aurora database engine version support and
availability for a feature in a given AWS Region, you can use the following
sections.

Some of these features are Aurora-only capabilities. For example, Aurora
Serverless, Aurora global databases, and support for integration with AWS
machine learning services aren't supported by Amazon RDS. Other features, such as
Amazon RDS Proxy, are supported by both Amazon Aurora and Amazon RDS.

###### Supported Regions and DB engines

- [Table
  conventions](#Concepts.Aurora_Fea_Regions_DB-eng.Feature.TableConventions "#Concepts.Aurora_Fea_Regions_DB-eng.Feature.TableConventions")
- [Blue/Green Deployments](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora cluster configurations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Database activity streams](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Exporting cluster data to Amazon S3](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Exporting snapshot data to Amazon S3](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora global databases](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [IAM database authentication](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Kerberos authentication](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora machine learning](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Performance Insights](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Zero-ETL integrations](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [RDS Proxy](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Secrets Manager integration](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora Serverless v2](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora Serverless v1](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [RDS Data API](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Zero-downtime patching (ZDP)](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Aurora PostgreSQL Limitless Database](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")
- [Engine-native features](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md")

## Table

conventions

The tables in the feature sections use the following patterns to specify version
numbers and level of support:

- **Version x.y** – The specific version
  alone is supported.
- **Version x.y and higher** – The specified
  version and all higher minor versions of its major version are supported. For
  example, "version 10.11 and higher" means that versions 10.11,
  10.11.1, and 10.12 are supported.
