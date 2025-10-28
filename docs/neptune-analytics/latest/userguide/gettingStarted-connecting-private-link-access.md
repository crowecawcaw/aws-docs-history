# Accessing Neptune Analytics interface endpoints

When you create an interface endpoint for Neptune Analytics, AWS PrivateLink generates two types of endpoint-specific,
Neptune Analytics DNS names: Regional and zonal.

- A Regional DNS name includes a unique Amazon VPC endpoint ID, a service identifier, the AWS Region,
  and `vpce.amazonaws.com` in its name. For example, for Amazon VPC endpoint ID
  `vpce-1a2b3c4d`, the DNS name generated might be similar to
  `vpce-1a2b3c4d-5e6f.neptune-graph.us-east-1.vpce.amazonaws.com`.
- A Zonal DNS name includes the Availability Zone - for example,
  `vpce-1a2b3c4d-5e6f-us-east-1a.neptune-graph.us-east-1.vpce.amazonaws.com`. You might
  use this option if your architecture isolates availability zones. For example, you could use it
  for fault containment or to reduce regional data transfer costs.
