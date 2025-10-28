# Extract images from video streams

You can use Amazon Kinesis Video Streams APIs and SDKs to perform on-demand image extraction and
automated image extraction in real time from your Kinesis video streams. You can use these images for enhanced playback
applications such as thumbnails or enhanced scrubbing, or for use in machine learning
workflows.

Kinesis Video Streams supports extracting images from video streams two ways:

- **[On-demand Image Generation](API_reader_GetImages.md "API_reader_GetImages.md")** -
  Use the `GetImages` API to extract a single image or multiple images from video stored in Kinesis Video Streams.
- **[Automated real-time image generation](s3-real-time-image-create.md "s3-real-time-image-create.md")** - Configure Kinesis Video Streams to automatically extract images from video data in
  real time based on fragment tags from video as it is ingested, and deliver the images to an S3 bucket.
