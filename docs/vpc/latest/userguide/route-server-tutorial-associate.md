# Step 3: Associate route server with a VPC

Complete the steps in this section to associate the route server with a VPC.

A route server association is the connection established between a route server and a VPC. This is a fundamental configuration step that enables the route server to work with appliances in your VPC.

When you create a route server association:

- It links the route server to a specific VPC.
- It enables the route server to interact with route tables within the
  VPC’s subnets.
- It allows the route server to receive and propagate routes within the
  associated VPC.
- It establishes the scope of where the route server can operate.
  Key aspects of a route server association:

- Each route server can be associated with one VPC. Each VPC can have up
  to 5 separate route server associations by default. For more information
  about quotas, see [Route server quotas](amazon-vpc-limits.md#vpc-limits-route-servers "amazon-vpc-limits.md#vpc-limits-route-servers").
- The association must be created before the route server can manage
  routes.
- The association can be monitored to track its state (such as
  associating and associated).
- The association can be removed (disassociated) if you no longer want
  the route server to operate in that VPC.

AWS Management Console

###### Associate a route server with a VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Virtual private cloud**, choose **Route servers**.
3. Select the route server you want to associate with a VPC.
4. On the **Association tab**, choose **Associate route server**.
5. In the Associate route server dialog box:
   - The **Route server ID** field is automatically populated with your selected route server
   - For **VPC ID**, choose the VPC you want to associate from the dropdown list

6. Choose **Associate route server**.
7. Wait for the association to complete. Once finished, the **State** will show
   as _Associated_ on the
   **Association** tab.

Command line
Use the following procedure to associate a route server with a VPC.

1. Command:

```
aws ec2 associate-route-server --route-server-id rs-1 --vpc-id vpc-1
```

Response:

```
{
    "RouteServerAssociation": {
        "RouteServerId": "rs-1",
        "VpcId": "vpc-1",
        "State": "associating"
    }
}
```

2. Wait for the association to complete.

Command:

```
aws ec2 get-route-server-associations --route-server-id rs-1

```

Response:

```
{
    "RouteServerAssociation": {
        "RouteServerId": "rs-1",
        "VpcId": "vpc-1",
        "State": "associated"
    }
}
```
