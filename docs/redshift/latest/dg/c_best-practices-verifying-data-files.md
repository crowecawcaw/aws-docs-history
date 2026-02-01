Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Verify data files before and

after a load

Before you load data from Amazon S3, first verify that your Amazon S3 bucket contains all the correct files,
and only those files. For more
information, see [Verifying that the
correct files are present in your bucket](verifying-that-correct-files-are-present.md "verifying-that-correct-files-are-present.md").

After the load operation is complete, query the [STL_LOAD_COMMITS](r_STL_LOAD_COMMITS.md "r_STL_LOAD_COMMITS.md") system table to verify that the expected files
were loaded. For more information, see [Verifying that the data loaded
correctly](verifying-that-data-loaded-correctly.md "verifying-that-data-loaded-correctly.md").
