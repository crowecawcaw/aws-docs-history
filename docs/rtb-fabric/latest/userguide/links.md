# Links

RTB Fabric links establish secure connections between your requester gateways and responder gateways in your real-time bidding infrastructure. Links can be between RTB Fabric users, or between an RTB Fabric user and an external entity (external links). These links enable seamless data flow and communication between gateways, allowing your applications to build comprehensive bidding workflows through RTB Fabric infrastructure.

###### Note

To create links with other RTB Fabric users, you need their responder gateway ID. Contact your RTB Fabric partners directly to exchange gateway IDs. AWS does not provide gateway IDs for external partners, so coordinate directly with your business partners to obtain this information.

###### Topics

- [Creating links between gateways](#creating-rtb-links "#creating-rtb-links")
- [Creating external links](#creating-external-links "#creating-external-links")
- [Editing links](#editing-links-api "#editing-links-api")
- [Accepting or declining a link request](#accepting-declining-link-request "#accepting-declining-link-request")
- [Deleting gateway links](#deleting-rtb-links "#deleting-rtb-links")
- [Adding modules to links](#adding-modules-to-links "#adding-modules-to-links")
- [Configuring link logging](#configuring-link-logging "#configuring-link-logging")

## Creating links between gateways

You can create links between RTB Fabric gateways through the AWS Management Console. Only requester gateways can initiate link creation to connect with responder gateways in the system.

###### To create a link between gateways

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/ "https://console.aws.amazon.com/rtbfabric/").
2. In the navigation pane, choose **Requester gateways**.
3. Select an RTB application from the list.
4. On the application details page, choose the **Associated links** tab.
5. Choose **Create link**.
6. On the **Create link** screen, review the **Gateway details** section, which displays information about the source gateway for this link:
   - **Gateway ID** – The unique identifier of the source gateway.
   - **Gateway name** – The name of the source gateway.
   - **Gateway created on** – The date and time when the gateway was created.

7. (Optional) In the **Link information** section, enter a **Correlation ID**. This is a unique identifier you can assign to your link for your own tracking purposes and is not visible to other RTB Fabric users. The correlation ID can have up to 64 characters.
8. In the **Application logs configuration** section, configure the sampling rates to capture exceptions, failures, and unexpected system behaviors:
   1. For **Error logs sampling rate**, enter the percentage (0.0-100.0) of error logs to deliver to your destination. These logs capture exceptions, failures, and unexpected system behaviors. Higher percentages incur additional storage costs.
   2. For **Filter logs sampling rate**, enter the percentage (0.0-100.0) of filter logs to deliver to your destination. These logs are generated from your other RTB Fabric filter modules. Higher percentages incur additional storage costs.Note the following:
   - AWS does not access or read your log data.
   - Range must be from 0.0-100.0.
   - To configure log delivery destinations, you must use the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](../api.md "../api.md").

9. In the **Target details** section, enter the **Target gateway ID** of the target gateway you want to link with. Enter a valid gateway ID (for example: `rtb-gw-q6jlbximmmnaz1q5676wots4xy`).

###### Note

Contact your RTB Fabric partner to obtain their gateway ID. AWS does not provide gateway IDs. 10. Choose **Create link** to send the link request. 11. The link is created with a **Requested** status and sent to the target gateway for approval. The target gateway owner must accept the link request before it becomes active.

Once the target application accepts the link request, the link status changes to **Active** and begins facilitating communication between your RTB applications. You can monitor link performance and make configuration changes as needed.

Use the following command to create a link between gateways using the AWS Command Line Interface (AWS CLI).

```
# Create a basic link between gateways
aws rtbfabric create-link \
    --gateway-id rtb-gw-source123 \
    --peer-gateway-id rtb-gw-target456 \
    --log-settings '{
        "applicationLogs": {
            "sampling": {
                "errorLog": 100.0,
                "filterLog": 0.0
            }
        }
    }'

# Create a link with customer-provided ID and tags
aws rtbfabric create-link \
    --gateway-id rtb-gw-source123 \
    --peer-gateway-id rtb-gw-target456 \
    --attributes customerProvidedId=my-link-correlation-123 \
    --log-settings '{
        "applicationLogs": {
            "sampling": {
                "errorLog": 100.0,
                "filterLog": 0.0
            }
        }
    }' \
    --tags Environment=Production Team=RTB
```

## Creating external links

Using the AWS Management Console, you can create outbound external links in your RTB Fabric requester gateway. Outbound external links allow connectivity with external responders (such as DSPs).

###### To create an outbound external link

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/ "https://console.aws.amazon.com/rtbfabric/").
2. In the navigation pane, choose **Requester gateways**.
3. Select an RTB application from the list.
4. On the application details page, choose the **Associated links** tab.
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

Once the link status changes to **Active**, it begins facilitating communication between your RTB application and the external target endpoint. You can monitor link performance and make configuration changes as needed.

External links enable connectivity between your RTB Fabric gateways and external partners over the public internet, extending your RTB infrastructure beyond private VPC connections. This feature supports integration with external supply-side platforms (SSPs), demand-side platforms (DSPs), and other RTB partners who are not using RTB Fabric infrastructure.

External links differ from standard RTB Fabric links in several key ways:

- **Public internet connectivity** – Traffic flows over the public internet rather than private AWS network infrastructure.
- **Client IP preservation** – In inbound external links, the original client IP addresses are preserved, enabling DSPs to implement IP-based filtering and geographic targeting.
- **Opt-in feature** – External link capability must be explicitly enabled for your account. Contact AWS support to request access to external link functionality.
- **API-only creation** – External links can only be created and managed through the RTB Fabric API, not through the console.

Use inbound external links to receive traffic from external partners, and outbound external links to send traffic to external endpoints. You can only create external links using the RTB Fabric API. For more information, see [CreateInboundExternalLink](../api/API_CreateInboundExternalLink.md "../api/API_CreateInboundExternalLink.md") and [CreateOutboundExternalLink](../api/API_CreateOutboundExternalLink.md "../api/API_CreateOutboundExternalLink.md") in the _RTB Fabric API Reference_.

### Creating inbound external links

Inbound external links allow external partners to send traffic to your responder gateway over the public internet. When you create an inbound external link, RTB Fabric provides a public domain name that external partners can use to reach your gateway. The following examples show how to create an inbound external link using the RTB Fabric API. For complete specifications, see [CreateInboundExternalLink](../api/API_CreateInboundExternalLink.md "../api/API_CreateInboundExternalLink.md") in the _RTB Fabric API Reference_.

#### API request

The following example shows the API request to create an inbound external link:

```
POST /responder-gateway/{gatewayId}/inbound-external-link

{
  "attributes": {
    "customerProvidedId": "external-partner-link-001"
  }
}
```

#### Example using curl

The following example shows how to create an inbound external link using curl:

```
curl -X POST \
  "https://rtbfabric.us-east-1.amazonaws.com/responder-gateway/rtb-gw-abc123/inbound-external-link" \
  -H "Authorization: AWS4-HMAC-SHA256 ..." \
  -H "Content-Type: application/json" \
  -d '{
    "attributes": {
      "customerProvidedId": "external-partner-link-001"
    }
  }'
```

#### Response

The following example shows the response from creating an inbound external link:

```
{
  "gatewayId": "rtb-gw-abc123",
  "linkId": "link-xyz789",
  "status": "Active",
  "domainName": "abc123.rtbfabric.amazonaws.com"
}
```

The `domainName` in the response is the public endpoint that external partners should use to send traffic to your responder gateway.

RTB Fabric sets a DNS TTL (time to live) of 60 seconds for provided domain names. External partners should configure their DNS clients to respect this TTL value to ensure proper failover and load balancing behavior.

### Creating outbound external links

Outbound external links allow your requester gateway to send traffic to external partner endpoints over the public internet. You must provide the public HTTPS endpoint URL of the external responder.

#### API request

The following example shows the API request to create an outbound external link:

```
POST /requester-gateway/{gatewayId}/outbound-external-link

{
  "publicEndpoint": "https://external-partner.com/bid-endpoint"
}
```

#### Example using curl

The following example shows how to create an outbound external link using curl:

```
curl -X POST \
  "https://rtbfabric.us-east-1.amazonaws.com/requester-gateway/rtb-gw-def456/outbound-external-link" \
  -H "Authorization: AWS4-HMAC-SHA256 ..." \
  -H "Content-Type: application/json" \
  -d '{
    "publicEndpoint": "https://external-partner.com/bid-endpoint"
  }'
```

#### Response

The following example shows the response from creating an outbound external link:

```
{
  "gatewayId": "rtb-gw-def456",
  "linkId": "link-uvw123",
  "status": "Active"
}
```

Once created, your requester gateway can send traffic to the specified `publicEndpoint` through the RTB Fabric infrastructure.

###### Important

External links operate over the public internet and may have different security, performance, and cost characteristics compared to internal links. Ensure that your external endpoints support HTTPS and follow security best practices for public internet communication.

## Editing links

You can only edit existing links using the API. To modify a link created in the console, you must delete the existing link and create a new one with the updated configuration. For more information, see [UpdateLink](../api/API_UpdateLink.md "../api/API_UpdateLink.md") in the _RTB Fabric API Reference_.

## Accepting or declining a link request

When another RTB application sends you a link request, you can accept or reject it from your application's **Associated links** tab. Link requests allow other applications to connect and send bid requests to your application.

###### To accept or reject a link request

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric "https://console.aws.amazon.com/rtbfabric").
2. Choose either **Requester Gateways** or **Responder Gateways** depending on which application received the link request.
3. Choose the RTB application that received the link request.
4. Choose the **Associated links** tab to view pending link requests.
5. In the **Links** section, locate the link request you want to respond to in the links table. The table displays the following information:
   - **Link ID** – Unique identifier for the link.
   - **Link status** – Current status of the link request.
   - **Link creation date (UTC)** – When the request was created.
   - **Responder Gateway ID** – Target application ID.
   - **Actions** – Available actions for the link.

6. In the **Actions** column for the link request, choose one of the following:
   - **To accept the link request:**
     1. Choose **Accept**.
     2. In the confirmation dialog, choose **Accept** to confirm.
     3. The link status changes to **Active** and bid requests can now flow between the applications.

   - **To reject the link request:**
     1. Choose **Reject**.
     2. In the confirmation dialog, choose **Reject** to confirm.
     3. The link status changes to **Rejected** and the connection request is rejected.

Once you accept a link request, the requesting application can send bid requests to your application. You can view link metrics and manage the connection from the **Associated links** tab.

###### Note

You can also choose **View details** to see more information about the link request before making your decision. The links table also includes action buttons for **Accept**, **Reject**, and **Delete** operations.

Use the following commands to accept or reject link requests using the AWS Command Line Interface (AWS CLI).

```
# Accept a link request
aws rtbfabric accept-link \
    --gateway-id "rtb-gw-kasoi29asfdhn" \
    --link-id "link-sedf903ujiose"

# Reject a link request
aws rtbfabric reject-link \
    --gateway-id "rtb-gw-kasoi29asfdhn" \
    --link-id "link-sedf903ujiose"
```

## Deleting gateway links

When you no longer need a link between RTB applications, you can delete it from either the requester or responder application. This action permanently removes the connection and stops all communication between the linked applications.

###### Warning

Deleting a link is irreversible and will immediately stop all bid request processing between the connected RTB applications. Ensure that you no longer need the link before proceeding.

###### To delete an RTB application link

1. Navigate to the RTB applications service and choose either **Requester Gateways** or **Responder Gateways** depending on which application owns the link you want to delete.
2. Access the link details using one of these methods:
   - On the applications page, select the radio button next to the desired application. In the **Links associated with this RTB application** section at the bottom of the page, choose the **Link ID** you want to delete.
   - Choose the **RTB application ID** to open the application details page. Choose the **Associated links** tab and choose the **Link ID** you want to delete.

3. On the link details page, review the link information including:
   - **Link ID** – Unique identifier for the link.
   - **Link status** – Current status (Requested, Active, etc.).
   - **RTB application ID** – Source application.
   - **Peer RTB application ID** – Target application.
   - **Link created on** and **Link updated on** – Timestamps.

4. Choose **Delete link** from the action buttons at the top of the page.
5. In the confirmation dialog, verify that you want to delete the selected link.
6. Choose **Delete** to confirm the deletion.

The link is immediately removed from both RTB applications and will no longer facilitate communication between them. Any ongoing bid requests using this link will be terminated.

Use the following command to delete a link between RTB applications using the AWS Command Line Interface (AWS CLI).

```
# Delete a link from a gateway
aws rtbfabric delete-link \
    --gateway-id "rtb-gw-kasoi29asfdhn" \
    --link-id "link-sedf903ujiose"
```

## Adding modules to links

You can only add modules to existing links using the RTB Fabric API. Modules enable you to implement rate limiting, filtering, error handling, and other traffic management capabilities on your links. For more information, see [Modules](modules.md "modules.md").

## Configuring link logging

You can configure individual links to deliver logs to CloudWatch Logs using the RTB Fabric API. Before configuring link logging, you must first set up log delivery infrastructure. For more information about setting up log delivery destinations, see [UpdateLink](../api/API_UpdateLink.md "../api/API_UpdateLink.md") in the _RTB Fabric API Reference_ and [Configuring RTB Fabric logs with Amazon CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").
