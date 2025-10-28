# Amazon EBS volumes

An Amazon EBS volume is a durable, block-level storage device that you can attach to your
instances. After you attach a volume to an instance, you can use it as you would use a physical
hard drive. EBS volumes are flexible. For current-generation volumes attached to
current-generation instance types, you can dynamically increase size, modify the provisioned
IOPS capacity, and change volume type on live production volumes.

You can use EBS volumes as primary storage for data that requires frequent updates, such as
the system drive for an instance or storage for a database application. You can also use them
for throughput-intensive applications that perform continuous disk scans. EBS volumes persist
independently from the running life of an EC2 instance.

You can attach multiple EBS volumes to a single instance. The volume and instance must be in
the same Availability Zone. Depending on the volume and instance types, you can use
[Multi-Attach](ebs-volumes-multi.md "ebs-volumes-multi.md") to mount a volume to multiple instances at
the same time.

Amazon EBS provides the following volume types: General Purpose SSD (`gp2` and `gp3`), Provisioned IOPS SSD (`io1` and `io2`), Throughput Optimized HDD
(`st1`), Cold HDD (`sc1`), and Magnetic (`standard`). They differ in performance characteristics
and price, allowing you to tailor your storage performance and cost to the needs of your
applications. For more information, see [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md").

Your account has a limit on the total storage available to you. For more information about
these limits, and how to request an increase in your limits, see [Amazon EBS endpoints and quotas](../../../general/latest/gr/ebs-service.md#limits_ebs "../../../general/latest/gr/ebs-service.md#limits_ebs").

A _managed EBS volume_ is managed by a service provider,
such as Amazon EKS Auto Mode. You can’t directly modify the settings of a managed EBS volume. Managed
EBS volumes are identified by a **true** value in the
**Managed** field. For more information, see [Amazon EC2 managed
instances](../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md "../../../AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.md").

For more information about pricing, see [Amazon EBS
Pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

###### Contents

- [Features and benefits of Amazon EBS volumes](EBSFeatures.md "EBSFeatures.md")
- [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md")
- [Amazon EBS volume constraints](volume_constraints.md "volume_constraints.md")
- [Amazon EBS volumes and NVMe](nvme-ebs-volumes.md "nvme-ebs-volumes.md")
- [Amazon EBS volume lifecycle](ebs-volume-lifecycle.md "ebs-volume-lifecycle.md")
- [Replace an Amazon EBS volume using a snapshot](ebs-restoring-volume.md "ebs-restoring-volume.md")
- [Amazon EBS volume status checks](monitoring-volume-checks.md "monitoring-volume-checks.md")
- [Fault testing on Amazon EBS](ebs-fis.md "ebs-fis.md")
