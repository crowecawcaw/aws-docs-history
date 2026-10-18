

# Supported Regions and models for Amazon Bedrock Guardrails
<a name="guardrails-supported"></a>

Amazon Bedrock Guardrails applies to foundation models that you invoke on the `bedrock-runtime` endpoint through the `InvokeModel`, `InvokeModelWithResponseStream`, `Converse`, and `ConverseStream` operations. Within those requests, a guardrail can evaluate both text and image content — for image content, see [Block harmful images with content filters](guardrails-mmfilter.md). The `bedrock-mantle` endpoint doesn't support Amazon Bedrock Guardrails.

Most models in the Amazon Bedrock catalog support guardrails. The following models don't.


| **Provider** | **Model** | **Model ID** | **Model type** | 
| --- | --- | --- | --- | 
| Amazon | Titan Embeddings G1 - Text | `amazon.titan-embed-text-v1` | Text embeddings | 
| Amazon | Titan Text Embeddings V2 | `amazon.titan-embed-text-v2:0` | Text embeddings | 
| Amazon | Titan Multimodal Embeddings G1 | `amazon.titan-embed-image-v1` | Multimodal embeddings | 
| Amazon | Amazon Nova Multimodal Embeddings | `amazon.nova-2-multimodal-embeddings-v1:0` | Multimodal embeddings | 
| Amazon | Rerank 1.0 | `amazon.rerank-v1:0` | Reranking | 
| Amazon | Nova 2 Sonic | `amazon.nova-2-sonic-v1:0` | Speech | 
| Amazon | Nova 2.5 Sonic | `amazon.nova-2-5-sonic` | Speech | 
| Cohere | Embed English | `cohere.embed-english-v3` | Text embeddings | 
| Cohere | Embed Multilingual | `cohere.embed-multilingual-v3` | Text embeddings | 
| Cohere | Embed v4 | `cohere.embed-v4:0` | Multimodal embeddings | 
| Cohere | Rerank 3.5 | `cohere.rerank-v3-5:0` | Reranking | 
| Luma AI | Ray2 | `luma.ray-v2:0` | Video generation | 
| OpenAI | GPT 5.4 | `openai.gpt-5.4` | Text | 
| OpenAI | GPT 5.5 | `openai.gpt-5.5` | Text | 
| TwelveLabs | Marengo Embed v2.7 | `twelvelabs.marengo-embed-2-7-v1:0` | Multimodal embeddings | 
| TwelveLabs | Marengo Embed 3.0 | `twelvelabs.marengo-embed-3-0-v1:0` | Multimodal embeddings | 
| TwelveLabs | Pegasus v1.5 | `twelvelabs.pegasus-1-5-v1:0` | Video understanding | 

Point-version model IDs follow their base model. For example, `amazon.titan-embed-text-v2:0:8k` doesn't support guardrails because `amazon.titan-embed-text-v2:0` doesn't.

A request that references a guardrail with one of these models fails with the following error, even though the same request succeeds when you omit the guardrail parameters:

```
ValidationException: Guardrail is not supported with the chosen model
```

**Note**  
Don't infer guardrail support from the model type. Models of the same type can differ — TwelveLabs Pegasus v1.2 supports guardrails while Pegasus v1.5 doesn't — and the Stability AI image generation models do support guardrails.

To evaluate content without invoking a model, use the `ApplyGuardrail` operation. It applies a guardrail to content that you supply directly, so it isn't tied to any model and works regardless of which models your application uses.

To confirm support for a specific model, go to [models at a glance](model-cards.md), choose the model, and check the *Capabilities and Features* section of its model card.