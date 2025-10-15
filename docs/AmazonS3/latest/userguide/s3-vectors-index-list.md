# Listing vector indexes

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

You can view all vector indexes within a vector bucket. The listing operation supports prefix-based filtering to help you find
 specific indexes when you have many indexes in a bucket. For more information about `ListIndexes`, prefix limits, and response limits, see [ListIndexes](../API/API_S3VectorBuckets_ListIndexes.md "../API/API_S3VectorBuckets_ListIndexes.md") in the Amazon Simple Storage Service API Reference.
 


## Prefix search capability


Prefix search allows you to list indexes that start with a specific prefix, making it easier to organize and find related vector indexes. This is particularly useful when you use naming conventions that group related indexes together:



* **By data type:** `text-embeddings-`, `image-features-`, `audio-vectors-`
* **By model:** `model1-embeddings-`, `model2-vectors-`, `custom-model-`
* **By use case:** `search-index-`, `recommendation-`, `similarity-`
* **By environment:** `prod-vectors-`, `staging-vectors-`, `dev-vectors-`

###### To list vector indexes

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Vector buckets**.
3. In the list of vector buckets, choose the name of the bucket containing the indexes you want to view.
4. The console displays a comprehensive list of all vector indexes in the bucket, including:




	* **Name** – The name for each index.
	* **Create date** – When the index was created.
	* **Amazon Resource Name (ARN)** – Full ARN for each index.
###### To filter the list

1. Enter an index name or prefix in the search box above the index list. Use prefixes to find groups of related indexes.
2. The list updates in real-time as you type.
Use the following example commands and replace the `user input placeholders` with your own information.

**To list indexes with a specific prefix in a vector bucket**

Example request:


```

aws s3vectors list-indexes \
  --vector-bucket-name "``amzn-s3-demo-bucket``" \
  --prefix "`idx`" \
  --max-results `1`
      
```
Example response:


```
{
    "nextToken": "lObb29ZkzxMGtBXs97Rkbs26xdtKemu4brsnq2jX8DCocADkILv5cRphemXS3PXXFnQBihQBmESgEeKaGA",
    "indexes": [
        {
            "vectorBucketName": "``amzn-s3-demo-bucket``",
            "indexName": "idx",
            "indexArn": "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/index/`idx`",
            "creationTime": "2025-06-12T15:50:23+00:00"
        }
    ]
}
```
**To list indexes with pagination**

Example request:


```
aws s3vectors list-indexes \
  --vector-bucket-name "``amzn-s3-demo-bucket``" \
  --prefix "`idx`" \
  --next-token "`lObb29ZkzxMGtBXs97Rkbs26xdtKemu4brsnq2jX8DCocADkILv5cRphemXS3PXXFnQBihQBmESgEeKaGA`"
```
Example response: 


```
{
    "indexes": [
        {
            "vectorBucketName": "``amzn-s3-demo-bucket``",
            "indexName": "idx2",
            "indexArn": "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/index/`idx2`",
            "creationTime": "2025-06-12T15:45:37+00:00"
        }
    ]
}
```
