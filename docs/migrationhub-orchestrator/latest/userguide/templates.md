

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Migration Hub Orchestrator templates
<a name="templates"></a>

Migration Hub Orchestrator offers the following templates to configure your migration workflows:
+ **Migrate SAP NetWeaver applications to AWS** – A template to migrate SAP NetWeaver-based applications (S/4HANA, BW4HANA, and ECC on HANA) running on SAP HANA database to AWS.
+ **Rehost applications on Amazon EC2** – A template to rehost applications on Amazon EC2 using AWS Application Migration Service (AWS MGN).
+ ** Rehost SQL Server on Amazon EC2 ** – A template to rehost SQL Server on Amazon EC2 using automated SQL Server backup and restore.
+ **Replatform SQL Server on Amazon Relational Database Service (Amazon RDS)** – A template to replatform SQL Server on Amazon RDS using native SQL Server backup and restore.
+ **Replatform applications to Amazon ECS** – A template to replatform applications to containers on Amazon Elastic Container Service (Amazon ECS).
+ **Import virtual machine images to AWS** – A template to import virtual machine (VM) images to AWS as an Amazon Machine Image (AMI) for Amazon EC2.
+ **Custom templates** – A template that you have created by modifying an existing AWS managed template and saving the changes.

Before you can run the workflow, some templates require the Migration Hub Orchestrator plugin to be configured on-premises. The plugin communicates with the source and target environments to orchestrate and automate migrations. To download and setup the Migration Hub Orchestrator plugin, see [Configure Migration Hub Orchestrator plugin](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/configure-plugin.html). The following table indicates which templates require the plugin setup.


| Template | Plugin setup required | 
| --- | --- | 
| [Migrate SAP NetWeaver applications to AWS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migrate-sap.html) | Yes | 
| [Rehost applications on Amazon EC2 ](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-on-ec2.html) | Yes | 
| [Rehost SQL server on Amazon EC2](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/rehost-sql-ec2.html) | Yes | 
| [Replatform SQL server on Amazon RDS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-sql-rds.html) | Yes | 
| [Import virtual machine images to AWS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html) | Optional | 
| [Replatform applications to Amazon ECS](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/replatform-to-ecs.html) | No | 