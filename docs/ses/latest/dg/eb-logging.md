# Mail Manager logging

Mail Manager logging provides detailed visibility into your Mail Manager operations. The logging
functionality tracks message flow from initial receipt at ingress endpoints through message
processing based on your configured rule sets and rules.

Mail Manager offers logging for the following resources:

- Ingress endpoints
- Rule sets
  Mail Manager delivers logs using the Amazon CloudWatch Logs service and the logs can be delivered to any of the
  following destinations: _CloudWatch Logs_, _Amazon S3_, or
  _Amazon Data Firehose_.

## Setting up Mail Manager log delivery

A working log delivery consists of three elements:

- **DeliverySource** – A logical object that
  represents the resource that sends the logs—either an ingress endpoint or a rule
  set.
- **DeliveryDestination** – A logical object
  that represents the actual delivery destination (CloudWatch Logs, S3, or
  Firehose).
- **Delivery** – Connects a delivery source
  to a delivery destination.

This section will explain how to create these objects along with the necessary
permissions required to use Mail Manager logging.

### Prerequisites

Before setting up Mail Manager logging, ensure that:

1. You have created either an [Ingress endpoint](eb-ingress.md "eb-ingress.md") or
   a [Rule set](eb-rules.md "eb-rules.md").
2. You have the necessary CloudWatch Logs and SES Mail Manager permissions to vend logs
   from your Mail Manager resources to their delivery destinations.

#### Required permissions

You'll need to setup the vended logs permissions as explained in the [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2") section of the
_Amazon CloudWatch Logs User Guide_ and apply the permissions that
correspond to your delivery destination:

- [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs")
- [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3")
- [Logs sent to Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose")

In addition, Mail Manager requires the following user permissions to configure log
delivery:

- `ses:AllowVendedLogDeliveryForResource` – Required
  to allow Mail Manager to vend the logs on your behalf to CloudWatch Logs for your specific
  resources as shown in the example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSesMailManagerLogDelivery",
 "Effect": "Allow",
 "Action": [
 "ses:AllowVendedLogDeliveryForResource"
 ],
 "Resource": [
 "arn:aws:ses:`us-east-1`:`111122223333`:mailmanager-ingress-point/inp-xxxxx",
 "arn:aws:ses:`us-east-1`:`111122223333`:mailmanager-rule-set/rs-xxxx"
 ]
 }
 ]
}`

```

### Enabling logging in the SES

console

To enable logging for Mail Manager resources using the console:

1. Open the SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane under **Mail Manager**, choose either
   **Ingress endpoints** or **Rule sets** and
   select the specific resource you wish to enable for logging.
3. On the details page of the resource, expand **Add log
   delivery** and choose delivery to either
   **CloudWatch Logs**, **S3**, or
   **Firehose**.
4. In the **Add delivery to** dialogue box for the
   destination you chose, follow the prompts to configure log delivery options
   specific to the destination type.
5. (Optional) Expand **Additional settings** to customize
   fields of the record, output format, field delimiter, and other parameters
   specific to the destination type.

### Enabling logging using the CloudWatch Logs API

To enable logging for Mail Manager resources using the CloudWatch Logs API, you will need to:

