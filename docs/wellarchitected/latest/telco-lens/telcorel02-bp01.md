# TELCOREL02-BP01 Deploy user plane functions in a distributed

architecture and highly available configuration

Follow a distributed architecture approach to deploy user plane nodes across multiple
geographical locations with built-in redundancy. Such a design maintains service continuity
through redundant instances and geographical distribution, minimizing the impact of localized
failures or outages while optimizing network performance through efficient load distribution.

**Desired outcome:**

- Achieve high availability on critical network functions.
- Minimized impact from localized failures.
- Optimized network performance.
- Reduced exposure to regional outages.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement a distributed and redundant architecture for the user plane functions that can
withstand regional service degradations or outages. This involves deploying redundant
instances of user plane network functions across multiple geographical locations. Within each
site, utilize strategies such as active-active or active-standby configurations, automated
health monitoring, and failover strategy. Comprehensive monitoring and data visualization
tools provide visibility into the network's performance and availability, enabling
rapid identification and response to potential issues. Geographical distribution of these
functions, based on user demands and regulatory requirements enhance the resilience and
responsiveness of the telecom infrastructure by reducing exposure in case of failure.
Automating failover mechanisms, with thresholds and triggers defined by the network management
systems, verifies that the network can quickly recover from failures without disrupting
service to end users.

### Implementation steps

- Deploy redundant instances across multiple Availability Zones:
  - Deploy your 5G network architecture across multiple AWS Regions, Availability
    Zones, and Outposts where possible.
  - Use AWS Auto Scaling and Amazon CloudWatch to monitor and scale your network function
    instances based on real-time and projected traffic patterns.

- Implement redundancy patterns:
  - Deploy your user plane functions as Auto Scaling groups with Amazon EC2 instances in
    an active-active or active-standby configuration.
  - Use Amazon CloudWatch for automated instance health monitoring and failover.

- Establish monitoring:
  - Deploy Amazon CloudWatch to capture and analyze performance and availability metrics
    across your distributed instances.

- Implement geographical distribution:
  - Choose AWS Regions and Availability Zones based on user distribution,
    regulatory requirements, and disaster recovery needs.
  - Evaluate AWS network connectivity options, such as AWS Direct Connect and Site-to-Site VPN,
    to optimize inter-region communication.

- Configure automatic failover:
  - Use Amazon CloudWatch alarms and metrics to define infrastructure and application-level
    thresholds for initiating automated failover.
  - Integrate with your 5G network management systems to correlate failures and
    trigger appropriate responses.

## Resources

**Key AWS services:**

- [Amazon EKS](https://aws.amazon.com/pm/eks/ "https://aws.amazon.com/pm/eks/")
- [Amazon ECS](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS Local
  Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/")
