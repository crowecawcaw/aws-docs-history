# Creating a routing control

health check in ARC

You associate a routing control health check with each routing control that you want to use for rerouting traffic.
Then you configure each health check with a Amazon Route 53 DNS record, for example, a failover DNS record. Then you can
reroute traffic in Amazon Application Recovery Controller (ARC) simply by updating the state of the associated routing control, to set it to
`On` or `Off`.

###### Note

You can't edit an existing routing control health check to associate it with a different routing control.

# To create a routing control health check

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Routing control**.
3. On the **Routing control** page, choose a routing control.
4. On the **Routing control** detail page, choose a
   **Create health check**.
5. Enter a name for the health check, and then choose **Create**.
   Next, you create Route 53 DNS records, and associate your routing control health checks with each one. For example,
   let's assume that you want to use two DNS failover records to associate your routing control health checks with.
   For ARC to correctly fail over traffic by using routing controls, start by creating the two failover records
   in Route 53: a primary and a secondary. For more information about configuring
   DNS failover records, see [Health checking concepts](../../../Route53/latest/DeveloperGuide/route-53-concepts.md#route-53-concepts-health-checking "../../../Route53/latest/DeveloperGuide/route-53-concepts.md#route-53-concepts-health-checking").

When you create the primary failover record, the values should be something like the following:

```

			Name: myapp.yourdomain.com
			Type: CNAME
			Set Identifier: Primary
			Failover: Primary
			TTL: 0
			Resource Records:
			Value: cell1.yourdomain.com
			Health Check ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

The secondary failover record values should be something like the following:

```

			Name: myapp.yourdomain.com
			Type: CNAME
			Set Identifier: Secondary
			Failover: Secondary
			TTL: 0
			Resource Records:
			Value: cell2.yourdomain.com
			Health Check ID: xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Now, say that you want to reroute traffic because there's a failure. To do this, you update the associated routing control
states to change the primary routing control state to `OFF` and the secondary routing control state to
`ON`. When you do this, the associated health checks stop traffic from going to the primary replica and route
it instead to the secondary replica. For more information about failing over traffic with routing controls, see
[Getting and updating routing control states using the ARC API (recommended)](routing-control.update.md "routing-control.update.md").

To see examples of the AWS CLI commands for creating routing controls and the associated health checks using ARC
API operations, see [Examples of using ARC routing control API operations with the AWS CLI](getting-started-cli-routing.md "getting-started-cli-routing.md").
