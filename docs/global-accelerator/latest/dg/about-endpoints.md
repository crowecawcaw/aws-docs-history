#

Transition endpoints with client IP address preservation

If you haven't yet configured client IP address preservation for the endpoints in your accelerator,
follow the guidance in this section add and transition one or more endpoints to
endpoints that preserve the user’s client IP address. You can choose to transition an Application Load Balancer, Network Load Balancer with security groups, or an Elastic
IP address endpoint to a corresponding endpoint—a corresponding load balancer endpoint or an
EC2 instance endpoint—that has client IP address preservation.

This section explains how to add and transition endpoints by using the AWS Global Accelerator console. If you
want to use API operations with Global Accelerator, see the [AWS Global Accelerator API Reference](../api/Welcome.md "../api/Welcome.md").

##

Transitioning endpoints to use client IP address preservation

We recommend that you transition endpoints to using client IP address preservation slowly.

- **Add the new endpoint:** First, add to Global Accelerator the new load balancer or
  EC2 instance endpoints that you enable to preserve the client IP address.
- **Slowly increase traffic:** Then, slowly move traffic from existing endpoints
  to the new endpoints by configuring weights on the endpoints.
- **Test as you go:** After you move a small amount of traffic to the new endpoint
  with client IP address preservation, test to make sure that your configuration is working as you expect it to.
  Then gradually increase the proportion of traffic to the new endpoint by adjusting the
  weights on the corresponding endpoints.

Follow the steps in the following sections to transition your endpoints.

Client IP address preservation is supported in all AWS Regions where Global Accelerator is supported. For a list of
supported Regions, see [AWS Region availability for AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").

###### Important

Before you begin to route traffic to endpoints that preserve the client IP address, make sure
that all the configurations in which you’ve included Global Accelerator client IP addresses on allow lists
are updated to include the user client IP address instead.

## To add an endpoint with client

IP address preservation

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. On the Accelerators page, choose an accelerator.
3. In the **Listeners** section, choose a listener.
4. In the **Endpoint group** section, choose an endpoint group.
5. In the **Endpoints** section, choose **Add endpoint**.
6. On the **Add endpoints** page, in the **Endpoints**
   drop-down menu, choose an endpoint that supports client IP address preservation.
7. In the **Weight** field, choose a low number compared to the weights that are set
   for your existing endpoints. For example, if the weight for a corresponding Application Load Balancer is 255, you could
   enter a weight of 5 for the new Application Load Balancer, to start with. For more information, see [How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").
8. If needed, under **Preserve client IP address**, select **Preserve address**.
9. Choose **Save changes**.

Next, follow the steps here to edit the corresponding existing endpoints (that you're replacing with the new endpoints with
client IP address preservation) to reduce the weights for existing endpoints so that less traffic goes to them.

## To reduce traffic for the existing endpoints

1. On the **Endpoint group** page, choose an existing endpoint that doesn't have client IP address
   preservation.
2. Choose **Edit**.
3. On the **Edit endpoint** page, in the **Weight** field,
   enter a lower number than the current number. For example, if the weight for an existing endpoint is 255, you could
   enter a weight of 220 for the new endpoint (with client IP address preservation).
4. Choose **Save changes**.

After you’ve tested with a small portion of the original traffic by setting the weight for
the new endpoint to a low number, you can slowly transition all the traffic by continuing
to adjust the weights for the original and new endpoints.

For example, say you start with an existing Application Load Balancer with a weight set to 200, and you add a
new Application Load Balancer endpoint with client IP address preservation enabled with a weight set to 5.
Gradually shift traffic from the original Application Load Balancer to the new Application Load Balancer by increasing the
weight for the new Application Load Balancer and decreasing the weight for the original Application Load Balancer. For example:

- Original weight → 190 new weight 10
- Original weight 180 → new weight 20
- Original weight 170 → new weight 30, and so on.

When you have decreased the weight to 0 for the original endpoint, all traffic (in this
example scenario) goes to the new Application Load Balancer endpoint, which includes client IP address preservation.

If you have additional endpoints—load balancers or EC2 instances—that you want to
transition to use client IP address preservation,
repeat the steps in this section to transition them.

If you need to revert your configuration for an endpoint so that traffic to the endpoint
doesn't preserve the client IP address, you can do that at any time: increase the weight
for the endpoint that does _not_ have client IP address preservation
to the original value, and decrease the weight for the endpoint
_with_ client IP address preservation to 0.
