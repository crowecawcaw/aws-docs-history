# Importing data from Db2 to Amazon RDS for Db2 with the INGEST utility

You can use the `INGEST` utility to continually stream data from files and
pipes on a client machine to a target Amazon RDS for Db2 DB instance. The `INGEST`
utility supports `INSERT` and `MERGE` operations. For more
information, see [Ingest
utility](https://www.ibm.com/docs/en/db2/11.1?topic=reference-ingest-utility "https://www.ibm.com/docs/en/db2/11.1?topic=reference-ingest-utility") in the IBM Db2 documentation.

Because the `INGEST` utility supports nicknames, you can use the utility to
transfer data from your self-managed Db2 database to an RDS for Db2 database. This approach
works as long as network connectivity exists between the two databases.

###### Important

The `INGEST` utility doesn't support large objects (LOBs). Use the [IMPORT command](db2-native-db2-tools-import.md "db2-native-db2-tools-import.md") instead.

To use the `RESTARTABLE` feature of the `INGEST` utility, run the
following command on the RDS for Db2 database.

```
db2 "call sysproc.sysinstallobjects(‘INGEST’,‘C’,NULL,NULL)"
```
