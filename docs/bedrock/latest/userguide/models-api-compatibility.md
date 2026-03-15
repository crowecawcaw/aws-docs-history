# API compatibility

Amazon Bedrock supports three families of runtime APIs, each designed for different integration patterns and use cases.

**Invoke family**: `InvokeModel` handles synchronous, single-response calls. `InvokeModelWithResponseStream` returns responses as a real-time stream. `InvokeModelWithBidirectionalStream` enables full-duplex streaming for interactive applications. `AsyncInvoke` submits long-running requests asynchronously, storing output to Amazon S3.

**Converse family**: `Converse` provides a unified, model-agnostic interface for synchronous multi-turn conversations. `ConverseStream` delivers the same experience with streaming output.

**OpenAI-compatible family**: `ChatCompletions` implements the OpenAI Chat Completions interface, enabling existing OpenAI-based integrations to run on Bedrock with minimal changes. `Responses` API implements the OpenAI Responses interface, supporting stateful, agentic interactions with built-in tool use and conversation history management.

We will now look at the list of APIs supported by each model.

## AI21

| Model name                                                                                                 | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Jamba 1.5 Large](model-card-ai21-labs-jamba-1-5-large.md "model-card-ai21-labs-jamba-1-5-large.md")\*** | Yes    | Yes      | No               | No        |
| **[Jamba 1.5 Mini](model-card-ai21-labs-jamba-1-5-mini.md "model-card-ai21-labs-jamba-1-5-mini.md")\***    | Yes    | Yes      | No               | No        |

## Amazon

| Model name                                                                                                                                               | Invoke | Converse | Chat Completions | Responses |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Amazon Nova Multimodal Embeddings](model-card-amazon-amazon-nova-multimodal-embeddings.md "model-card-amazon-amazon-nova-multimodal-embeddings.md")** | Yes    | No       | No               | No        |
| **[Nova 2 Lite](model-card-amazon-nova-2-lite.md "model-card-amazon-nova-2-lite.md")\***                                                                 | Yes    | Yes      | No               | No        |
| **[Nova 2 Sonic](model-card-amazon-nova-2-sonic.md "model-card-amazon-nova-2-sonic.md")**                                                                | No     | No       | No               | No        |
| **[Nova Canvas](model-card-amazon-nova-canvas.md "model-card-amazon-nova-canvas.md")**                                                                   | Yes    | No       | No               | No        |
| **[Nova Lite](model-card-amazon-nova-lite.md "model-card-amazon-nova-lite.md")\***                                                                       | Yes    | Yes      | No               | No        |
| **[Nova Micro](model-card-amazon-nova-micro.md "model-card-amazon-nova-micro.md")\***                                                                    | Yes    | Yes      | No               | No        |
| **[Nova Premier](model-card-amazon-nova-premier.md "model-card-amazon-nova-premier.md")\***                                                              | Yes    | Yes      | No               | No        |
| **[Nova Pro](model-card-amazon-nova-pro.md "model-card-amazon-nova-pro.md")\***                                                                          | Yes    | Yes      | No               | No        |
| **[Nova Reel](model-card-amazon-nova-reel.md "model-card-amazon-nova-reel.md")**                                                                         | No     | No       | No               | No        |
| **[Nova Sonic](model-card-amazon-nova-sonic.md "model-card-amazon-nova-sonic.md")\***                                                                    | Yes    | No       | No               | No        |
| **[Titan Embeddings G1<br>• Text](model-card-amazon-titan-embeddings-g1---text.md "model-card-amazon-titan-embeddings-g1---text.md")**                   | Yes    | No       | No               | No        |
| **[Titan Image Generator G1 v2](model-card-amazon-titan-image-generator-g1-v2.md "model-card-amazon-titan-image-generator-g1-v2.md")**                   | Yes    | No       | No               | No        |
| **[Titan Multimodal Embeddings G1](model-card-amazon-titan-multimodal-embeddings-g1.md "model-card-amazon-titan-multimodal-embeddings-g1.md")**          | Yes    | No       | No               | No        |
| **[Titan Text Embeddings V2](model-card-amazon-titan-text-embeddings-v2.md "model-card-amazon-titan-text-embeddings-v2.md")**                            | Yes    | No       | No               | No        |
| **[Titan Text Large](model-card-amazon-titan-text-large.md "model-card-amazon-titan-text-large.md")**                                                    | No     | Yes      | No               | No        |

