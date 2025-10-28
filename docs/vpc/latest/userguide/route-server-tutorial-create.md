# Step 2: Create a route server

Complete the steps in this section to create a route server.

The route server component updates your VPC and internet gateway route tables with the IPv4 or IPv6 routes in your Forwarding Information Base (FIB). The route server represents a single FIB and Routing Information Base (RIB).

AWS Management Console

###### To create a route server

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Virtual private cloud**, choose **Route
   servers**.
3. On the **Route servers** page, choose **Create route
   server**.
4. On the **Create route server** page, configure the following settings:
   - For **Name**, enter a name for your route server (e.g.,
     "my-route-server-01"). The name must be 255
     characters or less in length.
   - For **Amazon Side
     ASN**, enter a BGP ASN value. This value must be in
     the range of 1-4294967295. We recommend using a
     private ASN in the 64512–65534 (16-bit ASN) or
     4200000000–4294967294 (32-bit ASN) range.
   - For **Persist
     routes**, choose either **Enable** or **Disable**. This option determines whether routes should
     be maintained after all BGP sessions are
     terminated:
     - If enabled: Routes will be preserved in the
       route server's routing database even if all BGP
       sessions end
     - If disabled: Routes will be removed from the
       routing database when all BGP sessions end

   - If you enabled persist routes, for **Persist
     duration**, enter a value between 1-5
     minutes. This duration specifies how long the route
     server will wait after BGP is re-established to
     unpersist the routes. For example, if you set it to 1
     minute, your device has 1 minute after re-establishing
     BGP to relearn and advertise its routes before the route
     server resumes normal functionality. While 1 minute is
     typically sufficient, you can set up to 5 minutes if
     your BGP network needs more time to fully re-establish
     and re-learn all routes.
   - (Optional) To enable SNS notifications for BGP status
     changes, toggle the **Enable SNS
     notifications** switch. Enabling SNS
     notifications persists BGP or BFD session status changes
     on route server peers and maintenance notifications for
     route server endpoints to an SNS topic provisioned by
     AWS. For details about these notifications, see the
     **SNS notification
     details** table below.

5. (Optional) To add tags to your route server,
   scroll down to the **Tags -
   optional** section and choose **Add new
   tag**. Enter a key and an optional value for each tag.
   You can add up to 50 tags.
6. Review your settings and choose **Create route server**.
7. Wait for the route server to be created. Once complete, you will be redirected to the **Route
   servers** page, where you can see your new route server listed
   with a status of _Available_.

Command line
Use the following procedure to create a new route server to manage dynamic routing in a VPC.

For `--amazon-side-asn`, enter a BGP ASN value. This value must be in the range of 1-4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.

1. Command:

```
aws ec2 create-route-server --amazon-side-asn 65000
```

Response:

```
{
    "RouteServer": {
        "RouteServerId": "rs-1",
        "AmazonSideAsn": 65000,
        "State": "pending"
    }
}
```

2. Wait for the route server to be available.

Command:

```
aws ec2 describe-route-servers

```

Response:

```
{
    "RouteServer": {
        "RouteServerId": "rs-1",
        "AmazonSideAsn": 65000,
        "State": "available"
    }
}
```

**SNS notification details**

The following table shows details about the messages that Amazon VPC Route Server
will send using Amazon SNS:

| Standard fields                                                                                          |                                     | Message attributes (Metadata) |                                     |                           |                                |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------- | ----------------------------- | ----------------------------------- | ------------------------- | ------------------------------ |
| **Message**                                                                                              | **When it is sent**                 | **timestamp**                 | **eventCode**                       | **routeServerEndpointId** | **affectedRouteServerPeerIds** |
| Route Server Endpoint [ENDPOINT ID] is now undergoing maintenance. BFD and BGP sessions may be impacted. | Route server endpoint maintenance   | Format: 2025-02-17T15:55:00Z  | ROUTE_SERVER_ENDPOINT_MAINTENANCE   | Affected endpoint ID      | List of affected peer IDs      |
| **Message**                                                                                              | **When it is sent**                 | **timestamp**                 | **eventCode**                       | **routeServerPeerId**     | **newBgpStatus**               |
| BGP for Route Server Peer [PEER ID] is now [UP/DOWN].                                                    | Route server peer BGP status change | Format: 2025-02-17T15:55:00Z  | ROUTE_SERVER_PEER_BGP_STATUS_CHANGE | Affected peer ID          | UP or DOWN                     |
| **Message**                                                                                              | **When it is sent**                 | **timestamp**                 | **eventCode**                       | **routeServerPeerId**     | **newBfdStatus**               |
| BFD for Route Server Peer [PEER ID] is now [UP/DOWN].                                                    | Route server peer BFD status change | Format: 2025-02-17T15:55:00Z  | ROUTE_SERVER_PEER_BFD_STATUS_CHANGE | Affected peer ID          | UP or DOWN                     |
