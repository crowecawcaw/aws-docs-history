# Local network connectivity for Outposts servers

Use this topic to understand the network cabling and topology requirements for hosting an
Outposts server. For more information, see [Local network interfaces for your Outposts servers](local-network-interface.md "local-network-interface.md").

###### Contents

- [Server topology on your network](#lni-topology "#lni-topology")
- [Server physical connectivity](#lni-physical "#lni-physical")
- [Service link traffic for servers](#lni-sl "#lni-sl")
- [Local network interface link traffic](#lni-al "#lni-al")
- [Server IP address assignment](#lni-address "#lni-address")
- [Server registration](#lni-register "#lni-register")

## Server topology on your network

An Outposts server requires two distinct connections to your networking equipment. Each
connection uses a different cable and carries a different type of traffic. The multiple
cables are for traffic-class isolation only, and not for redundancy. The two cables do not
need to connect to a common network.

The following table describes Outposts server traffic types and labels.

| Traffic label | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**         | \*_Service link traffic_<br>• – This traffic<br>enables communication between the Outpost and the AWS Region for both management<br>of the Outpost and intra-VPC traffic between the AWS Region and the Outpost.<br>Service link traffic includes the service link connection from the Outpost to the<br>Region. The service link is a custom VPN or VPNs from the Outpost to the Region.<br>The Outpost connects to the Availability Zone in the Region that you chose at time<br>of purchase. |
| **1**         | \*_Local network interface link traffic_<br>• –<br>This traffic enables communication from your VPC to your local LAN over the local<br>network interface. Local link traffic includes instances running on the Outpost<br>that communicate with your on-premises network. Local link traffic can also<br>include instances communicating with the internet through your on-premises<br>network.                                                                                                |

## Server physical connectivity

Each Outposts server includes non-redundant physical
uplink ports. Ports have their own speed and connector requirements as follows:

- 10Gbe – connector type QSFP+

###### QSFP+ cable

The QSFP+ cable has a connector that you attach to port 3 on the Outposts server. The other
end of the QSFP+ cable has four SFP+ interfaces that you connect to your switch. Two of
the switch-side interfaces are labeled `1` and `2`. Both the
interfaces are required for an Outposts server to function. Use the `2`
interface for service link traffic and the `1` interface for local
network interface link traffic. The remaining interfaces are not used.

## Service link traffic for servers

Configure the service link port on your switch as an untagged access port to a VLAN with
a gateway and a route to the following Region endpoints:

- Service link endpoints
- Outposts registration endpoint

The service link connection must have public DNS available for the Outpost to discover
its registration endpoint in the AWS Region. The connection can have a NAT device between
the Outposts server and the registration endpoint. For more information about the public address
ranges for AWS, see [AWS IP address
ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md") in the _Amazon VPC User Guide_ and [AWS Outposts endpoints and
quotas](../../../general/latest/gr/outposts_region.md "../../../general/latest/gr/outposts_region.md") in the _AWS General Reference_.

To register the server, open the following network ports:

- TCP 443
- UDP 443
- UDP 53

## Local network interface link traffic

Configure the local network interface link port on your upstream network device as a
standard access port to a VLAN on your local network. If you have more than one VLAN,
configure all the ports on the upstream network device as trunk ports. Configure the port on
your upstream network device to expect multiple MAC addresses. Each instance launched on the
server will use a MAC address. Some network devices offer port-security features that will
shut down a port that reports multiple MAC addresses.

###### Note

AWS Outposts servers do not tag VLAN traffic. If you configure your local network interface
as trunk, you must ensure that your OS tags VLAN traffic.

The following example shows how to configure VLAN tagging for your local network
interface on Amazon Linux 2023. If you are using another Linux distribution, see the
documentation for your Linux distribution about configuring VLAN tagging.

###### Example: To configure VLAN tagging for your local network interface on Amazon Linux 2023

and Amazon Linux 2

1. Ensure that the 8021q module is loaded into the kernel. If not, load it using the
   `modprobe` command.

```
modinfo 8021q
modprobe --first-time 8021q
```

2. Create the VLAN device. In this example:
   - The interface name of the local network interface is `ens6`
   - The VLAN id is `59`
   - The name assigned for the VLAN device is `ens6.59`

```
ip link add link ens6 name ens6.59 type vlan id 59
```

3. Optional. Complete this step if you want to manually assign the IP. In this example
   we are assigning the IP 192.168.59.205, where the subnet CIDR is 192.168.59.0/24.

```
ip addr add 192.168.59.205/24 brd 192.168.59.255 dev ens6.59
```

4. Activate the link.

```
ip link set dev ens6.59 up
```

To configure your network interfaces at the OS level and make the VLAN tagging changes
persistent, refer to the following resources:

- If you are using Amazon Linux 2, see [Configure your network interface using
  ec2-net-utils for AL2](../../../linux/al2/ug/ec2-net-utils.md "../../../linux/al2/ug/ec2-net-utils.md") in the _Amazon Linux 2 User Guide_.
- If you are using Amazon Linux 2023, see [Networking service](../../../linux/al2023/ug/networking-service.md "../../../linux/al2023/ug/networking-service.md") in the
  _Amazon Linux 2023 User Guide_.

## Server IP address assignment

You do not need public IP address assignments for the AWS Outposts server's service link and local
network interfaces on instances. For the service link, you can assign IP addresses manually
or use the Dynamic host control protocol (DHCP). To configure the service link connection, see
[Configure and test the connection](../install-server/authorize-3.md "../install-server/authorize-3.md") in the _AWS Outposts server installation
guide_.

To configure the local network interface link, see [Configure the operating system](add-lni.md#os-configuration-lni "add-lni.md#os-configuration-lni").

###### Note

Ensure that you use a stable IP address for the Outposts server. IP address changes can cause
temporary service disruptions on the Outpost subnet.

## Server registration

When Outposts servers establish a connection on the local network, they use the service link
connection to connect to Outpost registration endpoints and register themselves.
Registration requires public DNS. When servers register, they create a secure tunnel to
their service link endpoint in the Region. Outposts servers use TCP port 443 to facilitate
communication with the Region over the public internet. Outposts servers do not support private
connectivity through VPC.
