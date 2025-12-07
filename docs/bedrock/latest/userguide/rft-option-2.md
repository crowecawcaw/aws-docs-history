# Option 2: Use invocation logs for data preparation

When you create a reinforcement fine-tuning job, you can have Amazon Bedrock use existing invocation logs from your S3 bucket as training data. For
Amazon Bedrock, an invocation log is a detailed record of model invocations.

To use invocation logs for reinforcement fine-tuning, set the model invocation logging on, use one of the model invocation operations, and make
sure that you've set up an Amazon S3 bucket as the destination for the logs. For more information about setting up the invocation logs, see
[Monitor model invocation using CloudWatch Logs and Amazon S3](model-invocation-logging.md "model-invocation-logging.md").

Before you can start the reinforcement fine-tuning job with invocation logs from an S3 bucket as input, you must provide Amazon Bedrock permissions to access the
logs from an S3 Bucket. For more information, see [Invocation log access](rft-access-security.md#rft-api-log-permissions "rft-access-security.md#rft-api-log-permissions").

You can optionally add request metadata to the prompt-response pairs in the invocation log using one of the model invocation operations and
then later use it to filter the logs. Amazon Bedrock can use the filtered logs to fine-tune the model.

## Add request metadata to prompts and responses in your invocation logs for reinforcement fine-tuning

With invocation logs, you can identify the training dataset prompts that you want Amazon Bedrock to use for reinforcement fine-tuning using
request metadata attached to invocation logs.

The following is an example of an invocation log from an `InvokeModel` call with the `requestMetadata`:

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

You can specify the invocation log as your input data source when you start a reinforcement fine-tuning job. You can start a reinforcement fine-tuning job through the Amazon Bedrock
console, using the API, AWS CLI, or SDK.

### Requirements for providing request metadata

The request metadata must meet the following requirements:

- Provided in the JSON `key:value` format.
- Key and value pair must be a string of 256 characters maximum.
- Provide a maximum of 16 key-value pairs.

### Using request metadata filters

Once invocation logs with request metadata are available, you can apply filters based on the request metadata to selectively
choose which prompts to include for fine-tuning the model. For example, you might want to include only those with
`"project": "CustomerService"` and `"priority": "High"` request metadata.

To filter the logs using multiple request metadata, use a single Boolean operator `AND` or `OR`.
You cannot combine these operators. For single request metadata filtering, use the `Equals` or `Not Equals` operator.
