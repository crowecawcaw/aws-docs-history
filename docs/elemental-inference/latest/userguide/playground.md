

# Using the Elemental Inference playground
<a name="playground"></a>

The Elemental Inference playground lets you preview smart cropping on a recorded MP4 video file in Amazon S3, without setting up a live feed. Use it to see how smart cropping reframes your content before you build a live workflow.

When you submit a playground job, it runs as an AWS Elemental MediaConvert job in your account. During the job, MediaConvert creates an Elemental Inference feed to analyze the video, and then deletes the feed when the job ends. MediaConvert writes the reframed output – a 1080x1920 portrait MP4 with H.264 video and stereo AAC audio – to the Amazon S3 location that you choose.

Smart cropping in the playground is the same feature described in the AWS Elemental MediaConvert documentation. For how smart cropping works and the list of AWS Regions where it is available, see [Smart Cropping with Elemental Inference](https://docs.aws.amazon.com/mediaconvert/latest/ug/smart-cropping-with-elemental-inference.html) in the AWS Elemental MediaConvert User Guide.

**Topics**
+ [How the playground works](playground-how-it-works.md)
+ [Permissions](playground-permissions.md)
+ [Creating a playground job](playground-create-job.md)
+ [Viewing job results](playground-job-details.md)
+ [Pricing](playground-pricing.md)
+ [Troubleshooting](playground-troubleshooting.md)