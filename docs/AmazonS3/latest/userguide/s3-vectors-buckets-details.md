# Viewing vector bucket attributes

You can view detailed information about a vector bucket, including its properties, encryption settings and creation details using
the Amazon S3 REST API, AWS SDKs, S3 Console, or the AWS Command Line Interface (AWS CLI). For more information about `GetVectorBucket`, see [GetVectorBucket](../API/API_S3VectorBuckets_GetVectorBucket.md "../API/API_S3VectorBuckets_GetVectorBucket.md") in the _Amazon S3 API Reference_.

1. Sign in to the console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. The console displays a list of all your vector buckets. Find a bucket based on the start of the bucket name, enter a vector bucket name or prefix in the search box above the bucket list. Once you locate your vector bucket, you can view detailed information about it, including its encryption settings, tags, and creation details in the **Properties** tab.

```
aws s3vectors get-vector-bucket --vector-bucket-name `"amzn-s3-demo-vector-bucket"`
```
