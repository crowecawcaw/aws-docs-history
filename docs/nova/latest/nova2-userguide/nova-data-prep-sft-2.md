

# Preparing data for SFT on Amazon Nova 2
<a name="nova-data-prep-sft-2"></a>

SFT on Amazon Nova 2 supports text, image, video, and document understanding, as well as tool calling, with or without reasoning support. This page describes the constraints, supported formats, and best practices for preparing SFT training data for Amazon Nova 2 Understanding models.

**Tip**  
To validate your dataset format before starting a training job, see [Validation tools](nova-data-preparation.md#nova-data-validation-tools).

**Topics**
+ [Data format](#nova-2-data-overview)
+ [Sample inputs](#nova-2-data-examples)
+ [Supported features](#nova-2-supported-features)
+ [General/Text understanding](#sft-general-constraints)
+ [Image understanding](#sft-image-understanding)
+ [Video understanding](#sft-video-understanding)
+ [Document understanding](#sft-document-understanding)
+ [Tool calling](#sft-tool-calling)
+ [Reasoning](#sft-reasoning)
+ [Designing effective training examples](#designing-effective-training-examples)

## Data format
<a name="nova-2-data-overview"></a>

Amazon Nova 2 SFT data uses the same [Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html) format as Amazon Nova 1, with the addition of optional [reasoning content](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ReasoningContentBlock.html) fields.

Each line in your JSONL training file is a JSON object with the following top-level fields. Expand a section to learn more:

### messages
<a name="sft-field-messages"></a>

Required. The `messages` field is an array of message objects, each of which defines a turn in the conversation. A message object contains the following fields:
+ **role** – Required. Defines whether the message is from the `user` (the prompt sent to the model) or `assistant` (the model response). The first turn must be `user`, the last must be `assistant`, and turns must alternate.
+ **content** – Required. An array of content blocks for this turn.

The `content` field maps to an array of content blocks. Amazon Nova 2 SFT data support the following blocks:

------
#### [ text ]

A string specifying text content. Supported in both `user` and `assistant` turns.

The following shows an example message object with a `content` array containing only a `text` content block:

```
{
    "role": "user",
    "content": [
        {
            "text": "{{string}}"
        }
    ]
}
```

------
#### [ image ]

An image object specifying its format and S3 location. Supported only in `user` turns.

The following shows an example message object with a content array containing only an image content block:

```
{
    "role": "user",
    "content": [
        {
            "image": {
                "format": "jpeg",
                "source": {
                    "s3Location": {
                        "uri": "s3://{{your-bucket}}/{{your-image.jpg}}",
                        "bucketOwner": "{{account-id}}"
                    }
                }
            }
        }
    ]
}
```

------
#### [ video ]

A video object specifying its format and S3 location. Supported only in `user` turns.

The following shows an example message object with a content array containing only a video content block:

```
{
    "role": "user",
    "content": [
        {
            "video": {
                "format": "mp4",
                "source": {
                    "s3Location": {
                        "uri": "s3://{{your-bucket}}/{{your-video.mp4}}",
                        "bucketOwner": "{{account-id}}"
                    }
                }
            }
        }
    ]
}
```

------
#### [ document ]

A document object specifying its format and S3 location. Supported only in `user` turns.

The following shows an example message object with a content array containing only a document content block:

```
{
    "role": "user",
    "content": [
        {
            "document": {
                "format": "pdf",
                "source": {
                    "s3Location": {
                        "uri": "s3://{{your-bucket}}/{{your-document.pdf}}",
                        "bucketOwner": "{{account-id}}"
                    }
                }
            }
        }
    ]
}
```

------
#### [ reasoningContent ]

A reasoning trace object. Supported only in `assistant` turns. Only text-based reasoning is supported; image-based reasoning content is not supported.

The following shows an example message object with a content array containing only a reasoning content block:

```
{
    "role": "assistant",
    "content": [
        {
            "reasoningContent": {
                "reasoningText": {
                    "text": "{{string}}"
                }
            }
        },
        {
            "text": "{{final answer}}"
        }
    ]
}
```

------
#### [ toolUse ]

A tool invocation object. Supported only in `assistant` turns. The `toolUseId` must be unique per conversation and the `name` must match a tool defined in `toolConfig`.

The following shows an example message object with a content array containing only a tool use content block:

```
{
    "role": "assistant",
    "content": [
        {
            "toolUse": {
                "toolUseId": "{{unique-id}}",
                "name": "{{tool-name}}",
                "input": { {{...}} }
            }
        }
    ]
}
```

------
#### [ toolResult ]

A tool result object. Supported only in `user` turns. Each `toolUseId` must reference a preceding `toolUse` and be used exactly once. Content must be text or JSON only.

The following shows an example message object with a content array containing only a tool result content block:

```
{
    "role": "user",
    "content": [
        {
            "toolResult": {
                "toolUseId": "{{matching-id}}",
                "content": [
                    {
                        "text": "{{result}}"
                    }
                ]
            }
        }
    ]
}
```

------

### system
<a name="sft-field-system"></a>

An optional array that defines a system prompt — instructions or context for the model about the task it should perform or the persona it should adopt. Use the same system prompt during both training and inference for best results.

```
"system": [
    {
        "text": "{{You are a helpful assistant.}}"
    }
]
```

### toolConfig
<a name="sft-field-toolconfig"></a>

An optional object that defines the tools available for the model to use during the conversation. Each tool is defined with a name, description, and a JSON Schema for its input parameters.

```
"toolConfig": {
    "tools": [
        {
            "toolSpec": {
                "name": "{{tool-name}}",
                "description": "{{tool-description}}",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "{{param}}": {
                                "type": "string",
                                "description": "{{param-description}}"
                            }
                        },
                        "required": ["{{param}}"]
                    }
                }
            }
        }
    ]
}
```

### schemaVersion
<a name="sft-field-schemaversion"></a>

Required. A string field identifying the schema version. Can be any string value.

```
"schemaVersion": "bedrock-conversation-2024"
```

**Validating your data**

Before submitting your training job, validate your dataset to catch formatting issues early. For available validation tools, see [Validation tools](nova-data-preparation.md#nova-data-validation-tools).

## Sample inputs
<a name="nova-2-data-examples"></a>

The following are complete example JSON objects showing how to combine the fields and content blocks for different modalities.

------
#### [ Text-only (Nova 1.0 compatible) ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are a digital assistant with a friendly personality"
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What country is right next to Australia?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "The closest country is New Zealand"
                }
            ]
        }
    ]
}
```

------
#### [ Image \+ text input ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are a helpful assistant."
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "image": {
                        "format": "jpeg",
                        "source": {
                            "s3Location": {
                                "uri": "s3://your-bucket/your-path/your-image.jpg",
                                "bucketOwner": "your-aws-account-id"
                            }
                        }
                    }
                },
                {
                    "text": "Which country is highlighted in the image?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "I will determine the highlighted country by examining its location on the map and using my geographical knowledge"
                        }
                    }
                },
                {
                    "text": "The highlighted country is New Zealand"
                }
            ]
        }
    ]
}
```

------
#### [ Video \+ text input ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are a helpful assistant."
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "video": {
                        "format": "mp4",
                        "source": {
                            "s3Location": {
                                "uri": "s3://your-bucket/your-path/your-video.mp4",
                                "bucketOwner": "your-aws-account-id"
                            }
                        }
                    }
                },
                {
                    "text": "What is shown in this video?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "I will analyze the video content to identify key elements"
                        }
                    }
                },
                {
                    "text": "The video shows a map with New Zealand highlighted"
                }
            ]
        }
    ]
}
```

------
#### [ Document \+ text input ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What are the ways in which a customer can experience issues during checkout on Amazon?"
                },
                {
                    "document": {
                        "format": "pdf",
                        "source": {
                            "s3Location": {
                                "uri": "s3://my-bucket-name/path/to/documents/customer_service_debugging.pdf",
                                "bucketOwner": "123456789012"
                            }
                        }
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "I need to find the relevant section in the document to answer the question."
                        }
                    }
                },
                {
                    "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
                }
            ]
        }
    ]
}
```

