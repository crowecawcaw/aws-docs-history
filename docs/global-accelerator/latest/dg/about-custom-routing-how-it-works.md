# How custom routing accelerators work in Global Accelerator

By using a custom routing accelerator in AWS Global Accelerator, you can use application logic to directly
map one or more users to a specific destination among many destinations while still
gaining the performance benefits of Global Accelerator. A custom routing accelerator maps listener port ranges to EC2 instance
destinations in Amazon VPC (VPC) subnets. This allows Global Accelerator to deterministically
route traffic to a specific Amazon EC2 private IP address and port destination in your subnet.

For example, you can use a custom routing accelerator with an online real-time gaming application in which you
assign multiple players to a single session on an Amazon EC2 game server based on factors that you choose,
such as geographic location, player skill, and game mode. Or you might have a VoIP or social media
application that assigns multiple users to a specific media server for voice, video, and
messaging sessions.

Your application can call a Global Accelerator API and receive a full static mapping of Global Accelerator ports and their
associated destination IP addresses and ports. You can save that static mapping, and then your
matchmaking service use it to route users to specific destination EC2 instances. You don't have
to make any modifications to your client software to start using Global Accelerator with your application.

To configure a custom routing accelerator, you select a VPC subnet endpoint. Then you define a destination port range that
incoming connections will be mapped to, so your software can listen on the same set
of ports across all instances. Global Accelerator creates a static mapping that allows your matchmaking service to
translate a destination IP address and port number for a session to an external IP address and
port that you give to users.

Your application’s network stack might operate over a single transport protocol, or perhaps
instead you use UDP for fast delivery and TCP for reliable delivery. You can set UDP, TCP, or both UDP and TCP
for each destination port range, to give you maximum flexibility without having to duplicate
your configuration for each protocol.

###### Note

By default, all VPC subnet destinations in a custom routing accelerator aren't allowed to receive traffic. This is
to be secure by default, and also to give you granular control over which private EC2 instance
destinations in your subnet are allowed to receive traffic. You can allow or deny traffic to
the subnet, or to specific IP address and port combinations (destination sockets). For more information, see
[Add a VPC subnet endpoint for a custom routing accelerator](about-custom-routing-endpoints-adding-endpoints.md "about-custom-routing-endpoints-adding-endpoints.md"). You can also specify destinations
by using the Global Accelerator API. For more information, see
[AllowCustomRoutingTraffic](../api/API_AllowCustomRoutingTraffic.md "../api/API_AllowCustomRoutingTraffic.md") and
[DenyCustomRoutingTraffic](../api/API_DenyCustomRoutingTraffic.md "../api/API_DenyCustomRoutingTraffic.md").
