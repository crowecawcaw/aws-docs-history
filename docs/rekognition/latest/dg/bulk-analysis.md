# Bulk analysis

Amazon Rekognition Bulk Analysis lets you process a large collection of images asynchronously by
using a manifest file with the [StartMediaAnalysisJob](../APIReference/API_StartMediaAnalysisJob.md "../APIReference/API_StartMediaAnalysisJob.md") operation. The output for each individual image matches
the output returned by the operation that you use for analysis.

Currently, Rekognition supports analysis with the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md") operation.

You will be charged for the number of images that have been successfully processed by the
job. The results of a finished job are outputted to a specified Amazon S3 bucket.

Note that Bulk Analysis does not support the Amazon A2I integration.

The API can detect animated or illustrated content types, and information about the
detected content type is returned as part of the response.

###### Topics

- [Processing images in bulk](to-process-images-in-bulk.md "to-process-images-in-bulk.md")
- [Bulk analysis output manifests](bulk-analysis-output-manifests.md "bulk-analysis-output-manifests.md")
- [Content type](bulk-analysis-content-type.md "bulk-analysis-content-type.md")
- [Verifying predictions and training
  adapters](bulk-analysis-pred-verify.md "bulk-analysis-pred-verify.md")
