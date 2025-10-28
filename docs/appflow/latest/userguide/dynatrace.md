# Dynatrace

The following are the requirements and connection instructions for using Dynatrace with
Amazon AppFlow.

###### Note

You can use Dynatrace as a source only.

###### Topics

- [Requirements](#dynatrace-requirements "#dynatrace-requirements")
- [Connection instructions](#dynatrace-setup "#dynatrace-setup")
- [Notes](#dynatrace-notes "#dynatrace-notes")
- [Supported destinations](#dynatrace-destinations "#dynatrace-destinations")
- [Related resources](#dynatrace-resources "#dynatrace-resources")

## Requirements

- You must provide Amazon AppFlow with an API token. For more information about how to retrieve
  or generate an API token to use with Amazon AppFlow, see the [Access tokens](https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/ "https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/") instructions in the Dynatrace documentation.
- You must configure your flow with a date filter with a date range that does not exceed 30
  days.

## Connection instructions

###### To connect to Dynatrace while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings** and
    then choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Dynatrace** from the **Source name** dropdown
    list.
8.  Choose **Connect** to open the **Connect to Dynatrace**
    dialog box.

        1. Under **API token**, enter your API token.
        2. Under **Subdomain**, enter the subdomain for your instance of
         Dynatrace.
        3. Under **Data encryption**, enter your AWS KMS key.
        4. Under **Connection name**, specify a name for your connection.
        5. Choose **Connect**.

    ![Dynatrace connection form with fields for API token, subdomain, data encryption, and connection name.](images/connection_setup-dynatrace-console.png)

9.  You will be redirected to the Dynatrace login page. When prompted, grant Amazon AppFlow
    permissions to access your Dynatrace account.

Now that you are connected to your Dynatrace account, you can continue with the flow
creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#dynatrace-requirements "#dynatrace-requirements").

## Notes

- When you use Dynatrace as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per minute.

## Supported destinations

When you create a flow that uses Dynatrace as the data source, you can set the destination to any of the following connectors:

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

- [Access tokens](https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/ "https://www.dynatrace.com/support/help/reference/dynatrace-concepts/access-tokens/") instructions in the Dynatrace documentation
- [Dynatrace API
  documentation](https://www.dynatrace.com/support/help/dynatrace-api/ "https://www.dynatrace.com/support/help/dynatrace-api/") for more information about the types of data you can extract from
  Dynatrace
- [Dynatrace is launch partner of Amazon AppFlow – a service for easy and secure data
  transfer](https://www.dynatrace.com/news/blog/dynatrace-integrates-with-amazon-appflow/ "https://www.dynatrace.com/news/blog/dynatrace-integrates-with-amazon-appflow/") from _Dynatrace Resources_
