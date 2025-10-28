# LoRaWAN

LoRaWAN is suitable for long-range, low power applications
such as smart agriculture, asset tracking and smart cities.

To maximize power savings on a LoRaWAN gateway or device, you
can consider the following configurations:

- Choose the appropriate device class.
  [LoRaWAN](https://lora-alliance.org/about-lorawan/ "https://lora-alliance.org/about-lorawan/")
  defines class A, B, and C device types. These device types
  have different receive window configurations that
  significantly impact the power consumption of a LoRaWAN
  device.
- Where possible use FUOTA (Firmware Update Over The Air)
  over multicast for efficient file transfer to many devices
  receiving the same firmware.
- Choose hardware components, such as processors and radios,
  that have low power consumption to minimize energy usage.
- Position the gateway antenna for maximum coverage and
  signal strength, to reduce the need for high transmit
  power.
- Set the gateway to use a lower transmit power that still
  provides good coverage in the target area. This reduces
  energy usage and can increase the lifetime of the gateway.
- Use Listen Before Talk (LBT) and Adaptive Data Rate (ADR)

* these features can help minimize the number of
  retransmissions and collisions, which can reduce energy
  usage.

- Configure the gateway to use the appropriate packet size
  and data rate for the application. Large packet sizes and
  high data rates can increase energy usage.
- Configure the gateway to use deep sleep mode when it is
  not actively transmitting or receiving data. This can
  significantly reduce energy usage.
