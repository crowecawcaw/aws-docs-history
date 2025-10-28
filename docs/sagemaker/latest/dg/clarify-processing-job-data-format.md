# Data Format Compatibility Guide

This guide describes the data format types that are compatible with SageMaker Clarify processing jobs.
The supported data format types include the file extensions, data structure, and specific
requirements or restrictions for tabular, image, and time series datasets. This guide also shows how to
check if your dataset conforms to these requirements.

At a high level, the SageMaker Clarify processing job follows the input–process–output model to
compute bias metrics and feature attributions. Refer to the following examples for
details.

The input to the SageMaker Clarify processing job consists of the following:

- The dataset to be analyzed.
- The analysis configuration. For more information about how to configure an
  analysis, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").
  During the processing stage, SageMaker Clarify computes bias metrics and feature attributions. The
  SageMaker Clarify processing job completes the following steps in the backend:

- The SageMaker Clarify processing job parses your analysis configuration and loads your
  **dataset**.
- To compute post-training bias metrics and feature attributions, the job requires
  model predictions from your model. The SageMaker Clarify processing job serializes your data and
  sends it as a **request** to your model that is
  deployed on a SageMaker AI real-time inference **endpoint**.
  After that, the SageMaker Clarify processing job extracts predictions from the **response**.
- The SageMaker Clarify processing job performs the bias and explainability analysis, and then
  it outputs the results.
  For more information, see [How SageMaker Clarify Processing Jobs
  Work](clarify-configure-processing-jobs.md#clarify-processing-job-configure-how-it-works "clarify-configure-processing-jobs.md#clarify-processing-job-configure-how-it-works") .

The parameter that' you use to specify the format of the data depends on where the data is
used in the processing flow as follows:

- For an **input dataset**, use the
  `dataset_type` parameter to specify the format or MIME type.
- For a **request** to an endpoint, use the
  `content_type` parameter to specify the format.
- For a **response** from an endpoint, use the
  `accept_type` parameter to specify the format.
  The input dataset, request, and the response to and from the endpoint don't require the
  same format. For example, you can use a Parquet dataset with a CSV **request** payload and a JSON Lines **response**
  payload given the following conditions.

- Your analysis is configured correctly.
- Your model supports the request and response formats.

###### Note

If `content_type` or `accept_type` are not provided, then the
SageMaker Clarify container infers the `content_type` and
`accept_type`.

###### Topics

- [Tabular data](clarify-processing-job-data-format-tabular.md "clarify-processing-job-data-format-tabular.md")
- [Image data requirements](clarify-processing-job-data-format-image.md "clarify-processing-job-data-format-image.md")
- [Time series data](clarify-processing-job-data-format-time-series.md "clarify-processing-job-data-format-time-series.md")
