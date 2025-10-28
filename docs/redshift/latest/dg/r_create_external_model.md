Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE EXTERNAL MODEL

###### Topics

- [Prerequisites for CREATE EXTERNAL
  MODEL](#r_create_external_model_prereqs "#r_create_external_model_prereqs")
- [Required privileges](#r_simple_create_model-privileges "#r_simple_create_model-privileges")
- [Cost control](#r_create_model_cost "#r_create_model_cost")
- [CREATE EXTERNAL MODEL syntax](#r_create_external_model_syntax "#r_create_external_model_syntax")
- [CREATE EXTERNAL MODEL
  parameters and settings](#r_create_external_model_parameters_settings "#r_create_external_model_parameters_settings")
- [CREATE EXTERNAL MODEL inference
  function parameters](#r_create_external_model_if_parameters "#r_create_external_model_if_parameters")

## Prerequisites for CREATE EXTERNAL

MODEL

Before you use the CREATE EXTERNAL MODEL statement, complete the prerequisites in
[Cluster setup for using Amazon Redshift ML](getting-started-machine-learning.md#cluster-setup "getting-started-machine-learning.md#cluster-setup"). The following is a
high-level summary of the prerequisites.

- Create an Amazon Redshift cluster with the AWS Management Console or the AWS
  Command Line Interface (AWS CLI).
- Attach the AWS Identity and Access Management (IAM) policy while creating the
  cluster.
- To allow Amazon Redshift and Amazon Bedrock to assume the role to interact with other services,
  add the appropriate trust policy to the IAM role.
- Enable access to the specific LLMs that you want to use from the Amazon Bedrock
  console.
- (Optional) If you encounter throttling exceptions coming from Amazon Bedrock such as
  `Too many requests, please wait before trying again`, even with
  small amounts of data, check the quotas under **Service Quotas**
  in your Amazon Bedrock account. Check that the applied account-level quota is at least the
  same as the AWS default quota value for the **InvokeModel**
  requests for the model you are using.

For details for the IAM role, trust policy, and other prerequisites, see [Cluster setup for using Amazon Redshift ML](getting-started-machine-learning.md#cluster-setup "getting-started-machine-learning.md#cluster-setup").

## Required privileges

Following are required privileges for CREATE EXTERNAL MODEL:

- Superuser
- Users with the CREATE MODEL privilege
- Roles with the GRANT CREATE MODEL privilege

## Cost control

Amazon Redshift ML uses existing cluster resources to create prediction models, so you
don’t have to pay additional costs. However, AWS charges for using Amazon Bedrock based on the
model you select. For more information, see [Costs for using Amazon Redshift ML](cost.md "cost.md").

## CREATE EXTERNAL MODEL syntax

The following is the full syntax of the CREATE EXTERNAL MODEL statement.

```
CREATE EXTERNAL MODEL model_name
FUNCTION function_name
IAM_ROLE {default/'arn:aws:iam::<account-id>:role/<role-name>'}
MODEL_TYPE BEDROCK
SETTINGS (
   MODEL_ID model_id
   [, PROMPT 'prompt prefix']
   [, SUFFIX 'prompt suffix']
   [, REQUEST_TYPE {RAW|UNIFIED}]
   [, RESPONSE_TYPE {VARCHAR|SUPER}]
);
```

The `CREATE EXTERNAL MODEL` command creates an inference function that you
use to generate content.

The following is the syntax of an inference function that `CREATE EXTERNAL
 MODEL` creates using a `REQUEST_TYPE` of `RAW`:

```
SELECT inference_function_name(request_super)
[FROM *table*];
```

The following is the syntax of an inference function that `CREATE EXTERNAL
 MODEL` creates using a `REQUEST_TYPE` of `UNIFIED`:

```
SELECT inference_function_name(input_text, [, inference_config [, additional_model_request_fields]])
[FROM *table*];
```

For information about how to use the inference function, see [Using an external model for Amazon Redshift ML integration with Amazon Bedrock](machine-learning-br.md#machine-learning-br-use "machine-learning-br.md#machine-learning-br-use").

## CREATE EXTERNAL MODEL

parameters and settings

This section describes the parameters and settings for the `CREATE EXTERNAL
 MODEL` command.

###### Topics

- [CREATE EXTERNAL MODEL
  parameters](#r_create_external_model_parameters "#r_create_external_model_parameters")
- [CREATE EXTERNAL MODEL
  settings](#r_create_external_model_settings "#r_create_external_model_settings")

### CREATE EXTERNAL MODEL

parameters

model_name

The name for the external model. The model name in a schema must be
unique.

FUNCTION _function_name (data_type [,...] )_

The name for the inference function that `CREATE EXTERNAL
 MODEL` creates. You use the inference function to send requests to
Amazon Bedrock and retrieve ML-generated text.

IAM_ROLE _{ default |
'arn:aws:iam::<account-id>:role/<role-name>' }_

The IAM role that Amazon Redshift uses to access Amazon Bedrock. For information about the
IAM role, see [Creating or updating an IAM role for Amazon Redshift ML integration with Amazon Bedrock](machine-learning-br.md#machine-learning-br-iam "machine-learning-br.md#machine-learning-br-iam").

MODEL_TYPE BEDROCK

Specifies the model type. The only valid value is
`BEDROCK`.

SETTINGS ( MODEL_ID model_id [,...] )

Specifies the external model settings. See the section following for
details.

### CREATE EXTERNAL MODEL

settings

MODEL_ID model_id

The identifier for the external model, for example,
`anthropic.claude-v2`. For information about Amazon Bedrock model IDs,
see [Amazon Bedrock model
IDs](../../../bedrock/latest/userguide/model-ids.md "../../../bedrock/latest/userguide/model-ids.md").

PROMPT 'prompt prefix'

Specifies a static prompt that Amazon Redshift adds to the beginning of every
inference request. Only supported with a `REQUEST_TYPE` of
`UNIFIED`.

SUFFIX 'prompt suffix'

Specifies a static prompt that Amazon Redshift adds to the end of every inference
request. Only supported with a `REQUEST_TYPE` of
`UNIFIED`.

REQUEST_TYPE { RAW | UNIFIED }

Specifies the format of the request sent to Amazon Bedrock. Valid values include
the following:

- **RAW**: The inference function takes
  the input as a single super value, and always returns a super value.
  The format of the super value is specific to to the Amazon Bedrock model
  selected. A super is a prediction model that combines multiple
  algorithms to produce a single, improved prediction.
- **UNIFIED**: The inference function
  uses the unified API. All models have a unified and consistent
  interface with Amazon Bedrock. This works for all models that support messages.
  This value is the default.

For more information, see the [Converse API documentation](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md") in the _Amazon Bedrock API
documentation_.

RESPONSE_TYPE { VARCHAR | SUPER }

Specifies the format of the response. If the `REQUEST_TYPE` is
`RAW`, the `RESPONSE_TYPE` is requred and the only
valid value is `SUPER`. For all other `REQUEST TYPE`
values, the default value is `VARCHAR`, and
`RESPONSE_TYPE` is optional. Valid values include the
following:

- **VARCHAR**: Amazon Redshift only returns the
  text response generated by the model.
- **SUPER**: Amazon Redshift returns the whole
  response JSON generated by the model as a super. This includes the
  text response, and information such as the stop reason, and the model
  input and output token usage. A super is a prediction model that
  combines multiple algorithms to produce a single, improved prediction.

## CREATE EXTERNAL MODEL inference

function parameters

This section describes valid parameters for the inference function that the
`CREATE EXTERNAL MODEL` command creates.

### CREATE EXTERNAL MODEL

inference function parameters for `REQUEST_TYPE` of
`RAW`

An inference function created with a `REQUEST_TYPE` of `RAW`
has one super input argument and always returns a super data type. The syntax of the
input super follows the syntax of the request of the specific model selected from
Amazon Bedrock.

### CREATE EXTERNAL MODEL

inference function parameters for `REQUEST_TYPE` of
`UNIFIED`

input_text

The text that Amazon Redshift sends to Amazon Bedrock.

inference_config

A super value that contains optional parameters that Amazon Redshift sends to Amazon Bedrock.
These can include the following:

- maxTokens
- stopSequences
- temperature
- topP

These parameters are all optional and are all case-sensitive. For
information about these parameters, see [InferenceConfiguration](../../../bedrock/latest/APIReference/API_runtime_InferenceConfiguration.md "../../../bedrock/latest/APIReference/API_runtime_InferenceConfiguration.md") in the _Amazon Bedrock API
Reference_.
