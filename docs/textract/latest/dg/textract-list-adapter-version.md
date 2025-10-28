# List adapter versions

An Amazon Textract adapter can have a number of different versions associated with it.
In order to see which adapter versions associated with a given adapter, you can call
the [ListAdapterVersions](API_ListAdapterVersions.md "API_ListAdapterVersions.md") operation. The operation will return all versions of an adapter unless provided
with filtering criteria using of the optional arguments such as AdapterId,
AfterCreationTime, BeforeCreationTIme, Statuses, or MaxResults.

To see a list of your adapter versions with the console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- From the list of your adapters, select the adapter.
- View the adapter versions in the **Adapter versions**
  box.
  To create an adapter with the AWS CLI or AWS SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```

aws textract list-adapter-versions
```
