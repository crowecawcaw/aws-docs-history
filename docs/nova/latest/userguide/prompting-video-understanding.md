# Vision understanding prompting best

practices

###### Note

This documentation is for Amazon Nova Version 1. For information about how to prompt multimodal understanding in Amazon Nova 2, visit [Prompting multimodal inputs](../nova2-userguide/prompting-multimodal.md "../nova2-userguide/prompting-multimodal.md").

The Amazon Nova model family is equipped with novel vision capabilities that enable the
model to comprehend and analyze images and videos, thereby unlocking exciting opportunities
for multimodal interaction. The following sections outline guidelines for working with
images and videos in Amazon Nova. This includes best practices, code examples, and relevant
limitations to consider.

The higher-quality images or videos that you provide, the greater the chances that the
models will accurately understand the information in the media file. Ensure the images or
videos are clear and free from excessive blurriness or pixelation to guarantee more accurate
results. If the image or video frames contains important text information, verify that the
text is legible and not too small. Avoid cropping out key visual context solely to enlarge
the text.

Amazon Nova models allow you to include a single video in the payload, which can be provided
either in base64 format or through an Amazon S3 URI. When using the base64 method, the overall
payload size must be less than 25 MB. However, you can specify an Amazon S3 URI for image, video, and document
understanding. Using Amazon S3 allows you to leverage the model for larger files and multiple media files, without being constrained by the overall payload size limitation. Amazon Nova can
analyze the input video and answer questions, classify a video, and summarize information in
the video based on provided instructions.

Amazon Nova models allow you to include multiple images in the payload. The total payload
size can't exceed 25 MB. Amazon Nova models can analyze the passed images and answer questions,
classify an image, and summarize images based on provided instructions.

| Image information | Media File Type           | File Formats supported   | Input Method |
| ----------------- | ------------------------- | ------------------------ | ------------ |
| Image             | PNG, JPG, JPEG, GIF, WebP | Base64 and Amazon S3 URI |

| Video information | Format           | MIME Type                                                                       | Video Encoding |
| ----------------- | ---------------- | ------------------------------------------------------------------------------- | -------------- |
| MKV               | video/x-matroska | H.264                                                                           |
| MOV               | video/quicktime  | H.264<br>H.265<br>ProRES                                                        |
| MP4               | video/mp4        | DIVX/XVID<br>H.264<br>H.265<br>J2K (JPEG2000)<br>MPEG-2<br>MPEG-4 Part 2<br>VP9 |
| WEBM              | video/webm       | VP8<br>VP9                                                                      |
| FLV               | video/x-flv      | FLV1                                                                            |
| MPEG              | video/mpeg       | MPEG-1                                                                          |
| MPG               | video/mpg        | MPEG-1                                                                          |
| WMV               | video/wmv        | MSMPEG4v3 (MP43)                                                                |
| 3GPP              | video/3gpp       | H.264                                                                           |

There are no differences in the video input token count, regardless of whether the video
is passed as base64 (as long as it fits within the size constraints) or via an Amazon S3
location.

Note that for 3gp file format, the "format" field passed in the API request should be of
the format "three_gp".

When using Amazon S3, ensure that your "Content-Type" metadata is set to the correct MIME type
for the video

###### Topics

- [Long and high-motion videos](#prompting-video-motion "#prompting-video-motion")
- [Latency](#prompting-video-latency "#prompting-video-latency")
- [Vision understanding prompting
  techniques](prompting-vision-prompting.md "prompting-vision-prompting.md")

## Long and high-motion videos

The model does video understanding by sampling videos frames at a base 1 frame per
second (FPS). It is a balance between capturing details in the video and consuming input
tokens utilized, which affects cost, latency, and maximum video length. While sampling
one event every second should be enough for general use cases, some use cases on high
motion videos such as sports videos might not perform well.

In order to handle longer videos, the sampling rate is decreased on videos longer than
16 minutes to a fixed 960 frames, spaced across the length of the video for Amazon Nova Lite and Amazon Nova Pro. This means
that, as a video gets longer than 16 minutes, the lower the FPS and fewer details will
be captured. This allows for use cases such as summarization of longer videos, but
exacerbates issues with high motion videos where details are important. For Amazon Nova Premier, the 1 FPS sampling rate is applied up to a limit of 3,200 frames.

In many cases, you can get a 1 FPS sampling on longer videos by using pre-processing
steps and multiple calls. The video can be split into smaller segments, then each
segment is analyzed using the multi-model capabilities of the model. The responses are
aggregated and a final step using text-to-text generates a final answer. Note there can
be loss of context when segmenting the videos this way. This is akin to the tradeoffs in
chunking for RAG use cases and many of the same mitigation techniques transfer well,
such as sliding-window.

Note that segmenting the video might also decrease latency as analysis is done in
parallel, but can generate significantly more input tokens, which affect cost.

## Latency

Videos can be large in size. Although we provide means to handle up to 1 GB files by
uploading them to Amazon S3, making invocation payloads very lean, the models still needs to
process a potentially large number of tokens. If you are using synchronous
Amazon Bedrock calls such as Invoke or Converse, make sure your SDK is
configured with an appropriate timeout.

Regardless, Amazon S3 URI is the preferred way when latency is a factor. Segmenting videos
as described in the previous section is another strategy. Pre-processing high-resolution
and high-frame rate videos down can also save bandwidth and processing on the service
size, lowering latency.
