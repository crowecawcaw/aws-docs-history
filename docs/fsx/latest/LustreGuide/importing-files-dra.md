# Importing changes from your data repository

You can import changes to data and POSIX metadata from a linked data repository to your Amazon FSx
file system. Associated POSIX metadata includes ownership, permissions, and timestamps.

To import changes to the file system, use one of the following methods:

- Configure your file system to automatically import new, changed, or deleted files
  from your linked data repository. For more information, see [Automatically import updates from your S3
  bucket](autoimport-data-repo-dra.md "autoimport-data-repo-dra.md").
- Select the option to import metadata when you create a data repository association.
  This will initiate an import data repository task immediately after creating the data repository
  association.
- Use an on-demand import data repository task. For more information, see
  [Using data repository tasks to import changes](import-data-repo-task-dra.md "import-data-repo-task-dra.md").
  Automatic import and import data repository tasks can run at the same time.

When you turn on automatic import for a data repository association, your file system
automatically updates file metadata as objects are created, modified, or deleted in S3.
When you select the option to import metadata while creating a data repository association,
your file system imports metadata for all objects in the data repository. When you import
using an import data repository task, your file system imports only metadata for objects
that were created or modified since the last import.

FSx for Lustre automatically copies the content of a file from your data repository and loads
it into the ﬁle system when your application first accesses the file in the file system.
This data movement is managed by FSx for Lustre and is transparent to your applications.
Subsequent reads of these files are served directly from the file system with
sub-millisecond latencies.

You can also preload your whole ﬁle system or a directory within your ﬁle system.
For more information, see
[Preloading files into your file
system](preload-file-contents-hsm-dra.md "preload-file-contents-hsm-dra.md").
If you request the preloading of multiple ﬁles simultaneously, FSx for Lustre loads ﬁles
from your Amazon S3 data repository in parallel.

FSx for Lustre only imports S3 objects that have POSIX-compliant object keys. Both
automatic import and import data repository tasks import POSIX metadata. For more information, see
[POSIX metadata support for data
repositories](posix-metadata-support.md "posix-metadata-support.md").

###### Note

FSx for Lustre doesn't support importing metadata for symbolic links (symlinks) from
S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes. Metadata for
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive objects that aren't symlinks
can be imported (that is, an inode is created on the FSx for Lustre file system with the correct
metadata). However, to read this data from the file system, you must first restore the
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive object. Importing
file data directly from Amazon S3 objects in the S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive storage class into FSx for Lustre isn't supported.
