# Manage Ethernet devices

When you installed each AWS Elemental Live in the cluster, you configured
eth0. You can now set up eth1 and any additional Ethernet devices.
Optionally, you can also bond two devices that you have set up.

When you installed Elemental Live, you configured eth0 as the
management interface. Note that setting up a device as the management
interface does _not_ dedicate this device to management
traffic. The device can still handle other traffic.

###### Topics

- [Create an Ethernet device](#config-wrkr-cf-cg-ethernet-add "#config-wrkr-cf-cg-ethernet-add")
- [Modify an Ethernet device](#config-live-ethernet-modify "#config-live-ethernet-modify")

## Create an Ethernet device

To create Ethernet devices use the CLI. For detailed information, see [Using the CLI](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface") in the Red Hat _Networking Guide_.

## Modify an Ethernet device

You must not modify Ethernet devices via the web interface. Instead, use the CLI. For more
information, see [Using the CLI](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface") in the Red Hat _Networking Guide_.

###### Warning

The **Devices** page on the Elemental Live web interface includes the
pencil icon that lets you edit the Ethernet device. However, you must not use the web
interface to modify devices because you will break the configuration.
