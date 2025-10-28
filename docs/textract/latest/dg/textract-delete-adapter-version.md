# Delete adapter version

You can delete an adapter version you’re no longer using by calling [DeleteAdapterVersion](API_DeleteAdapterVersion.md "API_DeleteAdapterVersion.md").
To delete an adapter version you provide the DeleteAdapterVersion operation with
both the adapter’s AdapterId and the specific AdapterVersion that you want to
delete. Note that you cannot delete adapter versions with an "IN_PROGRESS"
status.

To delete an adapter version with the console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- From the list of your adapters, select the adapter.
- Select **Delete** and follow the
  instructions.
- Select the adapter version that you want to delete from the list of
  versions in the **Adapter** versions
  box.
- Select **Delete** and follow the instructions
  to delete your adapter.
  To delete an adapter with the AWS CLI or AWS SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```

aws textract delete-adapter-version \
--adapter-id "abcdef123456" \
--adapter-version "1"

```
