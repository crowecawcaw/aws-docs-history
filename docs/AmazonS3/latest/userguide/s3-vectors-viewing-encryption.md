

# Viewing encryption configuration in S3 Vectors
<a name="s3-vectors-viewing-encryption"></a>

After creating your vector bucket, you can verify the encryption configuration using the console. Alternatively, you can use the GetVectorBucket and GetIndex API operations through the AWS REST API, AWS CLI, or AWS SDKs.

## Using the AWS CLI
<a name="s3-vectors-viewing-encryption-cli"></a>

Use the `get-vector-bucket` command to retrieve detailed bucket information, including encryption configuration. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3vectors get-vector-bucket \
  --vector-bucket-name {{amzn-s3-demo-vector-bucket}}
```

Use the `get-index` command to retrieve detailed vector index information, including encryption configuration. To use this example, replace the {{user input placeholders}} with your own information.

```
aws s3vectors get-index \
  --vector-bucket-name {{amzn-s3-demo-vector-bucket}}
  --index-name {{amzn-s3-demo-vector-index}}
```