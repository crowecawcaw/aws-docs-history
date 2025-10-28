#

Connecting to a private endpoint from a different VPC (including cross-account)

In some cases, you may be required to connect to your graph from a different VPC without enabling public
connectivity. For example, applications that segregate AWS services using different VPCs or different accounts.
In this case, connectivity can be achieved through the use of private graph endpoints and Amazon Route 53 private
hosted zones. The steps in the following procedure refer to a client in VPC B, wanting to access a Neptune Analytics graph
in VPC A.

1. ###### Establish network connectivity between VPC A and VPC B

You can use any method that allows traffic to move between VPCs. For example,
[VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") or
[AWS Transit Gateway](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md").
In addition to establishing the network connection, make sure your security groups and network ACLs allow
traffic between the two VPCs. You can verify network connectivity with the
[reachability analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md"). 2. ###### Create a private graph endpoint in VPC A

If you haven’t already, create a private graph endpoint in VPC A. This can be done through the console
or the [CreatePrivateGraphEndpoint](../apiref/API_CreatePrivateGraphEndpoint.md "../apiref/API_CreatePrivateGraphEndpoint.md") API. Once created, collect the DNS name for the VPC endpoint that was deployed.

    1. Find the VPC endpoint ID from the value of **vpcEndpointId** when
     calling the [ListPrivateGraphEndpoints](../apiref/API_ListPrivateGraphEndpoints.md "../apiref/API_ListPrivateGraphEndpoints.md")  API.
    2. From the console or using the
     [DescribeVpcEndpoints](../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md") API,
     collect the DNS name of the VPC endpoint. This should have the format of
     `vpce-<alphanumeric>.vpce-svc-<alphanumeric>.<region>.vpce.amazonaws.com`.

3. Use Amazon Route 53 to create a [private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md") for
   VPC B.
   1. From the Route 53 console, choose **Create hosted zone**.
   2. Set the **domain name** of the private hosted zone to the graph endpoint of the Neptune Analytics graph. The
      graph endpoint should have the format of
      `g-<alphanumeric>.<region>.neptune-graph.amazonaws.com`.
   3. Set the **Type** to **Private hosted zone**.
   4. Associate VPC B with the hosted zone.
   5. Choose **Create hosted zone**.

Add a record to route traffic destined for the graph endpoint to the VPC endpoint directly.

    1. When the hosted zone is created, choose **Create record**.
    2. From the creation wizard, choose **Simple routing** for the routing policy.
    3. Choose **Define simple record**. Set the **Record type**
     to **A**, which routes traffic to an IPv4 address and some AWS resources.
     Set **Value/Route** traffic to to the DNS hostname of the VPC endpoint from
     Step 2. This should have the format of
     `vpce-<alphanumeric>.vpce-svc-<alphanumeric>.<region>.vpce.amazonaws.com`.

To use private hosted zones, `enableDnsHostnames` and `enableDnsSupport` should be
set to `true` for both VPCs. Depending on your networking configuration, other considerations
may apply when using private hosted zones. See
[Route 53 private hosted zone considerations](../../../Route53/latest/DeveloperGuide/hosted-zone-private-considerations.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-considerations.md") documentation
to validate your setup. 4. ###### Establish cross-account IAM permissions (only required for cross-account access)

In addition to the network connectivity established in prior steps, if the client in VPC B is in a
different account (Account B), they will also need appropriate credentials to access the Neptune Analytics graph in
VPC A (in Account A). You can use
[cross-account IAM roles](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md#access_policies-cross-account-using-roles "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md#access_policies-cross-account-using-roles") to give permissions to the client.

    1. Create the IAM role and policy that the client in Account B will be using (IAM role B).
    2. Create an IAM role and policy in Account A that grants the desired permissions to the Neptune Analytics graph
     (IAM role A). Make sure that there are also permissions for IAM role B to assume this role.
    3. Add permissions to IAM role B to assume the IAM role A.
    4. When making a cross-account call to the Neptune Analytics graph, use the AWS Security Token Service AssumeRole API to have IAM
     role B assume IAM role A. Use the returned credentials when making requests to the Neptune Analytics graph,
     e.g. via AWS SDK, awscurl, etc.
