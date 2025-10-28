# Key AWS services

The key AWS services for performance efficiency include
[Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"),

[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/"),

[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/ "https://aws.amazon.com/iot-device-defender/"),

[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/"),

[AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/"), and

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/"). Amazon CloudWatch provides visibility into your
application's overall performance and operational health. The
following services support performance efficiency for IoT
workloads:

- **Architecture selection:**
  [:AWS hardware partners](https://partners.amazonaws.com/qualified-devices "https://partners.amazonaws.com/qualified-devices") provide production ready IoT
  devices that can be used as part of you IoT application.
  Consider using AWS device software such as AWS device SDK's,
  FreeRTOS, AWS IoT Greengrass for software on IoT devices.
- **Compute and hardware:**
  [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") allows you to run local compute, messaging,
  data caching, synchronization, and ML at the edge. Amazon CloudWatch metrics and Amazon CloudWatch Logs provide metrics,
  logs, filters, alarms, and notifications that you can
  integrate with your existing monitoring solution. These
  metrics can be augmented with device telemetry to monitor your
  application.
- **Data management:**
  [AWS IoT Rules](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") and AWS IoT Core support for MQTT QoS levels
  facilitate data routing, filtering, and prioritization to
  applications.
  [Amazon Kinesis Data Streams](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md") enables real-time ingestion of
  high-velocity IoT data, while Amazon DynamoDB's time-to-live
  (TTL) feature optimizes storage utilization by automatically
  removing expired data.

[Amazon Timestream](https://aws.amazon.com/timestream/ "https://aws.amazon.com/timestream/"), a purpose-built time series database,
offers configurable data retention properties, providing
cost-effective historical data storage in the memory or in the
magnetic store.

[AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/ "https://aws.amazon.com/iot-sitewise/") is a managed service that enables
industrial enterprises to collect, store, organize, and
visualize thousands of sensor data streams across multiple
industrial facilities.

- **Networking and content
  delivery:**
  [AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") is a managed IoT service that supports MQTT, a
  lightweight publish and subscribe protocol for device
  communication. For optimal performance efficiency,

[AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") provides dedicated network connections
for high-throughput IoT workloads. AWS IoT Core's support for
MQTT (both
[v3.1.1](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html "http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html")
and

[v5.0
specifications](http://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html "http://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html"), with

[documented
differences](../../../iot/latest/developerguide/mqtt.md#mqtt-differences "../../../iot/latest/developerguide/mqtt.md#mqtt-differences")) can be complemented by

[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") for RESTful communications and

[AWS AppSync](../../../appsync/latest/devguide/what-is-appsync.md "../../../appsync/latest/devguide/what-is-appsync.md") for GraphQL-based real-time data
synchronization across IoT fleets.

- **Process and culture:**
  [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/") enables inventory control, remote
  device fleet management and updates at scale, while
  [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") provides comprehensive monitoring with
  custom metrics and alarms to proactively identify performance
  bottlenecks across your IoT infrastructure. The
  [AWS IoT Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/ "https://aws.amazon.com/solutions/implementations/iot-device-simulator/") allows simulating large-scale IoT
  deployments for thorough testing.

[AWS IoT Core Jobs](../../../iot/latest/developerguide/iot-jobs.md "../../../iot/latest/developerguide/iot-jobs.md") facilitates reliable over-the-air device
software updates, complemented by

[AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") for automated patch management and
operational tasks.

[AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") offers deep tracing capabilities to analyze and
debug IoT applications, helping identify latency issues across
distributed components.
[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") enables tracking configuration changes that
might affect efficiency.

[Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") can orchestrate automated responses to
operational events, supporting rapid remediation of
performance issues across your IoT landscape.
