# Creating a dataset using Amazon S3 files

To create a dataset using one or more text files (.csv, .tsv, .clf, or .elf) from
Amazon S3, create a manifest for Quick Sight. Quick Sight uses this manifest to identify
the files that you want to use and to the upload settings needed to import them. When
you create a dataset using Amazon S3, the file data is automatically imported into [SPICE](spice.md "spice.md").

You must grant Quick Sight access to any Amazon S3 buckets that you want to read files
from. For information about granting Quick Sight access to AWS resources, see [Configuring Amazon Quick Sight access to AWS data
sources](access-to-aws-resources.md "access-to-aws-resources.md").

###### Topics

- [Supported formats for Amazon S3 manifest
  files](supported-manifest-file-format.md "supported-manifest-file-format.md")
- [Creating Amazon S3 datasets](create-a-data-set-s3-procedure.md "create-a-data-set-s3-procedure.md")
- [Datasets using S3 files in
  another AWS account](using-s3-files-in-another-aws-account.md "using-s3-files-in-another-aws-account.md")
