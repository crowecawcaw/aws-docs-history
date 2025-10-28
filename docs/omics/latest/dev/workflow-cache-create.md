AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating a run cache

When you create a run cache, you specify an Amazon S3 location for the cache data. This data must be immediately
accessible. Call caching doesn't retrieve objects archived in Glacier (such as GFR and GDA storage
classes).

If the Amazon S3 bucket for the cache data is owned by another AWS account, provide that account ID when you
create the run cache.

## Creating a run cache using the console

From the console, follow these steps to create a run cache.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Run caches**.
3. From the **Run caches** page, choose **Create run cache**.
4. In the **Run cache details** panel of the **Create run cache**
   page, configure these fields:
   1. Enter a name for the run cache.
   2. (Optional) Enter a description.
   3. Enter an S3 location for the cached output. Choose a bucket in the same Region as your workflow.
   4. (Optional) Enter the AWS account of the bucket owner to verify bucket ownership.
      If you don't enter a value, the default value is your account ID.
   5. Under **Cache behavior**, configure the default behavior (whether to cache outputs for failed
      runs or for all runs). When you start a run, you can optionally override the default behavior.

5. (Optional) Associate one or more tags with the run cache.
6. Choose **Create run cache**. The console displays the new run cache in the
   **Run caches** table.

## Creating a run cache using the CLI

Use the **create-run-cache** CLI command to create a run cache. The default
cache behavior is `CACHE_ON_FAILURE`.

```
aws omics create-run-cache \
      --name "workflow 123 run cache" \
      --description "my run cache" \
      --cache-s3-location "s3://amzn-s3-demo-bucket" \
      --cache-behavior "CACHE_ALWAYS"                \
      --cache-bucket-owner-id  "111122223333"

```

If the create is successful, you receive a response with the following fields.

```
{
  "arn": "string",
  "id": "string",
  "status": "ACTIVE"
  "tags": {}
  }
```
