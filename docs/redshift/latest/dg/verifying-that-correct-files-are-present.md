

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Verifying that the correct files are present in your bucket
<a name="verifying-that-correct-files-are-present"></a>

After you upload your files to your Amazon S3 bucket, we recommend listing the contents of the bucket to verify that all of the correct files are present and that no unwanted files are present. For example, if the bucket `amzn-s3-demo-bucket` holds a file named `venue.txt.back`, that file will be loaded, perhaps unintentionally, by the following command:

```
COPY venue FROM 's3://amzn-s3-demo-bucket/venue' … ;
```

If you want to control specifically which files are loaded, you can use a manifest file to explicitly list the data files. For more information about using a manifest file, see the [copy_from_s3_manifest_file](copy-parameters-data-source-s3.md#copy-manifest-file) option for the COPY command and [Using a manifest to specify data files](r_COPY_command_examples.md#copy-command-examples-manifest) in the COPY examples. 

For more information about listing the contents of the bucket, see [Listing Object Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ListingKeysUsingAPIs.html) in the *Amazon S3 Developer Guide*.