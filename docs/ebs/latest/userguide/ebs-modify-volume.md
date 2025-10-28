# Modify an Amazon EBS volume using Elastic Volumes operations

With Amazon EBS Elastic Volumes, you can increase the volume size, change the volume type, or
adjust the performance of your EBS volumes. If your instance supports Elastic Volumes, you can
do so without detaching the volume or restarting the instance. This enables you to continue
using your application while the changes take effect.

There is no charge to modify the configuration of a volume. You are charged for the new
volume configuration after volume modification starts. For more information, see the [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/") page.

###### Contents

- [Considerations](#elastic-volumes-considerations "#elastic-volumes-considerations")
- [Limitations](#elastic-volumes-limitations "#elastic-volumes-limitations")
- [Requirements for Amazon EBS volume modifications](modify-volume-requirements.md "modify-volume-requirements.md")
- [Request Amazon EBS volume modifications](requesting-ebs-volume-modifications.md "requesting-ebs-volume-modifications.md")
- [Monitor the progress of Amazon EBS volume modifications](monitoring-volume-modifications.md "monitoring-volume-modifications.md")
- [Extend the file system after resizing an Amazon EBS volume](recognize-expanded-volume-linux.md "recognize-expanded-volume-linux.md")

## Considerations

- After modifying a volume, you must wait at least **six hours**
  and ensure that the volume is in the `in-use` or `available` state before
  you can modify the same volume.
- Modifying an EBS volume can take from a few minutes to a few hours, depending on the
  configuration changes being applied. An EBS volume that is 1 TiB in size can typically take
  up to six hours to be modified. However, the same volume could take 24 hours or longer in
  other situations. The time it takes for volumes to be modified doesn't always scale linearly.
  Therefore, a larger volume might take less time, and a smaller volume might take more time.
- Modification time is increased for volumes that are not fully initialized. For more
  information see [Manually initialize the volumes after creation](initalize-volume.md#ebs-initialize "initalize-volume.md#ebs-initialize").
- If you change the volume type from `gp2` to `gp3`, and you do not specify
  IOPS or throughput performance, Amazon EBS automatically provisions either equivalent performance to that
  of the source `gp2` volume, or the baseline `gp3` performance, whichever is
  higher.

For example, if you modify a 500 GiB `gp2` volume with 250 MiB/s throughput and 1500
IOPS to `gp3` without specifying IOPS or throughput performance, Amazon EBS automatically
provisions the `gp3` volume with 3000 IOPS (baseline `gp3` IOPS) and 250 MiB/s
(to match the source `gp2` volume throughput).

- If you encounter an error message while attempting to modify an EBS volume, or if
  you are modifying an EBS volume attached to a previous-generation instance type, take
  one of the following steps:
  - For a non-root volume, detach the volume from the instance, apply the
    modifications, and then re-attach the volume.
  - For a root volume, stop the instance, apply the modifications, and then restart
    the instance.

## Limitations

- You can't cancel a volume modification request after it has been submitted.
- You must increase the volume size. You can't decrease the volume size. However,
  you can create a smaller volume and then migrate your data to it using an
  application-level tool such as **rsync** (Linux instances) or
  **robocopy** (Windows instances).
- There are limits to the maximum aggregated storage that can be requested across
  volume modifications. For more information, see [Amazon EBS service quotas](../../../general/latest/gr/ebs-service.md#limits_ebs "../../../general/latest/gr/ebs-service.md#limits_ebs") in the
  _Amazon Web Services General Reference_.
- The new volume size can't exceed the supported capacity of its file system and
  partitioning scheme. For more information, see [Amazon EBS volume constraints](volume_constraints.md "volume_constraints.md").
- If you are not changing the volume type, then volume size and performance modifications must
  be within the limits of the current volume type. If you are changing the volume type, then volume
  size and performance modifications must be within the limits of the target volume type. For more
  information, see [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md")
- [Nitro-based instances](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") support volumes provisioned with up to 256,000 IOPS. Other
  instance types can be attached to volumes provisioned with up to 64,000 IOPS, but can
  achieve up to 32,000 IOPS.
- You can't modify the volume type for Multi-Attach enabled `io2` volumes.
- You can't modify the volume type, size, or Provisioned IOPS of Multi-Attach enabled
  `io1` volumes.
- A root volume of type `io1`, `io2`, `gp2`, `gp3`, or `standard` can't be modified to
  an `st1` or `sc1` volume, even if it is detached from the instance.
- If the volume was attached before November 3, 2016 23:40 UTC, you must initialize
  Elastic Volumes support. For more information, see [Initializing Elastic Volumes
  Support](requesting-ebs-volume-modifications.md#initialize-modification-support "requesting-ebs-volume-modifications.md#initialize-modification-support").
- While `m3.medium` instances fully support volume modification,
  `m3.large`, `m3.xlarge`, and `m3.2xlarge` instances might not support all volume modification features.
