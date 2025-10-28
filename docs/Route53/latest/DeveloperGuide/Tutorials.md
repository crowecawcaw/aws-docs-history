# Tutorials

This section covers the following tutorials:

**Using Route 53 as the DNS service for subdomains**
Learn how to use Route 53 as the DNS service for a new or existing subdomain while still using another DNS service for the parent domain.

**Transitioning to Latency-based routing**
Discover how to gradually migrate from standard routing to latency-based routing in Route 53, directing users to the lowest-latency AWS endpoint available.

Combine weighted and latency records for a smooth, low-risk transition with full control and rollback capability.

**Adding another Region to latency-based routing**
Expand your latency-based routing setup by adding a new AWS Region and gradually shifting traffic to the new Region.

**Routing traffic to multiple Amazon EC2 instances in a Region**
Use a combination of latency and weighted records to route traffic to multiple Amazon EC2 instances within a specific AWS Region.

**Managing over 100 weighted records**
Learn how to direct traffic to more than 100 endpoints by creating a tree of weighted alias records and weighted records.

**Weighting fault-tolerant multi-record answers**
Understand how to weight DNS responses that contain multiple records, providing fault tolerance and load balancing across multiple endpoints.

These tutorials cover various use cases and scenarios, helping you effectively leverage Route 53's routing policies, weighted records, and latency-based routing to optimize your DNS management and traffic routing.

###### Topics

- [Using Amazon Route 53 as the DNS service for subdomains
  without migrating the parent domain](creating-migrating.md "creating-migrating.md")
- [Transitioning to latency-based routing in Amazon Route 53](TutorialTransitionToLBR.md "TutorialTransitionToLBR.md")
- [Adding another Region to your latency-based routing in Amazon Route 53](TutorialAddingLBRRegion.md "TutorialAddingLBRRegion.md")
- [Using latency and weighted records in Amazon Route 53
  to route traffic to multiple Amazon EC2 instances in a Region](TutorialLBRMultipleEC2InRegion.md "TutorialLBRMultipleEC2InRegion.md")
- [Managing over 100 weighted records in Amazon Route 53](TutorialManagingOver100WRR.md "TutorialManagingOver100WRR.md")
- [Weighting fault-tolerant multi-record answers in Amazon Route 53](TutorialWeightedFTMR.md "TutorialWeightedFTMR.md")
