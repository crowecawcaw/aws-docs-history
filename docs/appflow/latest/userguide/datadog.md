# Datadog

The following are the requirements and connection instructions for using Datadog with
Amazon AppFlow.

###### Note

You can use Datadog as a source only.

###### Topics

- [Requirements](#datadog-requirements "#datadog-requirements")
- [Connection instructions](#datadog-setup "#datadog-setup")
- [Notes](#datadog-notes "#datadog-notes")
- [Supported destinations](#datadog-destinations "#datadog-destinations")
- [Related resources](#datadog-resources "#datadog-resources")

## Requirements

- You must provide Amazon AppFlow with an API key and an application key. For more information
  about how to retrieve your API key and application key, see the [API and Application
  Keys](https://docs.datadoghq.com/account_management/api-app-keys/ "https://docs.datadoghq.com/account_management/api-app-keys/") information in the Datadog documentation.
- You must configure your flow with a date range and query filter.

## Connection instructions

###### To connect to Datadog while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Datadog** from the **Source name** dropdown
    list.
8.  Choose **Connect** to open the **Connect to Datadog**
    dialog box.

        1. Under **API key**, enter your API key.
        2. Under **Application key**, enter your application key.
        3. Under **Select region**, select the region for your instance of
         Datadog.
        4. Under **Data encryption**, enter your AWS KMS key.
        5. Under **Connection name**, specify a name for your connection.
        6. Choose **Connect**.

    ![Datadog connection form with API key, Application key, region selection, and encryption options.](images/connection_setup-datadog-console.png)

9.  You will be redirected to the Datadog login page. When prompted, grant Amazon AppFlow
    permissions to access your Datadog account.

Now that you are connected to your Datadog, you can continue with the flow creation steps as
described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#datadog-requirements "#datadog-requirements") section.

## Notes

- When you use Datadog as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per minute.

## Supported destinations

When you create a flow that uses Datadog as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon Honeycode
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

- [API and
  Application Keys](https://docs.datadoghq.com/account_management/api-app-keys/ "https://docs.datadoghq.com/account_management/api-app-keys/") information in the _Datadog_ documentation
