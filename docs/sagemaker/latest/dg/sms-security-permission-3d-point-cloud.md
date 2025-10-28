# 3D point cloud labeling job

permission requirements

When you create a 3D point cloud labeling job, in addition to the permission requirements
found in [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md"),
you must add a CORS policy to your S3 bucket that contains your input manifest file.

## Add a CORS permission policy to S3

bucket

When you create a 3D point cloud labeling job, you specify buckets in S3 where your
input data and manifest file are located and where your output data will be stored.
These buckets may be the same. You must attach the following Cross-origin resource
sharing (CORS) policy to your input and output buckets. If you use the Amazon S3 console to
add the policy to your bucket, you must use the JSON format.

**JSON**

```
[
        {
            "AllowedHeaders": [
                "*"
            ],
            "AllowedMethods": [
                "GET",
                "HEAD",
                "PUT"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": [
                "Access-Control-Allow-Origin"
            ],
            "MaxAgeSeconds": 3000
        }
    ]
```

**XML**

```
<?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <ExposeHeader>Access-Control-Allow-Origin</ExposeHeader>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
```

To learn how to add a CORS policy to an S3 bucket, see [How do I add cross-domain
resource sharing with CORS?](../../../AmazonS3/latest/user-guide/add-cors-configuration.md "../../../AmazonS3/latest/user-guide/add-cors-configuration.md") in the Amazon Simple Storage Service User Guide.
