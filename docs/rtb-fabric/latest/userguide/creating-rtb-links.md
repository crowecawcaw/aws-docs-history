

# Creating links between RTB Fabric users
<a name="creating-rtb-links"></a>

Links between RTB Fabric users can be created through the AWS Management Console, the AWS CLI, or AWS CloudFormation. Only requester gateways can initiate links to responder gateways.

**To create a link between gateways**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric/](https://console.aws.amazon.com/rtbfabric/).

1. In the navigation pane, choose **Requester gateways**.

1. Select a gateway from the list.

1. On the gateway details page, choose the **Associated links** tab.

1. Choose **Create link**.

1. On the **Create link** screen, review the **Gateway details** section, which displays information about the source gateway for this link:
   + **Gateway ID** – The unique identifier of the source gateway.
   + **Gateway name** – The name of the source gateway.
   + **Gateway created on** – The date and time when the gateway was created.

1. (Optional) In the **Link information** section, enter a **Correlation ID**. This is a unique identifier you can assign to your link for your own tracking purposes and is not visible to other RTB Fabric users. The correlation ID can have up to 64 characters.

1. In the **Application logs configuration** section, configure the sampling rates to capture exceptions, failures, and unexpected system behaviors:

   1. For **Error logs sampling rate**, enter the percentage (0.0-100.0) of error logs to deliver to your destination. These logs capture exceptions, failures, and unexpected system behaviors. Higher percentages incur additional storage costs.

   1. For **Filter logs sampling rate**, enter the percentage (0.0-100.0) of filter logs to deliver to your destination. These logs are generated from your other RTB Fabric filter modules. Higher percentages incur additional storage costs.

   Note the following:
   + Logs are delivered via Amazon CloudWatch Vended Logs, which provides delivery directly to Amazon S3, Amazon Data Firehose, or Amazon CloudWatch Logs.
   + To configure log delivery destinations, you must use the RTB Fabric API. For more information, see the [AWS RTB Fabric API Reference](https://docs.aws.amazon.com/rtb-fabric/latest/api/).
   + AWS does not access or read your log data.

1. In the **Target details** section, enter the **Target gateway ID** of the target gateway you want to link with. Enter a valid gateway ID (for example: **rtb-gw-source123**).
**Note**  
Contact your RTB Fabric partner to obtain their gateway ID. AWS does not provide gateway IDs.

1. Choose **Create link** to send the link request.

1. The link is created with a **Requested** status and sent to the target gateway for approval. The target gateway owner must accept the link request before it becomes active.
**Important**  
Links that are not accepted within 7 days of requesting will time out, and will need to be re-initiated. 

Once the target gateway accepts the link request, the link status changes to **Active** and begins facilitating communication between your gateways. You can monitor link performance and make configuration changes as needed.

## AWS CLI
<a name="create-link-cli"></a>

Use the following command to create a link between gateways using the AWS Command Line Interface (AWS CLI).

**Create a basic link between gateways**

```
$ aws rtbfabric create-link \
--gateway-id {{rtb-gw-source123}} \
--peer-gateway-id {{rtb-gw-target456}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

**Create a link with customer-provided ID and tags**

```
$ aws rtbfabric create-link \
--gateway-id {{rtb-gw-source123}} \
--peer-gateway-id {{rtb-gw-target456}} \
--attributes {{customerProvidedId=my-link-correlation-123}} \
--log-settings {{'{"applicationLogs":{"sampling":{"errorLog":100.0,"filterLog":0}}}'}} \
--tags {{'{"Environment": "Production", "Team": "RTB"}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```