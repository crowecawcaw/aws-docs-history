# Testing and using links

###### Note

Link addresses will only be visible and accessible from within your VPC.

###### To test your newly created link

1. The URL components in the example below will come from your API responses. If you don't have them at hand, your Gateway ID and Link ID can be found via the AWS Management Console, or by invoking the ListGateways and ListLinks operations outlined in [RTB Fabric API Reference](../api/welcome.md "../api/welcome.md")
2. From the command line, use `curl` to send a POST request to the Link. Supply an OpenRTB payload to validate full end-to-end requests to your partner, or an empty body to simply test connectivity. See below for a `curl` example in the us-east-1 region.

```
`curl -X POST -H "Content-Type: application/json" -d `{Your RTB JSON Payload}` \
 "https://`{your-gateway-id}`.`{your-aws-account}`.gateway.rtbfabric.`{your-region}`.amazonaws.com/link/`{your-link-id}`"`
```

Any additional URL or path params that your partner expects can be appended to the Link URI.
