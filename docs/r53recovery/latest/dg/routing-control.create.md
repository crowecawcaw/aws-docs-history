

# Creating routing control components in ARC
<a name="routing-control.create"></a>

This section explains how to create a cluster, routing controls, health checks, and control panels for working with routing control in Amazon Application Recovery Controller (ARC).

Start by creating a cluster, to host your routing controls and the control panels that you use to group them. Then create routing controls and health checks so you can reroute traffic to fail over from one cell to another, so that traffic goes to your backup replica, for example.

Note that you are charged by the hour for each cluster that you create. You typically only need one cluster to host the routing controls and control panels for recovery control management for an application. In addition, you can set up resource sharing by using AWS Resource Access Manager, so that one cluster can host routing controls and other ARC resources owned by multiple AWS accounts. To learn about resource sharing in ARC, [Support cross-account for clusters in ARC](routing-control.failover-different-accounts.md). For pricing information, see [Amazon Application Recovery Controller (ARC) Pricing](https://aws.amazon.com/application-recovery-controller/pricing/).

To use routing controls to fail over traffic, you create routing control health checks that you associate with Amazon Route 53 DNS records for resources in your application. As an example, let's say you have two cells, one that you've configured as the primary cell for your application, and the other that you've configured as the secondary, to fail over to. 

To set up health checks for failover, do the following:

1. Create a routing control for each cell.

1. Create a health check for each routing control.

1. Create two DNS records, for example, two DNS failover records, and associate a health check with each one.

Another scenario when you might create a routing control is when you create a safety rule that is a gating rule. In this case, you don't associate health checks and DNS records with the routing control because you will use it as a *gating routing control*. For more information, see [Creating safety rules for routing control](routing-control.safety-rules.md).

The steps to create the components for routing control on the ARC console are included in these sections. To learn about using recovery control configuration API operations with ARC, see the [Routing control API operations](actions.routing-control.md).