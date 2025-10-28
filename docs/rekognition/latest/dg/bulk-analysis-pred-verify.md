# Verifying predictions and training

adapters

Bulk Analysis can also be leveraged through the [Rekognition console](https://console.aws.amazon.com/rekognition/ "https://console.aws.amazon.com/rekognition/") to get
predictions for a batch of images, verify these predictions, and then create an adapter
using the verified predictions. Adapters allow you to enhance the accuracy of any
supported Rekognition operation.

Currently, you can create adapters for use with the Rekognition Custom Moderation
feature. By creating an adapter and providing it to the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md") operation, you can achieve better accuracy for the
content moderation tasks related to your specific use case.

For more information about Custom Moderation, see [Enhancing accuracy with Custom
Moderation](moderation-custom-moderation.md "moderation-custom-moderation.md"). See [Bulk analysis and verification](adapters-bulk-analysis.md "adapters-bulk-analysis.md")
for an explanation of how to verify predictions made with Bulk analysis. For a tutorial
covering how to use the Rekognition console to verify predictions and create an adapter, see
[Custom Moderation adapter tutorial](using-adapters-tutorial.md "using-adapters-tutorial.md").
