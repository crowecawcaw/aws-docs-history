# Get an Adapter version

You can retrieve configuration information and the current status of an adapter
version by calling the [GetAdapterVersion](API_GetAdapterVersion.md "API_GetAdapterVersion.md") operation. When calling
GetAdapterVersion, specify the AdapterId and the AdapterVersion. This returns
information about the specified adapter version so that you can check the current
operational status and configuration options.

To see details for your adapter using the console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- From the list of your adapters, select the adapter.
- Select the adapter version in the **Adapter versions**
  box.
  To see details for your adapter using the AWS CLI or AWS SDK

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```

aws textract get-adapter-version \
--adapter-id "abcdef123456" \
--adapter-version "1"

```
