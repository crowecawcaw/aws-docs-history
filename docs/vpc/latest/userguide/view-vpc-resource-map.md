# Visualize the resources in your VPC

This section describes how you can see a visual representation of the resources in your VPC using
the **Resource map** tab. The following resources are visible in the
resource map:

- VPC
- Subnets
  - The Availability Zone is represented with a letter.
  - Public subnets are green.
  - Private subnets are blue.

- Route tables
- Internet gateways
- Egress-only internet gateways
- NAT gateways
- Gateway endpoints (Amazon S3 and Amazon DynamoDB)
  The resource map shows relationships between resources inside a VPC and how traffic flows
  from subnets to NAT gateways, internet gateway and gateway endpoints.

You can use the resource map to understand the architecture of a VPC, see how many
subnets it has in it, which subnets are associated with which route tables, and which
route tables have routes to NAT gateways, internet gateways, and gateway
endpoints.

You can also use the resource map to spot undesirable or incorrect configurations,
such as private subnets disconnected from NAT gateways or private subnets with a route
directly to the internet gateway. You can choose resources within the resource map, such
as route tables, and edit the configurations for those resources.

###### To visualize the resources in your VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **VPCs**.
3. Select the VPC.
4. Choose the **Resource map** tab to display a visualization of the resources.
5. Choose **Show details** to view details in addition to the
   resource IDs and zones displayed by default.
   - **VPC**: The IPv4 and IPv6 CIDR ranges assigned to
     the VPC.
   - **Subnets**: The IPv4 and IPv6 CIDR ranges assigned
     to each subnet.
   - **Route tables**: The subnet associations, and the number of routes in
     the route table.
   - **Network connections**: The details related to each
     type of connection:
     - If there are public subnets in the VPC, there is an internet gateway resource with the
       number of routes and the source and destination subnets for
       traffic using the internet gateway.
     - If there is an egress-only internet gateway, there is an egress-only internet gateway
       resource with the number of routes and the source and
       destination subnets for traffic using the egress-only internet
       gateway.
     - If there is a NAT gateway, there is a NAT gateway resource with the number of network
       interfaces and Elastic IP addresses for the NAT gateway.
     - If there is a gateway endpoint, there is a gateway endpoint resource with the name of
       the AWS service (Amazon S3 or Amazon DynamoDB) that you can connect to
       using the endpoint.

6. Hover over a resource to see the relationship between the resources. Solid
   lines represent relationships between resources. Dotted lines represent network
   traffic to network connections.
