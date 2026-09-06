

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# File compression parameters
<a name="copy-parameters-file-compression"></a>

You can load from compressed data files by specifying the following parameters. File compression parameters

BZIP2   <a name="copy-bzip2"></a>
A value that specifies that the input file or files are in compressed bzip2 format (.bz2 files). The COPY operation reads each compressed file and uncompresses the data as it loads.

GZIP   <a name="copy-gzip"></a>
A value that specifies that the input file or files are in compressed gzip format (.gz files). The COPY operation reads each compressed file and uncompresses the data as it loads.

LZOP   <a name="copy-lzop"></a>
A value that specifies that the input file or files are in compressed lzop format (.lzo files). The COPY operation reads each compressed file and uncompresses the data as it loads.  
COPY doesn't support files that are compressed using the lzop *--filter* option.

ZSTD   <a name="copy-zstd"></a>
A value that specifies that the input file or files are in compressed Zstandard format (.zst files). The COPY operation reads each compressed file and uncompresses the data as it loads.  
ZSTD is supported only with COPY from Amazon S3.