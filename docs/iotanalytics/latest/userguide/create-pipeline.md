End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Creating a pipeline

A pipeline consumes messages from a channel and enables you to process and filter the
messages before storing them in a data store. To connect a channel to a data store, you
create a pipeline. The simplest possible pipeline contains no activities other than
specifying the channel that collects the data and identifying the data store to which
the messages are sent. For information about more complicated pipelines, see [Pipeline activities](pipeline-activities.md#aws-iot-analytics-pipeline-activities "pipeline-activities.md#aws-iot-analytics-pipeline-activities").

When starting out, we recommend that you create a pipeline that
does nothing other than connect a channel to a data store. Then,
after you verify that raw data flows to the data store, you can
introduce additional pipeline activities to process this data.

Run the following command to create a pipeline.

```
aws iotanalytics create-pipeline --cli-input-json file://mypipeline.json
```

The `mypipeline.json` file contains the following content.

```
{
    "pipelineName": "mypipeline",
    "pipelineActivities": [
        {
            "channel": {
                "name": "mychannelactivity",
                "channelName": "mychannel",
                "next": "mystoreactivity"
            }
        },
        {
            "datastore": {
                "name": "mystoreactivity",
                "datastoreName": "mydatastore"
            }
        }
    ]
}
```

Run the following command to list your existing pipelines.

```
aws iotanalytics list-pipelines
```

Run the following command to view the configuration of an individual pipeline.

```
aws iotanalytics describe-pipeline  --pipeline-name mypipeline
```
