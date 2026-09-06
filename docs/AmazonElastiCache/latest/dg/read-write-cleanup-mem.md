

# (Optional) Clean up
<a name="read-write-cleanup-mem"></a>

**Using the AWS Management Console**

The following procedure deletes a single cache from your deployment. To delete multiple caches, repeat the procedure for each cache that you want to delete. You do not need to wait for one cache to finish deleting before starting the procedure to delete another cache.

**To delete a cache**

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. In the ElastiCache console dashboard, choose the engine that is running on the cache that you want to delete. A list of all caches running that engine appears.

1. To choose the cache to delete, choose the cache's name from the list of caches.
**Important**  
 You can only delete one cache at a time from the ElastiCache console. Choosing multiple caches disables the delete operation.

1. For **Actions**, choose **Delete**.

1. In the **Delete Cache** confirmation screen, choose **Delete** to delete the cache, or choose **Cancel** to keep the cluster.

1. If you chose **Delete**, the status of the cache changes to *deleting*.

As soon as your cache moves in to the **DELETING** status, you stop incurring charges for it.

**Using the AWS CLI**

The following code deletes the cache my-cache.

```
aws elasticache delete-serverless-cache --serverless-cache-name my-cache
```

The delete-serverless-cache CLI action only deletes one serverless cache. To delete multiple caches, call delete-serverless-cache for each serverless cache that you want to delete. You do not need to wait for one serverless cache to finish deleting before deleting another.

**For Linux, macOS, or Unix:**

```
aws elasticache delete-serverless-cache \
		--serverless-cache-name my-cache
```

**For Windows:**

```
aws elasticache delete-serverless-cache ^
		--serverless-cache-name my-cache
```

For more information, see the AWS CLI for ElastiCache topic delete-serverless-cache.

You may now proceed to [Next Steps](next-steps-mem.md).