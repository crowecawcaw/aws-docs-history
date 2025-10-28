# Get adapter

You can retrieve configuration information for an adapter at any time by calling
the [GetAdapter](API_GetAdapter.md "API_GetAdapter.md") operation and
specifying an AdapterId. GetAdapter returns information on AdapterName, Description,
CreationTime, AutoUpdate status, and FeatureTypes.

To see details for your adapter with the console:

- Sign into the AWS console for Amazon Textract.
- Select **Custom Queries** from the navigation
  panel on the left.
- From the list of **Your adapters**, select
  the adapter you want to view the details for.
- Review the details for the adapter on your Adapter details page.
  To see details for your adapter with the CLI/SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```
aws textract get-adapter \
--adapter-id "abcdef123456"

```
