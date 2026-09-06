

# Deleting a run cache
<a name="workflow-cache-delete"></a>

You can delete a run cache if no active runs are using it. If any runs are using the run cache, wait for the runs to complete or you can cancel the runs.

Deleting a run cache removes the resource and its metadata, but doesn't delete the data in Amazon S3. After you delete the cache, you can't reattach it or use it for subsequent runs.

The cached data remains in Amazon S3 for your inspection. You can remove old cache data using standard S3 **Delete** operations. Alternatively, create an Amazon S3 lifecycle policy to expire cached data that you no longer use.

## Deleting a run cache using the console
<a name="workflow-cache-delete-console"></a>

From the console, follow these steps to delete a run cache.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/).

1.  If required, open the left navigation pane (≡). Choose **Run caches**.

1. From the **Run caches** table, choose the run cache to delete.

1. From the **Run caches** table menu, choose **Delete**.

1. From the modal dialog, save the Amazon S3 cache data link for future reference, then confirm that you want to delete the run cache.

    You can use the Amazon S3 link to inspect the cached data, but you can't relink the data to another run cache. Delete the cache data when you've finished the inspection.

## Deleting a run cache using the CLI
<a name="workflow-cache-delete-api"></a>

Use the **delete-run-cache** CLI command to delete a run cache. 

```
aws omics delete-run-cache \
      --id "my cache id"
```

If the delete is successful, you receive a response with no data fields.