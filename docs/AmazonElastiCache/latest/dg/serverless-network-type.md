

# Choosing a network type for serverless caches
<a name="serverless-network-type"></a>

ElastiCache serverless caches support the Internet Protocol versions 4 and 6 (IPv4 and IPv6). When creating a serverless cache, you choose one of the following network types:
+ **IPv4** – The cache accepts only IPv4 connections.
+ **IPv6** – The cache accepts only IPv6 connections.
+ **Dual stack** – The cache accepts both IPv4 and IPv6 connections.

For dual stack serverless caches, the IP protocol used for a connection depends on how your client resolves the cache endpoint's DNS hostname.

There are no additional charges for accessing ElastiCache over IPv6.

**Note**  
The network type can only be set when creating a serverless cache. You cannot change the network type after the cache is created.

## Configuring subnets for network type
<a name="serverless-network-type-subnets"></a>

When you create a serverless cache, you can provide subnet IDs. ElastiCache uses those subnets to allocate IP addresses for your cache. The subnets you provide must support the network type you choose:
+ **IPv4** – Subnets must have IPv4 address space. Dual stack subnets (with both IPv4 and IPv6) are also supported.
+ **IPv6** – Subnets must be IPv6-only. Dual stack subnets are not supported.
+ **Dual stack** – Subnets must have both IPv4 and IPv6 address space.

If you do not specify a network type, ElastiCache defaults to IPv4 unless all provided subnets are IPv6-only, in which case it defaults to IPv6. If you do not provide subnet IDs, ElastiCache selects default subnets in your VPC.

## Using the AWS Management Console
<a name="serverless-network-type-console"></a>

When creating a serverless cache using the console, choose **Customize default settings** under **Default settings**. In the **Connectivity** section, choose a **Network type**: **IPv4**, **IPv6**, or **Dual stack**. IPv4 is selected by default.

## Using the AWS CLI
<a name="serverless-network-type-cli"></a>

When creating a serverless cache using the AWS CLI, use the `--network-type` parameter with the **create-serverless-cache** command.

For Linux, macOS, or Unix:

```
aws elasticache create-serverless-cache \
  --serverless-cache-name {{<cache-name>}} \
  --engine {{<engine>}} \
  --network-type {{<network-type>}} \
  --subnet-ids {{<subnet-id-1>}} {{<subnet-id-2>}}
```

For Windows:

```
aws elasticache create-serverless-cache ^
  --serverless-cache-name {{<cache-name>}} ^
  --engine {{<engine>}} ^
  --network-type {{<network-type>}} ^
  --subnet-ids {{<subnet-id-1>}} {{<subnet-id-2>}}
```

Replace:
+ {{<cache-name>}} – A name for your serverless cache.
+ {{<engine>}} – The engine for your cache: `valkey`, `redis`, or `memcached`.
+ {{<network-type>}} – The network type: `ipv4`, `ipv6`, or `dual_stack`.
+ {{<subnet-id-1>}}, {{<subnet-id-2>}} – The IDs of the subnets for your cache. The subnets must support the chosen network type.

For more information about the **create-serverless-cache** command, see [create-serverless-cache](https://docs.aws.amazon.com/cli/latest/reference/elasticache/create-serverless-cache.html) in the AWS CLI reference.

For information about choosing a network type for node-based clusters, see [Choosing a network type in ElastiCache](network-type.md).