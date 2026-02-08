# Get validated JSON results from models

Structured outputs is a capability on Amazon Bedrock that ensures model responses conform to user-defined JSON schemas and tool definitions, reducing the need for custom parsing and validation mechanisms in production AI deployments.

## Benefits

Structured outputs addresses critical challenges in production AI applications:

- **Ensures schema compliance** – Eliminates error rates and retry loops from prompt-based approaches
- **Reduced development complexity** – Removes the need for custom parsing and validation logic
- **Lower operational costs** – Reduces failed requests and retries
- **Production reliability** – Enables confident deployment of AI applications requiring predictable, machine-readable outputs

## How it works

Structured outputs constrains model responses to follow a specific schema, ensuring valid, parseable output for downstream processing. You can use structured outputs through two complementary mechanisms:

### JSON Schema output format

For InvokeModel API with Anthropic Claude models, use the `output_config.format` request field. With open weight models, use the `response_format` request field. For Converse APIs, use the `outputConfig.textFormat` request field. The model's response will conform to the specified JSON schema.

### Strict tool use

Add the `strict: true` flag to tool definitions to enable schema validation on tool names and inputs. The model's tool calls will then follow the defined tool input schema.

These mechanisms can be used independently or together in the same request. Refer to [Bedrock API documentation](../APIReference/welcome.md "../APIReference/welcome.md") for more details.

### Request workflow

The following describes how Amazon Bedrock processes requests with structured outputs:

1. **Initial request** – You include either a JSON schema via the `outputConfig.textFormat`, `output_config.format`, or `response_format` parameter or a tool definition with the `strict: true` flag in your inference request.
2. **Schema validation** – Amazon Bedrock validates the JSON schema format against the supported JSON Schema Draft 2020-12 subset. If the schema contains unsupported features, Amazon Bedrock returns a 400 error immediately.
3. **First-time compilation** – For new schemas, Amazon Bedrock compiles the grammar, which may take up to a few minutes.
4. **Caching** – Successfully compiled grammars are cached for 24 hours from first access. Cached grammars are encrypted with AWS-managed keys.
5. **Subsequent requests** – Identical schemas from the same account use cached grammars, resulting in inference latency comparable to standard requests with minimal overhead.
6. **Response** – You receive standard inference responses with strict schema compliance.

## Supported APIs or features

You can use structured outputs across the following Amazon Bedrock features:

**Converse and ConverseStream APIs** – Use structured outputs with the Converse and ConverseStream APIs for conversational inference.

**InvokeModel and InvokeModelWithResponseStream APIs** – Use structured outputs with the InvokeModel and InvokeModelWithResponseStream APIs for single-turn inference.

**Cross-Region inference** – Use structured outputs within cross-Region inference without any additional setup.

**Batch inference** – Use structured outputs within batch inference without any additional setup.

###### Note

Structured outputs is incompatible with citations for Anthropic models. If you enable citations while using structured outputs, the model will return a 400 error.

## Supported models

Structured outputs is generally available in all commercial AWS regions for the select Amazon Bedrock serverless models. For the list of supported model, refer Model support by feature.

Anthropic

- Claude Haiku 4.5 (`anthropic.claude-haiku-4-5-20251001-v1:0`)
- Claude Sonnet 4.5 (`anthropic.claude-sonnet-4-5-20250929-v1:0`)
- Claude Opus 4.5 (`anthropic.claude-opus-4-5-20251101-v1:0`)
- Claude Opus 4.6 (`anthropic.claude-opus-4-6-v1`)

Qwen

- Qwen3 235B A22B 2507 (`qwen.qwen3-235b-a22b-2507-v1:0`)
- Qwen3 32B (dense) (`qwen.qwen3-32b-v1:0`)
- Qwen3-Coder-30B-A3B-Instruct (`qwen.qwen3-coder-30b-a3b-v1:0`)
- Qwen3 Coder 480B A35B Instruct (`qwen.qwen3-coder-480b-a35b-v1:0`)
- Qwen3 Next 80B A3B (`qwen.qwen3-next-80b-a3b`)
- Qwen3 VL 235B A22B (`qwen.qwen3-vl-235b-a22b`)

OpenAI

- gpt-oss-120b (`openai.gpt-oss-120b-1:0`)
- gpt-oss-20b (`openai.gpt-oss-20b-1:0`)
- GPT OSS Safeguard 120B (`openai.gpt-oss-safeguard-120b`)
- GPT OSS Safeguard 20B (`openai.gpt-oss-safeguard-20b`)

DeepSeek

- DeepSeek-V3.1 (`deepseek.v3-v1:0`)

Google

- Gemma 3 12B IT (`google.gemma-3-12b-it`)
- Gemma 3 27B PT (`google.gemma-3-27b-it`)

MiniMax

