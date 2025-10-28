# Connecting iSCSI Initiators

When managing your gateway, you work with volumes or virtual tape library (VTL) devices
that are exposed as Internet Small Computer System Interface (iSCSI) targets. For
Volume Gateways, the iSCSI targets are volumes. For Tape Gateways, the targets are VTL
devices. As part of this work, you do such tasks as connecting to those targets, customizing
iSCSI settings, connecting from a Red Hat Linux client, and configuring Challenge-Handshake
Authentication Protocol (CHAP).

###### Topics

- [Connecting to your volumes from a Windows
  client](ConfiguringiSCSIClient.md "ConfiguringiSCSIClient.md")
- [Connecting your volumes to
  a Linux client](ConfiguringiSCSIClientInitiatorRedHatClient.md "ConfiguringiSCSIClientInitiatorRedHatClient.md")
- [Customizing iSCSI Settings](recommendediSCSISettings.md "recommendediSCSISettings.md")
- [Configuring CHAP Authentication
  for Your iSCSI Targets](ConfiguringiSCSIClientInitiatorCHAP.md "ConfiguringiSCSIClientInitiatorCHAP.md")
  The iSCSI standard is an Internet Protocol (IP)–based storage networking standard
  for initiating and managing connections between IP-based storage devices and clients. The
  following list defines some of the terms that are used to describe the iSCSI connection and
  the components involved.

**iSCSI initiator**

The client component of an iSCSI network. The initiator sends requests to the
iSCSI target. Initiators can be implemented in software or hardware. Storage Gateway
only supports software initiators.

**iSCSI target**

The server component of the iSCSI network that receives and responds to
requests from initiators. Each of your volumes is exposed as an iSCSI target.
Connect only one iSCSI initiator to each iSCSI target.

**Microsoft iSCSI initiator**

The software program on Microsoft Windows computers that allows you to connect
a client computer (that is, the computer running the application whose data you
want to write to the gateway) to an external iSCSI-based array (that is, the
gateway). The connection is made using the host computer's Ethernet network
adapter card. The Microsoft iSCSI initiator has been validated with Storage Gateway on
Windows Server 2022. The initiator is built into the operating system.

**Red Hat iSCSI initiator**

The `iscsi-initiator-utils` Resource Package Manager (RPM)
package provides you with an iSCSI initiator implemented in software for Red Hat
Linux. The package includes a server daemon for the iSCSI protocol.

Each type of gateway can connect to iSCSI devices, and you can customize those
connections, as described following.
