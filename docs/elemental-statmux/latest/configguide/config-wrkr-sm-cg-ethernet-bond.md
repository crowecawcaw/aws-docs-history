This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Bond Ethernet Devices

You can bond Ethernet devices to suit your networking requirements. For example, you might
set-up two Ethernet devices as an active/redundant pair.

###### Perform the following steps from the command line.

- [Step A: Create Bond Configuration
  File](#config-wrkr-sm-cg-ethernet-bond-create "#config-wrkr-sm-cg-ethernet-bond-create")
- [Step B: Edit Ethernet Interface Configuration Files](#config-wrkr-sm-cg-ethernet-bond-assign "#config-wrkr-sm-cg-ethernet-bond-assign")
- [Step C: Restart the AWS Elemental Service Configuration Files](#config-wrkr-sm-cg-ethernet-bond-restart "#config-wrkr-sm-cg-ethernet-bond-restart")
- [Step D: Verify the Bond](#config-wrkr-sm-cg-ethernet-bond-verify "#config-wrkr-sm-cg-ethernet-bond-verify")
  For help creating and updating bonding files through the CLI, see [Using the CLI](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface") in the Red Hat _Networking Guide_.

###### Important

We recommend that when setting up a bond, you set up both eth0 and eth1 with static IP addresses and with eth0, eth1 and bond0 all on the same subnet.

###### Prerequisites

Before you begin this process, make sure that you've done the following:

- [Added to AWS Elemental Statmux the Ethernet devices](config-wrkr-sm-cg-ethernet-add.md "config-wrkr-sm-cg-ethernet-add.md") that you're bonding.

## Step A: Create Bond Configuration

File

Create a configuration file for the bond interface and name it after the bond.

###### To create the bond configuration file

1. Create the file with the following command.

```
sudo vim /etc/sysconfig/network-scripts/`ifcfg-bond0`
```

2. Insert the following settings in the file:
   - _`DEVICE`_ – Type `bond0`.
   - _`TYPE`_ – Type `Bond`.
   - _`NAME`_ – Provide a name for the bond that's unique
     among your bonded interfaces, such as `bond0`.
   - _`BONDING_MASTER`_ – Type
     `yes`.
   - _`BOOTPROTO`_ – If you're using a static IP address
     for the bond, type `none`. If you're using DHCP, type
     `dhcp`.
   - _`ONBOOT`_ – Type `yes`.
   - _`NM_CONTROLLED`_ – Type
     `no`.
   - _`IPADDR`_ – When you're using a static IP address,
     complete with your networking information.
   - _`NETMASK`_ – When you're using a static IP address,
     complete with your networking information.
   - _`GATEWAY`_ – When you're using a static IP address,
     complete with your networking information.
   - _`BONDING_OPTS`_ – Type the bonding mode you're using
     and other applicable options.

   For a list of additional options, see [Creating a Network Bond in CentOS7 and RHEL7 from the CLI](https://community.elemental.com/docs/DOC-3976 "https://community.elemental.com/docs/DOC-3976").

###### Bonding modes

The following table describes the bonding modes that are available.

| Bonding Mode Option | Mode Name                             | Description                                                                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mode=0              | Round robin                           | Transmissions are received and sent sequentially on each bonded interface,<br>beginning with the first one available.                                                                                                                                                                      |
| mode=1              | Active backup                         | Transmissions are received and sent out via the first available bonded<br>interface. The other interface is only used if the active interface<br>fails.                                                                                                                                    |
| mode=2              | Balanced XOR                          | Using the exclusive-or (XOR) method, the interface matches up the incoming<br>request's MAC address with the MAC address for one of the bonded interface NICs.<br>Once this link is established, transmissions are sent out sequentially, beginning<br>with the first available interface. |
| mode=3              | Broadcast                             | All transmissions are sent on all interfaces in the bond.                                                                                                                                                                                                                                  |
| mode=4              | IEEE 802.3ad dynamic link aggregation | This option creates aggregation groups that share the same speed and duplex settings. This<br>transmits and receives on all interfaces in the active aggregator. Requires a<br>switch that is 802.3ad compliant.                                                                           |
| mode=5              | Adaptive transmit load balancing      | Outgoing traffic is distributed according to current load on each interface<br>in the bond. Incoming traffic is received by the currently active interface. If<br>the receiving interface fails, another interface takes over the MAC address of<br>the failed interface.                  |
| mode=6              | Adaptive load balancing               | This option includes transmit and receive load balancing for IPV4 traffic. Receive load<br>balancing is achieved through ARP negotiation.                                                                                                                                                  |

###### Example

```
DEVICE=bond0
TYPE=Bond
NAME=bond0
BONDING_MASTER=yes
BOOTPROTO=none
ONBOOT=yes
NM_CONTROLLED=no
IPADDR=192.168.1.70
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
BONDING_OPTS="mode=5 miimon=100"
```

## Step B: Edit Ethernet Interface Configuration Files

Access the configuration files for each of the interfaces that are participating in the bond. Add the following lines.

```
MASTER=bond0
SLAVE=yes
```

For help creating and updating bonding files through the CLI, see [Using the CLI](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-network_bonding_using_the_command_line_interface") in the Red Hat _Networking Guide_.

## Step C: Restart the AWS Elemental Service Configuration Files

Restart the AWS Elemental service using the following command.

```
sudo systemctl restart network
```

## Step D: Verify the Bond

Verify that your bond is running using the following command.

```
cat /proc/net/bonding/bond0
```

###### Example Functioning bond interface

```
[elemental@host~]$ cat /proc/net/bonding/bond0
Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

Bonding Mode: transmit load balancing
Primary Slave: None
Currently Active Slave: eth0
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

Slave Interface: eth0
MII Status: up
Speed: 10000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:50:56:b8:64:44
Slave queue ID: 0

Slave Interface: eth2
MII Status: up
Speed: 10000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: 00:50:56:8d:8e:db
Slave queue ID: 0
[elemental@host~]$
```
