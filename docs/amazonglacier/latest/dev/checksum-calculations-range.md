**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Receiving Checksums When Downloading Data

When you retrieve an archive using the Initiate Job API (see [Initiate Job (POST jobs)](api-initiate-job-post.md "api-initiate-job-post.md")), you can
optionally specify a range to retrieve of the archive. Similarly, when you download your
data using the Get Job Output API (see [Get Job Output (GET output)](api-job-output-get.md "api-job-output-get.md")), you can optionally specify a range of data to
download. There are two characteristics of these ranges that are important to understand
when you are retrieving and downloading your archive's data. The range to retrieve is
required to be _megabyte aligned_ to the archive. Both the range to
retrieve and the range to download must be _tree hash aligned_ in
order to receive checksum values when you download your data. The definition of these
two types of range alignments are as follows:

- Megabyte aligned - A range [*StartByte*,
  *EndBytes*] is megabyte (1024\*1024) aligned when
  _StartBytes_ is divisible by 1 MB and
  _EndBytes_ plus 1 is divisible by 1 MB or is equal to
  the end of the archive specified (archive byte size minus 1). A range used
  in the Initiate Job API, if specified, is required to be megabyte
  aligned.
- Tree-hash aligned - A range [*StartBytes*,
  *EndBytes*] is tree hash aligned with respect to an
  archive if and only if the root of the tree hash built over the range is
  equivalent to a node in the tree hash of the whole archive. Both the range
  to retrieve and range to download must be tree hash aligned in order to
  receive checksum values for the data you download. For an example of ranges
  and their relationship to the archive tree hash, see [Tree Hash Example:
  Retrieving an archive range that is tree-hash aligned](#checksum-calculations-upload-archive-with-ranges "#checksum-calculations-upload-archive-with-ranges").

Note that a range that is tree-hash aligned is also megabyte aligned.
However, a megabyte aligned range is not necessarily tree-hash aligned.
The following cases describe when you receive a checksum value when you download your
archive data:

- If you do not specify a range to retrieve in the Initiate Job request and
  you download the whole archive in the Get Job Request.
- If you do not specify a range to retrieve in the Initiate Job request and
  you do specify a tree-hash aligned range to download in the Get Job
  Request.
- If you specify a tree-hash aligned range to retrieve in the Initiate Job
  request and you download the whole range in the Get Job Request.
- If you specify a tree-hash aligned range to retrieve in the Initiate Job
  request and you specify a tree-hash aligned range to download in the Get Job
  Request.
  If you specify a range to retrieve in the Initiate Job request that is not tree hash
  aligned, then you can still get your archive data but no checksum values are returned
  when you download data in the Get Job Request.

## Tree Hash Example:

Retrieving an archive range that is tree-hash aligned

Suppose you have a 6.5 MB archive in your vault and you want to retrieve 2 MB of the
archive. How you specify the 2 MB range in the Initiate Job request determines if
you receive data checksum values when you download your data. The following diagram
illustrates two 2 MB ranges for the 6.5 MB archive that you could download. Both
ranges are megabyte aligned, but only one is tree-hash aligned.

![Diagram showing retrieval of an archive range that is tree-hash aligned.](images/TreeHash-ArchiveWithRanges.png)

## Tree-Hash Aligned Range Specification

This section gives the exact specification for what constitutes a tree-hash
aligned range. Tree-hash aligned ranges are important when you are downloading a
portion of an archive and you specify the range of data to retrieve and the range to
download from the retrieved data. If both of these ranges are tree-hash aligned, then
you will receive checksum data when you download the data.

A range [*A*, *B*] is _tree-hash
aligned_ with respect to an archive if and only if when a new tree
hash is built over [*A*, *B*], the root of the
tree hash of that range is equivalent to a node in the tree hash of the whole
archive. You can see this shown in the diagram in [Tree Hash Example:
Retrieving an archive range that is tree-hash aligned](#checksum-calculations-upload-archive-with-ranges "#checksum-calculations-upload-archive-with-ranges"). In this section, we
provide the specification for tree-hash alignment.

Consider [_P_, _Q_) as the range query for
an archive of _N_ megabytes (MB) and _P_ and
_Q_ are multiples of one MB. Note that the actual inclusive
range is [*P* MB, *Q* MB – 1 byte], but for
simplicity, we show it as [_P_, _Q_). With
these considerations, then

- If _P_ is an odd number, there is only one possible
  tree-hash aligned range—that is [_P_,
  _P_ + 1 MB).
- If _P_ is an even number and _k_
  is the maximum number, where _P_ can be written as
  2*k* \* _X_, then there are at
  most _k_ tree-hash aligned ranges that start with
  _P_. _X_ is an integer greater
  than 0. The tree-hash aligned ranges fall in the following categories:
  - For each _i_, where (0 <=
    _i_ <= _k_) and
    where _P_ +
    2*i*
    < _N_, then [_P_,
    _Q_ +
    2*i*)
    is a tree-hash aligned range.
  - _P_ = 0 is the special case where
    _A_ = 2[lgN]\*0
