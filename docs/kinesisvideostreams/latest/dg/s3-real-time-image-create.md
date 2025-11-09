# Automated real-time image generation

Amazon Kinesis Video Streams offers the capability to transcode and deliver images. Kinesis Video Streams automatically extracts images from video data
in real-time, and delivers the images to your specified Amazon S3 bucket. Implementing real-time, automated image extraction involves the following steps:

- Creating an S3 bucket to receive the generated images.
- Configuring the [ImageGenerationConfiguration](API_ImageGenerationConfiguration.md "API_ImageGenerationConfiguration.md") stream property which tells Kinesis Video Streams
  how to create the images and where to send them.
- Add image generation tags – Kinesis Video Streams only generates images using fragments that have the image generation tag. These tags are added when uploading video
  using the Kinesis Video Streams Producer SDK along with the `putKinesisVideoEventMetadata` method.
  The following procedures provide instructions to complete each of these steps.

If you're using a customer managed key, ensure that the role performing the `PutMedia` calls (uploader) has the
following permissions that are required for encrypting and decrypting data, and for access to the Amazon S3 bucket.

- `kms:Encrypt`
- `kms:GenerateDataKey`
- `kms:Decrypt`
- `s3:PutObject`
  For more information, see [How do I get started with server-side encryption?](how-kms.md#getting-started-with-sse-akvs "how-kms.md#getting-started-with-sse-akvs").

###### To configure the generated images destination

1. Create an S3 destination bucket where the images will be sent.

Follow the [Amazon S3 User Guide](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") to create an Amazon S3 bucket.

Note the bucket's URI, which you'll need in the next step when updating the stream's image generation configuration. 2. Verify that you have the AWS CLI installed and configured. For more information, see the
[AWS Command Line Interface User Guide for Version 2](cli/latest/userguide/cli-chap-welcome.md "cli/latest/userguide/cli-chap-welcome.md"). 3. Create a new file called `update-image-generation-input.json` with the following content as input. Update the placeholder
values with the values that you want to use. For the maximum and minimum supported values, see the
[UpdateImageGenerationConfiguration](API_UpdateImageGenerationConfiguration.md "API_UpdateImageGenerationConfiguration.md") API.

```
{
   "StreamName": "`demo-stream`",
   "ImageGenerationConfiguration": {
      "Status": "ENABLED",
      "DestinationConfig": {
         "DestinationRegion": "`us-east-1`",
         "Uri": "s3://`my-bucket-name`"
      },
      "SamplingInterval": 200,
      "ImageSelectorType": "PRODUCER_TIMESTAMP",
      "Format": "JPEG",
      "FormatConfig": {
         "JPEGQuality": "80"
      },
      "WidthPixels": 320,
      "HeightPixels": 240
   }
}
```

4. Update the stream's image generation configuration using the [UpdateImageGenerationConfiguration](API_UpdateImageGenerationConfiguration.md "API_UpdateImageGenerationConfiguration.md") API and attaching the
   JSON file as the input, as shown in the following command. Note that the file path points to the file in the current directory.

```
aws kinesisvideo update-image-generation-configuration \
  --cli-input-json file://./update-image-generation-input.json
```

5. Upon success, an empty response is returned and nothing is printed in your terminal.

###### Note

It takes at least 1 minute to initiate the image generation workflow after updating the image generation configuration.
Wait at least 1 minute before uploading video to your stream. 6. Verify the configuration settings. Use the AWS CLI to call the [DescribeImageGenerationConfiguration](API_DescribeImageGenerationConfiguration.md "API_DescribeImageGenerationConfiguration.md") API for your stream.

```
aws kinesisvideo describe-image-generation-configuration \
  --stream-name "`demo-stream`"
```

Kinesis Video Streams will only generate and deliver images for fragments that have the image generation tag. Any additional fragment
metadata provided along with the Amazon S3 image generation tags will be saved as Amazon S3 metadata.

###### Note

Image generation tags refer to fragment-metadata tags and not to stream-level tags.

###### Important

Image generation tags count towards the fragment-metadata tag limit. For more information, see [Streaming metadata service quotas](limits.md#limits-streaming-metadata "limits.md#limits-streaming-metadata").

The following is an example of what the fragment metadata tags structure looks like using the `mkvinfo` utility. The image generation tag is an MKV simple tag
with a key of `AWS_KINESISVIDEO_IMAGE_GENERATION` and no value. For more information, see
[Video Tags Example](https://www.matroska.org/technical/tagging-video-example.html "https://www.matroska.org/technical/tagging-video-example.html") in the Matroska documentation.

```
|+ Tags
| + Tag
|  // MANDATORY: Predefined MKV tag to trigger image generation for the fragment
|  + Simple
|   + Name: AWS_KINESISVIDEO_IMAGE_GENERATION

|  // OPTIONAL: S3 prefix which will be set as prefix for generated image.
|  + Simple
|   + Name: AWS_KINESISVIDEO_IMAGE_PREFIX
|   + String: `image_prefix_in_s3` // 256 bytes max

| // OPTIONAL: Key value pairs that will be persisted as S3 Image object metadata.
|  + Simple
|   + Name: `CUSTOM_KEY_1` // Max 128 bytes
|   + String: `CUSTOM_VALUE_1` // Max 256 bytes
|  + Simple
|   + Name: `CUSTOM_KEY_2` // Max 128 bytes
|   + String: `CUSTOM_VALUE_2` // Max 256 bytes
```

## Adding image generation tags to fragments

Kinesis Video Streams generates and delivers images only for fragments that have the image generation tag.
Kinesis Video Streams recognizes these special MKV tags and initiates the image generation workflow based on the
stream's image processing configuration.

When using the Kinesis Video Streams Producer SDK to upload media, you use the `putKinesisVideoEventMetadata` method to
add the image generation tag to each fragment that you want to tag. A new fragment starts when `putFrame`
is called with a frame containing the `keyframe` flag.

If you're uploading a prerecorded video, it might get uploaded at a different rate than the rate
at which it was recorded, dependent on your network speed. We recommend that you use the Producer
timestamp to configure image generation if you want to generate images at regular intervals
based on the video's original timestamps, and not use the server timestamps
generated based on the rate at which Amazon Kinesis Video Streams received your video.

To view a full example of this code, see the
[`VideoOnlyRealtimeStreamingSample`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-c/blob/master/samples/KvsVideoOnlyRealtimeStreamingSample.c "https://github.com/awslabs/amazon-kinesis-video-streams-producer-c/blob/master/samples/KvsVideoOnlyRealtimeStreamingSample.c")
code sample in GitHub.

```
// Setup sample frame
MEMSET(frameBuffer, 0x00, frameSize);
frame.frameData = frameBuffer;
frame.version = FRAME_CURRENT_VERSION;
frame.trackId = DEFAULT_VIDEO_TRACK_ID;
frame.duration = HUNDREDS_OF_NANOS_IN_A_SECOND / DEFAULT_FPS_VALUE;
frame.decodingTs = defaultGetTime(); // current time
frame.presentationTs = frame.decodingTs;

Frame eofr = EOFR_FRAME_INITIALIZER;

while(defaultGetTime() > streamStopTime) {
    frame.index = frameIndex;
    frame.flags = fileIndex % DEFAULT_KEY_FRAME_INTERVAL == 0 ? FRAME_FLAG_KEY_FRAME : FRAME_FLAG_NONE;
    frame.size = SIZEOF(frameBuffer);

    CHK_STATUS(readFrameData(&frame, frameFilePath));

    // 1. End the previous fragment
    if (frame.flags == FRAME_FLAG_KEY_FRAME && !firstFrame) {
        putKinesisVideoFrame(streamHandle, &eofr);
    }

    // 2. putFrame call
    CHK_STATUS(putKinesisVideoFrame(streamHandle, &frame));

    if (frame.flags == FRAME_FLAG_KEY_FRAME) {
        // 3. Adding the image generation tag
        CHK_STATUS(putKinesisVideoEventMetadata(streamHandle, STREAM_EVENT_TYPE_IMAGE_GENERATION, NULL);)

        // 4. Adding fragment metadata
        for (n = 1; n <= 5; n++) {
            SNPRINTF(metadataKey, METADATA_MAX_KEY_LENGTH, "SAMPLE_KEY_%d", n);
            SNPRINTF(metadataValue, METADATA_MAX_VALUE_LENGTH, "SAMPLE_VALUE_%d", frame.index + n);
            CHK_STATUS(putKinesisVideoFragmentMetadata(streamHandle, metadataKey, metadataValue, FALSE));
        }
    }
    defaultThreadSleep(frame.duration);

    frame.decodingTs += frame.duration;
    frame.presentationTs = frame.decodingTs;
    frameIndex++;
    fileIndex++;
    fileIndex = fileIndex % NUMBER_OF_FRAME_FILES;
    firstFrame = TRUE;
}

// 5. End the final fragment
putKinesisVideoFrame(streamHandle, &eofr);
```

The elements of the example code for setting up sample frames are explained as follows:

1. Each fragment needs to end with an end of fragment (`eofr`). This statement says whenever
   a new keyframe is received, which signals the beginning of the next frame, put an
   `eofr` before adding the next frame into the stream.
2. Put the current frame into the stream.
3. Add the image generation tag. The `putKinesisVideoEventMetadata` method can be called any time after the `putFrame(keyFrame)`
   call and before the `putFrame(eofr)`. It must only be called at most once per fragment. Since every fragment will have only one keyframe,
   we call it at this time for simplicity. The return value for `putKinesisVideoEventMetadata` gets checked for a success code (0).
4. Add other custom fragment metadata, which Kinesis Video Streams will transform into Amazon S3 object metadata.
5. End the final fragment in this uploading session.

### Using the samples to add image generation tags

You can use the `kvs_gstreamer_audio_video_sample` in the C++ Producer SDK if you want a command line option
to add image generation tags. Enable this feature by adding either the `-e image` or `-e both` argument, as shown
in the following example.

```
./kvs_gstreamer_audio_video_sample `stream-name` \
  -f `video-to-upload.mp4` \
  -e both
```

For more information about this sample application, see the
[Amazon Kinesis Video Streams CPP Producer, GStreamer Plugin and JNI README](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/README.md "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/README.md")
in GitHub.

## Amazon S3 object path (image)

The S3 object path describes the location on the configured S3 bucket where the generated image will be delivered. It uses the following format:

```
`ImagePrefix`_`AccountID`_`StreamName`_`ImageTimecode`_`RandomID`.`file-extension`
```

The object path elements are defined as follows:

- `ImagePrefix` - Value of `AWS_KINESISVIDEO_IMAGE_PREFIX` if present.
- `AccountID` - The AWS account ID under which the stream is created.
- `StreamName` - Name of the stream from which the image is generated.
- `ImageTimecode` - Epoch timecode (in milliseconds) in the fragment at which the image is generated.
- `RandomID` - Random GUID.
- `file-extension` - JPG or PNG based on the image format requested.

In this example, the object path for the generated images will look as follows:

```
111122223333_demo-stream_16907729324_f20f9add-75e7-4399-a30f-fc7aefb1bab7.jpg
```

## Retrieving image metadata

You can use the S3 console or CLI to retrieve the metadata for the generated images.

Kinesis Video Streams sets the fragment number, the producer and server timestamp, and the content type metadata of the image generated, all formatted as Amazon S3 object metadata.
If any additional MKV tags are present, those tags will also be added as Amazon S3 object metadata. The following example shows how to use the Amazon S3 head-object API
command to retrieve the object metadata. The response includes the metadata created by Kinesis Video Streams.

```
`aws s3api head-object --bucket `my-bucket-name` --key `111122223333`_`demo-stream`_1690707290324_f20f9add-7e57-4399-a30f-fc7aefb1bab7.jpg`
`{
 "AcceptRanges": "bytes",
 "LastModified": "2023-07-30T08:54:51+00:00",
 "ContentLength": 22693,
 "ETag": "\"63e03cb6d57f77e2db984c1d344b1083\"",
 "ContentType": "image/jpeg",
 "ServerSideEncryption": "AES256",
 "Metadata": {
 "aws_kinesisvideo_producer_timestamp": "1690707290324",
 "aws_kinesisvideo_server_timestamp": "1690707289209",
 "aws_kinesisvideo_fragment_number": "91343852333182036507421233921329142742245756394"
 }
}`
```

For more information about S3 object metadata, see
[https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingMetadata.html](../../../AmazonS3/latest/userguide/UsingMetadata.md "../../../AmazonS3/latest/userguide/UsingMetadata.md").

## Amazon S3 URI recommendations to protect against throttling

If you write thousands of images to Amazon S3, there's a risk of throttling. For more information, see
[S3 Prefix Put Request Limits](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md").

An Amazon S3 prefix starts with a PUT limit of 3,500 PUT requests per second, and will gradually ramp up over
time for unique prefixes. Avoid using dates and times as Amazon S3 prefixes. Time coded data will impact one prefix at a time,
and will also change regularly, invalidating previous prefix scale ups.

To enable faster, consistent Amazon S3 scaling,
we recommend adding a random prefix, like a hex code or UUID to the Amazon S3 Destination URI.
For example, hex code prefixes will naturally split your requests randomly among 16 different prefixes
(a prefix for each unique hex character), which will allow a 56,000 PUT requests per second after Amazon S3 has auto-scaled.
