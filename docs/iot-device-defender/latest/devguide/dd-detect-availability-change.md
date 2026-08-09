# AWS IoT Device Defender detect feature availability change

The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. Existing AWS IoT Device Defender detect customers can continue using the feature.

As an active customer using the AWS IoT Device Defender detect feature, you can continue using rules detect
and ML detect as normal. The detect feature is going into maintenance mode starting August
31, 2026, which means no new capabilities will be added to detect and it will not be
available to new customers. AWS remains committed to providing security updates and maintaining feature
availability to ensure your monitoring workflows continue to run smoothly.

###### Note

The AWS IoT Device Defender audit feature continues to be fully available. Only the detect feature
(rules detect and ML detect) is entering maintenance mode and will no longer be available
to new customers starting August 31, 2026.

## AWS IoT Device Defender detect alternatives

### Self-managed alternative for cloud-side metrics

Detailed instructions and sample code are available in the [IoT
Device Anomaly Detection](https://github.com/aws-samples/sample-iot-device-anomaly-detection "https://github.com/aws-samples/sample-iot-device-anomaly-detection") project on the GitHub website. With this
open-source, serverless pipeline, you can replicate functionality similar to the
AWS IoT Device Defender detect feature for cloud-side metrics monitoring in your own AWS
account. It is built on AWS
serverless services including AWS IoT, Amazon Managed Service for Apache Flink,
AWS Lambda, Amazon Kinesis, Amazon SageMaker AI, Amazon DynamoDB, Amazon API Gateway, Amazon Simple Notification Service, and Amazon CloudWatch. The
project includes an AWS Serverless Application Model (SAM) template that
allows you to deploy the pipeline in your account within minutes, a REST API for
security profile management, and support for both rule-based thresholds and
machine-learning-based (ML) anomaly detection. You can tune the metrics
sliding-window interval to trade off detection latency against cost.

#### Key differences from AWS IoT Device Defender detect

- The sample code is an open-source software pipeline that you deploy and
  operate in your own AWS account. It is not an AWS-managed
  service.
- It covers cloud-side metrics out of the box. Device-side metrics and
  custom metrics require extending the pipeline as described in the
  project's README.
- Configuration is managed through a REST API and does not include AWS
  Management Console integration.
- Mitigation actions (for example, quarantining a device to a thing group
  or replacing a certificate) are not included. However, you can implement
  these by subscribing an Lambda function to the project's Amazon SNS alert
  topic.
- Improvements over the AWS IoT Device Defender detect feature:

  - **Customizable** – The
    fully customizable pipeline allows you to add dimensions, adjust
    aggregation windows, or extend detection logic without service
    limitations.
  - **Cost control** – The
    sample code provides levers to optimize costs based on the desired
    metrics. The pipeline enables you to leverage existing rules and supports
    messages published to AWS IoT rules basic ingest topics or to the AWS IoT
    message broker. You can also control the sliding window interval for
    metrics evaluation to trade off higher latency for lower costs. For ML
    metrics, the pipeline is also more cost effective at scale than ML detect
    because it runs on fixed infrastructure rather than incurring
    per-datapoint costs.
  - **Simplified monitoring**
    – The sample code replaces per-security-profile CloudWatch
    metrics with a single aggregated metric across the fleet for
    simplified monitoring, while maintaining device-level behavioral
    detection.
  - **Improved ML model
    granularity** – Unlike ML detect, which
    trains a single ML model across all behaviors within a security
    profile, the sample code trains a separate model per behavior.
    This gives each model a more focused baseline for a single
    metric's distribution and ensures that any failures in the model
    for one behavior do not affect detection accuracy for
    others.

### Open-source device agents for device-side metrics

To collect device-side metrics (such as listening TCP and UDP ports, established
TCP connections, destination IP addresses, and packet or byte counters), you can run
an open-source agent on your devices and publish the metrics to AWS IoT over MQTT.
Options include the [AWS IoT Device Client](https://github.com/awslabs/aws-iot-device-client "https://github.com/awslabs/aws-iot-device-client"), [Telegraf](https://github.com/influxdata/telegraf "https://github.com/influxdata/telegraf") (using its MQTT
output plugin), or [osquery](https://github.com/osquery/osquery "https://github.com/osquery/osquery")
combined with an Eclipse Paho MQTT client. The GitHub project README also
includes instructions on how to ingest the device-published metrics through AWS IoT
rules and extend the security profile schemas provided in the sample code.

## Frequently asked questions

What does this mean for the AWS IoT Device Defender detect feature?

The AWS IoT Device Defender detect feature will no longer be available to new customers
starting August 31, 2026. The feature will continue to operate for existing
customers, but there will be no further development of additional
functionality.

How are existing customers impacted?

Existing customers will not experience any disruption to their workloads.
They can continue using the AWS IoT Device Defender detect feature as normal, and security
updates will continue to be deployed to maintain feature reliability. There
is no impact to security posture and workflows.

When do I need to migrate to the self-managed alternative?

The AWS IoT Device Defender detect feature remains available to existing customers in
maintenance mode. You will receive [advance
notice](../../../general/latest/gr/service-lifecycle.md "../../../general/latest/gr/service-lifecycle.md") if any changes to feature
availability are planned. If you are interested in a more customizable
solution, explore the self-managed alternative.

Is AWS IoT Device Defender audit affected?

No. Only the detect feature is entering maintenance mode. The AWS IoT Device Defender audit
feature continues to be fully available.

Can I migrate gradually?

Yes. You can deploy the sample code in your account and run it alongside
AWS IoT Device Defender detect. Both evaluate the same AWS IoT data, so you can compare
results and migrate security profiles incrementally.

How can I get help if I have issues?

If you are experiencing issues, contact [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support").
