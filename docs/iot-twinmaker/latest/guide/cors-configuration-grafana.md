# CORS configuration for Grafana scene viewer

The AWS IoT TwinMaker Grafana plugin requires a CORS (cross-origin resource sharing) configuration, which
allows the Grafana user interface to load resources from the Amazon S3 bucket.
Without the CORS configuration, you will receive an error message as
"Load 3D Scene failed with Network Failure"
on the Scene viewer since the Grafana domain can't access the resources in the Amazon S3 bucket.

To configure your Amazon S3 bucket with CORS, use the following steps:

1. Sign in to the IAM console and open the [Amazon S3 console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the name of the bucket that you use as your AWS IoT TwinMaker workspace's resource bucket.
3. Choose **Permissions**.
4. In the **Cross-origin resource sharing** section, select **Edit**,
   to open the CORS editor.
5. In the **CORS configuration editor** text box, type or copy and paste the following
   JSON CORS configuration by replacing the Grafana workspace domain `GRAFANA-WORKSPACE-DOMAIN`
   with your domain.

###### Note

You need to keep the asterisk `*` character at the beginning of the
`"AllowedOrigins":` JSON element.

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
            "DELETE",
            "HEAD"
        ],
        "AllowedOrigins": [
            "*`GRAFANA-WORKSPACE-DOMAIN`"
        ],
        "ExposeHeaders": [
            "ETag"
        ]
    }
]

```

6. Select **Save changes** to finish the CORS configuration.
   For more information on CORS with Amazon S3 buckets, see
   [Using cross-origin resource sharing (CORS)](../../../AmazonS3/latest/userguide/cors.md "../../../AmazonS3/latest/userguide/cors.md").
