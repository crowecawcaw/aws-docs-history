

# Export Considerations
<a name="ExportConsiderations"></a>

## Exporting to a Different Region
<a name="CrossRegionExport"></a>

 You can export domain data to an Amazon S3 bucket in a different AWS Region. No additional parameters are required beyond specifying the bucket name and ensuring your IAM permissions allow cross-Region access. Standard Amazon S3 data transfer charges apply for cross-Region exports. 

## Using Different Encryption Algorithms
<a name="EncryptionOptions"></a>

 You can specify the encryption algorithm for the exported data using the `--s3-sse-algorithm` parameter: 

 **Default encryption (AES256/SSE-S3):** 

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm AES256
```

 **SSE-KMS with AWS managed key:** 

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm 'KMS'
```

 **SSE-KMS with customer managed key:** 

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-sse-algorithm 'KMS' \
		    --s3-sse-kms-key-id 'arn:aws::kms:us-east-1:111122223333:key/1ff46940-e71b-4cba-85a8-d5cd935e2e53'
```

## Using a Custom Amazon S3 Key Prefix
<a name="CustomS3Prefix"></a>

 By default, exported data is written to the path `AWSSimpleDB/<exportId>/<domainName>/` in your Amazon S3 bucket. You can specify a custom prefix using the `--s3-key-prefix` parameter: 

```
aws simpledbv2 start-domain-export \
		    --domain-name 'myDomain' \
		    --s3-bucket 'my-export-bucket' \
		    --s3-bucket-owner '111122223333' \
		    --s3-key-prefix 'exports/simpledb'
```

 With this prefix, data is written to `exports/simpledb/AWSSimpleDB/<exportId>/<domainName>/`. 