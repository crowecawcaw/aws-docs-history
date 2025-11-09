# HealthOmics ETags and data provenance

A HealthOmics ETag (entity tag) is a hash of the ingested content in a sequence store. This simplifies data
retrieval and processing while maintaining the content integrity of the ingested data files. The ETag reflects
changes to the semantic content of the object, not its metadata. The specified read set type and algorithm determine
how the ETag is calculated. The ETag calculation doesn't alter the actual file or genomic data. When the file type
schema of the read set permits it, the sequence store updates fields that are linked to data provenance.

Files have a bitwise identity and a semantic identity. The bitwise identity means that the bits of a ﬁle are
identical, and a semantic identity means that the contents of a ﬁle are identical. Semantic identity is resilient
to metadata changes and compression changes as it captures the content integrity of the file.

Read sets in HealthOmics sequence stores undergo compression/decompression cycles and data provenance tracking
throughout an object's lifecycle. During this processing, the bitwise identity of an ingested ﬁle may change and
is expected to change each time a file is activated; however, the semantic identity of the ﬁle is maintained. The
semantic identity is captured as a HealthOmics entity tag, or ETag that's calculated during sequence store
ingestion and available as read set metadata.

When the ﬁle type schema of the read set permits it, the sequence store updates ﬁelds are linked to data
provenance. For uBAM, BAM, and CRAM ﬁles, a new `@CO` or `Comment` tag is added to the header.
The comment contains the sequence store ID and ingestion timestamp.

## Amazon S3 ETags

When accessing a file using the Amazon S3 URI, Amazon S3 API operations may also return Amazon S3 ETag and checksum values.
The Amazon S3 ETag and checksum values differ from the HealthOmics ETags because they represent the file's bitwise identity.
To learn more about descriptive metadata and Objects, see the Amazon S3 [Object API documentation](../../../AmazonS3/latest/API/API_Object.md "../../../AmazonS3/latest/API/API_Object.md"). Amazon S3
ETag values can change with each activation cycle of a read set and you can use them to validate the reading of a
file. However, don't cache Amazon S3 ETag values to use for file identity validation during the file's lifecycle
because they don't remain consistent. In contrast, the HealthOmics ETag remains consistent throughout the read set's
lifecycle.

## How HealthOmics calculates ETags

The ETag is generated from a hash of the ingested file contents. The ETag algorithm family is set to
MD5up by default, but it can be configured differently during sequence store creation. When the ETag is
calculated, the algorithm and the calculated hashes are added to the read set. The supported MD5 algorithms for
file types are as follows.

- _FASTQ_MD5up_ – Calculates the MD5
  hash of an uncompressed, complete FASTQ read set source.
- _BAM_MD5up_ – Calculates the MD5 hash of the alignment
  section of an uncompressed BAM or uBAM read set source as represented in the SAM, based on the linked
  reference, if one is available.
- _CRAM_MD5up_ – Calculates the MD5 hash of the alignment
  section of the uncompressed CRAM read set source as represented in the SAM, based on the linked
  reference.

###### Note

MD5 hashing is known to be vulnerable to collisions. Because of this, two
different files might have the same ETag if they were manufactured to exploit
the known collision.

The following algorithms are supported for the SHA256 family. The algorithms are calculated as
follows:

- _FASTQ_SHA256up_ – Calculates the SHA-256 hash of an
  uncompressed, complete FASTQ read set source.
- _BAM_SHA256up_ – Calculates the SHA-256 hash of the
  alignment section of an uncompressed BAM or uBAM read set source as represented in the SAM, based on the
  linked reference, if one is available.
- _CRAM_SHA256up_ – Calculates the SHA-256 hash of the
  alignment section of an uncompressed CRAM read set source as represented in the SAM, based on the linked
  reference.

The following algorithms are supported for the SHA512 family. The algorithms are calculated as
follows:

- _FASTQ_SHA512up_ – Calculates the SHA-512 hash of an
  uncompressed, complete FASTQ read set source.
- _BAM_SHA512up_ – Calculates the SHA-512 hash of the
  alignment section of an uncompressed BAM or uBAM read set source as represented in the SAM, based on the
  linked reference, if one is available.
- _CRAM_SHA512up_ – Calculates the SHA-512 hash of the
  alignment section of an uncompressed CRAM read set source as represented in the SAM, based on the linked
  reference.
