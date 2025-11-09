# Supported storage classes and formats

To help you discover sensitive data in your Amazon Simple Storage Service (Amazon S3) data estate, Amazon Macie supports
most Amazon S3 storage classes and a wide variety of file and storage formats. This support applies to
the use of [managed data identifiers](managed-data-identifiers.md "managed-data-identifiers.md") and the use of
[custom data identifiers](custom-data-identifiers.md "custom-data-identifiers.md") to analyze S3
objects.

For Macie to analyze an S3 object, the object has to be stored in an Amazon S3 general purpose
bucket using a supported storage class. The object also has to use a supported file or storage
format. The topics in this section list the storage classes and the file and storage formats that
Macie currently supports.

###### Tip

Although Macie is optimized for Amazon S3, you can use it to discover sensitive data in resources
that you currently store elsewhere. You can do this by moving the data to Amazon S3 temporarily or
permanently. For example, export Amazon Relational Database Service or Amazon Aurora snapshots to Amazon S3 in Apache Parquet
format. Or export an Amazon DynamoDB table to Amazon S3. You can then create a sensitive data discovery job
to analyze the data in Amazon S3.

###### Topics

- [Supported storage
  classes](#discovery-supported-s3-classes "#discovery-supported-s3-classes")
- [Supported file and storage
  formats](#discovery-supported-formats "#discovery-supported-formats")

## Supported Amazon S3 storage classes

For sensitive data discovery, Amazon Macie supports the following Amazon S3 storage classes:

- Reduced Redundancy (RRS)
- S3 Glacier Instant Retrieval
- S3 Intelligent‐Tiering
- S3 One Zone‐Infrequent Access (S3 One Zone‐IA)
- S3 Standard
- S3 Standard‐Infrequent Access (S3 Standard‐IA)

Macie doesn’t analyze S3 objects that use other Amazon S3 storage classes, such as
S3 Glacier Deep Archive or S3 Express One Zone. In addition, Macie doesn't analyze
objects that are stored in S3 directory buckets.

If you configure a sensitive data discovery job to analyze S3 objects that don't use a supported Amazon S3 storage
class, Macie skips those objects when the job runs. Macie doesn't attempt to retrieve or analyze
data in the objects—the objects are treated as _unclassifiable
objects_. An _unclassifiable object_ is an object
that doesn't use a supported storage class or a supported file or storage format. Macie analyzes
only those objects that use a supported storage class and a supported file or storage
format.

Similarly, if you configure Macie to perform automated sensitive data discovery, unclassifiable objects aren't
eligible for selection and analysis. Macie selects only those objects that use a supported Amazon S3
storage class and a supported file or storage format.

To identify S3 buckets that store unclassifiable objects, you can [filter your S3 bucket inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md"). For each bucket
in your inventory, there are fields that report the number and total storage size of
unclassifiable objects in the bucket.

For detailed information about the storage classes that Amazon S3 provides, see [Using Amazon S3 storage
classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md") in the _Amazon Simple Storage Service User Guide_.

## Supported file and storage formats

When Amazon Macie analyzes an S3 object, Macie retrieves the latest version of the object from
Amazon S3, and then performs a deep inspection of the object's contents. This inspection factors the
file or storage format of the data. Macie can analyze data in many different formats, including
commonly used compression and archive formats.

When Macie analyzes data in a compressed or archive file, Macie inspects both the full file
and the contents of the file. To inspect the file’s contents, Macie decompresses the file, and
then inspects each extracted file that uses a supported format. Macie can do this for as many as
1,000,000 files and up to a nested depth of 10 levels. For information about additional quotas
that apply to sensitive data discovery, see [Quotas for Macie](macie-quotas.md "macie-quotas.md").

The following table lists and describes the types of file and storage formats that Macie can
analyze to detect sensitive data. For each supported type, the table also lists the applicable
file name extensions.

| File or storage type   | Description                                                                                                                                                                                                                                                                                        | File name extensions                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Big data               | Apache Avro object containers and Apache Parquet files                                                                                                                                                                                                                                             | .avro, .parquet                                                                                                               |
| Compression or archive | GNU Zip compressed archives, TAR archives, and ZIP compressed archives                                                                                                                                                                                                                             | .gz, .gzip, .tar, .zip                                                                                                        |
| Document               | Adobe Portable Document Format files, Microsoft Excel workbooks, and Microsoft Word<br>documents                                                                                                                                                                                                   | .doc, .docx, .pdf, .xls, .xlsx                                                                                                |
| Email message          | Electronic mail files whose contents comply with the requirements specified by an IETF<br>RFC for electronic mail messages, such as [RFC 2822](https://www.rfc-editor.org/rfc/rfc2822 "https://www.rfc-editor.org/rfc/rfc2822")                                                                    | .eml                                                                                                                          |
| Text                   | Non-binary text files. Examples are: comma-separated values (CSV) files, Extensible<br>Markup Language (XML) files, Hypertext Markup Language (HTML) files, JavaScript Object<br>Notation (JSON) files, JSON Lines files, plaintext documents, tab-separated values (TSV)<br>files, and YAML files | Depending on the type of non-binary text file: .csv, .htm, .html, .json, .jsonl, .tsv,<br>.txt, .xml, .yaml, .yml, and others |

Macie doesn’t analyze data in images, or audio, video, and other types of multimedia
content.

If you configure a sensitive data discovery job to analyze S3 objects that don't use a supported file or
storage format, Macie skips those objects when the job runs. Macie doesn't attempt to retrieve or
analyze data in the objects—the objects are treated as _unclassifiable objects_. An _unclassifiable object_
is an object that doesn't use a supported Amazon S3 storage class or a supported file or storage
format. Macie analyzes only those objects that use a supported storage class and a supported file
or storage format.

Similarly, if you configure Macie to perform automated sensitive data discovery, unclassifiable objects aren't
eligible for selection and analysis. Macie selects only those objects that use a supported Amazon S3
storage class and a supported file or storage format.

To identify S3 buckets that store unclassifiable objects, you can [filter your S3 bucket inventory](monitoring-s3-inventory-filter.md "monitoring-s3-inventory-filter.md"). For each bucket
in your inventory, there are fields that report the number and total storage size of
unclassifiable objects in the bucket.
