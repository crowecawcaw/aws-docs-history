# (Optional) Clean up

If you no longer need the Amazon ElastiCache cache that you created, you can delete it.
This step helps ensure that you are not charged for resources that you are not using.
You can use the ElastiCache console, the AWS CLI, or the ElastiCache API to delete your cache.

**AWS Management Console**

To delete your cache using the console:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane on the left side of the console, choose **Valkey or Redis OSS Caches**.
3. Choose the radio button next to the cache you want to delete.
4. Select **Actions** on the top right, and select **Delete**.
5. You can optionally choose to take a final snapshot before you delete your cache.
6. In the **Delete** confirmation screen, re-enter the cache name and choose
   **Delete** to delete the cluster, or choose **Cancel** to keep the cluster.
   As soon as your cache moves in to the **DELETING** status, you stop incurring charges for it.

**AWS CLI**

The following AWS CLI example deletes a cache using the delete-serverless-cache command.

**Linux**

```
aws elasticache delete-serverless-cache \
		--serverless-cache-name CacheName
```

**Windows**

```
aws elasticache delete-serverless-cache ^
		--serverless-cache-name CacheName
```

Note that the value of the **Status** field is set to **DELETING**.

You may now proceed to [Next Steps](GettingStarted.serverless-redis.md "GettingStarted.serverless-redis.md").
