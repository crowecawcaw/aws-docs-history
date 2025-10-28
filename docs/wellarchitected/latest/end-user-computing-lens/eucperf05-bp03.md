# EUCPERF05-BP03 Understand integrated storage capabilities (WorkSpaces)

Most existing workloads, either physical or virtual, will make use of integrated
storage that provides the system drive and data drives. For virtualized desktops and
servers, this will be virtual drives created from hyperconverged storage. Some workloads, if
not already virtualized, may also have fast boot and data drives (like SSD or NVMe) or
additional integrated storage in the form of internal hard drives or externally-connected
hard drives that deliver large or faster storage for specific applications.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

If any of the workloads you are migrating to AWS EUC services have been configured
with and require high performance or additional high-density storage, carefully review the
AWS instance types that provide higher performance storage. The Graphics G4 instance
types offer a local NVMe instance store which may meet your requirements.

This may also be an opportunity to review alternate networked AWS Storage solutions
as they might provide the speed and density you require.
