# REL11-BP03 Automate healing on all layers

Upon detection of a failure, use automated capabilities to perform
actions to remediate. Degradations may be automatically healed
through internal service mechanisms or require resources to be
restarted or removed through remediation actions.

For self-managed applications and cross-Region healing, recovery
designs and automated healing processes can be pulled from
[existing
best practices](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/ "https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/").

The ability to restart or remove a resource is an important tool to
remediate failures. A best practice is to make services stateless
where possible. This prevents loss of data or availability on
resource restart. In the cloud, you can (and generally should)
replace the entire resource (for example, a compute instance or
serverless function) as part of the restart. The restart itself is a
simple and reliable way to recover from failure. Many different
types of failures occur in workloads. Failures can occur in
hardware, software, communications, and operations.

Restarting or retrying also applies to network requests. Apply the
same recovery approach to both a network timeout and a dependency
failure where the dependency returns an error. Both events have a
similar effect on the system, so rather than attempting to make
either event a special case, apply a similar strategy of limited
retry with exponential backoff and jitter. Ability to restart is a
recovery mechanism featured in recovery-oriented computing and high
availability cluster architectures.

**Desired outcome:** Automated actions are performed to remediate detection of a failure.

**Common anti-patterns:**

- Provisioning resources without autoscaling.
- Deploying applications in instances or containers individually.
- Deploying applications that cannot be deployed into multiple
  locations without using automatic recovery.
- Manually healing applications that automatic scaling and
  automatic recovery fail to heal.
- No automation to failover databases.
- Lack automated methods to reroute traffic to new endpoints.
- No storage replication.

**Benefits of establishing this best
practice:** Automated healing can reduce your mean time to recovery and improve
your availability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Designs for Amazon EKS or other Kubernetes services should include both
minimum and maximum replica or stateful sets and the minimum
cluster and node group sizing. These mechanisms provide a minimum
amount of continually-available processing resources while
automatically remediating any failures using the Kubernetes
control plane.

Design patterns that are accessed through a load balancer using
compute clusters should leverage Amazon EC2 Auto Scaling groups. ELB (ELB) automatically distributes incoming
application traffic across multiple targets and virtual
appliances in one or more Availability Zones (AZs).

Clustered compute-based designs that do not use load balancing
should have their size designed for loss of at least one node.
This will allow for the service to maintain itself running in
potentially reduced capacity while it's recovering a new node.
Example services are Mongo, DynamoDB Accelerator, Amazon Redshift, Amazon EMR,
Cassandra, Kafka, MSK-EC2, Couchbase, ELK, and Amazon OpenSearch Service.
Many of these services can be designed with additional auto
healing features. Some cluster technologies must generate an
alert upon the loss a node triggering an automated or manual
workflow to recreate a new node. This workflow can be automated
using AWS Systems Manager to remediate issues quickly.

Amazon EventBridge can be used to monitor and filter for events
such as CloudWatch alarms or changes in state in other AWS
services. Based on event information, it can then invoke AWS Lambda, Systems Manager Automation, or other targets to run
custom remediation logic on your workload. Amazon EC2 Auto Scaling can be configured to check for EC2 instance health. If
the instance is in any state other than running, or if the
system status is impaired, Amazon EC2 Auto Scaling considers the
instance to be unhealthy and launches a replacement instance.
For large-scale replacements (such as the loss of an entire
Availability Zone), static stability is preferred for high
availability.

### Implementation steps

- Use Amazon EC2 Auto Scaling groups to deploy tiers in a workload.
  [Amazon EC2 Auto Scaling](../../../autoscaling/plans/userguide/how-it-works.md "../../../autoscaling/plans/userguide/how-it-works.md") can perform self-healing on stateless
  applications and add or remove capacity.
- For compute instances noted previously, use
  [load
  balancing](../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md "../../../autoscaling/ec2/userguide/autoscaling-load-balancer.md") and choose the appropriate type of load
  balancer.
