

# Pricing

Playground jobs incur both AWS Elemental Inference and AWS Elemental MediaConvert charges. For more information about pricing, see [AWS Elemental Inference pricing](https://aws.amazon.com/elemental-inference/pricing/) and [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/). Before you submit, the **Create job** page shows an estimated cost per minute of the clip. For an All features preview, it shows figures only when pricing is available for your Region. Otherwise, it describes what's charged.
+ A Smart Cropping job is charged only if it succeeds.
+ An All features preview is charged per minute of the clip. The charge includes MediaConvert transcoding once and Elemental Inference processing with four features.

  Each run of a preview, including **Run again**, is charged for Elemental Inference again. If the earlier run was stopped or failed before its clip was prepared, running again also charges MediaConvert transcoding again. Reopening a saved preview isn't charged.