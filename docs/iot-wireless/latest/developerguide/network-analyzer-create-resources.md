# Create network analyzer

configuration and add resources

Before you can stream trace messages, create a network analyzer configuration and add
the resources you want to monitor to this configuration. A LoRaWAN network analyzer
configuration is a set of settings and rules that define how network analyzer should
capture and analyze traffic in a LoRaWAN network. It specifies the types of information
and messages that should be included in the network trace, and any filtering or
processing rules that should be applied.

a LoRaWAN network analyzer configuration providesvisibility into the communication
between LoRaWAN devices and the network server. This enables troubleshooting,
performance monitoring, and security analysis of the LoRaWAN network.

When you create a configuration, you can:

- Specify a configuration name and optional description.
- Customize the configuration settings such as frame info and level of detail
  for your log messages.
- Add the resources that you want to monitor. The resources can be wireless
  devices or wireless gateways, or both.
  The configuration settings that you specify will determine the trace messaging
  information that you'll receive for resources you add to the configuration. You may also
  want to create multiple configurations depending on your monitoring use case.

The following shows how to create a configuration and add resources.

###### Topics

- [Create a network analyzer
  configuration](network-analyzer-create.md "network-analyzer-create.md")
- [Add resources and update the network
  analyzer configuration](network-analyzer-resources.md "network-analyzer-resources.md")
