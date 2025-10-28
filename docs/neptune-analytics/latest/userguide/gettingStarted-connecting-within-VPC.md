# Connecting to a private endpoint from within the same VPC

For graphs using private endpoints, you can connect to your graph from any resource that has access to the private
VPC, such as AWS Lambda, an Amazon SageMaker AI notebook instance, an Amazon EC2 instance, etc. The instance must be in the same
VPC and subnet as the private endpoint for your graph. Ensure that the security group attached to the VPC endpoint
of your private graph's endpoint allows ingress on port 443, and optionally port 8182.

For details on how to use notebooks and how to create one capable of connecting to the private endpoint of your
graph, see the Neptune Analytics user guide section on
[notebooks](notebooks.md "notebooks.md"),
making sure to supply the necessary VPC and subnet identifier when setting up your network options. If the VPC
CIDR is 172.17.0.0/16, notebooks will have some difficult connecting the graph endpoints.

You can also create an Amazon EC2 instance to connect to the private endpoint of your graph. You will need to select
the correct VPC and availability zone to match your graph’s private endpoint. When prompted for a security group
to associate with the instance, create or choose one that has inbound TCP rules allowing ingress traffic over
ports 22 (for SSH), and egress traffic over port 443 if custom egress rules are needed. For the detailed
prerequisites and steps to create and connect to an Amazon EC2 instance, see the
[Amazon EC2 user guide](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").

###### Note

For troubleshooting connectivity issues refer to the
[reachability analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") guide.
You can get destination VPC endpointId by using the
[GetPrivateGraphEndpoint](../apiref/API_GetPrivateGraphEndpoint.md "../apiref/API_GetPrivateGraphEndpoint.md") API.
