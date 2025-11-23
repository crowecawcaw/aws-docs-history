# Route server peer logging

Use VPC Route Server peer logging when you need to:

- Monitor BGP and BFD session health
- Troubleshoot connection issues
- Review historical session changes
- Track network status

## Pricing

- **CloudWatch**: Data ingestion and archival
  charges for vended logs apply when you publish route server peer logs to
  CloudWatch Logs.
- **S3**: Data ingestion and archival charges
  for vended logs apply when you publish route server peer logs to Amazon
  S3.
- **Data Firehose**: Standard ingestion and
  delivery charges apply.

Vended logs are logs from specific AWS services that are available at
volume tiered pricing and delivered to CloudWatch Logs, Amazon S3, or Amazon
Data Firehose. For more information, open [Amazon CloudWatch
Pricing](https://aws.amazon.com//cloudwatch/pricing/ "https://aws.amazon.com//cloudwatch/pricing/"), select **Logs** and find
**Vended Logs**.

## Example log format

```
{
    "resource_arn": "arn:aws:ec2:us-east-1:111122223333:route-server-peer/rsp-1234567890abcdef0",
    "event_timestamp": 1746643505367,
    "type": "RouteStatus",
    "status": "ADVERTISED",
    "message": {
        "prefix": "10.24.34.0/32",
        "asPath": "65000",
        "med": 100,
        "nextHopIp": "10.24.34.1"
    }
}

{
    "resource_arn": "arn:aws:ec2:us-east-1:111122223333:route-server-peer/rsp-1234567890abcdef0",
    "event_timestamp": 1746643490000,
    "type": "BGPStatus",
    "status": "UP",
    "message": null
}
```

Where:

- The `resource_arn` is the ARN for the route server peer.
- The `event_timestamp` is the timestamp of the event.
- The `type` of log events we produce (`RouteStatus`, `BGPStatus`, `BFDStatus`).
- The `status` field is the status update.
  - For `RouteStatus` type messages
    - `ADVERTISED` (route was advertised by the
      peer)
    - `UPDATED` (existing route was updated by the peer)
    - `WITHDRAWN` (route was withdrawn by peer)

  - For `BFDStatus` and `BGPStatus` updates
    - `UP`, `DOWN`.

- The `message` field is currently only used for route attributes for the RouteStatus message type but may be populated with relevant information for any type.

AWS Management Console
To create route server peer logs:

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, under **Virtual private cloud**, choose **Route servers**.
3. On the **Route servers** page, choose **Route server peers**.
4. Choose the **Log delivery** tab.
5. Choose **Add log delivery**.
6. Choose a destination and configure the settings:
   - Amazon CloudWatch Logs
     - **Log type**: Types of logs to deliver. The only supported log
       type is EVENT_LOGS.
     - **Destination log group**: The CloudWatch log group where logs will be sent. You can pick an existing log group or create a new one (example: /aws/vpc/route-server-peers).
     - **Field selection**: Data fields to include in your
       logs.
     - **Output format**: How logs
       are formatted:
       - JSON: Structured format for computer processing
       - Text: Plain text format

     - **Field delimiter**: When using Text format, this is the character that separates fields (example: comma, tab, space).

   - Amazon S3
     - Cross account - Sending logs to different AWS accounts
       - **Log type**: Types of logs to deliver. The only supported log
         type is EVENT_LOGS.
       - **Delivery destination ARN**: The Amazon Resource Name of the S3 bucket in another AWS account where logs will be sent.
       - **Field selection**: Data fields to include in your
         logs.
       - **Suffix**: The ending added to log file names (example: .log, .txt).
       - **Hive-compatible**: When turned on, organizes logs in a folder structure that works with Hive-based tools for easier searching with services like Amazon Athena.
       - **Field delimiter**: When using Text format, this is the character that separates fields.

     - In current account
       - **Log type**: Types of logs to deliver. The only supported log
         type is EVENT_LOGS.
       - **Destination S3 bucket**: The S3 bucket in your account where logs will be sent. You can specify a subfolder path.
       - **Field selection**: Data fields to include in your
         logs.
       - **Suffix**: The ending added to log file names (example: .log, .txt).
       - **Hive-compatible**: When turned on, organizes logs in a folder structure that works with Hive-based tools for easier searching.
       - **Field delimiter**: When using Text format, this is the character that separates fields.

   - Amazon Data Firehose
     - Cross account
       - **Log type**: Types of logs to deliver. The only supported log
         type is EVENT_LOGS.
       - **Delivery destination ARN**: The Amazon Resource Name of the Firehose delivery stream in another AWS account.
       - **Field selection**: Data fields to include in your
         logs.
       - **Field delimiter**: When using Text format, this is the character that separates fields.

     - In current account
       - **Log type**: Types of logs to deliver. The only supported log
         type is EVENT_LOGS.
       - **Delivery destination stream**: The Firehose delivery stream in your account where logs will be sent. The stream must use the "Direct Put" source type.
       - **Field selection**: Data fields to include in your
         logs.
       - **Output format**:
         How logs are formatted:
         - JSON: Structured format for computer processing
         - Text: Plain text format

       - **Field delimiter**: When using Text format, this is the character that separates fields.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

To create route server peer logs:

1. Use the [put-delivery-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-source.html") command.
   - Example request

   ```
   aws logs put-delivery-source --name "source-rsp-1234567890abcdef0" --resource-arn "arn:aws:ec2:us-east-1:111122223333:route-server-peer/rsp-1234567890abcdef0" --log-type "EVENT_LOGS"
   ```

   - Example response

   ```
   {
        "deliverySource": {
           "name": "source-rsp-1234567890abcdef0",
           "arn": "arn:aws:logs:us-east-1:111122223333:delivery-source:source-rsp-1234567890abcdef0",
           "resourceArns": [
               "arn:aws:ec2:us-east-1:111122223333:route-server-peer/rsp-1234567890abcdef0"
           ],
           "service": "ec2",
           "logType": "EVENT_LOGS"
       }
   }
   ```

2. Use the [put-delivery-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-destination.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-delivery-destination.html") command.
   - The following AWS CLI example creates a route server log. The logs are delivered to the specified log group.
   - Example request

   ```
   aws logs put-delivery-destination --name "destination-rsp-abcdef01234567890" --destination-resource-arn "arn:aws:logs:us-east-1:111122223333:log-group:/aws/vendedlogs/ec2/route-server-peer/EVENT_LOGS/rsp-abcdef01234567890"
   ```

   - Example response

   ```
   {
        "deliveryDestination": {
           "name": "destination-rsp-abcdef01234567890",
           "arn": "arn:aws:logs:us-east-1:111122223333:delivery-destination:destination-rsp-abcdef01234567890",
           "deliveryDestinationType": "CWL",
           "deliveryDestinationConfiguration": {
               "destinationResourceArn": "arn:aws:logs:us-east-1:111122223333:log-group:/aws/vendedlogs/ec2/route-server-peer/EVENT_LOGS/rsp-abcdef01234567890"
           }
       }
   }
   ```

3. Use the [create-delivery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-delivery.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-delivery.html") command.
   - Example request

   ```
   aws logs create-delivery --delivery-source-name "source-rsp-1234567890abcdef0" --delivery-destination-arn "arn:aws:logs:us-east-1:111122223333:delivery-destination:destination-rsp-abcdef01234567890"
   ```

   - Example response

   ```
   {
        "delivery": {
           "id": "1234567890abcdef0",
           "arn": "arn:aws:logs:us-east-1:111122223333:delivery:1234567890abcdef0",
           "deliverySourceName": "source-rsp-1234567890abcdef0",
           "deliveryDestinationArn": "arn:aws:logs:us-east-1:111122223333:delivery-destination:destination-rsp-abcdef01234567890",
           "deliveryDestinationType": "CWL",
           "recordFields": [
               "resource_arn",
               "event_timestamp",
               "type",
               "status",
               "message"
           ]
       }
   }
   ```
