# Monitoring your Amazon Neptune global database using CloudWatch metrics

Neptune supports the following CloudWatch metrics that you can use to monitor a
Neptune global database:

- **`GlobalDbDataTransferBytes`**   –  
  The number of bytes of redo log data transferred from the primary AWS Region to a secondary
  AWS Region in a Neptune global database.
- **`GlobalDbReplicatedWriteIO`**   –  
  The number of write I/O operations replicated from the primary AWS Region in the
  global database to the cluster volume in a secondary AWS Region.

The billing calculations for each DB cluster in a Neptune global database
use the `VolumeWriteIOPS` metric to account for writes performed
within that cluster. For the primary DB cluster, the billing calculations use
`NeptuneGlobalDbReplicatedWriteIO` to account for the cross-region
replication to secondary DB clusters.

- **`GlobalDbProgressLag`**   –  
  The number of milliseconds that a secondary cluster is behind the primary cluster
  for both user transactions and system transactions.

| Metric                      | Dimension                                                                                          | Published in       | Units        |
| --------------------------- | -------------------------------------------------------------------------------------------------- | ------------------ | ------------ |
| `GlobalDbDataTransferBytes` | SourceRegion, DBClusterIdentifier                                                                  | Secondary          | Bytes        |
| `GlobalDbReplicatedWriteIO` | SourceRegion, DBClusterIdentifier                                                                  | Secondary          | Count        |
| `GlobalDbProgressLag`       | DBClusterIdentifier, SecondaryRegion : in Primary DBClusterIdentifier, SourceRegion : in Secondary | Primary, Secondary | Milliseconds |
