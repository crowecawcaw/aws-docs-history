# Site-to-Site VPN attachments in AWS Cloud WAN

Attaching a Site-to-Site VPN connection to your core network edge, first requires that you create a
Site-to-Site VPN connection with **Target Gateway Type** set to **Not
Associated**. See [Create an AWS Cloud WAN
Site-to-Site VPN attachment](../../../vpn/latest/s2svpn/create-cwan-vpn-attachment.md "../../../vpn/latest/s2svpn/create-cwan-vpn-attachment.md") in the _AWS Site-to-Site VPN User Guide_.

###### Note

- Your Site-to-Site VPN must be attached to a core network before you can start configuring a
  customer gateway. AWS doesn't provision these endpoints until the Site-to-Site VPN is
  attached to the core network.
- A Site-to-Site VPN attachment must be created in the same AWS account that owns the core
  network.

###### Topics

- [Create a Site-to-Site VPN attachment](cloudwan-vpn-attachment-add.md "cloudwan-vpn-attachment-add.md")
- [View or edit a Site-to-Site VPN attachment](cloudwan-attachments-viewing-editing-vpn.md "cloudwan-attachments-viewing-editing-vpn.md")
