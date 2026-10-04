

# Changing a vector index's mode
<a name="s3-vectors-index-mode"></a>

A vector index whose index mode is `ENHANCED` applies your metadata filter before the vector search, ensuring high recall even when filters match a small fraction of vectors, and it supports the `$startsWith` filter operator. Indexes in vector buckets created before September 30, 2026 use `CLASSIC` by default, including indexes you create in those buckets later. We recommend moving these indexes to `ENHANCED`.

Changing an index to `ENHANCED` takes effect in place, with no re-ingestion, no changes to your queries or your application, and no additional charge. To change an index's mode, call [UpdateIndexMode](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UpdateIndexMode.html). To see an index's current mode, call [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html) or view the index's detail page in the Amazon S3 console.

**To change an index's mode (console)**

1. Sign in to the console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation pane, choose **Vector buckets**.

1. Choose the vector bucket that contains the index, then choose the index.

1. Choose **Enable enhanced index mode**.

1. Review the information in the confirmation dialog, select the acknowledgement, and then choose **Enable**.

```
aws s3vectors update-index-mode --vector-bucket-name "amzn-s3-demo-vector-bucket" --index-name "idx" --index-mode "ENHANCED"
```

Before you change an index, confirm that your queries use 100 or fewer filter constraints. On an `ENHANCED` index, a query that exceeds the limit returns a validation error. For how constraints are counted, and for how to consolidate or split a query that exceeds the limit, see [Filter constraints per query](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-constraints). For how a filter affects query latency, see [Query performance with filters](s3-vectors-metadata-filtering.md#s3-vectors-metadata-filtering-performance).

**Topics**
+ [Test an index before you change it](#s3-vectors-index-mode-test)
+ [Set the index mode for new indexes in a vector bucket](#s3-vectors-index-mode-bucket-default)
+ [Turn off the enhanced index mode](#s3-vectors-index-mode-turn-off)

## Test an index before you change it
<a name="s3-vectors-index-mode-test"></a>

On a `CLASSIC` index, you can set the `queryMode` parameter to `ENHANCED` on a [QueryVectors](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_QueryVectors.html) request to run that query with pre-filtering while the index stays as it is. You can also set `queryMode` to `ENHANCED` on an index whose index mode is already `ENHANCED`, where it has no additional effect.

If a query uses `$startsWith` under `queryMode=ENHANCED` and you later remove `queryMode`, the request returns a validation error, because `$startsWith` requires `ENHANCED` query behavior. Update the index mode to use `$startsWith` without setting `queryMode` on every request.

## Set the index mode for new indexes in a vector bucket
<a name="s3-vectors-index-mode-bucket-default"></a>

Each vector bucket has a default index mode, inherited by new vector indexes. Setting the default applies to indexes you create afterward, and does not change any index that already exists in the bucket. To read a bucket's default, call [GetVectorBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetVectorBucket.html), or view the bucket's **Properties** tab in the Amazon S3 console.

To move a vector bucket and its indexes to `ENHANCED`, complete the following steps.

1. Set the bucket's default index mode to `ENHANCED` with [PutVectorBucketDefaultIndexMode](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_PutVectorBucketDefaultIndexMode.html), so that vector indexes you create afterward use `ENHANCED`.

1. List the vector indexes in the bucket with [ListIndexes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_ListIndexes.html), and call [GetIndex](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetIndex.html) on each one to find those whose index mode is `CLASSIC`.

1. Call [UpdateIndexMode](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UpdateIndexMode.html) with `indexMode` set to `ENHANCED` on each of those indexes.

```
aws s3vectors put-vector-bucket-default-index-mode --vector-bucket-name "amzn-s3-demo-vector-bucket" --default-index-mode "ENHANCED"
```

## Turn off the enhanced index mode
<a name="s3-vectors-index-mode-turn-off"></a>

Changing an index to `ENHANCED` is reversible if your vector bucket was created before September 30, 2026. You can change the index back to `CLASSIC` with the AWS CLI, the AWS SDKs, or the Amazon S3 REST API. You cannot do this from the Amazon S3 console.

```
aws s3vectors update-index-mode --vector-bucket-name "amzn-s3-demo-vector-bucket" --index-name "idx" --index-mode "CLASSIC"
```

On a `CLASSIC` index, a query with a selective filter can return fewer than top K results, and `$startsWith` is available only when the request sets `queryMode` to `ENHANCED`. For which indexes accept `CLASSIC`, see [UpdateIndexMode](https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_UpdateIndexMode.html) in the *Amazon S3 API Reference*.