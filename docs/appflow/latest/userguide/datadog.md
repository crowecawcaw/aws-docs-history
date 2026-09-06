

# Datadog
<a name="datadog"></a>

The following are the requirements and connection instructions for using Datadog with Amazon AppFlow.

**Note**  
You can use Datadog as a source only.

**Topics**
+ [Requirements](#datadog-requirements)
+ [Connection instructions](#datadog-setup)
+ [Notes](#datadog-notes)
+ [Supported destinations](#datadog-destinations)
+ [Related resources](#datadog-resources)

## Requirements
<a name="datadog-requirements"></a>
+ You must provide Amazon AppFlow with an API key and an application key. For more information about how to retrieve your API key and application key, see the [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/) information in the Datadog documentation.
+ You must configure your flow with a date range and query filter.

## Connection instructions
<a name="datadog-setup"></a>

**To connect to Datadog while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Datadog** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Datadog** dialog box.

   1. Under **API key**, enter your API key.

   1. Under **Application key**, enter your application key.

   1. Under **Select region**, select the region for your instance of Datadog.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Datadog connection form with API key, Application key, region selection, and encryption options.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-datadog-console.png)

1. You will be redirected to the Datadog login page. When prompted, grant Amazon AppFlow permissions to access your Datadog account.

Now that you are connected to your Datadog, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#datadog-requirements) section.

## Notes
<a name="datadog-notes"></a>
+ When you use Datadog as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per minute.

## Supported destinations
<a name="datadog-destinations"></a>

When you create a flow that uses Datadog as the data source, you can set the destination to any of the following connectors: 
+ Amazon Connect Customer
+ Amazon Honeycode
+ Amazon Redshift
+ Amazon S3
+ Marketo
+ Salesforce
+ Snowflake
+ Upsolver
+ Zendesk

You can also set the destination to any custom connectors that you create with the Amazon AppFlow Custom Connector SDKs for [ Python](https://github.com/awslabs/aws-appflow-custom-connector-python) or [Java ](https://github.com/awslabs/aws-appflow-custom-connector-java). You can download these SDKs from GitHub.

## Related resources
<a name="datadog-resources"></a>
+ [API and Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/) information in the *Datadog* documentation