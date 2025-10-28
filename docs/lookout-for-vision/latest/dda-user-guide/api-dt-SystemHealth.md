Defect Detection App is in preview release and is subject to change.

# SystemHealth

Information about the health of a station. To get the station health,
call the [GET
/system-health](api-get-system-health.md "api-get-system-health.md") operation.
For more information, see [Managing station health](dda-managing-system-health.md "dda-managing-system-health.md").

## cpuUsagePercent

The percentage CPU usage for the edge device that hosts the station. The percentage is a float
value ranging from 0 (0%) to 1.0 (100%).

Type: Float

## memoryUsagePercent

The percentage amount memory that the station is using on the edge device. The
percentage is a float value ranging from 0 (0%) to 1.0 (100%).

Type: Float

## disktotalSize

The size of the disk volume where the
`/aws_dda/` folder is mounted.

Type: String

## diskUsedSize

The amount of space that the station is using on the disk volume where the
`/aws_dda/` folder is mounted.

Type: String

## diskUsagePercent

The percentage amount of space that the station is using on the disk volume
where the `/aws_dda/` folder is mounted. The percentage is a float
value ranging from 0 (0%) to 1.0 (100%).

Type: Float
