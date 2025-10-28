Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# File compression

parameters

You can load from compressed data files by specifying the following parameters.

###### File compression parameters

BZIP2

A value that specifies that the input file or files are in compressed
bzip2 format (.bz2 files). The COPY operation reads each compressed file and
uncompresses the data as it loads.

GZIP

A value that specifies that the input file or files are in compressed
gzip format (.gz files). The COPY operation reads each compressed file and
uncompresses the data as it loads.

LZOP

A value that specifies that the input file or files are in compressed
lzop format (.lzo files). The COPY operation reads each compressed file and
uncompresses the data as it loads.

###### Note

COPY doesn't support files that are compressed using the lzop
_--filter_ option.

ZSTD

A value that specifies that the input file or files are in compressed
Zstandard format (.zst files). The COPY operation reads each compressed file and
uncompresses the data as it loads.

###### Note

ZSTD is supported only with COPY from Amazon S3.
