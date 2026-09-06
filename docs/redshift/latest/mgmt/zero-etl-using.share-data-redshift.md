

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Sharing your data in Amazon Redshift
<a name="zero-etl-using.share-data-redshift"></a>

After you add data to the source, it's immediately replicated into Amazon Redshift and ready to be shared by creating datashares. 

To share data, you must create a destination database first.

**To share data in Amazon Redshift Serverless using the Amazon Redshift console**

1. In the Amazon Redshift console, in the left navigation pane, choose **Amazon Redshift Serverless > Serverless dashboard**.

1. From the left navigation pane, choose **Zero-ETL integrations**.

1. Choose **Share data**.

1. On the create datashare page, follow the steps in [Creating datashares](https://docs.aws.amazon.com/redshift/latest/dg/datashare-creation.html).

**To share data in Amazon Redshift provisioned clusters using the Amazon Redshift console**

1. In the Amazon Redshift console, in the left navigation pane, choose **Provisioned clusters dashboard**.

1. From the left navigation pane, choose **Zero-ETL integrations**.

1. From the integration list, choose an integration.

1. On the integration details page, choose **Connect to database**.

1. On the **Connection to database** page, you can either create a new connection or use a recent connection. Make sure that the connection is made to the destination database.

1. If you create a new connection, then enter a **Database name** for the database. Then, click **Connect**.

1. On the integration details page, choose **Share data**.

1. On the create datashare page, follow the steps in [Creating datashares](https://docs.aws.amazon.com/redshift/latest/dg/datashare-creation.html).