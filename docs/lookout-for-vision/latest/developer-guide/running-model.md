End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Running your trained Amazon Lookout for Vision model

To detect anomalies in images with your model, you must first start your model with the
[StartModel](../APIReference/API_StartModel.md "../APIReference/API_StartModel.md") operation. The Amazon Lookout for Vision
console provides AWS CLI commands that you can use to start and stop your model. This section
includes example code that you can use.

After your model starts, you can use the `DetectAnomalies` operation to detect
anomalies in an image. For more information, see [Detecting anomalies in an image](inference-detect-anomalies.md "inference-detect-anomalies.md").

###### Topics

- [Inference units](#running-model-inference-units "#running-model-inference-units")
- [Availability Zones](#running-model-availability-zones "#running-model-availability-zones")
- [Starting your Amazon Lookout for Vision model](run-start-model.md "run-start-model.md")
- [Stopping your Amazon Lookout for Vision model](run-stop-model.md "run-stop-model.md")

## Inference units

When you start your model, Amazon Lookout for Vision provisions a minimum of one compute resource,
known as an inference unit. You specify the number of inference units to use in the `MinInferenceUnits`
input parameter to the `StartModel` API. The default allocation for a model is 1 inference unit.

###### Important

You are charged for the number of hours that your model is running and for the number
of inference units that your model uses while it's running, based on how you configure
the running of your model. For example, if you start the model with two inference units
and use the model for 8 hours, you are charged for 16 inference hours (8 hours running
time \* two inference units). For more information, see [Amazon Lookout for Vision
Pricing](https://aws.amazon.com/lookout-for-vision/pricing/ "https://aws.amazon.com/lookout-for-vision/pricing/"). If you don't explicitly stop your model by calling [StopModel](../APIReference/API_StopModel.md "../APIReference/API_StopModel.md"), you are charged even if you are
not actively analyzing images with your model.

The transactions per second (TPS) that a single inference unit supports is affected by the following:

- The algorithm that Lookout for Vision uses to train the model. When you train a model, multiple models are trained.
  Lookout for Vision selects the model with the best performance based on the size
  of the dataset and its composition of normal and anomalous images.
- Higher resolution images require more time for analysis.
- Smaller sized images (measured in MBs) are analyzed faster than larger images.

### Managing throughput with inference units

You can increase or decrease the throughput of your model depending on the demands
on your application. To increase throughput, use additional inference units.
Each additional inference unit increases your processing speed by one inference
unit. For information about calculating the number of inference units that you need, see
[Calculate inference units for Amazon Rekognition Custom Labels and Amazon Lookout
for Vision models](https://aws.amazon.com/blogs/machine-learning/calculate-inference-units-for-an-amazon-rekognition-custom-labels-model/ "https://aws.amazon.com/blogs/machine-learning/calculate-inference-units-for-an-amazon-rekognition-custom-labels-model/"). If you want to change the supported throughput of your model, you have two
options:

#### Manually add or remove inference units

[Stop](run-stop-model.md "run-stop-model.md") the model and then [restart](run-start-model.md "run-start-model.md") with the required number of inference units. The
disadvantage with this approach is that the model can't receive requests while
it's restarting and can't be used to handle spikes in demand. Use this approach
if your model has steady throughput and your use case can tolerate 10–20
minutes of downtime. An example would be if you want to batch calls to your
model using a weekly schedule.

#### Auto-scale inference

units

If your model has to accommodate spikes in demand, Amazon Lookout for Vision can
automatically scale the number of inference units that your model uses. As
demand increases, Amazon Lookout for Vision adds additional inference units to the model and
removes them when demand decreases.

To let Lookout for Vision automatically scale inference units for a model, [start](run-start-model.md "run-start-model.md") the model and set the maximum number of
inference units that it can use by using the `MaxInferenceUnits`
parameter. Setting a maximum number of inference units lets you manage the cost
of running the model by limiting the number of inference units available to it.
If you don't specify a maximum number of units, Lookout for Vision won't automatically
scale your model, only using the number of inference units that you started
with. For information regarding the maximum number of inference units, see
[Service
Quotas](../../../general/latest/gr/rekognition.md#limits_lookoutvision "../../../general/latest/gr/rekognition.md#limits_lookoutvision").

You can also specify a minimum number of inference units by using the
`MinInferenceUnits` parameter. This lets you specify the minimum
throughput for your model, where a single inference unit represents 1 hour of
processing time.

###### Note

You can't set the maximum number of inference units with the Lookout for Vision
console. Instead, specify the `MaxInferenceUnits` input parameter
to the `StartModel` operation.

Lookout for Vision provides the following Amazon CloudWatch Logs metrics that you can use to
determine the current automatic scaling status for a model.

| Metric                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| `DesiredInferenceUnits`   | The number of inference units to which Lookout for Vision is<br>scaling up or down. |
| `InServiceInferenceUnits` | The number of inference units that the model is<br>using.                           |

If `DesiredInferenceUnits` = `InServiceInferenceUnits`,
Lookout for Vision is not currently scaling the number of inference units.

If `DesiredInferenceUnits` >
`InServiceInferenceUnits`, Lookout for Vision is scaling up to the value
of `DesiredInferenceUnits`.

If `DesiredInferenceUnits` <
`InServiceInferenceUnits`, Lookout for Vision is scaling down to the
value of `DesiredInferenceUnits`.

For more information regarding the metrics returned by Lookout for Vision and
filtering dimensions, see
[Monitoring Lookout for Vision with Amazon CloudWatch](security-monitoring-cloudwatch.md "security-monitoring-cloudwatch.md").

To find out the maximum number of inference units that you requested for a
model, call [DescribeModel](../APIReference/API_DescribeModel.md "../APIReference/API_DescribeModel.md")
and check the `MaxInferenceUnits` field in the response.

## Availability Zones

Amazon Lookout for Vision; distributes inference units across multiple Availability Zones within an AWS
Region to provide increased availability. For more information, see [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones"). To help protect your production models from
Availability Zone outages and inference unit failures, start your production models with
at least two inference units.

If an Availability Zone outage occurs, all inference units in the Availability Zone are
unavailable and model capacity is reduced. Calls to [DetectAnomalies](../APIReference/API_DetectAnomalies.md "../APIReference/API_DetectAnomalies.md") are redistributed across the remaining inference units.
Such calls succeed if they don’t exceed the supported Transactions Per Seconds (TPS) of
the remaining inference units. After AWS repairs the Availability Zone, the inference
units are restarted, and full capacity is restored.

If a single inference unit fails, Amazon Lookout for Vision automatically starts a new inference unit in the same Availability Zone.
Model capacity is reduced until the new inference unit starts.
