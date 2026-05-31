# Managing collection-level document compression

Amazon DocumentDB 5.0 collection-level document compression allows you to lower storage and IO costs by compressing the documents in your collections.
You can enable document compression at a collection level and view compression metrics as needed by measuring the storage gains through compression metrics such as storage size of compressed documents and compression status.
Amazon DocumentDB 5.0 uses the LZ4 compression algorithm to compress documents.

Amazon DocumentDB supports document compression starting with version 5.0.
The following are collection-level document compression functions:

- **Default behavior** — The default compression setting for new collections on a 5.0 cluster is determined by the cluster parameter `default_collection_compression`.
  This parameter is set to “disabled” by default.
- **Compressing existing collections** — The compression setting for existing collections can be changed using the `collMod` command.
- **Changing the compression threshold** — The default compression threshold is 2KB.
  This value can be specified for new collections using the `createCollection` command, and changed for existing collections using `collMod` command.

###### Note

Amazon DocumentDB document compression is not supported on Amazon DocumentDB versions 3.6 and 4.0.

###### Topics

- [Managing document compression](#manage-compression "#manage-compression")
- [Monitoring document compression](#monitoring-compression "#monitoring-compression")

## Managing document compression

### Enabling document compression in a collection

Enable document compression while creating a collection on Amazon DocumentDB 5.0 by using `db.createCollection()` method:

```
db.createCollection( sample_collection,{
    storageEngine : {
        documentDB: {
            compression:{enable: <true | false>}
        }
    }
})
```

### Enabling document compression in a cluster

Document compression can be enabled by default for all new collections on a cluster level by setting the cluster parameter `default_collection_compression` to “enabled”.
When this parameter is set to “enabled”, newly created collections on the cluster will have compression enabled by default with a compression threshold of 2 KB.

### Compressing existing collections

You can also modify the compression settings for an existing collection using the `collMod` operation and specifying the following `storageEngine` configuration.
Please note that the change made using this command will only apply to newly inserted/updated documents and the compression on previously inserted documents will not change.

```
db.runCommand({
    collMod: "orders",
    storageEngine: {
        documentDB: {compression: {enable: <true | false>} }
    }
})
```

### Setting the compression thresholds

By default, the compression threshold for compressed collections is 2032 bytes.
This threshold value can be set in the `createCollection` command when creating a new collection with compression enabled:

```
db.createCollection( sample_collection, {
    storageEngine : {
        documentDB: {
            compression: {
                enable: true,
                threshold: <128 - 8000>
            }
        }
    }
})
```

You can also modify the compression threshold for an existing compressed collection using the `collMod` operation and specifying the following `storageEngine` configuration:

```
db.runCommand({
    collMod: "orders",
    storageEngine: {
        documentDB: {
            compression: {
                enable: true,
                threshold: <128 - 8000>
            }
        }
    }
})
```

Please note that the compression threshold can only be set to a value between 128 to 8000 bytes.
Additionally, the `enable` option needs to be set to “true” when specifying the compression threshold.

## Monitoring document compression

You can check if a collection is compressed and calculate it's compression ratio as follows.

View compression statistics by running the `db.printCollectionStats()` or `db.collection.stats()` command from the mongo shell.
The output shows you the original size and compressed size that you can compare to analyze the storage gains from document compression.
In this example, statistics for a collection named “sample_collection” are shown below.
A scaling factor of 1024\*1024 is used below to output the `size` and `storageSize` values in MB.

```
db.sample_collection.stats(1024*1024)
```

The following is an example of the output for the above command:

```
{
    "ns" : "test.sample_collection",
    "count" : 1000000,
    "size" : 3906.3,
    "avgObjSize" : 4096,
    "storageSize" : 1953.1,
    compression:{"enabled" : true,"threshold" : 2032},
    ...
}
```

- **size** - The original size of the document collection.
- **avgObjSize** - The average document size before compression rounded off to first decimal. The unit of measure is bytes.
- **storageSize** - The storage size of the collection after compression. The unit of measure is bytes.
- **enabled** - Indicates if compression is enabled or disabled.

To calculate the actual compression ratio, divide the collection size by the storage size (size/storageSize).
For the example above, the calculation is 3906.3/1953.1 which translates to a 2:1 compression ratio.
