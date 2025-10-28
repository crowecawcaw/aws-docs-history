# Salesforce Pardot

The following are the requirements and connection instructions for using Pardot with
Amazon AppFlow.

###### Note

You can use Pardot as a source only.

###### Topics

- [Requirements](#pardot-requirements "#pardot-requirements")
- [Setup instructions](#pardot-setup "#pardot-setup")
- [Notes](#pardot-notes "#pardot-notes")
- [Supported destinations](#salesforce-pardot-destinations "#salesforce-pardot-destinations")
- [Related resources](#pardot-resources "#pardot-resources")

## Requirements

- Your Salesforce account must be enabled for API access. API access is enabled by default
  for Enterprise, Unlimited, Developer, and Performance editions.
- Your Salesforce account must allow you to install connected apps. If this option is
  disabled, contact your Salesforce administrator.
- After you create a Pardot connection in Amazon AppFlow, verify that the connected app named
  _Amazon AppFlow Pardot Embedded Login App_ is installed in your
  Salesforce account. For instructions on how to create a connected app in Salesforce, see [Requirements for using
  your own connected app](salesforce.md#salesforce-global-connected-app-instructions "salesforce.md#salesforce-global-connected-app-instructions"). For more information about
  connected apps in Salesforce, see [Connected
  Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm "https://help.salesforce.com/articleView?id=connected_app_overview.htm") in the Salesforce documentation.
- The refresh token policy for the **Amazon AppFlow Pardot Embedded Login
  App** must be set to **Refresh token is valid until
  revoked**. Otherwise, your flows will fail when your refresh token expires.
- If your Pardot app enforces IP address restrictions, you must grant access to the
  addresses used by Amazon AppFlow. For more information, see [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the
  _Amazon Web Services General Reference_.

###### Pardot version support

Amazon AppFlow supports Pardot version 4 only. If you are still using version 3, you must
upgrade to version 4 to use Amazon AppFlow. For more information, see [Transitioning from version 3 to version 4](https://developer.pardot.com/kb/api-version-4/#transitioning-from-version-3-to-version-4 "https://developer.pardot.com/kb/api-version-4/#transitioning-from-version-3-to-version-4") in the Pardot documentation.

###### Authentication and Pardot business ID

- Amazon AppFlow supports authentication via OAuth2 with Pardot. For more information, see
  [Authentication Via Salesforce OAuth](https://developer.pardot.com/kb/authentication/#via-salesforce-oauth "https://developer.pardot.com/kb/authentication/#via-salesforce-oauth") in the Pardot documentation.
- You must have the Pardot Business Unit ID that you are trying to authenticate with. To
  find the Pardot Business Unit ID in Salesforce, go to **Setup** and enter
  `Pardot Account Setup` in the **Quick Find** box. Your
  Pardot Business Unit ID begins with _0Uv_ and is 18 characters
  long. If you cannot access the Pardot account setup information, ask your Salesforce
  administrator to provide you with the Pardot Business Unit ID.

## Setup instructions

###### To connect to Pardot while creating a flow

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. Choose **Create flow**.
3. For **Flow details**, enter a name and description for the flow.
4. (Optional) To use a customer managed CMK instead of the default AWS managed CMK, choose
   **Data encryption**, **Customize encryption settings** and
   then choose an existing CMK or create a new one.
5. (Optional) To add a tag, choose **Tags**, **Add tag**
   and then enter the key name and value.
6. Choose **Next**.
7. Choose **Pardot** from the **Source name** dropdown
   list.
8. Choose **Connect** to open the **Connect to Pardot**
   dialog box. If you are connecting to Pardot for the first time, follow the instructions to
   complete the OAuth workflow and create a connection profile.
9. You will be redirected to the Pardot login page. When prompted, grant Amazon AppFlow
   permissions to access your Pardot account.

Now that you are connected to your Pardot account, you can continue with the flow creation
steps as described in [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

###### Tip

If you aren’t connected successfully, ensure that you have followed the instructions in the
[Requirements](#pardot-requirements "#pardot-requirements") section.

## Notes

- When you use Pardot as a source, you can run schedule-triggered flows at a maximum
  frequency of one flow run per minute.
- You can connect Amazon AppFlow to your Pardot [sandbox
  account](https://pi.demo.pardot.com/ "https://pi.demo.pardot.com/") in addition to your Pardot [production
  account](http://pi.pardot.com/ "http://pi.pardot.com/").

- Amazon AppFlow inherits quotas from Pardot. Quotas are enforced on daily requests and
  concurrent requests at the customer level._Pardot Pro_
  customers are allocated 25,000 API requests a day._Pardot
  Ultimate_ customers can make up to 100,000 API requests a day. These limits reset at
  the beginning of the day based on your account time zone settings. Any request that exceeds
  these quotas results in an [error code
  122](http://developer.pardot.com/kb/error-codes-messages/#error-code-122 "http://developer.pardot.com/kb/error-codes-messages/#error-code-122"). Amazon AppFlow handles these error codes transparently.

## Supported destinations

When you create a flow that uses Salesforce Pardot as the data source, you can set the destination to any of the following connectors:

- Amazon Connect
- Amazon EventBridge
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

- [Transitioning from version 3 to version 4](https://developer.pardot.com/kb/api-version-4/#transitioning-from-version-3-to-version-4 "https://developer.pardot.com/kb/api-version-4/#transitioning-from-version-3-to-version-4") in the Pardot documentation
- [Connected Apps](https://help.salesforce.com/articleView?id=connected_app_overview.htm "https://help.salesforce.com/articleView?id=connected_app_overview.htm") in the Salesforce documentation
- [Authentication Via Salesforce OAuth](https://developer.pardot.com/kb/authentication/#via-salesforce-oauth "https://developer.pardot.com/kb/authentication/#via-salesforce-oauth") in the Pardot documentation
