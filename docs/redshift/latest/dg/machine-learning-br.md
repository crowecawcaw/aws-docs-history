Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift ML integration with Amazon Bedrock

This section describes how to use Amazon Redshift ML integration with Amazon Bedrock. With this feature, you can
invoke an Amazon Bedrock model using SQL, and you can use your data from a Amazon Redshift data warehouse to build generative AI
applications such as text generation, sentiment analysis, or translation.

###### Topics

- [Creating or updating an IAM role for Amazon Redshift ML integration with Amazon Bedrock](#machine-learning-br-iam "#machine-learning-br-iam")
- [Creating an external model for Amazon Redshift ML integration with Amazon Bedrock](#machine-learning-br-create "#machine-learning-br-create")
- [Using an external model for Amazon Redshift ML integration with Amazon Bedrock](#machine-learning-br-use "#machine-learning-br-use")
- [Prompt engineering for Amazon Redshift ML integration with Amazon Bedrock](#machine-learning-br-prompt "#machine-learning-br-prompt")

## Creating or updating an IAM role for Amazon Redshift ML integration with Amazon Bedrock

This section demonstrates how to create an IAM role to use with Amazon Redshift ML integration with Amazon Bedrock.

Add the following policy to the IAM role you use with Amazon Redshift ML integration with Amazon Bedrock:

- `AmazonBedrockFullAccess`

To allow Amazon Redshift to assume a role to interact with other services, add the following trust policy to the IAM role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "redshift.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

If the cluster or namespace is in a VPC, follow the instructions in [Cluster and configure setup for Amazon Redshift ML
administration](getting-started-machine-learning.md#admin-setup "getting-started-machine-learning.md#admin-setup").

If you need a more restrictive policy, you can create one that includes only the Amazon Bedrock
permissions specified in the following pages:

- [Cluster and configure setup for Amazon Redshift ML
  administration](getting-started-machine-learning.md#admin-setup "getting-started-machine-learning.md#admin-setup")
- [Permissions required to use Amazon Redshift machine learning (ML)](../mgmt/redshift-iam-access-control-identity-based.md#iam-permission-ml? "../mgmt/redshift-iam-access-control-identity-based.md#iam-permission-ml?")

For information about creating an IAM role, see
[IAM Role Creation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md")
in the _AWS Identity and Access Management User Guide_.

## Creating an external model for Amazon Redshift ML integration with Amazon Bedrock

This section shows how to create an external model to use as an interface for Amazon Bedrock within your Amazon Redshift data warehouse.

To invoke an Amazon Bedrock model from Amazon Redshift, you must first run the `CREATE EXTERNAL MODEL` command. This command creates an
external model object in the database, and an associated user function that you use to generate text content
with Amazon Bedrock.

The following code example shows a basic `CREATE EXTERNAL MODEL` command:

```
CREATE EXTERNAL MODEL llm_claude
FUNCTION llm_claude_func
IAM_ROLE '`<IAM role arn>`'
MODEL_TYPE BEDROCK
SETTINGS (
   MODEL_ID 'anthropic.claude-v2:1',
   PROMPT 'Summarize the following text:');
```

The `CREATE EXTERNAL MODEL` command has a unified and consistent interface with Amazon Bedrock
for all Foundation Models (FM) that support messages. This is the default option when using the
`CREATE EXTERNAL MODEL` command or when explicitly specifying the request type to be
`UNIFIED`. For more information, see the
[Converse API documentation](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md")
in the _Amazon Bedrock API documentation_.

If an FM doesn't support messages, then you must set the `request_type`
setting to `RAW`, as the following example demonstrates. When you set
`request_type` to `RAW`, you must construct the request sent to
Amazon Bedrock when using the inference function based on the selected FM. Make sure that you
enable access to the Titan Text G1 – Express model in Amazon Bedrock before running the following
example.

```
CREATE EXTERNAL MODEL titan_raw
FUNCTION func_titan_raw
IAM_ROLE '`<IAM role arn>`'
MODEL_TYPE BEDROCK
SETTINGS (
   MODEL_ID 'amazon.titan-text-express-v1',
   REQUEST_TYPE RAW,
   RESPONSE_TYPE SUPER);
```

If you need more information about an input request such as total tokens,
you can request the `RESPONSE_TYPE` to be `super` when you create the model.

```
CREATE EXTERNAL MODEL patient_recommendations_v2
FUNCTION patient_recommendations_func_v2
IAM_ROLE '`<IAM role arn>`'
MODEL_TYPE BEDROCK
SETTINGS (
   MODEL_ID 'anthropic.claude-v2',
   PROMPT 'Generate personalized diet plan for following patient:',
   RESPONSE_TYPE SUPER);
```

The `PROMPT` parameter for the `CREATE EXTERNAL MODEL` command
is a static prompt. If you need a dynamic prompt for your application, you must specify
it when using the inference function. For more details, see [Prompt engineering for Amazon Redshift ML integration with Amazon Bedrock](#machine-learning-br-prompt "#machine-learning-br-prompt").

For more information about the `CREATE EXTERNAL MODEL` statement and its parameters and settings,
see [CREATE EXTERNAL MODEL](r_create_external_model.md "r_create_external_model.md").

## Using an external model for Amazon Redshift ML integration with Amazon Bedrock

This section shows how to invoke an external model to generate text in response to provided prompts. To
invoke an external model, use the inference function that you create with `CREATE EXTERNAL MODEL`.

###### Topics

- [Inference with UNIFIED request type models](#machine-learning-br-use-unified "#machine-learning-br-use-unified")
- [Inference with RAW request type models](#machine-learning-br-use-raw "#machine-learning-br-use-raw")
- [Inference functions as leader-only functions](#machine-learning-br-use-leader "#machine-learning-br-use-leader")
- [Inference function usage notes](#machine-learning-br-use-usage "#machine-learning-br-use-usage")

### Inference with `UNIFIED` request type models

The inference function for models with request type `UNIFIED` has the following three parameters
that are passed to the function in order:

- **Input text** (required): This parameter specifies the input
  text that Amazon Redshift passes to Amazon Bedrock.
- **Inference configuration** and
  **Additional model request fields** (optional): Amazon Redshift passes these parameters
  to the corresponding parameters for the Converse model API.

The following code example shows how to use a `UNIFIED` type inference function:

```
SELECT llm_claude_func(input_text, object('temperature', 0.7, 'maxtokens', 500))
   FROM some_data;

```

### Inference with `RAW` request type models

The inference function for models with request type `RAW` has only one parameter of data type
`SUPER`. The syntax of this parameter depends on the Amazon Bedrock model used.

The following code example shows how to use a `RAW` type inference function:

```
SELECT llm_titan_func(
    object(
        "inputText", "Summarize the following text: " | input_text,
        "textGenerationConfig", object("temperature", 0.5, "maxTokenCount", 500)
    )
)
FROM some_data;

```

### Inference functions as leader-only functions

Inference functions for Amazon Bedrock models can run as leader node-only functions when the query
that uses them doesn't reference any tables. This can be helpful if you want to quickly ask
an LLM a question.

The following code example shows how to use a leader-only inference function:

```
SELECT general_titan_llm_func('Summarize the benefits of LLM on data analytics in 100 words');

```

### Inference function usage notes

Note the following when using inference functions with Amazon Redshift ML integration with Amazon Bedrock:

- The names of the parameters for all Amazon Bedrock models are case sensitive.
  If your parameters do not match the ones required by the model, Amazon Bedrock might quietly ignore them.
- The throughput of inference queries is limited by the runtime quotas of the different models offered
  by Amazon Bedrock in different regions. For more information, see
  [Quotas for Amazon Bedrock](../../../bedrock/latest/userguide/quotas.md "../../../bedrock/latest/userguide/quotas.md") in the
  _Amazon Bedrock User Guide_.
- If you need guaranteed and consistent throughput, consider getting provisioned
  throughput for the model you need from Amazon Bedrock. For more information, see
  [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](../../../bedrock/latest/userguide/prov-throughput.md "../../../bedrock/latest/userguide/prov-throughput.md") in the
  _Amazon Bedrock User Guide_.
- Inference queries with large amounts of data might
  get throttling exceptions. This is because of the limited runtime quotas for Amazon Bedrock.
  Amazon Redshift retries requests multiple times, but queries can still get throttled because
  throughput for non-provisioned models might be variable.
- If you encounter throttling exceptions coming from Amazon Bedrock such as `Too many requests, 
please wait before trying again.` even with small amounts of data, check the quotas under
  **Service Quotas** in your Amazon Bedrock account. Check that the applied account-level
  quota is at least the same as the AWS default quota value for the **InvokeModel** requests
  for the model you are using.

## Prompt engineering for Amazon Redshift ML integration with Amazon Bedrock

This section shows how to use static prompts with an external model.

To use static prefix and suffix prompts for your external model, provide them using the `PROMPT`
and `SUFFIX` parameters of the `CREATE EXTERNAL MODEL` statement. These prompts
are added to every query using the external model.

The following example shows how to add prefix and suffix prompts to an external model:

```
CREATE EXTERNAL MODEL llm_claude
FUNCTION llm_claude_func
IAM_ROLE '`<IAM role arn>`'
MODEL_TYPE BEDROCK
SETTINGS (
   MODEL_ID 'anthropic.claude-v2:1',
   `PROMPT 'Summarize the following text:',
 SUFFIX 'Respond in an analytic tone')`;
```

To use dynamic prompts, you can provide them when using the inference function by
concatenating them in the function input. The following example shows how to use dynamic
prompts with an inference function:

```
SELECT llm_claude_func('Summarize the following review:' | input_text | 'The review should have formal tone.')
FROM some_data
```
