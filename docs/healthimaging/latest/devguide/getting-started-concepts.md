# AWS HealthImaging concepts

The following terminology and concepts are central to your understanding and use of
AWS HealthImaging.

###### Concepts

- [Data store](#concept-data-store "#concept-data-store")
- [Image set](#concept-image-set "#concept-image-set")
- [Metadata](#concept-metadata "#concept-metadata")
- [Image frame](#concept-image-frame "#concept-image-frame")

## Data store

A data store is a repository of medical imaging data that resides within a single
AWS Region. An AWS account can have zero or many data stores. A data store has its own AWS KMS
encryption key, so data in one data store can be physically and logically isolated from data in
other data stores. Data stores support access control using IAM roles, permissions, and
attribute-based access control.

For more information, see [Managing data stores](managing-data-stores.md "managing-data-stores.md") and [Cost Optimization](cost-optimization.md "cost-optimization.md").

## Image set

An image set is an AWS concept that defines an abstract grouping mechanism for optimizing
related medical imaging data. When you import your DICOM P10 imaging data into an AWS HealthImaging data
store, it is transformed into image sets comprised of [metadata](#concept-metadata "#concept-metadata") and [image frames](#concept-image-frame "#concept-image-frame") (pixel data). HealthImaging
attempts to organize imported data according to the DICOM hierarchy of Study, Series, and Instance.
DICOM instances that are successfully added to the HealthImaging managed hierarchy are denoted as
primary image sets. Importing DICOM P10 data will either: create a new primary image set; merge
instances into an existing primary image set if the instances already exist in the primary collection;
or, in the case of metadata element conflicts, create a new non-primary image set.

For more information, see [Importing imaging data](importing-imaging-data.md "importing-imaging-data.md") and [Understanding image sets](understanding-image-sets.md "understanding-image-sets.md").

## Metadata

Metadata is the non-pixel attributes that exist within an [image set](#concept-image-set "#concept-image-set"). For DICOM, this includes patient demographics, procedure details, and other
acquisition-specific parameters. AWS HealthImaging separates the image set into metadata and image frames
(pixel data) so applications can access it quickly. This is helpful for image viewers, analytics,
and AI/ML use cases that don't require pixel data. DICOM data [normalizes](metadata-normalization.md "metadata-normalization.md") at the Patient, Study, and Series levels,
eliminating inconsistencies. This simplifies use of the data, increases safety, and improves
access performance.

For more information, see [Getting image set metadata](get-image-set-metadata.md "get-image-set-metadata.md") and [Metadata normalization](metadata-normalization.md "metadata-normalization.md").

## Image frame

An image frame is the pixel data that exists within an [image set](#concept-image-set "#concept-image-set") to make up a 2D medical image. Some files retain their original transfer
syntax encoding during import, while others are transcoded to High-Throughput JPEG 2000 (HTJ2K)
lossless by default. If an image frame is encoded in HTJ2K, it must be decoded prior to viewing
in an image viewer. For more information, see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md"), [Getting image set pixel data](get-image-frame.md "get-image-frame.md"), and [HTJ2K decoding libraries](reference-htj2k.md "reference-htj2k.md").
