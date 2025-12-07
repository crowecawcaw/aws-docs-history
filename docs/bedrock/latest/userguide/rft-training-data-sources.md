# Requirements for training data sources

Amazon Bedrock supports multiple data sources for reinforcement fine-tuning training. This section outlines the requirements for Bedrock API logs and new training datasets.

###### Note

We only support the OpenAI chat completion format.

## Using existing Bedrock API invocation logs

You can use customer-side stored Invoke/Converse API invocation logs from Amazon S3 for training.

**Requirements:**

- API logging must be enabled for your Amazon Bedrock usage
- Logs must be in a supported format (Amazon Bedrock Invoke/Converse API)
- A minimum of 100 prompt examples

## Uploading new training datasets

You can upload custom datasets in JSONL format or select existing datasets from Amazon S3.

**Requirements:**

- JSONL format with prompts in OpenAI chat completion format (one prompt per line)
- A minimum of 100 records in training dataset
- Amazon Bedrock automatically validates training dataset format
