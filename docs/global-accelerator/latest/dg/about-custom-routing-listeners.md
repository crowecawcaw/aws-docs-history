# Listeners for custom routing accelerators in Global Accelerator

For a custom routing accelerator in AWS Global Accelerator, you configure a listener that specifies a range of listener ports
with associated protocols that Global Accelerator maps to specific destination Amazon EC2 instances in your VPC subnet endpoints.
When you add a VPC subnet endpoint, Global Accelerator creates a static port mapping between the port ranges that you define for
your listener and the destination IP addresses and ports in the subnet.
Then you can use the port mapping to specify your accelerator static IP addresses together with a
listener port and protocol to direct user traffic to specific destination Amazon EC2 instance IP addresses and ports
in your VPC subnet.

You define a listener when you create your custom routing accelerator, and you can add more listeners at any time. Each listener
can have one or more endpoint groups, one for each AWS Region in which you have VPC subnet endpoints. A
listener in a custom routing accelerator supports both TCP and UDP protocols. You specify the protocol or protocols for each
destination port range that you define: UDP, TCP, or both UDP and TCP.

For more information, see [How custom routing accelerators work in Global Accelerator](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md").

###### Contents

- [Add listener](about-custom-routing-listeners.md "about-custom-routing-listeners.md")
- [Edit listener](about-custom-routing-listeners.md "about-custom-routing-listeners.md")
- [Remove listener](about-custom-routing-listeners.md "about-custom-routing-listeners.md")
