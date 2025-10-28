# Option 2: Use invocation logs for data preparation

When you create a distillation job, you can have Amazon Bedrock use
existing teacher responses from CloudWatch Logs invocation logs as training data.
For Amazon Bedrock, an invocation log is a detailed record of model invocations.

To use invocation logs for model distillation, set the model invocation
logging on, use one of the model invocation operations, and make sure that
you've set up an Amazon S3 bucket as the destination for the logs. Before you can
start the model distillation job, you must provide Amazon Bedrock permissions to
access the logs. For more information about setting up the invocation logs,
see [Monitor
model invocation using Amazon CloudWatch Logs](model-invocation-logging.md "model-invocation-logging.md").

With this option, you can specify if you want Amazon Bedrock to use only the
prompts, or to use prompt-response pairs from the invocation log. If you
want Amazon Bedrock to use only prompts, then Amazon Bedrock might add proprietary data
synthesis techniques to generate diverse and higher-quality responses from
the teacher model. If you want Amazon Bedrock to use prompt-response pairs, then Amazon Bedrock
won't re-generate responses from the teacher model. Amazon Bedrock will directly use
the responses from the invocation log to fine-tune the student model.

###### Important

You can provide a maximum of 15K prompts or prompt-response pairs to
Amazon Bedrock for fine-tuning the student model. To ensure that the student model
is fine-tuned to meet your specific requirements, we highly recommend
the following:

- If you want Amazon Bedrock to use prompts only, make sure that there are
  at least 100 prompt-response pairs generated from across all
  models.
- If you want Amazon Bedrock to use responses from your invocation logs,
  make sure that you have at least 100 prompt-response pairs
  generated from the model in your invocation logs that exactly
  match with the teacher model you've chosen.
  You can optionally [add request
  metadata](#add-metadata-to-prompts "#add-metadata-to-prompts") to the prompt-response pairs in the invocation log using
  one of the model invocation operations and then later use it to filter the
  logs. Amazon Bedrock can use the filtered logs to fine-tune the student model.

To filter the logs using multiple request metadata, use a single operation
Boolean operator AND, OR, or NOT. You cannot combine operations. For single
request metadata filtering, use the Boolean operator NOT.

## Add request metadata to prompts and responses in your

invocation logs for model distillation

The model invocation logging collects invocation logs, model input data (prompts), and model
output data(responses) for all invocations used in Amazon Bedrock. If you've enabled logging, you
can collect the logs whenever you interact with Amazon Bedrock foundation models through any
`Invoke` or `Converse` API operations. If you want Amazon Bedrock to use
the prompts and associated responses from the invocation log to fine-tune the student
model, then you must give Amazon Bedrock access to these logs. Using the responses that a model
has already generated makes it quicker to fine-tune the student model. Using responses from the invocation
logs also makes model distillation more cost-effective, however, Amazon Bedrock's proprietary data synthesis
techniques are not added which may result in a more performant distilled model.

With invocation logs, you can identify the prompt-response pairs that you want Amazon Bedrock to
use for model distillation. These prompt-response pairs can be for specific use cases.
To be able to identify the prompt-response pairs to use for distillation, you must add a
request metadata string to the prompt-response pairs when you invoke a model or use the
`Converse` API operation. The request metadata is provided in the format:
`"`priority`" :
 "`High`"`.

As you continue to interact with the model using the `Invoke` or
`Converse` API operations, the interactions and the request metadata are
logged in the invocation logs. The following is an example of an invocation log from an
`InvokeModel` call that shows the request metadata:

```
{
    "schemaType": "ModelInvocationLog",
    "schemaVersion": "1.0",
    "timestamp": "2024-09-11T17:16:18Z",
    "accountId": "XXXXX",
    "identity": {
        "arn": "arn:aws:sts::XXXXXXX:assumed-role/Admin/XXXXXX"
    },
    "region": "us-east-1",
    "requestId": "7ee514f3-9eff-467c-af75-8fd564ce58e5",
    "operation": "InvokeModel",
    "modelId": "meta.llama3-1-405b-instruct-v1:0",
    "input": {
        "inputContentType": "application/json",
        "inputBodyJson": {
            "prompt": "story of two dogs",
            "max_tokens_to_sample": 300
        },
        "inputTokenCount": 13
    },
    "output": {
        "outputContentType": "application/json",
        "outputBodyJson": {
            "type": "completion",
            "completion": " Here is a story about two dogs:\n\nRex and Charlie were best friends who lived next door to each other. Every morning, their owners would let them out into the backyard to play. Rex was a golden retriever with long, shaggy fur. He loved to run and chase sticks. Charlie was a corgi with short legs and a big smile. He was happy just sniffing the grass and rolling around. \n\nThe two dogs spent every day playing together. Rex would grab a stick and bring it over to Charlie, wagging his tail excitedly. Charlie would take the other end of the stick in his mouth and they'd have a friendly game of tug-of-war. After tiring themselves out, they'd flop down in the warm sunshine for a nap. \n\nAt lunchtime, their owners would call them in for food. Rex would gobble up his kibble hungrily while Charlie ate his at a more leisurely pace. After lunch, it was right back outside for more playtime. The afternoon sunbeams would light up their fur as they chased each other around the yard. \n\nWhen it started getting late, their owners called them in for the night. Rex and Charlie would head inside, tired but happy after another fun day of play. After slurping up fresh water from their bowls, they'd curl up on their beds, Rex's fluffy golden tail tucked over his nose and little",
            "stop_reason": "max_tokens",
            "stop": null
        },
        "outputTokenCount": 300
    },
    "requestMetadata": {
        "project": "CustomerService",
        "intent": "ComplaintResolution",
        "priority": "High"
    }
}

```

You can specify the invocation log as your input data source when you start a model
distillation job. You can start model distillation job in the Amazon Bedrock console, using the
API, AWS CLI, or AWS SDK.

**Requirements for providing request metadata**

The request metadata must meet the following requirements:

- Provided in the JSON `key:value` format.
- Key and value pair must be a string of 256 characters maximum.
- Provide a maximum of 16 key-value pairs.

### Using request metadata filters

You can apply filters to the request metadata to selectively choose which
prompt-response pairs to include in distillation for fine-tuning the student model.
For example, you might want to include only those with "project" :
"CustomerService" and "priority" : "High" request
metadata.

To filter the logs using multiple request metadata, use a single Boolean operator
AND, OR, or NOT. You cannot combine operations. For single request metadata
filtering, use the Boolean operator NOT.

You can specify the invocation log as your input data source and what filters to use
to select the prompt-response pairs when you start a model distillation job. You can
start model distillation job in the Amazon Bedrock console, using the API, AWS CLI, or AWS SDK.
For more information, see [Submit a model distillation job in
Amazon Bedrock](submit-model-distillation-job.md "submit-model-distillation-job.md").

## Validate your dataset

Before you run your distillation job, you can validate your input dataset using a [Python script](https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/model_distillation/dataset-validation/README.md "https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/model_distillation/dataset-validation/README.md").
