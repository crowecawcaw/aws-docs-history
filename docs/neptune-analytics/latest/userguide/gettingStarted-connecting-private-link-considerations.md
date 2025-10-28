# Considerations when using AWS PrivateLink for Neptune Analytics

Amazon VPC considerations apply to AWS PrivateLink for Neptune Analytics. For more information, see
[Interface endpoint considerations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and
[AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the AWS PrivateLink guide. Additionally, the following restrictions apply:

1. The AWS PrivateLink for Neptune Analytics control plane i.e. `neptune-graph` service does not support
   [VPC endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md"). However, AWS PrivateLink for Neptune Analytics data plane i.e.
   `neptune-graph-data` service supports VPC endpoint policies.
2. The AWS PrivateLink for Neptune Analytics supports
   [Federal Information Processing
   Standard (FIPS)](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/") endpoints in
   US East (N. Virginia), US East (Ohio), and US West (Oregon) for control plane API operations
   under the service name `neptune-graph-fips`. FIPS endpoints are not supported in any
   AWS region for AWS PrivateLink for data plane API operations.
3. Transport Layer Security (TLS) 1.1 is **not** supported.
4. Private and Hybrid Domain Name System (DNS) services are **not** supported.