1. Create a DeliverySource with [`PutDeliverySource`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md").
2. Create a DeliveryDestination with [`PutDeliveryDestination`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md").
3. Create a Delivery by pairing exactly one delivery source and one delivery
   destination by using [`CreateDelivery`](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md").

You can view examples of IAM role and permissions policies with all the required
permissions for your specific logging destination in the [Logging that requires additional permissions [V2]](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2") section of the
_Amazon CloudWatch Logs User Guide_, and follow the IAM role and permissions
policy examples for your logging destination, including allowing updates to your
specific logging destination resource, such as _CloudWatch Logs_,
_S3_, or _Firehose_.

###### Note

When creating a DeliverySource, the [`resourceArn`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md#API_PutDeliverySource_RequestSyntax "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md#API_PutDeliverySource_RequestSyntax") can be an Ingress endpoint ARN or a Rule set
ARN. Depending on the DeliverySource, the [`logType`](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md#API_PutDeliverySource_RequestSyntax "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md#API_PutDeliverySource_RequestSyntax") can be as follows:

- **Ingress endpoint ARN** –
  `APPLICATION_LOGS` or
  `TRAFFIC_POLICY_DEBUG_LOGS`
- **Rule set ARN** –
  `APPLICATION_LOGS`

## Interpreting the logs

The logs can be used to gain additional insight into the flow of your received
messages as they are processed by Mail Manager.

The following examples detail the different fields of the logs for each resource and
log type:

###### Log examples

- [Ingress endpoint logs –
  APPLICATION_LOGS](#ingress-endpoint-logs-app "#ingress-endpoint-logs-app")
- [Ingress endpoint logs –
  TRAFFIC_POLICY_DEBUG_LOGS](#ingress-endpoint-logs-traffic "#ingress-endpoint-logs-traffic")
- [Rule set logs –
  APPLICATION_LOGS](#rule-set-logs "#rule-set-logs")

### Ingress endpoint logs –

`APPLICATION_LOGS`

The logs are generated per message.

```
{
  "resource_arn": "arn:aws:ses:us-east-1:1234567890:mailmanager-ingress-point/inp-xxxxx",
  "event_timestamp": 1728562395042,
  "ingress_point_type": "OPEN" | "AUTH",
  "ingress_point_name": "MyIngressPoint",
  "message_id": "0000llcki1jmushh817gr586f963a5inhkvnh81",
  "message_size_bytes": 100000,
  "rule_set_id": "rs-xxxx",
  "sender_ip_address": "1.2.3.4",
  "smtp_mail_from": "someone@domain.com",
  "smtp_helo": "domain.com",
  "tls_protocol": "TLSv1.2",
  "tls_cipher_suite": "TLS_AES_256_GCM_SHA384",
  "recipients": ["me@mydomain.com", "you@mydomain.com", "they@mydomain.com"],
  "ingress_point_metadata": { // only applies to AUTH Ingress Endpoint
       "password_version": "",
       "secrets_manager_arn": ""
  }
}
```

###### Note

Logs are created only for messages that are accepted by the ingress endpoint. An
ingress endpoint that rejects all the incoming messages will not publish any
application logs.

#### Example CloudWatch Logs Insights

queries

Query messages from sender@domain.com:

````
fields @timestamp, @message, @logStream, @log
| filter smtp_mail_from like /sender@domain.com/
| sort @timestamp desc
| limit 10000 ``` Query messages with size greater than 5000 bytes: ``` fields @timestamp, @message, @logStream, @log
| filter message_size_bytes > 5000
| sort @timestamp desc
| limit 10000 ``` ### Ingress endpoint logs – `TRAFFIC_POLICY_DEBUG_LOGS` The logs are generated per recipient. ``` { "resource_arn": "arn:aws:ses:us-east-1:1234567890:mailmanager-ingress-point/inp-xxxxx" CPY, "event_timestamp": 1728562395042, "ingress_point_type": "OPEN" | "AUTH", "ingress_point_id": "inp-xxxx", "ingress_point_session_id": "xxxx", "traffic_policy_id": "tp-xxxx", "traffic_policy_evaluation": [ // Array of policy evaluations { "action": "ALLOW" | "DENY", "conditions": [ // Array of conditions { "expression": { "attribute": "RECIPIENT", "operator": "CONTAINS", "value": ["@domain.com", "@mydomain.com"] }, "expressionResult": true | false }], "policyStatementMatched": true | false }, // If no policy statement match then default action will be applied { "action": "ALLOW" | "DENY", "policyStatementMatched": true, "type": "DefaultAction" } ], "traffic_policy_verdict": "REJECT" | "ACCEPT", "sender_ip_address": "1.2.3.4", "smtp_mail_from": "someone@domain.com", "smtp_helo": "domain.com", "tls_protocol": "TLSv1.2", "recipient": "me@mydomain.com", "tls_cipher_suite": "TLS_AES_256_GCM_SHA384" } ``` ###### Note <br>• Logs are created for all messages that are evaluated by the traffic policy at the ingress endpoint regardless of whether they're accepted or rejected. <br>• All recipient traffic policy evaluations belonging to the same message (within the same SMTP conversation) share a common `ingress_point_session_id`. This ID serves as a correlation identifier since the `message_id` isn't available until after message acceptance. <br>• The `traffic_policy_evaluation` content varies based on your configuration and may terminate early once a verdict is determined. #### Example CloudWatch Logs Insights queries Query messages from sender@domain.com: ``` fields @timestamp, @message, @logStream, @log
| filter smtp_mail_from like /sender@domain.com/
| sort @timestamp desc
| limit 10000 ``` Query messages belonging to a specific `ingress_point_session_id`: ``` fields @timestamp, @message, @logStream, @log
| filter ingress_point_session_id = 'xxx'
| sort @timestamp desc
| limit 10000 ``` Query messages that were rejected: ``` fields @timestamp, @message, @logStream, @log
| filter traffic_policy_verdict = 'REJECT'
| sort @timestamp desc
| limit 10000 ``` ### Rule set logs – `APPLICATION_LOGS` The logs are generated per message per action. This means that a log record is generated each time a message is processed by an action in a rule in the rule set: ``` { "resource_arn": "arn:aws:ses:us-east-1:1234567890:mailmanager-rule-set/rs-xxxx", "event_timestamp": 1732298258254, "message_id": "0000llcki1jmushh817gr586f963a5inhkvnh81", "rule_set_name": "MyRuleSet", "rule_name": "MyRule", "rule_index": 1, "recipients_matched": ["recipient1@domain.com", "recipient2@domain.com"], "action_metadata": { "action_name": "WRITE_TO_S3" | "DROP" | "RELAY" | "DELIVER_TO_MAILBOX" | etc., "action_index": 2, "action_status": "SUCCESS" | "FAILURE" | "IN_PROGRESS", "action_failure": "Access denied" } } ``` <br>• `recipients_matched` – The recipients that were matched by the conditions of the rule for which the action is being performed. <br>• `rule_index` – The rule's order within the rule set. <br>• `action_index` – The action's order within the rule. <br>• `action_status` – Indicates the outcome of performing the action on the given message. <br>• `action_failure` – Indicates the failure details of the action (only applies when an action fails). For instance, if the provided role does not have enough permissions to perform the action. In addition, if the rule conditions did not match for a message, that is, the message is not processed by the rule, a single log is published to indicated that the message has been processed by the rule set, but did not have any actions performed on it: ``` { "resource_arn": "arn:aws:ses:us-east-1:1234567890:mailmanager-rule-set/rs-xxxx", "event_timestamp": 1732298258254, "message_id": "0000llcki1jmushh817gr586f963a5inhkvnh81", "rule_set_name": "MyRuleSet", "rule_name": "MyRule", "rule_index": 1, "recipients_matched": [], } ``` #### Example CloudWatch Logs Insights queries Query for a specific message-id (shows the message flow through the rule set): ``` fields @timestamp, @message, @logStream, @log
| filter message_id = 'message-id-123'
| sort @timestamp desc
| limit 10000 ``` Query for failed WRITE\_TO\_S3 actions: ``` fields @timestamp, @message, @logStream, @log
| filter action_metadata.action_name = 'WRITE_TO_S3' and action_metadata.action_status = 'FAILURE'
| sort @timestamp desc
| limit 10000 ``` Query for messages that did not get processed by the second rule of a rule set (the message did not meet the rule's conditions): ``` fields @timestamp, @message, @logStream, @log
| filter recipients_matched = '[]' and rule_index = 2
| sort @timestamp desc
| limit 10000 ```
````
