# Delete an Adapter

You can delete a custom Amazon Textract adapter at any time by calling the [DeleteAdapter](API_DeleteAdapter.md "API_DeleteAdapter.md") API operation.
You can delete an adapter by providing the DeleteAdapter operation with the
AdapterId of the adapter that you want to delete. Invoke DeleteAdapter will delete
all Adapter Versions associated with the Adapter ARN.

To delete an adapter with the console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- From the list of your adapters, select the adapter to delete.
- Select **Delete** and follow the instructions
  to delete your adapter.
  To create an adapter with the AWS CLI or AWS SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```
aws textract delete-adapter \
--adapter-id 'abcdef123456'

```
