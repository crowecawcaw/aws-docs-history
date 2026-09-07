

# Workload architecture
<a name="workload-architecture"></a>


| HCL\_REL2. How do you ensure acceptable network availability for your healthcare workloads? | 
| --- | 
|   | 

 **Architect redundant and reliable network connections to ensure care continuity** 

 Many healthcare applications, such as those in a hospital, require secure connectivity between the cloud and on-premises resources and users. When evaluating your network setup, consider your business continuity and disaster recovery requirements. Certain healthcare applications will be more accepting of shifts in latency or availability compared to others. For example, medical imaging or EHR systems may require more consistent latency and connectivity compared to other systems in a hospital. 

 Following the [Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-your-network-topology.html), redundant, encrypted connections are critical to verify service continuity and, more importantly, consistent patient care. Many best practices can be found in the [AWS Well-Architected Framework Hybrid Networking Lens](https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hybrid-networking-lens.html?did=wp_card&trk=wp_card). 

 AWS Direct Connect is key to establishing consistent, redundant connections with your on-premises data sources. Direct Connect establishes a dedicated network connection to AWS. It is possible to create multiple connections to AWS from a single location. 

 There are [two common approaches](https://docs.aws.amazon.com/directconnect/latest/UserGuide/disaster-recovery-resiliency.html) to establishing redundancy across your network connection to AWS: 
+  Redundant Direct Connect connections: Use the [AWS Direct Connect resiliency toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) to enable resilient applications and achieve an SLA of 99.99%. 
+  [Failover to public internet connection with VPN routing.](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html) Customers can either connect to Amazon VPCs using VPNs or through AWS Transit Gateway. 

 In both cases, check that encryption is enabled for all connections into AWS as well as within AWS. Encryption can be enabled at multiple layers, such as at the network or application layers. 