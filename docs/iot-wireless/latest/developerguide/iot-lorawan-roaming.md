# Managing LoRaWAN traffic from public networks

(Everynet)

You can connect your LoRaWAN devices to the cloud in minutes by using publicly
available LoRaWAN networks. AWS IoT Core for LoRaWAN now supports Everynet’s network coverage in
the US, UK, Ireland, and Spain. When using the public network, you'll be charged a
public network connectivity charge for each device every month. The pricing applies to
all AWS Regions where public network connectivity is offered. For information about
pricing for this feature, see the [AWS IoT Core pricing page](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").

###### Important

The public network is operated and provided as a service directly by Everynet.
Before using this feature, see the applicable [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"). In addition, if you use a
public network through AWS IoT Core for LoRaWAN, certain LoRaWAN device information such as
`DevEUI` and `JoinEUI` will be replicated across regions
where AWS IoT Core for LoRaWAN is available.

AWS IoT Core for LoRaWAN supports the public LoRaWAN network according to the LoRa Alliance
specification for roaming, as described in [LoRaWAN Backend Interfaces 1.0 Specification](https://lora-alliance.org/wp-content/uploads/2020/11/lorawantm-backend-interfaces-v1.0.pdf "https://lora-alliance.org/wp-content/uploads/2020/11/lorawantm-backend-interfaces-v1.0.pdf"). The public network
capability can be used to connect your end devices that are outside the home network. To
support this capability, AWS IoT Core for LoRaWAN partners with Everynet to offer extended radio
coverage.

## Benefits of using a public LoRaWAN

network

Your LoRaWAN devices can use a public network to connect to the cloud, which
reduces the time to deployment, and reduces the time and cost that are required to
maintain a private LoRaWAN network.

By using a public LoRaWAN network, you'll receive benefits such as coverage
extension, running core without radio network, and coverage densification. This
feature can be used to:

- Provide coverage to devices when they move out of their home network, such
  as _Device A_ in figure shown in the [Public LoRaWAN network support
  architecture](lorawan-roaming-works.md#lorawan-roaming-architecture "lorawan-roaming-works.md#lorawan-roaming-architecture") section.
- Extend coverage to devices that don't have a LoRa gateway to connect to,
  such as _Device B_ in figure shown in the
  [Public LoRaWAN network support
  architecture](lorawan-roaming-works.md#lorawan-roaming-architecture "lorawan-roaming-works.md#lorawan-roaming-architecture") section. The device can
  then use the gateway provided by the partner to connect to the home
  network.

Your LoRaWAN devices can use a public network to connect to the cloud using the
roaming feature, which reduces the time to deployment, and reduces the time and cost
that are required to maintain a private LoRaWAN network.

The following sections describe the public network support architecture, how public
LoRaWAN network support works, and how to use this feature.

###### Topics

- [How LoRaWAN public network support
  works](lorawan-roaming-works.md "lorawan-roaming-works.md")
- [How to use AWS IoT Core for LoRaWAN public network
  support](lorawan-roaming-use.md "lorawan-roaming-use.md")
