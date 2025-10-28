# Commands

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

This documentation describes how to use the [commands feature for AWS IoT FleetWise](remote-command-concepts-states.md#commands-iotfw-namespace "remote-command-concepts-states.md#commands-iotfw-namespace"). For information about using the commands
feature in AWS IoT Device Management, see [commands](../../../iot/latest/developerguide/iot-remote-command.md "../../../iot/latest/developerguide/iot-remote-command.md").

You are solely responsible for deploying commands in a manner that is safe and
compliant with applicable laws. For more information on your responsibilities, please
see the [AWS Service Terms for AWS IoT
Services](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/").

Use the commands feature to execute commands on a vehicle from the cloud. Commands
target one device at a time, and can be used for low-latency, high-throughput applications,
such as to retrieve the device-side logs, or to initiate a device state change.

The _command_ is a resource that's managed by AWS IoT Device Management. It contains
reusable configurations that are applied when sending a command execution to the vehicle.
You can pre-define a set of commands for specific use cases, or use them to create reusable
configurations for recurrent use cases. For example, you can configure commands that can be
used by an App to lock a vehicle's door or to change the temperature remotely.

Using the AWS IoT commands feature, you can:

- Create a command resource and reuse the configuration to send multiple commands to
  your target device and then execute them on the device.
- Control the granularity with which you want each command to be executed on the
  device. For example, you can provision a vehicle as an AWS IoT thing, and then send a
  command to lock or unlock the doors of the vehicle.
- Run multiple commands concurrently on the target device without waiting for the
  previous one to be completed.
- Choose to enable notifications for commands events, and retrieve the status and
  result information from the device as it runs the command and once it's
  completed.
  The following topics show you how to create, send, receive, and manage commands.

###### Topics

- [Commands concepts](remote-command-concepts-states.md "remote-command-concepts-states.md")
- [Vehicles and commands](remote-command-vehicles.md "remote-command-vehicles.md")
- [Create and manage commands](create-manage-remote-command-cli.md "create-manage-remote-command-cli.md")
- [Start and monitor command
  executions](send-monitor-remote-command-cli.md "send-monitor-remote-command-cli.md")
- [Example: Using commands to control a vehicle
  steering mode (AWS CLI)](remote-command-tutorial.md "remote-command-tutorial.md")
- [Command usage scenarios](remote-command-use-cases.md "remote-command-use-cases.md")
