# Troubleshoot alert manager with CloudWatch Logs

Using [Monitor Amazon Managed Service for Prometheus events with CloudWatch Logs](CW-logs.md "CW-logs.md"), you can troubleshoot Alert
Manager and Ruler related issues. This section contains Alert Manager related
troubleshooting topics.

###### Topics

- [Active alerts
  warning](#Troubleshooting-alerting-active-alerts "#Troubleshooting-alerting-active-alerts")
- [Alert aggregation
  group size warning](#Troubleshooting-alerting-aggregation-group-size "#Troubleshooting-alerting-aggregation-group-size")
- [Alerts size too big
  warning](#Troubleshooting-alerting-size-too-big "#Troubleshooting-alerting-size-too-big")
- [Empty content warning](#Troubleshooting-alerting-empty "#Troubleshooting-alerting-empty")
- [Invalid
  key/value warning](#Troubleshooting-alerting-invalid-keyvalue "#Troubleshooting-alerting-invalid-keyvalue")
- [Message limit warning](#Troubleshooting-alerting-msg-limit "#Troubleshooting-alerting-msg-limit")
- [No resource based policy
  error](#Troubleshooting-alerting-no-policy "#Troubleshooting-alerting-no-policy")
- [Non ASCII warning](#Troubleshooting-alerting-non-ASCII "#Troubleshooting-alerting-non-ASCII")
- [Not authorized to call
  KMS](#Troubleshooting-alerting-no-access-kms "#Troubleshooting-alerting-no-access-kms")
- [Template error](#Troubleshooting-template-error "#Troubleshooting-template-error")

## Active alerts

warning

**When the log contains the following
warning**

```
{
    "workspaceId": "ws-efdc5b42-b051-11ec-b123-4567ac120002",
    "message": {
        "log": "too many alerts, limit: 1000",
        "level": "WARN"
    },
    "component": "alertmanager"
}
```

This means that the Alert manager **Active alerts** quota is
exceeded.

**Action to take**

Request a quota increase. Sign in to the AWS Management Console and open the Service Quotas console
at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

## Alert aggregation

group size warning

**When the log contains the following
warning**

```
{
    "workspaceId": "ws-efdc5b42-b051-11ec-b123-4567ac120002",
    "message": {
        "log": "Too many aggregation groups, cannot create new group for alert, groups=1000, limit=1000, alert=sample-alert",
        "level": "WARN"
    },
    "component": "alertmanager"
}
```

This means that the Alert manager Alert aggregation group size quota has been
exceeded.

**Action to take**

Reduce the Alert aggregation group size by using the `group_by`
parameter. For more information, see [Route-related
settings in the](https://prometheus.io/docs/alerting/latest/configuration/ "https://prometheus.io/docs/alerting/latest/configuration/")_Prometheus documentation_.

You can also request a quota increase. Sign in to the AWS Management Console and open the
Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

## Alerts size too big

warning

**When the log contains the following
warning**

```
{
    "workspaceId": "ws-efdc5b42-b051-11ec-b123-4567ac120002",
    "message": {
        "log": "alerts too big, total size limit: 20000000 bytes",
        "level": "WARN"
    },
    "component": "alertmanager"
}
```

This means that Alert manager Alerts per workspace, in size quota has been
exceeded.

**Action to take**

Remove unnecessary annotations and labels to reduce alert size.

## Empty content warning

**When the log contains the following
warning**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "Message has been modified because the content was empty."
       "level": "WARN"
   },
   "component": "alertmanager"
}
```

This means that the Alert manager template resolved the outbound alert to an empty
message.

**Action to take**

Validate your Alert manager template and ensure that you have a valid template for
all receiver pathways.

## Invalid

`key/value` warning

**When the log contains the following
warning**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "MessageAttributes has been removed because of invalid key/value, numberOfRemovedAttributes=1"
       "level": "WARN"
   },
   "component": "alertmanager"
}
```

This means that some of the message attributes have been removed due to
keys/values being invalid.

**Action to take**

Re-evaluate the templates you are using to populate the message attributes, and
ensure it is resolving to a valid SNS message attribute. For more information about
validating a message to an Amazon SNS topic, see [Validating SNS topic](../../../sns/latest/api/API_Publish.md#API_Publish_RequestParameters "../../../sns/latest/api/API_Publish.md#API_Publish_RequestParameters")

## Message limit warning

**When the log contains the following
warning**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "Message has been truncated because it exceeds size limit, originSize=266K, truncatedSize=12K"
       "level": "WARN"
   },
   "component": "alertmanager"
}
```

This means that some of the message size is too big.

**Action to take**

Look at the Alert receiver message template and re-work it to fit within the size
limit.

## No resource based policy

error

**When the log contains the following error**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "Notify for alerts failed, AMP is not authorized to perform: SNS:Publish on resource: arn:aws:sns:us-west-2:12345:testSnsReceiver because no resource-based policy allows the SNS:Publish action"
       "level": "ERROR"
   },
   "component": "alertmanager"
}
```

This means that Amazon Managed Service for Prometheus does not have the permissions to submit the alert to the
SNS topic specified.

**Action to take**

Validate that the access policy on your Amazon SNS topic grants Amazon Managed Service for Prometheus the ability
to send SNS messages to the topic. Create an SNS Access Policy giving the service
`aps.amazonaws.com` (Amazon Managed Service for Prometheus) access to your Amazon SNS topic. For more
information about SNS Access Policies, see [Using the Access
Policy Language](../../../sns/latest/dg/sns-access-policy-language-using.md "../../../sns/latest/dg/sns-access-policy-language-using.md") and [Example cases for Amazon SNS
access control](../../../sns/latest/dg/sns-access-policy-use-cases.md "../../../sns/latest/dg/sns-access-policy-use-cases.md") in the _Amazon Simple Notification Service Developer
Guide_.

## Non ASCII warning

**When the log contains the following
warning**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "Subject has been modified because it contains control or non-ASCII characters."
       "level": "WARN"
   },
   "component": "alertmanager"
}
```

This means that the subject has non-ASCII characters.

**Action to take**

Remove references in subject field of your template to the labels that might
contain non-ASCII characters.

## Not authorized to call

KMS

**When the log contains the following AWS KMS
error**

```
{
   "workspaceId": "ws-abcd1234-ef56-78ab-cd90-1234abcd0000",
   "message": {
       "log": "Notify for alerts failed, AMP is not authorized to call KMS",
       "level": "ERROR"
   },
   "component": "alertmanager"
}
```

**Action to take**

Validate that the key policy of the key used to encrypt the Amazon SNS topic allows the
Amazon Managed Service for Prometheus service principal `aps.amazonaws.com` to perform the following
actions: `kms:GenerateDataKey*`, and `kms:Decrypt`. For more
information, see [AWS
KMS Permissions for SNS Topic](../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse "../../../sns/latest/dg/sns-key-management.md#sns-what-permissions-for-sse").

## Template error

**When the log contains the following error**

```

               {
   "workspaceId": "ws-efdc5b42-b051-11ec-b123-4567ac120002",
   "message": {
       "log": "Notify for alerts failed. There is an error in a receiver that is using templates in the AlertManager definition. Make sure that the syntax is correct and only template functions and variables that exist are used in the receiver 'default', sns_configs position #2, section 'attributes'"
       "level": "ERROR"
   },
   "component": "alertmanager"
}

```

This means that there is an error in a template being used in the AlertManager
definition. The error entry contains directions about what receiver, the position in
the sns_configs and the property that contains errors.

**Action to take**

Validate your Alert Manager definition. Make sure that the syntax is correct and
that you reference template variables and functions that exist. For more
information, see the [Notification
Template Reference](https://prometheus.io/docs/alerting/latest/notifications/ "https://prometheus.io/docs/alerting/latest/notifications/") in the _Prometheus_ open-source
documentation.
