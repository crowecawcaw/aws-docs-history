# ADVPERF01-BP01 Design geographical affinity architecture with external entities (DSPs and SSPs)

Design for the least-network path, but keep regulatory needs in
consideration. Use the AWS backbone network to improve latency.

## Implementation guidance

Implement Amazon Route 53 (fail-over and geolocation routing) to
route traffic to the target load balancers and compute workloads
in the closest Region to the origination of intake requests.
This architecture may help align with specific compliance and residency needs. Consult with legal counsel for guidance tailored to your specific use case and jurisdiction.

Implement AWS PrivateLink on the same Region between
external entities (like DSPs and SSPs) where both parties are on
AWS.

For privacy-enhanced collaboration using AWS Clean Rooms, it is recommended to have collaborators in the same Region as the clean room to avoid latency with cross-Region data transfer.

## Key AWS services

- [Amazon Route 53 (R53)](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")
- [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/ "https://aws.amazon.com/clean-rooms/")

## Resources

- [Disaster
  Recovery Solutions with AWS managed services, Part 3: Multi-Site Active/Passive](https://aws.amazon.com/blogs/architecture/disaster-recovery-solutions-with-aws-managed-services-part-3-multi-site-active-passive/ "https://aws.amazon.com/blogs/architecture/disaster-recovery-solutions-with-aws-managed-services-part-3-multi-site-active-passive/")
- [How
  Storygize and Sharethrough are using AWS PrivateLink to reduce costs and increase revenue](https://aws.amazon.com/blogs/industries/how-storygize-and-sharethrough-are-using-aws-privatelink-to-reduce-costs-and-increase-revenue/ "https://aws.amazon.com/blogs/industries/how-storygize-and-sharethrough-are-using-aws-privatelink-to-reduce-costs-and-increase-revenue/")
