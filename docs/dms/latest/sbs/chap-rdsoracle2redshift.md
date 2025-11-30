# Prerequisites for migrating from Amazon RDS for Oracle to Amazon Redshift

The following prerequisites are also required to complete this walkthrough:

- Familiarity with Amazon RDS, Amazon Redshift, the applicable database technologies, and SQL.
- The custom scripts that include creating the tables to be migrated and SQL queries for confirming the migration, as listed following:
  - `Oracle_Redshift_For_DMSDemo.template` — an AWS CloudFormation template.
  - `Oraclesalesstarschema.sql` — SQL statements to build the **SH** schema.

  These scripts are available at the following link: `dms-sbs-RDSOracle2Redshift.zip`.

  Each step in the walkthrough also contains a link to download the file involved or includes the exact query in the step.

- A user with AWS Identity and Access Management (IAM) credentials that allow you to launch Amazon RDS, AWS Database Migration Service (AWS DMS) instances, and Amazon Redshift clusters in your AWS Region. For information about IAM credentials, see [Setting up for Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM "../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM").
- Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups. For information about using Amazon VPC with Amazon RDS, see [Virtual Private Clouds (VPCs) and Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md"). For information about Amazon RDS security groups, see [Amazon RDS Security Groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md"). For information about using Amazon Redshift in a VPC, see [Managing Clusters in an Amazon Virtual Private Cloud (VPC)](../../../redshift/latest/mgmt/managing-clusters-vpc.md "../../../redshift/latest/mgmt/managing-clusters-vpc.md").
- An understanding of the supported features and limitations of AWS DMS. For information about AWS DMS, see [https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html](../userguide/Welcome.md "../userguide/Welcome.md").
- Knowledge of the supported data type conversion options for Oracle and Amazon Redshift. For information about data types for Oracle as a source, see [Using an Oracle database as a source](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md"). For information about data types for Amazon Redshift as a target, see [Using an Amazon Redshift Database as a Target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md").
  For more information about AWS DMS, see [Getting started with Database Migration Service](../userguide/CHAP_GettingStarted.md "../userguide/CHAP_GettingStarted.md").
