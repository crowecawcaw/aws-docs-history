# Onboard your gateways to

AWS IoT Core for LoRaWAN

If you're using AWS IoT Core for LoRaWAN for the first time, you can add your first LoRaWAN
gateway and device by using the console.

###### Note

If you're using a public network to connect your LoRaWAN devices to the cloud, you
can skip onboarding your gateways. For more information, see [Managing LoRaWAN traffic from public networks
(Everynet)](iot-lorawan-roaming.md "iot-lorawan-roaming.md").

###### Before onboarding your gateway

Before you onboard your gateway to AWS IoT Core for LoRaWAN, we recommend that you:

- Use gateways that are qualified for use with AWS IoT Core for LoRaWAN. These gateways
  connect to AWS IoT Core without any additional configuration settings and have a
  version 2.0.4 or later of the [LoRa
  Basics Station](https://doc.sm.tc/station/ "https://doc.sm.tc/station/") software running on them. For more information, see
  [Managing gateways with AWS IoT Wireless](lorawan-manage-gateways.md "lorawan-manage-gateways.md").
- Consider the naming convention of the resources that you create so that you
  can more easily manage them. For more information, see [Describing your AWS IoT Wireless
  resources](getting-started.md#iotwireless-describe-resources "getting-started.md#iotwireless-describe-resources").
- Have the configuration parameters that are unique to each gateway ready to
  enter in advance, which makes entering the data into the console go more
  smoothly. The wireless gateway configuration parameters that AWS IoT requires to
  communicate with and manage the gateway include the gateway's EUI and its LoRa
  frequency band.

###### For onboarding your gateways to AWS IoT Core for LoRaWAN:

- [Consider frequency band selection and
  add necessary IAM role](lorawan-rfregion-permissions.md "lorawan-rfregion-permissions.md")
- [Add a gateway to AWS IoT Core for LoRaWAN](lorawan-onboard-gateway-add.md "lorawan-onboard-gateway-add.md")
- [Connect your LoRaWAN gateway and
  verify its connection status](lorawan-gateway-connection-status.md "lorawan-gateway-connection-status.md")
