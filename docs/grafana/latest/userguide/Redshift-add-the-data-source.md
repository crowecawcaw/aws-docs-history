# Manually adding the Amazon Redshift data

source

## Prerequisites

- You have access to **Amazon Redshift** from your account.

###### To add the Amazon Redshift data source:

1. Attach the [AmazonRedshiftAccessPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonGrafanaRedshiftAccess") to your workspace user role.
2. Ensure your user role is admin or editor.
3. Select the workspace you want to work on from the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
4. In the Grafana console side menu, pause on the **Configuration** (gear) icon, then choose **Data Sources**.
5. Choose **Add data source**.
6. Choose the **AWS Redshift** data source. If necessary, you
   can start typing `Redshift` in the search box to help you
   find it.
7. This opens the **Connection Details** page. Follow the steps
   in configuring the [Connection
   details settings](Redshift-config.md#Redshift-connection-details "Redshift-config.md#Redshift-connection-details").
