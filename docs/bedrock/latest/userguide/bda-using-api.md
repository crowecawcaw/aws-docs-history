# Using the Bedrock Data Automation API

The Amazon Bedrock Data Automation (BDA) feature provides a streamlined API workflow
for processing your data. For all modalities, this workflow consists of three main steps: creating
a project, invoking the analysis, and retrieving the results. To retrieve custom output for your
processed data, you provide the Blueprint ARN when you invoke the analysis operation.

## Create a Data Automation Project

To begin processing files with BDA, you first need to create a Data Automation Project. This can be done in two ways, with the CreateDataAutomationProject operation or the Amazon Amazon Bedrock Console.

### Using the API

When using the API to create a project, you invoke the CreateDataAutomationProject.
When creating a project, you must define your configuration settings for the type of file you tend to process (the modality you intend to use). Here's an example of how you might configure the standard output for images:

```
{
    "standardOutputConfiguration": {
        "image": {
            "state": "ENABLED",
            "extraction": {
                "category": {
                    "state": "ENABLED",
                    "types": [
                        "CONTENT_MODERATION",
                        "TEXT_DETECTION"
                    ]
                },
                "boundingBox": {
                    "state": "ENABLED"
                }
            },
            "generativeField": {
                "state": "ENABLED",
                "types": [
                    "IMAGE_SUMMARY",
                    "IAB"
                ]
            }
        }
    }
}
```

The API validates the input configuration. It creates a new project with a unique ARN. The project settings are stored for future use. If a project is created with no parameters, the default settings will apply. For example, when processing images, image summarization and text detection will be enabled by default.

There's a limit to the number of projects that can be created per AWS account. Certain
combinations of settings may not be allowed or may require additional permissions.

## Invoke Data Automation Async

You have a project set up, you can start processing images using the InvokeDataAutomationAsync operation. If using custom output, you can only submit a single blueprint ARN per request.

This API call initiates the asynchronous processing of your files in a specified S3 bucket. The API accepts the project ARN and the file to be processed, then starts the asynchronous processing job. A job ID is returned for tracking the process. Errors will be raised if the project doesn't exist, or if the caller doesn't have the necessary permissions, or if the input files aren't in a supported format.

The following is the structure of the JSON request:

```
{
   {
   "blueprints": [
      {
         "blueprintArn": "`string`",
         "stage": "`string`",
         "version": "`string`"
      }
   ],
   "clientToken": "`string`",
   "dataAutomationConfiguration": {
      "dataAutomationProjectArn": "`string`",
      "stage": "`string`"
   },
   "dataAutomationProfileArn": "`string`",
   "encryptionConfiguration": {
      "kmsEncryptionContext": {
         "string" : "`string`"
      },
      "kmsKeyId": "`string`"
   },
   "inputConfiguration": {
      "assetProcessingConfiguration": {
         "video": {
            "segmentConfiguration": { ... }
         }
      "s3Uri": "`string`"
   },
   "notificationConfiguration": {
      "eventBridgeConfiguration": {
         "eventBridgeEnabled": `boolean`
      }
   },
   "outputConfiguration": {
      "s3Uri": "`string`"
   },
   "tags": [
      {
         "key": "s`string`",
         "value": "`string`"
      }
   ]
}
}
```

When you run `InvokeDataAutomationAsync` on a video file, you can set a 5 minute or longer section of a video
that will be treated as a full video for the data extraction. This time is set with a timestamp of the
starting millisecond and ending millisecond. This information is added in the `assetProcessingConfiguration`
element.

## Get Data Automation Status

To check the status of your processing job and retrieve results, use
GetDataAutomationStatus.

The GetDataAutomationStatus API allows you to monitor the progress of your job and access
the results once processing is complete. The API accepts the invocation ARN returned by
InvokeDataAutomationAsync. It checks the current status of the job and returns relevant
information. Once the job is complete, it provides the location of the results in S3.

If the job is still in progress, it returns the current state (e.g., "InProgress"). If the job is complete, it returns "Success" along with the S3 location of the results. If there was an error, it returns "ServiceError" or "ClientError" with error details.

The following is the format of the request JSON:

```
{
   "InvocationArn": "string" // Arn
}
```

## Async Output Response

The results of the file processing are stored in the S3 bucket configured for the input
images. The output includes unique structures depending on both the file modality and the
operation types specified in the call to InvokeDataAutomationAsync.

For information on the standard outputs for a given modality, see [Standard output in Bedrock Data
Automation](bda-standard-output.md "bda-standard-output.md").

As an example, for images it can include information on the following:

- Image Summarization: A descriptive summary or caption of the image.
- IAB Classification: Categorization based on the IAB taxonomy.
- Image Text Detection: Extracted text with bounding box information.
- Content Moderation: Detects inappropriate, unwanted, or offensive content in an image.

The following is an example snippet of the output for image processing:

```
{
    "metadata": {
        "id": "image_123",
        "semantic_modality": "IMAGE",
        "s3_bucket": "my-s3-bucket",
        "s3_prefix": "images/",
        "image_width_pixels": 1920,
        "image_height_pixels": 1080
    },
    "image": {
        "summary": "A lively party scene with colorful decorations and supplies",
        "iab_categories": [
            {
                "category": "Party Supplies",
                "confidence": 0.9,
                "parent_name": "Events & Attractions"
            }
        ],
        "content_moderation": [
            {
                "category": "Drugs & Tobacco Paraphernalia & Use",
                "confidence": 0.7
            }
        ],
        "text_words": [
            {
                "id": "word_1",
                "text": "lively",
                "confidence": 0.9,
                "line_id": "line_1",
                "locations": [
                    {
                        "bounding_box": {
                            "left": 100,
                            "top": 200,
                            "width": 50,
                            "height": 20
                        },
                        "polygon": [
                            {
                                "x": 100,
                                "y": 200
                            },
                            {
                                "x": 150,
                                "y": 200
                            },
                            {
                                "x": 150,
                                "y": 220
                            },
                            {
                                "x": 100,
                                "y": 220
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

This structured output allows for easy integration with downstream applications and further analysis.
