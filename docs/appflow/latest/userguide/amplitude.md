

# Amplitude
<a name="amplitude"></a>

The following are the requirements and connection instructions for using Amplitude with Amazon AppFlow.

**Note**  
You can use Amplitude as a source only.

**Topics**
+ [Requirements](#amplitude-requirements)
+ [Connection instructions](#amplitude-setup)
+ [Notes](#amplitude-notes)
+ [Supported destinations](#amplitude-destinations)
+ [Related resources](#amplitude-resources)

## Requirements
<a name="amplitude-requirements"></a>

You must provide Amazon AppFlow with the API key and secret key for the project with the data that you want to transfer. Your API key can be found on the Settings page of the Amplitude dashboard. For more information about how to retrieve this information from Amplitude, see [Settings](https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings) in the Amplitude documentation.

## Connection instructions
<a name="amplitude-setup"></a>

**To connect to Amplitude while creating a flow**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. Choose **Create flow**.

1. For **Flow details**, enter a name and description for the flow.

1. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose **Data encryption**, **Customize encryption settings** and then choose an existing CMK or create a new one.

1. (Optional) To add a tag, choose **Tags**, **Add tag** and then enter the key name and value.

1. Choose **Next**.

1. Choose **Amplitude** from the **Source name** dropdown list.

1. Choose **Connect** to open the **Connect to Amplitude** dialog box.

   1. Under **API key**, enter your API key.

   1. Under **Secret key**, enter your secret key.

   1. Under **Data encryption**, enter your AWS KMS key.

   1. Under **Connection name**, specify a name for your connection.

   1. Choose **Connect**.  
![Connect to Amplitude dialog with fields for API key, secret key, AWS KMS key, and connection name.](http://docs.aws.amazon.com/appflow/latest/userguide/images/connection_setup-amplitude-console.png)

1. You will be redirected to the Amplitude login page. When prompted, grant Amazon AppFlow permissions to access your Amplitude account.

Now that you are connected to your Amplitude account, you can continue with the flow creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md).

**Tip**  
If you aren’t connected successfully, ensure that you have followed the instructions in the [Requirements](#amplitude-requirements).

## Notes
<a name="amplitude-notes"></a>
+ When you use Amplitude as a source, you can run schedule-triggered flows at a maximum frequency of one flow run per day.
+ Amplitude can process 25 MB of data as part of a single flow run.

## Supported destinations
<a name="amplitude-destinations"></a>

When you create a flow that uses Amplitude as the data source, you can set the destination to any of the following connectors: 
+ Lookout for Metrics
+ Amazon S3

You can also set the destination to any custom connectors that you create with the Amazon AppFlow Custom Connector SDKs for [ Python](https://github.com/awslabs/aws-appflow-custom-connector-python) or [Java ](https://github.com/awslabs/aws-appflow-custom-connector-java). You can download these SDKs from GitHub.

## Related resources
<a name="amplitude-resources"></a>
+  [Settings](https://help.amplitude.com/hc/en-us/articles/235649848#project-general-settings) in the Amplitude documentation
+  [Breaking Data Silos with Amazon AppFlow and Amplitude](https://amplitude.com/blog/aws-appflow-amplitude-announcement) from *Inside Amplitude* 