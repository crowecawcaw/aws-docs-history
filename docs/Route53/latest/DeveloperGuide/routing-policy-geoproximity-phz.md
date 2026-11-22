

# Geoproximity routing in private hosted zones

For private hosted zones, Route 53 responds to DNS queries based on the AWS Region of the VPC that the query originated from, and routes traffic to the closest resource, taking bias into account.

**Note**  
If you have an outbound endpoint forwarded to an inbound endpoint, the record resolves based on where the inbound endpoint is, not the outbound endpoint.