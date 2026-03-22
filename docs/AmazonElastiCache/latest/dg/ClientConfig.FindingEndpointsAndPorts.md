# Finding node endpoints and port numbers

To connect to a cache node, your application needs to know the endpoint and port
number for that node.

## Finding node endpoints and port numbers (Console)

**To determine node endpoints and port numbers**

1. Sign in to the [Amazon ElastiCache management console](https://aws.amazon.com/elasticache "https://aws.amazon.com/elasticache") and
   choose the engine running on your cluster.

A list of all clusters running the chosen engine appears. 2. Continue below for the engine and configuration you're running. 3. Choose the name of the cluster of interest. 4. Locate the **Port** and **Endpoint** columns
for the node you're interested in.

## Finding cache node endpoints and port numbers (AWS CLI)

To determine cache node endpoints and port numbers,
use the command `describe-cache-clusters` with the
`--show-cache-node-info` parameter.

```
aws elasticache describe-cache-clusters --show-cache-node-info
```

The fully qualified DNS names and port numbers are in the Endpoint section of the output.

## Finding cache node endpoints and port numbers (ElastiCache API)

To determine cache node endpoints and port numbers,
use the action `DescribeCacheClusters` with the
`ShowCacheNodeInfo=true` parameter.

###### Example

```

https://elasticache.us-west-2.amazonaws.com /
    ?Action=DescribeCacheClusters
    &ShowCacheNodeInfo=true
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20140421T220302Z
    &Version=2014-09-30
    &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
    &X-Amz-Credential=<credential>
    &X-Amz-Date=20140421T220302Z
    &X-Amz-Expires=20140421T220302Z
    &X-Amz-Signature=<signature>
    &X-Amz-SignedHeaders=Host
```
