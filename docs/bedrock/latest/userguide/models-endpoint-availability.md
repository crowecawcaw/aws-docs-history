# Endpoint availability

Amazon Bedrock supports two endpoints: bedrock-runtime and bedrock-mantle. Please refer to the [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") to learn more about how to choose between the two endpoints.

| **Endpoint**                             | **Supported APIs**                                                                                                                                                                                               | **Description**                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-mantle.{region}.api.aws`        | [Responses API](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions API](bedrock-mantle.md "bedrock-mantle.md")                                                                                           | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the OpenAI-compatible endpoints.                                                                                                                                                                                      |
| `bedrock-runtime.{region}.amazonaws.com` | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the InvokeModel/Converse/Chat Completions APIs. Read more on Amazon Bedrock Runtime APIs [here](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md"). |

The following tables show which Amazon Bedrock endpoints support each model, organized by provider.

## AI21 Labs

| Model name                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Jamba 1.5 Large](model-card-ai21-labs-jamba-1-5-large.md "model-card-ai21-labs-jamba-1-5-large.md")** | Yes               | No               |
| **[Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md")**    | Yes               | No               |

## Amazon

| Model name                                                                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md")** | Yes               | No               |
| **[Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md")**                                                                   | Yes               | No               |
| **[Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md")**                                                                | Yes               | No               |
| **[Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md")**                                                                   | Yes               | No               |
| **[Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md")**                                                                         | Yes               | No               |
| **[Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md")**                                                                      | Yes               | No               |
| **[Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md")**                                                                | Yes               | No               |
| **[Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md")**                                                                            | Yes               | No               |
| **[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md")**                                                                         | Yes               | No               |
| **[Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md")**                                                                      | Yes               | No               |
| **[Titan Embeddings G1<br>• Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md")**                   | Yes               | No               |
| **[Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md")**                   | Yes               | No               |
| **[Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md")**          | Yes               | No               |
| **[Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md")**                            | Yes               | No               |
| **[Titan Text Embeddings v2](model-card-amazon-titan-text-embeddings-v2-2.md "model-card-amazon-titan-text-embeddings-v2-2.md")**                        | Yes               | No               |
| **[Titan Text Large](model-card-amazon-titan-text-large.md "model-card-amazon-titan-text-large.md")**                                                    | Yes               | No               |

## Anthropic

| Model name                                                                                                     | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md")**          | Yes               | No               |
| **[Claude 3.5 Haiku](model-card-anthropic-claude-3-5-haiku.md "model-card-anthropic-claude-3-5-haiku.md")**    | Yes               | No               |
| **[Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md")**    | Yes               | No               |
| **[Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md")**       | Yes               | No               |
| **[Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md")**       | Yes               | No               |
| **[Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md")**       | Yes               | No               |
| **[Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md")**       | Yes               | No               |
| **[Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md")** | Yes               | No               |
| **[Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md")** | Yes               | No               |

## Cohere

| Model name                                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md")**                            | Yes               | No               |
| **[Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md")**                 | Yes               | No               |
| **[Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md")**                | Yes               | No               |
| **[Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md")** | Yes               | No               |
| **[Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md")**                               | Yes               | No               |
| **[Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md")**                         | Yes               | No               |

## DeepSeek

| Model name                                                                                       | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------ | ----------------- | ---------------- |
| **[DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md")** | Yes               | Yes              |
| **[DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md")**       | Yes               | No               |
| **[DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md")** | Yes               | Yes              |

## Google

| Model name                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md")** | Yes               | Yes              |
| **[Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md")** | Yes               | Yes              |
| **[Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md")**    | Yes               | Yes              |

## Meta

| Model name                                                                                                                               | `bedrock-runtime` | `bedrock-mantle` |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md")**                            | Yes               | No               |
| **[Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md")**                               | Yes               | No               |
| **[Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md")**                   | Yes               | No               |
| **[Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md")**                      | Yes               | No               |
| **[Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md")**                         | Yes               | No               |
| **[Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md")**                      | Yes               | No               |
| **[Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md")**                         | Yes               | No               |
| **[Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md")**                         | Yes               | No               |
| **[Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md")**                      | Yes               | No               |
| **[Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md")**                      | Yes               | No               |
| **[Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md")** | Yes               | No               |
| **[Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md")**          | Yes               | No               |

## MiniMax

| Model name                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md")**       | Yes               | Yes              |
| **[MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md")** | Yes               | Yes              |

## Mistral AI

| Model name                                                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md")**                      | Yes               | Yes              |
| **[Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md")**       | Yes               | Yes              |
| **[Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md")**                | Yes               | Yes              |
| **[Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md")**                         | Yes               | Yes              |
| **[Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md")**                               | Yes               | Yes              |
| **[Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md")**          | Yes               | No               |
| **[Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md")**                            | Yes               | No               |
| **[Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md")**                      | Yes               | Yes              |
| **[Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md")**                            | Yes               | No               |
| **[Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md")**    | Yes               | No               |
| **[Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md")**                            | Yes               | No               |
| **[Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md")**       | Yes               | Yes              |
| **[Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md")** | Yes               | Yes              |

## Moonshot AI

| Model name                                                                                                      | `bedrock-runtime` | `bedrock-mantle` |
| --------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Kimi K2 Thinking](model-card-moonshot-ai-kimi-k2-thinking.md "model-card-moonshot-ai-kimi-k2-thinking.md")** | Yes               | Yes              |
| **[Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md")**                      | Yes               | Yes              |

## NVIDIA

| Model name                                                                                                                                                     | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md")** | Yes               | Yes              |
| **[NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md")**                            | Yes               | Yes              |
| **[Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md")**                                                 | Yes               | Yes              |

## OpenAI

| Model name                                                                                                              | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md")** | Yes               | Yes              |
| **[GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md")**    | Yes               | Yes              |
| **[gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md")**                               | Yes               | Yes              |
| **[gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md")**                                  | Yes               | Yes              |

## Qwen

| Model name                                                                                                                                  | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md")**                               | Yes               | Yes              |
| **[Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md")**                                                                | Yes               | Yes              |
| **[Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md")** | Yes               | Yes              |
| **[Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md")**                                           | Yes               | Yes              |
| **[Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md")**                                     | Yes               | Yes              |
| **[Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md")**                                     | Yes               | Yes              |
| **[Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md")**       | Yes               | Yes              |

## Stability AI

| Model name                                                                                                                                                           | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md")** | Yes               | No               |
| **[Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md")**                   | Yes               | No               |
| **[Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md")**          | Yes               | No               |
| **[Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md")**             | Yes               | No               |
| **[Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md")**                         | Yes               | No               |
| **[Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md")**                         | Yes               | No               |
| **[Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md")**                                        | Yes               | No               |
| **[Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md")**                                     | Yes               | No               |
| **[Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md")**          | Yes               | No               |
| **[Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md")**       | Yes               | No               |
| **[Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md")**       | Yes               | No               |
| **[Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md")**                            | Yes               | No               |
| **[Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md")**                   | Yes               | No               |

## TwelveLabs

| Model name                                                                                                          | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md")**    | Yes               | No               |
| **[Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md")** | Yes               | No               |
| **[Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md")**                   | Yes               | No               |

## Writer

| Model name                                                                          | `bedrock-runtime` | `bedrock-mantle` |
| ----------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md")** | Yes               | No               |
| **[Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md")** | Yes               | No               |

## Z.AI

| Model name                                                                             | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **[GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md")**                   | Yes               | Yes              |
| **[GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md")** | Yes               | Yes              |
