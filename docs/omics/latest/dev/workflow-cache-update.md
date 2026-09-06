

# Updating a run cache
<a name="workflow-cache-update"></a>

You can change the cache name, description, tags, or cache behavior, but not the S3 location for the cache.

## Updating a run cache using the console
<a name="workflow-cache-update-console"></a>

From the console, follow these steps to update a run cache.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/).

1.  If required, open the left navigation pane (≡). Choose **Run caches**.

1. From the **Run caches** table, choose the run cache to update, then choose **Edit**. 

1. In the **Run cache details** panel, you can update the run cache name, description, and cache behavior fields.

1. (Optional) Associate one or more new tags with the run cache, or remove existing tags.

1. Choose **Save run cache**.

## Updating a run cache using the CLI
<a name="workflow-cache-update-api"></a>

Use the **update-run-cache** CLI command to update a run cache.

```
aws omics update-run-cache \
      --name "workflow 123 run cache" \
      --id "workflow id" \
      --description "my run cache" \
      --cache-behavior "CACHE_ALWAYS"
```

If the update is successful, you receive a response with no data fields.