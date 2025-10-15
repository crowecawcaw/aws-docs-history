# Viewing encryption configuration in S3 Vectors

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

After creating your vector bucket, you can verify the encryption configuration using either the console or CLI.

Use the `get-vector-bucket` command to retrieve detailed bucket information, including encryption configuration. To use this example, replace the `user input placeholders` with your own information.


```
aws s3vectors get-vector-bucket \
  --vector-bucket-name `amzn-s3-demo-vector-bucket`
```
