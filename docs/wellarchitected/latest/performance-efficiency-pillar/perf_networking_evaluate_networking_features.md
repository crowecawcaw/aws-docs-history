

# PERF04-BP02 Evaluate available networking features
<a name="perf_networking_evaluate_networking_features"></a>

Evaluate networking features in the cloud that may increase performance. Measure the impact of these features through testing, metrics, and analysis. For example, take advantage of network-level features that are available to reduce latency, network distance, or jitter.

 **Common anti-patterns:** 
+ You stay within one Region because that is where your headquarters is physically located.
+ You use firewalls instead of security groups for filtering traffic.
+ You break TLS for traffic inspection rather than relying on security groups, endpoint policies, and other cloud-native functionality.
+ You only use subnet-based segmentation instead of security groups.

 **Benefits of establishing this best practice:** Evaluating all service features and options can increase your workload performance, reduce the cost of infrastructure, decrease the effort required to maintain your workload, and increase your overall security posture. You can use the global AWS backbone to provide the optimal networking experience for your customers. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS offers services like [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) and [Amazon CloudFront](https://aws.amazon.com/cloudfront/) that can help improve network performance, while most AWS services have product features (such as the [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/) feature) to optimize network traffic. 

 Review which network-related configuration options are available to you and how they could impact your workload. Performance optimization depends on understanding how these options interact with your architecture and the impact that they will have on both measured performance and user experience. 

### Implementation steps
<a name="implementation-steps"></a>
+  Create a list of workload components. 
  +  Consider using [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) to build, manage and monitor your organization's network when building a unified global network. 
  +  Monitor your global and core networks with [Amazon CloudWatch Logs metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-cloudwatch-metrics.html). Leverage [Amazon CloudWatch RUM](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-cloudwatch-rum-applications-client-side-performance/), which provides insights to help to identify, understand, and enhance users’ digital experience. 
  +  View aggregate network latency between AWS Regions and Availability Zones, as well as within each Availability Zone, using [AWS Network Manager](https://aws.amazon.com/transit-gateway/network-manager/) to gain insight into how your application performance relates to the performance of the underlying AWS network. 
  +  Use an existing configuration management database (CMDB) tool or a service such as [AWS Config](https://aws.amazon.com/config/) to create an inventory of your workload and how it’s configured. 
+  If this is an existing workload, identify and document the benchmark for your performance metrics, focusing on the bottlenecks and areas to improve. Performance-related networking metrics will differ per workload based on business requirements and workload characteristics. As a start, these metrics might be important to review for your workload: bandwidth, latency, packet loss, jitter, and retransmits. 
+  If this is a new workload, perform [load tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to identify performance bottlenecks. 
+  For the performance bottlenecks you identify, review the configuration options for your solutions to identify performance improvement opportunities. Check out the following key networking options and features:     
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_evaluate_networking_features.html)

## Resources
<a name="resources"></a>

 **Related documents:** 
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+ [EC2 Enhanced Networking on Linux ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
+ [EC2 Enhanced Networking on Windows ](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
+ [EC2 Placement Groups ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+ [Enabling Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
+ [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+ [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+ [Transitioning to Latency-Based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+ [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
+ [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

 **Related videos:** 
+  [AWS re:Invent 2023 – Ready for what's next? Designing networks for growth and flexibility](https://www.youtube.com/watch?v=FkWOhTZSfdA) 
+  [AWS re:Invent 2023 – Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es) 
+  [AWS re:Invent 2023 – A developer's guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY) 
+  [AWS re:Invent 2022 – Dive deep on AWS networking infrastructure](https://www.youtube.com/watch?v=HJNR_dX8g8c) 
+ [AWS re:Invent 2019 – Connectivity to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs)
+ [AWS re:Invent 2018 – Optimizing Network Performance for Amazon EC2 Instances](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+ [AWS Global Accelerator](https://www.youtube.com/watch?v=Docl4julOQw)

 **Related examples:** 
+ [AWS Transit Gateway and Scalable Security Solutions ](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+ [AWS Networking Workshops](https://catalog.workshops.aws/networking/en-US)
+  [Observing and diagnosing your network](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US) 
+  [Finding and addressing network misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/) 