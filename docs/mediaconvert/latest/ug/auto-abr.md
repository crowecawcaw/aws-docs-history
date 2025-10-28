# Automated ABR

With automated ABR, AWS Elemental MediaConvert sets up your adaptive bitrate (ABR) stack for you.
MediaConvert chooses the right number of renditions and the resolution for each, based on
the input video. MediaConvert minimizes the total minutes of transcoded output by
eliminating renditions that increase bitrate without providing increased video quality.
Automated ABR also maximizes video quality at various bitrates by employing the
quality-defined variable bitrate (QVBR) rate control mode.

###### Topics

- [Understanding how automated ABR works](#how-automated-abr-works "#how-automated-abr-works")
- [Creating a job with automated ABR](creating-an-automated-abr-stack.md "creating-an-automated-abr-stack.md")
- [Applying automated ABR rules](automated-abr-rules.md "automated-abr-rules.md")
- [Job settings limitations for
  automated ABR](feature-restrictions-for-automated-abr.md "feature-restrictions-for-automated-abr.md")

## Understanding how automated ABR works

With all adaptive bitrate (ABR) streaming, the end viewer's player device adjusts
which rendition of the package it downloads based on the available bandwidth. For
example, a viewer with access to high-quality wifi would automatically see a
high-bitrate rendition. When they move to a location with only limited bandwidth, their
player device automatically switches over to a lower-bitrate rendition. How well the
adaptive streaming works depends on the construction of the ABR stack and how well that
construction suits the content of the specific video. For example, with a fast-moving,
visually complex asset, your ABR stack might include two 720p outputs with different
bitrates. If you used that same stack setup with a simple cartoon, those two outputs
would likely look the same. The extra encoding, storage, and distribution would cost
money without conferring any benefit to the end viewer.

When you run an automated ABR job, MediaConvert maximizes the video quality that the
end viewer sees based on their available bandwidth. It does this by analyzing a broad
set of possible renditions and eliminating any that increase required bandwidth without
increasing video quality. When you run your job, MediaConvert analyzes the content of
your input video and chooses the number of renditions and the characteristics of each
rendition for you.

You can use the MediaConvert console to run your job without setting anything. There are three
categories of optional settings you can specify if you choose
to:

- Limits on your adaptive bitrate (ABR) stack.
- Limits that apply to the renditions in the ABR stack. These output-level
  limits apply to all renditions in the stack.
- All other encoding settings.

For these settings, MediaConvert uses default values unless you specify
something different. This works the same as with outputs that don't use
automated ABR, except that whatever values you set apply to all renditions in
the stack. For example, if you set **Profile** to
**High 10-bit**, every rendition will have that codec
profile.

### Settings that apply to the

ABR stack

You can set the following limits that relate to the whole ABR stack:

- **Max renditions**: This is the upper limit for the
  number of renditions in your ABR stack. The number of renditions in your
  stack might be less than this, but won't be more.

You can specify a number from 3–15. If you don't specify this, the
default maximum is 15.

- **Max ABR bitrate**: The maximum average bitrate for the
  highest-bitrate rendition in your stack.

This is the rendition that is delivered to viewers with the fastest
internet connections. Use to limit the total bytes that are egressed to
viewers who receive the highest-bitrate rendition.

If you don't specify this, the default maximum is 8 mb/s.

The average bitrate of your highest-quality rendition will be equal to or
below this value, depending on the quality, complexity, and resolution of
your content. The instantaneous maximum bitrate can vary above the value
that you specify.

- **Min ABR bitrate**: The minimum average bitrate for the
  lowest-quality rendition in your stack.

This is the rendition that is delivered to viewers with the slowest
internet connections.

If you don't specify this, the default minimum is 600 kb/s.

The instantaneous minimum bitrate can vary below the value that you
specify.

### Settings that apply

to renditions in the stack

You can set the following limits that relate to properties of the renditions in
the stack:

- **Max resolution**: This is the maximum resolution of
  your highest-bitrate rendition. When you set this value, choose the
  resolution of the highest quality device that you expect end viewers to use.
  MediaConvert won't create a rendition with a resolution larger than
  this.

If you don't specify this, the default maximum is the resolution of your
input video.

If you specify a value larger than your input video's resolution,
MediaConvert uses your input resolution as the maximum. MediaConvert won't
use a resolution larger than the input for any rendition because upscaling
the input resolution would add bandwidth without adding video
quality.

- **Max frame rate**: MediaConvert uses this value as the
  frame rate for the for highest-bandwidth rendition in your stack. Depending
  on the input, this might be the frame rate for all renditions. When your
  input frame rate is high, MediaConvert might halve the frame rate for
  lower-bandwidth renditions. For example, if your input frame rate is 60 fps,
  MediaConvert might use 30 fps for some of the lower-bandwidth renditions,
  and perhaps 15 fps for the very lowest.

If you don't specify this value, the default maximum is your input frame
rate.

For these settings, MediaConvert determines these values for each rendition
automatically:

- **Quality tuning level**: MediaConvert encodes all
  renditions with **Multi pass HQ**.

This behavior is automatic in the MediaConvert console but not when you submit your job
programmatically. When you set up your JSON job specification without using
the MediaConvert console, you must explicitly set `qualityTuningLevel` to
`MULTI_PASS_HQ`.

- **Rate control mode**: MediaConvert encodes all
  renditions with [QVBR](cbr-vbr-qvbr.md "cbr-vbr-qvbr.md") rate control
  mode.

This behavior is automatic in the MediaConvert console but not when you submit your job
programmatically. When you set up your JSON job specification without using
the MediaConvert console, you must explicitly set `rateControlMode` to
`QVBR`.

- These QVBR required settings:
  - **QVBR quality level**:
  - **Max bitrate**
  - **Max average bitrate**

- **HDR buffer size**
- **HDR buffer initial fill**

### Automated ABR frequently

asked
questions

###### How can I see what renditions AWS Elemental MediaConvert created for me?

You can see the properties of the outputs in your ABR stack in these
places:

- The job completion event from Amazon EventBridge. For more information, see [Using EventBridge with AWS Elemental MediaConvert](eventbridge_events.md "eventbridge_events.md").
- The **Job summary** page on the MediaConvert console. For
  more information, see [Viewing your job history](viewing-job-history.md "viewing-job-history.md").

###### Will my automated ABR job take a long time to run?

We recommend that you always use [accelerated transcoding](accelerated-transcoding.md "accelerated-transcoding.md") with automated ABR. When you do, your job should
take only slightly longer than an accelerated transcoding job for a manually
specified ABR stack with similar outputs. You don't pay more for enabling
accelerated transcoding because automated ABR is already billed at the 2 Pass
(Quality Optimized) professional tier rate.

When you run an automated ABR job without accelerated transcoding, it takes much
longer to run than a job with a manually specified ABR stack with similar
outputs..

###### Why do some of my output renditions have the same resolution?

When display devices stream an ABR asset, they request segments based on the
bitrate of the rendition, not based on the resolution of the rendition. Therefore,
an ABR stack can have renditions for different bandwidths that have the same
resolution. The higher bandwidth rendition will have better quality at the same
resolution.

Whether increasing the resolution improves video quality when you go up to the next
rendition of the stack depends on the complexity of the video. The ability to
automatically adjust these choices on a per-job basis is one of the ways that this
feature gives you better results with less effort.

###### Can I tell ahead of time how many renditions will be in my stack?

No. MediaConvert determines which renditions to use during the transcoding
process. Because the encoding decisions depend on qualities of your input video,
there's no way to know before running the job what those decisions will be.

You can use the optional limits settings to make sure that the number of renditions,
and the size of those renditions, won't exceed what you want.

###### How will I be billed for an automated ABR stack?

MediaConvert bills you for only the renditions that it writes to your output
location. For example, you might set **Max renditions** to 12, but
MediaConvert might determine that there is no advantage to creating more than eight
renditions. In this case, MediaConvert would bill you for only eight
renditions.

Automated ABR is a professional-tier feature and also requires 2 pass encoding. Every
rendition is billed per-minute at the 2 Pass (Quality Optimized) rate. For example, say
your automated ABR stack ends up with 10 renditions, each of them being 60 minutes long.
You would then be charged for 600 minutes. For rates, see [AWS Elemental MediaConvert Pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/") in the
_AWS Cloud Products_ website.

###### What about audio?

Automated ABR does the set up for your video renditions only. You add audio
renditions as audio-only outputs inside of your automated ABR output group. For
instructions, see [Creating a job with automated ABR](creating-an-automated-abr-stack.md "creating-an-automated-abr-stack.md").

###### What about captions?

Add captions to your automated ABR package as captions-only output. For
instructions, see [Creating a job with automated ABR](creating-an-automated-abr-stack.md "creating-an-automated-abr-stack.md").
