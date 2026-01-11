# Prerequisites for migrating from Amazon RDS for Oracle to Amazon Aurora MySQL

The following prerequisites are also required to complete this walkthrough:

- Familiarity with Amazon RDS, the applicable database technologies, and SQL.
- The custom scripts that include creating the tables to be migrated and SQL queries for confirming the migration, as listed following:
  - `Oracle-HR-Schema-Build.sql` — SQL statements to build the **HR** schema.
  - `Oracle_Aurora_For_DMSDemo.template` — an AWS CloudFormation template.

  These scripts are available at the following link: [`dms-sbs-RDSOracle2Aurora.zip`](samples/dms-sbs-RDSOracle2Aurora.md "samples/dms-sbs-RDSOracle2Aurora.md").

  Each step in the walkthrough also contains a link to download the file involved or includes the exact query in the step.

- A user with AWS Identity and Access Management (IAM) credentials that allow you to launch Amazon Relational Database Service (Amazon RDS) and AWS Database Migration Service (AWS DMS) instances in your AWS Region. For information about IAM credentials, see [Setting up for Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM "../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM").
- Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups. For information about using Amazon VPC with Amazon RDS, see [Amazon VPC VPCs and Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md"). For information about Amazon RDS security groups, see [Amazon RDS Security Groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md").
- An understanding of the supported features and limitations of AWS DMS. For information about AWS DMS, see [https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html](../userguide/Welcome.md "../userguide/Welcome.md").
- Knowledge of the supported data type conversion options for Oracle and Amazon Aurora MySQL. For information about data types for Oracle as a source, see [Using an Oracle database as a source](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md"). For information about data types for Amazon Aurora MySQL as a target, see [Using a MySQL-Compatible database as a target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md").
  For more information about AWS DMS, see [Getting started with Database Migration Service](../userguide/CHAP_GettingStarted.md "../userguide/CHAP_GettingStarted.md").
