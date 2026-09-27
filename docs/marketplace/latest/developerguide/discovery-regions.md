

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Supported AWS Regions for the AWS Marketplace Discovery API
<a name="discovery-regions"></a>

The AWS Marketplace Discovery API is available in the following AWS Regions:
+ US East (N. Virginia) — `us-east-1`
+ US West (Oregon) — `us-west-2`
+ Europe (Ireland) — `eu-west-1`

You can call the Discovery API in a specific Region with the following endpoint format:

```
discovery-marketplace.{{region}}.api.aws
```

You can also call the Discovery API by using the global endpoint. The global endpoint routes each request to the nearest available AWS Region where the Discovery API is deployed, based on latency and availability health checks. Requests to the global endpoint must be signed with AWS Signature Version 4A (SigV4a), and pagination tokens aren't portable across Regions. For more information about signing and pagination with the global endpoint, see [Global endpoint](discovery-apis.md#discovery-global-endpoint).

```
discovery-marketplace.global.api.aws
```