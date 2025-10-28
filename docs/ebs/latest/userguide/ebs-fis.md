# Fault testing on Amazon EBS

AWS Fault Injection Service (AWS FIS) is a fully managed service that helps you perform fault injection
experiments on your AWS workloads. With EBS actions in AWS FIS, you can test how your
applications respond to storage faults that can result in I/O interruptions and degraded
performance on your volumes. This controlled testing environment enables you to observe
how your applications respond to disruptions so you can identify weaknesses in your
architecture and improve the overall resilience of your applications. Using the pause
I/O action and the latency injection action, you can test your monitoring and recovery
mechanisms such as Amazon CloudWatch alarms and failover workflows, and improve the resiliency of
your mission-critical applications to storage faults. For more information about AWS FIS,
see the [AWS Fault Injection Service
User Guide](../../../fis/latest/userguide/what-is.md "../../../fis/latest/userguide/what-is.md").

## Available experiments

Amazon EBS currently supports two AWS FIS fault injections:

- [Pause I/O fault injection](ebs-fis-pause-io.md "ebs-fis-pause-io.md")
- [Latency injection](ebs-fis-latency-injection.md "ebs-fis-latency-injection.md")

## Considerations

The following considerations apply:

- All Amazon EBS volume types are supported. Both root volumes and data volumes are supported.
  Instance store volumes are not supported.
- Volumes must be attached to [Nitro-based EC2 instances](../../../AWSEC2/latest/UserGuide/instance-types.md#instance-hypervisor-type "../../../AWSEC2/latest/UserGuide/instance-types.md#instance-hypervisor-type").
- Your volumes will resume their original I/O performance once the experiment completes based
  on the duration. You can also stop a running experiment before it completes. Alternatively, you
  can create a stop condition to stop the experiment if it reaches a threshold that you define in
  a CloudWatch alarm.
- You can use AWS FIS with Multi-Attach enabled volumes. All of the attached instances are
  impacted. You can't select a specific volume-instance attachment for experiments.
- FIS is currently not available in Local Zones, Outposts, or Wavelength Zones.
- You can test up to 5 volumes in the same Availability Zone simultaneously when specifying
  volume ARNs in the console.
- You can't use AWS FIS with volumes created on an Outpost, in an AWS Wavelength Zone, or in a
  Local Zone.
