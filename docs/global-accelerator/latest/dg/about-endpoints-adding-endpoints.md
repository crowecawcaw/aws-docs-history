#

Add a standard endpoint

You add endpoints to endpoint groups so that traffic can be directed to your resources. You
can edit a standard endpoint to change the weight for the endpoint. Or you can remove an
endpoint from your accelerator by removing it from an endpoint group. Removing an endpoint
doesn't affect the endpoint itself, but Global Accelerator can no longer direct traffic to that
resource.

You must create a resource first, and then you can add it as an endpoint in Global Accelerator.
A resource must be valid and active when you add it as an endpoint. For detailed information
about the endpoint types and configurations that Global Accelerator supports,
see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

One reason that you might add or remove endpoints from endpoint groups is usage. For example, if demand on your application
increases, you can create more resources. Then, you can add more endpoints to one or more endpoint groups to
handle the increased traffic. Global Accelerator starts routing requests to an endpoint as soon as you add it and the
endpoint passes the initial health checks.

You can manage traffic to endpoints by adjusting the weights
on an endpoint, to send proportionally more or less traffic to the endpoint. For more information, see
[How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").

Note: if you're considering adding an endpoint with client IP address preservation, first review the information in
[Preserve client IP addresses in AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").

This section explains how to add endpoints on the AWS Global Accelerator console. If you want to
use API operations with AWS Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

# To add a standard endpoint

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. On the **Accelerators** page, choose an accelerator.
3. In the **Listeners** section, for **Listener ID**,
   choose the ID of a listener.
4. In the **Endpoint groups** section, for **Endpoint group
   ID**, choose the ID of the endpoint group that you want to add an
   endpoint to.
5. Choose **Edit**.
6. In the **Endpoints** section, choose **Add endpoint**.
7. On the **Add endpoints** page, choose a resource from the dropdown
   list.

If you don't have any AWS resources, there aren't any items in the list. To continue, create
AWS resources such as load balancers, Amazon EC2 instances, or Elastic IP addresses. Then come
back to the steps here, and choose a resource from the list.

###### Note

If you have a dual-stack accelerator, you must add a dual-stack endpoint. Network Load Balancers, Application Load Balancers,
and Amazon EC2 instances can be added as dual-stack endpoints. 8. Optionally, for **Weight**, enter a number from 0 to 255 to set a weight
for routing traffic to this endpoint. When you add weights to endpoints, you configure Global Accelerator to
route traffic based on proportions that you specify. By default, all endpoints have a weight of 128.
For more information, see [How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md"). 9. Optionally, enable client IP address preservation for the endpoint. Under
**Preserve client IP address**, select **Preserve
address**. For more information, see [Preserve client IP addresses in AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").

###### Note

Before you add and begin to route traffic to endpoints that preserve the client IP address, make sure
that all your required security configurations, for example, security groups, are updated to include the user client
IP address on allow lists. 10. Choose **Add endpoint**.
