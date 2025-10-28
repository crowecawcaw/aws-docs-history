# Video generation access and usage

Generating a video with Amazon Nova Reel is an asynchronous process that typically takes
about 90 seconds for a 6 second video and approximately 14-17 minutes for a 2 minute video. After initiating the generation of a video, the video is
written to an Amazon S3 bucket in your account. Because Amazon Bedrock writes a file to
an Amazon S3 bucket on your behalf, the AWS role that you use needs permissions configured to
allow the appropriate Amazon Bedrock and Amazon S3 actions and the
`s3:PutObject` action. The minimum action permissions required to generate a
video are:

- `bedrock:InvokeModel`
- `s3:PutObject`
  However, we recommend the following additional actions so you can track the status of
  video generation jobs:

- `bedrock:GetAsyncInvoke`
- `bedrock:ListAsyncInvokes`
  When video generation completes, the video and its constituent shots are stored in the Amazon S3 bucket you specified. Amazon Nova creates a folder for each invocation ID. This folder contains the manifest.json, output.mp4, and generation-status.json files that are created by the video generation request.

###### Topics

- [Starting a video generation job](#video-gen-start-a-job "#video-gen-start-a-job")
- [Video generation input parameters](#video-gen-input-params "#video-gen-input-params")
- [Checking progress of video generation
  jobs](#video-gen-check-progress "#video-gen-check-progress")
- [Accessing the results of a video generation job](#video-gen-read-results "#video-gen-read-results")

## Starting a video generation job

To initiate the generation of a video, call `start_async_invoke()`. This
creates a new invocation job. When the job completes, Amazon Nova automatically saves the
generated video to an Amazon S3 bucket that you specify.

`start_async_invoke()` takes the following arguments:

- **modelId** (Required) – The model ID to use. For
  Amazon Nova Reel, this is "amazon.nova-reel-v1:1"
- **modelInput** (Required) – Defines all of the
  video generation parameters specific to the Amazon Nova Reel model. For more
  information, see [Video generation input parameters](#video-gen-input-params "#video-gen-input-params").
- **outputDataConfig** (Required) – Defines where
  the generated video should be saved. The value must have the following
  structure:

```
`{
 "s3OutputDataConfig": {
 "s3Uri": `string (S3 URL starting with "s3://")`
 }
}`
```

## Video generation input parameters

Refer to the following parameter descriptions for information about how to generate videos using Amazon Nova Reel.

Text-to-video generation
The following structure defines an video generation job for Amazon Nova Reel:

```
`{
 "taskType": "TEXT_VIDEO",
 "textToVideoParams": {
 "text": `string`,
 "images": `ImageSource[] (list containing a single ImageSource)`
 },
 "videoGenerationConfig": {
 "durationSeconds": `int`,
 "fps": `int`,
 "dimension": `string`,
 "seed": `int`
 }
}`
```

These input parameters are necessary to create the video generation job:

- **text** (Required) – A text prompt to generate
  the video. Must be 1-512 characters in length.
- **images** (Optional) – A single JPEG or PNG
  image that is used as the starting keyframe of the output video. This input
  image is used along with the text prompt to generate the video. The image must
  be formatted as a base64 string or stored in an Amazon S3 bucket.

Images can be in PNG or JPEG format and must be
8 bits per color channel (RGB). PNG images may contain an additional alpha
channel, but that channel must not contain any transparent or translucent
pixels. Currently, the model accepts only images of 1280 (width) x 720
(height).

Images included through an Amazon S3 bucket can't exceed 25 MB.

- **durationSeconds** (Required) - Duration of the
  output video. 6 is the only supported value currently.
- **fps** (Required)- Frame rate of the output
  video. 24 is the only supported value currently.
- **dimension** (Required) - Width and height of
  the output video. "1280x720" is the only supported value currently.
- **seed** (Optional) – Determines the initial
  noise setting for the generation process. Changing the seed value while leaving
  all other parameters the same will produce a totally new video that still
  adheres to your prompt, dimensions, and other settings. It is common to
  experiment with a variety of seed values to find the perfect image.

The seed value must be between 0-2,147,483,646 and the default value is 42.

###### imageSource schema

When you use an image as the input, use the following structure to include the image
in your request:

```
`{
 "format": "png" | "jpeg"
 "source": {
 "bytes": `string (base64 encoded image)`
 }
}`
```

- **format** (Required) - Must match the format of
  the input image. Either "png" or "jpeg".
- **source** (Required)
  - **bytes** (Required) - The input image
    encoded as a base64 string. The image must have a resolution of 1280 x
  720.

Automated long video generation
You can generate videos up to two minutes long, in six second increments, with just a text prompt using the `MULTI_SHOT_AUTOMATED` task. You can provide a text prompt of up to 4000 characters but can't provide an input image.

```
`{
 "taskType": "MULTI_SHOT_AUTOMATED",
 "multiShotAutomatedParams": {
 "text": `string`,
 },
 "videoGenerationConfig": {
 "durationSeconds": `int`,
 "fps": `int`,
 "dimension": `string`,
 "seed": `int`
 }
}`
```

These input parameters are necessary to create the video generation job:

- **text** (Required) – A text prompt to generate
  the video. Must be 1-4000 characters in length.
- **durationSeconds** (Required) - Duration of the
  output video. A multiple of 6 between 12 and 120, inclusive.
- **fps** (Required)- Frame rate of the output
  video. 24 is the only supported value currently.
- **dimension** (Required) - Width and height of
  the output video. "1280x720" is the only supported value currently.
- **seed** (Optional) – Determines the initial
  noise setting for the generation process. Changing the seed value while leaving
  all other parameters the same will produce a totally new image that still
  adheres to your prompt, dimensions, and other settings. It is common to
  experiment with a variety of seed values to find the perfect image.

The seed value must be between 0-2,147,483,646 and the default value is 42.

Manual long video generation
You can use the `MULTI_SHOT_MANUAL` task to generate videos up to two minutes long with multiple text prompts and input images. For each six second shot in the video, you can provide a text prompt with an optional input image. The duration of the video is determined based on the number shots that you specify.

```
`model_input = {
 "taskType": "MULTI_SHOT_MANUAL",
 "multiShotManualParams": {
 "shots": [
 {
 "text": "`Information for shot 1`"
 },
 {
 "text": "`Information for shot 2`",
 "image": {
 "format": "png", # Must be "png" or "jpeg"
 "source": {
 "bytes": "<base64 image string>"
 },
 },
 },
 {
 "text": "`Information for shot 3`",
 "image": {
 "format": "png", # Must be "png" or "jpeg"
 "source": {
 "s3Location": {
 "uri": "<S3 URI string>",
 "bucketOwner": "<S3 bucket owner string>" # Optional
 }
 }
 }
 },
 ]
 },
 "videoGenerationConfig": {
 "fps": `int`,
 "dimension": `string`,
 "seed": `int`
 }
}`
```

These input parameters are necessary to create the video generation job:

- **shots** (Required) - Contains information about the text prompts and input images that are used for video generation.
- **text** (Required) – A text prompt to generate
  the video. Must be 1-512 characters in length.
- **image** (Optional) – Contains information about the input image that is used for this shot. The image can be provided as either a base64 string in the `bytes` field or as an Amazon S3 URI in the `s3Location` field.

Images can be in PNG or JPEG format and must be
8 bits per color channel (RGB). PNG images may contain an additional alpha
channel, but that channel must not contain any transparent or translucent
pixels. Currently, the model accepts only images of 1280 (width) x 720
(height).

Images included through an Amazon S3 bucket can't exceed 25 MB.

- **fps** (Required)- Frame rate of the output
  video. 24 is the only supported value currently.
- **dimension** (Required) - Width and height of
  the output video. "1280x720" is the only supported value currently.
- **seed** (Optional) – Determines the initial
  noise setting for the generation process. Changing the seed value while leaving
  all other parameters the same will produce a totally new image that still
  adheres to your prompt, dimensions, and other settings. It is common to
  experiment with a variety of seed values to find the perfect image.

The seed value must be between 0-2,147,483,646 and the default value is 42.

The video generation process will result in the following files being written to the Amazon S3 destination you specify:

- **manifest.json** - A file written at the start of the job, containing the request ID.
- **video-generation-status.json** - This file is written whether the job succeeds of fails. When a job fails, it will contain detailed information explaining exactly which part of the job failed and what action to take to fix the error.
- **output.mp4** - The complete multi-shot video. Written only if the job succeeds.
- **shot_N.mp4** - Each individual shot is also provided as its own video. The file name follows the format "shot_0001.mp4", "shot_0002.mp4", and so on. These files are written only if the whole job succeeds.

## Checking progress of video generation

jobs

There are two ways to check on the progress of a video generation job. If you have a
reference to the invocation ARN that was returned when starting the invocation, you can
use the `get_async_invoke()` method of the Amazon Bedrock
Runtime.

```
`response = bedrock_runtime.get_async_invoke(
 invocationArn="arn:AWS:bedrock:us-east-1:`account-id`:async-invoke/`invocation-id`"
)

status = response["status"]
print(f"Status: {status}")`
```

The status of a job will be "Completed", "InProgress", or "Failed". For more details
on using the `get_async_invoke()` method, see the
Async Invoke API documentation.

If you do not have a reference to the invocation ARN, or if you want to check the
status for multiple jobs at once, you can use the `list_async_invokes()`
method of the Amazon Bedrock Runtime.

```
`invocations_details = bedrock_runtime.list_async_invokes(
 maxResults=10, # (Optional)
 statusEquals="InProgress", # (Optional) Can be "Completed", "InProgress", or "Failed". Omit this argument to list all jobs, regardless of status.
 # Note: There are other supported arguments not demonstrated here.
)

print(json.dumps(invocations_details, indent=2, default=str))`
```

For more details on using the `list_async_invokes()` method, see the
Async Invoke API documentation.

## Accessing the results of a video generation job

After a video generation job succeeds or fails, a JSON file is added to your Amazon S3 bucket. This file contains metadata about the shots that were created for the video. The file is named `video-generation-status.json`.

For a successful video generation request, the file contains the location of each individual shot that comprises the full video. For a failed request, the file contains the failure message and additional details about why the shot failed.

The schema of this JSON file is provided below.

```
{
    "schemaVersion": string,
    "shots": [{
            "status": enum, // where success is generation + upload
            "location": string,
            "failureType": enum,
            "failureMessage": string,
        },
        ...
    ],
    "fullVideo": {
        "status": enum, // where success is generation + upload
        "location": string,
        "failureType": enum,
        "failureMessage": string,
    }
}
```

- **schemaVersion** - The version of the JSON schema.
- **shots** - Provides information about each shot in the video.
  - **status** - The completion state (SUCCESS or FAILURE) of the shot.
  - **location** - The file name and Amazon S3 location where the shot is stored. The location will be available only when all shots are successfully generated and the complete video is uploaded to its Amazon S3 location.
  - **failureType** - Provides the reason for failure.
  - **failureMessage** - Provides more information about the failure reason.

- **fullVideo** - Provides information about the full video.
  - **status** - The completion state (SUCCESS or FAILURE) of the full video.
  - **location** - The file name and Amazon S3 location where the full video is stored.
  - **failureType** - Provides the reason for failure.
  - **failureMessage** - Provides more information about the failure reason.

Possible failure reasons and messages are

- INTERNAL_SERVER_EXCEPTION - "Something went wrong on the server side."
- RAI_VIOLATION_OUTPUT_VIDEO_DEFLECTION - "The generated content has been blocked by our content filters."
- RATE_LIMIT_EXCEEDED - "Service capacity limit has been reached. Please try again later."
- ABORTED - "Request has been aborted."
