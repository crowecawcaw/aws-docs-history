# CodeBuild CloudWatch resource utilization

metrics

###### Note

CodeBuild resource utilization metrics are only available in the following regions:

- Asia Pacific (Tokyo) Region
- Asia Pacific (Seoul) Region
- Asia Pacific (Mumbai) Region
- Asia Pacific (Singapore) Region
- Asia Pacific (Sydney) Region
- Canada (Central) Region
- Europe (Frankfurt) Region
- Europe (Ireland) Region
- Europe (London) Region
- Europe (Paris) Region
- South America (São Paulo) Region
- US East (N. Virginia) Region
- US East (Ohio) Region
- US West (N. California) Region
- US West (Oregon) Region
  The following resource utilization metrics can be tracked. For more information about using CloudWatch
  with CodeBuild, see [Monitor CodeBuild builds with CloudWatch](monitoring-builds.md "monitoring-builds.md").

CPUUtilized

The number of CPU units of allocated processing used by the build
container.

Units: CPU units

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

CPUUtilizedPercent

The percentage of allocated processing used by the build container.

Units: Percent

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

MemoryUtilized

The number of megabytes of memory used by the build container.

Units: Megabytes

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

MemoryUtilizedPercent

The percentage of allocated memory used by the build container.

Units: Percent

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

StorageReadBytes

The storage read speed used by the build container.

Units: Bytes/second

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum

StorageWriteBytes

The storage write speed used by the build container.

Units: Bytes/second

Valid CloudWatch statistics: Average (recommended), Maximum, Minimum
