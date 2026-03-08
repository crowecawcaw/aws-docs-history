# API compatibility

Amazon Bedrock supports three families of runtime APIs, each designed for different integration patterns and use cases.

**Invoke family**: `InvokeModel` handles synchronous, single-response calls. `InvokeModelWithResponseStream` returns responses as a real-time stream. `InvokeModelWithBidirectionalStream` enables full-duplex streaming for interactive applications. `AsyncInvoke` submits long-running requests asynchronously, storing output to Amazon S3.

**Converse family**: `Converse` provides a unified, model-agnostic interface for synchronous multi-turn conversations. `ConverseStream` delivers the same experience with streaming output.

**OpenAI-compatible family**: `ChatCompletions` implements the OpenAI Chat Completions interface, enabling existing OpenAI-based integrations to run on Bedrock with minimal changes. `Responses` API implements the OpenAI Responses interface, supporting stateful, agentic interactions with built-in tool use and conversation history management.

We will now look at the list of APIs supported by each model.

## AI21

| Model name            | Invoke | Converse | Chat Completions | Responses |
| --------------------- | ------ | -------- | ---------------- | --------- |
| **Jamba 1.5 Large\*** | Yes    | Yes      | No               | No        |
| **Jamba 1.5 Mini\***  | Yes    | Yes      | No               | No        |

## Amazon

| Model name                         | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------- | ------ | -------- | ---------------- | --------- |
| **Nova Multimodal Embeddings**     | Yes    | No       | No               | No        |
| **Nova 2 Lite\***                  | Yes    | Yes      | No               | No        |
| **Nova 2 Sonic**                   | No     | No       | No               | No        |
| **Nova Canvas**                    | Yes    | No       | No               | No        |
| **Nova Lite\***                    | Yes    | Yes      | No               | No        |
| **Nova Micro\***                   | Yes    | Yes      | No               | No        |
| **Nova Premier\***                 | Yes    | Yes      | No               | No        |
| **Nova Pro\***                     | Yes    | Yes      | No               | No        |
| **Nova Reel**                      | No     | No       | No               | No        |
| **Nova Sonic\***                   | Yes    | No       | No               | No        |
| **Titan Embeddings G1<br>• Text**  | Yes    | No       | No               | No        |
| **Titan Image Generator G1 v2**    | Yes    | No       | No               | No        |
| **Titan Multimodal Embeddings G1** | Yes    | No       | No               | No        |
| **Titan Text Embeddings V2**       | Yes    | No       | No               | No        |
| **Titan Text Large**               | No     | Yes      | No               | No        |

## Anthropic

| Model name              | Invoke | Converse | Chat Completions | Responses |
| ----------------------- | ------ | -------- | ---------------- | --------- |
| **Claude 3 Haiku\***    | Yes    | Yes      | No               | No        |
| **Claude 3.5 Haiku\***  | Yes    | Yes      | No               | No        |
| **Claude Haiku 4.5\***  | Yes    | Yes      | No               | No        |
| **Claude Opus 4.1\***   | Yes    | Yes      | No               | No        |
| **Claude Opus 4.5\***   | Yes    | Yes      | No               | No        |
| **Claude Opus 4.6\***   | Yes    | Yes      | No               | No        |
| **Claude Sonnet 4\***   | Yes    | Yes      | No               | No        |
| **Claude Sonnet 4.5\*** | Yes    | Yes      | No               | No        |
| **Claude Sonnet 4.6\*** | Yes    | Yes      | No               | No        |

## Cohere

| Model name             | Invoke | Converse | Chat Completions | Responses |
| ---------------------- | ------ | -------- | ---------------- | --------- |
| **Command R\***        | Yes    | Yes      | No               | No        |
| **Command R+\***       | Yes    | Yes      | No               | No        |
| **Embed English**      | Yes    | No       | No               | No        |
| **Embed Multilingual** | Yes    | No       | No               | No        |
| **Embed v4**           | Yes    | No       | No               | No        |
| **Rerank 3.5**         | Yes    | No       | No               | No        |

