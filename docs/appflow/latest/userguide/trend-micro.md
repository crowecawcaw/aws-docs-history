

# Trend Micro
<a name="trend-micro"></a>

The following are the requirements and connection instructions for using Trend Micro with Amazon AppFlow.

**Note**  
You can use Trend Micro as a source only.

**Topics**
+ [Requirements](#trendmicro-requirements)
+ [Connection instructions](#trendmicro-setup)
+ [Notes](#trendmicro-notes)
+ [Supported destinations](#trend-micro-destinations)
+ [Related resources](#trendmicro-resources)

## Requirements
<a name="trendmicro-requirements"></a>

You must provide Amazon AppFlow with an API secret. For more information about how to generate or retrieve an API secret from Trend Micro, see [Create and Manage API Keys](https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/) in the *Trend Micro* documentation.

## Connection instructions
<a name="trendmicro-setup"></a>

**To connect to Trend Micro while creating a flow:**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Trend Micro** from the **Source name** drop-down list.

1. Choose **Connect** or **Connect with PrivateLink** to open the **Connect to Trend Micro** dialog box.

   1. Under **API secret key**, enter your API secret key.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Connect to Trend Micro dialog with fields for API secret key, AWS KMS key, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-trendmicro-console.png)

Now that you are connected to your Trend Micro account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#trendmicro-requirements) section.

## Notes
<a name="trendmicro-notes"></a>
+ When you use Trend Micro as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per hour.

## Supported destinations
<a name="trend-micro-destinations"></a>

When you create a flow that uses Trend Micro as the data source, you can set the destination to any of the following connectors: 
+ Amazon Connect Customer
+ Amazon Honeycode
+ Lookout for Metrics
+ Amazon Redshift
+ Amazon S3
+ Marketo
+ Salesforce
+ Snowflake
+ Upsolver
+ Zendesk

You can also set the destination to any custom connectors that you create with the Amazon AppFlow Custom Connector SDKs for [ Python](https://github.com/awslabs/aws-appflow-custom-connector-python) or [Java ](https://github.com/awslabs/aws-appflow-custom-connector-java). You can download these SDKs from GitHub.

## Related resources
<a name="trendmicro-resources"></a>
+  [Create and Manage API Keys](https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/) in the Trend Micro documentation 