# Prepare data for fine-tuning your models

To prepare training and validation datasets for your custom model, you create `.jsonl` files, where each
line is a JSON object corresponding to a record. Before you can begin a model customization job, you
must at minimum prepare a training dataset. The files you create must conform to the format for the
customization method and model that you choose. The records in it must conform to size requirements depending
your model.

For information about model requirments, see [Model requirements for training and validation
datasets](#model-training-validation-requirements "#model-training-validation-requirements"). To see the
default quotas that apply for training and validation datasets used for customizing different models, see the
**Sum of training and validation records** quotas in [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") in the AWS General Reference.

Whether a validation dataset is supported and the format of your training and validation dataset depend on the
following factors.

- The type of fine-tuning customization job.
- The input and output modalities of the data.
  For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

The following sections describe the different fine-tuning capabilities supported by each
model, organized by their input and output modalities. For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

**Text-to-Text models**

Text-to-Text models can be fine-tuned for various text-based tasks, including both conversational and
non-conversational applications. For information about preparing data for fine-tuning Text-to-Text models, see [Prepare data for fine-tuning text-to-text models](#preparing-text-data "#preparing-text-data").

The following non-conversational models are optimized for tasks like summarization, translation, and
question answering:

- Amazon Titan Text G1 - Express
- Amazon Titan Text G1 - Lite
- Amazon Titan Text Premier
- Cohere Command
- Cohere Command Light
- Meta Llama 3.1 8B Instruct
- Meta Llama 3.1 70B Instruct
  The following conversational models are designed for single-turn and multi-turn interactions. If a model uses the Converse API, your fine-tuning dataset must follow the Converse API message format and include system,
  user, and assistant messages. For examples, see [Prepare data for fine-tuning text-to-text models](#preparing-text-data "#preparing-text-data"). For more information about Converse API operations, see [Carry out a conversation with the
  Converse API operations](conversation-inference.md "conversation-inference.md").

- Anthropic Claude 3 Haiku
- Meta Llama 3.2 1B Instruct (Converse API format)
- Meta Llama 3.2 3B Instruct (Converse API format)
- Meta Llama 3.2 11B Instruct Vision (Converse API format)
- Meta Llama 3.2 90B Instruct Vision (Converse API format)
- Meta Llama 3.3 70B Vision Instruct (Converse API format)
  **Text-Image-to-Text & Text-to-Image model**s

The following models support fine-tuning for image generation and text-image processing. These models
process or generate images based on textual input, or generate text based on both textual and image
inputs. For information about preparing data for fine-tuning Text-Image-to-Text & Text-to-Image models models, see [Prepare data for fine-tuning image and text processing models](#preparing-image-text-data "#preparing-image-text-data").

- Amazon Titan Image Generator G1 V1
- Meta Llama 3.2 11B Instruct Vision
- Meta Llama 3.2 90B Instruct Vision
- Meta Llama 3.3 70B Vision Instruct
  **Image-to-Embeddings**

The following models support fine-tuning for tasks like classification and retrieval. These models
generate numerical representations (embeddings) from image inputs. For information about preparing data for fine-tuning Image-to-Embeddings models, see [Prepare data for fine-tuning image generation and embedding
models](#preparing-image-generation-data "#preparing-image-generation-data").

- Amazon Titan Multimodal Embeddings G1
- Amazon Titan Image Generator G1 V1
  The following sections list the requirements for training and validation datasets for a model. For information
  about dataset constraints for Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

| Description                                                  | Maximum (Fine-tuning)       |
| ------------------------------------------------------------ | --------------------------- |
| Sum of input and output tokens when batch size is 1          | 4,096                       |
| Sum of input and output tokens when batch size is 2, 3, or 4 | N/A                         |
| Character quota per sample in dataset                        | Token quota x 6 (estimated) |
| Training dataset file size                                   | 1 GB                        |
| Validation dataset file size                                 | 100 MB                      |

| Description                                                  | Maximum (Fine-tuning)       |
| ------------------------------------------------------------ | --------------------------- |
| Sum of input and output tokens when batch size is 1          | 4,096                       |
| Sum of input and output tokens when batch size is 2, 3, or 4 | 2,048                       |
| Character quota per sample in dataset                        | Token quota x 6 (estimated) |
| Training dataset file size                                   | 1 GB                        |
| Validation dataset file size                                 | 100 MB                      |

| Description                                                     | Maximum (Fine-tuning)       |
| --------------------------------------------------------------- | --------------------------- |
| Sum of input and output tokens when batch size is 1 or 2        | 4,096                       |
| Sum of input and output tokens when batch size is 3, 4, 5, or 6 | 2,048                       |
| Character quota per sample in dataset                           | Token quota x 6 (estimated) |
| Training dataset file size                                      | 1 GB                        |
| Validation dataset file size                                    | 100 MB                      |

| Description                                          | Minimum (Fine-tuning) | Maximum (Fine-tuning) |
| ---------------------------------------------------- | --------------------- | --------------------- |
| Text prompt length in training sample, in characters | 3                     | 1,024                 |
| Records in a training dataset                        | 5                     | 10,000                |
| Input image size                                     | 0                     | 50 MB                 |
| Input image height in pixels                         | 512                   | 4,096                 |
| Input image width in pixels                          | 512                   | 4,096                 |
| Input image total pixels                             | 0                     | 12,582,912            |
| Input image aspect ratio                             | 1:4                   | 4:1                   |

| Description                                          | Minimum (Fine-tuning) | Maximum (Fine-tuning) |
| ---------------------------------------------------- | --------------------- | --------------------- |
| Text prompt length in training sample, in characters | 0                     | 2,560                 |
| Records in a training dataset                        | 1,000                 | 500,000               |
| Input image size                                     | 0                     | 5 MB                  |
| Input image height in pixels                         | 128                   | 4096                  |
| Input image width in pixels                          | 128                   | 4096                  |
| Input image total pixels                             | 0                     | 12,528,912            |
| Input image aspect ratio                             | 1:4                   | 4:1                   |

| Description                            | Minimum (Fine-tuning) | Maximum (Fine-tuning)                    |
| -------------------------------------- | --------------------- | ---------------------------------------- |
| Input tokens                           | 0                     | 16,000                                   |
| Output tokens                          | 0                     | 16,000                                   |
| Character quota per sample in dataset  | 0                     | Token quota x 6 (estimated)              |
| Sum of Input and Output tokens         | 0                     | 16,000                                   |
| Sum of training and validation records | 100                   | 10,000 (adjustable using service quotas) |

Supported image formats for Meta Llama-3.2 11B Vision Instruct and Meta
Llama-3.2 90B Vision Instruct include: `gif`, `jpeg`,
`png`, and `webp`. For estimating the image-to-token conversion during
fine-tuning of these models, you can use this formula as an approximation: `Tokens = min(2,
 max(Height // 560, 1)) * min(2, max(Width // 560, 1)) * 1601`. Images are converted
into approximately 1,601 to 6,404 tokens based on their size.

| Description                                                                  | Minimum (Fine-tuning) | Maximum (Fine-tuning)                    |
| ---------------------------------------------------------------------------- | --------------------- | ---------------------------------------- |
| Sum of Input and Output tokens                                               | 0                     | 16,000 (10000 for Meta Llama 3.2 90B)    |
| Sum of training and validation records                                       | 100                   | 10,000 (adjustable using service quotas) |
| Input image size for Meta Llama 11B and 90B instruct<br>models)              | 0                     | 10 MB                                    |
| Input image height in pixels for Meta Llama 11B and 90B<br>instruct models   | 10                    | 8192                                     |
| Input image width in pixels for Meta Llama 11B and 90B90B<br>instruct models | 10                    | 8192                                     |

| Description                            | Minimum (Fine-tuning) | Maximum (Fine-tuning)                    |
| -------------------------------------- | --------------------- | ---------------------------------------- |
| Sum of Input and output tokens         | 0                     | 16000                                    |
| Sum of training and validation records | 100                   | 10,000 (adjustable using Service Quotas) |

| Description                           | Maximum (Fine-tuning)       |
| ------------------------------------- | --------------------------- |
| Input tokens                          | 4,096                       |
| Output tokens                         | 2,048                       |
| Character quota per sample in dataset | Token quota x 6 (estimated) |
| Records in a training dataset         | 10,000                      |
| Records in a validation dataset       | 1,000                       |

| Description                     | Maximum (Fine-tuning)                    |
| ------------------------------- | ---------------------------------------- |
| Minimum number of records       | 32                                       |
| Maximum training records        | 10,000                                   |
| Maximum validation records      | 1,000                                    |
| Maximum total records           | 10,000 (adjustable using service quotas) |
| Maximum tokens                  | 32,000                                   |
| Maximum training dataset size   | 10 GB                                    |
| Maximum validation dataset size | 1 GB                                     |

###### Note

For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

For fine-tuning text-to-text models, each JSON object is a sample containing structured fields
designed to guide the model toward generating the desired textual output based on a provided textual
prompt. The data format varies depending on the use case, broadly categorized into non-conversational
and conversational use cases.

Non-conversational tasks
Non-conversational tasks involve generating a single output for a given input. Each dataset sample
includes a `prompt` field containing the input text and a `completion` field with
the expected output. This format supports a range of tasks such as question-answering, summarizing,
translation, text completion, and information extraction.

Example format

```
{"prompt": "What is the capital of France?", "completion": "The capital of France is Paris."}
{"prompt": "Summarize the article about climate change.", "completion": "Climate change refers to the long-term alteration of temperature and typical weather patterns in a place."}
```

Use approximately 6 characters per token to estimate the number of tokens for planning dataset
size.

Converse API format (Single turn and Multi turn)
To use the Converse API, you call the `Converse` or `ConverseStream` operations
to send messages to a model. To call `Converse`, you require permission for the
`bedrock:InvokeModel` operation. To call `ConverseStream`, you require
permission for the `bedrock:InvokeModelWithResponseStream` operation. For more information,
see [Using the Converse
API](conversation-inference-call.md "conversation-inference-call.md").
For more information about Converse API operations, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md")

Example format

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
                    "text": "What is the capital of Mars?"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "text": "Mars does not have a capital. Perhaps it will one day."
                }
            ]
        }
    ]
}
```

Anthropic Claude 3 Haiku: Single-turn conversations
Single-turn conversational tasks involve isolated exchanges, where the model generates a response
based solely on the current user input without considering prior context. Each dataset sample uses a
messages array, with alternating roles of `user` and `assistant`.

Format

```
{"system": "<system message>","messages":[{"role": "user", "content": "<user query>"},{"role": "assistant", "content": "<expected generated text>"}]}
```

Example

```
{"system": "You are an helpful assistant.","messages":[{"role": "user", "content": "what is AWS"},{"role": "assistant", "content": "it's Amazon Web Services."}]}
```

Anthropic Claude 3 Haiku: Multi-turn conversations
Multi-turn conversational tasks involve extended dialogues where the model must generate responses
while preserving the context of previous exchanges. This format captures the dynamic nature of
interactive tasks, such as customer support or complex discussions.

Format

```
{"system": "<system message>","messages":[{"role": "user", "content": "<user query 1>"},{"role": "assistant", "content": "<expected generated text 1>"}, {"role": "user", "content": "<user query 2>"},{"role": "assistant", "content": "<expected generated text 2>"}]}
```

Example

```
{"system": "system message","messages":[{"role": "user", "content": "Hello there."},{"role": "assistant", "content": "Hi, how can I help you?"},{"role": "user", "content": "what are LLMs?"},{"role": "assistant", "content": "LLM means large language model."},]}
```

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

###### Note

Amazon Nova models have different fine-tuning requirements. To fine-tune these models, follow the
instructions at [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

For text-to-image or image-to-embedding models, prepare a training dataset. Validation datasets are
not supported. Each JSON object is a sample containing an `image-ref`, the Amazon S3 URI for an
image, and a `caption` that could be a prompt for the image.

The images must be in JPEG or PNG format.

```
{"image-ref": "s3://bucket/path/to/image001.png", "caption": "<prompt text>"}
{"image-ref": "s3://bucket/path/to/image002.png", "caption": "<prompt text>"}{"image-ref": "s3://bucket/path/to/image003.png", "caption": "<prompt text>"}

```

The following is an example item:

```
{"image-ref": "s3://*amzn-s3-demo-bucket*/my-pets/cat.png", "caption": "an orange cat with white spots"}
```

To allow Amazon Bedrock access to the image files, add an IAM policy similar to the one in [Permissions to access training and validation files and to write output files in S3](model-customization-iam-role.md#model-customization-iam-role-s3 "model-customization-iam-role.md#model-customization-iam-role-s3") to the
Amazon Bedrock model customization service role that you set up or that was automatically set up for you in the
console. The Amazon S3 paths you provide in the training dataset must be in folders that you specify in the
policy.
