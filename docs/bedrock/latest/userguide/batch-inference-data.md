# Format and upload your batch inference data

You must add your batch inference data to an S3 location that you'll choose or specify when submitting a model invocation job. The S3 location must contain the following items:

- At least one JSONL file that defines the model inputs. A JSONL contains rows of JSON objects. Your JSONL file must end in the extension .jsonl and be in the following format:

```
{ "recordId" : "`alphanumeric string`", "modelInput" : `{JSON body}` }
...

```

Each line contains a JSON object with a `recordId` field and a `modelInput` field containing the request body for an input you want to submit. The format of the `modelInput` JSON object must match the `body` field for the model that you use in the `InvokeModel` request. For more information, see [Inference request parameters and response fields for foundation models](model-parameters.md "model-parameters.md").

###### Note

    + If you omit the `recordId` field, Amazon Bedrock adds it in the output.
    + The order of records in the output JSONL file is not guaranteed to match the order of records in the input JSONL file.
    + You specify the model that you want to use when you create the [batch inference job](batch-inference-create.md "batch-inference-create.md").

- (If you define input content as an Amazon S3 location) Some models allow you to define the content of the input as an S3 location. If you choose this option, ensure that the S3 location that you'll specify contains both your content and your JSONL files. Your content and JSONL files can be nested in folders at the S3 location that you specify. For an example, see [Example video input for Amazon Nova](#batch-inference-data-ex-s3 "#batch-inference-data-ex-s3").
  Ensure that your inputs conform to the batch inference quotas. You can search for the following quotas at [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock"):

- **Minimum number of records per batch inference job** – The minimum number of records (JSON objects) across JSONL files in the job.
- **Records per input file per batch inference job** – The maximum number of records (JSON objects) in a single JSONL file in the job.
- **Records per batch inference job** – The maximum number of records (JSON objects) across JSONL files in the job.
- **Batch inference input file size** – The maximum size of a single file in the job.
- **Batch inference job size** – The maximum cumulative size of all input files.
  To better understand how to set up your batch inference inputs, see the following examples:

## Example text input for Anthropic Claude 3 Haiku

If you plan
to run batch inference using the [Messages API](model-parameters-anthropic-claude-messages.md "model-parameters-anthropic-claude-messages.md") format for the Anthropic Claude 3 Haiku model, you might provide a JSONL file containing the following JSON object as one of the lines:

```
{
    "recordId": "CALL0000001",
    "modelInput": {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Summarize the following call transcript: ..."
                    }
                ]
            }
        ]
    }
}
```

## Example video input for Amazon Nova

If you plan to run batch inference on video inputs using the Amazon Nova Lite or Amazon Nova Pro models, you have the option of defining the video in bytes or as an S3 location in the JSONL file. For example, you might have an S3 bucket whose path is `s3://batch-inference-input-bucket` and contains the following files:

```
videos/
    video1.mp4
    video2.mp4
    ...
    video50.mp4
input.jsonl
```

A sample record from the `input.jsonl` file would be the following:

```
{
    "recordId": "RECORD01",
    "modelInput": {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": "You are an expert in recipe videos. Describe this video in less than 200 words following these guidelines: ..."
                    },
                    {
                        "video": {
                            "format": "mp4",
                            "source": {
                                "s3Location": {
                                    "uri": "`s3://batch-inference-input-bucket/videos/video1.mp4`",
                                    "bucketOwner": "`111122223333`"
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
}
```

When you create the batch inference job, you can specify `s3://batch-inference-input-bucket` as the S3 location. Batch inference will process the `input.jsonl` file in the location, in addition to the video files within the `videos` folder that are referenced in the JSONL file.

The following resources provide more information about submitting video inputs for batch inference:

- To learn how to proactively validate of Amazon S3 URIs in an input request, see the [Amazon S3 URL Parsing blog](https://aws.amazon.com/blogs/devops/s3-uri-parsing-is-now-available-in-aws-sdk-for-java-2-x/ "https://aws.amazon.com/blogs/devops/s3-uri-parsing-is-now-available-in-aws-sdk-for-java-2-x/").
- For more information on how to set up invocation records for video understanding with Nova, refer to [Amazon Nova vision prompting guidelines](../../../nova/latest/userguide/prompting-vision-prompting.md "../../../nova/latest/userguide/prompting-vision-prompting.md").

The following topic describes how to set up S3 access and batch inference permissions for an identity to be able to carry out batch inference.
