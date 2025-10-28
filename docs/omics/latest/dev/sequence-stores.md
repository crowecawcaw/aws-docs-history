AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# HealthOmics storage

Use HealthOmics storage to store, retrieve, organize, and share genomics data efficiently and at low cost.
HealthOmics storage understands the relationships between different data objects, so that you can define which read
sets originated from the same source data. This provides you with data provenance.

Data that's stored in `ACTIVE` state is retrievable immediately. Data that hasn't been accessed for
30 days or more is stored in `ARCHIVE` state. To access archived data, you can reactivate it through the
API operations or console.

HealthOmics sequence stores are designed to preserve the content integrity of files. However, bitwise
equivalence of imported data files and exported files isn't preserved because of the compression during active and
archive tiering.

During ingestion, HealthOmics generates an entity tag, or _HealthOmics ETag_, to make it possible to
validate the content integrity of your data files. Sequencing portions are identified and captured as an ETag at the
source level of a read set. The ETag calculation doesn't alter the actual file or genomic data. After a read set is
created, the ETag shouldn't change throughout the lifecycle of the read set source. This means that reimporting the
same file results in the same ETag value being calculated.

###### Topics

- [HealthOmics ETags and data provenance](etags-and-provenance.md "etags-and-provenance.md")
- [Creating a HealthOmics reference store](create-reference-store.md "create-reference-store.md")
- [Creating a HealthOmics sequence store](create-sequence-store.md "create-sequence-store.md")
- [Deleting HealthOmics reference and
  sequence stores](deleting-reference-and-sequence-stores.md "deleting-reference-and-sequence-stores.md")
- [Importing read sets into a HealthOmics sequence store](import-sequence-store.md "import-sequence-store.md")
- [Direct upload to a HealthOmics sequence store](synchronous-uploads.md "synchronous-uploads.md")
- [Exporting HealthOmics read sets to an Amazon S3 bucket](read-set-exports.md "read-set-exports.md")
- [Accessing HealthOmics read sets with Amazon S3 URIs](s3-access.md "s3-access.md")
- [Activating read sets in HealthOmics](activating-read-sets.md "activating-read-sets.md")
