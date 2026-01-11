# Core inference

Inference is the process of sending a request to a Amazon Nova model and receiving a generated
response. Amazon Nova models support inferencing through two API options:

- **Converse API** ([Converse](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md"), [ConverseStream](../../../bedrock/latest/APIReference/API_runtime_ConverseStream.md "../../../bedrock/latest/APIReference/API_runtime_ConverseStream.md")): Provides a consistent interface across different
  models, making it easier to switch between models or build applications that work
  with multiple models. Recommended for most use cases.
- **Invoke API** ([InvokeModel](../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md "../../../bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.md")): Request payloads are structured
  specifically for each model's native format. Runs inference using the prompt and
  inference parameters provided in the request body.
  Both APIs support the same core features including:

- Multi-turn conversations
- Multimodal inputs (text, images, video, audio)
- Tool use
- Guardrails
- Streaming responses
  The request structure is nearly identical between the two APIs, differing only in how byte data (documents, images, video and audio) is encoded.For model request parameters unique to Amazon Nova models, such as
  `reasoningConfig` and `TopK`, these are placed within an
  additional `inferenceConfig` object within the
  `additionalModelRequestFields`. These are top-level parameters for
  `InvokeModel` and `InvokeModelWithResponseStream`.

###### Note

Review Code Samples and Troubleshooting for a list of code samples with Nova 2 models.

Set the `modelId` to one of the following to use Amazon Nova models:

| Model                      | Model ID                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| Nova 2 Lite                | • global.amazon.nova-2-lite-v1:0<br>• us.amazon.nova-2-lite-v1:0   |
| Nova 2 Sonic               | • global.amazon.nova-2-sonic-v1:0<br>• us.amazon.nova-2-sonic-v1:0 |
| Nova Multimodal Embeddings | amazon.nova-2-multimodal-embeddings-v1:0                           |

## Important: Timeout Configuration

###### Important

Amazon Nova inference requests can take up to 60 minutes to complete. Configure your client
timeout settings accordingly:

The following example is Python code. Users can check the documentation for their preferred SDK language version in that SDK's API docs.

```
from botocore.config import Config

bedrock = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    config=Config(
        read_timeout=3600  # 60 minutes
    )
)
```

## Core Inference Topics

This section discusses the following topics:

- Using the converse API: A consistent interface offering compatibility across most Bedrock models
- Using the invoke API: An interface unique to Nova models and not portable to other Bedrock models
- Streaming responses: Real-time response generation
- Using Amazon Nova embeddings: Text embeddings capabilities
- On-demand inference: Pay-per-use inference model
