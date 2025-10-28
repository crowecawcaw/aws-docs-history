# Modifying an Ethernet

interface

You use the CLI to modify Ethernet interfaces using the web interface.

- If the node is a Conductor Live node and if HA is currently enabled, disable it now. Conductor Live
  redundancy (HA, or _high availability_) must be disabled
  before you configure network interfaces. For instructions, see [Disabling Conductor Live HA
  (high availability)](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md").
- To modify an Ethernet interface, see the [Red Hat _Networking Guide_](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_ifcg_files "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ip_networking_with_ifcg_files").

###### Warning

The **Devices** page on the Conductor Live web interface includes the pencil
icon that lets you edit the Ethernet interface. However, you must not use the web interface
to modify interfaces because you will break the configuration.
