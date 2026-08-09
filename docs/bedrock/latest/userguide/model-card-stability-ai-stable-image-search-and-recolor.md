# Stable Image Search and Recolor

## Icon showing a purple letter S with a red dot in the lower right corner. Stability AI — Stable Image Search and Recolor

## Model Details

Stable Image Search and Recolor is Stability AI's model that identifies objects in images and changes their colors based on text prompts. For more information about model development and performance, see the [model/service card](https://stability.ai/stable-image "https://stability.ai/stable-image").

- **Model launch date:** Aug 19, 2024
- **Model EOL date:** N/A
- **End User License Agreements and Terms of Use:** [View](https://aws.amazon.com/legal/bedrock/third-party-models/ "https://aws.amazon.com/legal/bedrock/third-party-models/")
- **Model lifecycle:** Active

| **Input Modalities**                                                           | **Output Modalities**                                                             | **[APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md")**  | **[Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md")** |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Red circle with white X icon indicating error, cancel, or close action. Audio  | Red circle with white X icon indicating error, cancel, or close action. Embedding | Red circle with white X icon indicating error, cancel, or close action. `Responses`        | Green circle with white checkmark icon. `bedrock-runtime`                                                |
| Green circle with white checkmark icon. Image                                  | Green circle with white checkmark icon. Image                                     | Red circle with white X icon indicating error, cancel, or close action. `Chat Completions` | Red circle with white X icon indicating error, cancel, or close action. `bedrock-mantle`                 |
| Red circle with white X icon indicating error, cancel, or close action. Speech | Red circle with white X icon indicating error, cancel, or close action. Speech    | Green circle with white checkmark icon. `Invoke`                                           |                                                                                                          |
| Green circle with white checkmark icon. Text                                   | Red circle with white X icon indicating error, cancel, or close action. Text      | Red circle with white X icon indicating error, cancel, or close action. `Converse`         |                                                                                                          |
| Red circle with white X icon indicating error, cancel, or close action. Video  | Red circle with white X icon indicating error, cancel, or close action. Video     |                                                                                            |                                                                                                          |

## Capabilities and Features

**Bedrock Features**

**Features supported using `bedrock-runtime` endpoint**

| **Supported**                                                                                                                                                                                                                                                                                     | **Not Supported**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| • Green circle with white checkmark icon. [Abuse detection](bedrock/latest/userguide/abuse-detection.md "bedrock/latest/userguide/abuse-detection.md")<br>• Green circle with white checkmark icon. [Guardrails](bedrock/latest/userguide/guardrails.md "bedrock/latest/userguide/guardrails.md") | • Red circle with white X icon indicating error, cancel, or close action. [Intelligent prompt routing](bedrock/latest/userguide/prompt-routing.md "bedrock/latest/userguide/prompt-routing.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Response streaming](bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt optimization](bedrock/latest/userguide/prompt-management-optimize.md "bedrock/latest/userguide/prompt-management-optimize.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Count tokens](bedrock/latest/userguide/count-tokens.md "bedrock/latest/userguide/count-tokens.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Knowledge base](bedrock/latest/userguide/knowledge-base.md "bedrock/latest/userguide/knowledge-base.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Model evaluation](bedrock/latest/userguide/evaluation.md "bedrock/latest/userguide/evaluation.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Prompt management](bedrock/latest/userguide/prompt-management.md "bedrock/latest/userguide/prompt-management.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Flows](bedrock/latest/userguide/flows.md "bedrock/latest/userguide/flows.md")<br>• Red circle with white X icon indicating error, cancel, or close action. [Agents](bedrock/latest/userguide/agents.md "bedrock/latest/userguide/agents.md") |

## Pricing

For pricing information, see the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/") page.

## Programmatic Access

Use the following model IDs and endpoint URLs to access this model programmatically. For more information about the available APIs and endpoints, see [APIs supported](bedrock/latest/userguide/apis.md "bedrock/latest/userguide/apis.md") and [Endpoints supported](bedrock/latest/userguide/endpoints.md "bedrock/latest/userguide/endpoints.md").

| **Endpoint**      | **Model ID**                                 | **In-Region endpoint URL**                       | **Geo inference ID**                            | **Global inference ID** |
| ----------------- | -------------------------------------------- | ------------------------------------------------ | ----------------------------------------------- | ----------------------- |
| `bedrock-runtime` | `stability.stable-image-search-recolor-v1:0` | `https://bedrock-runtime.{region}.amazonaws.com` | `us.stability.stable-image-search-recolor-v1:0` | Not supported           |

_For example, if region is us-east-1 (N. Virginia), then the bedrock-runtime endpoint URL will be "https://bedrock-runtime.us-east-1.amazonaws.com" and for bedrock-mantle will be "https://bedrock-mantle.us-east-1.api.aws/v1"._

## Service Tiers

Amazon Bedrock offers multiple service tiers to match your workload requirements. **Standard** provides pay-per-token access with no commitment. **Priority** offers higher throughput with a time-based commitment. **Flex** provides lower-cost access for flexible, non-time-sensitive workloads. **Reserved** provides dedicated throughput with a term commitment for predictable workloads. For more information, see [service tiers](bedrock/latest/userguide/service-tiers-inference.md "bedrock/latest/userguide/service-tiers-inference.md").

| **Standard**                            | **Priority**                                                            | **Flex**                                                                | **Reserved**                                                            |
| --------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. | Red circle with white X icon indicating error, cancel, or close action. |

## Regional Availability

**Regional availability at a glance**

Amazon Bedrock offers three inference options: **In-Region** keeps requests within a single Region for strict compliance, **Geo Cross-Region** routes across Regions within a geography (such as US, EU, and APAC) while respecting data residency, and **Global Cross-Region** routes anywhere worldwide when there are no residency constraints. Refer to the [Regional availability by models](models-region-compatibility.md "models-region-compatibility.md") page for more details.

| **Region**                | **In-Region**                                                           | **Geo**                                 | **Global**                                                              |
| ------------------------- | ----------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| `us-east-1` (N. Virginia) | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-east-2` (Ohio)        | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |
| `us-west-2` (Oregon)      | Red circle with white X icon indicating error, cancel, or close action. | Green circle with white checkmark icon. | Red circle with white X icon indicating error, cancel, or close action. |

**Geo inference details**

**Geo: US**

Geo Inference ID: `us.stability.stable-image-search-recolor-v1:0`

| **Source Region**       | **Destination Regions**                                       |
| ----------------------- | ------------------------------------------------------------- |
| us-east-1 (N. Virginia) | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-east-2 (Ohio)        | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |
| us-west-2 (Oregon)      | us-east-1 (N. Virginia), us-east-2 (Ohio), us-west-2 (Oregon) |

## Quotas and Limits

Your AWS account has default quotas to maintain the performance of the service and to ensure appropriate usage of Amazon Bedrock. The default quotas assigned to an account might be updated depending on regional factors, payment history, fraudulent usage, and/or approval of a quota [increase request](bedrock/latest/userguide/quotas-increase.md "bedrock/latest/userguide/quotas-increase.md"). For more information, see [Quotas for Amazon Bedrock](quotas.md "quotas.md") documentation and see the [limits](general/latest/gr/bedrock.md#limits_bedrock "general/latest/gr/bedrock.md#limits_bedrock") for the model.

## Sample Code

**Step 1 - AWS Account:** If you have an AWS account already, skip this step. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").

**Step 2 - API key:** Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create "https://console.aws.amazon.com/bedrock/home#/api-keys/long-term/create") and generate a long-term API key.

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

```
pip install boto3
```

**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"
```

**Step 5 - Run your first inference request:** Save the file as `bedrock-first-request.py`

Invoke API

```
import json
import base64
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
with open('input.png', 'rb') as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')
params = {'image': image_base64, 'prompt': 'pink jacket', 'select_prompt': 'jacket'}
response = client.invoke_model(
    modelId='stability.stable-image-search-recolor-v1:0',
    body=json.dumps(params)
)
response_body = json.loads(response['body'].read())
print(f'Image generated: {len(response_body["images"][0])} bytes (base64)')
```
