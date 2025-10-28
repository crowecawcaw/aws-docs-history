# Singular

The following are the requirements and connection instructions for using Singular with
Amazon AppFlow.

###### Note

You can use Singular as a source only.

###### Topics

- [Requirements](#singular-requirements "#singular-requirements")
- [Connection instructions](#singular-setup "#singular-setup")
- [Notes](#singular-notes "#singular-notes")
- [Supported destinations](#singular-destinations "#singular-destinations")
- [Related resources](#singular-resources "#singular-resources")

## Requirements

- You must provide Amazon AppFlow with an API key. For more information about retrieving your
  client ID and client secret, see [Authentication](https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference "https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference") in the Singular documentation.
- The date range for the flow cannot exceed 30 days.
- The flow cannot return more than 100,000 records.

## Connection instructions

###### To connect to Singular while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Singular** from the **Source name** dropdown
    list.
8.  Choose **Connect** to open the **Connect to Singular**
    dialog box.

        1. Under **API key**, enter your API key.
        2. Under **Data encryption**, enter your AWS KMS key.
        3. Under **Connection name**, specify a name for your connection.
        4. Choose **Connect**.

    ![Connect to Singular dialog with fields for API key, data encryption, and connection name.](images/connection_setup-singular-console.png)

9.  You will be redirected to the Singular login page. When prompted, grant Amazon AppFlow
    permissions to access your Singular account.

Now that you are connected to your Singular account, you can continue with the flow creation
steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#singular-requirements "#singular-requirements") section.

## Notes

- When you use Singular as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per hour.

## Supported destinations

When you create a flow that uses Singular as the data source, you can set the destination to any of the following connectors:

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

- [Authentication](https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference "https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference") in the Singular documentation
- [Load all your paid marketing with
  Amazon AppFlow. No code required.](https://www.singular.net/amazon-appflow/ "https://www.singular.net/amazon-appflow/") from Singular
