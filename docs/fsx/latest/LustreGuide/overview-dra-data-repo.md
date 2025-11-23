# Overview of data repositories

When you use Amazon FSx for Lustre with data repositories, you can ingest and process
large volumes of file data in a high-performance file system by using automatic import and
import data repository tasks. At the same time, you can write results to your data
repositories by using automatic export or export data repository tasks. With these features,
you can restart your workload at any time using the latest data stored in your data
repository.

###### Note

Data repository associations, automatic export, and support for multiple data repositories
aren't available on FSx for Lustre 2.10 file systems or `Scratch 1` file systems.

FSx for Lustre is deeply integrated with Amazon S3. This integration means that you can seamlessly
access the objects stored in your Amazon S3 buckets from applications that mount your FSx for Lustre file
system. You can also run your compute-intensive workloads on Amazon EC2 instances in the
AWS Cloud and export the results to your data repository after your workload is
complete.

In order to access objects in the Amazon S3 data repository as files and directories on the
file system, file and directory metadata must be loaded into the file system. You can load
metadata from a linked data repository when you create a data repository association.

Additionally you can import file and directory metadata from your linked data
repositories to the file system using automatic import or using an import data repository
task. When you turn on automatic import for a data repository association, your file system
automatically imports file metadata as files are created, modified, and/or deleted in the S3 data
repository. Alternatively, you can import metadata for new or changed files and directories
using an import data repository task.

###### Note

Automatic import and import data repository tasks can be used simultaneously on a file
system.

You can also export files and their associated metadata in your file system to your
data repository using automatic export or using an export data repository task. When
you turn on automatic export on a data repository association, your file system automatically
exports file data and metadata as files are created, modified, or deleted. Alternatively, you
can export files or directories using an export data repository task. When you use an export
data repository task, file data and metadata that were created or modified since the last such
task are exported.

###### Note

- Automatic export and export data repository tasks can't be used simultaneously
  on a file system.
- Data repository associations only export regular files, symlinks and directories.
  This means all the other type of files (FIFO special, block special, character special, and socket)
  won't be exported as part of the export processes like automatic export and export data repository
  tasks.
  FSx for Lustre also supports cloud bursting workloads with on-premises file systems by enabling
  you to copy data from on-premises clients using Direct Connect or VPN.

###### Important

If you have linked one or more FSx for Lustre file systems to a data repository on Amazon S3,
don't delete the Amazon S3 bucket until you have deleted or unlinked all linked file systems.

## Region and account support for linked S3

buckets

When you create links to S3 buckets, keep in mind the following Region and account
support limitations:

- Automatic export supports cross-Region configurations. The Amazon FSx file system and the
  linked S3 bucket can be located in the same AWS Region or in different
  AWS Regions.
- Automatic import doesn't support cross-Region configurations. Both
  the Amazon FSx file system and the linked S3 bucket must be located in the
  same AWS Region.
- Both automatic export and automatic import support cross-Account configurations. The
  Amazon FSx file system and the linked S3 bucket can belong to the same AWS account or to
  different AWS accounts.
