# Running a trained Amazon Rekognition Custom Labels model

When you're satisfied with the performance of the model, you can start to use it. You can
start and stop a model by using the console or the AWS SDK. The console also includes
example SDK operations that you can use.

###### Topics

- [Inference units](#running-model-inference-units "#running-model-inference-units")
- [Availability Zones](#running-model-availability-zones "#running-model-availability-zones")
- [Starting an Amazon Rekognition Custom Labels model](rm-start.md "rm-start.md")
- [Stopping an Amazon Rekognition Custom Labels model](rm-stop.md "rm-stop.md")
- [Reporting running duration and inference units used](rm-model-usage.md "rm-model-usage.md")

## Inference units

When you start your model, you specify the number of compute resources,
known as an inference unit, that the model uses.

###### Important

You are charged for the number of hours that your model is running and for the number
of inference units that your model uses while it's running, based on how you configure
the running of your model. For example, if you start the model with two inference units
and use the model for 8 hours, you are charged for 16 inference hours (8 hours running
time \* two inference units). For more information, see [Inference hours](https://aws.amazon.com/rekognition/pricing/#Amazon_Rekognition_Custom_Labels_pricing "https://aws.amazon.com/rekognition/pricing/#Amazon_Rekognition_Custom_Labels_pricing"). If you don't explicitly [stop your
model](rm-stop.md "rm-stop.md"), you are charged even if you are not actively analyzing images with
your model.

The transactions per second (TPS) that a single inference unit supports is affected by
the following.

- A model that detects image-level labels (classification) generally has a
  higher TPS than a model that detects and localizes objects with bounding boxes
  (object detection).
- The complexity of the model.
- A higher resolution image requires more time for analysis.
- More objects in an image requires more time for analysis.
- Smaller images are analyzed faster than larger images.
- An image passed as image bytes is analyzed faster than first uploading the
  image to an Amazon S3 bucket and then referencing the uploaded image. Images
  passed as image bytes must be smaller than 4.0 MB. We recommend that you use
  image bytes for near real time processing of images and when the image size is
  less that 4.0 MB. For example, images captured from an IP camera.
- Processing images stored in an Amazon S3 bucket is faster than downloading the
  images, converting to image bytes, and then passing the image bytes for
  analysis.
- Analyzing an image already stored in an Amazon S3 bucket is probably faster
  than analyzing the same image passed as image bytes. That's especially true if
  the image size is larger.

If the number of calls to `DetectCustomLabels` exceeds the maximum TPS
supported by the sum of inference units that a model uses, Amazon Rekognition Custom Labels returns an
`ProvisionedThroughputExceededException` exception.

### Managing throughput with inference units

You can increase or decrease the throughput of your model depending on the demands
on your application. To increase throughput, use additional inference units.
Each additional inference unit increases your processing speed by one inference
unit. For information about calculating the number of inference units that you need, see
[Calculate inference units for Amazon Rekognition Custom Labels and Amazon Lookout
for Vision models](https://aws.amazon.com/blogs/machine-learning/calculate-inference-units-for-an-amazon-rekognition-custom-labels-model/ "https://aws.amazon.com/blogs/machine-learning/calculate-inference-units-for-an-amazon-rekognition-custom-labels-model/"). If you want to change the supported throughput of your model, you have two
options:

#### Manually add or remove inference units

[Stop](rm-stop.md "rm-stop.md") the model and then [restart](rm-start.md "rm-start.md") with the required number of inference units. The
disadvantage with this approach is that the model can't receive requests while
it's restarting and can't be used to handle spikes in demand. Use this approach
if your model has steady throughput and your use case can tolerate 10–20
minutes of downtime. An example would be if you want to batch calls to your
model using a weekly schedule.

#### Auto-scale inference

units

If your model has to accommodate spikes in demand, Amazon Rekognition Custom Labels can
automatically scale the number of inference units your model uses. As demand
increases, Amazon Rekognition Custom Labels adds additional inference units to the model and removes
them when demand decreases.

To let Amazon Rekognition Custom Labels automatically scale inference units for a model, [start](rm-start.md "rm-start.md") the model and set the maximum number of
inference units that it can use by using the `MaxInferenceUnits`
parameter. Setting a maximum number of inference units lets you manage the cost
of running the model by limiting the number of inference units available to it.
If you don't specify a maximum number of units, Amazon Rekognition Custom Labels won't automatically
scale your model, only using the number of inference units that you started
with. For information regarding the maximum number of inference units, see
[Service
Quotas](../../../general/latest/gr/rekognition.md#limits_rekognition "../../../general/latest/gr/rekognition.md#limits_rekognition").

You can also specify a minimum number of inference units by using the
`MinInferenceUnits` parameter. This lets you specify the minimum
throughput for your model, where a single inference unit represents 1 hour of
processing time.

###### Note

You can't set the maximum number of inference units with the Amazon Rekognition Custom Labels
console. Instead, specify the `MaxInferenceUnits` input parameter
to the `StartProjectVersion` operation.

Amazon Rekognition Custom Labels provides the following Amazon CloudWatch Logs metrics that you can use to
determine the current automatic scaling status for a model.

| Metric                    | Description                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| `DesiredInferenceUnits`   | The number of inference units to which Amazon Rekognition Custom Labels is<br>scaling up or down. |
| `InServiceInferenceUnits` | The number of inference units that the model is<br>using.                                         |

If `DesiredInferenceUnits` = `InServiceInferenceUnits`,
Amazon Rekognition Custom Labels is not currently scaling the number of inference units.

If `DesiredInferenceUnits` >
`InServiceInferenceUnits`, Amazon Rekognition Custom Labels is scaling up to the value
of `DesiredInferenceUnits`.

If `DesiredInferenceUnits` <
`InServiceInferenceUnits`, Amazon Rekognition Custom Labels is scaling down to the
value of `DesiredInferenceUnits`.

For more information regarding the metrics returned by Amazon Rekognition Custom Labels and
filtering dimensions, see [CloudWatch metrics
for Rekognition](../dg/cloudwatch-metricsdim.md "../dg/cloudwatch-metricsdim.md").

To find out the maximum number of inference units that you requested for a
model, call `DescribeProjectsVersion` and check the
`MaxInferenceUnits` field in the response. For example code, see
[Describing a model (SDK)](md-describing-model-sdk.md "md-describing-model-sdk.md").

## Availability Zones

Amazon Rekognition Custom Labels distributes inference units across multiple Availability Zones within an AWS
Region to provide increased availability. For more information, see [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones"). To help protect your production models from
Availability Zone outages and inference unit failures, start your production models with
at least two inference units.

If an Availability Zone outage occurs, all inference units in the Availability Zone are
unavailable and model capacity is reduced. Calls to [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md") are redistributed across the remaining inference units.
Such calls succeed if they don’t exceed the supported Transactions Per Seconds (TPS) of
the remaining inference units. After AWS repairs the Availability Zone, the inference
units are restarted, and full capacity is restored.

If a single inference unit fails, Amazon Rekognition Custom Labels automatically starts a new inference unit in the same Availability Zone.
Model capacity is reduced until the new inference unit starts.
