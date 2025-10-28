# Creating or modifying a bond

If you set up more Ethernet interfaces on the Conductor Live node, you can optionally bond two
Ethernet interfaces.

You can bond Ethernet interfaces to suit your networking requirements. For example, you
might set up two Ethernet interfaces as an active/redundant pair.

###### Important

We recommend that when you set up a bond, you set up both eth0 and eth1 with static IP
addresses and with eth0, eth1 and bond0 all on the same subnet.

###### Prerequisites

Before you begin this process, make sure that you have done the following:

- [Set up the individual
  Ethernet interfaces](config-conductor-live-config-ethernet-add.md "config-conductor-live-config-ethernet-add.md") that you want to bond together.
- If HA is currently enabled, disable it now. Conductor Live redundancy (HA or _high availability_) must be disabled before you configure
  Ethernet interfaces. For instructions, see [Disabling Conductor Live HA
  (high availability)](conductor-live-config-ha-chg.md "conductor-live-config-ha-chg.md").

###### Warning

Don't use the web interface to create or modify a bond because you will break the
configuration.

## Step A: Create bond

configuration file

Create a configuration file for the bond interface and name it after the bond.

###### To create the bond configuration file

1. Create the file with the following command.

```
sudo vim /etc/sysconfig/network-scripts/`ifcfg-bond0`
```

2. Insert the following settings in the file:
   - _`DEVICE`_ – Type
     `bond0`.
   - _`TYPE`_ – Type
     `Bond`.
   - _`NAME`_ – Provide a name for the bond
     that is unique among your bonded interfaces, such as
     `bond0`.
   - _`BONDING_MASTER`_ – Type
     `yes`.
   - _`BOOTPROTO`_ – If you are using a
     static IP address for the bond, type `none`. If you are using
     DHCP, type `dhcp`.
   - _`ONBOOT`_ – Type
     `yes`.
   - _`NM_CONTROLLED`_ – Type
     `no`.
   - _`IPADDR`_ – When you are using a static
     IP address, complete with your networking information.
   - _`NETMASK`_ – When you are using a
     static IP address, complete with your networking information.
   - _`GATEWAY`_ – When you are using a
     static IP address, complete with your networking information.
   - _`BONDING_OPTS`_ – Type the bonding mode
     you are using.

###### Bonding modes

The following table describes the bonding modes that are available.

| Bonding mode option | Mode name                             | Description                                                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mode=0              | Round robin                           | Transmissions are received and sent sequentially on each bonded interface, beginning with the first one available.                                                                                                                                                                |
| mode=1              | Active backup                         | Transmissions are received and sent out using the first available bonded interface. The other interface is only used if the active interface fails.                                                                                                                               |
| mode=2              | Balanced XOR                          | Using the exclusive-or (XOR) method, the interface matches up the incoming request's MAC address with the MAC address for one of the bonded interface NICs. When this link is established, transmissions are sent out sequentially, beginning with the first available interface. |
| mode=3              | Broadcast                             | All transmissions are sent on all interfaces in the bond.                                                                                                                                                                                                                         |
| mode=4              | IEEE 802.3ad dynamic link aggregation | This option creates aggregation groups that share the same speed and duplex settings. This transmits and receives on all interfaces in the active aggregator. Requires a switch that is 802.3ad compliant.                                                                        |
| mode=5              | Adaptive transmit load balancing      | Outgoing traffic is distributed according to current load on each interface in the bond. Incoming traffic is received by the currently active interface. If the receiving interface fails, another interface takes over the MAC address of the failed interface.                  |
| mode=6              | Adaptive load balancing               | This option includes transmit and receive load balancing for IPV4 traffic. Receive load balancing is achieved through ARP negotiation.                                                                                                                                            | `DEVICE=bond0 TYPE=Bond NAME=bond0 BONDING_MASTER=yes BOOTPROTO=none ONBOOT=yes NM_CONTROLLED=no IPADDR=192.168.1.70 NETMASK=255.255.255.0 GATEWAY=192.168.1.1 BONDING_OPTS="mode=5 miimon=100"` ## Step B: Edit Ethernet interface configuration files Access the configuration files for each of the interfaces that are participating in the bond. Add the following lines. `MASTER=bond0 SLAVE=yes` For help with creating and updating bonding files through the CLI, see [Using the CLI](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface") in the Red Hat _Networking Guide_. ## Step C: Restart the AWS Elemental service configuration files Restart the AWS Elemental service using the following command. `sudo systemctl restart network` ## Step D: Verify the bond Enter this command to display information about a specific bond: `cat /proc/net/bonding/bond0` In this example, bond0 is correctly set up. `[elemental@host~]$ cat /proc/net/bonding/bond0 Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011) Bonding Mode: transmit load balancing Primary Slave: None Currently Active Slave: eth0 MII Status: up MII Polling Interval (ms): 100 Up Delay (ms): 0 Down Delay (ms): 0 Slave Interface: eth0 MII Status: up Speed: 10000 Mbps Duplex: full Link Failure Count: 0 Permanent HW addr: 00:50:56:b8:64:44 Slave queue ID: 0 Slave Interface: eth2 MII Status: up Speed: 10000 Mbps Duplex: full Link Failure Count: 0 Permanent HW addr: 00:50:56:8d:8e:db Slave queue ID: 0 [elemental@host~]$` |
