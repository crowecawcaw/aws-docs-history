# Resilience in AWS Wavelength

AWS recommends that you architect edge applications in a hub and spoke model with the
Region providing the most scalable, resilient, and cost effective options for components
that are less latency sensitive, that need to be shared across Zones, or that have states
that need to persist. Then, use Wavelength Zones for the application components that need low
latency, data residency, higher bandwidth, or increased quality of service over 5G mobile networks.

If you need to replicate your data or applications in a Wavelength Zone, AWS recommends
that you use an Availability Zone in the Region that is not the parent zone as the failover
zone. In the following example, the parent Availability Zone is Availability Zone A, so the
resources are replicated to Availability Zone B.

![AWS Wavelength failover](images/wavelength_dr.png)
To learn more about resiliency in Amazon EC2 and Amazon EC2 Auto Scaling, see the following:

- [Resilience in
  Amazon EC2](../../../AWSEC2/latest/UserGuide/disaster-recovery-resiliency.md "../../../AWSEC2/latest/UserGuide/disaster-recovery-resiliency.md") in the _Amazon EC2 User Guide_
- [Resilience in
  Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/disaster-recovery-resiliency.md "../../../autoscaling/ec2/userguide/disaster-recovery-resiliency.md") in the _Amazon EC2 Auto Scaling User
  Guide_.
  For more information about AWS Regions, Availability Zones, Local Zones, and Wavelength
  Zones, see [AWS Global
  Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
