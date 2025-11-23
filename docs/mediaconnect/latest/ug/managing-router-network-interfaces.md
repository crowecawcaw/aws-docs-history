# Managing router network interfaces in

MediaConnect

Router network interfaces control how the router communicates with the outside world.
Router I/Os that connect to a public or VPC endpoints need a network interface, which determines
how the router I/O connects to other resources and what security measures protect the connection.
Note that router connections to MediaLive channels and MediaConnect flows are automatically managed and do
not require a network interface.

You can work with two types of router network interface:

- **Public network interfaces** - These allow communication
  over the public internet. They're ideal for connecting to external sources or destinations
  like cameras, encoders, and content delivery platforms. When using public interfaces,
  you must specify allowed IP addresses (CIDRs) for security purposes.
- **VPC network interfaces** - These connect to resources
  within your Amazon Virtual Private Cloud (VPC), and provide private networking within
  AWS. VPC interfaces are best suited for connecting your router to other AWS services
  or resources within your VPC.
  You can use the same router network interface for multiple inputs and outputs on your router.
  This allows you to simplify your network configuration and reduce the number of interfaces
  you need to maintain.

This chapter shows you everything you need to know about working with router network interfaces.

###### Topics

- [Creating a router network interface in
  MediaConnect](creating-router-network-interfaces.md "creating-router-network-interfaces.md")
- [Viewing router network interfaces in
  MediaConnect](viewing-router-network-interfaces.md "viewing-router-network-interfaces.md")
- [Updating a router network interface in
  MediaConnect](editing-router-network-interface.md "editing-router-network-interface.md")
- [Deleting a router network interface in
  MediaConnect](deleting-router-network-interface.md "deleting-router-network-interface.md")
