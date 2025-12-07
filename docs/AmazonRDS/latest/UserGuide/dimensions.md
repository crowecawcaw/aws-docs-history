# Amazon CloudWatch dimensions for Amazon RDS

You can filter Amazon RDS metrics
data by using any dimension in the following table.

| Dimension                          | Filters the requested data for . . .                                                                                                            |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `DBInstanceIdentifier`             | A specific DB instance.                                                                                                                         |
| `DatabaseClass`                    | All instances in a database class. For example, you can aggregate metrics for all instances<br>that belong to the database class `db.r5.large`. |
| `EngineName`                       | The identified engine name only. For example, you can aggregate metrics for all instances that have the engine name<br>`postgres`.              |
| `SourceRegion`                     | The specified Region only. For example, you can aggregate metrics for all DB instances in<br>the `us-east-1` Region.                            |
| `DbInstanceIdentifier, VolumeName` | The metrics per-volume for a single instance.<br>RDS captures metrics for multiple storage volumes.                                             |

###### Note

If you are using additional storage volumes, you can see aggregate storage metrics under
the `DBInstanceIdentifier` dimension. To see per-volume storage metrics, use the
`DbInstanceIdentifier, VolumeName` dimensions.
