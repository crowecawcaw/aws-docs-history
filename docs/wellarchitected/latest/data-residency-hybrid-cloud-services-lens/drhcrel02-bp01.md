

# DRHCREL02-BP01 Provision redundant power and network to on-premises components
<a name="drhcrel02-bp01"></a>

 To ensure high availability for AWS Outposts deployments, implement redundant power sources and network connectivity while considering multi-Outpost distribution across different Availability Zones. 

 **Desired outcome:** Achieve high availability of on-premises systems, helping to provide consistent data access and processing capabilities in compliance with data residency requirements. 

 **Benefits of establishing this best practice:** Redundant power and network infrastructure improves the reliability and availability of on-premises components, minimizing potential downtime. 

 **Level of risk exposed if this best practice is not established**: High 

 [Outpost Racks](https://docs.aws.amazon.com/outposts/latest/userguide/disaster-recovery-resiliency.html) are designed with redundant power and networking equipment. Customer racks will house individual [Outposts servers](https://docs.aws.amazon.com/outposts/latest/server-userguide/what-is-outposts.html). To meet high availability objectives, we recommend providing dual power sources and redundant network connectivity to Outposts and customer racks. 

## Implementation guidance
<a name="implementation-guidance-31"></a>
+  Provide dual power sources to Outposts and Customer racks. 
+  Provision redundant network connectivity (for example, redundant network devices) to Outposts. 
+  For higher availability, deploy applications on multiple Outposts, each attached to a different Availability Zone, to build additional application resilience and avoid dependence on a single Availability Zone. 