## Anthropic

| Model name                                                                                                       | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Claude 3 Haiku](model-card-anthropic-claude-3-haiku.md "model-card-anthropic-claude-3-haiku.md")\***          | Yes    | Yes      | No               | No        |
| **[Claude 3.5 Haiku](model-card-anthropic-claude-3-5-haiku.md "model-card-anthropic-claude-3-5-haiku.md")\***    | Yes    | Yes      | No               | No        |
| **[Claude Haiku 4.5](model-card-anthropic-claude-haiku-4-5.md "model-card-anthropic-claude-haiku-4-5.md")\***    | Yes    | Yes      | No               | No        |
| **[Claude Opus 4.1](model-card-anthropic-claude-opus-4-1.md "model-card-anthropic-claude-opus-4-1.md")\***       | Yes    | Yes      | No               | No        |
| **[Claude Opus 4.5](model-card-anthropic-claude-opus-4-5.md "model-card-anthropic-claude-opus-4-5.md")\***       | Yes    | Yes      | No               | No        |
| **[Claude Opus 4.6](model-card-anthropic-claude-opus-4-6.md "model-card-anthropic-claude-opus-4-6.md")\***       | Yes    | Yes      | No               | No        |
| **[Claude Sonnet 4](model-card-anthropic-claude-sonnet-4.md "model-card-anthropic-claude-sonnet-4.md")\***       | Yes    | Yes      | No               | No        |
| **[Claude Sonnet 4.5](model-card-anthropic-claude-sonnet-4-5.md "model-card-anthropic-claude-sonnet-4-5.md")\*** | Yes    | Yes      | No               | No        |
| **[Claude Sonnet 4.6](model-card-anthropic-claude-sonnet-4-6.md "model-card-anthropic-claude-sonnet-4-6.md")\*** | Yes    | Yes      | No               | No        |

## Cohere

| Model name                                                                                                  | Invoke | Converse | Chat Completions | Responses |
| ----------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Command R](model-card-cohere-command-r.md "model-card-cohere-command-r.md")\***                          | Yes    | Yes      | No               | No        |
| **[Command R+](model-card-cohere-command-r-plus.md "model-card-cohere-command-r-plus.md")\***               | Yes    | Yes      | No               | No        |
| **[Embed English](model-card-cohere-embed-english.md "model-card-cohere-embed-english.md")**                | Yes    | No       | No               | No        |
| **[Embed Multilingual](model-card-cohere-embed-multilingual.md "model-card-cohere-embed-multilingual.md")** | Yes    | No       | No               | No        |
| **[Embed v4](model-card-cohere-embed-v4.md "model-card-cohere-embed-v4.md")**                               | Yes    | No       | No               | No        |
| **[Rerank 3.5](model-card-cohere-rerank-3-5.md "model-card-cohere-rerank-3-5.md")**                         | Yes    | No       | No               | No        |

## DeepSeek

| Model name                                                                                         | Invoke | Converse | Chat Completions | Responses |
| -------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[DeepSeek V3.2](model-card-deepseek-deepseek-v3-2.md "model-card-deepseek-deepseek-v3-2.md")\*** | Yes    | Yes      | Yes              | No        |
| **[DeepSeek-R1](model-card-deepseek-deepseek-r1.md "model-card-deepseek-deepseek-r1.md")\***       | Yes    | Yes      | No               | No        |
| **[DeepSeek-V3.1](model-card-deepseek-deepseek-v3-1.md "model-card-deepseek-deepseek-v3-1.md")\*** | Yes    | Yes      | Yes              | No        |

## Google

| Model name                                                                                        | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Gemma 3 12B IT](model-card-google-gemma-3-12b-it.md "model-card-google-gemma-3-12b-it.md")\*** | Yes    | Yes      | Yes              | No        |
| **[Gemma 3 27B PT](model-card-google-gemma-3-27b-pt.md "model-card-google-gemma-3-27b-pt.md")\*** | Yes    | Yes      | Yes              | No        |
| **[Gemma 3 4B IT](model-card-google-gemma-3-4b-it.md "model-card-google-gemma-3-4b-it.md")\***    | Yes    | Yes      | Yes              | No        |

