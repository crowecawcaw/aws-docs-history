# Trend Micro

The following are the requirements and connection instructions for using Trend Micro with
Amazon AppFlow.

###### Note

You can use Trend Micro as a source only.

###### Topics

- [Requirements](#trendmicro-requirements "#trendmicro-requirements")
- [Connection instructions](#trendmicro-setup "#trendmicro-setup")
- [Notes](#trendmicro-notes "#trendmicro-notes")
- [Supported destinations](#trend-micro-destinations "#trend-micro-destinations")
- [Related resources](#trendmicro-resources "#trendmicro-resources")

## Requirements

You must provide Amazon AppFlow with an API secret. For more information about how to generate
or retrieve an API secret from Trend Micro, see [Create and Manage API Keys](https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/ "https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/") in the _Trend Micro_
documentation.

## Connection instructions

###### To connect to Trend Micro while creating a flow:

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Trend Micro** from the **Source name**
    drop-down list.
8.  Choose **Connect** or **Connect with PrivateLink** to
    open the **Connect to Trend Micro** dialog box.

        1. Under **API secret key**, enter your API secret key.
        2. Under **Data encryption**, enter your AWS KMS key.
        3. Under **Connection name**, specify a name for your connection.
        4. Choose **Connect**.

    ![Connect to Trend Micro dialog with fields for API secret key, data encryption, and connection name.](images/connection_setup-trendmicro-console.png)

Now that you are connected to your Trend Micro account, you can continue with the flow
creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#trendmicro-requirements "#trendmicro-requirements")
section.

## Notes

- When you use Trend Micro as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per hour.

## Supported destinations

When you create a flow that uses Trend Micro as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon Honeycode
- Lookout for Metrics
- Amazon Redshift
- Amazon S3
- Marketo
- Salesforce
- Snowflake
- Upsolver
- Zendesk

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [Create and Manage API Keys](https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/ "https://automation.deepsecurity.trendmicro.com/article/12_0/create-and-manage-api-keys/") in the Trend Micro documentation
