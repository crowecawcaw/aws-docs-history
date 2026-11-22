

# Managing collection-level document compression

Amazon DocumentDB collection-level document compression lowers storage and I/O costs by compressing the documents in your collections. You can enable compression for a collection or for all new collections in a cluster, and measure the storage savings with collection statistics.

Amazon DocumentDB supports two compression algorithms:
+ **LZ4** — A fast algorithm that uses little CPU. Available in Amazon DocumentDB 5.0 and 8.0.
+ **Zstandard (Zstd)** — A dictionary-based algorithm that achieves higher compression ratios than LZ4. Available in Amazon DocumentDB 8.0.

The following table compares compression in Amazon DocumentDB 5.0 and 8.0.


|  | Amazon DocumentDB 5.0 | Amazon DocumentDB 8.0 | 
| --- | --- | --- | 
| Algorithms | LZ4 | Zstd, LZ4 | 
| Default for new collections | Disabled | Zstd | 
| Valid default\_collection\_compression values | enabled, disabled | zstd, lz4, disabled | 
| Default compression threshold | 2,032 bytes | 128 bytes (Zstd), 2,032 bytes (LZ4) | 

**Note**  
Amazon DocumentDB versions 3.6 and 4.0 don't support document compression.

**Topics**
+ [Choosing a compression algorithm](#doc-compression-algorithms)
+ [Managing document compression](#manage-compression)
+ [Monitoring document compression](#monitoring-compression)

## Choosing a compression algorithm
<a name="doc-compression-algorithms"></a>

LZ4 is designed for fast compression and decompression. It uses little CPU and achieves noticeable compression.

Zstd uses more CPU than LZ4 but achieves better compression ratios. When you choose Zstd for an Amazon DocumentDB 8.0 collection, Amazon DocumentDB samples documents from the collection to train a custom compression dictionary. Amazon DocumentDB compresses new and updated documents with this dictionary. Dictionaries improve compression further for most JSON documents, especially in collections with consistent schemas or repeated field names.

Zstd has the following benefits:
+ **Reduced storage costs** — Higher compression ratios mean less storage usage and lower costs.
+ **Lower I/O** — Compressed documents require less I/O, which can improve performance.
+ **Optimized for your collection** — Amazon DocumentDB trains the dictionary on your collection's data patterns.

Zstd involves the following trade-offs:
+ **Storage versus CPU** — Zstd achieves better compression ratios but can use slightly more CPU than LZ4.
+ **Initial compression** — New collections might not compress optimally until they contain enough documents to train an effective dictionary. Amazon DocumentDB trains a dictionary when a collection has at least 100 documents.
+ **Workload type** — Read-intensive workloads whose data fits in the buffer cache can see higher latency and CPU usage from decompression overhead.

Zstd is most effective for collections with small documents, document arrays, and repeated field names.

## Managing document compression
<a name="manage-compression"></a>

### Enabling document compression in a cluster
<a name="enabling-cluster-compression"></a>

The `default_collection_compression` cluster parameter sets the compression for new collections in a cluster. It doesn't change existing collections.
+ **Amazon DocumentDB 5.0** — The default value is `disabled`. Set the parameter to `enabled` to compress new collections with LZ4.
+ **Amazon DocumentDB 8.0** — The default value is `zstd`. Set the parameter to `lz4` to use LZ4, or to `disabled` to turn off compression for new collections. `enabled` isn't a valid value in Amazon DocumentDB 8.0.

New collections use the default compression threshold for their algorithm. For more information, see [Setting the compression thresholds](#set-compression-threshold).

### Enabling document compression in a collection
<a name="enabling-collection-compression"></a>

To enable compression when you create a collection on Amazon DocumentDB 5.0, use the `db.createCollection()` method:

```
db.createCollection("sample_collection", {
    storageEngine: {
        documentDB: {
            compression: {enable: true}
        }
    }
})
```

On Amazon DocumentDB 8.0, use the `algorithm` option to choose `zstd` or `lz4`:

```
db.createCollection("sample_collection", {
    storageEngine: {
        documentDB: {
            compression: {
                enable: true,
                algorithm: "zstd"
            }
        }
    }
})
```

### Compressing existing collections
<a name="compress-existing-collections"></a>

To change the compression settings of an existing collection, run the `collMod` command with a `storageEngine` configuration. The change applies only to documents that you insert or update afterward. Existing documents keep their current compression.

To turn off compression, set `enable` to `false`.

Amazon DocumentDB 5.0:

```
db.runCommand({
    collMod: "sample_collection",
    storageEngine: {
        documentDB: {compression: {enable: true}}
    }
})
```

Amazon DocumentDB 8.0:

```
db.runCommand({
    collMod: "sample_collection",
    storageEngine: {
        documentDB: {
            compression: {
                enable: true,
                algorithm: "zstd"
            }
        }
    }
})
```

### Setting the compression thresholds
<a name="set-compression-threshold"></a>

Amazon DocumentDB compresses only documents larger than the compression threshold. The default threshold depends on the algorithm:
+ **LZ4** — 2,032 bytes
+ **Zstd** — 128 bytes

To set the threshold when you create a collection, use the `createCollection` command:

```
db.createCollection("sample_collection", {
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

To change the threshold for an existing compressed collection, use the `collMod` command:

```
db.runCommand({
    collMod: "sample_collection",
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

The threshold must be between 128 and 8,000 bytes, and you must set `enable` to `true` when you specify it.

## Monitoring document compression
<a name="monitoring-compression"></a>

To view compression statistics for a collection, run `db.collection.stats()` or `db.runCommand({ collStats: "sample_collection" })`. The following example uses a scale factor of 1024\*1024 to return `size` and `storageSize` in MB.

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
    "compression" : {
        "enable" : true,
        "threshold" : 128,
        "algorithm" : "zstd",
        "usingDictionary" : true
    },
    ...
}
```
+ **compression.enable** — Whether compression is enabled.
+ **compression.threshold** — The compression threshold, in bytes. Amazon DocumentDB compresses only documents larger than this value.
+ **compression.algorithm** — The algorithm the collection uses (`lz4` or `zstd`).
+ **compression.usingDictionary** — For Zstd collections, whether Amazon DocumentDB compresses documents with a trained dictionary.
+ **storageSize** — The storage the collection uses after compression. This value includes fragmentation (unused space in database pages).
+ **avgObjSize** — The average decompressed size of the collection's documents, in bytes. For collections with more than 20,000 documents, Amazon DocumentDB estimates this value from a sample of 20,000 documents.
+ **size** — The logical size of the collection without compression: `avgObjSize` multiplied by `count`. If `avgObjSize` is an estimate, so is this value.
+ **count** — The number of documents in the collection.

To calculate the compression ratio, divide `size` by `storageSize`. In the example, 3906.3/1953.1 gives a 2:1 compression ratio.

To see how compression affects your cluster, watch the `CPUUtilization`, `FreeableMemory`, `VolumeBytesUsed`, `VolumeReadIOPs`, and `VolumeWriteIOPs` CloudWatch metrics.

Also track your application's own metrics, such as latency and throughput per query type or API.

### Compressor statistics
<a name="doc-compression-compressor-stats"></a>

Starting with Amazon DocumentDB 8.0.3, the `collStats` command and the `db.collection.stats()` method return a `compressor_stats` object inside the `compression` field. It reports how much data the compression algorithm has processed for the collection, and works for both Zstd and LZ4.

Use compressor statistics to see how effectively compression reduces the size of the data that you write to a collection. For example, you can use them to compare Zstd and LZ4 on your workload, or to evaluate a change to the compression threshold.

To view compressor statistics for a collection, run the following command:

```
db.runCommand({ collStats: "sample_collection" })
```

For a collection that uses Zstd, the output includes:

```
"compression": {
    "enable": true,
    "threshold": 128,
    "algorithm": "zstd",
    "usingDictionary": true,
    "compressor_stats": {
        "input_bytes": 10000000,
        "output_bytes": 2500000,
        "compression_operations": 10000,
        "compression_ratio": 4
    }
}
```

For a collection that uses LZ4, the output doesn't include `usingDictionary`:

```
"compression": {
    "enable": true,
    "threshold": 2032,
    "algorithm": "lz4",
    "compressor_stats": {
        "input_bytes": 10000000,
        "output_bytes": 2500000,
        "compression_operations": 10000,
        "compression_ratio": 4
    }
}
```

The following table describes the fields in the `compressor_stats` object.


| Field | Description | 
| --- | --- | 
| compressor\_stats.input\_bytes | Total uncompressed size, in bytes, of the data processed by the compressor. | 
| compressor\_stats.output\_bytes | Total size, in bytes, of the data after compression. | 
| compressor\_stats.compression\_operations | Number of documents that Amazon DocumentDB attempted to compress. This includes documents that meet the compression threshold but that Amazon DocumentDB stores uncompressed because compression doesn't reduce their size enough. | 
| compressor\_stats.compression\_ratio | input\_bytes divided by output\_bytes. Higher values mean better compression. If the compressor hasn't processed any documents, the ratio is 1, which indicates no compression. | 

In these examples, compression reduces 10,000 documents totaling 10 MB to 2.5 MB, a 4:1 compression ratio.

#### How compressor statistics accumulate
<a name="doc-compression-compressor-stats-understanding"></a>

Compressor statistics are cumulative totals of compression operations, and they don't represent the collection's current data size. The following table describes how operations on the collection affect these statistics.


| Operation | Counted in statistics? | Details | 
| --- | --- | --- | 
| Updating a document | Yes, on every update | If you update a document 10 times, the statistics include it 10 times. | 
| Deleting a document | Not subtracted | The compressor doesn't subtract deleted documents from input\_bytes or output\_bytes. | 
| Writing small documents | No | The compressor skips documents smaller than the compression threshold. | 
| Writing documents before compression is enabled or before the statistics were last reset | Not until updated | The compressor counts these documents when you update them. | 
| Writing documents while compression is disabled | No | collStats doesn't return compressor\_stats while compression is disabled. Disabling compression doesn't reset the statistics. When you re-enable compression, the compressor adds new values to the previous totals. | 

#### Choosing the right metric
<a name="doc-compression-compressor-stats-choosing"></a>

Compressor statistics and collection size statistics measure different things, so their ratios usually don't match. `compression_ratio` covers only data that the compressor processed. `size/storageSize` covers the whole collection, including uncompressed documents and page fragmentation.

The following table shows which metric to use, depending on your goal.


| Goal | Use | 
| --- | --- | 
| See how well recent writes compress, for example after switching from LZ4 to Zstd | compressor\_stats.compression\_ratio | 
| See the collection's overall storage savings | size/storageSize | 