# Amazon Detective Regions and quotas

When using Amazon Detective, be aware of these quotas.

## Detective Regions and endpoints

To see the list of AWS Regions where Detective is available, see [Detective service endpoints](../../../general/latest/gr/detective.md "../../../general/latest/gr/detective.md").

## Detective quotas

Detective has the following quotas, which cannot be configured.

| Resource                                                              | Quota         | Comments                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Number of member accounts                                             | 1,200         | The number of member accounts that an administrator account can add to a behavior graph.                                                                                                                                                                               |
| Behavior graph data volume – volume warning                           | 9 TB per day  | If the behavior graph data volume is larger than 9 TB per day, then Detective displays a warning that the behavior graph is nearing the maximum allowed volume.                                                                                                        |
| Behavior graph data volume – no new accounts                          | 10 TB per day | If the behavior graph data volume is larger than 10 TB per day, then you cannot add new member accounts to the behavior graph.                                                                                                                                         |
| Behavior graph data volume – stop data ingest into the behavior graph | 15 TB per day | If the behavior graph data volume is larger than 15 TB per day, then Detective stops ingesting data into the behavior graph. The 15 TB per day reflects both normal data volume and spikes in the data volume. To re-enable the data ingest, you must contact Support. | ## Internet Explorer 11 not supported You cannot use Detective with Internet Explorer 11. |
