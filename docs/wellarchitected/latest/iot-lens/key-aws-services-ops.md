# Key AWS services

Several services can be used to drive operational excellence for
your IoT application. The AWS Device Qualification Program helps
you select hardware components that have been designed and tested
for AWS IoT interoperability. Qualified hardware can get you to
market faster and reduce operational friction. AWS IoT Core offers
features used to manage the initial onboarding of a device. With
AWS IoT Greengrass, you can run custom computes, such as AWS Lambda functions and Docker containers on the device to respond
quickly to local events, interact with local resources, and
process data to minimize the cost of transmitting data to the
cloud and simplify remote application management. AWS IoT Device Management reduces the operational overhead of performing
fleet-wide operations, such as device grouping and searching. In
addition, Amazon CloudWatch is used for monitoring IoT metrics,
collecting logs, generating alerts, and triggering responses.
Other services and features that support the four areas of
operational excellence are as follows:

- **Preparation: AWS IoT Device Tester
  (IDT) for FreeRTOS and AWS IoT Greengrass** is a test
  automation tool for connected devices to determine if your
  devices running FreeRTOS or AWS IoT Greengrass can
  interoperate with AWS IoT Services.
- **Preparation: AWS IoT Core**
  supports provisioning and onboarding your devices in the
  field, including registering the device identity using
  just-in-time provisioning, just-in-time registration, or
  Multi-Account Registration. Devices can then be associated
  with their metadata and device state using the device registry
  and the Device Shadow.
- **Operations**:
  **AWS IoT thing registry groups and
  Fleet Indexing** allow you to quickly develop an
  organizational structure for your devices and search across
  the current metadata of your devices to perform recurring
  device operations. Amazon CloudWatch allows you to monitor the
  operational health of your devices and your application.
- **Operations: AWS IoT Greengrass** provides many pre-built capabilities on
  the device to help you focus mostly on their business logic
  and offers many foundational infrastructure and operation
  features such as remote application management.
- **Responses**:
  **AWS IoT Jobs** enables you to
  proactively push updates to one or more devices such as
  firmware updates or device configuration. AWS IoT rules engine
  allows you to inspect IoT messages as they are received by AWS IoT Core and immediately respond to the data, at the most
  granular level. AWS IoT Device Defender enable you to
  proactively trigger notifications or remediation based on
  real-time analysis, real-time security and data thresholds
  with Device Defender.
