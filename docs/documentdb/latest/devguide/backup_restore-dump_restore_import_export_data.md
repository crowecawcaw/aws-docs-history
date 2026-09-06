

# Dumping, restoring, importing, and exporting data
<a name="backup_restore-dump_restore_import_export_data"></a>

You can use the `mongodump`, `mongorestore`, `mongoexport`, and `mongoimport` utilities to move data in and out of your Amazon DocumentDB cluster. This section discusses the purpose of each of these tools and configurations to help you achieve better performance.

**MongoDB Database Tools version requirement**  
Use MongoDB Database Tools up to and including version 100.11.0 for Amazon DocumentDB. To download, see [MongoDB Database Tools releases](https://www.mongodb.com/download-center/database-tools/releases/archive) on the MongoDB website.

**Topics**
+ [`mongodump`](#backup_restore-dump_restore_import_export_data-mongodump)
+ [`mongorestore`](#backup_restore-dump_restore_import_export_data-mongorestore)
+ [`mongoexport`](#backup_restore-dump_restore_import_export_data-mongoexport)
+ [`mongoimport`](#backup_restore-dump_restore_import_export_data-mongoimport)
+ [Tutorial](#backup_restore-dump_restore_import_export_data-tutorial)

## `mongodump`
<a name="backup_restore-dump_restore_import_export_data-mongodump"></a>

The `mongodump` utility creates a binary (BSON) backup of a MongoDB database. The `mongodump` tool is the preferred method of dumping data from your source MongoDB deployment when looking to restore it into your Amazon DocumentDB cluster due to the size efficiencies achieved by storing the data in a binary format.

Depending on the resources available on the instance or machine you are using to perform the command, you can speed up your `mongodump` by increasing the number of parallel collections dumped from the default 1 using the `--numParallelCollections` option. A good rule of thumb is to start with one worker per vCPU on your Amazon DocumentDB cluster's primary instance.

### Example usage
<a name="backup_restore-dump_restore_import_export_data-mongodump-example"></a>

The following is an example usage of the `mongodump` utility in the Amazon DocumentDB cluster, `sample-cluster`.

```
mongodump --ssl \
    --host="sample-cluster.node.us-east-1.docdb.amazonaws.com:27017" \
    --collection=sample-collection \
    --db=sample-database \
    --out=sample-output-file \
    --numParallelCollections 4  \
    --username=sample-user \
    --password=abc0123 \
    --sslCAFile global-bundle.pem
```

## `mongorestore`
<a name="backup_restore-dump_restore_import_export_data-mongorestore"></a>

The `mongorestore` utility enables you to restore a binary (BSON) backup of a database that was created with the `mongodump` utility. You can improve restore performance by increasing the number of workers for each collection during the restore with the `--numInsertionWorkersPerCollection` option (the default is 1). A good rule of thumb is to start with one worker per vCPU on your Amazon DocumentDB cluster's primary instance.

### Example usage
<a name="backup_restore-dump_restore_import_export_data-mongorestore-example"></a>

The following is an example usage of the `mongorestore` utility in the Amazon DocumentDB cluster, `sample-cluster`.

```
mongorestore --ssl \
    --host="sample-cluster.node.us-east-1.docdb.amazonaws.com:27017" \
    --username=sample-user \
    --password=abc0123 \
    --sslCAFile global-bundle.pem <fileToBeRestored>
```

## `mongoexport`
<a name="backup_restore-dump_restore_import_export_data-mongoexport"></a>

The `mongoexport` tool exports data in Amazon DocumentDB to JSON, CSV, or TSV file formats. The `mongoexport` tool is the preferred method of exporting data that needs to be human or machine readable.

**Note**  
`mongoexport` does not directly support parallel exports. However, it is possible to increase performance by executing multiple `mongoexport` jobs concurrently for different collections.

### Example usage
<a name="backup_restore-dump_restore_import_export_data-mongoexport-example"></a>

The following is an example usage of the `mongoexport` tool in the Amazon DocumentDB cluster, `sample-cluster`.

```
mongoexport --ssl \
    --host="sample-cluster.node.us-east-1.docdb.amazonaws.com:27017" \
    --collection=sample-collection \
    --db=sample-database \
    --out=sample-output-file \
    --username=sample-user \
    --password=abc0123 \
    --sslCAFile global-bundle.pem
```

## `mongoimport`
<a name="backup_restore-dump_restore_import_export_data-mongoimport"></a>

The `mongoimport` tool imports the contents of JSON, CSV, or TSV files into an Amazon DocumentDB cluster. You can use the `-–numInsertionWorkers` parameter to parallelize and speed up the import (the default is 1).

### Example usage
<a name="backup_restore-dump_restore_import_export_data-mongoimport-example"></a>

The following is an example usage of the `mongoimport` tool in the Amazon DocumentDB cluster, `sample-cluster`.

```
mongoimport --ssl \
    --host="sample-cluster.node.us-east-1.docdb.amazonaws.com:27017" \
    --collection=sample-collection \
    --db=sample-database \
    --file=<yourFile> \
    --numInsertionWorkers 4 \
    --username=sample-user \
    --password=abc0123 \
    --sslCAFile global-bundle.pem
```

## Tutorial
<a name="backup_restore-dump_restore_import_export_data-tutorial"></a>

The following tutorial describes how to use the `mongodump`, `mongorestore`, `mongoexport`, and `mongoimport` utilities to move data in and out of an Amazon DocumentDB cluster.

1. **Prerequisites** — Before you begin, ensure that your Amazon DocumentDB cluster is provisioned and that you have access to an Amazon EC2 instance in the same VPC as your cluster. For more information, see [Connect using Amazon EC2](connect-ec2.md). 

   To be able to use the mongo utility tools, you must have the mongodb-org-tools package installed in your EC2 instance, as follows.

   ```
   sudo yum install mongodb-org-tools-4.0.18
   ```

   Because Amazon DocumentDB uses Transport Layer Security (TLS) encryption by default, you must also download the Amazon RDS certificate authority (CA) file to use the mongo shell to connect, as follows.

   ```
   wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
   ```

1. **Download sample data** — For this tutorial, you will download some sample data that contains information about restaurants.

   ```
   wget https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/restaurant.json
   ```

1. **Import the sample data into Amazon DocumentDB ** — Since the data is in a logical JSON format, you will use the `mongoimport` utility to import the data into your Amazon DocumentDB cluster.

   ```
   mongoimport --ssl \ 
       --host="tutorialCluster.amazonaws.com:27017" \ 
       --collection=restaurants \
       --db=business \ 
       --file=restaurant.json \
       --numInsertionWorkers 4 \
       --username=<yourUsername> \
       --password=<yourPassword> \
       --sslCAFile global-bundle.pem
   ```

1. **Dump the data with `mongodump` ** — Now that you have data in your Amazon DocumentDB cluster, you can take a binary dump of that data using the `mongodump` utility.

   ```
   mongodump --ssl \
       --host="tutorialCluster.us-east-1.docdb.amazonaws.com:27017"\
       --collection=restaurants \
       --db=business \
       --out=restaurantDump.bson \
       --numParallelCollections 4 \
       --username=<yourUsername> \
       --password=<yourPassword> \
       --sslCAFile global-bundle.pem
   ```

1. **Drop the `restaurants` collection** — Before you restore the `restaurants` collection in the `business` database, you have to first drop the collection that already exists in that database, as follows. 

   ```
   use business
   ```

   ```
   db.restaurants.drop()
   ```

1. **Restore the data with `mongorestore`** — With the binary dump of the data from Step 3, you can now use the `mongorestore` utility to restore your data to your Amazon DocumentDB cluster.

   ```
   mongorestore --ssl \
       --host="tutorialCluster.us-east-1.docdb.amazonaws.com:27017" \
       --numParallelCollections 4 \
       --username=<yourUsername> \
       --password=<yourPassword> \
       --sslCAFile global-bundle.pem restaurantDump.bson
   ```

1. **Export the data using `mongoexport`** — To complete the tutorial, export the data from your cluster in the format of a JSON file, no different than the file you imported in Step 1. 

   ```
   mongoexport --ssl \
       --host="tutorialCluster.node.us-east-1.docdb.amazonaws.com:27017" \
       --collection=restaurants \
       --db=business \
       --out=restaurant2.json \
       --username=<yourUsername> \
       --password=<yourPassword> \
       --sslCAFile global-bundle.pem
   ```

1. **Validation** — You can validate that the output of Step 5 yields the same result as Step 1 with the following commands.

   ```
   wc -l restaurant.json
   ```

   Output from this command:

   ```
   2548 restaurant.json
   ```

   ```
   wc -l restaurant2.json
   ```

   Output from this command:

   ```
   2548 restaurant2.json
   ```