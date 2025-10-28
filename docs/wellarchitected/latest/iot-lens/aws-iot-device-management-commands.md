# AWS IoT Device Management Commands

AWS IoT Device Management Commands feature enables customers to send remote commands to IoT devices at scale, facilitating remote monitoring, control and diagnostics. Devices subscribe to MQTT topics to receive user-defined payload from the cloud. The commands feature support delivering messages to reserved MQTT topics and for added flexibility, the target resource can be either a ThingName or a ClientID (for devices not registered in the IoT registry). Each command is a reusable AWS resource that supports granular permissions controls — you can authorize users to send specific commands targeting individual devices. If a command execution needs to be initiated within a specific time frame, you can configure them to expire after a defined timeout period. You have full visibility into command execution through status tracking, and you can optionally configure notifications to be alerted when the command state changes. Command is well suited for remotely sending specific instructions, triggering actions or modifying device configurations on-demand. Common use cases include retrieving device logs, initiating changes to device states, and allowing end users to remotely control devices through web application or a companion app, such as turning lights on and off or starting the air conditioner or fan.

To send commands using Commands feature, see the following diagram:

![Sending commands to devices using AWS IoT Device Management Commands feature](images/image4.png)
_Sending commands to devices using AWS IoT Device Management Commands feature_

1. A device subscribes to the commands topic
   `$aws/commands/things/<thingname>/executions/#/request` or
   `$aws/commands/clients/<clientId>/executions/#/request` upon which IoT commands payload will be delivered.
2. Create pre-defined commands and store them in AWS IoT Device Management Commands for reusability.
3. A user initiates a commands execution through user
   application, which publishes command payload to the request
   topic.
4. The device performs the actions specified by the commands
   execution.
5. The device publishes command execution progress and updates
   status through
   `$aws/commands/things/<thingname>/executions/<executionid>/response` or
   `$aws/commands/clients/<clientId>/executions/<executionid>/response` topic.
6. Commands publish update notifications through
   `$aws/events/commandExecutions/<CommandId>/#`. The user
   can configure AWS IoT rules to receive notifications
   optionally.