------
#### [ Text with tool calling ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are an expert in composing function calls."
        }
    ],
    "toolConfig": {
        "tools": [
            {
                "toolSpec": {
                    "name": "getItemAvailability",
                    "description": "Retrieve whether an item is available in a given location",
                    "inputSchema": {
                        "json": {
                            "type": "object",
                            "properties": {
                                "zipcode": {
                                    "type": "string",
                                    "description": "The zipcode of the location to check in"
                                },
                                "quantity": {
                                    "type": "integer",
                                    "description": "The number of items to check availability for"
                                },
                                "item_id": {
                                    "type": "string",
                                    "description": "The ASIN of item to check availability for"
                                }
                            },
                            "required": ["item_id", "zipcode"]
                        }
                    }
                }
            }
        ]
    },
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "I need to check whether there are twenty pieces of the following item available. Here is the item ASIN on Amazon: id-123. Please check for the zipcode 94086"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "The user wants to check how many pieces of the item with ASIN id-123 are available in the zipcode 94086"
                        }
                    }
                },
                {
                    "toolUse": {
                        "toolUseId": "getItemAvailability_0",
                        "name": "getItemAvailability",
                        "input": {
                            "zipcode": "94086",
                            "quantity": 20,
                            "item_id": "id-123"
                        }
                    }
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "toolResult": {
                        "toolUseId": "getItemAvailability_0",
                        "content": [
                            {
                                "text": "[{\"name\": \"getItemAvailability\", \"results\": {\"availability\": true}}]"
                            }
                        ]
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "Yes, there are twenty pieces of item id-123 available at 94086. Would you like to place an order or know the total cost?"
                }
            ]
        }
    ]
}
```

------
#### [ Text with reasoning ]

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [
        {
            "text": "You are a digital assistant with a friendly personality"
        }
    ],
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "text": "What country is right next to Australia?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "I need to use my world knowledge of geography to answer this question"
                        }
                    }
                },
                {
                    "text": "The closest country to Australia is New Zealand, located to the southeast across the Tasman Sea."
                }
            ]
        }
    ]
}
```

