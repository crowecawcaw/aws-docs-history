# Create an Adapter

To customize the Amazon Textract base model, create an adapter. To do so, use the [CreateAdapter](API_CreateAdapter.md "API_CreateAdapter.md") operation. When
calling `CreateAdapter,` you provide an AdapterName and FeatureType as an
input. Currently Queries is the only feature type supported.

When creating an adapter you can also provide a Description, Tags, and a
ClientRequestToken. Finally, you can choose whether the adapter should be
auto-updated with the AutoUpdate argument. After creating an adapter, you can start
training it on your own sample documents by using the [CreateAdapterVersion](API_CreateAdapterVersion.md "API_CreateAdapterVersion.md")
operation.

To create an adapter with the Amazon Textract console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- Select **Create adapter**.
  To create an adapter with the AWS CLI or AWS SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create an adapter:

CLI

```

aws textract create-adapter \
--adapter-name "test-w2" \
--feature-types '["QUERIES"]' \
--description 'demo'

```
