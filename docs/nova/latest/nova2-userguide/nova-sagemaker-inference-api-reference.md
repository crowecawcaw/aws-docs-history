# API Reference

Amazon Nova models on SageMaker use the standard SageMaker Runtime API for inference. For complete API documentation, see [Test a deployed model](../../../sagemaker/latest/dg/realtime-endpoints-test-endpoints.md "../../../sagemaker/latest/dg/realtime-endpoints-test-endpoints.md").

## Endpoint invocation

Amazon Nova models on SageMaker support two invocation methods:

- **Synchronous invocation**: Use the [InvokeEndpoint](../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.md "../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.md") API for real-time, non-streaming inference requests.
- **Streaming invocation**: Use the [InvokeEndpointWithResponseStream](../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md "../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md") API for real-time streaming inference requests.

## Request format

Amazon Nova models support two request formats:

**Chat completion format**

Use this format for conversational interactions:

```
{
  "messages": [
    {"role": "user", "content": "string"}
  ],
  "max_tokens": integer,
  "max_completion_tokens": integer,
  "stream": boolean,
  "temperature": float,
  "top_p": float,
  "top_k": integer,
  "logprobs": boolean,
  "top_logprobs": integer,
  "reasoning_effort": "low" | "high",
  "allowed_token_ids": [integer],
  "truncate_prompt_tokens": integer,
  "stream_options": {
    "include_usage": boolean
  }
}
```

**Text completion format**

Use this format for simple text generation:

```
{
  "prompt": "string",
  "max_tokens": integer,
  "stream": boolean,
  "temperature": float,
  "top_p": float,
  "top_k": integer,
  "logprobs": integer,
  "allowed_token_ids": [integer],
  "truncate_prompt_tokens": integer,
  "stream_options": {
    "include_usage": boolean
  }
}
```

**Multimodal chat completion format**

Use this format for image and text inputs:

```
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image?"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
      ]
    }
  ],
  "max_tokens": integer,
  "temperature": float,
  "top_p": float,
  "stream": boolean
}
```

**Request parameters**

- `messages` (array): For chat completion format. Array of message objects with `role` and `content` fields. Content can be a string for text-only or an array for multimodal inputs.
- `prompt` (string): For text completion format. The input text to generate from.
- `max_tokens` (integer): Maximum number of tokens to generate in the response. Range: 1 or greater.
- `max_completion_tokens` (integer): Alternative to max_tokens for chat completions. Maximum number of completion tokens to generate.
- `temperature` (float): Controls randomness in generation. Range: 0.0 to 2.0 (0.0 = deterministic, 2.0 = maximum randomness).
- `top_p` (float): Nucleus sampling threshold. Range: 1e-10 to 1.0.
- `top_k` (integer): Limits token selection to top K most likely tokens. Range: -1 or greater (-1 = no limit).
- `stream` (boolean): Whether to stream the response. Set to `true` for streaming, `false` for non-streaming.
- `logprobs` (boolean/integer): For chat completions, use boolean. For text completions, use integer for number of log probabilities to return. Range: 1 to 20.
- `top_logprobs` (integer): Number of most likely tokens to return log probabilities for (chat completions only).
- `reasoning_effort` (string): Level of reasoning effort. Options: "low", "high" (chat completions for Nova 2 Lite custom models only).
- `allowed_token_ids` (array): List of token IDs that are allowed to be generated. Restricts output to specified tokens.
- `truncate_prompt_tokens` (integer): Truncate the prompt to this many tokens if it exceeds the limit.
- `stream_options` (object): Options for streaming responses. Contains `include_usage` boolean to include token usage in streaming responses.

## Response format

The response format depends on the invocation method and request type:

**Chat completion response (non-streaming)**

For synchronous chat completion requests:

```
{
  "id": "chatcmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! I'm doing well, thank you for asking. How can I help you today?",
        "refusal": null,
        "reasoning": null,
        "reasoning_content": null
      },
      "logprobs": {
        "content": [
          {
            "token": "Hello",
            "logprob": -0.31725305,
            "bytes": [72, 101, 108, 108, 111],
            "top_logprobs": [
              {
                "token": "Hello",
                "logprob": -0.31725305,
                "bytes": [72, 101, 108, 108, 111]
              },
              {
                "token": "Hi",
                "logprob": -1.3190403,
                "bytes": [72, 105]
              }
            ]
          }
        ]
      },
      "finish_reason": "stop",
      "stop_reason": null,
      "token_ids": [9906, 0, 358, 2157, 1049, 11, 1309, 345, 369, 6464, 13]
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "prompt_token_ids": [9906, 0, 358]
}
```

