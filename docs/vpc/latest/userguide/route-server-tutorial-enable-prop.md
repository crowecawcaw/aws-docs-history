# Step 5: Enable route server propagation

Complete this step to enable route server propagation.

When enabled, route server propagation installs the routes in the FIB on the route table you've specified. Route server supports IPv4 and IPv6 route propagation.

Route server propagation is the mechanism that automates route table updates -
instead of manually updating route tables, the route server automatically propagates
the appropriate routes to the configured route tables with routes from the
FIB.

Key aspects of route server propagation:

- Configuration
  - Links a route server to specific route tables
  - Determines which route tables will receive dynamic route updates
  - Can be enabled or disabled per route table

- Functionality
  - Automatically updates route tables with routes learned from BGP peers
  - Propagates the best available routes based on BGP attributes
  - Maintains route consistency across specified route tables
  - Updates routes dynamically when network conditions change

- States
  - Can be enabled (routes are being propagated)
  - Can be disabled (routes are not being propagated)

AWS Management Console

###### To enable route server propagation

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Select the route server for which you want to enable propagation.
3. Choose the **Propagations** tab in the route server details panel.
4. Choose **Enable propagation**.
5. In the **Enable propagation** dialog:
   - The **Route server ID** will be pre-populated.
   - Under **Route table**, select the destination route table from the dropdown menu for newly propagated routes.

6. Choose **Enable propagation** to confirm.
7. Wait for the propagation status to change to Available in the **Propagations** list.
8. Verify that the selected route table appears in the **Propagations** list
   with a state of _Available_.

Command line
Use the following procedure to enable route server propagation.

1. Command:

```
aws ec2 enable-route-server-propagation --route-table-id rtb-1 --route-server-id rs-1
```

Response:

```
{
    "RouteServerRoutePropagation": {
        "RouteServerId": "rs-1",
        "RouteTableId": "rtb-1",
        "State": "pending"
    }
}

```

2. Wait for the propagation state to change to available.

Command:

```
aws ec2 get-route-server-propagations --route-server-id rs-1
```

Response:

```
{
    "RouteServerRoutePropagation": {
        "RouteServerId": "rs-1",
        "RouteTableId": "rtb-1",
        "State": "available"
    }
}

```
