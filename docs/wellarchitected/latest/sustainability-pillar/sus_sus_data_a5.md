# SUS04-BP04 Use elasticity and automation to expand block storage or file system

Use elasticity and automation to expand block storage or file system as data grows to minimize the total provisioned storage.

**Common anti-patterns:**

- You procure large block storage or file system for future need.
- You overprovision the input and output operations per second (IOPS) of your file system.
- You do not monitor the utilization of your data volumes.

**Benefits of establishing this best practice:** Minimizing over-provisioning for storage system reduces the idle resources and improves the overall efficiency of your workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Create block storage and file systems with size allocation, throughput, and latency that are appropriate for your workload. Use elasticity and automation to expand block storage or file system as data grows without having to over-provision these storage services.

### Implementation steps

- For fixed size storage like [Amazon EBS](https://aws.amazon.com/ebs/ "https://aws.amazon.com/ebs/"), verify that you are monitoring the amount of storage used versus the overall storage size and create automation, if possible, to increase the storage size when reaching a threshold.
- Use elastic volumes and managed block data services to automate allocation of additional storage as your persistent data grows. As an example, you can use [Amazon EBS Elastic Volumes](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md") to change volume size, volume type, or adjust the performance of your Amazon EBS volumes.
- Choose the right storage class, performance mode, and throughput mode for your file system to address your business need, not exceeding that.
  - [Amazon EFS performance](../../../efs/latest/ug/performance.md "../../../efs/latest/ug/performance.md")
  - [Amazon EBS volume performance on Linux instances](../../../AWSEC2/latest/UserGuide/EBSPerformance.md "../../../AWSEC2/latest/UserGuide/EBSPerformance.md")

- Set target levels of utilization for your data volumes, and resize volumes outside of expected ranges.
- Right size read-only volumes to fit the data.
- Migrate data to object stores to avoid provisioning the excess capacity from fixed volume sizes on block storage.
- Regularly review elastic volumes and file systems to terminate idle volumes and shrink over-provisioned resources to fit the current data size.

## Resources

**Related documents:**

- [Extend the file system after resizing an EBS volume](../../../ebs/latest/userguide/recognize-expanded-volume-linux.md "../../../ebs/latest/userguide/recognize-expanded-volume-linux.md")
- [Modify a volume using Amazon EBS Elastic Volumes](../../../ebs/latest/userguide/ebs-modify-volume.md "../../../ebs/latest/userguide/ebs-modify-volume.md")
- [Amazon FSx Documentation](../../../fsx/index.md "../../../fsx/index.md")
- [What
  is Amazon Elastic File System?](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md")

**Related videos:**

- [Deep Dive on Amazon EBS Elastic Volumes](https://www.youtube.com/watch?v=Vi_1Or7QuOg "https://www.youtube.com/watch?v=Vi_1Or7QuOg")
- [Amazon EBS and Snapshot Optimization Strategies for Better Performance and Cost Savings](https://www.youtube.com/watch?v=h1hzRCsJefs "https://www.youtube.com/watch?v=h1hzRCsJefs")
- [Optimizing Amazon EFS for cost and performance, using best practices](https://www.youtube.com/watch?v=9kfeh6_uZY8 "https://www.youtube.com/watch?v=9kfeh6_uZY8")
