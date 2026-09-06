

# DRHCREL01-BP01 Set service quotas to accommodate for the peak usage of AWS resources on Outposts for their homed Regions
<a name="drhcrel01-bp01"></a>

 AWS Outposts and Local Zones adhere to the service quotas of their parent AWS Regions, requiring management of service quotas to accommodate peak usage. 

 **Desired outcome:** Proactively adjust service quotas to meet your capacity requirements in specific Regions, which helps you maintain data residency in those Regions. 

 **Benefits of establishing this best practice:** Proper service quota management and planning validates availability of AWS resources on Outposts and Local Zones, reducing the risk of service disruptions due to resource limitations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-30"></a>

 [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) and [AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/what-is-aws-local-zones.html) are homed to specific [AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html). Regional [service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) apply to AWS resources (for example, Amazon EC2 instances) running on Outposts or Local Zones and should be managed. The best practices to [manage service quotas and constraints](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html) apply to the Regions that the chosen Outposts or Local Zones are homed to. Apply [service quotas best practices](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html) to Outpost and Local Zones. 