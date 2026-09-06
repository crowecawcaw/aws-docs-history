

# Troubleshooting querying in Amazon Athena
<a name="querying-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when using Athena to query objects that are stored in your Security Lake S3 bucket. For more Athena troubleshooting topics, see the [Troubleshooting in Athena](https://docs.aws.amazon.com/athena/latest/ug/troubleshooting-athena.html) section of the *Amazon Athena User Guide*.

## Querying isn't returning new objects in the data lake
<a name="query-not-returning-objects"></a>

Your Athena query may not return new objects in your data lake even when the S3 bucket for Security Lake contains those objects. This may occur if you've disabled Security Lake and then enabled it again. As a result, the AWS Glue partitions may not properly register the new objects.

To resolve the error, follow these steps:

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. From the navigation bar, on the Regions selector, choose the Region in which Security Lake is enabled but the Athena query isn't returning results.

1. From the navigation pane, choose **Functions**, and select the function from the following list depending on the source version:
   + `Source version 1 (OCSF 1.0.0-rc.2) ` – **SecurityLake\_Glue\_Partition\_Updater\_Lambda\_{{≪region>}}** function.
   + `Source version 2 (OCSF 1.1.0)` – **AmazonSecurityLakeMetastoreManager\_{{≪region>}}** function.

1. On the **Configurations** tab, choose **Triggers**.

1. Select the option next to the function, and choose **Edit**.

1. Select **Activate trigger**, and choose **Save**. This will turn the function state to **Enabled**.

## Unable to access AWS Glue tables
<a name="access-glue-tables"></a>

A query access subscriber may not be able to access AWS Glue tables that contain Security Lake data.

First, ensure that you've followed the steps outlined in [Setting up cross-account table sharing (subscriber step)](create-query-subscriber-procedures.md#grant-query-access-subscriber).

If the subscriber still doesn't have access, follow these steps:

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. From the navigation pane, choose **Data Catalog** and **Catalog settings**.

1. Give permission to the subscriber to access the AWS Glue tables with a resource-based policy. For information about creating resource-based policies, see [Resource-based policy examples for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/security_iam_resource-based-policy-examples.html) in the *AWS Glue Developer Guide*.