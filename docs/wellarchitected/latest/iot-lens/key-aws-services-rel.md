# Key AWS services

Use
[Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/ "https://aws.amazon.com/pm/cloudwatch/") to monitor runtime metrics and support
reliability. Other services and features that support the three
areas of reliability are as follows:

**Foundations**:
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") enables you to scale your IoT application without
having to manage the underlying infrastructure. You can scale
[AWS IoT Core](https://aws.amazon.com/iot-core/ "https://aws.amazon.com/iot-core/") by requesting account level limit increases.

**Change management**:
[AWS IoT Device Management](https://aws.amazon.com/iot-device-management/ "https://aws.amazon.com/iot-device-management/") enables you to update devices in the
field while using
[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") to
version firmware, software, and update manifests for devices.
[AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") lets you document your IoT infrastructure as
code and provision cloud resources using a CloudFormation
template.

**Failure management**:
[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
allows you to durably archive telemetry from devices. The
[AWS IoT rules engine](../../../iot/latest/developerguide/iot-rules.md "../../../iot/latest/developerguide/iot-rules.md") Error action enables you to fall back to
other AWS services when a primary AWS service is returning errors.

**Resilience at the edge:**
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ "https://aws.amazon.com/greengrass/") offers several features to help support data
resiliency and backup needs with features which allow devices to
communicate over the local network even after loss in internet
connectivity, allowing the core to receive messages sent while the
core is offline and using stream manager to process data locally
until the connection is restored and send data to cloud or local
storage destinations.
