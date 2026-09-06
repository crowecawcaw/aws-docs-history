

# Creating outbound external links
<a name="creating-outbound-external-links"></a>

Outbound external links enable connectivity between your requester gateway and external partner endpoints (such as DSPs), extending your RTB infrastructure beyond private VPC connections. Traffic is routed over the AWS Global Network where possible, falling back to public internet routing when required. You must provide the public HTTP or HTTPS endpoint URL of the external responder.

Note the following about outbound external links:
+ **Quota** – By default, you can create up to two outbound external links per gateway. To request a quota increase, see [Quotas for AWS RTB Fabric](rtb-fabric-quotas.md).
+ **Multiple creation methods** – You can create outbound external links using the AWS Management Console, the RTB Fabric API, the AWS CLI, or AWS CloudFormation.

For more information, see [CreateOutboundExternalLink](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateOutboundExternalLink.html) in the *RTB Fabric API Reference*.

**To create an outbound external link**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/).

1. In the navigation pane, choose **Requester gateways**.

1. Select a gateway from the list.

1. On the gateway details page, choose the **Associated links** tab.

1. Choose **Create link**.

1. On the **Create link** screen, review the **Requester Gateway details** section, which displays information about the source gateway for this external outbound link:
   + **Gateway ID** – The unique identifier of the source gateway.
   + **Gateway name** – The name of the source gateway.
   + **Gateway created on** – The date and time when the gateway was created.

1. Choose **Outbound external link** in the **Link settings**.

1. In the **Target details** section, enter the **Target endpoint** of the target responder you want to link with. Enter a valid HTTPS or HTTP public endpoint that accepts RTB requests (for example: **https://example.com**).

1. (Optional) In the **Link information** section, enter a **Correlation ID**. This is a unique identifier you can assign to your link for your own tracking purposes and is not visible to other RTB Fabric users. The correlation ID can have up to 64 characters.

1. In the **Application logs configuration** section, configure the sampling rates to capture exceptions, failures, and unexpected system behaviors:

   1. For **Error logs sampling rate**, enter the percentage (0.0-100.0) of error logs to deliver to your destination. These logs capture exceptions, failures, and unexpected system behaviors. Higher percentages incur additional storage costs.

   1. For **Filter logs sampling rate**, enter the percentage (0.0-100.0) of filter logs to deliver to your destination. These logs are generated from your other RTB Fabric filter modules. Higher percentages incur additional storage costs.

   1. Note the following:

      1. Logs are delivered via [Amazon CloudWatch Vended Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html), which provides delivery directly to Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs.

      1. To configure log delivery destinations, you must use the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](https://docs.aws.amazon.com/rtb-fabric/latest/api/).

      1. AWS does not access or read your log data.

1. Choose **Create link** to send the link request.

1. The link starts in **Pending Creation** status. The first outbound external link on a gateway can take up to 45 minutes to become **Active**. Subsequent outbound external links on the same gateway typically become **Active** in 2-4 minutes.

Once the link status changes to **Active**, it begins facilitating communication between your gateway and the external target endpoint. You can monitor link performance and make configuration changes as needed.

## AWS CLI
<a name="outbound-external-link-cli"></a>

Use the following command to create an outbound external link using the AWS Command Line Interface (AWS CLI).

**Create an outbound external link**

```
$ aws rtbfabric create-outbound-external-link \
--gateway-id {{rtb-gw-source123}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'}} \
--public-endpoint {{http://example.com}} \
--tags {{'{"Name": "Team RTB Outbound External Link"}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Response
<a name="outbound-response"></a>

The following example shows the response from creating an outbound external link:

```
{
  "gatewayId": {{"rtb-gw-source123"}},
  "linkId": {{"link-uvw123"}},
  "status": "PENDING_CREATION"
}
```

Once created, your requester gateway can send traffic to the specified `publicEndpoint` through the RTB Fabric infrastructure.

**Important**  
External links leverage the AWS Global Network where possible but may require public internet routing to reach certain endpoints. This can result in different security, performance, and cost characteristics compared to standard RTB Fabric links.