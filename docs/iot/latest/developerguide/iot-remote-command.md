# AWS IoT Device Management commands

###### Important

This documentation describes how you can use the [commands feature in AWS IoT Device Management](iot-remote-command-concepts.md#command-iot-namespace "iot-remote-command-concepts.md#command-iot-namespace"). For information about using this feature for
AWS IoT FleetWise, see [Remote
commands](../../../iot-fleetwise/latest/developerguide/remote-commands.md "../../../iot-fleetwise/latest/developerguide/remote-commands.md").

You are solely responsible for deploying commands in a manner that is safe and
compliant with applicable laws. For more information on your responsibilities, please
see the [AWS Service Terms for AWS IoT
Services](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").

Use AWS IoT Device Management commands to send an instruction from the cloud to a device that's connected to
AWS IoT. Commands target one device at a time, and can be used for low-latency,
high-throughput applications, such as to retrieve the device-side logs, or to initiate a
device state change.

The _command_ is a reusable resource that's managed by AWS IoT Device Management. It
contains configurations that are applied before they are published onto the device. You can
pre-define a set of commands for specific use cases, such as turning on a light bulb or
unlocking a vehicle door.

By using the AWS IoT commands feature, you can:

- Create a command resource and reuse its configuration to send a command multiple
  times to your target device.
- Target a device that has been registered as an AWS IoT thing, or an MQTT client that
  has not been registered in AWS IoT.
- Run multiple commands concurrently on the target device without overloading the
  device.
- Enable notifications for commands events, and retrieve and track the status from
  the device as it runs the command to completion.
  The following topics show you how to create commands, send them to your device, and
  retrieve the status reported by the device.

###### Topics

- [Commands concepts and status](iot-remote-command-concepts.md "iot-remote-command-concepts.md")
- [High level commands workflow](iot-remote-command-workflow.md "iot-remote-command-workflow.md")
- [Create and manage commands](iot-remote-command-create-manage.md "iot-remote-command-create-manage.md")
- [Start and monitor command
  executions](iot-remote-command-execution-start-monitor.md "iot-remote-command-execution-start-monitor.md")
- [Deprecate a command resource](iot-remote-command-deprecate.md "iot-remote-command-deprecate.md")