## DeepSeek

| Model name          | Invoke | Converse | Chat Completions | Responses |
| ------------------- | ------ | -------- | ---------------- | --------- |
| **DeepSeek V3.2\*** | Yes    | Yes      | Yes              | No        |
| **DeepSeek-R1\***   | Yes    | Yes      | No               | No        |
| **DeepSeek-V3.1\*** | Yes    | Yes      | Yes              | No        |

## Google

| Model name           | Invoke | Converse | Chat Completions | Responses |
| -------------------- | ------ | -------- | ---------------- | --------- |
| **Gemma 3 12B IT\*** | Yes    | Yes      | Yes              | No        |
| **Gemma 3 27B PT\*** | Yes    | Yes      | Yes              | No        |
| **Gemma 3 4B IT\***  | Yes    | Yes      | Yes              | No        |

## Meta

| Model name                          | Invoke | Converse | Chat Completions | Responses |
| ----------------------------------- | ------ | -------- | ---------------- | --------- |
| **Llama 3 70B Instruct\***          | Yes    | Yes      | No               | No        |
| **Llama 3 8B Instruct\***           | Yes    | Yes      | No               | No        |
| **Llama 3.1 405B Instruct**         | No     | Yes      | No               | No        |
| **Llama 3.1 70B Instruct\***        | Yes    | Yes      | No               | No        |
| **Llama 3.1 8B Instruct\***         | Yes    | Yes      | No               | No        |
| **Llama 3.2 11B Instruct\***        | Yes    | Yes      | No               | No        |
| **Llama 3.2 1B Instruct\***         | Yes    | Yes      | No               | No        |
| **Llama 3.2 3B Instruct\***         | Yes    | Yes      | No               | No        |
| **Llama 3.2 90B Instruct\***        | Yes    | Yes      | No               | No        |
| **Llama 3.3 70B Instruct\***        | Yes    | Yes      | No               | No        |
| **Llama 4 Maverick 17B Instruct\*** | Yes    | Yes      | No               | No        |
| **Llama 4 Scout 17B Instruct\***    | Yes    | Yes      | No               | No        |

## MiniMax

| Model name         | Invoke | Converse | Chat Completions | Responses |
| ------------------ | ------ | -------- | ---------------- | --------- |
| **MiniMax M2\***   | Yes    | Yes      | Yes              | No        |
| **MiniMax M2.1\*** | Yes    | Yes      | Yes              | No        |

## Mistral

| Model name                      | Invoke | Converse | Chat Completions | Responses |
| ------------------------------- | ------ | -------- | ---------------- | --------- |
| **AI Devstral 2 123B\***        | Yes    | Yes      | Yes              | No        |
| **AI Magistral Small 2509\***   | Yes    | Yes      | Yes              | No        |
| **Ministral 14B 3.0\***         | Yes    | Yes      | Yes              | No        |
| **Ministral 3 8B\***            | Yes    | Yes      | Yes              | No        |
| **Ministral 3B\***              | Yes    | Yes      | Yes              | No        |
| **Mistral 7B Instruct\***       | Yes    | Yes      | No               | No        |
| **Mistral Large\***             | Yes    | Yes      | No               | No        |
| **Mistral Large 3\***           | Yes    | Yes      | Yes              | No        |
| **Mistral Small\***             | Yes    | Yes      | No               | No        |
| **Mixtral 8x7B Instruct\***     | Yes    | Yes      | No               | No        |
| **AI Pixtral Large\***          | Yes    | Yes      | No               | No        |
| **AI Voxtral Mini 3B 2507\***   | Yes    | Yes      | Yes              | No        |
| **AI Voxtral Small 24B 2507\*** | Yes    | Yes      | Yes              | No        |

## Moonshot

| Model name             | Invoke | Converse | Chat Completions | Responses |
| ---------------------- | ------ | -------- | ---------------- | --------- |
| **Kimi K2 Thinking\*** | Yes    | Yes      | No               | No        |
| **Kimi K2.5\***        | Yes    | Yes      | Yes              | No        |

