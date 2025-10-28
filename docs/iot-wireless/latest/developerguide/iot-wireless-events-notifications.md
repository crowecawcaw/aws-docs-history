# Event notifications for wireless

resources

You can use the AWS Management Console or AWS IoT Wireless API operations to notify you of events
for your Sidewalk devices, and your LoRaWAN devices and gateways. For information about
event notifications and how to enable them, see [Event notifications for AWS IoT Wireless](iot-wireless-events.md "iot-wireless-events.md") and [Enable events for wireless
resources](iot-wireless-control-events.md "iot-wireless-control-events.md").

## Event notifications for LoRaWAN

resources

Events that you can enable for your LoRaWAN resources include:

- Join events that notify you of join events for your LoRaWAN device. You'll
  receive notifications when a device joins with AWS IoT Core for LoRaWAN, or when a
  rejoin request of type 0 or type 2 is received.
- Connection status events that notify you when the connection status of
  your LoRaWAN gateway changes to connected or disconnected.

## Event notifications for Sidewalk

resources

Events that you can enable for your Sidewalk resources include:

- Device events that notify you of changes to the state of your Sidewalk
  device, such as when the device has been registered and is ready to
  use.
- Proximity events that notify you when AWS IoT Wireless receives a
  notification from Amazon Sidewalk that a beacon has been discovered or
  lost.
- Message delivery status events that notify you about the status of
  messages that are exchanged between your Sidewalk devices and
  AWS IoT Wireless.

The following sections contain more information about the events for your LoRaWAN and
Sidewalk resources.

###### Topics

- [Enable notifications for LoRaWAN join
  events](iot-lorawan-join-events.md "iot-lorawan-join-events.md")
- [Enable notifications for LoRaWAN
  gateway connection status events](iot-lorawan-gateway-events.md "iot-lorawan-gateway-events.md")
- [Enable notifications for Sidewalk
  device registration state events](iot-sidewalk-device-events.md "iot-sidewalk-device-events.md")
- [Enable notifications for Sidewalk
  proximity events](iot-sidewalk-proximity-events.md "iot-sidewalk-proximity-events.md")
- [Enable notifications for
  message delivery status events](iot-sidewalk-message-delivery-events.md "iot-sidewalk-message-delivery-events.md")
