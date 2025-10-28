# Transit gateway registrations in AWS Global Networks for Transit Gateways

You can register your existing transit gateways with a global network. Any transit gateway
attachments (such as VPCs, VPN connections, and AWS Direct Connect gateways) are automatically included in
your global network.

## Transit gateway limitations

Note the following about registering transit gateways in a global network:

- A transit gateway must first be created in Amazon Virtual Private Cloud (VPC) before it can be
  registered in a global network. For more information about transit gateways and creating
  one, see [Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in the _Amazon VPC Transit Gateways User Guide_.
- You can have multiple global networks, but you can only register one transit gateway
  with one global network.
- You can register transit gateways that are in the same AWS account as the global
  network.
- You cannot create, delete, or modify your transit gateways and their attachments using
  the Network Manager console or APIs. To work with transit gateways, use the Amazon VPC console or the
  Amazon EC2 APIs.

###### Transit gateway registration tasks

- [Register a transit gateway](register-tgw.md "register-tgw.md")
- [View registered transit gateways](view-registered-tgws.md "view-registered-tgws.md")
- [Deregister a transit gateway](deregister-tgw.md "deregister-tgw.md")
