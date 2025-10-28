# Step 5: Connect your Outposts server to your network

To complete the network setup, you connect the server to your upstream networking device
with network cable.

Consider the following information about connecting to the network:

- The server requires connections for two types of traffic: service link traffic and local
  network interface (LNI) link traffic. The instructions in the following section describe
  which ports to use on the server to segment traffic. Consult with your IT group to determine
  which port on your upstream networking device should carry each type of traffic.
- Ensure the server has connected to your upstream networking device and has been assigned
  an IP address. For more information, see [Server IP address
  assignment](../server-userguide/local-server.md#lni-address "../server-userguide/local-server.md#lni-address") in the _AWS Outposts User guide for servers_.
- The optical connection on an AWS Outposts server only supports 10 Gbits and does not support
  auto-negotiation of port speed. If the host port tries to negotiate port speed, for example,
  between 10 through 25 Gbits, you can run into problems. In such cases, we recommend you do
  the following:
  - Set the port speed on the switch port to 10 Gbits.
  - Work with your switch vendor to support a static configuration.

###### Tasks

- [Configure the QSFP network for your Outposts server](connect-2.md "connect-2.md")
