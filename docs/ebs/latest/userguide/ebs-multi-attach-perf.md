# Performance for Multi-Attach Amazon EBS volumes

Each attached instance is able to drive its maximum IOPS performance up to the volume's
maximum provisioned performance. However, the aggregate performance of all of the
attached instances can't exceed the volume's maximum provisioned performance. If the
attached instances' demand for IOPS is higher than the volume's Provisioned IOPS, the
volume will not exceed its provisioned performance.

For example, say you create an `io2` Multi-Attach enabled volume with
`80,000` provisioned IOPS and you attach it to an `m7g.large`
instance that supports up to `40,000` IOPS, and an `r7g.12xlarge`
instance that supports up to `60,000` IOPS. Each instance can drive its
maximum IOPS as it is less than the volume's Provisioned IOPS of `80,000`.
However, if both instances drive I/O to the volume simultaneously, their combined
IOPS can't exceed the volume's provisioned performance of `80,000` IOPS.

To achieve consistent performance, it is best practice to balance I/O driven from
attached instances across the sectors of a Multi-Attach enabled volume.

For more information about IOPS performance for the Amazon EC2 instance types, see
[Amazon EBS optimized instance types](../../../AWSEC2/latest/UserGuide/ebs-optimized.md "../../../AWSEC2/latest/UserGuide/ebs-optimized.md") in the _Amazon EC2 User Guide_.
