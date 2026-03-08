# Endpoint availability

Amazon Bedrock supports two endpoints: bedrock-runtime and bedrock-mantle. Please refer to the [Endpoints supported by Amazon Bedrock](endpoints.md "endpoints.md") to learn more about how to choose between the two endpoints.

| **Endpoint**                             | **Supported APIs**                                                                                                                                                                                               | **Description**                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bedrock-mantle.{region}.api.aws`        | [Responses API](bedrock-mantle.md "bedrock-mantle.md") / [Chat Completions API](bedrock-mantle.md "bedrock-mantle.md")                                                                                           | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the OpenAI-compatible endpoints.                                                                                                                                                                                      |
| `bedrock-runtime.{region}.amazonaws.com` | [InvokeModel](inference-invoke.md "inference-invoke.md") / [Converse](conversation-inference.md "conversation-inference.md") / [Chat Completions](inference-chat-completions.md "inference-chat-completions.md") | Region-specific endpoints for making inference requests for models hosted in Amazon Bedrock using the InvokeModel/Converse/Chat Completions APIs. Read more on Amazon Bedrock Runtime APIs [here](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md"). |

The following tables show which Amazon Bedrock endpoints support each model, organized by provider.

## AI21 Labs

| Model name          | `bedrock-runtime` | `bedrock-mantle` |
| ------------------- | ----------------- | ---------------- |
| **Jamba 1.5 Large** | Yes               | No               |
| **Jamba 1.5 Mini**  | Yes               | No               |

## Amazon

| Model name                            | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------- | ----------------- | ---------------- |
| **Amazon Nova Multimodal Embeddings** | Yes               | No               |
| **Nova 2 Lite**                       | Yes               | No               |
| **Nova 2 Sonic**                      | Yes               | No               |
| **Nova Canvas**                       | Yes               | No               |
| **Nova Lite**                         | Yes               | No               |
| **Nova Micro**                        | Yes               | No               |
| **Nova Premier**                      | Yes               | No               |
| **Nova Pro**                          | Yes               | No               |
| **Nova Reel**                         | Yes               | No               |
| **Nova Sonic**                        | Yes               | No               |
| **Titan Embeddings G1<br>• Text**     | Yes               | No               |
| **Titan Image Generator G1 v2**       | Yes               | No               |
| **Titan Multimodal Embeddings G1**    | Yes               | No               |
| **Titan Text Embeddings V2**          | Yes               | No               |
| **Titan Text Embeddings v2**          | Yes               | No               |
| **Titan Text Large**                  | Yes               | No               |

## Anthropic

| Model name            | `bedrock-runtime` | `bedrock-mantle` |
| --------------------- | ----------------- | ---------------- |
| **Claude 3 Haiku**    | Yes               | No               |
| **Claude 3.5 Haiku**  | Yes               | No               |
| **Claude Haiku 4.5**  | Yes               | No               |
| **Claude Opus 4.1**   | Yes               | No               |
| **Claude Opus 4.5**   | Yes               | No               |
| **Claude Opus 4.6**   | Yes               | No               |
| **Claude Sonnet 4**   | Yes               | No               |
| **Claude Sonnet 4.5** | Yes               | No               |
| **Claude Sonnet 4.6** | Yes               | No               |

## Cohere

| Model name             | `bedrock-runtime` | `bedrock-mantle` |
| ---------------------- | ----------------- | ---------------- |
| **Command R**          | Yes               | No               |
| **Command R+**         | Yes               | No               |
| **Embed English**      | Yes               | No               |
| **Embed Multilingual** | Yes               | No               |
| **Embed v4**           | Yes               | No               |
| **Rerank 3.5**         | Yes               | No               |

## DeepSeek

| Model name        | `bedrock-runtime` | `bedrock-mantle` |
| ----------------- | ----------------- | ---------------- |
| **DeepSeek V3.2** | Yes               | Yes              |
| **DeepSeek-R1**   | Yes               | No               |
| **DeepSeek-V3.1** | Yes               | Yes              |

## Google

| Model name         | `bedrock-runtime` | `bedrock-mantle` |
| ------------------ | ----------------- | ---------------- |
| **Gemma 3 12B IT** | Yes               | Yes              |
| **Gemma 3 27B PT** | Yes               | Yes              |
| **Gemma 3 4B IT**  | Yes               | Yes              |

## Meta

| Model name                        | `bedrock-runtime` | `bedrock-mantle` |
| --------------------------------- | ----------------- | ---------------- |
| **Llama 3 70B Instruct**          | Yes               | No               |
| **Llama 3 8B Instruct**           | Yes               | No               |
| **Llama 3.1 405B Instruct**       | Yes               | No               |
| **Llama 3.1 70B Instruct**        | Yes               | No               |
| **Llama 3.1 8B Instruct**         | Yes               | No               |
| **Llama 3.2 11B Instruct**        | Yes               | No               |
| **Llama 3.2 1B Instruct**         | Yes               | No               |
| **Llama 3.2 3B Instruct**         | Yes               | No               |
| **Llama 3.2 90B Instruct**        | Yes               | No               |
| **Llama 3.3 70B Instruct**        | Yes               | No               |
| **Llama 4 Maverick 17B Instruct** | Yes               | No               |
| **Llama 4 Scout 17B Instruct**    | Yes               | No               |

## MiniMax

| Model name       | `bedrock-runtime` | `bedrock-mantle` |
| ---------------- | ----------------- | ---------------- |
| **MiniMax M2**   | Yes               | Yes              |
| **MiniMax M2.1** | Yes               | Yes              |

## Mistral AI

| Model name                 | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------- | ----------------- | ---------------- |
| **Devstral 2 123B**        | Yes               | Yes              |
| **Magistral Small 2509**   | Yes               | Yes              |
| **Ministral 14B 3.0**      | Yes               | Yes              |
| **Ministral 3 8B**         | Yes               | Yes              |
| **Ministral 3B**           | Yes               | Yes              |
| **Mistral 7B Instruct**    | Yes               | No               |
| **Mistral Large**          | Yes               | No               |
| **Mistral Large 3**        | Yes               | Yes              |
| **Mistral Small**          | Yes               | No               |
| **Mixtral 8x7B Instruct**  | Yes               | No               |
| **Pixtral Large**          | Yes               | No               |
| **Voxtral Mini 3B 2507**   | Yes               | Yes              |
| **Voxtral Small 24B 2507** | Yes               | Yes              |

## Moonshot AI

| Model name           | `bedrock-runtime` | `bedrock-mantle` |
| -------------------- | ----------------- | ---------------- |
| **Kimi K2 Thinking** | Yes               | Yes              |
| **Kimi K2.5**        | Yes               | Yes              |

## NVIDIA

| Model name                              | `bedrock-runtime` | `bedrock-mantle` |
| --------------------------------------- | ----------------- | ---------------- |
| **NVIDIA Nemotron Nano 12B v2 VL BF16** | Yes               | Yes              |
| **NVIDIA Nemotron Nano 9B v2**          | Yes               | Yes              |
| **Nemotron Nano 3 30B**                 | Yes               | Yes              |

## OpenAI

| Model name                 | `bedrock-runtime` | `bedrock-mantle` |
| -------------------------- | ----------------- | ---------------- |
| **GPT OSS Safeguard 120B** | Yes               | Yes              |
| **GPT OSS Safeguard 20B**  | Yes               | Yes              |
| **gpt-oss-120b**           | Yes               | Yes              |
| **gpt-oss-20b**            | Yes               | Yes              |

## Qwen

| Model name                         | `bedrock-runtime` | `bedrock-mantle` |
| ---------------------------------- | ----------------- | ---------------- |
| **Qwen3 235B A22B 2507**           | Yes               | Yes              |
| **Qwen3 32B**                      | Yes               | Yes              |
| **Qwen3 Coder 480B A35B Instruct** | Yes               | Yes              |
| **Qwen3 Coder Next**               | Yes               | Yes              |
| **Qwen3 Next 80B A3B**             | Yes               | Yes              |
| **Qwen3 VL 235B A22B**             | Yes               | Yes              |
| **Qwen3-Coder-30B-A3B-Instruct**   | Yes               | Yes              |

## Stability AI

| Model name                            | `bedrock-runtime` | `bedrock-mantle` |
| ------------------------------------- | ----------------- | ---------------- |
| **Stable Image Conservative Upscale** | Yes               | No               |
| **Stable Image Control Sketch**       | Yes               | No               |
| **Stable Image Control Structure**    | Yes               | No               |
| **Stable Image Creative Upscale**     | Yes               | No               |
| **Stable Image Erase Object**         | Yes               | No               |
| **Stable Image Fast Upscale**         | Yes               | No               |
| **Stable Image Inpaint**              | Yes               | No               |
| **Stable Image Outpaint**             | Yes               | No               |
| **Stable Image Remove Background**    | Yes               | No               |
| **Stable Image Search and Recolor**   | Yes               | No               |
| **Stable Image Search and Replace**   | Yes               | No               |
| **Stable Image Style Guide**          | Yes               | No               |
| **Stable Image Style Transfer**       | Yes               | No               |

## TwelveLabs

| Model name             | `bedrock-runtime` | `bedrock-mantle` |
| ---------------------- | ----------------- | ---------------- |
| **Marengo Embed 3.0**  | Yes               | No               |
| **Marengo Embed v2.7** | Yes               | No               |
| **Pegasus v1.2**       | Yes               | No               |

## Writer

| Model name     | `bedrock-runtime` | `bedrock-mantle` |
| -------------- | ----------------- | ---------------- |
| **Palmyra X4** | Yes               | No               |
| **Palmyra X5** | Yes               | No               |

## Z.AI

| Model name        | `bedrock-runtime` | `bedrock-mantle` |
| ----------------- | ----------------- | ---------------- |
| **GLM 4.7**       | Yes               | Yes              |
| **GLM 4.7 Flash** | Yes               | Yes              |
