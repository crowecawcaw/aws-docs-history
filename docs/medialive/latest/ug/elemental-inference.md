# AWS Elemental Inference

AWS Elemental MediaLive includes features that are seamless implementations of the features of
AWS Elemental Inference. Elemental Inference is an AI service that lets you easily apply machine learning
foundational models to video, audio, and image content for automated analysis,
classification, and insights generation.

MediaLive implements the following features of AWS Elemental Inference:

- Automatic subtitling, which generates TTML or WebVTT subtitles from the audio in your
  source media using automatic speech recognition. For more information, see [Smart Subtitles using Elemental Inference](elemental-inference-automatic-subtitling.md "elemental-inference-automatic-subtitling.md").
- Smart crop, which lets you produce channel video outputs that are a different
  aspect ratio and/or orientation from the video source. For more information, see
  [Smart cropping video using Elemental Inference](elemental-inference-smart-crop.md "elemental-inference-smart-crop.md").
- Event clipping, which lets you produce file clips from the channel video source.
  For more information, see [Clipping video using AWS Elemental Inference](elemental-inference-event-clip.md "elemental-inference-event-clip.md").

## Elemental Inference quotas

Elemental Inference has its own quotas. All of these quotas apply when you use
the Elemental Inference features of MediaLive.

For example, there are Elemental Inference quotas relating to feeds and feed outputs. To
use Elemental Inference features with an MediaLive channel, select an existing feed. Configure
the feed with the appropriate outputs for the features you want to use (for example,
a subtitling output for Smart Subtitles, a cropping output for smart crop, or a
clipping output for event clipping).

Keep in mind that these feeds and outputs count toward your Elemental Inference quotas.

For information about the default values for quotas and which quotas can be changed
(adjusted) see the Elemental Inference section in [AWS General
Reference](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

For more information about changing Elemental Inference quotas, see the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas").
