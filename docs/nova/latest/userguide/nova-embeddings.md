# Using Nova Embeddings

Amazon Nova Multimodal Embeddings is a state-of-the-art multimodal embeddings model for agentic
RAG and semantic search applications. It is the first unified embeddings model that supports
text, documents, images, video, and audio through a single model, to enable cross-modal
retrieval with leading accuracy. Nova Multimodal Embeddings maps each of these content types
into a unified semantic space enabling developers to conduct unimodal, cross-modal and
multimodal vector operations.

The Nova Embeddings API can be leveraged in a variety of applications, such as:

- Semantic Content Retrieval and Recommendation: Generate embeddings for your content, then use them to
  find similar items or provide personalized recommendations to your users.
- Multimodal Search: Combine embeddings from different content types to enable powerful cross-modal search
  capabilities.
- RAG: Generate embeddings from multimodal content such as documents with interleaved text and images to
  power your retrieval workflow for GenAI applications.

# Key Features

- Support for text, image, document image, video and audio in a unified semantic space.
  The maximum context length is 8K tokens or 30s of video and 30s of audio.
- Synchronous and asynchronous APIs: The API supports both synchronous and asynchronous use.
- Large file segmentation: The async API makes it easy to work with large inputs by providing API
  built segmentation for long text, video, and audio, controlled by user-defined parameters. The model will generate a single embedding for each segment.
- Video with audio: Process video with audio simultaneously. The API enables you to specify if you would like a single embedding representing both modalities or two separate embeddings representing the video and audio stream respectively.
- Embedding purpose: Nova Multimodal Embeddings enables you to optimize your embeddings depending on the intended downstream application. Supported use-cases include retrieval (RAG/Search), classification, and clustering. The specific values depend on the application (see best practices).
- Dimension sizes: 4 dimension sizes to trade-off embedding accuracy and vector storage cost:
  3072; 1024; 384; 256.
- Input methods: You can either pass content to be embed by specifying an S3 URI or inline as a base64 encoding.

# How Nova Multimodal Embeddings works

- When a piece of content is passed through Nova embeddings, the model converts that content
  into a universal numerical format, referred to as a vector. A vector is a set of arbitrary
  numerical values which can then be used for various search functionalities. Similar content
  is given a closer vector than less similar content. For example content that could be
  described as "happy" is given a vector closer to a vector like "joyful" as opposed to one
  like "sadness".

## Prerequisites

To use Multimodal Embeddings, you need the following:

- Python installed
- The AWS CLI Installed
- The AWS CLI configured with access credentials for your AWS account
- The Nova Multimodal Embeddings model enabled on your AWS Account

With these enabled, you can perform either asynchronous or synchronous embeddings requests.

## Generating embeddings synchronously

For smaller content items, you can use the Bedrock Runtime InvokeModel API. This is a good option for
quickly generating embeddings for text, images, or short audio/video files.

The following example generates a synchronous embedding for the text "Hello World!"

```
import json
import boto3

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

# Define the request body.
request_body = {
    "taskType": "SINGLE_EMBEDDING",
    "singleEmbeddingParams": {
        "embeddingPurpose": "GENERIC_INDEX",
        "embeddingDimension": 3072,
        "text": {"truncationMode": "END", "value": "Hello, World!"},
    },
}

try:
    # Invoke the Nova Embeddings model.
    response = bedrock_runtime.invoke_model(
        body=json.dumps(request_body, indent=2),
        modelId="amazon.nova-2-multimodal-embeddings-v1:0",
        accept="application/json",
        contentType="application/json",
    )

except Exception as e:
    # Add your own exception handling here.
    print(e)

# Print the request ID.
print("Request ID:", response.get("ResponseMetadata").get("RequestId"))

# Print the response body.
response_body = json.loads(response.get("body").read())
print(json.dumps(response_body, indent=2))
```

The output will look like this:

```

   Request ID: fde55db5-c129-423b-c62d-7a8b36cf2859
{
  "embeddings": [
    {
      "embeddingType": "TEXT",
      "embedding": [
        0.031115104,
        0.032478657,
        0.10006265,
        ...
      ]
    }
  ]
}

```

## Generating embeddings asynchronously

For larger content files, you can use the Bedrock Runtime StartAsyncInvoke function to generate embeddings
asynchronously. This allows you to submit a job and retrieve the results later, without blocking application
execution. Results are saved to Amazon S3.

The following example starts an asynchronous embedding generation job for a video file:

```
import boto3

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

model_input = {
    "taskType": "SEGMENTED_EMBEDDING",
    "segmentedEmbeddingParams": {
        "embeddingPurpose": "GENERIC_INDEX",
        "embeddingDimension": 3072,
        "video": {
            "format": "mp4",
            "embeddingMode": "AUDIO_VIDEO_COMBINED",
            "source": {
                "s3Location": {"uri": "s3://amzn-s3-demo-bucket/path/to/video.mp4"}
            },
            "segmentationConfig": {
                "durationSeconds": 15  # Segment into 15 second chunks
            },
        },
    },
}

try:
    # Invoke the Nova Embeddings model.
    response = bedrock_runtime.start_async_invoke(
        modelId="amazon.nova-2-multimodal-embeddings-v1:0",
        modelInput=model_input,
        outputDataConfig={
            "s3OutputDataConfig": {
                "s3Uri": "s3://amzn-s3-demo-bucket"
            }
        },
    )

except Exception as e:
    # Add your own exception handling here.
    print(e)

# Print the request ID.
print("Request ID:", response.get("ResponseMetadata").get("RequestId"))

# Print the invocation ARN.
print("Invocation ARN:", response.get("invocationArn"))
```

The output will look like this:

```

   Request ID: 07681e80-5ce0-4723-cf52-68bf699cd23e
   Invocation ARN: arn:aws:bedrock:us-east-1:`111122223333`:async-invoke/g7ur3b32a10n

```

After you start the async job, use the invocationArn to check the job status with the GetAsyncInvoke function. To view recent async invocations and their status, use the ListAsyncInvokes function.

When asynchronous embeddings generation is complete, artifacts are written to the S3 bucket you specified as the output
destination. The files will have the following structure:

```

   `amzn-s3-demo-bucket`/
    `job-id`/
        segmented-embedding-result.json
        embedding-audio.jsonl
        embedding-image.json
        embedding-text.jsonl
        embedding-video.jsonl
        manifest.json

```
