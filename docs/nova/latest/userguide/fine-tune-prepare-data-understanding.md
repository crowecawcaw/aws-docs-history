

# Preparing data for multimodal fine-tuning
<a name="fine-tune-prepare-data-understanding"></a>

**Important**  
Before you begin preparing your dataset, make sure supervised fine-tuning (SFT) is the right approach for your use case. SFT teaches the model new *behaviors*, response formats, and reasoning patterns. It does not teach the model new factual knowledge. If your primary goal is to introduce domain-specific facts, terminology, or knowledge the model hasn't seen, consider retrieval-augmented generation (RAG) to supply that context at inference time. For guidance on choosing between SFT, reinforcement fine-tuning (RFT), and RAG, see [Amazon Nova customization on SageMaker Training Jobs](nova-model-training-job.md).

The following are guidelines and requirements for preparing data for fine-tuning Understanding models:

1. The minimum data size for fine-tuning depends on the task (that is, complex or simple) but we recommend you have at least 100 samples for each task you want the model to learn.

1. We recommend using your optimized prompt in a zero-shot setting during both training and inference to achieve the best results.

1. Training and validation datasets must be JSONL files, where each line is a JSON object corresponding to a record. These file names can consist of only alphanumeric characters, underscores, hyphens, slashes, and dots.

1. Image and video constraints

   1. Dataset can't contain different media modalities. That is, the dataset can either be text with images or text with videos.

   1. One sample (single record in messages) can have multiple images

   1. One sample (single record in messages) can have only 1 video

1. `schemaVersion` can be any string value

1. The (*optional*) `system` turn can be a customer-provided custom system prompt.

1. Supported roles are `user` and `assistant`.

1. The first turn in `messages` should always start with `"role": "user"`. The last turn is the bot's response, denoted by `"role": "assistant"`.

1. The `image.source.s3Location.uri` and `video.source.s3Location.uri` must be accessible to Amazon Bedrock.

1.  Your Amazon Bedrock service role must be able to access the image files in Amazon S3. For more information about granting access, see [Create a service role for model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html) 

1. The images or videos must be in the same Amazon S3 bucket as your dataset. For example, if your dataset is in `s3://amzn-s3-demo-bucket/train/train.jsonl`, then your images or videos must be in `s3://amzn-s3-demo-bucket`

1. The terms `User:`, `Bot:`, `Assistant:`, `System:`, `<image>`, `<video>`, and `[EOS]` are reserved keywords. If a user prompt or system prompt starts with any of these keywords, or has these keywords anywhere in the prompt, your training job will fail due to data issues. If you need to use these keywords for your use case, you must substitute them for different keywords with similar meanings so that your training can proceed.

**Note**  
To validate your dataset before submitting a fine-tuning job, you can use the [dataset validation script](https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/bedrock-finetuning/understanding/dataset_validation) available on GitHub.

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

**Topics**
+ [Designing effective training examples](#designing-effective-training-examples)
+ [Example dataset formats](#customize-fine-tune-examples)
+ [Dataset constraints](#custom-fine-tune-constraints)

## Example dataset formats
<a name="customize-fine-tune-examples"></a>

The following example dataset formats provide a guide for you to follow.

### Text-only custom fine tuning format
<a name="example4"></a>

The following example is for custom fine tuning over text only.

```
// train.jsonl
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

### Single image custom fine tuning format
<a name="example1"></a>

The following example is for custom fine tuning over text and a single image.

```
// train.jsonl{
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
                                "uri": "s3://{{your-bucket/your-path/your-image.png}}",
                                "bucketOwner": "{{your-aws-account-id}}"
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

### Video custom fine tuning format
<a name="example3"></a>

The following example is for custom fine tuning over text and video.

```
{
    "schemaVersion": "bedrock-conversation-2024",
    "system": [{
        "text": "You are a helpful assistant designed to answer questions crisply and to the point"
    }],
    "messages": [{
            "role": "user",
            "content": [{
                    "text": "How many white items are visible in this video?"
                },
                {
                    "video": {
                        "format": "mp4",
                        "source": {
                            "s3Location": {
                                "uri": "s3://{{your-bucket/your-path/your-video.mp4}}",
                                "bucketOwner": "{{your-aws-account-id}}"
                            }
                        }
                    }
                }
            ]
        },
        {
            "role": "assistant",
            "content": [{
                "text": "There are at least eight visible items that are white"
            }]
        }
    ]
}
```

## Dataset constraints
<a name="custom-fine-tune-constraints"></a>

Amazon Nova applies the following constraints on model customizations for Understanding models.


| Model | Minimum Samples | Maximum Samples | Context Length | 
| --- |--- |--- |--- |
| Amazon Nova Micro | 8 | 20k | 32k | 
| Amazon Nova Lite | 8 | 20k | 32k | 
| Amazon Nova Pro | 8 | 20k | 32k | 


**Image and video constraints**  

|  |  | 
| --- |--- |
| Maximum images | 10/sample | 
| Maximum image file size | 10 MB | 
| Maximum videos | 1/sample | 
| Maximum video length/duration | 90 seconds | 
| Maximum video file size | 50 MB | 

**Supported media formats**
+ Image - `png`, `jpeg`, `gif`, `webp`
+ Video - `mov`, `mkv`, `mp4`, `webm`