## NVIDIA

| Model name                         | Invoke | Converse | Chat Completions | Responses |
| ---------------------------------- | ------ | -------- | ---------------- | --------- |
| **Nemotron Nano 12B v2 VL BF16\*** | Yes    | Yes      | Yes              | No        |
| **Nemotron Nano 9B v2\***          | Yes    | Yes      | Yes              | No        |
| **Nemotron Nano 3 30B\***          | Yes    | Yes      | Yes              | No        |

## OpenAI

| Model name                   | Invoke | Converse | Chat Completions | Responses |
| ---------------------------- | ------ | -------- | ---------------- | --------- |
| **GPT OSS Safeguard 120B\*** | Yes    | Yes      | Yes              | Yes       |
| **GPT OSS Safeguard 20B\***  | Yes    | Yes      | Yes              | Yes       |
| **gpt-oss-120b\***           | Yes    | Yes      | Yes              | Yes       |
| **gpt-oss-20b\***            | Yes    | Yes      | Yes              | Yes       |

## Qwen

| Model name                           | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------ | ------ | -------- | ---------------- | --------- |
| **Qwen3 235B A22B 2507\***           | Yes    | Yes      | Yes              | No        |
| **Qwen3 32B\***                      | Yes    | Yes      | Yes              | No        |
| **Qwen3 Coder 480B A35B Instruct\*** | Yes    | Yes      | Yes              | No        |
| **Qwen3 Coder Next\***               | Yes    | Yes      | Yes              | No        |
| **Qwen3 Next 80B A3B\***             | Yes    | Yes      | Yes              | No        |
| **Qwen3 VL 235B A22B\***             | Yes    | Yes      | Yes              | No        |
| **Qwen3-Coder-30B-A3B-Instruct\***   | Yes    | Yes      | Yes              | No        |

## Stability

| Model name                            | Invoke | Converse | Chat Completions | Responses |
| ------------------------------------- | ------ | -------- | ---------------- | --------- |
| **Stable Image Conservative Upscale** | Yes    | No       | No               | No        |
| **Stable Image Control Sketch**       | Yes    | No       | No               | No        |
| **Stable Image Control Structure**    | Yes    | No       | No               | No        |
| **Stable Image Creative Upscale**     | Yes    | No       | No               | No        |
| **Stable Image Erase Object**         | Yes    | No       | No               | No        |
| **Stable Image Fast Upscale**         | Yes    | No       | No               | No        |
| **Stable Image Inpaint**              | Yes    | No       | No               | No        |
| **Stable Image Outpaint**             | Yes    | No       | No               | No        |
| **Stable Image Remove Background**    | Yes    | No       | No               | No        |
| **Stable Image Search and Recolor**   | Yes    | No       | No               | No        |
| **Stable Image Search and Replace**   | Yes    | No       | No               | No        |
| **Stable Image Style Guide**          | Yes    | No       | No               | No        |
| **Stable Image Style Transfer**       | Yes    | No       | No               | No        |

## TwelveLabs

| Model name            | Invoke | Converse | Chat Completions | Responses |
| --------------------- | ------ | -------- | ---------------- | --------- |
| **Marengo Embed 3.0** | Yes    | No       | No               | No        |
| **Marengo Embed 2.7** | No     | No       | No               | No        |
| **Pegasus v1.2**      | Yes    | No       | No               | No        |

## Writer

| Model name       | Invoke | Converse | Chat Completions | Responses |
| ---------------- | ------ | -------- | ---------------- | --------- |
| **Palmyra X4\*** | Yes    | Yes      | No               | No        |
| **Palmyra X5\*** | Yes    | Yes      | No               | No        |

## Z.AI

| Model name          | Invoke | Converse | Chat Completions | Responses |
| ------------------- | ------ | -------- | ---------------- | --------- |
| **GLM 4.7\***       | Yes    | Yes      | Yes              | No        |
| **GLM 4.7 Flash\*** | Yes    | Yes      | Yes              | No        |

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
