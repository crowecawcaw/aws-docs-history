# AWS IoT Device Management commands

###### Important

This documentation describes how you can use the [commands feature in AWS IoT Device Management](iot-remote-command-concepts.md#command-iot-namespace "iot-remote-command-concepts.md#command-iot-namespace"). For information about using this feature for
AWS IoT FleetWise, see [Remote
commands](../../../iot-fleetwise/latest/developerguide/remote-commands.md "../../../iot-fleetwise/latest/developerguide/remote-commands.md").

You are solely responsible for deploying commands in a manner that is safe and
compliant with applicable laws. For more information on your responsibilities, please
see the [AWS Service Terms for AWS IoT
Services](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").

Use AWS IoT Device Management Commands to send an instruction from the cloud to a device that's connected to
AWS IoT. Commands target one device at a time and can be used for low-latency,
high-throughput applications, such as retrieving device-side logs or initiating a
device state change.

The _command_ is a reusable resource that's managed by AWS IoT Device Management. It
contains configurations that are applied before they are published to the device. You can
predefine a set of commands for specific use cases, such as turning on a light bulb or
unlocking a vehicle door.

The AWS IoT Commands feature enables you to:

- Create reusable command templates with static or dynamic payloads, then execute them on specific devices.
- Target devices registered as AWS IoT things or unregistered MQTT clients.
- Run multiple commands concurrently on the same device.
- Enable event notifications and track execution status as devices process commands.
  The following topics show you how to create commands, send them to your device, and
  retrieve the status reported by the device.

###### Topics

- [Quick start](iot-commands-quickstart.md "iot-commands-quickstart.md")
- [Commands concepts and status](iot-remote-command-concepts.md "iot-remote-command-concepts.md")
- [High-level commands workflow](iot-remote-command-workflow.md "iot-remote-command-workflow.md")
- [Create and manage commands](iot-remote-command-create-manage.md "iot-remote-command-create-manage.md")
- [Start and monitor command
  executions](iot-remote-command-execution-start-monitor.md "iot-remote-command-execution-start-monitor.md")
- [Deprecate a command resource](iot-remote-command-deprecate.md "iot-remote-command-deprecate.md")
