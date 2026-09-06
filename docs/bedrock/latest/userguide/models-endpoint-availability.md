# Endpoint availability

Amazon Bedrock supports two endpoints: bedrock-runtime and bedrock-mantle. For new applications, we recommend the `bedrock-runtime` endpoint. Please refer to the [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") to learn more about how to choose between the two endpoints.

| **Endpoint**                                           | **Supported APIs**                                                                                                                                                                                                                                                                                                                                                                                                                          | **Description**                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bedrock-runtime.{region}.amazonaws.com` (recommended) | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") / [Responses API](bedrock-mantle.md#bedrock-mantle-responses "bedrock-mantle.md#bedrock-mantle-responses") / [Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md") | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the InvokeModel/Converse/Chat Completions/Responses/Messages APIs. For more information, see [Amazon Bedrock Runtime API operations](bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.md "bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.md"). |
| `bedrock-mantle.{region}.api.aws`                      | [Responses API](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions API](bedrock-mantle.md "bedrock-mantle.md") / [Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md")                                                                                                                                                                                                      | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the OpenAI-compatible endpoints and the Anthropic Messages API.                                                                                                                                                                                                                    |

The following tables show which Amazon Bedrock endpoints support each model, organized by provider.

## AI21 Labs

| Model name                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Jamba 1.5 Large](model-card-ai21-labs-jamba-1-5-large.md "model-card-ai21-labs-jamba-1-5-large.md")** | supported         | not-supported    |
| **[Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md")**    | supported         | not-supported    |

## Amazon

| Model name                                                                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md")** | supported         | not-supported    |
| **[Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md")**                                                                   | supported         | not-supported    |
| **[Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md")**                                                                | supported         | not-supported    |
| **[Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md")**                                                                   | supported         | not-supported    |
| **[Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md")**                                                                         | supported         | not-supported    |
| **[Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md")**                                                                      | supported         | not-supported    |
| **[Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md")**                                                                | supported         | not-supported    |
| **[Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md")**                                                                            | supported         | not-supported    |
| **[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md")**                                                                         | supported         | not-supported    |
| **[Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md")**                                                                      | supported         | not-supported    |
| **[Titan Embeddings G1<br>• Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md")**                   | supported         | not-supported    |
| **[Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md")**                   | supported         | not-supported    |
| **[Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md")**          | supported         | not-supported    |
| **[Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md")**                            | supported         | not-supported    |
| **[Titan Embeddings G1<br>• Text v2](model-card-amazon-titan-text-embeddings-v2-2.md "model-card-amazon-titan-text-embeddings-v2-2.md")**                | supported         | not-supported    |

## Anthropic

| Model name                                                                                                                 | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Claude Fable 5.1](model-card-anthropic-claude-fable-5-1.md "model-card-anthropic-claude-fable-5-1.md")**                | supported         | supported        |
| **[Claude Mythos 5.1](model-card-anthropic-claude-mythos-5-1.md "model-card-anthropic-claude-mythos-5-1.md")**             | supported         | not-supported    |
| **[Claude Opus 5](model-card-anthropic-claude-opus-5.md "model-card-anthropic-claude-opus-5.md")**                         | supported         | supported        |
| **[Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md "model-card-anthropic-claude-sonnet-5.md")**                   | supported         | supported        |
| **[Claude Mythos 5](model-card-anthropic-claude-mythos-5.md "model-card-anthropic-claude-mythos-5.md")**                   | not-supported     | supported        |
| **[Claude Fable 5](model-card-anthropic-claude-fable-5.md "model-card-anthropic-claude-fable-5.md")**                      | supported         | supported        |
| **[Claude Mythos Preview](model-card-anthropic-claude-mythos-preview.md "model-card-anthropic-claude-mythos-preview.md")** | not-supported     | supported        |
| **[Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md")**                      | supported         | not-supported    |
| **[Claude 3.5 Haiku](model-card-anthropic-claude-3-5-haiku.md "model-card-anthropic-claude-3-5-haiku.md")**                | supported         | not-supported    |
| **[Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md")**                | supported         | supported        |
| **[Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md")**                   | supported         | not-supported    |
| **[Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md")**                   | supported         | not-supported    |
| **[Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md")**                   | supported         | not-supported    |
| **[Claude Opus 4.7](model-card-anthropic-claude-opus-4-7.md "model-card-anthropic-claude-opus-4-7.md")**                   | supported         | supported        |
| **[Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md "model-card-anthropic-claude-opus-4-8.md")**                   | supported         | supported        |
| **[Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md")**                   | supported         | not-supported    |
| **[Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md")**             | supported         | not-supported    |
| **[Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md")**             | supported         | not-supported    |

## Cohere

| Model name                                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md")**                            | supported         | not-supported    |
| **[Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md")**                 | supported         | not-supported    |
| **[Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md")**                | supported         | not-supported    |
| **[Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md")** | supported         | not-supported    |
| **[Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md")**                               | supported         | not-supported    |
| **[Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md")**                         | supported         | not-supported    |

## DeepSeek

| Model name                                                                                       | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------ | ----------------- | ---------------- |
| **[DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md")** | supported         | supported        |
| **[DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md")**       | supported         | not-supported    |
| **[DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md")** | supported         | supported        |

## Google

| Model name                                                                                         | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Gemma 4 31B](model-card-google-gemma-4-31b.md "model-card-google-gemma-4-31b.md")**             | not-supported     | supported        |
| **[Gemma 4 26B-A4B](model-card-google-gemma-4-26b-a4b.md "model-card-google-gemma-4-26b-a4b.md")** | not-supported     | supported        |
| **[Gemma 4 E2B](model-card-google-gemma-4-e2b.md "model-card-google-gemma-4-e2b.md")**             | not-supported     | supported        |
| **[Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md")**    | supported         | supported        |
| **[Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md")**    | supported         | supported        |
| **[Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md")**       | supported         | supported        |

## Meta

| Model name                                                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md")**                            | supported         | not-supported    |
| **[Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md")**                               | supported         | not-supported    |
| **[Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md")**                   | supported         | not-supported    |
| **[Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md")**                      | supported         | not-supported    |
| **[Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md")**                         | supported         | not-supported    |
| **[Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md")**                      | supported         | not-supported    |
| **[Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md")**                         | supported         | not-supported    |
| **[Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md")**                         | supported         | not-supported    |
| **[Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md")**                      | supported         | not-supported    |
| **[Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md")**                      | supported         | not-supported    |
| **[Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md")** | supported         | not-supported    |
| **[Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md")**          | supported         | not-supported    |

## MiniMax

| Model name                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md")**       | supported         | supported        |
| **[MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md")** | supported         | supported        |
| **[MiniMax M2.5](model-card-minimax-minimax-m2-5.md "model-card-minimax-minimax-m2-5.md")** | supported         | supported        |

## Mistral AI

| Model name                                                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md")**                      | supported         | supported        |
| **[Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md")**       | supported         | supported        |
| **[Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md")**                | supported         | supported        |
| **[Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md")**                         | supported         | supported        |
| **[Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md")**                               | supported         | supported        |
| **[Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md")**          | supported         | not-supported    |
| **[Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md")**                            | supported         | not-supported    |
| **[Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md")**                      | supported         | supported        |
| **[Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md")**                            | supported         | not-supported    |
| **[Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md")**    | supported         | not-supported    |
| **[Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md")**                            | supported         | not-supported    |
| **[Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md")**       | supported         | supported        |
| **[Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md")** | supported         | supported        |

## Moonshot AI

| Model name                                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| --------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Kimi K2 Thinking](model-card-moonshot-ai-kimi-k2-thinking.md "model-card-moonshot-ai-kimi-k2-thinking.md")** | supported         | supported        |
| **[Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md")**                      | supported         | supported        |

## NVIDIA

| Model name                                                                                                                                                     | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md")**                            | supported         | supported        |
| **[NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md")** | supported         | supported        |
| **[Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md")**                                                 | supported         | supported        |
| **[NVIDIA Nemotron 3 Super 120B](model-card-nvidia-nemotron-super-3-120b.md "model-card-nvidia-nemotron-super-3-120b.md")**                                    | supported         | supported        |

## OpenAI

| Model name                                                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[GPT-5.6 Sol](model-card-openai-gpt-56-sol.md "model-card-openai-gpt-56-sol.md")**                                            | supported         | supported        |
| **[Daybreak Red: GPT-5.6 Cyber](model-card-openai-gpt-56-cyber.md "model-card-openai-gpt-56-cyber.md")**                        | not-supported     | supported        |
| **[Daybreak Blue: GPT-5.6 Sol](model-card-openai-gpt-daybreak-blue-56-sol.md "model-card-openai-gpt-daybreak-blue-56-sol.md")** | not-supported     | supported        |
| **[GPT-5.6 Terra](model-card-openai-gpt-56-terra.md "model-card-openai-gpt-56-terra.md")**                                      | supported         | supported        |
| **[GPT-5.6 Luna](model-card-openai-gpt-56-luna.md "model-card-openai-gpt-56-luna.md")**                                         | supported         | supported        |
| **[GPT-5.5](model-card-openai-gpt-55.md "model-card-openai-gpt-55.md")**                                                        | not-supported     | supported        |
| **[GPT-5.4](model-card-openai-gpt-54.md "model-card-openai-gpt-54.md")**                                                        | not-supported     | supported        |
| **[GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md")**         | supported         | supported        |
| **[GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md")**            | supported         | supported        |
| **[gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md")**                                       | supported         | supported        |
| **[gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md")**                                          | supported         | supported        |

## Qwen

| Model name                                                                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md")**                               | supported         | supported        |
| **[Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md")**                                                                | supported         | supported        |
| **[Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md")** | supported         | supported        |
| **[Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md")**                                           | supported         | supported        |
| **[Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md")**                                     | supported         | supported        |
| **[Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md")**                                     | supported         | supported        |
| **[Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md")**       | supported         | supported        |

## Stability AI

| Model name                                                                                                                                                           | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md")** | supported         | not-supported    |
| **[Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md")**                   | supported         | not-supported    |
| **[Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md")**          | supported         | not-supported    |
| **[Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md")**             | supported         | not-supported    |
| **[Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md")**                         | supported         | not-supported    |
| **[Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md")**                         | supported         | not-supported    |
| **[Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md")**                                        | supported         | not-supported    |
| **[Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md")**                                     | supported         | not-supported    |
| **[Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md")**          | supported         | not-supported    |
| **[Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md")**       | supported         | not-supported    |
| **[Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md")**       | supported         | not-supported    |
| **[Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md")**                            | supported         | not-supported    |
| **[Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md")**                   | supported         | not-supported    |

## TwelveLabs

| Model name                                                                                                          | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md")**    | supported         | not-supported    |
| **[Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md")** | supported         | not-supported    |
| **[Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md")**                   | supported         | not-supported    |

## Writer

| Model name                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Palmyra Vision 7B](model-card-writer-palmyra-vision-7b.md "model-card-writer-palmyra-vision-7b.md")** | supported         | supported        |
| **[Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md")**                      | supported         | not-supported    |
| **[Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md")**                      | supported         | not-supported    |

## xAI

| Model name                                                              | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Grok 4.3](model-card-xai-grok-4-3.md "model-card-xai-grok-4-3.md")** | not-supported     | supported        |
| **[Grok 4.6](model-card-xai-grok-4-6.md "model-card-xai-grok-4-6.md")** | supported         | supported        |

## Z.AI

| Model name                                                                             | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md")**                   | supported         | supported        |
| **[GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md")** | supported         | supported        |
| **[GLM 5](model-card-zai-glm-5.md "model-card-zai-glm-5.md")**                         | supported         | supported        |