## Meta

| Model name                                                                                                                                 | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------- | ---------------- | --------- |
| **[Llama 3 70B Instruct](model-card-meta-llama-3-70b-instruct.md "model-card-meta-llama-3-70b-instruct.md")\***                            | Yes    | Yes      | No               | No        |
| **[Llama 3 8B Instruct](model-card-meta-llama-3-8b-instruct.md "model-card-meta-llama-3-8b-instruct.md")\***                               | Yes    | Yes      | No               | No        |
| **[Llama 3.1 405B Instruct](model-card-meta-llama-3-1-405b-instruct.md "model-card-meta-llama-3-1-405b-instruct.md")**                     | No     | Yes      | No               | No        |
| **[Llama 3.1 70B Instruct](model-card-meta-llama-3-1-70b-instruct.md "model-card-meta-llama-3-1-70b-instruct.md")\***                      | Yes    | Yes      | No               | No        |
| **[Llama 3.1 8B Instruct](model-card-meta-llama-3-1-8b-instruct.md "model-card-meta-llama-3-1-8b-instruct.md")\***                         | Yes    | Yes      | No               | No        |
| **[Llama 3.2 11B Instruct](model-card-meta-llama-3-2-11b-instruct.md "model-card-meta-llama-3-2-11b-instruct.md")\***                      | Yes    | Yes      | No               | No        |
| **[Llama 3.2 1B Instruct](model-card-meta-llama-3-2-1b-instruct.md "model-card-meta-llama-3-2-1b-instruct.md")\***                         | Yes    | Yes      | No               | No        |
| **[Llama 3.2 3B Instruct](model-card-meta-llama-3-2-3b-instruct.md "model-card-meta-llama-3-2-3b-instruct.md")\***                         | Yes    | Yes      | No               | No        |
| **[Llama 3.2 90B Instruct](model-card-meta-llama-3-2-90b-instruct.md "model-card-meta-llama-3-2-90b-instruct.md")\***                      | Yes    | Yes      | No               | No        |
| **[Llama 3.3 70B Instruct](model-card-meta-llama-3-3-70b-instruct.md "model-card-meta-llama-3-3-70b-instruct.md")\***                      | Yes    | Yes      | No               | No        |
| **[Llama 4 Maverick 17B Instruct](model-card-meta-llama-4-maverick-17b-instruct.md "model-card-meta-llama-4-maverick-17b-instruct.md")\*** | Yes    | Yes      | No               | No        |
| **[Llama 4 Scout 17B Instruct](model-card-meta-llama-4-scout-17b-instruct.md "model-card-meta-llama-4-scout-17b-instruct.md")\***          | Yes    | Yes      | No               | No        |

## MiniMax

| Model name                                                                                    | Invoke | Converse | Chat Completions | Responses |
| --------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[MiniMax M2](model-card-minimax-minimax-m2.md "model-card-minimax-minimax-m2.md")\***       | Yes    | Yes      | Yes              | No        |
| **[MiniMax M2.1](model-card-minimax-minimax-m2-1.md "model-card-minimax-minimax-m2-1.md")\*** | Yes    | Yes      | Yes              | No        |

## Mistral

