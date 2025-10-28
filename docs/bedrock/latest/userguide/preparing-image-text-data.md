# Prepare data for fine-tuning image and text processing models

###### Note

For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

For fine-tuning image-text-to-text models, each JSON object is a sample containing a conversation
structured as a `messages` array, consisting of alternating JSON objects representing the
user's inputs and the assistant's responses. User inputs can include both text and images, while
assistant responses are always textual. This structure supports both single-turn and multi-turn
conversational flows, enabling the model to handle diverse tasks effectively. Supported image formats
for Meta Llama-3.2 11B Vision Instruct and Meta Llama-3.2 90B Vision
Instruct include: `gif`, `jpeg`, `png`, and
`webp`.

To allow Amazon Bedrock access to the image files, add an IAM policy similar to the one in [Permissions to access training and validation files and to write output files in S3](model-customization-iam-role.md#model-customization-iam-role-s3 "model-customization-iam-role.md#model-customization-iam-role-s3") to the
Amazon Bedrock model customization service role that you set up or that was automatically set up for you in the
console. The Amazon S3 paths you provide in the training dataset must be in folders that you specify in the
policy.

**Single-turn conversations**

Each JSON object for single-turn conversations consists of a user message and an assistant message.
The user message includes a role field set to *user*and a
_content_ field containing an array with a `type` field
(_text_ or _image_) that describes the input modality. For
text inputs, the `content` field includes a `text` field with the user’s question
or prompt. For image inputs, the `content` field specifies the image `format` (for
example, _jpeg_, _png_) and its `source` with a
`uri` pointing to the Amazon S3 location of the image. The `uri` represents the
unique path to the image stored in an Amazon S3 bucket, typically in the format
`s3://<bucket-name>/<path-to-file>`. The assistant message includes a
`role` field set to _assistant_ and a `content` field
containing an array with a `type` field set to _text_ and a
`text` field containing the assistant’s generated response.

Example format

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [{
        "text": "You are a smart assistant that answers questions respectfully"
    }],
    "messages": [{
            "role": "user",
            "content": [{
                    "text": "What does the text in this image say?"
                },
                {
                    "image": {
                        "format": "png",
                        "source": {
                            "s3Location": {
                                "uri": "s3://your-bucket/your-path/your-image.png",
                                "bucketOwner": "your-aws-account-id"
                            }
                        }
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": [{
                "text": "The text in the attached image says 'LOL'."
            }]
        }
    ]
}
```

**Multi-turn conversations**

Each JSON object for multi-turn conversations contains a sequence of messages with alternating roles,
where user messages and assistant messages are structured consistently to enable coherent exchanges.
User messages include a `role` field set to _user_ and a
`content` field that describes the input modality. For text inputs, the
`content` field includes a `text` field with the user’s question or follow-up,
while for image inputs, it specifies the image `format` and its `source` with a
`uri` pointing to the Amazon S3 location of the image. The `uri` serves as a unique
identifier in the format s3://<bucket-name>/<path-to-file> and allows the model to access
the image from the designated Amazon S3 bucket. Assistant messages include a `role` field set to
_assistant_ and a `content` field containing an array with a
`type` field set to _text_ and a `text` field containing
the assistant’s generated response. Conversations can span multiple exchanges, allowing the assistant to
maintain context and deliver coherent responses throughout.

Example format

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [{
        "text": "You are a smart assistant that answers questions respectfully"
    }],
    "messages": [{
            "role": "user",
            "content": [{
                    "text": "What does the text in this image say?"
                },
                {
                    "image": {
                        "format": "png",
                        "source": {
                            "s3Location": {
                                "uri": "s3://your-bucket/your-path/your-image.png",
                                "bucketOwner": "your-aws-account-id"
                            }
                        }
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": [{
                "text": "The text in the attached image says 'LOL'."
            }]
        },
        {
            "role": "user",
            "content": [{
                    "text": "What does the text in this image say?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [{
                "text": "The text in the attached image says 'LOL'."
            }]
        }

    ]
}

```
