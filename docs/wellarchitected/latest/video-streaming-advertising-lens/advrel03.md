

# Single and Multi-Region deployments

 There are multiple strategies for achieving reliability in single and Multi-Region deployments. Implement full regional deployment using auto scaling and container orchestration. Select AWS Regions based on legal and disaster recovery requirements. Configure databases with appropriate reliability and recovery strategies. Manage service capacity through proper resource reservation and load testing. Focus on building resilient architectures that balance performance, compliance, and cost considerations. 


|  ADVREL03: How do you design your advertising workload for resilient single-region and Multi-Region deployments?  | 
| --- | 
| [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) | 
| [ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements](advrel03-bp02.md) | 
| [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) | 
| [ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions](advrel03-bp04.md) | 

## Capability intent
<a name="advrel03-capability-intent"></a>
+  Compute resources are distributed across multiple Availability Zones behind zone-aware load balancers, enabling automatic recovery from Availability Zone-level failures without manual intervention. 
+  AWS Region selection accounts for both legal data residency requirements and disaster recovery needs for your advertising workloads. 
+  Databases span multiple Availability Zones with failover strategies calibrated to your component-level RTO and RPO. 
+  Service capacity reservations are sized based on load test results to handle peaks without manual intervention. 

## Common issues to watch for
<a name="advrel03-common-issues-to-watch-for"></a>
+  Deploying compute across multiple Availability Zones but not implementing zone-aware routing, resulting in unnecessary cross-AZ data transfer costs. 
+  Selecting AWS Regions based purely on geographic proximity without considering data residency regulations for advertising audience data. 
+  Using Multi-AZ database deployments for all components regardless of their actual RTO requirements, paying for failover capabilities that exceed what the business needs. 