# Read and write data to the cache

This section assumes that you've created an Amazon EC2 instance and can connect to it.
For instructions on how to do this,
see the [Amazon EC2 Getting Started Guide](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md").

This section also assumes that you have setup VPC access and security group settings for the EC2 instance from where you are connecting to your cache, and setup valkey-cli on your EC2 instance.
For more information on that step see [Setting up ElastiCache](set-up.md "set-up.md").

In addition to the steps below, if you have a large or global application you can greatly increase read performance by creating and reading from replicas. For more information on this more advanced step see [Best Practices for using Read Replicas](ReadReplicas.md "ReadReplicas.md").

**Find your cache endpoint**

**AWS Management Console**

To find your cache’s endpoint using the ElastiCache console:

1. Sign in to the AWS Management Console and open the Amazon ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane on the left side of the console, choose **Valkey caches**.
3. On the right side of the console, click on the name of the cache that you just created.
4. In the **Cache details**, locate and copy the cache endpoint.
   **AWS CLI**

The following AWS CLI example shows to find the endpoint for your new cache using the describe-serverless-caches command.
Once you have run the command, look for the "Endpoint" field.

**Linux**

```
aws elasticache describe-serverless-caches \
		--serverless-cache-name CacheName
```

**Windows**

```
aws elasticache describe-serverless-caches ^
		--serverless-cache-name CacheName
```

Now that you have the endpoint you need, you can log in to your EC2 instance and connect to the cache.
In the following example, you use the _valkey-cli_ utility to connect to a cluster. The following command
connects to a cache (note: replace cache-endpoint with the endpoint you retrieved in the previous step).

```
src/valkey-cli -h cache-endpoint --tls -p 6379
set a "hello"          // Set key "a" with a string value and no expiration
OK
get a                  // Get value for key "a"
"hello"
```

Now that you have the endpoint you need, you can log in to your EC2 instance and connect to the cache. In the following example,
you use the _valkey-cli_ utility to connect to a cluster. The following command connects to a cache.
Open the Command Prompt and change to the Valkey or Redis OSS directory and run the command (note: replace Cache_Endpoint with the endpoint you retrieved in the previous step).

```
c:\Valkey>valkey-cli -h Valkey_Cluster_Endpoint --tls -p 6379
set a "hello"          // Set key "a" with a string value and no expiration
OK
get a                  // Get value for key "a"
"hello"
```

You may now proceed to [(Optional) Clean up](GettingStarted.serverless-valkey.md "GettingStarted.serverless-valkey.md").
