# Connect your Sidewalk

device and view uplink metadata format

In this tutorial, you'll use the MQTT test client to test the connectivity and see
messages exhanged between your end device and the AWS Cloud. To receive messages, in
the MQTT test client, subscribe to the topic specified when creating the IoT rule for
your destination. You can also send a downlink message from AWS IoT Core for Amazon Sidewalk to your
device using the `SendDataToWirelessDevice` API operation. You can verify
that the message was delivered by enabling the message delivery status event
notification.

###### Note

For information about connecting your hardware platform and setting it up, see
[Provisioning and
registering your end device](https://docs.sidewalk.amazon/provisioning/ "https://docs.sidewalk.amazon/provisioning/") and [Setting up the hardware development kit (HDK)](https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-hdk.html "https://docs.sidewalk.amazon/getting-started/sidewalk-onboard-prereq-hdk.html") in the _Amazon Sidewalk documentation_..

## Send downlink messages to your end

device

Use the [`SendDataToWirelessDevice`](../apireference/API_SendDataToWirelessDevice.md "../apireference/API_SendDataToWirelessDevice.md") API operation or the [`send-data-to-wireless-device`](../../../cli/latest/reference/iotwireless/send-data-to-wireless-device.md "../../../cli/latest/reference/iotwireless/send-data-to-wireless-device.md") CLI command to send
downlink messages from AWS IoT Core for Amazon Sidewalk to your Sidewalk end device. Following
shows an example of how to run this command. The payload data is the binary to be
sent, encoded in base64.

```
aws iotwireless send-data-to-wireless-device \
    --id `"<Wireless_Device_ID>"` \
    --payload-data `"SGVsbG8gVG8gRGV2c2lt"` \
    --wireless-metadata Sidewalk=`{Seq=1,AckModeRetryDurationSecs=10}`
```

Following shows a sample output of running this command, which is an ID of the
downlink message sent to the device.

```
{
    MessageId: `"6011dd36-0043d6eb-0072-0008"`
}
```

###### Note

The `SendDataToWirelessDevice` API can return a message ID but the
message might not be successfully delivered. To check the status of the message
that was sent to the device, you can enable message delivery status events for
your Sidewalk accounts and devices. For information about how to enable
this event, see [Event notifications for Sidewalk
resources](iot-wireless-events-notifications.md#iot-sidewalk-events "iot-wireless-events-notifications.md#iot-sidewalk-events"). For more information about this event
type, see [Message delivery events](../../../iot/latest/developerguide/iot-sidewalk-message-delivery-events.md "../../../iot/latest/developerguide/iot-sidewalk-message-delivery-events.md").

## View format of uplink messages from

the device

After you've connected your device, you can subscribe to the topic (for example,
`project/sensor/observed`) that you
specified when creating the destination rule, and observe uplink messages from the
device.

If you specified a topic name when creating your destination, you can subscribe to
the topic to monitor uplink messages from your end device. Go to the [MQTT test client](https://console.aws.amazon.com/iot/home#/test "https://console.aws.amazon.com/iot/home#/test") on the
**Test** page of the AWS IoT console, enter the topic name (for
example, `project/sensor/observed`), and then
choose **Subscribe**.

The following example shows the format of the uplink messages that are sent from
Sidewalk devices to AWS IoT. The `WirelessMetadata` contains
metadata about the message request.

```
{
   "PayloadData":`"ZjRlNjY1ZWNlNw=="`,
   "WirelessDeviceId":`"wireless_device_id"`,
   "WirelessMetadata":{
      "Sidewalk":{
         "CmdExStatus":"Cmd",
         "SidewalkId":"`device_id`",
         "Seq":0,
         "MessageType":"`messageType`",
         "Timestamp": "2024-10-21T19:33:01.295912052Z"
      }
    }
}

```

The following table shows a definition of the different parameters in the uplink
metadata. The `device-id` is the ID of the
wireless device, such as `ABCDEF1234` and the
`messageType` is the type of uplink
message that's received from the device.

| Sidewalk uplink metadata parameters | Parameter                                                                                                                                                                    | Description      | Type | Required |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---- | -------- |
| `PayloadData`                       | The message payload that is sent from the wireless device.                                                                                                                   | String           | Yes  |
| `WirelessDeviceID`                  | The identifier of the wireless device that's sending the<br>data                                                                                                             | String           | Yes  |
| `Sidewalk.CmdExStatus`              | Command runtime status. Response-type messages shall include<br>the status code, `COMMAND_EXEC_STATUS_SUCCESS`.<br>However, notifications might not include the status code. | Enumeration      | No   |
| `Seq`                               | The message sequence number.                                                                                                                                                 | Integer          | Yes  |
| `Sidewalk.NackExStatus`             | Response nack status, which can be `RADIO_TX_ERROR`<br>or `MEMORY_ERROR`.                                                                                                    | Array of strings | No   |
| `Timestamp`                         | The time when the Sidewalk device sent an uplink<br>request.                                                                                                                 | Timestamp        | Yes  |
