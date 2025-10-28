# Working with custom routing accelerators in AWS Global Accelerator

This chapter includes information about how a custom routing accelerator in AWS Global Accelerator works, and how to configure accelerators,
listeners, endpoint groups, and VPC subnet endpoints for a custom routing accelerator.

A custom routing accelerator lets you use application logic to directly map one or more users to a specific Amazon EC2
instance among many destinations, while gaining the performance
improvements of routing your traffic through Global Accelerator. This is useful when you have an application that
requires a group of users to interact with each other on the same session running on a specific EC2
instance and port, such as gaming applications or Voice over IP (VoIP) sessions.

Endpoints for custom routing accelerators must be Amazon VPC (VPC) subnets, and a custom routing accelerator can only
route traffic to Amazon EC2 instances in those subnets. When you create a custom routing accelerator, you can
include thousands of Amazon EC2 instances running in a single or multiple VPC subnets. To learn more,
see [How custom routing accelerators work in Global Accelerator](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md").

###### Note

If you want Global Accelerator to instead automatically choose the closest healthy endpoint to your clients, create a standard accelerator.
For more information, see [Working with standard accelerators in AWS Global Accelerator](work-with-standard-accelerators.md "work-with-standard-accelerators.md").

To set up custom routing accelerator, you do the following:

1. Review the guidelines and requirements for creating a custom routing accelerator.
   See [Guidelines and restrictions for custom routing accelerators](about-custom-routing-guidelines.md "about-custom-routing-guidelines.md").
2. Create a VPC subnet. You can add EC2 instances to the subnet at any time after adding
   the subnet to Global Accelerator.
3. Create an accelerator in Global Accelerator. Select the option for a custom routing accelerator.
4. Add a listener in which you specify a range of ports for Global Accelerator to listen on. Make sure that you include
   a large range with enough ports for Global Accelerator to map to all the destinations that you expect
   to have. These ports are distinct from destination ports, which you specify in the next step.
   For more information about listener port requirements, see
   [Guidelines and restrictions for custom routing accelerators](about-custom-routing-guidelines.md "about-custom-routing-guidelines.md").
5. Add one or more endpoint groups for AWS Regions in which you have VPC subnets. You specify
   the following for each endpoint group:
   - An endpoint port range, which represents the ports on your destination EC2 instances that will be able to
     receive traffic.
   - The protocol for each destination port range: UDP, TCP, or both UDP and TCP.

6. For the endpoint subnet, select a subnet ID. You can add multiple subnets in each endpoint group
   and subnets can be different sizes (up to /17).
   The following sections explain how custom routing accelerators work, and provide steps for creating and working with custom routing accelerators and their
   components, including listeners, endpoint groups, and VPC subnet endpoints.

###### Topics

- [How custom routing accelerators work](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md")
- [Custom routing example](about-custom-routing-how-it-works.md "about-custom-routing-how-it-works.md")
- [Custom routing guidelines](about-custom-routing-guidelines.md "about-custom-routing-guidelines.md")
- [Custom routing accelerators](about-custom-routing-accelerators.md "about-custom-routing-accelerators.md")
- [Listeners for custom routing accelerators](about-custom-routing-listeners.md "about-custom-routing-listeners.md")
- [Endpoint groups for custom routing accelerators](about-custom-routing-endpoint-groups.md "about-custom-routing-endpoint-groups.md")
- [VPC subnet endpoints](about-custom-routing-endpoints.md "about-custom-routing-endpoints.md")
