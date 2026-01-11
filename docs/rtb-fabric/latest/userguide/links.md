# Links

RTB Fabric links provide secure, performant one-to-one connections between requesters and responders for real-time bidding. Links can be established between two RTB Fabric users (such as between your application and one of your real-time bidding partners that also uses RTB Fabric), or between an RTB Fabric user and an entity outside RTB Fabric, known as external links. These connections form the foundation of your real-time bidding network infrastructure, enabling secure and efficient data exchange between all participants.

###### Note

To create links with other RTB Fabric users, you must first obtain their gateway ID. Contact your business partners directly to exchange gateway IDs, as AWS does not distribute this information.

###### Topics

- [Creating links between RTB Fabric users](#creating-rtb-links "#creating-rtb-links")
- [Testing and using links](#testing-and-using-links "#testing-and-using-links")
- [Creating external links](#creating-external-links "#creating-external-links")
- [Editing links](#editing-links-api "#editing-links-api")
- [Accepting or declining a link request](#accepting-declining-link-request "#accepting-declining-link-request")
- [Deleting links](#deleting-rtb-links "#deleting-rtb-links")
- [Adding modules to links](#adding-modules-to-links "#adding-modules-to-links")
- [Configuring link logging](#configuring-link-logging "#configuring-link-logging")

## Creating links between RTB Fabric users

Links between RTB Fabric users can be created through the AWS Management Console, the AWS CLI, or AWS CloudFormation. Only requester gateways can initiate links to responder gateways.

###### To create a link between gateways

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/ "https://console.aws.amazon.com/rtbfabric/").
2. In the navigation pane, choose **Requester gateways**.
3. Select a gateway from the list.
4. On the gateway details page, choose the **Associated links** tab.
5. Choose **Create link**.
6. On the **Create link** screen, review the **Gateway details** section, which displays information about the source gateway for this link:
   - **Gateway ID** – The unique identifier of the source gateway.
   - **Gateway name** – The name of the source gateway.
   - **Gateway created on** – The date and time when the gateway was created.

7. (Optional) In the **Link information** section, enter a **Correlation ID**. This is a unique identifier you can assign to your link for your own tracking purposes and is not visible to other RTB Fabric users. The correlation ID can have up to 64 characters.
8. In the **Application logs configuration** section, configure the sampling rates to capture exceptions, failures, and unexpected system behaviors:
   1. For **Error logs sampling rate**, enter the percentage (0.0-100.0) of error logs to deliver to your destination. These logs capture exceptions, failures, and unexpected system behaviors. Higher percentages incur additional storage costs.
   2. For **Filter logs sampling rate**, enter the percentage (0.0-100.0) of filter logs to deliver to your destination. These logs are generated from your other RTB Fabric filter modules. Higher percentages incur additional storage costs.Note the following:
   - Logs are delivered via Amazon CloudWatch Vended Logs, which provides delivery directly to Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs.
   - To configure log delivery destinations, you must use the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](../api.md "../api.md").
   - AWS does not access or read your log data.

9. In the **Target details** section, enter the **Target gateway ID** of the target gateway you want to link with. Enter a valid gateway ID (for example: `rtb-gw-source123`).

###### Note

Contact your RTB Fabric partner to obtain their gateway ID. AWS does not provide gateway IDs. 10. Choose **Create link** to send the link request. 11. The link is created with a **Requested** status and sent to the target gateway for approval. The target gateway owner must accept the link request before it becomes active.

Once the target gateway accepts the link request, the link status changes to **Active** and begins facilitating communication between your gateways. You can monitor link performance and make configuration changes as needed.

Use the following command to create a link between gateways using the AWS Command Line Interface (AWS CLI).

**Create a basic link between gateways**

```
`$` `aws rtbfabric create-link \
--gateway-id `rtb-gw-source123` \
--peer-gateway-id `rtb-gw-target456` \
--log-settings `'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

**Create a link with customer-provided ID and tags**

```
`$` `aws rtbfabric create-link \
--gateway-id `rtb-gw-source123` \
--peer-gateway-id `rtb-gw-target456` \
--attributes `customerProvidedId=my-link-correlation-123` \
--log-settings `'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'` \
--tags `'{"Environment": "Production", "Team": "RTB"}'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

## Testing and using links

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

## Creating external links

External links enable connectivity between your RTB Fabric gateways and external partners using the AWS Global Network or public internet, extending your RTB infrastructure beyond private VPC connections. This feature supports integration with external supply-side platforms (SSPs), demand-side platforms (DSPs), and other RTB partners who are not using RTB Fabric infrastructure.

External links differ from standard RTB Fabric links in several key ways:

- **External routing** – Traffic is routed over the AWS Global Network when possible, and the public internet when required to reach external endpoints.
- **Client IP preservation** – In inbound external links, the original client IP addresses are preserved, enabling DSPs to implement IP-based filtering and geographic targeting.
- **Opt-in feature** – External link capability must be explicitly enabled for your account. Use the Service Quotas tool to request access to external link functionality.
- **Limited console support** – While outbound external links can be created through the console, API, AWS CLI, or AWS CloudFormation, inbound external links can only be created and managed through the RTB Fabric API, AWS CLI, or AWS CloudFormation.

Use inbound external links to receive traffic from external partners, and outbound external links to send traffic to external endpoints. For more information, see [CreateInboundExternalLink](../api/API_CreateInboundExternalLink.md "../api/API_CreateInboundExternalLink.md") and [CreateOutboundExternalLink](../api/API_CreateOutboundExternalLink.md "../api/API_CreateOutboundExternalLink.md") in the _RTB Fabric API Reference_.

### Creating outbound external links

Outbound external links allow your requester gateway to send traffic to external partner endpoints (such as DSPs) using optimized routing over the AWS Global Network where possible, falling back to public internet routing when required. You must provide the public HTTP or HTTPS endpoint URL of the external responder. You can create outbound external links using the AWS Management Console, the RTB Fabric API, the AWS CLI, or AWS CloudFormation.

###### To create an outbound external link

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/ "https://console.aws.amazon.com/rtbfabric/").
2. In the navigation pane, choose **Requester gateways**.
3. Select a gateway from the list.
4. On the gateway details page, choose the **Associated links** tab.
5. Choose **Create link**.
6. On the **Create link** screen, review the **Requester Gateway details** section, which displays information about the source gateway for this external outbound link:
   - **Gateway ID** – The unique identifier of the source gateway.
   - **Gateway name** – The name of the source gateway.
   - **Gateway created on** – The date and time when the gateway was created.

7. Choose **Outbound external link** in the **Link settings**.
8. In the **Target details** section, enter the **Target endpoint** of the target responder you want to link with. Enter a valid HTTPS or HTTP public endpoint that accepts RTB requests (for example: `https://example.com`).
9. (Optional) In the **Link information** section, enter a **Correlation ID**. This is a unique identifier you can assign to your link for your own tracking purposes and is not visible to other RTB Fabric users. The correlation ID can have up to 64 characters.
10. In the **Application logs configuration** section, configure the sampling rates to capture exceptions, failures, and unexpected system behaviors:
    1. For **Error logs sampling rate**, enter the percentage (0.0-100.0) of error logs to deliver to your destination. These logs capture exceptions, failures, and unexpected system behaviors. Higher percentages incur additional storage costs.
    2. For **Filter logs sampling rate**, enter the percentage (0.0-100.0) of filter logs to deliver to your destination. These logs are generated from your other RTB Fabric filter modules. Higher percentages incur additional storage costs.
    3. Note the following:
       1. Logs are delivered via [Amazon CloudWatch Vended Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md"), which provides delivery directly to Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs.
       2. To configure log delivery destinations, you must use the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](../api.md "../api.md").
       3. AWS does not access or read your log data.

11. Choose **Create link** to send the link request.
12. The link starts in **Pending Creation** status and becomes **Active** within 3 minutes.

Once the link status changes to **Active**, it begins facilitating communication between your gateway and the external target endpoint. You can monitor link performance and make configuration changes as needed.

Use the following command to create an outbound external link using the AWS Command Line Interface (AWS CLI).

**Create an outbound external link**

```
`$` `aws rtbfabric create-outbound-external-link \
--gateway-id `rtb-gw-source123` \
--log-settings `'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'` \
--public-endpoint `http://example.com` \
--tags `'{"Name": "Team RTB Outbound External Link"}'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

#### Response

The following example shows the response from creating an outbound external link:

```
{
  "gatewayId": `"rtb-gw-source123"`,
  "linkId": `"link-uvw123"`,
  "status": "Active"
}
```

Once created, your requester gateway can send traffic to the specified `publicEndpoint` through the RTB Fabric infrastructure.

###### Important

External links leverage the AWS Global Network where possible but may require public internet routing to reach certain endpoints. This can result in different security, performance, and cost characteristics compared to standard RTB Fabric links.

### Creating inbound external links

Inbound external links allow external partners (e.g., SSPs) to send traffic to your responder gateway over the public internet. When you create an inbound external link, RTB Fabric provides a public domain name that external partners can use to reach your gateway. Creating inbound external links is supported through the RTB Fabric API, the AWS CLI, and AWS CloudFormation. The following examples show how to create an inbound external link using the RTB Fabric API. For complete specifications, see [CreateInboundExternalLink](../api/API_CreateInboundExternalLink.md "../api/API_CreateInboundExternalLink.md") in the _RTB Fabric API Reference_.

Use the following command to create an inbound external link using the AWS Command Line Interface (AWS CLI).

**Create an inbound external link**

```
`$` `aws rtbfabric create-inbound-external-link \
--gateway-id `rtb-gw-target123` \
--log-settings `'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'` \
--tags `'{"Name": "Team Inbound External Link"}'` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

#### Response

The following example shows the response from creating an inbound external link:

```
{
  "gatewayId": `"rtb-gw-target123"`,
  "linkId": `"link-xyz789"`,
  "status": "Active",
  "domainName": "`link-xyz789`.`123456789012`.gateway.`rtbfabric`.us-east-1.amazonaws.com"
}
```

The `domainName` in the response is the public endpoint that external partners should use to send traffic to your responder gateway.

RTB Fabric sets a DNS TTL (time to live) of 60 seconds for provided domain names. External partners should configure their DNS clients to respect this TTL value to ensure proper failover and load balancing behavior.

## Editing links

You can only edit existing links using the API. To modify a link created in the console, you must delete the existing link and create a new one with the updated configuration. For more information, see [UpdateLink](../api/API_UpdateLink.md "../api/API_UpdateLink.md") in the _RTB Fabric API Reference_.

## Accepting or declining a link request

When another RTB Fabric user sends you a link request, you can accept or reject it from your gateway's **Associated links** tab. Link requests allow other RTB Fabric users to connect and send bid requests to your gateway.

###### To accept or reject a link request

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric "https://console.aws.amazon.com/rtbfabric").
2. Choose either **Requester Gateways** or **Responder Gateways** depending on which gateway received the link request.
3. Choose the gateway that received the link request.
4. Choose the **Associated links** tab to view pending link requests.
5. In the **Links** section, locate the link request you want to respond to in the links table. The table displays the following information:
   - **Link ID** – Unique identifier for the link.
   - **Link status** – Current status of the link request.
   - **Link creation date (UTC)** – When the request was created.
   - **Responder Gateway ID** – Target gateway ID.
   - **Actions** – Available actions for the link.

6. In the **Actions** column for the link request, choose one of the following:
   - **To accept the link request:**
     1. Choose **Accept**.
     2. In the confirmation dialog, choose **Accept** to confirm.
     3. The link status changes to **Active** and bid requests can now flow between the gateways.

   - **To reject the link request:**
     1. Choose **Reject**.
     2. In the confirmation dialog, choose **Reject** to confirm.
     3. The link status changes to **Rejected** and the connection request is rejected.

Once you accept a link request, the requesting gateway can send bid requests to your gateway. You can view link metrics and manage the connection from the **Associated links** tab.

###### Note

You can also choose **View details** to see more information about the link request before making your decision. The links table also includes action buttons for **Accept**, **Reject**, and **Delete** operations.

Use the following commands to accept or reject link requests using the AWS Command Line Interface (AWS CLI).

**Accept a link request**

```
`$` `aws rtbfabric accept-link \
--gateway-id `"rtb-gw-target456"` \
--link-id `"link-sedf903ujiose"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

**Reject a link request**

```
`$` `aws rtbfabric reject-link \
--gateway-id `"rtb-gw-target456"` \
--link-id `"link-sedf903ujiose"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

## Deleting links

When you no longer need a link, you can delete it from either the requester or responder gateway. This action permanently removes the connection and stops all communication between the linked gateways.

###### Warning

Deleting a link is irreversible and will immediately stop all bid request processing between the connected gateways. Ensure that you no longer need the link before proceeding.

###### To delete a link

1. Navigate to RTB Fabric console and choose either **Requester Gateways** or **Responder Gateways** depending on which resource owns the link you want to delete.
2. Access the link details using one of these methods:
   - On the gateways page, select the radio button next to the desired gateway. In the **Links associated with this gateway** section at the bottom of the page, choose the **Link ID** you want to delete.
   - Choose the **gateway ID** to open the gateway details page. Choose the **Associated links** tab and choose the **Link ID** you want to delete.

3. On the link details page, review the link information including:
   - **Link ID** – Unique identifier for the link.
   - **Link status** – Current status (Requested, Active, etc.).
   - **gateway ID** – Source gateway.
   - **Peer gateway ID** – Target gateway.
   - **Link created on** and **Link updated on** – Timestamps.

4. Choose **Delete link** from the action buttons at the top of the page.
5. In the confirmation dialog, verify that you want to delete the selected link.
6. Choose **Delete** to confirm the deletion.

The link is immediately removed from both gateways and will no longer facilitate communication between them. Any ongoing bid requests using this link will be terminated.

Use the following command to delete a link between gateways using the AWS Command Line Interface (AWS CLI).

**Delete a link from a gateway**

```
`$` `aws rtbfabric delete-link \
--gateway-id `"rtb-gw-source123"` \
--link-id `"link-sedf903ujiose"` \
--endpoint-url https://rtbfabric.`us-east-1`.amazonaws.com \
--region `us-east-1``
```

## Adding modules to links

You can only add modules to existing links using the RTB Fabric API. Modules enable you to implement rate limiting, filtering, error handling, and other traffic management capabilities on your links. For more information, see [Modules](modules.md "modules.md").

## Configuring link logging

You can configure individual links to deliver logs Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs using the RTB Fabric API. Before configuring link logging, you must first set up log delivery infrastructure. For more information about setting up log delivery destinations, see [UpdateLink](../api/API_UpdateLink.md "../api/API_UpdateLink.md") in the _RTB Fabric API Reference_ and [Configuring RTB Fabric logs with Amazon CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").