- Consider healing for Amazon RDS. With standby instances, configure
  for
  [auto
  failover](https://repost.aws/questions/QU4DYhqh2yQGGmjE_x0ylBYg/what-happens-after-failover-in-rds "https://repost.aws/questions/QU4DYhqh2yQGGmjE_x0ylBYg/what-happens-after-failover-in-rds") to the standby instance. For Amazon RDS Read
  Replica, automated workflow is required to make a read
  replica primary.
- Implement
  [automatic
  recovery on EC2 instances](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md") that have applications
  deployed that cannot be deployed in multiple locations, and
  can tolerate rebooting upon failures. Automatic recovery can
  be used to replace failed hardware and restart the instance
  when the application is not capable of being deployed in
  multiple locations. The instance metadata and associated IP
  addresses are kept, as well as the
  [EBS volumes](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") and mount points to
  [Amazon Elastic File System](../../../AWSEC2/latest/UserGuide/AmazonEFS.md "../../../AWSEC2/latest/UserGuide/AmazonEFS.md") or
  [File
  Systems for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md") and
  [Windows](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md").
  Using
  [AWS OpsWorks](../../../opsworks/latest/userguide/workinginstances-autohealing.md "../../../opsworks/latest/userguide/workinginstances-autohealing.md"), you can configure automatic healing of EC2
  instances at the layer level.
- Implement automated recovery using
  [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md") and
  [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") when you cannot use automatic scaling or
  automatic recovery, or when automatic recovery fails. When
  you cannot use automatic scaling, and either cannot use
  automatic recovery or automatic recovery fails, you can
  automate the healing using AWS Step Functions and AWS Lambda.
- [Amazon EventBridge](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md") can be used to monitor and filter for
  events such as
  [CloudWatch
  alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") or changes in state in other AWS services.
  Based on event information, it can then invoke AWS Lambda
  (or other targets) to run custom remediation logic on your
  workload.

## Resources

**Related best practices:**

- [Availability
  Definition](availability.md "availability.md")
- [REL11-BP01
  Monitor all components of the workload to detect
  failures](rel_withstand_component_failures_notifications_sent_system.md "rel_withstand_component_failures_notifications_sent_system.md")

**Related documents:**

- [How
  AWS Auto Scaling Works](../../../autoscaling/plans/userguide/how-it-works.md "../../../autoscaling/plans/userguide/how-it-works.md")
- [Amazon EC2 Automatic Recovery](../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md "../../../AWSEC2/latest/UserGuide/ec2-instance-recover.md")
- [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md")
- [Amazon Elastic File System (Amazon EFS)](../../../AWSEC2/latest/UserGuide/AmazonEFS.md "../../../AWSEC2/latest/UserGuide/AmazonEFS.md")
- [What
  is Amazon FSx for Lustre?](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md")
- [What
  is Amazon FSx for Windows File Server?](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md")
- [AWS OpsWorks: Using Auto Healing to Replace Failed
  Instances](../../../opsworks/latest/userguide/workinginstances-autohealing.md "../../../opsworks/latest/userguide/workinginstances-autohealing.md")
- [What
  is AWS Step Functions?](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md")
- [What
  is AWS Lambda?](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
- [What
  Is Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")
- [Using
  Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [Amazon RDS
  Failover](https://d1.awsstatic.com/rdsImages/IG1_RDS1_AvailabilityDurability_Final.pdf "https://d1.awsstatic.com/rdsImages/IG1_RDS1_AvailabilityDurability_Final.pdf")
- [SSM

* Systems Manager Automation](../../../resilience-hub/latest/userguide/integrate-ssm.md "../../../resilience-hub/latest/userguide/integrate-ssm.md")

- [Resilient
  Architecture Best Practices](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/ "https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/")

**Related videos:**

- [Automatically
  Provision and Scale OpenSearch Service](https://www.youtube.com/watch?v=GPQKetORzmE "https://www.youtube.com/watch?v=GPQKetORzmE")
- [Amazon RDS
  Failover Automatically](https://www.youtube.com/watch?v=Mu7fgHOzOn0 "https://www.youtube.com/watch?v=Mu7fgHOzOn0")

**Related examples:**

- [Amazon RDS
  Failover Workshop](https://catalog.workshops.aws/resilient-apps/en-US/rds-multi-availability-zone/failover-db-instance "https://catalog.workshops.aws/resilient-apps/en-US/rds-multi-availability-zone/failover-db-instance")

**Related tools:**

- [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [CloudWatch
  X-Ray](../../../xray/latest/devguide/security-logging-monitoring.md "../../../xray/latest/devguide/security-logging-monitoring.md")
