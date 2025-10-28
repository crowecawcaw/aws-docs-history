# Create adapter version

To customize the Amazon Textract base model to fit your specific use cases, create an
adapter. After you create an adapter, you need to train the adapter. You can start
training an adapter by calling the [CreateAdapterVersion](API_CreateAdapterVersion.md "API_CreateAdapterVersion.md") operation. You provide the operation
with an AdapterId and use the DatasetConfig to specify an Amazon S3 bucket
containing the dataset you want to train the adapter on. The manifest file you
provide must follow a specific format. For more information, see [Preparing training and testing
datasets](textract-preparing-training-testing.md "textract-preparing-training-testing.md"). You can also provide the
operation with an optional KMSKeyId, optional ClientRequestToken, or any Tags to add
to the adapter version.

Running this operation requires the appropriate IAM permissions. For a sample
IAM policy, see [Permissions needed for
CreateAdapterVersion](security_iam_id-based-policy-examples.md#security_iam_create-adapter-version "security_iam_id-based-policy-examples.md#security_iam_create-adapter-version").

To create a new adapter version with the console:

- Sign in to the Amazon Textract console.
- Select **Custom Queries** from the left
  navigation panel.
- From the list of **Your adapters**, select
  the adapter.
- On the adapter details page, select **Modify the
  dataset**.
- Select the **Add documents** dropdown menu
  and add documents to the training dataset.
- On the following page, choose how to add your training documents (by S3
  bucket or directly from your computer).
- Choose **Add documents** to finish adding
  your documents to the dataset.
- Wait until the auto-labeling is complete.
- Review the annotations by clicking **Review
  Annotations**.
- Review each document, clicking “**Submit and
  next**”.
- After you review all annotations, choose **Train
  adapter** to start training the new adapter.
  The number of successful trainings that can be performed per
  month is limited per AWS account. Refer to [Set Quotas in Amazon Textract](limits-quotas-explained.md "limits-quotas-explained.md") for more information regarding limits.

To create an adapter version with the AWS CLI or AWS SDK:

- If you haven't already done so, install and configure the AWS CLI and
  the AWS SDKs. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md "setup-awscli-sdk.md").
- Use the following code to create a adapter:

CLI

```

aws textract create-adapter-version \
--adapter-id "012345678910" \
--dataset-config '{"ManifestS3Object": {"Bucket":"`amzn-s3-demo-source-bucket`","Name":"test/sample-manifest.jsonl"}}' \
--output-config '{"S3Bucket": "`amzn-s3-demo-destination-bucket`", "S3Prefix": "prefix-string"}'

```
