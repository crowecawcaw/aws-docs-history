AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Updating a run cache

You can change the cache name, description, tags, or cache behavior, but not the S3 location for the
cache.

## Updating a run cache using the console

From the console, follow these steps to update a run cache.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Run caches**.
3. From the **Run caches** table, choose the run cache to update, then choose
   **Edit**.
4. In the **Run cache details** panel, you can update the run cache name,
   description, and cache behavior fields.
5. (Optional) Associate one or more new tags with the run cache, or remove existing tags.
6. Choose **Save run cache**.

## Updating a run cache using the CLI

Use the **update-run-cache** CLI command to update a run cache.

```
aws omics update-run-cache \
      --name "workflow 123 run cache" \
      --id "workflow id" \
      --description "my run cache" \
      --cache-behavior "CACHE_ALWAYS"
```

If the update is successful, you receive a response with no data fields.
