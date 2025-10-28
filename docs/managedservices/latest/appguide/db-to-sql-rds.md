# Database (DB) import to AMS RDS for Microsoft SQL Server

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

The DB import to AMS RDS for SQL Server, process relies on AMS change types (CTs) submitted as requests for change (RFCs), and uses the
Amazon RDS API parameters as input. MicroSoft SQL Server is a relational database management system (RDBMS). To learn more, see also:
[Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/") and
[rds](../../../cli/latest/reference/rds/index.md "../../../cli/latest/reference/rds/index.md") or
[Amazon RDS API reference](../../../AmazonRDS/latest/UserGuide/ProgrammingGuide.md "../../../AmazonRDS/latest/UserGuide/ProgrammingGuide.md").

###### Note

Make sure each RFC completes successfully before moving on to the next step.

High level import steps:

1. Back up your source on-premises MS SQL database into a .bak (backup) file
2. Copy the .bak file into the transit (encrypted) Amazon Simple Storage Service (S3) bucket
3. Import the .bak into a new DB on your target Amazon RDS MS SQL instance
   Requirements:

- MS SQL RDS stack in AMS
- RDS stack with restore option (`SQLSERVER_BACKUP_RESTORE`)
- Transit S3 bucket
- IAM role with bucket access allowing Amazon RDS to assume the role
- An EC2 instance with MS SQL Management Studio installed to manage the RDS (can be a workstation on-premises)
