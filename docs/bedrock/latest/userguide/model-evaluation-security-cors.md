# Required Cross Origin Resource Sharing

(CORS) permissions on S3 buckets

###### Cross Origin Resource Sharing (CORS) permission requirements

All console-based model evaluation jobs require Cross Origin Resource Sharing (CORS)
permissions to be enabled on any Amazon S3 buckets specified in the model evaluation job. To
learn more, see Required Cross Origin Resource Sharing
(CORS) permissions on S3 buckets

When you create a model evaluation job that uses the Amazon Bedrock console, you must specify a CORS
configuration on the S3 bucket.

A CORS configuration is a document that defines rules that identify the origins that you
will allow to access your bucket, the operations (HTTP methods) supported for each origin,
and other operation-specific information. To learn more about setting the required CORS
configuration using the S3 console, see [Configuring cross-origin
resource sharing (CORS)](../../../AmazonS3/latest/userguide/enabling-cors-examples.md "../../../AmazonS3/latest/userguide/enabling-cors-examples.md") in the _Amazon S3 User Guide_.

The following is the minimal required CORS configuration for S3 buckets.

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "PUT",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin"
        ]
    }
]
```
