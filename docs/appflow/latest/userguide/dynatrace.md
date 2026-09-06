

# Dynatrace
<a name="dynatrace"></a>

The following are the requirements and connection instructions for using Dynatrace with Amazon AppFlow.

**Note**  
You can use Dynatrace as a source only.

**Topics**
+ [Requirements](#dynatrace-requirements)
+ [Connection instructions](#dynatrace-setup)
+ [Notes](#dynatrace-notes)
+ [Supported destinations](#dynatrace-destinations)
+ [Related resources](#dynatrace-resources)

## Requirements
<a name="dynatrace-requirements"></a>
+ You must provide Amazon AppFlow with an API token. For more information about how to retrieve or generate an API token to use with Amazon AppFlow, see the [Access tokens](https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/) instructions in the Dynatrace documentation.
+ You must configure your flow with a date filter with a date range that does not exceed 30 days.

## Connection instructions
<a name="dynatrace-setup"></a>

**To connect to Dynatrace while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Dynatrace** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Dynatrace** dialog box.

   1. Under **API token**, enter your API token.

   1. Under **Subdomain**, enter the subdomain for your instance of Dynatrace.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Connect to Dynatrace dialog with fields for API token, subdomain, encryption key, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-dynatrace-console.png)

1. You will be redirected to the Dynatrace login page. When prompted, grant Amazon AppFlow permissions to access your Dynatrace account.

Now that you are connected to your Dynatrace account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#dynatrace-requirements).

## Notes
<a name="dynatrace-notes"></a>
+ When you use Dynatrace as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per minute.

## Supported destinations
<a name="dynatrace-destinations"></a>

When you create a flow that uses Dynatrace as the data source, you can set the destination to any of the following connectors: 
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
<a name="dynatrace-resources"></a>
+ [Access tokens](https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/) instructions in the Dynatrace documentation 
+  [Dynatrace API documentation](https://www.dynatrace.com/support/help/dynatrace-api/) for more information about the types of data you can extract from Dynatrace
+  [Dynatrace is launch partner of Amazon AppFlow – a service for easy and secure data transfer](https://www.dynatrace.com/news/blog/dynatrace-integrates-with-amazon-appflow/) from *Dynatrace Resources*