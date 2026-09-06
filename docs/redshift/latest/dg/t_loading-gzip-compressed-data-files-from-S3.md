

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Loading compressed data files from Amazon S3
<a name="t_loading-gzip-compressed-data-files-from-S3"></a>

To load data files that are compressed using gzip, lzop, or bzip2, include the corresponding option: GZIP, LZOP, or BZIP2.

For example, the following command loads from files that were compressing using lzop.

```
COPY customer FROM 's3://amzn-s3-demo-bucket/customer.lzo' 
IAM_ROLE 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
DELIMITER '|' LZOP;
```

**Note**  
If you compress a data file with lzop compression and use the *--filter* option, the COPY command doesn't support it.