------

## Supported features
<a name="nova-2-supported-features"></a>

The following table compares feature support for SFT across Nova model versions.


**SFT feature support by model version**  

| Feature | SFT on Nova 2.0 | 
| --- | --- | 
| Text understanding | Supported on Nova 2.0 Lite. See [General/Text understanding](#sft-general-constraints). | 
| Image understanding | Supported on Nova 2.0 Lite. See [Image understanding](#sft-image-understanding). | 
| Video understanding | Supported on Nova 2.0 Lite. See [Video understanding](#sft-video-understanding). | 
| Document understanding | Supported on Nova 2.0 Lite. See [Document understanding](#sft-document-understanding). | 
| Tool calling | Supported on Nova 2.0 Lite. See [Tool calling](#sft-tool-calling). | 
| Reasoning | Supported on Nova 2.0 Lite. See [Reasoning](#sft-reasoning). | 

## General/Text understanding
<a name="sft-general-constraints"></a>

This section summarizes the general constraints for preparing SFT on Amazon Nova 2 training data.

**Constraints**


**General dataset constraints**  

| Constraint | Details | 
| --- | --- | 
| Dataset format | JSONL (one JSON object per line). File names can consist of only alphanumeric characters, underscores, hyphens, slashes, and dots. | 
| Minimum samples | 8 | 
| Maximum samples | 20k | 
| Context length | 32k | 
| Dataset homogeneity | A dataset cannot mix different media modalities. Use text with images, text with videos, or text with documents — but not a combination. | 
| Reserved keywords | User:, Bot:, Assistant:, System:, <image>, <video>, [EOS]. Prompts containing these keywords will cause the training job to fail. Substitute them for different keywords with similar meanings. | 

**Best practices**
+ The minimum data size for fine-tuning depends on the task (that is, complex or simple) but we recommend you have at least 200 samples for each task you want the model to learn.
+ We recommend using your optimized prompt in a zero-shot setting during both training and inference to achieve the best results.
+ Prioritize quality over quantity. A few hundred high-quality, consistent examples typically outperform thousands of noisy or contradictory ones.

**Sample input**
+ `schemaVersion` can be any string value
+ Supported roles are `user` and `assistant`. The (*optional*) `system` turn can be a customer-provided custom system prompt.
+ The first turn in `messages` should always start with `"role": "user"`. The last turn is the bot's response, denoted by `"role": "assistant"`.

### Text-only sample
<a name="sft-general-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a digital assistant with a friendly personality"
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What country is right next to Australia?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "The closest country is New Zealand"
        }
      ]
    }
  ]
}
```

## Image understanding
<a name="sft-image-understanding"></a>

SFT supports training on image-based tasks, enabling your model to learn how to analyze and respond to questions about images.

**Constraints**


**Image constraints**  

| Constraint | Details | 
| --- | --- | 
| Supported formats | PNG, JPEG, GIF, WebP | 
| Maximum images per sample | 10 | 
| Maximum image file size | 10 MB | 
| Dataset homogeneity | A sample can have images and text, but cannot have images combined with other modalities (videos, documents). | 
| S3 location | The image.source.s3Location.uri must be in the same Amazon S3 bucket as your dataset. For example, if your dataset is in s3://amzn-s3-demo-bucket/train/train.jsonl, then your images or videos must be in s3://amzn-s3-demo-bucket | 

**Best practices**
+ Ensure images are high quality and relevant to the task.
+ Provide diverse examples covering different image types and question formats.
+ Include clear questions that reference specific aspects of the image content.

**Sample input**

### Image \+ text sample
<a name="sft-image-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a helpful assistant."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "image": {
            "format": "jpeg",
            "source": {
              "s3Location": {
                "uri": "s3://your-bucket/your-path/your-image.jpg",
                "bucketOwner": "your-aws-account-id"
              }
            }
          }
        },
        {
          "text": "Which country is highlighted in the image?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "The highlighted country is New Zealand"
        }
      ]
    }
  ]
}
```

## Video understanding
<a name="sft-video-understanding"></a>

SFT supports training on video-based tasks, enabling your model to learn how to analyze and respond to questions about video content.

**Constraints**


**Video constraints**  

| Constraint | Details | 
| --- | --- | 
| Supported formats | MOV, MKV, MP4, WebM | 
| Maximum videos per sample | 1 | 
| Maximum video file size | 50 MB | 
| Maximum video duration | 15 minutes | 
| Dataset homogeneity | A sample can have video and text, but cannot have video combined with other modalities (images, documents). | 
| S3 location | The video.source.s3Location.uri must be in the same Amazon S3 bucket as your dataset. For example, if your dataset is in s3://amzn-s3-demo-bucket/train/train.jsonl, then your videos must be in s3://amzn-s3-demo-bucket | 

**Best practices**
+ Keep videos concise and focused on the content relevant to your task.
+ Ensure video quality is sufficient for the model to extract meaningful information.
+ Provide clear questions that reference specific aspects of the video content.
+ Include diverse examples covering different video types and question formats.

**Sample input**

### Video \+ text sample
<a name="sft-video-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What are the ways in which a customer can experience issues during checkout on Amazon?"
        },
        {
          "video": {
            "format": "mp4",
            "source": {
              "s3Location": {
                "uri": "s3://my-bucket-name/path/to/videos/customer_service_debugging.mp4",
                "bucketOwner": "123456789012"
              }
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ]
    }
  ]
}
```

## Document understanding
<a name="sft-document-understanding"></a>

SFT supports training on document-based tasks, enabling your model to learn how to analyze and respond to questions about PDF documents.

**Constraints**


**Document constraints**  

| Constraint | Details | 
| --- | --- | 
| Supported format | PDF | 
| Maximum document size | 10 MB | 
| Dataset homogeneity | A sample can have documents and text, but cannot have documents mixed with other modalities (images, videos). | 
| S3 location | The document.source.s3Location.uri must be in the same Amazon S3 bucket as your dataset. For example, if your dataset is in s3://amzn-s3-demo-bucket/train/train.jsonl, then your documents must be in s3://amzn-s3-demo-bucket | 

**Best practices**
+ Ensure documents are clearly formatted and text is extractable.
+ Provide diverse examples covering different document types and question formats.
+ Include reasoning content to help the model learn document analysis patterns.

**Sample input**

### Document \+ text sample
<a name="sft-document-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What are the ways in which a customer can experience issues during checkout on Amazon?"
        },
        {
          "document": {
            "format": "pdf",
            "source": {
              "s3Location": {
                "uri": "s3://my-bucket-name/path/to/documents/customer_service_debugging.pdf",
                "bucketOwner": "123456789012"
              }
            }
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Customers can experience issues with 1. Data entry, 2. Payment methods, 3. Connectivity while placing the order. Which one would you like to dive into?"
        }
      ]
    }
  ]
}
```

