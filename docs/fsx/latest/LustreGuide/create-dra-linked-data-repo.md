# Linking your file system to an Amazon S3 bucket

You can link your Amazon FSx for Lustre file system to data repositories in Amazon S3. You can create
the link when creating the file system or at any time after the file system has been created.

A link between a directory on the file system and an S3 bucket or prefix is called a
_data repository association (DRA)_. You can configure a maximum of 8 data repository
associations on an FSx for Lustre file system. A maximum of 8 DRA requests can be queued, but only
one request can be worked on at a time for the file system. Each DRA must have a unique
FSx for Lustre file system directory and a unique S3 bucket or prefix associated with it.

###### Note

Data repository associations, automatic export, and support for multiple data repositories
aren't available on FSx for Lustre 2.10 file systems or `Scratch 1` file systems.

In order to access objects on the S3 data repository as files and directories on the file
system, file and directory metadata must be loaded into the file system. You can load metadata
from a linked data repository when you create the DRA or load metadata for batches of files
and directories that you want to access using the FSx for Lustre file system at a later time
using an import data repository task, or use automatic export to load metadata automatically
when objects are added to, changed in, or deleted from the data repository.

You can configure a DRA for automatic import only, for automatic export only, or for both.
A data repository association configured with both automatic import and automatic export propagates data in both
directions between the file system and the linked S3 bucket. As you make changes to data in
your S3 data repository, FSx for Lustre detects the changes and then automatically imports the
changes to your file system. As you create, modify, or delete files, FSx for Lustre automatically
exports the changes to Amazon S3 asynchronously once your application finishes modifying the file.

###### Important

- If you modify the same file in both the file system and the S3 bucket, you
  should ensure application-level coordination to prevent conflicts. FSx for Lustre doesn't
  prevent conflicting writes in multiple locations.
- For files marked with an immutable attribute, FSx for Lustre is unable to
  synchronize changes between your FSx for Lustre file system and an S3 bucket linked to
  the file system. Setting an immutable flag for an extended period of time can cause
  the performance of data movement between Amazon FSx and S3 to degrade.
  When you create a data repository association, you can configure the following properties:

- **File system path** – Enter a local path on the file system
  that points to a directory (such as `/ns1/`) or subdirectory (such as
  `/ns1/subdir/`) that will be mapped one-to-one with the specified data
  repository path below. The leading forward slash in the name is required. Two data
  repository associations cannot have overlapping file system paths. For example, if a data
  repository is associated with file system path `/ns1`, then you cannot link
  another data repository with file system path `/ns1/ns2`.

###### Note

If you specify only a forward slash (`/`) as the file system
path, you can link only one data repository to the file system. You can only specify
"/" as the file system path for the first data repository associated with
a file system.

- **Data repository path** – Enter a path in the S3 data
  repository. The path can be an S3 bucket or prefix in the format
  `s3://`bucket-name`/`prefix`/`.
  This property specifies where in the S3 data repository files will be imported from or
  exported to. FSx for Lustre will append a trailing "/" to your data repository path if you
  don't provide one. For example, if you provide a data repository path of
  `s3://amzn-s3-demo-bucket/my-prefix`, FSx for Lustre will interpret it as
  `s3://amzn-s3-demo-bucket/my-prefix/`.

Two data repository associations cannot have overlapping data repository paths. For
example, if a data repository with path `s3://amzn-s3-demo-bucket/my-prefix/` is
linked to the file system, then you cannot create another data repository association with data
repository path `s3://amzn-s3-demo-bucket/my-prefix/my-sub-prefix`.

- **Import metadata from repository** – You can select this
  option to import metadata from the entire data repository immediately after creating the
  data repository association. Alternatively, you can run an import data repository task to
  load all or a subset of the metadata from the linked data repository into the file system
  at any time after the data repository association is created.
- **Import settings** – Choose an import policy that specifies
  the type of updated objects (any combination of new, changed, and deleted) that will be
  automatically imported from the linked S3 bucket to your file system. Automatic import
  (new, changed, deleted) is turned on by default when you add a data repository from the
  console, but is disabled by default when using the AWS CLI or Amazon FSx API.
- **Export settings** – Choose an export policy that specifies
  the type of updated objects (any combination of new, changed, and deleted) that will be
  automatically exported to the S3 bucket. Automatic export (new, changed, deleted) is
  turned on by default when you add a data repository from the console, but is disabled by
  default when using the AWS CLI or Amazon FSx API.
  The **File system path** and **Data repository path**
  settings provide a 1:1 mapping between paths in Amazon FSx and object keys in S3.

###### Topics

- [Creating a link to an S3 bucket](create-linked-dra.md "create-linked-dra.md")
- [Updating data repository association settings](update-dra-settings.md "update-dra-settings.md")
- [Deleting an association to an S3 bucket](delete-linked-dra.md "delete-linked-dra.md")
- [Viewing data repository association details](view-dra-details.md "view-dra-details.md")
- [Data repository association lifecycle state](dra-lifecycles.md "dra-lifecycles.md")
- [Working with server-side encrypted Amazon S3
  buckets](s3-server-side-encryption-support.md "s3-server-side-encryption-support.md")
