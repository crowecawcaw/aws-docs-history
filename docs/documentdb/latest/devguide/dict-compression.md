

# Managing dictionary-based compression in Amazon DocumentDB 8.0
<a name="dict-compression"></a>

Amazon DocumentDB 8.0 introduces a new document compression algorithm, Zstd, as an improved alternative to LZ4. When you enable dictionary compression on an Amazon DocumentDB 8.0 collection by selecting Zstd as the compression algorithm, documents from your collection are sampled to create a custom compression dictionary. New and updated documents are compressed using this dictionary and the Zstd algorithm. This approach typically achieves higher compression ratios than standard compression methods, especially for collections with consistent document schemas or repeated field names. 

LZ4 is an algorithm designed for fast compression and decompression. It is known to be light on the CPU while achieving noticeable compression. Zstd is a general-purpose algorithm that with default settings uses more CPU but achieves better compression ratios than LZ4. The usage of dictionaries improves compression even further for most JSON documents. Some benefits of the Zstd algorithm are:
+ **Reduced Storage Costs** — Higher compression ratios mean less storage usage and lower costs.
+ **Lower I/O** — Compressed documents require less I/O, potentially improving performance.
+ **Optimized for your collection** — The dictionary is trained specifically for your collection's data patterns.

**Note**  
Dictionary-based compression is not supported on Amazon DocumentDB versions 3.6, 4.0, and 5.0.

## Performance considerations
<a name="perf-considerations"></a>

Zstd compression involves the following trade-offs: 
+ **Storage versus CPU** — Zstd compression achieves better compression ratios but may use slightly more CPU resources compared to LZ4 compression.
+ **Initial Compression** — New collections might not achieve optimal compression until enough documents are inserted to train an effective dictionary. Currently, Amazon DocumentDB trains a dictionary when a collection has at least 100 documents.
+ **Workload Type** — Read-intensive workloads where the entire data fits into the buffer cache may experience an increase in latency and CPU usage due to decompression overhead.

Zstd compression is particularly effective for collections with small documents, document arrays and repeated field names.

## Enabling dictionary-based compression
<a name="enabling-zstd"></a>

For new collections you can use the below command to enable Zstd compression: 

```
db.createCollection("myCollection", 
    { 
        storageEngine: { 
            documentDB: { 
                compression: {
                    enable: true,
                    algorithm: "zstd"
                } 
            }
        }
    }
 )
```

You can also enable or modify compression on an existing collection: 