## Tool calling
<a name="sft-tool-calling"></a>

SFT supports training models on tool calling patterns, enabling your model to learn when and how to invoke external tools or functions.

**Constraints**


**Tool calling constraints**  

| Constraint | Details | 
| --- | --- | 
| Supported formats | Text or JSON for ToolResult content | 
| ToolUse placement | ToolUse must appear in assistant turns only | 
| ToolResult placement | ToolResult must appear in user turns only | 
| inputSchema format | The inputSchema within the toolSpec must be a valid JSON Schema object | 
| toolUseId matching | Each ToolResult must reference a valid toolUseId from a preceding assistant ToolUse, with each toolUseId used exactly once per conversation | 

**Best practices**
+ Ensure your tool definitions are consistent across all training samples.
+ The model learns tool invocation patterns from the demonstrations you provide.
+ Include diverse examples of when to use each tool and when not to use tools.

**Sample input**

### Text with tool calling sample
<a name="sft-tool-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are an expert in composing function calls."
    }
  ],
  "toolConfig": {
    "tools": [
      {
        "toolSpec": {
          "name": "getItemAvailability",
          "description": "Retrieve whether an item is available in a given location",
          "inputSchema": {
            "json": {
              "type": "object",
              "properties": {
                "zipcode": {
                  "type": "string",
                  "description": "The zipcode of the location to check in"
                },
                "quantity": {
                  "type": "integer",
                  "description": "The number of items to check availability for"
                },
                "item_id": {
                  "type": "string",
                  "description": "The ASIN of item to check availability for"
                }
              },
              "required": ["item_id", "zipcode"]
            }
          }
        }
      }
    ]
  },
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "I need to check whether there are twenty pieces of the following item available. Here is the item ASIN on Amazon: id-123. Please check for the zipcode 94086"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "toolUse": {
            "toolUseId": "getItemAvailability_0",
            "name": "getItemAvailability",
            "input": {
              "zipcode": "94086",
              "quantity": 20,
              "item_id": "id-123"
            }
          }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "toolResult": {
            "toolUseId": "getItemAvailability_0",
            "content": [
              {
                "text": "[{\"name\": \"getItemAvailability\", \"results\": {\"availability\": true}}]"
              }
            ]
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Yes, there are twenty pieces of item id-123 available at 94086. Would you like to place an order or know the total cost?"
        }
      ]
    }
  ]
}
```

## Reasoning
<a name="sft-reasoning"></a>

Reasoning content (also called chain-of-thought) captures the model's intermediate thinking steps before generating a final answer.

**Constraints**


**Reasoning constraints**  

| Constraint | Details | 
| --- | --- | 
| Supported format | Text only. Image-based reasoning content is not supported. | 
| Placement | Assistant turns only, via the reasoningContent field. | 
| Formatting | Use plain text. Avoid markup tags like <thinking> and </thinking> unless specifically required by your task. | 

**Best practices**
+ High-quality reasoning content should include intermediate thoughts, logical deductions, step-by-step problem-solving approaches, and explicit connections between steps and conclusions.
+ You can include `reasoningContent` across multiple assistant turns in multi-turn conversations.
+ If your dataset lacks reasoning traces, you can create them using a reasoning-capable model like Nova Premier.

**Sample input**

### Text with reasoning sample
<a name="sft-reasoning-sample"></a>

```
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a digital assistant with a friendly personality"
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What country is right next to Australia?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "reasoningContent": {
            "reasoningText": {
              "text": "I need to use my world knowledge of geography to answer this question"
            }
          }
        },
        {
          "text": "The closest country to Australia is New Zealand, located to the southeast across the Tasman Sea."
        }
      ]
    }
  ]
}
```

**Additional notes**

How loss is calculated:
+ **With reasoning content** – Training loss includes both reasoning tokens and final output tokens.
+ **Without reasoning content** – Training loss is calculated only on the final output tokens.

Set `reasoning_enabled: true` in your training configuration when your training data has reasoning tokens, you want the model to generate thinking tokens before producing final outputs, or you need improved performance on complex reasoning tasks.

Set `reasoning_enabled: false` when your training data does not have reasoning tokens, you're training on straightforward tasks that don't benefit from explicit reasoning steps, or you want to optimize for speed and reduce token usage.

Training Nova on a non-reasoning dataset with `reasoning_enabled = true` is permitted. However, doing so may cause the model to lose its reasoning capabilities, as Nova primarily learns to generate the responses presented in the data without applying reasoning. In general, enable reasoning for both training and inference when using reasoning datasets, and disable it for both when using non-reasoning datasets.

## Designing effective training examples
<a name="designing-effective-training-examples"></a>

Your training data should demonstrate the *behavior* you want the model to exhibit. SFT teaches the model *how* to respond, not *what* to know. If you find yourself creating training examples primarily to inject factual knowledge (for example, "What does error code E-45 mean?" with the answer "E-45 indicates a sensor timeout"), consider whether RAG or prompt engineering could achieve the same result without fine-tuning.

When converting source data into the conversational format, follow these principles:

1. **Start from real user queries.** Write user turns that mirror how end users will actually prompt the model in production. Avoid artificial or overly simplified questions that don't reflect real usage patterns.

1. **Write gold-standard assistant responses.** Each assistant turn should be the ideal response you want the model to produce — correct, well-formatted, and consistent in tone and structure across all examples.

1. **Use the system prompt strategically.** Place persistent instructions such as output format, persona, and domain context in the system turn. Use the same system prompt during both training and inference to achieve the best results.

1. **Keep examples focused on one skill per sample.** If you need the model to classify, answer questions, and summarize, create separate example sets for each skill rather than combining multiple skills in a single sample.

1. **Prioritize quality over quantity.** A few hundred high-quality, consistent examples typically outperform thousands of noisy or contradictory ones. Deduplicate and review your data before training.

### Common data transformation patterns
<a name="common-data-transformation-patterns"></a>

The following patterns illustrate how to convert common enterprise data formats into effective SFT training examples.

**Pattern 1: Structured records to classification or lookup**  
When your source data is a table or database of records with fields such as `issue`, `cause`, and `resolution`, frame each record as a user question with the relevant input fields and the assistant response as the target output fields.

```
// train.jsonl
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a technical support assistant. Given an issue description, identify the most likely root cause and recommended resolution."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "A user reports: 'Application crashes on startup after the latest update.' What is the likely cause and resolution?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Cause: Incompatible configuration file from the previous version.\nResolution: Delete the local configuration cache and restart the application to regenerate default settings."
        }
      ]
    }
  ]
}
```

**Pattern 2: Hierarchical or taxonomy data to structured Q&A**  
When your source data is a code hierarchy or taxonomy such as product category trees or classification systems, generate questions that ask the model to navigate the hierarchy. Include the classification context in the system prompt or user turn.

```
// train.jsonl
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are a product catalog assistant. Answer questions about product categories and classifications accurately."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "What top-level category does product code 'EL-4520' belong to, and what subcategories does it include?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Product code EL-4520 belongs to the Electronics category. It includes the subcategories: Audio Equipment, Portable Speakers, and Wireless Accessories."
        }
      ]
    }
  ]
}
```

**Pattern 3: Procedural documents to instructional dialog**  
When your source data consists of standard operating procedures, runbooks, or step-by-step guides, convert procedures into task-oriented questions. The user asks how to perform a task and the assistant provides the steps in a consistent format.

```
// train.jsonl
{
  "schemaVersion": "bedrock-conversation-2024",
  "system": [
    {
      "text": "You are an IT operations assistant. Provide step-by-step instructions based on approved runbooks and standard operating procedures."
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "text": "How do I reset a user's multi-factor authentication when they have lost access to their device?"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "text": "Follow these steps to reset a user's multi-factor authentication:\n1. Verify the user's identity using the approved verification procedure.\n2. Disable the existing MFA configuration in the identity management console.\n3. Generate a new temporary access code and send it to the user's verified email.\n4. Instruct the user to log in with the temporary code and re-enroll their new device.\n5. Confirm the new MFA device is working by requesting a test authentication.\n6. Document the reset in the support ticket."
        }
      ]
    }
  ]
}
```

**Note**  
In Patterns 1 and 2, if the factual content (such as codes, categories, or resolutions) is not already in the model's pre-training data, consider using RAG to supply this information at inference time rather than relying solely on SFT to memorize it. SFT is most effective for teaching the model the response format and reasoning pattern, while RAG handles the factual grounding.