# Monitoring of LoRaWAN resources using network

analyzer

Network analyzer uses a default WebSocket connection to receive real-time trace message
logs for your wireless connectivity resources. By using network analyzer, you can add the
resources you want to monitor, activate a trace messaging session, and start receiving trace
messages in real time.

To monitor your resources, you can also use Amazon CloudWatch. To use CloudWatch, you set up an IAM
role to configure logging and then wait for the log entries to be displayed in the console.
Network analyzer significantly reduces the time that it takes to set up a connection and
start receiving trace messages, providing you with just-in-time log information for your
fleet of resources. For information about monitoring by using CloudWatch, see [Monitoring your AWS IoT Wireless resources using
Amazon CloudWatch Logs](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

By reducing your setup time and using the information from the trace messages, you can
monitor your resources more effectively, get meaningful insights, and troubleshoot errors.
You can monitor both LoRaWAN devices and LoRaWAN gateways. For example, you can quickly
identify a join error when onboarding one of your LoRaWAN devices. To debug the error, use
the information in the provided trace message log.

###### How to use network analyzer

To monitor your resource fleet and start receiving trace messages, perform the
following steps

1. ###### Create network analyzer configuration and add resources

Before you can activate trace messaging, create a network analyzer
configuration and add resources to your configuration. First, specify the
configuration settings, which include log levels and wireless device frame
information. Then, add the wireless resources you want to monitor by using the
wireless gateway and wireless device identifiers. 2. ###### Stream trace messages with WebSockets

You can generate a presigned request URL using the credentials for your IAM
role to stream network analyzer trace messages by using the WebSocket
protocol. 3. ###### Activate trace messaging session and monitor trace messages

To start receiving trace messages, activate your trace messaging session. To
avoid incurring additional costs, you can either deactivate or close your
network analyzer trace messaging session.
The following video describes how AWS IoT Core for LoRaWAN network analyzer works and walks you
through the process of adding resources and tracing join activities using network
analyzer.

The following topics show how to create your configuration, add resources, and activate
your trace messaging session.

###### Topics

- [Add necessary IAM role for network
  analyzer](network-analyzer-iam.md "network-analyzer-iam.md")
- [Create network analyzer
  configuration and add resources](network-analyzer-create-resources.md "network-analyzer-create-resources.md")
- [Stream network analyzer trace messages with
  WebSockets](network-analyzer-api.md "network-analyzer-api.md")
- [View and monitor trace message
  logs in real time](network-analyzer-logs.md "network-analyzer-logs.md")
- [Debug and troubleshoot your multicast
  groups and FUOTA tasks using network analyzer](lorawan-network-analyzer-fuota.md "lorawan-network-analyzer-fuota.md")
