# Get the maximum Amazon EBS optimized performance

An instance's EBS performance is bounded by the instance type's performance limits, or the
aggregated performance of its attached volumes, whichever is smaller. To achieve maximum
EBS performance, an instance must have attached volumes that provide a combined performance
equal to or greater than the maximum instance performance. For example, to achieve
`80,000` IOPS for `r6i.16xlarge`, the instance must have at least
`5` `gp2` volumes provisioned with `16,000` IOPS each
(`5` volumes x `16,000` IOPS = `80,000` IOPS), or it can
have `1` `gp3` volume provisioned with `80,000` IOPS. We
recommend that you choose an instance type that provides more dedicated Amazon EBS throughput
than your application needs; otherwise, the connection between Amazon EBS and Amazon EC2 can become a
performance bottleneck.

###### Important

When using configurable bandwidth weightings, the EBS bandwidth limits for your instance
might change. For instances with the `VPC-1` weighting configuration, which
increases networking bandwidth, you might experience lower than expected IOPS for EBS
volumes due to reaching the EBS bandwidth limit before the IOPS limit. This is particularly
noticeable with larger I/O sizes. Always test your specific workload to ensure it meets
your performance requirements with your selected bandwidth weighting. For more information,
see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md "configure-bandwidth-weighting.md").

You can use the `EBSIOBalance%` and `EBSByteBalance%` metrics to
help you determine whether your instances are sized correctly. You can view these metrics
in the CloudWatch console and set an alarm that is triggered based on a threshold you
specify. These metrics are expressed as a percentage. Instances with a consistently low
balance percentage are candidates to size up. Instances where the balance percentage never
drops below 100% are candidates for downsizing. For more information, see
[Monitor your instances using CloudWatch](using-cloudwatch.md "using-cloudwatch.md").

The high memory instances are designed to run large in-memory databases, including
production deployments of the SAP HANA in-memory database, in the cloud. To maximize
EBS performance, use high memory instances with an even number of `io1` or `io2` volumes
with identical provisioned performance. For example, for IOPS heavy workloads, use four
`io1` or `io2` volumes with 40,000 provisioned IOPS to get the maximum 160,000 instance IOPS.
Similarly, for throughput heavy workloads, use six `io1` or `io2` volumes with 48,000
provisioned IOPS to get the maximum 4,750 MB/s throughput. For additional recommendations,
see [Storage Configuration for SAP HANA](../../../sap/latest/sap-hana/hana-ops-storage-config.md "../../../sap/latest/sap-hana/hana-ops-storage-config.md").

###### Considerations

- G4dn, I3en, Inf1, M5a, M5ad, R5a, R5ad, T3, T3a, and Z1d instances launched
  after February 26, 2020 provide the maximum EBS optimized performance. To get
  the maximum performance from an instance launched before February
  26, 2020, stop and start it.
- C5, C5d, C5n, M5, M5d, M5n, M5dn, R5, R5d, R5n, R5dn, and P3dn instances launched
  after December 3, 2019 provide the maximum EBS optimized performance. To get the maximum
  performance from an instance launched before December 3, 2019, stop and start it.
- `u-6tb1.metal`, `u-9tb1.metal`, and `u-12tb1.metal`
  instances launched after March 12, 2020 provide the maximum EBS optimized performance.
  Instances of these types launched before March 12, 2020 might provide lower performance.
  To get the maximum performance from an instance launched before March 12, 2020, contact
  your account team to upgrade the instance at no additional cost.