| Model name                                                                                                                        | Invoke | Converse | Chat Completions | Responses |
| --------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Devstral 2 123B](model-card-mistral-ai-devstral-2-123b.md "model-card-mistral-ai-devstral-2-123b.md")\***                      | Yes    | Yes      | Yes              | No        |
| **[Magistral Small 2509](model-card-mistral-ai-magistral-small-2509.md "model-card-mistral-ai-magistral-small-2509.md")\***       | Yes    | Yes      | Yes              | No        |
| **[Ministral 14B 3.0](model-card-mistral-ai-ministral-14b-3-0.md "model-card-mistral-ai-ministral-14b-3-0.md")\***                | Yes    | Yes      | Yes              | No        |
| **[Ministral 3 8B](model-card-mistral-ai-ministral-3-8b.md "model-card-mistral-ai-ministral-3-8b.md")\***                         | Yes    | Yes      | Yes              | No        |
| **[Ministral 3B](model-card-mistral-ai-ministral-3b.md "model-card-mistral-ai-ministral-3b.md")\***                               | Yes    | Yes      | Yes              | No        |
| **[Mistral 7B Instruct](model-card-mistral-ai-mistral-7b-instruct.md "model-card-mistral-ai-mistral-7b-instruct.md")\***          | Yes    | Yes      | No               | No        |
| **[Mistral Large](model-card-mistral-ai-mistral-large.md "model-card-mistral-ai-mistral-large.md")\***                            | Yes    | Yes      | No               | No        |
| **[Mistral Large 3](model-card-mistral-ai-mistral-large-3.md "model-card-mistral-ai-mistral-large-3.md")\***                      | Yes    | Yes      | Yes              | No        |
| **[Mistral Small](model-card-mistral-ai-mistral-small.md "model-card-mistral-ai-mistral-small.md")\***                            | Yes    | Yes      | No               | No        |
| **[Mixtral 8x7B Instruct](model-card-mistral-ai-mixtral-8x7b-instruct.md "model-card-mistral-ai-mixtral-8x7b-instruct.md")\***    | Yes    | Yes      | No               | No        |
| **[Pixtral Large](model-card-mistral-ai-pixtral-large.md "model-card-mistral-ai-pixtral-large.md")\***                            | Yes    | Yes      | No               | No        |
| **[Voxtral Mini 3B 2507](model-card-mistral-ai-voxtral-mini-3b-2507.md "model-card-mistral-ai-voxtral-mini-3b-2507.md")\***       | Yes    | Yes      | Yes              | No        |
| **[Voxtral Small 24B 2507](model-card-mistral-ai-voxtral-small-24b-2507.md "model-card-mistral-ai-voxtral-small-24b-2507.md")\*** | Yes    | Yes      | Yes              | No        |

## Moonshot

| Model name                                                                                                        | Invoke | Converse | Chat Completions | Responses |
| ----------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Kimi K2 Thinking](model-card-moonshot-ai-kimi-k2-thinking.md "model-card-moonshot-ai-kimi-k2-thinking.md")\*** | Yes    | Yes      | No               | No        |
| **[Kimi K2.5](model-card-moonshot-ai-kimi-k2-5.md "model-card-moonshot-ai-kimi-k2-5.md")\***                      | Yes    | Yes      | Yes              | No        |

## NVIDIA

| Model name                                                                                                                                                       | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[NVIDIA Nemotron Nano 12B v2 VL BF16](model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md "model-card-nvidia-nvidia-nemotron-nano-12b-v2-vl-bf16.md")\*** | Yes    | Yes      | Yes              | No        |
| **[NVIDIA Nemotron Nano 9B v2](model-card-nvidia-nvidia-nemotron-nano-9b-v2.md "model-card-nvidia-nvidia-nemotron-nano-9b-v2.md")\***                            | Yes    | Yes      | Yes              | No        |
| **[Nemotron Nano 3 30B](model-card-nvidia-nemotron-nano-3-30b.md "model-card-nvidia-nemotron-nano-3-30b.md")\***                                                 | Yes    | Yes      | Yes              | No        |

## OpenAI

| Model name                                                                                                                | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[GPT OSS Safeguard 120B](model-card-openai-gpt-oss-safeguard-120b.md "model-card-openai-gpt-oss-safeguard-120b.md")\*** | Yes    | Yes      | Yes              | Yes       |
| **[GPT OSS Safeguard 20B](model-card-openai-gpt-oss-safeguard-20b.md "model-card-openai-gpt-oss-safeguard-20b.md")\***    | Yes    | Yes      | Yes              | Yes       |
| **[gpt-oss-120b](model-card-openai-gpt-oss-120b.md "model-card-openai-gpt-oss-120b.md")\***                               | Yes    | Yes      | Yes              | Yes       |
| **[gpt-oss-20b](model-card-openai-gpt-oss-20b.md "model-card-openai-gpt-oss-20b.md")\***                                  | Yes    | Yes      | Yes              | Yes       |

## Qwen

