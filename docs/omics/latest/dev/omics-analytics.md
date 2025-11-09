# HealthOmics analytics

###### Important

AWS HealthOmics variant stores and annotation stores are no longer open to new customers.
Existing customers can continue to use the service as normal.
For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

HealthOmics analytics supports the storage and analysis of genomic variants and annotations. Analytics provides
two types of storage resources - Variant stores and Annotation stores. You use these resources to store, transform,
and query genomic variant data and annotation data. After you import data into a datastore, you can use Athena to
peform advanced analytics on the data.

You can use the HealthOmics console or API to create and manage stores, import data, and share analytic store data with collaborators.

Variant stores support data in VCF formats, and annotation stores support TSV/CSV and GFF3
formats. Genomic coordinates are represented as zero-based, half-closed half-open intervals.
When your data is in the HealthOmics analytics data store, access to the VCF files is managed
through AWS Lake Formation. You can then query the VCF files by using Amazon Athena. Queries
must use Athena query engine version 3. To read more about Athena query engine versions, see the
[Amazon Athena documentation](../../../athena/latest/ug/engine-versions-changing.md "../../../athena/latest/ug/engine-versions-changing.md").

###### Topics

- [Creating HealthOmics variant stores](creating-variant-stores.md "creating-variant-stores.md")
- [Creating HealthOmics variant store import jobs](parsing-annotation-stores.md "parsing-annotation-stores.md")
- [Creating HealthOmics annotation stores](creating-and-managing-annotation-store.md "creating-and-managing-annotation-store.md")
- [Creating import jobs for HealthOmics annotation stores](annotation-store-import-jobs.md "annotation-store-import-jobs.md")
- [Creating HealthOmics annotation store versions](annotation-store-versioning.md "annotation-store-versioning.md")
- [Deleting HealthOmics analytics stores](deleting-a-store-examples.md "deleting-a-store-examples.md")
- [Querying HealthOmics analytics data](analytics-query-data.md "analytics-query-data.md")
- [Sharing HealthOmics analytics stores](cross-account-sharing.md "cross-account-sharing.md")
