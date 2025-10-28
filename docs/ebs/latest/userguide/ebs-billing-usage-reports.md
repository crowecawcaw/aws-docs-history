# Understand codes for Amazon EBS in billing and usage reports

When you use Amazon EBS, we include related codes in your AWS billing and usage reports. Reviewing these
codes helps you understand your costs and usage patterns for Amazon EBS. Tracking and managing your
expenses is essential for optimizing your costs.

The following tables describe the codes for Amazon EBS that appear in your billing and usage reports.
For a list of the Region codes used in the billing and usage reports, see [AWS Region billing codes](../../../global-infrastructure/latest/regions/aws-region-billing-codes.md "../../../global-infrastructure/latest/regions/aws-region-billing-codes.md").

###### Billing codes for:

- [Snapshots](#snapshot-billing-usage-reports "#snapshot-billing-usage-reports")
- [Volume storage](#volume-billing-usage-reports "#volume-billing-usage-reports")
- [Provisioned performance](#perf-billing-usage-reports "#perf-billing-usage-reports")
- [EBS direct APIs](#direct-billing-usage-reports "#direct-billing-usage-reports")
- [Fast snapshot restore (FSR)](#fsr-billing-usage-reports "#fsr-billing-usage-reports")

###### Related resources

- [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/")
- [Pricing for EBS direct APIs](ebsapi-pricing.md "ebsapi-pricing.md")

## Snapshots

| Code                                      | Description                                                                                    | Units                     | Granularity                   |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------- | ------------------------------ |
| ``region`-EBS:SnapshotUsage`              | Standard tier snapshots (incremental copies).                                                  | GB-Month                  | Hourly                        |
| ``region`-EBS:SnapshotArchiveStorage`     | Archive tier snapshots (full copies).                                                          | GB-Month                  | Hourly                        |
| ``region`-EBS:SnapshotArchiveEarlyDelete` | Deleting archived snapshots before the minimum retention period ends.                          | GB                        | Per deletion                  |
| ``region`-EBS:SnapshotArchiveRetrieval`   | Retrieving archived snapshots.                                                                 | GB                        | Per GB                        | ## Volume storage              |
| Code                                      | Description                                                                                    | Units                     | Granularity                   |
| ---                                       | ---                                                                                            | ---                       | ---                           |
| ``region`-EBS:VolumeUsage.gp3`            | Storage for General Purpose SSD (gp3) volumes.                                                 | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage.gp2`            | Storage for General Purpose SSD (g2) volumes.                                                  | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage.io2`            | Storage for Provisioned IOPS SSD (io2) volumes.                                                | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage.piops`          | Storage for Provisioned IOPS SSD (io1) volumes.                                                | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage.st1`            | Storage for Throughput Optimized HDD volumes.                                                  | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage.sc1`            | Storage for Cold HDD volumes.                                                                  | GB-Month                  | Hourly                        |
| ``region`-EBS:VolumeUsage`                | Storage for Magnetic volumes.                                                                  | GB-Month                  | Hourly                        | ## Provisioned performance     |
| Code                                      | Description                                                                                    | Units                     | Granularity                   |
| ---                                       | ---                                                                                            | ---                       | ---                           |
| ``region`-EBS:VolumeP-Throughput.gp3`     | Provisioned throughput for gp3 volumes over 125 MB/s.                                          | MB/s-Month                | Hourly                        |
| ``region`-EBS:VolumeP-IOPS.gp3`           | Provioned IOPS for gp3 volumes over 3,000.                                                     | IOPS-Month                | Hourly                        |
| ``region`-EBS:VolumeP-IOPS.io2`           | Provisioned IOPS for io2 volumes up to 32,000.                                                 | IOPS-Month                | Hourly                        |
| ``region`-EBS:VolumeP-IOPS.io2.tier2`     | Provisioned IOPS for io2 volumes from 32,001 to 64,000.                                        | IOPS-Month                | Hourly                        |
| ``region`-EBS:VolumeP-IOPS.io2.tier3`     | Provisioned IOPS for io2 volumes greater than 64,000.                                          | IOPS-Month                | Hourly                        |
| ``region`-EBS:VolumeP-IOPS.piops`         | Provisioned IOPS for io1 volumes.                                                              | IOPS-Month                | Hourly                        |
| ``region`-EBS:VolumeIOUsage`              | Legacy IOPS.                                                                                   | IOPS-Month                | Hourly                        | ## EBS direct APIs             |
| Code                                      | Description                                                                                    | Units                     | Granularity                   |
| ---                                       | ---                                                                                            | ---                       | ---                           |
| ``region`-EBS:directAPI.snapshot.List`    | Calls to the `ListChangedBlocks` and `ListSnapshotBlocks` API actions.                         | Per 1,000 requests        | Per request                   |
| ``region`-EBS:directAPI.snapshot.Get`     | Blocks returned by the `GetSnapshotBlock` API action.                                          | Per 1,000 blocks returned | Per request                   |
| ``region`-EBS:directAPI.snapshot.Put`     | Blocks written by the `PutSnapshotBlock` API action.                                           | Per 1,000 blocks written  | Per request                   | ## Fast snapshot restore (FSR) |
| Code                                      | Description                                                                                    | Units                     | Granularity                   |
| ---                                       | ---                                                                                            | ---                       | ---                           |
| ``region`-EBS:FastSnapshotRestore`        | Data Services Unit-Hours (DSU-Hours) for snapshots enabled for fast snapshot restore (per AZ). | DSU-Hours                 | Per minute (one-hour minimum) |
