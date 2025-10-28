# Working with standard accelerators in AWS Global Accelerator

This chapter includes procedures and recommendations for creating standard accelerators in AWS Global Accelerator, including
configuring accelerators, listeners, endpoint groups, and endpoints. With a
standard accelerator, Global Accelerator chooses the closest healthy endpoint for your traffic.

If instead you want to use custom application logic to
direct one or more users to a specific endpoint among many endpoints, create a custom routing accelerator.
For more information, see [Working with custom routing accelerators in AWS Global Accelerator](work-with-custom-routing-accelerators.md "work-with-custom-routing-accelerators.md").

To set up a standard accelerator, do the following:

1. Create an accelerator, and choose the standard accelerator option.
2. For **Address type**, select **IPv4** or **Dual-stack**.
3. Optionally, configure static IP addresses with bring your own IP address.
4. Add a listener with a specific set of ports or port range, and choose the protocol
   to accept: TCP or UDP.
5. Add one or more endpoint groups, one for each AWS Region in which you have endpoint resources.
6. Add one or more endpoints to the endpoint groups. This isn't required, but traffic won't be routed
   if you don't have any endpoints. To learn about the types of endpoints and requirements, see
   [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").
   The following sections provide steps for adding, deleting, and configuring standard accelerators and their
   components, including listeners, endpoint groups, and endpoints.

###### Topics

- [Standard accelerators in AWS Global Accelerator](about-accelerators.md "about-accelerators.md")
- [Listeners for standard accelerators in AWS Global Accelerator](about-listeners.md "about-listeners.md")
- [Endpoint groups for standard accelerators in AWS Global Accelerator](about-endpoint-groups.md "about-endpoint-groups.md")
- [Endpoints for standard accelerators in AWS Global Accelerator](about-endpoints.md "about-endpoints.md")
