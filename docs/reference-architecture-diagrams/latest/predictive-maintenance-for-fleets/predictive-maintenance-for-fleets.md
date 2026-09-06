

# Predictive Maintenance for Fleets
<a name="predictive-maintenance-for-fleets"></a>

Publication date: **October 21, 2020 ([Diagram history](#fleet-history))**

With this architecture, you can predict battery failures in your vehicle fleet. Train a predictive model on historical telemetry data, then run it against live telemetry. Schedule controlled maintenance events before failures occur. The solution uses [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for vehicle connectivity, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for model training and deployment, and [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) for prediction storage.

## Fleet predictive maintenance diagram
<a name="fleet-diagram"></a>

![Reference architecture diagram showing how to predict fleet battery failures by using AWS IoT Core, SageMaker AI, Lambda, and Amazon Aurora.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/predictive-maintenance-for-fleets/images/predictive-maintenance-for-fleets.png)


The following steps describe the ML pipeline and notification flow for this architecture:

1. Create an extract from the Fleet Management system. Include vehicle data and historical sensor logs.

1. Deploy the SageMaker AI model after training it to predict battery failures.

1. Send sensor logs from connected vehicles to AWS IoT Core. You can also send logs by using the HTTP interface.

1. Send telemetry messages from AWS IoT Core to [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for analysis by the model.

1. Send the sensor logs to Lambda for analysis. Run the trained model against the data.

1. Use Lambda with the trained prediction model on sensor logs to generate predictions.

1. Store completed predictions in Amazon Aurora for record-keeping and future model improvements.

1. Display predictions on the [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) dashboard.

1. Send real-time failure warning notifications to [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

1. Notify connected vehicles through Amazon SNS to alert drivers and fleet managers. Schedule a controlled maintenance event before the predicted failure.

## Further reading
<a name="fleet-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="fleet-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#fleet-history) | Reference architecture diagram first published. | October 21, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.