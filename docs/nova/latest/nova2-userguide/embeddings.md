# Using Amazon Nova embeddings

Amazon Nova Multimodal Embeddings is a multimodal embeddings model for agentic RAG and
semantic search applications. It supports text, documents, images, video and audio
through a single model, enabling cross-modal retrieval. Nova Multimodal Embeddings maps
each of these content types into a unified semantic space, enabling you to conduct
unimodal, cross-modal and multimodal vector operations.

When a piece of content is passed through Nova embeddings, the model converts that
content into a universal numerical format, referred to as a vector. A vector is a set of
numerical values that can be used for various search functionalities. Similar content is
given a closer vector than less similar content.

Applications:

- Semantic Content Retrieval and Recommendation: Generate embeddings for your
  content, then use them to find similar items or provide personalized
  recommendations.
- Multimodal Search: Combine embeddings from different content types to enable
  cross-modal search capabilities.
- RAG: Generate embeddings from multimodal content such as documents with
  interleaved text and images to power your retrieval workflow for GenAI
  applications.

## Key features

These eky features distinguish Nova Embeddings:

- Support for text, image, document image, video, and audio in a unified
  semantic space. Maximum context length is 8K tokens or 30s of video and
  30s of audio.
- Synchronous and asynchronous APIs: The API supports both synchronous and
  asynchronous use.
- Large file segmentation: The async API makes it easy to work with large
  inputs by providing API built segmentation for long text, video, and audio,
  controlled by user-defined parameters. The model will generate a single
  embedding for each segment.
- Video with audio: Process video with audio simultaneously. Specify if you would like a single embedding representing both modalities or two separate embeddings.
- Embedding purpose: Optimize your embeddings depending on the intended downstream application (retrieval/RAG/Search, classification, clustering).
- Dimension sizes: 4 dimension sizes to trade-off embedding accuracy and
  vector storage cost: 3072; 1024; 384; 256.
- Input methods: Pass content to be embedded by specifying an S3 URI or inline as a base64 encoding.

## Generating embeddings

Complete the following to generate embeddings.

Synchronous embedding for text:

```
import boto3
import json

# Create the Bedrock Runtime client.
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
)

# Define the request body.
request_body = {
    'taskType': 'SINGLE_EMBEDDING',
    'singleEmbeddingParams': {
        'embeddingPurpose': 'GENERIC_INDEX',
        'embeddingDimension': 3072,
        'text': {'truncationMode': 'END', 'value': 'Hello, World!'},
    },
}

try:
    # Invoke the Nova Embeddings model.
    response = bedrock_runtime.invoke_model(
        body=json.dumps(request_body, indent=2),
        modelId='amazon.nova-2-multimodal-embeddings-v1:0',
        accept='application/json',
        contentType='application/json',
    )

except Exception as e:
    # Add your own exception handling here.
    print(e)

# Print the request ID.
print('Request ID:', response.get('ResponseMetadata').get('RequestId'))

# Print the response body.
response_body = json.loads(response.get('body').read())
print(json.dumps(response_body, indent=2))
```

try:

```
response = bedrock_runtime.invoke_model(
        body=json.dumps(request_body, indent=2),
        modelId='amazon.nova-2-multimodal-embeddings-v1:0',
        accept='application/json',
        contentType='application/json',
    )
except Exception as e:
    print(e)

print('Request ID:', response.get('ResponseMetadata').get('RequestId'))
response_body = json.loads(response.get('body').read())
print(json.dumps(response_body, indent=2))

```

Asynchronous embedding for video:

```
 import boto3

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
)

model_input = {
    'taskType': 'SEGMENTED_EMBEDDING',
    'segmentedEmbeddingParams': {
        'embeddingPurpose': 'GENERIC_INDEX',
        'embeddingDimension': 3072,
        'video': {
            'format': 'mp4',
            'embeddingMode': 'AUDIO_VIDEO_COMBINED',
            'source': {
                's3Location': {'uri': 's3://my-bucket/path/to/video.mp4'}
            },
            'segmentationConfig': {
                'durationSeconds': 15  # Segment into 15 second chunks
            },
        },
    },
}

```

try:

```
response = bedrock_runtime.start_async_invoke(
        modelId='amazon.nova-2-multimodal-embeddings-v1:0',
        modelInput=model_input,
        outputDataConfig={
            's3OutputDataConfig': {
                's3Uri': 's3://my-bucket'
            }
        },
    )
except Exception as e:
    print(e)

print('Request ID:', response.get('ResponseMetadata').get('RequestId'))
print('Invocation ARN:', response.get('invocationArn'))
```

**Batch inference**

With batch inference, you can submit multiple requests and generate embeddings asynchronously. Batch inference helps you process many requests efficiently by sending a single request and generating responses in an Amazon S3 bucket.

- After defining model inputs in files you create, you upload the files to an S3 bucket.
- You then submit a batch inference request and specify the S3 bucket.
- After the job is complete, you can retrieve the output files from S3.
- You can use batch inference to improve the performance of model inference on large datasets.

**Format and upload your batch inference
data**

You must add your batch inference data to an S3 location that you'll choose or
specify when submitting a model invocation job. The S3 location must the following items:

At least one JSONL file that defines the model inputs. A JSONL contains rows of JSON objects. Your JSONL file must end in the extension .jsonl and be in the following format:

```
{
    "recordId": "record001",
    "modelInput": {
        "taskType": "SINGLE_EMBEDDING",
        "singleEmbeddingParams": {
            "embeddingPurpose": "GENERIC_INDEX",
            "embeddingDimension": 3072,
            "text": {
                "source": {
                    "s3Location": {
                        "uri": "s3://batch-inference-input-bucket/text_001.txt",
                        "bucketOwner": "111122223333"
                    }
                },
                "truncationMode": "END"
            }
        }
    }
}
```

**Supported input file types**

- Image Formats: PNG, JPEG, WEBP, GIF
- Audio Formats: MP3, WAV, OGG
- Video Formats: MP4, MOV, MKV, WEBM, FLV, MPEG, MPG, WMV, 3GP
