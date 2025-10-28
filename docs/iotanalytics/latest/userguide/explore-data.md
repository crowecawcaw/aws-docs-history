End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Exploring AWS IoT Analytics data

You have several options for storing, analyzing and visualizing your AWS IoT Analytics data.

###### Topics on this page:

- [Amazon S3](#amazon-s3 "#amazon-s3")
- [AWS IoT Events](#aws-iot-events "#aws-iot-events")
- [Quick Suite](#quicksight "#quicksight")
- [Jupyter Notebook](#jupyter-noteboo "#jupyter-noteboo")

## Amazon S3

You can send dataset contents to an [Amazon Simple Storage Service (Amazon S3)](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md") bucket, enabling integration with your existing data
lakes or access from in-house applications and visualization tools. See the field
`contentDeliveryRules::destination::s3DestinationConfiguration` in
[CreateDataset](api.md#cli-iotanalytics-createdataset "api.md#cli-iotanalytics-createdataset").

## AWS IoT Events

You can send dataset contents as an input to AWS IoT Events, a service which enables you to monitor devices or processes
for failures or changes in operation, and to trigger additional actions when such events occur.

To do this, create a dataset using [CreateDataset](api.md#cli-iotanalytics-createdataset "api.md#cli-iotanalytics-createdataset")
and specify an AWS IoT Events input in the field
`contentDeliveryRules :: destination :: iotEventsDestinationConfiguration :: inputName`.
You must also specify the `roleArn` of a role which grants AWS IoT Analytics permission to execute "iotevents:BatchPutMessage".
Whenever the dataset's contents are created, AWS IoT Analytics will send each dataset content entry as a message to the specified AWS IoT Events input.
For example, if your dataset contains:

```
"what","who","dt"
"overflow","sensor01","2019-09-16 09:04:00.000"
"overflow","sensor02","2019-09-16 09:07:00.000"
"underflow","sensor01","2019-09-16 11:09:00.000"
...
```

then AWS IoT Analytics will send messages containing fields like this:

```
{ "what": "overflow", "who": "sensor01", "dt": "2019-09-16 09:04:00.000" }
```

```
{ "what": "overflow", "who": "sensor02", "dt": "2019-09-16 09:07:00.000" }
```

and you will want to create an AWS IoT Events input that recognized the fields you are interested in (one or more of `what`,
`who`, `dt`) and to create an AWS IoT Events detector model that uses these input fields in events to trigger
actions or set internal variables.

## Quick Suite

AWS IoT Analytics provides direct integration with [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/"). Quick Suite is a fast business analytics service you can use to build
visualizations, perform ad-hoc analysis, and quickly get business insights from your
data. Quick Suite enables organizations to scale to hundreds of thousands of users, and
delivers responsive performance by using a robust in-memory engine (SPICE). Quick Suite is
available in [these regions](../../../general/latest/gr/quicksight.md "../../../general/latest/gr/quicksight.md").

## Jupyter Notebook

AWS IoT Analytics datasets can also be directly consumed by Jupyter Notebook in order to perform advanced analytics and data exploration.
Jupyter Notebook is an open source solution. You can install and download from
[http://jupyter.org/install.html](https://jupyter.org/install.html "https://jupyter.org/install.html"). Additional integration with SageMaker AI,
an Amazon hosted notebook solution, is also available.
