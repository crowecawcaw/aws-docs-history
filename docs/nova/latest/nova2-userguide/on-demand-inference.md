# On-demand inference

On-demand inference provides serverless access to Amazon Nova models without requiring
provisioned capacity. This mode automatically scales to handle your workload and charges
based on usage.

## Benefits

On-demand inference offers several advantages:

- **No capacity planning:** Automatically
  scales to meet demand
- **Pay per use:** Charged only for tokens
  processed
- **Instant availability:** No provisioning or
  warm-up time required
- **Cost effective:** Ideal for variable or
  unpredictable workloads

## Using on-demand inference

On-demand inference is the default mode for Amazon Nova models. Simply specify the
model ID when making API calls:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Hello, Nova!'}]
        }
    ]
)

# Print the response text
content_list = response["output"]["message"]["content"]
text = next((item["text"] for item in content_list if "text" in item), None)
if text is not None:
    print(text)
```

## Pricing

On-demand inference is billed based on the number of input and output tokens
processed. For current pricing details, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").

## Quotas and limits

On-demand inference has default quotas that vary by model and region. To request
quota increases, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
