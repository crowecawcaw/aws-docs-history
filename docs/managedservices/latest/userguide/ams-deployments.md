# AMS application deployments

_AMS Application Developer's_ guide provides detailed descriptions and walkthroughs for the following deployments:

- The AMS workload ingest CT allows you and an AMS cloud migration partner to easily move
  your existing workloads into an AMS-managed VPC.
  Using AMS workload ingest, you can create an AMS AMI by submitting an RFC with the Deployment | Ingestion |
  Stack from migration partner migrated instance | Create CT (ct-257p9zjk14ija).
  You must have an instance migrated from your on-premises to AWS by a migration partner, as well as a target AMS
  VPC and subnet, into which the instance will be ingested.

For details, see the _AMS Application Developer's_ guide at
[Workload Ingest](../appguide/ams-workload-ingest.md "../appguide/ams-workload-ingest.md").

- The AWS CloudFormation ingest change type (ct-36cn2avfrrj9v) feature allows you to easily use
  an existing CloudFormation template to deploy custom stacks in an AMS-managed VPC.

For details, see the _AMS Application Developer's_ guide at
[CloudFormation Template Ingest](../appguide/ams-cfn-ingest.md "../appguide/ams-cfn-ingest.md").

- You can import your on-premises database into a new database to your AMS-managed Amazon S3 bucket or Amazon RDS instance. You do this using a
  Deployment | Advanced stack components | Database Migration Service (DMS) change types, including Create replication instance (ct-27apldkhqr0ol),
  Create replication subnet group (ct-2q5azjd8p1ag5), Create replication task (ct-1d2fml15b9eth), Create source endpoint (ct-0attesnjqy2cx) or
  Create source endpoint (S3) (ct-2oxl37nphsrjz), and Create target endpoint (ct-3gf8dolbo8x9p) or Create target endpoint (S3) (ct-05muqzievnxk5).

For details, see the _AMS Application Developer's_ guide at
[Database Migration Service](ex-create-dms.md "ex-create-dms.md").

- You can import your on-premises MS SQL database into a new database on your AMS-managed RDS SQL instance. You do this using a
  variety of AMS change types, and the Amazon RDS API, plus AWS consoles.

For details, see the AMS Application Guide at
[Database (DB) Import to MS SQL RDS](../appguide/db-to-sql-rds.md "../appguide/db-to-sql-rds.md").
