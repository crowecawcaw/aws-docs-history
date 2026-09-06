

# Connecting to an Amazon Neptune cluster over a private network
<a name="get-started-connect-private-net"></a>

You can access a Neptune DB cluster from a private network in two different ways:
+ Using an [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connection.
+ Using an [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) connection.

The links above have information about these connection methods and how to set them up. The configuration of an AWS Site-to-Site connection might look like this:

![Diagram of accessing a Neptune cluster from a private network.](http://docs.aws.amazon.com/neptune/latest/userguide/images/VPC-connection-04.png)