- MiniMax M2 (`minimax.minimax-m2`)

Mistral AI

- Magistral Small 2509 (`mistral.magistral-small-2509`)
- Ministral 3B (`mistral.ministral-3-3b-instruct`)
- Ministral 3 8B (`mistral.ministral-3-8b-instruct`)
- Ministral 14B 3.0 (`mistral.ministral-3-14b-instruct`)
- Mistral Large 3 (`mistral.mistral-large-3-675b-instruct`)
- Voxtral Mini 3B 2507 (`mistral.voxtral-mini-3b-2507`)
- Voxtral Small 24B 2507 (`mistral.voxtral-small-24b-2507`)

Moonshot AI

- Kimi K2 Thinking (`moonshot.kimi-k2-thinking`)

NVIDIA

- NVIDIA Nemotron Nano 12B v2 VL BF16 (`nvidia.nemotron-nano-12b-v2`)
- NVIDIA Nemotron Nano 9B v2 (`nvidia.nemotron-nano-9b-v2`)

## Example requests

### JSON Schema output format

The following examples show how to use JSON Schema output format with structured outputs.

#### Converse API

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "Given the following unstructured data, extract it into the provided structure."
        },
        {
          "text": "..."
        }
      ]
    }
  ],
  "outputConfig": {
    "textFormat": {
      "type": "json_schema",
      "structure": {
        "jsonSchema": {
          "schema": "{\"type\": \"object\", \"properties\": {\"title\": {\"type\": \"string\", \"description\": \"title\"}, \"summary\": {\"type\": \"string\", \"description\": \"summary\"}, \"next_steps\": {\"type\": \"string\", \"description\": \"next steps\"}}, \"required\": [\"title\", \"summary\", \"next_steps\"], \"additionalProperties\": false}",
          "name": "data_extraction",
          "description": "Extract structured data from unstructured text"
        }
      }
    }
  }
}
```

#### InvokeModel (Anthropic Claude)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Given the following unstructured data, extract it into the provided structure."
        },
        {
          "type": "text",
          "text": "..."
        }
      ]
    }
  ],
  "max_tokens": 3000,
  "temperature": 1.0,
  "output_config": {
    "format": {
      "type": "json_schema",
      "schema": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "title"
          },
          "summary": {
            "type": "string",
            "description": "summary"
          },
          "next_steps": {
            "type": "string",
            "description": "next steps"
          }
        },
        "required": [
          "title",
          "summary",
          "next_steps"
        ],
        "additionalProperties": false
      }
    }
  }
}
```

#### InvokeModel (Open-weight models)

```
{
  "messages": [
    {
      "role": "user",
      "content": "Given the following unstructured data, extract it into the provided structure."
    },
    {
      "role": "user",
      "content": "..."
    }
  ],
  "inferenceConfig": {
    "maxTokens": 3000,
    "temperature": 1.0
  },
  "response_format": {
    "json_schema": {
      "name": "summarizer",
      "schema": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "title"
          },
          "summary": {
            "type": "string",
            "description": "summary"
          },
          "next_steps": {
            "type": "string",
            "description": "next steps"
          }
        },
        "required": [
          "title",
          "summary",
          "next_steps"
        ],
        "additionalProperties": false
      }
    },
    "type": "json_schema"
  }
}
```

### Strict tool use

The following examples show how to use the strict field with tool use.

#### Converse API

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What's the weather like in New York?"
        }
      ]
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "get_weather",
          "description": "Get the current weather for a specified location",
          "strict": true,
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": [
                    "fahrenheit",
                    "celsius"
                  ],
                  "description": "The temperature unit to use"
                }
              },
              "required": [
                "location",
                "unit"
              ]
            }
          }
        }
      }
    ]
  }
}
```

#### InvokeModel (Anthropic Claude)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What's the weather like in San Francisco?"
        }
      ]
    }
  ],
  "max_tokens": 3000,
  "temperature": 1.0,
  "tools": [
    {
      "name": "get_weather",
      "description": "Get the current weather for a specified location",
      "strict": true,
      "input_schema": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "fahrenheit",
              "celsius"
            ],
            "description": "The temperature unit to use"
          }
        },
        "required": [
          "location",
          "unit"
        ],
        "additionalProperties": false
      }
    }
  ]
}
```

#### InvokeModel (Open-weight models)

```
{
  "messages": [
    {
      "role": "user",
      "content": "What's the weather like in San Francisco?"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather for a specified location",
        "strict": true,
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": [
                "fahrenheit",
                "celsius"
              ],
              "description": "The temperature unit to use"
            }
          },
          "required": [
            "location",
            "unit"
          ]
        }
      }
    }
  ],
  "tool_choice": "auto",
  "max_tokens": 2000,
  "temperature": 1.0
}
```
