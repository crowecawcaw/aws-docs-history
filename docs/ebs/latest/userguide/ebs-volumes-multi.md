# Attach an EBS volume to multiple EC2 instances using Multi-Attach

Amazon EBS Multi-Attach enables you to attach a single Provisioned IOPS SSD (`io1` or `io2`)
volume to multiple instances that are in the same Availability Zone. You can attach multiple
Multi-Attach enabled volumes to an instance or set of instances. Each instance to which the
volume is attached has full read and write permission to the shared volume. Multi-Attach
makes it easier for you to achieve higher application availability in applications that
manage concurrent write operations.

###### Pricing and billing

There are no additional charges for using Amazon EBS Multi-Attach. You are billed the
standard charges that apply to Provisioned IOPS SSD (`io1` and `io2`) volumes. For more
information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

###### Contents

- [Considerations and limitations](#considerations "#considerations")
- [Performance for Multi-Attach volumes](ebs-multi-attach-perf.md "ebs-multi-attach-perf.md")
- [Enable Multi-Attach](working-with-multi-attach.md "working-with-multi-attach.md")
- [Disable Multi-Attach](disable-multi-attach.md "disable-multi-attach.md")
- [NVMe reservations](nvme-reservations.md "nvme-reservations.md")

## Considerations and limitations

- Multi-Attach enabled volumes can be attached to up to 16 instances built on the
  [Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") that are in the same Availability Zone.
- **Linux instances** support Multi-Attach enabled
  `io1` and `io2` volumes. **Windows instances** support
  Multi-Attach enabled `io2` volumes only.
- The maximum number of Amazon EBS volumes that you can attach to an instance depends
  on the instance type and instance size. For more information, see
  [instance volume limits](../../../AWSEC2/latest/UserGuide/volume_limits.md "../../../AWSEC2/latest/UserGuide/volume_limits.md").
- Multi-Attach is supported exclusively on [Provisioned
  IOPS SSD (io1 and io2) volumes](provisioned-iops.md#EBSVolumeTypes_piops "provisioned-iops.md#EBSVolumeTypes_piops").
- Multi-Attach for `io1` volumes is available in the following Regions only:
  US East (N. Virginia), US West (Oregon), and Asia Pacific (Seoul).

Multi-Attach for `io2` is available in all Regions that support `io2`.

###### Note

For better performance, consistency, and durability at a lower cost, we
recommend that you use `io2` volumes.

- `io1` volumes with Multi-Attach enabled are not supported with [instances built on
  the Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") that support the Scalable Reliable Datagram (SRD) networking
  protocol only. To use Multi-Attach with these instance types, you must use `io2`.
- Standard file systems, such as XFS and EXT4, are not designed to be accessed simultaneously
  by multiple servers, such as EC2 instances. You should use a clustered file system to ensure
  data resiliency and reliability for your production workloads.
- Multi-Attach enabled `io2` volumes support I/O fencing. I/O fencing protocols control write
  access in a shared storage environment to maintain data consistency. Your applications must
  provide write ordering for the attached instances to maintain data consistency. For more
  information, see [Use NVMe reservations with Multi-Attach enabled Amazon EBS volumes](nvme-reservations.md "nvme-reservations.md").

Multi-Attach enabled `io1` volumes do not support I/O fencing.

- Multi-Attach enabled volumes can't be created as boot volumes.
- Multi-Attach enabled volumes can be attached to one block device mapping per instance.
- Multi-Attach can't be enabled during instance launch using either the Amazon EC2 console or RunInstances
  API.
- Multi-Attach enabled volumes that have an issue at the Amazon EBS infrastructure layer are
  unavailable to all attached instances. Issues at the Amazon EC2 or networking layer
  might impact only some attached instances.
- The following table shows volume modification support for Multi-Attach enabled
  `io1` and `io2` volumes after creation.

|                         | `io2` volumes | `io1` volumes |
| ----------------------- | ------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Modify volume type      | ✗             | ✗             |
| Modify volume size      | ✓             | ✗             |
| Modify provisioned IOPS | ✓             | ✗             |
| Enable Multi-Attach     | ✓ \*          | ✗             |
| Disable Multi-Attach    | ✓ \*          | ✗             | \* You can't enable or disable Multi-Attach while the volume is attached to an instance. <br>• Multi-Attach enabled volumes are deleted on instance termination if the last attached instance is terminated and if that instance is configured to delete the volume on termination. If the volume is attached to multiple instances that have different delete on termination settings in their volume block device mappings, the last attached instance's block device mapping setting determines the delete on termination behavior. To ensure predictable delete on termination behavior, enable or disable delete on termination for all of the instances to which the volume is attached. For more information, see [Preserve data when an instance is terminated](../../../AWSEC2/latest/UserGuide/preserving-volumes-on-termination.md "../../../AWSEC2/latest/UserGuide/preserving-volumes-on-termination.md"). <br>• You can monitor a Multi-Attach enabled volume using the CloudWatch Metrics for Amazon EBS volumes. Data is aggregated across all of the attached instances. You can't monitor metrics for individual attached instances. For more information, see [Amazon CloudWatch metrics for Amazon EBS](using_cloudwatch_ebs.md "using_cloudwatch_ebs.md"). |
