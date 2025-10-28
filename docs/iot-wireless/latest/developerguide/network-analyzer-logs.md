# View and monitor trace message

logs in real time

If you've added resources to your network analyzer configuration, you can activate
trace messaging to start receiving trace messages for your resources. You can use either
the AWS Management Console, the AWS IoT Wireless API, or the AWS CLI.

## Prerequisites

Before you can activate trace messaging by using network analyzer, you must
have:

- Added the resources that you want to monitor to your default network
  analyzer configuration. For more information, see [Add resources and update the network
  analyzer configuration](network-analyzer-resources.md "network-analyzer-resources.md").
- Generated a presigned request by using the
  `StartNetworkAnalyzerStream` request URL. The request will be
  signed using the credentials for the AWS Identity and Access Management role that makes this request.
  For more information, see [Create a presigned URL](network-analyzer-generate-request.md#network-analyzer-presigned-url "network-analyzer-generate-request.md#network-analyzer-presigned-url").

## Activate trace messaging by

using the console

To activate trace messaging

1. Open the [Network Analyzer hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer "https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer") and choose your
   network analyzer configuration,
   **NetworkAnalyzerConfig_Default**.
2. In the details page of your network analyzer configuration, choose
   **Activate trace messaging** and then choose
   **Activate**.

You'll start receiving trace messages where the newest trace message
appears first in the console.

###### Note

After the messaging session starts, receiving trace messages can incur
additional costs until you deactivate the session or leave the trace
session. For more information about pricing, see [AWS IoT Core pricing](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").

## View and monitor trace

messages

After you activate trace messaging, the WebSocket connection is established and
trace messages start appearing in real time, newest first. You can customize the
preferences to specify the number of trace messages to be displayed in each page and
to display only the relevant fields for each message. For example, you can customize
the trace message log to show only logs for wireless gateway resources that have
**Log level** set to `ERROR`, so that you can
quickly identify and debug errors with your gateways. The trace messages contain the
following information.

- **Message Number**: A unique number that shows the last
  message received first.
- **Resource ID**: The wireless gateway or wireless device
  ID of the resource.
- **Timestamp**: The time when the message was
  received.
- **Message ID**: An identifier that AWS IoT Core for LoRaWAN assigns
  to each received message.
- **FPort**: The frequency port for communicating with the
  device by using the WebSocket connection.
- **DevEui**: The extended unique identifier (EUI) for your
  wireless device.
- **Resource**: Whether the monitored resource is a
  wireless device or a wireless gateway.
- **Event**: The event for a log message for a wireless
  device, which can be **Join**, **Rejoin**,
  **Uplink_Data**, **Downlink_Data**, or
  **Registration**.
- **Log level**:Information about `INFO` or
  `ERROR` log streams for your device.

## Network analyzer JSON log

message

You can also choose one trace message at a time to view the JSON payload for that
message. Depending on the message that you select in the trace message logs, you'll
see information in the JSON payload that indicates contains 2 parts:
**CustomerLog** and **LoRaFrame**.

###### CustomerLog

The **CustomerLog** part of the JSON displays the type and
identifier of the resource that received the message, the log level, and the
message content. The following example shows a **CustomerLog**
log message. You can use the `message` field in the JSON to get more
information about the error and how it can be resolved.

###### LoRaFrame

The **LoRaFrame** part of the JSON has a **Message
ID** and contains information about the physical payload for the
device and the wireless metadata. The wireless metadata also contains
information about the gateway metadata, and whether the trave message was
received from the public network or from a private LoRaWAN gateway.

The following shows examples of the trace message.

The following example shows a sample trace message received using network
analyzer if your devices connect to AWS IoT Core for LoRaWAN using your own private
LoRaWAN gateways. The metadata consists of the ID of the gateway and it's
EUI, and the SNR and RSSI values. These values can help you determine the
strength of your gateway channel and whether to switch to a stronger
channel. For more information about the public network, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

```
{
    "resource_id": "d05bef08-cab2-41bf-b69e-ce306b9a5f81",
    "frame_type": "LoRa",
    "timestamp": "2024-02-15T16:49:35.966023978Z",
    "lora_frame":
     {
        "dev_eui": "4d767373e0ec05c4",
        "message_id": "8e6dcc61-80b6-45c1-89d3-c712cf5603fb",
        "phy_payload": "XXX",
        "wireless_metadata":
        {
            "dev_eui": "4d767373e0ec05c4",
            "m_type": "CONFIRMED_DATA_UP",
            "f_port": 22,
            "data_rate": 3,
            "frequency": 904300000,
            "timestamp": "2024-02-15T16:49:35.966023978Z",
            "lorawan_gateways":
            {
                 "wireless_gateway_id": "d0bfb1d8-b0b6-48f8-b9bb-d0aadf1ab2cf",
                 "gateway_eui": "4b634d3cc5879def",
                 "snr": 5.099999904632568,
                 "rssi": -35
            }
        },
        "dev_addr": "012c58d1"
    }
}
```

The following example shows a sample trace message received using network
analyzer if your devices use the public network to connect to AWS IoT Core for LoRaWAN.
The public network is provided and operated as a service directly by
Everynet. The following example shows the public LoRaWAN network metadata in
the uplink message. The metadata consists of the ID of the gateway and the
network provider (Everynet), whether downlink is allowed, and the SNR and
RSSI values. These values can help you determine the strength of your public
network. For more information about the public network, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

###### Note

The uplink message will mention `public_lorawan_gateways`
to indicate that it's received from the public network and not a private
LoRaWAN gateway.

```
{
    "resource_id": "d05bef08-cab2-41bf-b69e-ce306b9a5f81",
    "frame_type": "LoRa",
    "timestamp": "2024-02-15T16:49:35.966023978Z",
    "lora_frame":
     {
        "dev_eui": "4d767373e0ec05c4",
        "message_id": "8e6dcc61-80b6-45c1-89d3-c712cf5603fb",
        "phy_payload": "XXX",
        "wireless_metadata":
        {
            "dev_eui": "4d767373e0ec05c4",
            "m_type": "CONFIRMED_DATA_UP",
            "f_port": 22,
            "data_rate": 3,
            "frequency": 904300000,
            "timestamp": "2024-02-15T16:49:35.966023978Z",
            "public_lorawan_gateways":
            {
                 "provider_net_id: "0x0000b",
                 "id": "3abe094",
                 "snr": 5.099999904632568,
                 "rssi": -35,
                 "rfregion": US915,
                 "dl_allowed": true
            }
        },
        "dev_addr": "012c58d1"
    }
}
```

If you want to exclude the gateway metadata information from your trace
message, disable the **AddGwMetadata** parameter when you
create the service profile. For information about disabling this parameter,
see [Add service profiles](lorawan-define-profiles.md#lorawan-service-profiles "lorawan-define-profiles.md#lorawan-service-profiles").

The following example shows a trace message with the
`lora_frame` and `customer_log` information and
doesn't contain any gateway information.

```
{
    "resource_id": "d05bef08-cab2-41bf-b69e-ce306b9a5f81",
    "frame_type": "LoRa",
    "timestamp": "2024-02-15T16:49:35.966023978Z",
    "lora_frame":
     {
        "dev_eui": "4d767373e0ec05c4",
        "message_id": "8e6dcc61-80b6-45c1-89d3-c712cf5603fb",
        "phy_payload": "XXX",
        "wireless_metadata":
        {
            "dev_eui": "4d767373e0ec05c4",
            "m_type": "CONFIRMED_DATA_UP",
            "f_port": 22,
            "data_rate": 3,
            "frequency": 904300000,
            "timestamp": "2024-02-15T16:49:35.966023978Z"
        },
        "dev_addr": "012c58d1"
    },
    "customer_log"
    {
        "resource": "WirelessDevice",
        "wireless_device_id":8 "ab0c23d3-b001-45ef-6a01-2bc3de4f5333",
        "wireless_device_type": "LoRaWAN",
        "log_level": "INFO",
        "event": "Uplink_Data",
        "message": "Uplink message received",
        "messageId": "59e7d840-d756-4978-8c64-7f60cfd3fd3b"
     }
}
```

## Review and next steps

In this section, you've viewed trace messages and learned how you can use the
information to debug errors. After you've viewed all messages, you can:

- ###### Deactivate trace messaging

To avoid incurring any additional costs, you can deactivate the trace
messaging session. Deactivating the session disconnects your WebSocket
connection so you won't receive any additional trace messages. You can
still continue viewing the existing messages in the console.

- ###### Edit frame info for your configuration

You can edit the network analyzer configuration and choose whether to
deactivate frame info and choose the log levels for your messages.
Before you update your configuration, consider deactivating your trace
messaging session. To make these edits, open the [Network Analyzer details page in the AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer/details/NetworkAnalyzerConfig_Default "https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer/details/NetworkAnalyzerConfig_Default") and
choose **Edit**. You can then update your
configuration with the new configuration settings and activate trace
messaging to see the updated messages.

- ###### Add resources to your configuration

You can also add more resources to your network analyzer configuration
and monitor them in real time. You can add up to a combined total of 250
wireless gateway and wireless device resources. To add resources, on the
[Network Analyzer details page of the AWS IoT console](https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer/details/NetworkAnalyzerConfig_Default "https://console.aws.amazon.com/iot/home#/wireless/networkAnalyzer/details/NetworkAnalyzerConfig_Default"), choose
the **Resources** tab and choose **Add
resources**. You can then update your configuration with
the new resources and activate trace messaging to see the updated
messages for the additional resources.

For more information about updating your network analyzer configuration by editing
the configuration settings and adding resources, see [Add resources and update the network
analyzer configuration](network-analyzer-resources.md "network-analyzer-resources.md").
