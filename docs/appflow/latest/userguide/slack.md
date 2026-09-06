

# Slack
<a name="slack"></a>

The following are the requirements and connection instructions for using Slack with Amazon AppFlow.

**Note**  
You can use Slack as a source only.

**Topics**
+ [Requirements](#slack-requirements)
+ [Connection instructions](#slack-setup)
+ [Notes](#slack-notes)
+ [Supported destinations](#slack-destinations)
+ [Related resources](#slack-resources)

## Requirements
<a name="slack-requirements"></a>
+ To create a Slack connection in Amazon AppFlow, you must note your client ID, client secret, and Slack instance name. To retrieve your client ID and secret from Slack, you first must create a Slack App if you haven't already. For more information about how to create an App and then retrieve your client ID and secret, see the [Slack documentation](https://api.slack.com/docs/sign-in-with-slack#sign-in-with-slack__details__create-your-slack-app-if-you-havent-already).
+ Set the redirect URL as follows:
  + https://console.aws.amazon.com/appflow/oauth for the us-east-1 Region
  + https://{{region}}.console.aws.amazon.com/appflow/oauth for all other Regions
+ Set the following user token scopes:
  + `channels:history`
  + `channels:read`
  + `groups:history`
  + `groups:read`
  + `im:history`
  + `im:read`
  + `mpim:history`
  + `mpim:read`

## Connection instructions
<a name="slack-setup"></a>

**To connect to Slack while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Slack** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Slack** dialog box.

   1. Under **Client ID**, enter your Slack client ID.

   1. Under **Client secret**, enter your Slack client secret.

   1. Under **Workspace**, enter the name of your Slack instance.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Continue**.  
![Slack connection form with fields for client ID, secret, workspace URL, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-slack-console.png)

1. You will be redirected to the Slack login page. When prompted, grant Amazon AppFlow permissions to access your Slack account.

Now that you are connected to your Slack account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#slack-requirements) section.

## Notes
<a name="slack-notes"></a>
+ When you use Slack as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per minute.

## Supported destinations
<a name="slack-destinations"></a>

When you create a flow that uses Slack as the data source, you can set the destination to any of the following connectors: 
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
<a name="slack-resources"></a>
+  [Retrieve your client ID and secret](https://api.slack.com/docs/sign-in-with-slack#sign-in-with-slack__details__create-your-slack-app-if-you-havent-already) in the Slack documentation
+  [New – Announcing Amazon AppFlow (dataflow: Slack, S3, Athena, QuickSight)](https://aws.amazon.com/blogs/aws/new-announcing-amazon-appflow) in the *AWS News* blog
+ How to transfer data from Slack to Amazon S3 using Amazon AppFlow  
