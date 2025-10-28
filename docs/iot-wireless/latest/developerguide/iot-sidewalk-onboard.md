# Connecting to AWS IoT Core for Amazon Sidewalk

This section shows you how to onboard your Sidewalk end device and then connect
your device to the Sidewalk network. It describes the steps that you perform in the
onboarding tutorial, as mentioned in [Introduction to onboarding your Sidewalk
devices](sidewalk-getting-started.md#sidewalk-gs-workflow "sidewalk-getting-started.md#sidewalk-gs-workflow"). You'll learn how to onboard devices by using the
AWS IoT console and the AWS IoT Core for Amazon Sidewalk API operations. You'll also learn about the AWS CLI
commands that perform these operations.

## Prerequisites

To add your end device and destination to AWS IoT Core for Amazon Sidewalk, you must set up your
AWS account. To perform these operations using the AWS IoT Wireless API or the AWS CLI
commands, you must also set up the AWS CLI. For more information about the prerequisites
and setting up, see [Installing Python and Python3-pip](getting-started.md#wireless-onboard-prereq "getting-started.md#wireless-onboard-prereq").

###### Note

To perform the entire onboarding workflow for provisioning and registering your
end device, and connecting to your hardware development kit (HDK), you must also set
up your Sidewalk gateway and HDK. For more information, see [Setting up the hardware development kit (HDK)](https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-hdk.html "https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-hdk.html") and [Setting up a Sidewalk gateway](https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-gateway.html "https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-gateway.html") in the _Amazon Sidewalk documentation_.

## Describing your Sidewalk

resources

Before you get started and create the resources, we recommend that you consider the
naming convention of your Sidewalk end devices, device profiles, and destinations.
AWS IoT Core for Amazon Sidewalk assigns a unique identifier to the resources that you create. However,
you can give them more descriptive names, add a description, or add optional tags to
help identify and manage them.

###### Note

The destination name can't be changed after it's created. Use a name that's unique
to your AWS account and AWS Region.

For more information, see [Describing your AWS IoT Wireless
resources](getting-started.md#iotwireless-describe-resources "getting-started.md#iotwireless-describe-resources").

###### Topics

- [Add your device to AWS IoT Core for Amazon Sidewalk](iot-sidewalk-create-device.md "iot-sidewalk-create-device.md")
- [Add a destination for your
  Sidewalk end device](iot-sidewalk-qsg-destination.md "iot-sidewalk-qsg-destination.md")
- [Connect your Sidewalk
  device and view uplink metadata format](iot-sidewalk-connect-uplink-metadata.md "iot-sidewalk-connect-uplink-metadata.md")
