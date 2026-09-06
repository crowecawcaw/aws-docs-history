

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Database (DB) import to AMS RDS for Microsoft SQL Server
<a name="db-to-sql-rds"></a>

**Note**  
The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1` when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.

The DB import to AMS RDS for SQL Server, process relies on AMS change types (CTs) submitted as requests for change (RFCs), and uses the Amazon RDS API parameters as input. MicroSoft SQL Server is a relational database management system (RDBMS). To learn more, see also: [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) and [rds](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html) or [Amazon RDS API reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ProgrammingGuide.html).

**Note**  
Make sure each RFC completes successfully before moving on to the next step.

High level import steps:

1. Back up your source on-premises MS SQL database into a .bak (backup) file

1. Copy the .bak file into the transit (encrypted) Amazon Simple Storage Service (S3) bucket

1. Import the .bak into a new DB on your target Amazon RDS MS SQL instance

Requirements:
+ MS SQL RDS stack in AMS
+ RDS stack with restore option (`SQLSERVER_BACKUP_RESTORE`)
+ Transit S3 bucket
+ IAM role with bucket access allowing Amazon RDS to assume the role
+ An EC2 instance with MS SQL Management Studio installed to manage the RDS (can be a workstation on-premises)