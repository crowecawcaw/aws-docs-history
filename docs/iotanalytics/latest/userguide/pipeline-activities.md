End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Pipeline activities

The simplest functional pipeline connects a channel to a data store, which makes it a
pipeline with two activities: a `channel` activity and a `datastore`
activity. You can achieve more powerful message processing by adding additional activities to your
pipeline.

You can use the [RunPipelineActivity](../APIReference/API_RunPipelineActivity.md "../APIReference/API_RunPipelineActivity.md") operation to simulate the results of running a pipeline activity on
a message payload you provide. You might find this helpful when you are developing and debugging
your pipeline activities. [RunPipelineActivity example](run-pipeline-activity.md "run-pipeline-activity.md")
demonstrates how it is used.
