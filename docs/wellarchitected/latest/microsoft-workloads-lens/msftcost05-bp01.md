# MSFTCOST05-BP01 Migrate Amazon EBS volumes from gp2 to

gp3

General Purpose SSD (gp3) volumes are the latest generation of
General Purpose SSD volumes, and the lowest cost SSD volume offered
by Amazon EBS. This volume type helps to provide the right balance
of price and performance for most applications. It also helps you to
scale volume performance independently of volume size. This means
that you can provision the required performance with no need to
provision additional block storage capacity. Additionally, gp3
volumes offer a 20 percent lower price per GiB than General Purpose
SSD (gp2) volumes.

**Desired outcome:** By migrating
Amazon EBS volumes from gp2 to gp3, we aim to achieve a 20%
reduction in storage costs while gaining the ability to
independently scale volume performance without increasing capacity.
This transition will optimize our storage expenses and provide
better performance control for our workloads, ultimately resulting
in improved cost efficiency without compromising performance
requirements.

**Common anti-patterns:**

- Some organizations maintain large gp2 volumes to achieve higher
  IOPS, unnecessarily increasing costs. They fail to recognize
  that gp3 volumes allow separate scaling of IOPS and throughput,
  potentially leading to significant overspending on storage.
- Some teams might hastily migrate all gp2 volumes to gp3 without
  analyzing workload-specific performance needs. This can result
  in performance degradation for applications that require higher
  baseline performance than what's provided by the default gp3
  configuration, leading to potential application issues and the
  need for retroactive adjustments.

**Benefits of establishing this best
practice:**

- Immediate 20% reduction in per-GiB storage costs compared to gp2
  volumes, leading to significant cost savings across the storage
  infrastructure, especially for large-scale deployments with
  multiple volumes.
- Independent scaling of IOPS and throughput without increasing
  volume size, allowing precise performance tuning based on
  application needs while avoiding unnecessary storage capacity
  expenses.
- The ability to maintain smaller volume sizes while still
  achieving desired performance levels eliminates the need to
  overprovision storage for performance reasons, resulting in more
  efficient resource utilization and easier capacity management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by identifying all existing gp2 volumes using AWS Cost Explorer or AWS Systems Manager. Create a phased migration plan,
prioritizing non-production environments first to validate the
performance impact. Use AWS CloudFormation templates or AWS CLI
scripts to automate the modification process, ensuring each
volume's baseline performance requirements are properly configured
during the transition to gp3. Monitor performance metrics through
Amazon CloudWatch before and after migration to verify that
application performance remains optimal. Include snapshot backups
in your migration strategy as a rollback mechanism, and schedule
migrations during low-traffic periods to minimize potential impact
on business operations.

### Implementation steps

1. Conduct an inventory analysis using AWS Cost Explorer and
   Systems Manager to identify all gp2 volumes, documenting
   their current size, IOPS requirements, and associated
   workloads.
2. Create automated scripts using AWS CLI or Infrastructure as
   Code (IaC) to modify volumes from gp2 to gp3, including
   proper configuration of baseline IOPS and throughput based
   on historical performance data.
3. Implement the migration in phases, starting with development
   and test environments, followed by non-critical production
   workloads, and finally business-critical applications, with
   performance validation at each stage.
4. Monitor post-migration performance using Amazon CloudWatch
   metrics and establish a feedback loop to adjust gp3 volume
   configurations as needed, ensuring optimal performance while
   maintaining cost savings.

## Resources

**Related documents:**

- [Amazon EBS General Purpose SSD volumes](../../../ebs/latest/userguide/general-purpose.md "../../../ebs/latest/userguide/general-purpose.md")
- [Migrate
  Amazon EBS volumes from gp2 to gp3](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.md")
