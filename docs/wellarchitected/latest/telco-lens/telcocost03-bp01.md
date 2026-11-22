

# TELCOCOST03-BP01 Use edge zones and services to implement cloud workloads made up of containers and microservices

 Edge services let telecom operators run containerized microservices closer to subscribers and to the network infrastructure. AWS Local Zones place compute, storage, and other AWS services near large population and industry centers. AWS Wavelength Zones embed AWS compute and storage within communication service providers' 5G networks. AWS Outposts extends AWS infrastructure and services to operator-owned facilities. Placing latency-sensitive or high-volume processing at the edge can reduce the volume of data carried back to an AWS Region and improve responsiveness for users. Each edge service has its own pricing, so evaluate the cost of edge placement against your traffic patterns before you commit to it. 

 **Desired outcome:** 
+  Control data transfer costs by placing processing where your traffic patterns make it cost-effective. 
+  Improve application performance and user experience by serving content and processing from the network edge. 
+  Achieve high availability and fault tolerance through distributed, microservices-based architectures. 

 **Common anti-patterns:** 
+  Monolithic application architectures with centralized data and processing. 
+  Lack of edge computing capabilities to bring services closer to users. 
+  Inefficient communication patterns between distributed components, leading to high data transfer costs. 
+  Assuming that a service or architecture pattern reduces data transfer costs without validating it against published pricing and your measured traffic. 

 **Benefits of establishing this best practice:** 
+  Potential reduction in data transfer costs, depending on traffic patterns, by processing data closer to where it is generated or consumed. 
+  Enhanced application performance and responsiveness through edge-based processing and content delivery. 
+  Improved resilience and fault tolerance through a distributed, microservices-based design. 
+  Increased agility in scaling and deploying new features and services. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data transfer cost is driven by how much data moves and which path it takes. Placing processing at the edge, in AWS Local Zones, AWS Wavelength Zones, or AWS Outposts, can shorten the path between users and the services they consume and reduce the volume of traffic that returns to the Region. Whether this lowers total cost depends on your traffic patterns, because edge capacity and data transfer to and from edge locations are priced separately. 

 Distributing microservices across multiple Availability Zones is an availability decision, not a cost-saving one. Data transfer between Availability Zones in the same Region is charged per GB in each direction, so chatty services split across Availability Zones can increase data transfer costs. Where your design allows, keep high-volume service-to-service traffic within an Availability Zone and replicate only what your availability targets require. Within a single VPC that spans multiple Availability Zones, use the VPC's existing routing between subnets. Use AWS Transit Gateway when you interconnect multiple VPCs, on-premises networks, VPN connections, or AWS Direct Connect, and include its attachment and data processing charges in your cost model. 

 Amazon ECS and Amazon EKS run the distributed microservices in the Region and on supported edge infrastructure. AWS PrivateLink provides private connectivity between services and is primarily a security and network isolation choice. Interface endpoints are billed for each hour they are provisioned and for the data they process, so include them in your cost model. AWS Global Accelerator improves availability and performance by routing user traffic over the AWS global network to the nearest healthy endpoint. It adds a fixed fee and a per-GB data transfer premium on top of standard data transfer charges, so treat it as a performance investment rather than a cost saving. 

### Implementation steps
<a name="implementation-steps"></a>
+  Design your application architecture using a microservices approach with containers. 
+  Identify latency-sensitive or high-volume workloads that benefit from edge placement, and evaluate AWS Local Zones, AWS Wavelength Zones, or AWS Outposts against your latency, data residency, and cost requirements. Estimate the cost with the AWS Pricing Calculator before you deploy. 
+  Deploy your containerized microservices with Amazon ECS or Amazon EKS in the AWS Region and on the selected edge infrastructure. 
+  Distribute services across multiple Availability Zones to meet your availability targets, and keep high-volume service-to-service traffic within an Availability Zone where your design allows, because data transfer between Availability Zones is charged. 
+  Use the VPC's existing routing for communication within a single VPC. Use AWS Transit Gateway to interconnect multiple VPCs or hybrid networks, and include its charges in your cost model. 
+  Use AWS PrivateLink where private, isolated connectivity between services is required, and account for interface endpoint hourly and data processing charges. 
+  Use AWS Global Accelerator where users need improved availability and performance, and account for its fixed fee and data transfer premium. 
+  Implement service discovery using AWS Cloud Map to enable efficient communication between microservices. 
+  Monitor traffic patterns and data transfer charges with AWS Cost Explorer, and adjust your edge and regional deployment strategy based on measured cost and performance. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) 
+  [AWS Wavelength](https://aws.amazon.com/wavelength/) 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [Amazon EKS](https://aws.amazon.com/pm/eks/) 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [AWS Cloud Map](https://aws.amazon.com/cloud-map/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 

 **Related documents:** 
+  [Amazon EC2 On-Demand pricing (data transfer)](https://aws.amazon.com/ec2/pricing/on-demand/) 
+  [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/) 
+  [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/) 
+  [AWS Global Accelerator pricing](https://aws.amazon.com/global-accelerator/pricing/) 
+  [AWS Pricing Calculator](https://calculator.aws/) 