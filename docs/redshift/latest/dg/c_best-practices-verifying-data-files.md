

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Verify data files before and after a load
<a name="c_best-practices-verifying-data-files"></a>

Before you load data from Amazon S3, first verify that your Amazon S3 bucket contains all the correct files, and only those files. For more information, see [Verifying that the correct files are present in your bucket](verifying-that-correct-files-are-present.md). 

After the load operation is complete, query the [STL\_LOAD\_COMMITS](r_STL_LOAD_COMMITS.md) system table to verify that the expected files were loaded. For more information, see [Verifying that the data loaded correctly](verifying-that-data-loaded-correctly.md). 