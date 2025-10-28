# DRHCSUS05-BP01 Consider using supported AWS-managed file services to minimize data duplication in Local Zones

Shared file services can be implemented using AWS managed file
services, AWS marketplace offerings, or even self-managed
solutions to minimize data duplication for your data-residency
workloads.

**Desired outcome:** Duplication of
data is minimized using managed or self-managed shared storage
services in Local Zones.

**Benefits of establishing this best
practice:** Data duplication and overall storage
consumption can be minimized to reduce energy utilization and
support your sustainability objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

A growing number of AWS Local Zones now support
[Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows "https://aws.amazon.com/fsx/windows") and
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre "https://aws.amazon.com/fsx/lustre"). These managed shared-file services can be
used to efficiently store and share data between large numbers
of data residency workloads, minimizing the environmental costs
of duplicating data for individual workloads or users. While
choosing a Local Zone, review the
[Local
Zone feature matrix](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/") to determine if these services are
available in location that meets your data residency
requirements.

If Amazon FSx services are not available in the Local Zone you
choose, consider using self-managed or
[AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=shared+storage "https://aws.amazon.com/marketplace/search/results?searchTerms=shared+storage") shared storage solutions for Windows SMB or
NFS shares to minimize the duplication or movement of data
within the Local Zone.
