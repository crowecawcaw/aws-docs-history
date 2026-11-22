

# ADVPERF01-BP01 Design geographical affinity architecture with external entities (DSPs and SSPs)

 Design for the least-network path between publishers, SSPs, DSPs, and data partners. Route traffic over the AWS backbone network using geographic proximity and keep same-cloud partner traffic off the public internet. 

 **Desired outcome:** 
+  Your workloads route traffic over the shortest possible path using AWS backbone infrastructure. 
+  Latency is minimized for end users and integrated partners, while data residency and compliance obligations are satisfied by design. 
+  Same-region DSP-to-SSP traffic flows over [AWS PrivateLink](https://aws.amazon.com/privatelink/) rather than the public internet. 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) collaborations run within a single Region, avoiding cross-region transfer latency. 

 **Common anti-patterns:** 
+  Routing traffic between two AWS-hosted parties (such as a DSP and SSP) over the public internet when AWS PrivateLink could keep that traffic private and local. 
+  Deploying all compute in a single Region regardless of where requests originate, when geolocation-aware routing would serve distant users faster. 
+  Using the same Route 53 routing policy for all traffic types without distinguishing between latency-sensitive bid requests and batch analytics workloads. 

 **Benefits of establishing this best practice:** 
+  Keeping traffic on the AWS backbone reduces round-trip latency, lowers data transfer costs, and shrinks network exposure surface. 
+  Geolocation-aware routing gives you a foundation to address data residency requirements proactively, reducing compliance risk as your architecture scales. 
+  Private connectivity between same-region partners removes public internet routing variability from the bid response path. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Programmatic advertising latency budgets are tight. The industry standard for a complete bid round-trip (from publisher ad request to DSP response) is typically under 100 ms. Network path selection reduces this budget without changing application code. 

 The regional deployment for a request is chosen upstream, before any packet reaches your workload. Physics bounds the outcome: no downstream tuning can make a transoceanic request fast. Placement determines the minimum latency. In-region path quality determines the variance. Optimizing path while getting placement wrong is the common mistake. In-region tuning is measurable, whereas the transoceanic hop is invisible in the metrics of any single service. 

 In a deadline-driven auction, variance matters more than the mean. The bid deadline is absolute, and late requests are equal to undelivered requests. AWS measurements show a larger improvement in jitter than in first-byte latency for the backbone compared to public-internet paths. A path with a good median but an unpredictable tail misses auctions at the tail. 

 Bid traffic carries pricing signals and audience attributes. Keeping it off the public internet removes a class of observation that competitors or intermediaries can otherwise perform on volume and timing patterns alone. This benefit applies even when the path is not measurably faster. 

 Routing traffic to the nearest deployment usually keeps data inside its jurisdiction, because viewers and their data are co-located. When the nearest deployment is outside the required jurisdiction, the residency requirement is non-negotiable. Define the candidate regions from residency, then pick among those by latency. Routing rules that satisfy residency without documenting the intent are fragile: the next engineer tuning for latency cannot tell which rules exist for compliance. 

 In multi-party collaboration, placement is set by where the joint computation runs. Data contributed from elsewhere must move before it can be matched, and that transfer is both a latency cost and a residency event. Negotiate placement with counterparties before the collaboration is live. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Route 53 geographic routing for regional workloads:** Set up Route 53 with geolocation and failover routing policies to direct incoming bid requests to the load balancers and compute resources in the Region geographically closest to the request origin. Use weighted routing within a region to distribute load across multiple availability zones. Test routing behavior by simulating requests from each geographic zone before going live. 

1.  **Establish AWS PrivateLink for same-region DSP/SSP connectivity:** For external partners (DSPs and SSPs) operating on AWS in the same Region, create AWS PrivateLink endpoint services so that bid traffic flows over a private VPC endpoint rather than the public internet. Document which partners use PrivateLink compared to public connectivity. Prioritize the highest-volume partner links for PrivateLink migration first. 

1.  **Colocate Clean Rooms collaborators with the clean room:** When setting up AWS Clean Rooms collaborations for audience matching or campaign measurement, verify that all contributing parties store their source data in the same AWS region as the clean room. Document regional placement requirements as part of the collaboration onboarding checklist to guard against cross-region transfers being introduced unnoticed. 

1.  **Validate routing with latency measurement:** After configuring geographic routing, measure round-trip latency from each major publisher or partner location to confirm that traffic is reaching the nearest regional endpoint. Use [Amazon CloudWatch Synthetics](https://aws.amazon.com/cloudwatch/) to run ongoing latency probes from multiple geographic origins. Establish baseline latency targets per region and set alarms when latency exceeds thresholds. 

1.  **Document data residency constraints alongside routing policies:** For each Route 53 routing rule, annotate the data residency requirement it satisfies. This makes it possible to audit compliance intent alongside technical configuration, so that routing changes are reviewed against residency obligations before deployment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF01-BP03 Design for low latency with appropriate compute, storage, and network considerations](advperf01-bp03.md) 
+  [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) 

 **Related documents:** 
+  [AWS Global Accelerator FAQs (latency and jitter measurements at p90)](https://aws.amazon.com/global-accelerator/faqs/) 
+  [Amazon Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) 
+  [AWS PrivateLink concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) 
+  [Navigating GDPR compliance on AWS](https://aws.amazon.com/compliance/gdpr-center/) 

 **Related examples:** 
+  [Disaster Recovery Solutions with AWS managed services, Part 3: Multi-Site Active/Passive](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/) 

 **Related services:** 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/) 