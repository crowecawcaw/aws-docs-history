# Create a Valkey serverless cache

In this step, you create a new cache in Amazon ElastiCache.

**AWS Management Console**

To create a new cache using the ElastiCache console:

1. Sign in to the AWS Management Console and open the [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane on the left side of the console, choose **Valkey caches**.
3. On the right side of the console, choose **Create Valkey cache**
4. In the **Cache settings** enter a **Name**.
   You can optionally enter a **description** for the cache.
5. Leave the default settings selected.
6. Click **Create** to create the cache.
7. Once the cache is in "ACTIVE" status, you can begin writing and reading data to the cache. .
   **AWS CLI**

The following AWS CLI example creates a new cache using create-serverless-cache.

**Linux**

```
aws elasticache create-serverless-cache \
    --serverless-cache-name CacheName \
    --engine valkey
```

**Windows**

```
aws elasticache create-serverless-cache ^
    --serverless-cache-name CacheName ^
    --engine valkey
```

Note that the value of the Status field is set to `CREATING`.

To verify that ElastiCache has finished creating the cache, use the `describe-serverless-caches` command.

**Linux**

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

**Windows**

```
aws elasticache describe-serverless-caches --serverless-cache-name CacheName
```

After creating the new cache, proceed to
[Read and write data to the cache](GettingStarted.serverless-valkey.md "GettingStarted.serverless-valkey.md").
