# Creating a vector index in a vector bucket

###### Note

Choose your vector index configuration parameters carefully. After you create a vector index, you can't update the vector index name, dimension, distance metric, or non-filterable metadata keys. To change any of these values, you must create a new vector index.

A vector index is a resource within a vector bucket that stores and organizes vector
data for efficient similarity search. When you create a vector index, you define the
characteristics that all vectors in that index must share, such as the dimension, the distance
metric used for similarity calculations, and optionally non-filterable metadata keys. You can also optionally configure dedicated encryption settings and tags for the vector index at the time of index creation. For more
information about vector index naming requirements, dimension requirements, distance metric
options, and non-filterable metadata keys, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). For more information about setting encryption configuration for vector indexes, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md"). For more information about setting tags, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md").

Vector indexes must be created within an existing vector bucket and require specific
configuration parameters that can't be modified after creation.

**To create a vector index**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. In the list of vector buckets, choose the name of the bucket where you want to
   create a vector index.
4. Choose **Create vector index**.
5. For **Vector index name**, enter a name for your
   vector index.

Vector index names must be unique within the vector bucket. Index name must be
between 3 and 63 characters. Valid characters are lowercase letters (a-z), numbers
(0-9), hyphens (-), and dots (.). For more information about the vector index naming
requirements, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). 6. For **Dimension**, enter the number of values in each
vector.

###### Note

    * The value for **Dimension** determines how many
     numerical values each vector will contain.
    * All vectors added to this index must have exactly this number of
     values.
    * Dimension must be between 1 and 4096.
    * A larger dimension requires more storage space.
    * Choose based on your embedding model's output dimensions.

For more information about the dimension requirements, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). 7. For **Distance metric**, choose one of the following
options:

    * **Cosine** – Measures the cosine of the angle
     between vectors. Best for normalized vectors and when direction matters more than
     magnitude
    * **Euclidean** – Measures the straight-line distance
     between vectors. Best when both direction and magnitude are important.

8. (Optional) Under **Non-filterable metadata**, configure
   metadata keys that will be stored but not used for filtering:

To add non-filterable metadata keys:

    1. Choose **Add key**.
    2. Enter a key name (1-63 characters and unique within this vector index).
    3. Repeat to add additional keys (maximum 10 keys).

###### Note

You can attach filterable metadata as key-value pairs to each vector when you
insert vector data after you create a vector index. By default, all metadata keys that
are attached to vectors are filterable and can be used as filters in a similarity
query. Only metadata keys that are specified as non-filterable during vector index
creation are excluded from filtering. For more information about metadata size limits
per vector, including both total and filterable metadata constraints, see [Limitations and restrictions](s3-vectors-limitations.md "s3-vectors-limitations.md"). 9. Review your configuration carefully.

###### Note

These settings can't be changed after creation. 10. Under **Encryption**, choose **Specify encryption type**. You have the option to **Use bucket settings for encryption** or override the encryption settings for the vector index. If you override the bucket-level settings, you have the option to specify encryption type for the vector index as **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** or the **Server-side encryption with Amazon S3 managed keys (SSE-S3)**. For more information about setting encryption configuration for vector indexes, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md"). 11. Under **Tags (Optional)**, you can add tags as key-value pairs to help track and organize vector index costs using AWS Billing and Cost Management. Enter a **Key** and a **Value**. To add another tag, choose **Add Tag**. You can enter up to 50 tags for a vector index. For more information, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md"). 12. Choose **Create vector index**.
To create a vector index in a vector bucket, use the following example commands and
replace the `user input placeholders` with your own information.

**Example 1: Creating a vector index with non-filterable metadata keys**

```

aws s3vectors create-index \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --index-name "`idx`" \
  --data-type "float32" \
  --dimension `1` \
  --distance-metric "`cosine`" \
  --metadata-configuration '{"nonFilterableMetadataKeys":["`nonFilterableKey1`"]}'

```

**Example 2: Creating a vector index without non-filterable metadata keys**

```

aws s3vectors create-index \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --index-name "`idx2`" \
  --data-type "float32" \
  --dimension `4096` \
  --distance-metric "`euclidean`"

```

In addition, all metadata (both filterable and non-filterable) is retrieved the same way by using the `GetVectors`, `ListVectors`, or `QueryVectors` API operations.
The following CLI command shows how to retrieve vectors with metadata (including non-filterable metadata).

Example request:

```
aws s3vectors get-vectors \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --index-name "`idx`" \
  --keys '["vec1", "vec3"]' \
  --return-data \
  --return-metadata \
```

Example response:

```
{
    "vectors": [
        {
            "key": "vec1",
            "data": {
                "float32": [
                    0.10000000149011612,
                    0.20000000298023224,
                    0.30000001192092896,
                    0.4000000059604645,
                    0.5
                ]
            },
            "metadata": {
                "category": "test",
                "text": "First vector"
            }
        },
        {
            "key": "vec3",
            "data": {
                "float32": [
                    0.6000000238418579,
                    0.699999988079071,
                    0.800000011920929,
                    0.8999999761581421,
                    1.0
                ]
            },
            "metadata": {
                "text": "Third vector",
                "category": "test"
            }
        }
    ]
}
```

The response will include all metadata associated with the vector, regardless of whether it was specified as filterable or non-filterable during index creation.

SDK for Python

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#Create a vector index "movies" in the vector bucket "media-embeddings" without non-filterable metadata keys
s3vectors.create_index(
    vectorBucketName="media-embeddings",
    indexName="movies",
    dimension=3,
    distanceMetric="cosine",
    dataType = "float32"
)


#Create a vector index "movies" in the vector bucket "media-embeddings" with non-filterable metadata keys
s3vectors.create_index(
    vectorBucketName="media-embeddings",
    indexName="movies",
    dimension=3,
    distanceMetric="cosine",
    dataType = "float32",
    metadataConfiguration= {"nonFilterableMetadataKeys": ["nonFilterableMetadataKey1"]}
)
```
