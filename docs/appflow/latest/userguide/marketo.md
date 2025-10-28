# Marketo

The following are the requirements and connection instructions for using Marketo with
Amazon AppFlow.

###### Note

You can use Marketo as a source or destination.

###### Topics

- [Requirements](#marketo-requirements "#marketo-requirements")
- [Connection instructions](#marketo-setup "#marketo-setup")
- [Notes](#marketo-notes "#marketo-notes")
- [Supported destinations](#marketo-destinations "#marketo-destinations")
- [Related resources](#marketo-resources "#marketo-resources")

## Requirements

You must provide Amazon AppFlow with your client ID and client secret. For more information
about how to retrieve your client ID and client secret, see [Credentials for API Access](https://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API#CreateaCustomServiceforUsewithReSTAPI-CredentialsforAPIAccess "https://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API#CreateaCustomServiceforUsewithReSTAPI-CredentialsforAPIAccess") in the Marketo documentation.

## Connection instructions

###### To connect to Marketo while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
    **Data encryption**, **Customize encryption settings**. Then
    choose an existing CMK or create a new one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**,
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Marketo** from the **Source name** or
    **Destination name** dropdown list.
8.  Choose **Connect** to open the **Connect to Marketo**
    dialog box.

        1. Under **Client ID**, enter your Marketo client ID.
        2. Under **Client secret**, enter your client secret.
        3. Under **Account/Munchkin ID**, specify the unique part of the base URL
         or endpoint assigned to your Marketo account.
        4. Under **Data encryption**, enter your AWS KMS key.
        5. Under **Connection name**, specify a name for your connection.
        6. Choose **Connect**.

    ![Marketo connection form with fields for client ID, secret, account ID, and connection name.](images/connection_setup-marketo-console.png)

9.  You will be redirected to the Marketo login page. When prompted, grant Amazon AppFlow
    permissions to access your Marketo account.

Now that you are connected to your Marketo account, you can continue with the flow creation
steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in
[Requirements](#marketo-requirements "#marketo-requirements").

## Notes

- When you use Marketo as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per hour.
- Depending on your instance, Marketo might queue requests for data extraction. This can
  result in longer flow run times. If you want to avoid queueing, contact your Marketo
  administrator for assistance. We recommend that you avoid running concurrent flows using
  Marketo if your use case does not benefit from it.
- Depending on your Marketo instance, you can submit more than one bulk import request (with
  limitations). Each request is added as a job to be processed in a First-In-First-Out (FIFO)
  queue. A maximum of two jobs are processed at the same time. A maximum of ten jobs are allowed
  in the queue at any given time, including the two currently being processed. If you exceed the
  ten job maximum, a **`1016: Too many imports`** error is returned. If you want
  to avoid queueing, contact your Marketo administrator for assistance.
- There is a soft quota of 1 GB per flow when extracting data from Marketo. If you need to
  process more records in a single flow, you can submit a request to Amazon AppFlow through the
  Amazon AppFlow support channel. For more information, see [Creating a support
  case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _AWS Support User Guide_.

## Supported destinations

When you create a flow that uses Marketo as the data source, you can set the destination to any of the following connectors:

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

- [Credentials for API Access](https://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API#CreateaCustomServiceforUsewithReSTAPI-CredentialsforAPIAccess "https://docs.marketo.com/display/public/DOCS/Create+a+Custom+Service+for+Use+with+ReST+API#CreateaCustomServiceforUsewithReSTAPI-CredentialsforAPIAccess") in the Marketo documentation
- [API Limits with Marketo](https://developers.marketo.com/rest-api/marketo-integration-best-practices/ "https://developers.marketo.com/rest-api/marketo-integration-best-practices/") in the Marketo documentation
- [Error Codes with
  Marketo](https://developers.marketo.com/rest-api/error-codes/ "https://developers.marketo.com/rest-api/error-codes/") in the Marketo documentation
- Introduction to the Marketo Connector in Amazon AppFlow
