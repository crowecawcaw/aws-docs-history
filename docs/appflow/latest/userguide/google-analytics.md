# Google Analytics

The following are the requirements and connection instructions for using Google Analytics
with Amazon AppFlow.

###### Notes

- The Google Analytics connector transfers data only from Universal Analytics
  properties. If you want to transfer data from Google Analytics 4 properties instead, use
  the [Google Analytics 4
  connector](connectors-google-analytics-4.md "connectors-google-analytics-4.md").

In time, Google Analytics will end support for Universal Analytics properties, and
that platform will fully support only Google Analytics 4 properties. For more information,
see [Introducing
the next generation of Analytics, Google Analytics 4 (GA4)](https://support.google.com/analytics/answer/10089681?hl=en "https://support.google.com/analytics/answer/10089681?hl=en").

- You can use Google Analytics as a source only.

## Requirements

You must log in to the Google API Console at [https://console.developers.google.com](https://console.developers.google.com "https://console.developers.google.com") and do
the following:

- Activate the Analytics API.
- Create a new app named **AppFlow**. Set the user type as
  **Internal**. Add the scope for read-only access and add
  `amazon.com` as an authorized domain.
- Create a new OAuth 2.0 client. Set the application type as **Web
  application**.
- Set the authorized JavaScript origins URL to `https://console.aws.amazon.com`.
- Set the authorized redirect URL to
  `https://`region`.console.aws.amazon.com/appflow/oauth`.
  For example, if you use Amazon AppFlow in the US East (N. Virginia) Region, set the URL to
  `https://us-east-1.console.aws.amazon.com/appflow/oauth`.
- Provide Amazon AppFlow with your client ID and client secret. After you provide them, you are
  redirected to the Google login page. When prompted, grant Amazon AppFlow permissions to access
  your Google Analytics account. Note that your Google Analytics user account must also be a
  Google Workspaces user account.

For more information, see [Management
API - Authorization](https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization "https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization") in the Google Analytics documentation.

## Connection instructions

###### To connect to Google Analytics while creating a flow

1.  Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2.  Choose **Create flow**.
3.  For **Flow details**, enter a name and description for the flow.
4.  (Optional) To use a customer managed key in the AWS Key Management Service (AWS KMS) instead of the default
    AWS managed KMS key, choose **Data encryption**, **Customize
    encryption settings** and then choose an existing KMS key or create a new
    one.
5.  (Optional) To add a tag, choose **Tags**, **Add tag**
    and then enter the key name and value.
6.  Choose **Next**.
7.  Choose **Google Analytics** from the **Source name**
    dropdown list.
8.  Choose **Connect** to open the **Connect to Google
    Analytics** dialog box.

        1. Under **Client ID**, enter your client ID.
        2. Under **Client secret**, enter your client secret.
        3. Under **Secret access key**, enter your secret access key.
        4. Under **Data encryption**, enter your AWS KMS key.
        5. Under **Connection name**, specify a name for your connection.
        6. Choose **Continue**.

    ![Google Analytics connection form with fields for client ID, secret, data encryption, and connection name.](images/connection_setup-googleanalytics-console.png)

9.  You will be redirected to the Google Analytics login page. When prompted, grant Amazon AppFlow
    permissions to access your Google Analytics account.

Now that you are connected to your Google Analytics account, you can continue with the flow
creation steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#googleanalytics-requirements "#googleanalytics-requirements")
section.

## Notes

- When you use Google Analytics as a source, you can run schedule-triggered flows at a
  maximum frequency of one flow run per day.
- Google Analytics can process 9 dimension and 10 metrics (including custom ones) as part of
  a single flow run.
- If you choose Google Analytics, you can only specify JSON as the data format for the Amazon S3
  destination file.
- You can import custom dimensions and metrics from Google Analytics into Amazon S3. To specify
  custom dimensions or metrics, choose the **upload a .csv file with mapped
  field** option in the **Map data fields** step of the flow
  configuration. In the source field name in the CSV file, specify the custom dimension or the
  metric as `ga:dimension`XX`` or
`ga:metric`XX``, with `XX`
  containing the actual index (numerical value) that you provided to Google Analytics.

The following is an example row in the CSV file:

`ga:dimension24|DIMENSION, PriceDimension`

This imports the custom dimension in Google Analytics to a field named
`PriceDimension` in the destination Amazon S3 file.

###### Note

The option to specify custom dimensions and metrics is available only when you upload a
CSV file with mapped fields, and not when you manually map fields using the console.

## Supported destinations

When you create a flow that uses Google Analytics as the data source, you can set the destination to any of the following connectors:

- Lookout for Metrics
- Amazon S3
- Upsolver

You can also set the destination to any custom connectors that you
create with the Amazon AppFlow Custom Connector SDKs for [Python](https://github.com/awslabs/aws-appflow-custom-connector-python "https://github.com/awslabs/aws-appflow-custom-connector-python") or [Java](https://github.com/awslabs/aws-appflow-custom-connector-java "https://github.com/awslabs/aws-appflow-custom-connector-java") . You can download these SDKs from GitHub.

## Related resources

- [Management API - Authorization](https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization "https://developers.google.com/analytics/devguides/config/mgmt/v3/authorization") in the Google Analytics documentation
- [Create a
  Property](https://support.google.com/analytics/answer/10269537#property "https://support.google.com/analytics/answer/10269537#property") in the Google Analytics documentation
- [Analyzing Google Analytics data with Amazon AppFlow and Athena](https://aws.amazon.com/blogs/big-data/analyzing-google-analytics-data-with-amazon-appflow-and-amazon-athena "https://aws.amazon.com/blogs/big-data/analyzing-google-analytics-data-with-amazon-appflow-and-amazon-athena") in the _AWS Big
  Data Blog_
- How to transfer data from Google Analytics to Amazon S3 using
  Amazon AppFlow
