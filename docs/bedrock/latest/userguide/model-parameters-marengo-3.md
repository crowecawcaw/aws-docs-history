# TwelveLabs Marengo Embed 3.0

The TwelveLabs Marengo Embed 3.0 model generates enhanced embeddings from video, text, audio, or image inputs. This latest version offers improved performance and accuracy for similarity search, clustering, and other machine learning tasks.

- Provider — TwelveLabs
- Model ID — twelvelabs.marengo-embed-3-0-v1:0
  Marengo Embed 3.0 delivers several key enhancements:

- **Extended video processing capacity** – Process up to 4 hours of video and audio content and files up to 6 GB—double the capacity of previous versions—making it ideal for analyzing full sporting events, extended training videos, and complete film productions.
- **Enhanced sports analysis** – The model delivers significant improvements with better understanding of gameplay dynamics, player movements, and event detection.
- **Global multilingual support** – Expanded language capabilities from 12 to 36 languages, enabling global organizations to build unified search and retrieval systems that work seamlessly across diverse regions and markets.
- **Multimodal search precision** – Combine images and descriptive text in a single embedding request, merging visual similarity with semantic understanding to deliver more accurate and contextually relevant search results.
- **Reduced embedding dimension** – Reduced from 1024 to 512, cutting storage costs.
  The TwelveLabs Marengo Embed 3.0 model supports the Amazon Bedrock Runtime operations in the following table.

- For more information about use cases for different API methods, see [Learn about use cases for different model inference methods](inference-methods.md "inference-methods.md").
- For more information about model types, see [How inference works in Amazon Bedrock](inference-how.md "inference-how.md").
  - For a list of model IDs and to see the models and AWS Regions that TwelveLabs Marengo Embed 3.0 is supported in, search for the model in the table at [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").
  - For a full list of inference profile IDs, see [Supported Regions and models for inference profiles](inference-profiles-support.md "inference-profiles-support.md"). The inference profile ID is based on the AWS Region.

| API operation    | Supported model types                                                                                                                                                                                                                                                                                                                                                    | Input modalities                                                                                | Output modalities |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------- |
| InvokeModel      | US East (N. Virginia) – [Base models](models-supported.md "models-supported.md") and [Inference profiles](inference-profiles-support.md "inference-profiles-support.md")<br>Europe (Ireland) – [Inference profiles](inference-profiles-support.md "inference-profiles-support.md")<br>Asia Pacific (Seoul)<br>• [Base models](models-supported.md "models-supported.md") | Text<br>Image<br>\*_Note:_<br>• Text and image interleaved is also supported.                   | Embedding         |
| StartAsyncInvoke | [Base models](models-supported.md "models-supported.md")                                                                                                                                                                                                                                                                                                                 | Video<br>Audio<br>Image<br>Text<br>\*_Note:_<br>• Text and image interleaved is also supported. | Embedding         |

###### Note

Use `InvokeModel` to generate embeddings for search query. Use `StartAsyncInvoke` to generate embeddings for assets at a large scale.

The following quotas apply to the input:

| Input modality | Maximum             |
| -------------- | ------------------- |
| Text           | 500 tokens          |
| Image          | 5 MB per image      |
| Video (S3)     | 6 GB, 4 hour length |
| Audio (S3)     | 6 GB, 4 hour length |

###### Note

If you define audio or video inline by using base64-encoding, make sure that the request body payload
doesn't exceed the Amazon Bedrock 25 MB model invocation quota.

###### Topics

- [TwelveLabs Marengo Embed 3.0 request parameters](#model-parameters-marengo-3-async-request "#model-parameters-marengo-3-async-request")
- [TwelveLabs Marengo Embed 3.0 response](#model-parameters-marengo-3-response "#model-parameters-marengo-3-response")

## TwelveLabs Marengo Embed 3.0 request parameters

When you make a request, the field in which the model-specific input is specified depends on the API operation:

- [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") – In the request `body`.
- [StartAsyncInvoke](../APIReference/API_runtime_StartAsyncInvoke.md "../APIReference/API_runtime_StartAsyncInvoke.md") – In the `modelInput` field of the request body.

The format of the model input depends on the input modality:

Text

```
{
    "inputType": "text",
    "text": {
        "inputText": "`string`"
    }
}
```

Text & image

```
{
    "inputType": "text_image",
    "text_image": {
        "inputText": "`string`",
        "mediaSource": {
            "s3Location": {
                "uri": "s3://`amzn-s3-demo-bucket`",
                "bucketOwner": "`123456789012`"
            }
        }
    }
}
```

Inline image

```
{
    "inputType": "image",
    "image": {
        "mediaSource": {
            "base64String": "`base64-encoded string`"
        }
    }
}
```

S3 image

```
{
    "inputType": "image",
    "image": {
        "mediaSource": {
            "s3Location": {
                "uri": "s3://`amzn-s3-demo-bucket`",
                "bucketOwner": "`string`"
            }
        }
    }
}
```

S3 video

```
{
    "inputType": "video",
    "video": {
        "mediaSource": {
            "s3Location": {
               "uri": "s3://`amzn-s3-demo-bucket`",
               "bucketOwner": "`string`"
            }
        }
    }
}
```

S3 audio

```
{
    "inputType": "audio",
    "audio": {
       "mediaSource": {
           "s3Location": {
              "uri": "s3://`amzn-s3-demo-bucket`",
              "bucketOwner": "`string`"
           }
       }
    }
}
```

Expand the following sections for details about the input parameters:

Modality for the embedding.

- **Type:** String
- **Required:** Yes
- **Valid values:** `video` | `text` | `audio` | `image` | `text_image`
  Text to be embedded.

- **Type:** String
- **Required:** Yes (for compatible input types)
- **Compatible input types:** Text
  Contains information about the media source.

- **Type:** Object
- **Required:** Yes (if compatible type)
- **Compatible input types:** Image, Video, Audio
  The format of the `mediaSource` object in the request body depends on whether the media is defined as a Base64-encoded string or as an S3 location.

- **Base64-encoded string**

```
{
    "mediaSource": {
        "base64String": "base64-encoded string"
    }
}
```

    + `base64String` – The Base64-encoded string for the media.

- **S3 location** – Specify the S3 URI and the bucket owner.

```
{
    "s3Location": {
        "uri": "string",
        "bucketOwner": "string"
    }
}
```

    + `uri` – The S3 URI containing the media.
    + `bucketOwner` – The AWS account ID of the S3 bucket owner.

## TwelveLabs Marengo Embed 3.0 response

The response body is in the following format:

```
{
    "data": [
        {
            "embedding": [float]
        }
    ]
}
```

The embeddings are returned as an array of floats.

Where you see this response depends on the API method you used:

- InvokeModel – Appears in the response body.
- StartAsyncInvoke – Appears at the S3 location that you specified in the request. The response returns an `invocationArn` that you can use to get metadata about the asynchronous invocation, including the status and the S3 location to which the results are written.
