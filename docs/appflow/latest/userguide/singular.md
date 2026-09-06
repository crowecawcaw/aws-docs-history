

# Singular
<a name="singular"></a>

The following are the requirements and connection instructions for using Singular with Amazon AppFlow.

**Note**  
You can use Singular as a source only.

**Topics**
+ [Requirements](#singular-requirements)
+ [Connection instructions](#singular-setup)
+ [Notes](#singular-notes)
+ [Supported destinations](#singular-destinations)
+ [Related resources](#singular-resources)

## Requirements
<a name="singular-requirements"></a>
+ You must provide Amazon AppFlow with an API key. For more information about retrieving your client ID and client secret, see [Authentication](https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference) in the Singular documentation.
+ The date range for the flow cannot exceed 30 days.
+ The flow cannot return more than 100,000 records.

## Connection instructions
<a name="singular-setup"></a>

**To connect to Singular while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Singular** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Singular** dialog box.

   1. Under **API key**, enter your API key.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Connect to Singular dialog with fields for API key, AWS KMS key, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-singular-console.png)

1. You will be redirected to the Singular login page. When prompted, grant Amazon AppFlow permissions to access your Singular account.

Now that you are connected to your Singular account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#singular-requirements) section.

## Notes
<a name="singular-notes"></a>
+ When you use Singular as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per hour.

## Supported destinations
<a name="singular-destinations"></a>

When you create a flow that uses Singular as the data source, you can set the destination to any of the following connectors: 
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
<a name="singular-resources"></a>
+ [Authentication](https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference) in the Singular documentation
+ [Load all your paid marketing with Amazon AppFlow. No code required.](https://www.singular.net/amazon-appflow/) from Singular