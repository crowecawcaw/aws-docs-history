# List adapters

You can list all of the adapters associated with your account by using the [ListAdapters](API_ListAdapters.md "API_ListAdapters.md") operation. You can
filter the list of returned adapters by the date and time of creation by using the
AfterCreationTime and BeforeCreationTime arguments. You can also set a number of
maximum results to return using MaxResults.

To see a list of your adapters with the console:

- Sign into the AWS console for Amazon Textract.
- Select **Custom Queries** from the navigation
  panel on the left.
- View your adapters in the list of your adapters.
  To create an adapter with the CLI/SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```
aws textract list-adapters
```
