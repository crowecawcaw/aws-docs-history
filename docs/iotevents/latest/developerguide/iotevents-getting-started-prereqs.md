End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Prerequisites to get started with

AWS IoT Events

If you don't have an AWS account, create one.

1. Follow the step in [Setting up AWS IoT Events](iotevents-start.md "iotevents-start.md")
   to ensure proper account setup and permissions.
2. Create two Amazon Simple Notification Service (Amazon SNS) topics.

This tutorial (and the corresponding example) assume that you created two Amazon SNS
topics. The ARNs of these topics are shown as:
`arn:aws:sns:us-east-1:123456789012:underPressureAction` and
`arn:aws:sns:us-east-1:123456789012:pressureClearedAction`.
Replace these values with the ARNs of Amazon SNS topics that you create. For more information,
see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

As an alternative to publishing alerts to Amazon SNS topics, you can have the detectors
send MQTT messages with a topic that you specify. With this option, you can verify that
your detector model is creating instances and that those instances are sending alerts by
using the AWS IoT Core console to subscribe to and monitor messages sent to those MQTT
topics. You can also define the MQTT topic name dynamically at runtime by using an input
or variable created in the detector model. 3. Choose an AWS Region that supports AWS IoT Events. For more information, see [AWS IoT Events](../../../general/latest/gr/rande.md#iotevents_region "../../../general/latest/gr/rande.md#iotevents_region") in the
_AWS General Reference_. For help, see [Getting started
with a service in the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/start-service.md "../../../awsconsolehelpdocs/latest/gsg/start-service.md") in the
_Getting Started with the AWS Management Console_.
