

# Zendesk
<a name="zendesk"></a>

The following are the requirements and connection instructions for using Zendesk with Amazon AppFlow.

**Note**  
You can use Zendesk as a source or a destination.

**Topics**
+ [Requirements](#zendesk-requirements)
+ [Connection instructions](#zendesk-setup)
+ [Notes](#zendesk-notes)
+ [Supported destinations](#zendesk-destinations)
+ [Related resources](#zendesk-resources)

## Requirements
<a name="zendesk-requirements"></a>
+ To use Amazon AppFlow, you need to register the application to generate OAuth credentials that your application can use to authenticate API calls to Zendesk. This is done in Zendesk Support.
+ In Zendesk, you must create an OAuth client with the following settings:
  + Unique identifier: aws\_integration\_to\_Zendesk
  + Redirect URL: https://console.aws.amazon.com/appflow/oauth (us-east-1) or https://{{region}}.console.aws.amazon.com/appflow/oauth (all other Regions)

For more information, see [Setting up the Amazon AppFlow integration with Zendesk](https://support.zendesk.com/hc/en-us/articles/360047196173-Setting-up-the-Amazon-AppFlow-integration-with-Zendesk#topic_lk1_xxn_4lb) in the Zendesk documentation.

## Connection instructions
<a name="zendesk-setup"></a>

**To connect to Zendesk while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Zendesk** from the **Source name** or **Destination name** dropdown list.

1. Choose **Connect** to open the **Connect to Zendesk** dialog box.

   1. Under **Client ID**, enter your Zendesk client ID.

   1. Under **Client secret**, enter your Zendesk client secret.

   1. Under **Account**, enter the name of your instance of Zendesk.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Continue**.  
![Zendesk connection form with fields for client ID, secret, account URL, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-zendesk-console.png)

Now that you are connected to your Zendesk account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#zendesk-requirements).

## Notes
<a name="zendesk-notes"></a>
+ When you use Zendesk as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per minute.
+ When you use Zendesk as a destination, the following additional settings are available:


| Setting name | Description | 
| --- | --- | 
| **Insert new records** |  +  This is the default data transfer option. <br />+  When you choose this setting, Amazon AppFlow inserts your source data into the chosen Zendesk object as a new record.   | 
| **Update existing records** |  +  When you choose this setting, Amazon AppFlow uses your source data to update existing records in Zendesk. For every source record, Amazon AppFlow looks for a matching record in Zendesk based on your criteria. You can specify matching criteria on the Map data fields page. To do so, select a field in the source application and map it to a Zendesk record ID or external field using the dropdown list. <br />+  When a matching record is found, Amazon AppFlow updates the record in Zendesk. If no matching record is found, Amazon AppFlow ignores the record or fails the flow per your chosen error handling option. You can specify your error handling preferences on the Configure flow page.   | 
| **Upsert records ** |  +  When you choose this setting, Amazon AppFlow performs an upsert operation in Zendesk. For every source record, Amazon AppFlow looks for a matching record in Zendesk based on your criteria. You can specify matching criteria on the Map data fields page. To do so, select a field in the source application and map it to a Zendesk external field using the dropdown list. <br />+  When a matching record is found, Amazon AppFlow updates the record in Zendesk. If no matching record is found, Amazon AppFlow inserts the data as a new record. Any errors in performing the operation are handled per your chosen error handling option. You can specify your error handling preferences on the Configure flow page.   | 

## Supported destinations
<a name="zendesk-destinations"></a>

When you create a flow that uses Zendesk as the data source, you can set the destination to any of the following connectors: 
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
<a name="zendesk-resources"></a>
+  [Setting up the Amazon AppFlow integration with Zendesk](https://support.zendesk.com/hc/en-us/articles/360047196173-Setting-up-the-Amazon-AppFlow-integration-with-Zendesk#topic_lk1_xxn_4lb) in the Zendesk documentation 
+  [Building great customer experiences with Zendesk and AWS](https://www.zendesk.com/blog/building-great-customer-experiences-zendesk-aws/) from Zendesk 
+ How to transfer data from Zendesk Support to Amazon S3 using Amazon AppFlow  
