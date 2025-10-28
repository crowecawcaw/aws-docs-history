# Best practice 10.3 – Utilize compression techniques to both decrease storage requirements and enhance I/O efficiency

Store data in a compressed format to reduce the burden on
the underlying storage host and network. For example, for
columnar data stored in Amazon S3, use a compatible
compression algorithm that supports parallel reads.

We recommend that your organization test the performance and
storage overhead of both uncompressed and compressed
datasets to determine best fit prior to implementing this
approach.

## Suggestion 10.3.1 – Compress data to reduce the transfer time

When storage read/write performance becomes a bottleneck,
use compression to reduce data transfer time. Consider the
tradeoffs between compute time needed to perform compression
and decompression versus the storage I/O bottleneck in your
estimates of overall improvements in performance efficiency.

## Suggestion 10.3.2 – Evaluate the available compression options for each resource of the workload

Compressing data can improve the performance as there are
fewer bytes transferred between the disk and compute
layers. The trade-off using this approach is that it
requires more compute for data compression and
decompression. You can, however, obtain a net efficiency
improvement if compression performs as well as or better
than uncompressed data transfer time. Compression also
requires much less storage, depending on the data type in
use, thus saving on data storage latency and costs.
