# Getting started with Amazon Aurora Global Database

To get started with Aurora Global Database, first decide which Aurora DB engine you want to
use and in which AWS Regions. Only specific versions of the Aurora MySQL and Aurora PostgreSQL
database engines in certain AWS Regions support Aurora Global Database. For the complete
list, see [Supported Regions and DB engines for Aurora global databases](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

You can create an Aurora Global Database in one of the following ways:

- **Create a new Aurora Global Database with new Aurora DB clusters and Aurora DB instances**
  – You can do this by following the steps in [Creating an Amazon Aurora global database](aurora-global-database-creating.md "aurora-global-database-creating.md"). After
  you create the primary Aurora DB cluster, you then add the secondary AWS Region by following the
  steps in [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").
- **Use an existing Aurora DB cluster that supports the Aurora Global
  Database feature and add an AWS Region to it** – You can do this only
  if your existing Aurora DB cluster uses a DB engine version that
  is global-compatible.

Check whether you can choose **Add region** for
**Action** on the AWS Management Console when your Aurora DB cluster is selected. If
you can, you can use that Aurora DB cluster for your Aurora global cluster. For more
information, see [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md").
Before creating an Aurora Global Database, we recommend that you understand all configuration requirements.

###### Topics

- [Configuration requirements of an Amazon Aurora global database](aurora-global-database.configuration.md "aurora-global-database.configuration.md")
- [Creating an Amazon Aurora global database](aurora-global-database-creating.md "aurora-global-database-creating.md")
- [Adding an AWS Region to an Amazon Aurora global database](aurora-global-database-attaching.md "aurora-global-database-attaching.md")
- [Creating a headless Aurora DB cluster in a secondary Region](aurora-global-database-attach.console.md "aurora-global-database-attach.console.md")
- [Creating an Amazon Aurora global database from an Aurora or Amazon RDS snapshot](aurora-global-database.md "aurora-global-database.md")