**Text completion response (non-streaming)**

For synchronous text completion requests:

```
{
  "id": "cmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "text_completion",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "text": "Paris, the capital and most populous city of France.",
      "logprobs": {
        "tokens": ["Paris", ",", " the", " capital"],
        "token_logprobs": [-0.31725305, -0.07918124, -0.12345678, -0.23456789],
        "top_logprobs": [
          {
            "Paris": -0.31725305,
            "London": -1.3190403,
            "Rome": -2.1234567
          },
          {
            ",": -0.07918124,
            " is": -1.2345678
          }
        ]
      },
      "finish_reason": "stop",
      "stop_reason": null,
      "prompt_token_ids": [464, 6864, 315, 4881, 374],
      "token_ids": [3915, 11, 279, 6864, 323, 1455, 95551, 3363, 315, 4881, 13]
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 11,
    "total_tokens": 16,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  }
}
```

**Chat completion streaming response**

For streaming chat completion requests, responses are sent as Server-Sent Events (SSE):

```
data: {
  "id": "chatcmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "delta": {
        "role": "assistant",
        "content": "Hello",
        "refusal": null,
        "reasoning": null,
        "reasoning_content": null
      },
      "logprobs": {
        "content": [
          {
            "token": "Hello",
            "logprob": -0.31725305,
            "bytes": [72, 101, 108, 108, 111],
            "top_logprobs": [
              {
                "token": "Hello",
                "logprob": -0.31725305,
                "bytes": [72, 101, 108, 108, 111]
              }
            ]
          }
        ]
      },
      "finish_reason": null,
      "stop_reason": null
    }
  ],
  "usage": null,
  "prompt_token_ids": null
}

data: {
  "id": "chatcmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "delta": {
        "content": "! I'm"
      },
      "logprobs": null,
      "finish_reason": null,
      "stop_reason": null
    }
  ],
  "usage": null
}

data: {
  "id": "chatcmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "chat.completion.chunk",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "delta": {},
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  }
}

data: [DONE]
```

**Text completion streaming response**

For streaming text completion requests:

```
data: {
  "id": "cmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "text_completion",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "text": "Paris",
      "logprobs": {
        "tokens": ["Paris"],
        "token_logprobs": [-0.31725305],
        "top_logprobs": [
          {
            "Paris": -0.31725305,
            "London": -1.3190403
          }
        ]
      },
      "finish_reason": null,
      "stop_reason": null
    }
  ],
  "usage": null
}

data: {
  "id": "cmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "text_completion",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "text": ", the capital",
      "logprobs": null,
      "finish_reason": null,
      "stop_reason": null
    }
  ],
  "usage": null
}

data: {
  "id": "cmpl-123e4567-e89b-12d3-a456-426614174000",
  "object": "text_completion",
  "created": 1677652288,
  "model": "nova-micro-custom",
  "choices": [
    {
      "index": 0,
      "text": "",
      "finish_reason": "stop",
      "stop_reason": null
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 11,
    "total_tokens": 16
  }
}

data: [DONE]
```

**Response fields explanation**

- `id`: Unique identifier for the completion
- `object`: Type of object returned ("chat.completion", "text_completion", "chat.completion.chunk")
- `created`: Unix timestamp of when the completion was created
- `model`: Model used for the completion
- `choices`: Array of completion choices
- `usage`: Token usage information including prompt, completion, and total tokens
- `logprobs`: Log probability information for tokens (when requested)
- `finish_reason`: Reason why the model stopped generating ("stop", "length", "content_filter")
- `delta`: Incremental content in streaming responses
- `reasoning`: Reasoning content when reasoning_effort is used
- `token_ids`: Array of token IDs for the generated text

For complete API documentation, see [InvokeEndpoint API reference](../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.md "../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.md") and [InvokeEndpointWithResponseStream API reference](../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md "../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md").
