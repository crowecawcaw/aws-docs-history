# Viewing Amazon S3 Storage Lens metrics using a data

export

Amazon S3 Storage Lens metrics are generated daily in CSV or Apache Parquet-formatted
metrics export files and placed in an S3 general purpose bucket in your account. From there, you
can ingest the metrics export into the analytics tools of your choice, such as Amazon Quick Suite and
Amazon Athena, where you can analyze storage usage and activity trends. You can also send daily
metric exports to an AWS-managed S3 table bucket for immediate querying, using AWS analytics
services or third-party tools.

###### Topics

- [Using an AWS KMS key to encrypt your
  metrics exports](storage_lens_encrypt_permissions.md "storage_lens_encrypt_permissions.md")
- [What is an S3 Storage Lens export
  manifest?](storage_lens_whatis_metrics_export_manifest.md "storage_lens_whatis_metrics_export_manifest.md")
- [Understanding the
  Amazon S3 Storage Lens export schemas](storage_lens_understanding_metrics_export_schema.md "storage_lens_understanding_metrics_export_schema.md")