| Model name                                                                                                                                    | Invoke | Converse | Chat Completions | Responses |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Qwen3 235B A22B 2507](model-card-qwen-qwen3-235b-a22b-2507.md "model-card-qwen-qwen3-235b-a22b-2507.md")\***                               | Yes    | Yes      | Yes              | No        |
| **[Qwen3 32B](model-card-qwen-qwen3-32b.md "model-card-qwen-qwen3-32b.md")\***                                                                | Yes    | Yes      | Yes              | No        |
| **[Qwen3 Coder 480B A35B Instruct](model-card-qwen-qwen3-coder-480b-a35b-instruct.md "model-card-qwen-qwen3-coder-480b-a35b-instruct.md")\*** | Yes    | Yes      | Yes              | No        |
| **[Qwen3 Coder Next](model-card-qwen-qwen3-coder-next.md "model-card-qwen-qwen3-coder-next.md")\***                                           | Yes    | Yes      | Yes              | No        |
| **[Qwen3 Next 80B A3B](model-card-qwen-qwen3-next-80b-a3b.md "model-card-qwen-qwen3-next-80b-a3b.md")\***                                     | Yes    | Yes      | Yes              | No        |
| **[Qwen3 VL 235B A22B](model-card-qwen-qwen3-vl-235b-a22b.md "model-card-qwen-qwen3-vl-235b-a22b.md")\***                                     | Yes    | Yes      | Yes              | No        |
| **[Qwen3-Coder-30B-A3B-Instruct](model-card-qwen-qwen3-coder-30b-a3b-instruct.md "model-card-qwen-qwen3-coder-30b-a3b-instruct.md")\***       | Yes    | Yes      | Yes              | No        |

## Stability

| Model name                                                                                                                                                           | Invoke | Converse | Chat Completions | Responses |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Stable Image Conservative Upscale](model-card-stability-ai-stable-image-conservative-upscale.md "model-card-stability-ai-stable-image-conservative-upscale.md")** | Yes    | No       | No               | No        |
| **[Stable Image Control Sketch](model-card-stability-ai-stable-image-control-sketch.md "model-card-stability-ai-stable-image-control-sketch.md")**                   | Yes    | No       | No               | No        |
| **[Stable Image Control Structure](model-card-stability-ai-stable-image-control-structure.md "model-card-stability-ai-stable-image-control-structure.md")**          | Yes    | No       | No               | No        |
| **[Stable Image Creative Upscale](model-card-stability-ai-stable-image-creative-upscale.md "model-card-stability-ai-stable-image-creative-upscale.md")**             | Yes    | No       | No               | No        |
| **[Stable Image Erase Object](model-card-stability-ai-stable-image-erase-object.md "model-card-stability-ai-stable-image-erase-object.md")**                         | Yes    | No       | No               | No        |
| **[Stable Image Fast Upscale](model-card-stability-ai-stable-image-fast-upscale.md "model-card-stability-ai-stable-image-fast-upscale.md")**                         | Yes    | No       | No               | No        |
| **[Stable Image Inpaint](model-card-stability-ai-stable-image-inpaint.md "model-card-stability-ai-stable-image-inpaint.md")**                                        | Yes    | No       | No               | No        |
| **[Stable Image Outpaint](model-card-stability-ai-stable-image-outpaint.md "model-card-stability-ai-stable-image-outpaint.md")**                                     | Yes    | No       | No               | No        |
| **[Stable Image Remove Background](model-card-stability-ai-stable-image-remove-background.md "model-card-stability-ai-stable-image-remove-background.md")**          | Yes    | No       | No               | No        |
| **[Stable Image Search and Recolor](model-card-stability-ai-stable-image-search-and-recolor.md "model-card-stability-ai-stable-image-search-and-recolor.md")**       | Yes    | No       | No               | No        |
| **[Stable Image Search and Replace](model-card-stability-ai-stable-image-search-and-replace.md "model-card-stability-ai-stable-image-search-and-replace.md")**       | Yes    | No       | No               | No        |
| **[Stable Image Style Guide](model-card-stability-ai-stable-image-style-guide.md "model-card-stability-ai-stable-image-style-guide.md")**                            | Yes    | No       | No               | No        |
| **[Stable Image Style Transfer](model-card-stability-ai-stable-image-style-transfer.md "model-card-stability-ai-stable-image-style-transfer.md")**                   | Yes    | No       | No               | No        |

