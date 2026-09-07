

# ADVPERF01-BP01 Design geographical affinity architecture with external entities (DSPs and SSPs) 
<a name="advperf01-bp01"></a>

 Design for the least-network path, but keep regulatory needs in consideration. Use the AWS backbone network to improve latency. 

## Implementation guidance
<a name="implementation-guidance-34"></a>

 Implement Amazon Route 53 (fail-over and geolocation routing) to route traffic to the target load balancers and compute workloads in the closest Region to the origination of intake requests. This architecture may help align with specific compliance and residency needs. Consult with legal counsel for guidance tailored to your specific use case and jurisdiction. 

 Implement AWS PrivateLink on the same Region between external entities (like DSPs and SSPs) where both parties are on AWS. 

 For privacy-enhanced collaboration using AWS Clean Rooms, it is recommended to have collaborators in the same Region as the clean room to avoid latency with cross-Region data transfer. 

## Key AWS services
<a name="key-aws-services-20"></a>
+  [Amazon Route 53 (R53)](https://aws.amazon.com/route53/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+ [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)

## Resources
<a name="resources-29"></a>
+  [Disaster Recovery Solutions with AWS managed services, Part 3: Multi-Site Active/Passive](https://aws.amazon.com/blogs/architecture/disaster-recovery-solutions-with-aws-managed-services-part-3-multi-site-active-passive/) 
+  [How Storygize and Sharethrough are using AWS PrivateLink to reduce costs and increase revenue](https://aws.amazon.com/blogs/industries/how-storygize-and-sharethrough-are-using-aws-privatelink-to-reduce-costs-and-increase-revenue/) 