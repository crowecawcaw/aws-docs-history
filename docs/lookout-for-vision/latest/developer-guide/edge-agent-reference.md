End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Amazon Lookout for Vision Edge Agent API reference

This section is the API reference for the Amazon Lookout for Vision Edge Agent.

## Detecting anomalies with a model

You use the [DetectAnomalies](edge-agent-reference-detect-anomalies.md "edge-agent-reference-detect-anomalies.md") API
to detect anomalies in images by using a running model on an AWS IoT Greengrass Version 2 core device.

## Getting model information

APIs that get information about models deployed to a core device.

- [ListModels](edge-agent-reference-list-models.md "edge-agent-reference-list-models.md")
- [DescribeModel](edge-agent-reference-describe-model.md "edge-agent-reference-describe-model.md")

## Running a model

APIs for starting and stopping an Amazon Lookout for Vision model that's deployed to a core
device.

- [StartModel](edge-agent-reference-start-model.md "edge-agent-reference-start-model.md")
- [StopModel](edge-agent-reference-stop-model.md "edge-agent-reference-stop-model.md")
