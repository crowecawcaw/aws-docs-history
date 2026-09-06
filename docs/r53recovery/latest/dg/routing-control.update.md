

# Viewing and updating routing control states in ARC
<a name="routing-control.update"></a>

This section describes how to view and update routing control states in Amazon Application Recovery Controller (ARC). Routing controls are simple on-off switches that manage traffic flow to cells in your recovery group. Cells are typically AWS Regions, or sometimes Availability Zones, that includes your resources. When a routing control state is `On`, traffic flows to the cell that is controlled by that routing control. 

You group routing controls into control panels, which are logical failover groupings. When you open a control panel on the console, for example, you can view all of the routing controls for a grouping at once, to see where traffic is flowing.

You can update a routing control state on the ARC console or by using the ARC API. We recommend that you update routing control states by using the API. First, ARC offers extreme reliability with the API in the data plane to perform these actions. That's important when you're changing these states because routing state changes fail over across cells by rerouting application traffic. In addition, by using the API, you can try connecting to different cluster endpoints in rotation, as needed, if a cluster endpoint that you try connecting to is unavailable.

You can update one routing control state, or you can update several routing control states at once. For example, you might want to set one routing control state to `Off` to stop traffic from flowing to one cell, such as an Availability Zone where an application is experiencing increased latency. At the same time, you might want to set another routing control state to `On` to start traffic flowing to another cell or Availability Zone. In this scenario, you can update both routing control states at the same time, so traffic continues to flow.

**Topics**
+ [Getting and updating routing control states using the ARC API (recommended)](routing-control.update.api.md)
+ [Getting and updating routing control states in the AWS Management Console](routing-control.update.console.md)