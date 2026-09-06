

# Creating inbound external links
<a name="creating-inbound-external-links"></a>

**Important**  
The `CreateInboundExternalLink` API operation is deprecated on regular responder gateway. This API can only be used on an external responder gateway instead. Existing inbound external links created with `CreateInboundExternalLink` continue to function. For new configurations, use `CreateInboundExternalLink` on an external responder gateway. For more information about creating an external responder gateway, see [Creating a responder gateway](working-with-responder-gateways.md#creating-responder-gateway).

Inbound external links enable external partners (such as SSPs) to send traffic to your responder gateway over the public internet, extending your RTB infrastructure beyond private VPC connections. Traffic is routed over the AWS Global Network where possible, and the original client IP addresses are preserved, enabling DSPs to implement IP-based filtering and geographic targeting.

Note the following about inbound external links:
+ **Quota** – By default, you can create up to two inbound external links per gateway. To request a quota increase, see [Quotas for AWS RTB Fabric](rtb-fabric-quotas.md).
+ **Limited console support** – Inbound external links can only be created and managed through the RTB Fabric API, AWS CLI, or AWS CloudFormation.

To create new inbound external links, use the `CreateInboundExternalLink` API on an external responder gateway. Both use cases produce the same result — an inbound external link — but differ in the returned endpoint format. `CreateResponderGateway` with `gatewayType` as `EXTERNAL` returns an external inbound endpoint (e.g. "rtb-gw-target123.123456789012.gateway.rtbfabric.us-east-1.amazonaws.com"), while `CreateInboundExternalLink` on an internal responder gateway returns a domain name as link endpoint.

Creating inbound external links is supported through the RTB Fabric API, the AWS CLI, and AWS CloudFormation. For complete specifications, see [CreateInboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateInboundExternalLink.html) in the *RTB Fabric API Reference*.

## AWS CLI
<a name="inbound-external-link-cli"></a>

Use the following command to create an inbound external link on an external responder gateway using the AWS Command Line Interface (AWS CLI).

**Create an inbound external link (recommended using external gateway id)**

```
$ aws rtbfabric create-inbound-external-link \
--gateway-id {{rtb-gw-target123}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'}} \
--tags {{'{"Name": "Team Inbound External Link"}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create an inbound external link (deprecated using internal gateway id)**

```
$ aws rtbfabric create-inbound-external-link \
--gateway-id {{rtb-gw-target123}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'}} \
--tags {{'{"Name": "Team Inbound External Link"}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Response
<a name="inbound-response"></a>

The following example shows the response from creating an inbound external link using `CreateInboundExternalLink` on an external responder gateway:

```
{
  "gatewayId": {{"rtb-gw-target123"}},
  "linkId": {{"link-xyz789"}},
  "status": "PENDING_CREATION"
}
```

To find the external inbound endpoint that external partners should use to send traffic to your external responder gateway, see the `externalInboundEndpoint` in the response of `CreateResponderGateway` API.

RTB Fabric sets a DNS TTL (time to live) of 60 seconds for provided domain names. External partners should configure their DNS clients to respect this TTL value to ensure proper failover and load balancing behavior.