```
db.runCommand({ 
    collMod: "myCollection", 
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

To enable the Zstd algorithm for all new collections in your cluster, set the `default_collection_compression` parameter in your cluster parameter group to `zstd`.

## Getting Started
<a name="getting-started"></a>

In Amazon DocumentDB 8.0, new collections use Zstd compression by default. To turn off compression for new collections, set the `default_collection_compression` parameter in your cluster parameter group to `disabled`.

Starting with Amazon DocumentDB 8.0, `enabled` is no longer a valid value for `default_collection_compression`. The valid values are `zstd`, `lz4`, and `disabled`.

## Monitoring
<a name="monitoring"></a>

You can view compression information for a collection using one of the following commands:
+ db.runCommand({ collStats: "myCollection" }) OR
+ db.collection.stats()

These commands return key statistics that you can use to compute compression ratio:
+ **compression.algorithm** — The algorithm used (`lz4` or `zstd`)
+ **storageSize** — The actual storage used by the collection, after compression. Note that this number includes fragmentation (that is, the unused space in database pages)
+ **avgObjSize** — The average logical size of the collection's documents, decompressed. Note that if your collection has more than 20k documents, this number will be an approximation based on a sample of 20k documents.
+ **size** — The logical size of the collection without compression. This number is obtained by multiplying avgObjSize by the total number of documents in the collection, so if avgObjSize is an approximation, this number will also be an approximation.
+ **count** — Number of documents in the collection

The following CloudWatch metrics can be helpful while evaluating dictionary-based compression:
+ CPUUtilization
+ FreeableMemory
+ VolumeBytesUsed
+ VolumeReadIOPs
+ VolumeWriteIOPs

collStats metrics:
+ storageSize
+ size

In addition, it can be useful to keep track of metrics specific to your application, like latency and throughput per query type or API.

### Compressor statistics
<a name="dict-compression-compressor-stats"></a>

Starting with Amazon DocumentDB 8.0.3, the `collStats` command and the `db.collection.stats()` method return a `compressor_stats` object inside the `compression` field. It reports how much data the compression algorithm has processed for the collection, and works for both Zstd and LZ4.

Use compressor statistics to see how effectively compression reduces the size of the data that you write to a collection. For example, you can use them to compare Zstd and LZ4 on your workload, or to evaluate a change to the compression threshold.

To view compressor statistics for a collection, run the following command:

```
db.runCommand({ collStats: "myCollection" })
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
    "threshold": 128,
    "algorithm": "lz4",
    "compressor_stats": {
        "input_bytes": 10000000,
        "output_bytes": 2500000,
        "compression_operations": 10000,
        "compression_ratio": 4
    }
}
```

The following table describes the fields in the `compression` object.


| Field | Description | 
| --- | --- | 
| enable | Specifies whether compression is enabled for the collection. | 
| threshold | The minimum document size for compression. The compressor doesn't compress documents smaller than this value. | 
| algorithm | The compression algorithm used by the collection (zstd or lz4). | 
| usingDictionary | Specifies whether the collection uses a trained compression dictionary. Returned only for Zstd. | 
| compressor\_stats.input\_bytes | Total uncompressed size, in bytes, of the data processed by the compressor. | 
| compressor\_stats.output\_bytes | Total size, in bytes, of the data after compression. | 
| compressor\_stats.compression\_operations | Number of documents that Amazon DocumentDB attempted to compress. This includes documents that meet the compression threshold but that Amazon DocumentDB stores uncompressed because compression doesn't reduce their size enough. | 
| compressor\_stats.compression\_ratio | input\_bytes divided by output\_bytes. Higher values mean better compression. If the compressor hasn't processed any documents, the ratio is 1, which indicates no compression. | 

In these examples, compression reduces 10,000 documents totaling 10 MB to 2.5 MB, a 4:1 compression ratio.

#### How compressor statistics accumulate
<a name="dict-compression-compressor-stats-understanding"></a>

Compressor statistics are cumulative totals of compression operations, and they don't represent the collection's current data size. The following table describes how operations on the collection affect these statistics.


| Operation | Counted in statistics? | Details | 
| --- | --- | --- | 
| Updating a document | Yes, on every update | If you update a document 10 times, the statistics include it 10 times. | 
| Deleting a document | Not subtracted | The compressor doesn't subtract deleted documents from input\_bytes or output\_bytes. | 
| Writing small documents | No | The compressor skips documents smaller than the compression threshold. | 
| Writing documents before compression is enabled or before the statistics were last reset | Not until updated | The compressor counts these documents when you update them. | 
| Writing documents while compression is disabled | No | collStats doesn't return compressor\_stats while compression is disabled. Disabling compression doesn't reset the statistics. When you re-enable compression, the compressor adds new values to the previous totals. | 

#### Choosing the right metric
<a name="dict-compression-compressor-stats-choosing"></a>

Compressor statistics and collection size statistics measure different things, so their ratios usually don't match. `compression_ratio` covers only data that the compressor processed. `size/storageSize` covers the whole collection, including uncompressed documents and page fragmentation.

The following table shows which metric to use, depending on your goal.


| Goal | Use | 
| --- | --- | 
| See how well recent writes compress, for example after switching from LZ4 to Zstd | compressor\_stats.compression\_ratio | 
| See the collection's overall storage savings | size/storageSize | 