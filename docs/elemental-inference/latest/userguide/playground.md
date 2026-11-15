

# Using the Elemental Inference playground
<a name="playground"></a>

Use the Elemental Inference playground to try Elemental Inference on an MP4 video file in Amazon S3, without setting up a live feed. Choose one of two kinds of jobs:
+ **Smart Cropping** – AWS Elemental MediaConvert writes a 1080x1920 portrait MP4 (H.264 video, stereo AAC audio) to your Amazon S3 folder. Choose this to get a cropped video file.
+ **All features** – The console runs smart cropping, event clipping, smart subtitles, and contextual metadata on a clip of 5 seconds to 5 minutes, and shows each feature's results as the clip plays. Choose this to see what each feature returns for your content. It doesn't write a cropped video, and your browser tab must stay open until it finishes. For more information, see [Previewing all features](playground-preview.md).

For how smart cropping works and the AWS Regions where it's available, see [Smart Cropping with Elemental Inference](https://docs.aws.amazon.com/mediaconvert/latest/ug/smart-cropping-with-elemental-inference.html) in the AWS Elemental MediaConvert User Guide.

**Topics**
+ [How the playground works](playground-how-it-works.md)
+ [Permissions](playground-permissions.md)
+ [Creating a Smart Cropping job](playground-create-job.md)
+ [Previewing all features](playground-preview.md)
+ [Viewing job results](playground-job-details.md)
+ [Pricing](playground-pricing.md)
+ [Troubleshooting](playground-troubleshooting.md)