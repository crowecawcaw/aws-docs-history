# Managing Aurora PostgreSQL Limitless Database

The following topics describe how to manage your Aurora PostgreSQL Limitless Database DB clusters.

###### Topics

- [Database and table size considerations](#limitless-db-size "#limitless-db-size")
- [Reclaiming storage space by vacuuming](limitless-vacuum.md "limitless-vacuum.md")

## Database and table size considerations

For Aurora PostgreSQL Limitless Database, on each shard a sharded table is divided into a number of table slices
that varies depending on how many shards are available in the DB shard group. Each table
slice can grow up to 32 TiB, but each shard has a maximum capacity of 128 TiB. Reference
tables have a size limit of 32 TiB for the entire DB shard group.

###### Note

The maximum capacity of each node (router or shard) is 128 TiB, as this is the
maximum capacity for an Aurora PostgreSQL DB cluster.

The maximum number of relations per database (including tables, views, and indexes) in both Aurora PostgreSQL and Aurora PostgreSQL Limitless Database is
1,431,650,303.

For more information, see [Appendix K. PostgreSQL limits](https://www.postgresql.org/docs/current/limits.html "https://www.postgresql.org/docs/current/limits.html") in the PostgreSQL
documentation and [Amazon Aurora size limits](CHAP_Limits.md#RDS_Limits.FileSize.Aurora "CHAP_Limits.md#RDS_Limits.FileSize.Aurora").