## TwelveLabs

| Model name                                                                                                          | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Marengo Embed 3.0](model-card-twelvelabs-marengo-embed-3-0.md "model-card-twelvelabs-marengo-embed-3-0.md")**    | Yes    | No       | No               | No        |
| **[Marengo Embed v2.7](model-card-twelvelabs-marengo-embed-v2-7.md "model-card-twelvelabs-marengo-embed-v2-7.md")** | No     | No       | No               | No        |
| **[Pegasus v1.2](model-card-twelvelabs-pegasus-v1-2.md "model-card-twelvelabs-pegasus-v1-2.md")**                   | Yes    | No       | No               | No        |

## Writer

| Model name                                                                            | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[Palmyra X4](model-card-writer-palmyra-x4.md "model-card-writer-palmyra-x4.md")\*** | Yes    | Yes      | No               | No        |
| **[Palmyra X5](model-card-writer-palmyra-x5.md "model-card-writer-palmyra-x5.md")\*** | Yes    | Yes      | No               | No        |

## Z.AI

| Model name                                                                               | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------------------------------------------------------------- | ------ | -------- | ---------------- | --------- |
| **[GLM 4.7](model-card-zai-glm-4-7.md "model-card-zai-glm-4-7.md")\***                   | Yes    | Yes      | Yes              | No        |
| **[GLM 4.7 Flash](model-card-zai-glm-4-7-flash.md "model-card-zai-glm-4-7-flash.md")\*** | Yes    | Yes      | Yes              | No        |

###### Note

**\* Streaming Support:** Models marked with an asterisk (\*) also support `InvokeModelWithResponseStream`, which returns responses as a real-time stream.

## **Models supporting StartAsyncInvoke**

StartAsyncInvoke is an Amazon Bedrock Runtime API that allows callers to submit a model invocation request and immediately receive back an invocationArn without waiting for the model to finish processing. The job runs in the background, and the output is written to a caller-specified S3 bucket once complete. Callers can then poll job status using the companion GetAsyncInvoke and ListAsyncInvokes APIs. The pattern is purpose-built for workloads involving large or latency-insensitive inputs, particularly video, audio, and bulk embedding generation, where holding an open synchronous connection would be impractical.

In terms of which models support it, the following models support StartAsyncInvoke:

- **TwelveLabs Marengo Embed 2.7** (twelvelabs.marengo-embed-2-7-v1:0) — required for video and audio input; InvokeModel only handles text and image
- **TwelveLabs Marengo Embed 3.0** (twelvelabs.marengo-embed-3-0-v1:0) — same pattern; async required for video/audio at scale
- **Amazon Nova Reel** (amazon.nova-reel-v1:0 and v1:1) — video generation is exclusively async; output lands in S3
- **Amazon Nova Multimodal Embeddings** (amazon.nova-2-multimodal-embeddings-v1:0) — async is required for video inputs larger than 25MB base64-encoded; sync is available for text, image, and document inputs

## **InvokeModelWithBidirectionalStream**

`InvokeModelWithBidirectionalStream` is an Amazon Bedrock Runtime API that establishes a persistent, full-duplex channel between the caller and the model, allowing audio data to flow in both directions simultaneously and continuously. Unlike the standard `InvokeModel` or even `InvokeModelWithResponseStream` APIs, which follow a request-then-response pattern, this API keeps the connection open for the duration of a session so that the model can process incoming audio as it arrives and stream generated speech back in near real-time, without waiting for a complete utterance to finish. The interaction is structured around three phases: session initialization (where the client sends configuration events to set up the stream), audio streaming (where captured audio is encoded and sent as a continuous event stream), and response streaming (where the model simultaneously returns text transcriptions of user speech and synthesized audio output). `InvokeModelWithBidirectionalStream` cannot be used with Amazon Bedrock API keys and requires standard AWS credential-based authentication, reflecting its more complex session lifecycle compared to other Bedrock Runtime operations.

The following models support this API:

- **Amazon Nova Sonic family**: Both amazon.nova-sonic-v1:0 and amazon.nova-2-sonic-v1:0 use it as their sole invocation path, since the speech-to-speech architecture fundamentally requires a live bidirectional channel that neither InvokeModel nor Converse can provide.
