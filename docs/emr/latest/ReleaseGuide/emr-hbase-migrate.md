

# Migrating from previous HBase versions
<a name="emr-hbase-migrate"></a>

To migrate data from a previous HBase version, see [Upgrading](https://hbase.apache.org/book.html#upgrading) and [HBase version number and compatibility](https://hbase.apache.org/book.html#hbase.versioning) in the Apache HBase Reference Guide. You might need to pay special attention to the requirements for upgrading from pre-1.0 versions of HBase.

## Migrating to Amazon EMR version 7.4.0 or later
<a name="emr-hbase-migrate-versions"></a>

**Note**  
Follow these guidelines if you're migrating from an EMR release earlier than 7.4.0 to a release greater than 7.3.0.

If you are currently running an EMR version with Amazon's Store File Tracking feature enabled, which is included in versions 6.2.0 to 7.3.0, and you want to upgrade to a version with OSS Store File Tracking, which is available on EMR versions later than 7.3.0, follow these steps:

1. In the existing cluster:

   1. Disable the `hbase:storefile` table.

   1. Drop the `hbase:storefile` table.

   1. Flush `hbase:meta`.

   1. Wait for the metadata to be updated.

1. In the new cluster:

   1. Set the same Amazon S3 directory as the root directory.

   1. Start the cluster with the `DefaultStoreFileTracker` implementation:

      ```
      {
        "Classification": "hbase-site",
        "Properties": {
          hbase.store.file-tracker.impl: "org.apache.hadoop.hbase.regionserver.storefiletracker.DefaultStoreFileTracker"
         }
      }
      ```

   1. At the table or column family level, use the following commands to change the store file tracker:

      1. Change the table's or table column family's Store File Tracker:

         ```
         hbase> change_sft 't1','FILE'
         hbase> change_sft 't2','cf1','FILE'
         ```

      1. Change all of the table's Store File Tracker matching the given regular expression (regex):

         ```
         hbase> change_sft_all 't.*','FILE'
         hbase> change_sft_all 'ns:.*','FILE'
         hbase> change_sft_all 'ns:t.*','FILE'
         ```

## Migrating HBase on Amazon S3 clusters to Amazon EMR Version 7.12.0 or later using Read-Replica clusters
<a name="emr-hbase-migrate-s3-read-replica"></a>

Starting with EMR 7.12.0, you can switch a read-replica HBase on Amazon S3 cluster from read-only mode to active mode, enabling both read and write operations. This functionality is provided through two new HBase shell commands.

1. `readonly_state`

   Retrieves the current read-write operational state of the cluster.

   Output:
   + INACTIVE - Cluster is in read-only mode and write is in-active.
   + ACTIVE - Cluster supports both read and write operations.

1. `readonly_switch`

   Enables or disables read-only mode with configurable options for the switching process.

   Syntax:

   ```
   readonly_switch <readonly>,<force_flush>,<force_refresh_meta>,<force_refresh_hfile>
   ```

   Parameters:
   + readonly (required) - Boolean value to enable (true) or disable (false) read-only mode
   + force\_flush (optional) - Forces data flush before switching from active to read-only mode (default: true)
   + force\_refresh\_meta (optional) - Forces meta table refresh when switching from read-only to active mode (default: true)
   + force\_refresh\_hfile (optional) - Forces HFile refresh when switching from read-only to active mode (default: true)

### Migration Steps
<a name="emr-hbase-migrate-s3-steps"></a>

If you are currently running an EMR 6.0.0\+ HBase on Amazon S3 cluster and want to migrate to an EMR 7.12.0 or later cluster, follow these steps:

1. Ensure your source cluster is in a stable state with no inconsistencies using the hbck report or stuck procedures from the HBase master UI.

   ```
   sudo -u hbase hbase hbck > hbck_report.txt
   ```

1. Ensure there are no regions in the SPLIT state on the source cluster:

   1. If there are regions in SPLIT state, run major compactions on the respective tables and wait for them to complete

      ```
      major_compact <table_name>
      ```

   1. Run `catalogjanitor_run` in the HBase shell after the compaction is complete

1. Create a new EMR 7.12.0\+ cluster configured as a read-replica pointing to the same Amazon S3 location as your source cluster. Refer to this [blog](https://aws.amazon.com/blogs/big-data/setting-up-read-replica-clusters-with-hbase-on-amazon-s3/) for more details on how to set up a read replica cluster. Launch the new cluster with the DefaultStoreFileTracker configuration as mentioned in the above steps if you want to upgrade to the OSS Store file tracking.

1. Wait for the master node to initialize completely. Verify data accessibility by reading the tables and confirm the new cluster is in read-only mode

   ```
   hbase:001:0> readonly_state
   Took 0.4612 seconds
   => "INACTIVE"
   ```

1. Disable balancing and compactions on the source cluster:

   ```
   echo "balance_switch false" | hbase shell
   echo "compaction_switch false" | hbase shell
   ```

1. Ensure there are no overlaps/inconsistencies showing up in the read-replica cluster UI and verify that regions show OPEN status and are properly assigned.

1. Convert the Store file tracking using the commands on the read-replica cluster mentioned in the section above if you want to change to FileBasedTracker.

1. Stop the jobs pointing to the source cluster, flush all the tables, and shut down the source cluster. Wait for complete termination before proceeding.

   ```
   echo "flush 'usertable'" | hbase shell
   echo "flush 'hbase:meta'" | hbase shell
   echo "flush 'hbase:namespace'" | hbase shell
   ```

1. Switch the read-replica cluster to active mode to enable write operations. After completing this step, your new cluster will support both read and write operations, and the migration is complete.

   ```
   hbase:010:0> readonly_switch false
   Took 38.1568 seconds
   ```

1. Validate writes on the new cluster and ensure all regions are serving requests.

**Note**  
There can be only one active cluster pointing to an Amazon S3 location at any point in time. Therefore, switching the read-replica to active should be done only after the source cluster is terminated.