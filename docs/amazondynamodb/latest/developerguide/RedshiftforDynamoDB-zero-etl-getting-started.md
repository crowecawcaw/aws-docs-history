# Creating a DynamoDB

zero-ETL integration with Amazon Redshift

Before creating a zero-ETL integration, you must first set up your source DynamoDB
table and then the target Amazon Redshift data warehouse.

## Step

1: Configuring a source DynamoDB table

To create a zero-ETL integration with Amazon Redshift, you need to enable
point-in-time recovery (PITR) on your table. If you do not have PITR turned on,
the console can fix this for you during the integration setup process. For
details on how to enable PITR, see [Point-in-time recovery](PointInTimeRecovery_Howitworks.md "PointInTimeRecovery_Howitworks.md").

## Step 2:

Creating an Amazon Redshift data warehouse

If you don't already have an Amazon Redshift data warehouse, you can create one. To
create an Amazon Redshift Serverless workgroup, see [Creating a workgroup with a namespace](../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md "../../../redshift/latest/mgmt/serverless-console-workgroups-create-workgroup-wizard.md"). To create an Amazon Redshift cluster,
see [Creating a cluster](../../../redshift/latest/mgmt/create-cluster.md "../../../redshift/latest/mgmt/create-cluster.md").

The target Amazon Redshift workgroup or cluster must have the
enable_case_sensitive_identifier parameter turned on for the integration to be
successful. For more information on enabling case sensitivity, see [Turn
on case sensitivity for your data warehouse](../../../redshift/latest/mgmt/zero-etl-setting-up.md "../../../redshift/latest/mgmt/zero-etl-setting-up.md") in the Amazon Redshift
management guide.

After the Amazon Redshift workgroup or cluster setup is complete, you need to
configure your data warehouse. See [Zero-ETL integrations](../../../redshift/latest/mgmt/zero-etl-using.md "../../../redshift/latest/mgmt/zero-etl-using.md")
in the Amazon Redshift Management Guide for more information.

##

Step 3: Creating a DynamoDB zero-ETL integration

Before you create a zero-ETL integration, make sure to complete the tasks in
the section titled [Prerequisites before creating
a DynamoDB zero-ETL integration with Amazon Redshift](RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs "RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs"). Creating an
integration between DynamoDB and Amazon Redshift is a two-step process. First create an
integration from the DynamoDB, and then attach a Amazon Redshift database to this newly
created integration.

###### Create a zero-ETL

integration

1. Sign in to the AWS Management Console and open the Amazon DynamoDB
   console at [https://console.aws.amazon.com/dynamodbv2](https://console.aws.amazon.com/dynamodbv2 "https://console.aws.amazon.com/dynamodbv2").
2. In the navigation pane, choose **Integrations**.
3. Select **Create zero-ETL integration** and choose
   **Amazon Redshift**.
4. This will take you to the **Amazon Redshift console**. To
   continue with the procedure, see the **DynamoDB section**
   in [Create a zero-ETL integration for DynamoDB](../../../redshift/latest/mgmt/zero-etl-setting-up.md "../../../redshift/latest/mgmt/zero-etl-setting-up.md").
