AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Migration Hub Orchestrator templates

Migration Hub Orchestrator offers the following templates to configure your migration workflows:

- Migrate SAP NetWeaver applications to AWS – A
  template to migrate SAP NetWeaver-based applications (S/4HANA, BW4HANA, and ECC on HANA) running
  on SAP HANA database to AWS.
- Rehost applications on Amazon EC2 – A template to rehost
  applications on Amazon EC2 using AWS Application Migration Service (AWS MGN).
- Rehost SQL Server on Amazon EC2 – A template to rehost
  SQL Server on Amazon EC2 using automated SQL Server backup and restore.
- Replatform SQL Server on Amazon Relational Database Service (Amazon RDS) – A
  template to replatform SQL Server on Amazon RDS using native SQL Server backup and restore.
- Replatform applications to Amazon ECS – A template to
  replatform applications to containers on Amazon Elastic Container Service (Amazon ECS).
- Import virtual machine images to AWS – A template
  to import virtual machine (VM) images to AWS as an Amazon Machine Image (AMI) for Amazon EC2.
- Custom templates – A template that you have created
  by modifying an existing AWS managed template and saving the changes.
  Before you can run the workflow, some templates require the Migration Hub Orchestrator plugin
  to be configured on-premises. The plugin communicates with the source and target environments to orchestrate
  and automate migrations. To download and setup the Migration Hub Orchestrator plugin, see [Configure Migration Hub Orchestrator
  plugin](configure-plugin.md "configure-plugin.md"). The following table indicates which templates require the plugin setup.

| Template                                                                             | Plugin setup required |
| ------------------------------------------------------------------------------------ | --------------------- |
| [Migrate SAP<br>NetWeaver applications to AWS](migrate-sap.md "migrate-sap.md")      | Yes                   |
| [Rehost<br>applications on Amazon EC2](rehost-on-ec2.md "rehost-on-ec2.md")          | Yes                   |
| [Rehost SQL<br>server on Amazon EC2](rehost-sql-ec2.md "rehost-sql-ec2.md")          | Yes                   |
| [Replatform SQL server on Amazon RDS](replatform-sql-rds.md "replatform-sql-rds.md") | Yes                   |
| [Import<br>virtual machine images to AWS](import-vm-images.md "import-vm-images.md") | Optional              |
| [Replatform applications to Amazon ECS](replatform-to-ecs.md "replatform-to-ecs.md") | No                    |
