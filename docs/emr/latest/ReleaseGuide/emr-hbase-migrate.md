# Migrating from previous HBase versions

To migrate data from a previous HBase version, see [Upgrading](https://hbase.apache.org/book.html#upgrading "https://hbase.apache.org/book.html#upgrading") and [HBase version number and
compatibility](https://hbase.apache.org/book.html#hbase.versioning "https://hbase.apache.org/book.html#hbase.versioning") in the Apache HBase Reference Guide. You might need to pay
special attention to the requirements for upgrading from pre-1.0 versions of
HBase.

## Migrating to Amazon EMR version 7.4.0 or later

###### Note

Follow these guidelines if you're migrating from an EMR release earlier than 7.4.0 to a release greater than 7.3.0.

If you are currently running an
EMR version with Amazon's Store File Tracking feature enabled, which is included in versions 6.2.0 to 7.3.0, and you want to upgrade to a version
with OSS Store File Tracking, which is available on EMR versions later than 7.3.0, follow these steps:

1. In the existing cluster:
   1. Disable the `hbase:storefile` table.
   2. Drop the `hbase:storefile` table.
   3. Flush `hbase:meta`.
   4. Wait for the metadata to be updated.

2. In the new cluster:
   1. Set the same Amazon S3 directory as the root directory.
   2. Start the cluster with the `DefaultStoreFileTracker` implementation:

   ```
   {
     "Classification": "hbase-site",
     "Properties": {
       hbase.store.file-tracker.impl: "org.apache.hadoop.hbase.regionserver.storefiletracker.DefaultStoreFileTracker"
      }
   }
   ```

   3. At the table or column family level, use the following commands to change the store file tracker:
      1. Change the table's or table column family's Store File Tracker:

      ```
      hbase> change_sft 't1','FILE'
      hbase> change_sft 't2','cf1','FILE'
      ```

      2. Change all of the table's Store File Tracker matching the given regular expression (regex):

      ```
      hbase> change_sft_all 't.*','FILE'
      hbase> change_sft_all 'ns:.*','FILE'
      hbase> change_sft_all 'ns:t.*','FILE'
      ```
