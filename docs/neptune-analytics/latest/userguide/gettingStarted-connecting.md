# Connecting to a graph

In Neptune Analytics, you can provision your graph to be accessed publicly over the internet or have a private endpoint to access
the graph within a VPC. If your graph is not configured for public connectivity, then you must create a private
endpoint for your Neptune Analytics graph that allows access to the graph only from within the same Amazon Virtual Private Cloud
(VPC) and availability zones associated with the subnet associated with the graph’s private endpoint
(You must ensure the subnets belong to all the availability zones in the VPC). This means that applications using
Neptune Analytics must be deployed in the same VPC; or For applications which are deployed in different VPC but uses techniques
like VPC peering, AWS Site-to-Site VPN connections, or AWS Direct Connect connections might face issues with DNS
resolution to connect to private graph endpoint.

If your graph is configured for public connectivity, you can connect to your graph from multiple VPCs and from the
internet. This allows you to access a Neptune Analytics graph without also setting up additional supporting AWS services.
The simplicity of setting up public connectivity-enabled graphs makes it useful for initial exploration of the
service.

Graphs are created with public connectivity disabled by default. However, this can be configured by enabling public
connectivity at [graph creation](../apiref/API_CreateGraph.md "../apiref/API_CreateGraph.md") or by
[updating the graph configuration](../apiref/API_UpdateGraph.md "../apiref/API_UpdateGraph.md")
post-creation.

###### Note

All Neptune Analytics graphs are configured to use AWS Identity and Access Management ([IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")) for authentication and
authorization. This means that all requests to the graph should be signed using AWS Signature Version 4
[(SIGV4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md").
If you are using the AWS CLI or SDK to connect, then the signing of the requests is handled by the client
library. The library requires the user to provide the credentials to sign using one of the known methods.
You can also make HTTP requests to the APIs by using
[AWSCurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl"), which provides a curl like interface to make
HTTP requests and supports SIGV4. For Neptune Analytics specific IAM documentation please refer to the Neptune Analytics user guide
[Security IAM](security-iam.md#security_iam_authentication "security-iam.md#security_iam_authentication")
section.

###### Topics

- [AWS PrivateLink for Neptune Analytics](gettingStarted-connecting-private-link.md "gettingStarted-connecting-private-link.md")
- [Connecting to a private endpoint from within the same VPC](gettingStarted-connecting-within-VPC.md "gettingStarted-connecting-within-VPC.md")
- [Connecting to a private endpoint from a different VPC (including cross-account)](gettingStarted-connecting-different-VPC.md "gettingStarted-connecting-different-VPC.md")
- [Accessing the graph](gettingStarted-accessing.md "gettingStarted-accessing.md")
- [Best practices](gettingStarted-connecting-best-practices.md "gettingStarted-connecting-best-practices.md")
