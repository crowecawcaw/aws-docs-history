# Network Interfaces in Amazon AppStream 2.0

Each AppStream 2.0 streaming instance has the following network interfaces:

- The customer network interface provides connectivity to the resources
  within your VPC, as well as the internet, and is used to join the streaming
  instance to your directory.
- The management network interface is connected to a secure AppStream 2.0
  management network. It is used for interactive streaming of the streaming
  instance to a user's device, and to allow AppStream 2.0 to manage the
  streaming instance.
  AppStream 2.0 selects the IP address for the management network interface from the following
  private IP address range: 198.19.0.0/16. Do not use this range for your VPC CIDR or
  peer your VPC with another VPC with this range, as this might create a conflict and
  cause streaming instances to be unreachable. Also, do not modify or delete any of
  the network interfaces attached to a streaming instance, as this might also cause
  the streaming instance to become unreachable.
