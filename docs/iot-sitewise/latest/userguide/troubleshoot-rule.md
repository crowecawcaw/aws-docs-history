# Troubleshoot an AWS IoT SiteWise rule action

To troubleshoot your AWS IoT SiteWise rule action in AWS IoT Core, you can do one of the following
procedures:

- Configure Amazon CloudWatch Logs
- Configure a republish error action for your rule
  Then, compare the error messages with the errors in this topic to troubleshoot your
  issue.

###### Topics

- [Configure AWS IoT Core logs](#configure-iot-logs "#configure-iot-logs")
- [Configure a republish error action](#configure-republish-error-action "#configure-republish-error-action")
- [Troubleshoot rule issues](#troubleshoot-rule-issues "#troubleshoot-rule-issues")
- [Troubleshoot a rule (AWS IoT SiteWise)](#rule-tutorial-troubleshoot-rule "#rule-tutorial-troubleshoot-rule")
- [Troubleshoot a rule (DynamoDB)](#dynamodb-tutorial-troubleshoot-rule "#dynamodb-tutorial-troubleshoot-rule")

## Configure AWS IoT Core logs

You can configure AWS IoT to log various levels of information to CloudWatch Logs.

###### To configure and access CloudWatch Logs

1. To configure logging for AWS IoT Core, see [Monitoring with CloudWatch Logs](../../../iot/latest/developerguide/cloud-watch-logs.md "../../../iot/latest/developerguide/cloud-watch-logs.md") in the
   _AWS IoT Developer Guide_.
2. Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Log groups**.
4. Choose the **AWSIotLogs** group.
5. Choose a recent log stream. By default, CloudWatch displays the most recent log stream
   first.
6. Choose a log entry to expand the log message. Your log entry might look like the following
   screenshot.

![CloudWatch "AWS IoT Logs" screenshot.](images/rule-ingestion/troubleshoot-rule-logs-console.png) 7. Compare the error messages with the errors in this topic to troubleshoot your
issue.

## Configure a republish error action

You can configure an error action on your rule to handle error messages. In this procedure,
you configure the republish rule action as an error action to view error messages in the MQTT
test client.

###### Note

The republish error action outputs only the equivalent of `ERROR` level logs. If
you want more verbose logs, you must [configure
CloudWatch Logs](#configure-iot-logs "#configure-iot-logs").

###### To add a republish error action to a rule

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Act** and then choose
   **Rules**.
3. Choose your rule.
4. Under **Error action**, choose **Add action**.
5. Choose **Republish a message to an AWS IoT topic**.

![AWS IoT Core "Select an action" page screenshot with the Republish action highlighted.](images/rule-ingestion/rule-choose-republish-action-console.png) 6. Choose **Configure action** at the bottom of the page. 7. In **Topic**, enter a unique topic (for example,
`sitewise/windfarm/rule/error`). AWS IoT Core will republish error messages
to this topic. 8. Choose **Select** to grant AWS IoT Core access to perform the error
action. 9. Choose **Select** next to the role that you created for the rule. 10. Choose **Update Role** to add the additional permissions to the
role. 11. Choose **Add action**.

Your rule's error action should look similar to the following screenshot.

![AWS IoT Core "Rule" page Republish error action screenshot.](images/rule-ingestion/rule-confirm-republish-error-action-console.png) 12. Choose the back arrow in the upper left of the console to return to the AWS IoT console
home.

After you set up the republish error action, you can view the error messages in the MQTT
test client in AWS IoT Core.

In the following procedure, you subscribe to the error topic in the MQTT test client. In the
MQTT test client, you can receive your rule's error messages to troubleshoot the issue.

###### To subscribe to the error action topic

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation page, choose **Test** to open the MQTT test
   client.
3. In the **Subscription topic** field, enter the error topic that you
   configured earlier (for example, `sitewise/windfarm/rule/error`) and
   choose **Subscribe to topic**.

![AWS IoT Core "MQTT client" page screenshot with the "Subscribe to topic" button highlighted.](images/rule-ingestion/troubleshoot-rule-subscribe-error-topic-console.png) 4. Watch for error messages to appear and then expand the `failures` array in any
error message.

Next, compare the error messages with the errors in this topic to troubleshoot your
issue.

## Troubleshoot rule issues

Use the following information to troubleshoot rule issues.

###### Issues

- [Error: Member must be within 604800 seconds
  before and 300 seconds after the current timestamp](#rule-error-timestamp-out-of-range "#rule-error-timestamp-out-of-range")
- [Error: Property value does not match data type
  <type>](#rule-error-invalid-data-type "#rule-error-invalid-data-type")
- [Error: User: <role-arn> is not authorized
  to perform: iotsitewise:BatchPutAssetPropertyValue on resource](#rule-error-role-not-authorized "#rule-error-role-not-authorized")
- [Error: iot.amazonaws.com is unable to
  perform: sts:AssumeRole on resource: <role-arn>](#rule-error-unable-to-assume-role "#rule-error-unable-to-assume-role")
- [Info: No requests were sent.
  PutAssetPropertyValueEntries was empty after performing substitution templates.](#rule-info-request-was-empty "#rule-info-request-was-empty")

### Error: Member must be within 604800 seconds

before and 300 seconds after the current timestamp

Your timestamp is older than 7 days or newer than 5 minutes, compared to current Unix epoch
time. Try the following:

- Check that your timestamp is in Unix epoch (UTC) time. If you provide a timestamp with a
  different timezone, you receive this error.
- Check that your timestamp is in seconds. AWS IoT SiteWise expects timestamps split into time in
  seconds (in Unix epoch time) and offset in nanoseconds.
- Check that you're uploading data that is timestamped no later than 7 days in the
  past.

### Error: Property value does not match data type

 <type>

An entry in your rule action has a different data type than the target asset property. For
example, your target asset property is a `DOUBLE` and your selected data type is
**Integer** or you passed the value in `integerValue`. Try the
following:

- If you configure the rule from the AWS IoT console, check that you chose the correct
  **Data type** for each entry.
- If you configure the rule from the API or AWS Command Line Interface (AWS CLI), check that your
  `value` object uses the correct type field (for example, `doubleValue`
  for a `DOUBLE` property).

### Error: User: <role-arn> is not authorized

to perform: iotsitewise:BatchPutAssetPropertyValue on resource

Your rule isn't authorized to access the target asset property, or the target asset
property doesn't exist. Try the following:

- Check that your property alias is correct and that you have an asset property with the
  given property alias. For more information, see [Manage data streams for AWS IoT SiteWise](manage-data-streams.md "manage-data-streams.md").
- Check that your rule has a role and that the role allows
  `iotsitewise:BatchPutAssetPropertyValue` permission to the targeted asset
  property, such as through the target asset's hierarchy. For more information, see [Grant AWS IoT the required access](grant-rule-access.md "grant-rule-access.md").

### Error: iot.amazonaws.com is unable to

perform: sts:AssumeRole on resource: <role-arn>

Your user isn't authorized to assume the role on your rule in AWS Identity and Access Management (IAM).

Check that your user is allowed `iam:PassRole` permission to the role on your
rule. For more information, see [Pass role permissions](../../../iot/latest/developerguide/pass-role.md "../../../iot/latest/developerguide/pass-role.md") in the
_AWS IoT Developer Guide_.

### Info: No requests were sent.

PutAssetPropertyValueEntries was empty after performing substitution templates.

###### Note

This message is an `INFO` level log.

Your request must have at least one entry with all of the required parameters.

Check that your rule's parameters, including substitution templates, result in non-empty
values. Substitution templates can't access values defined in `AS` clauses in your
rule query statement. For more information, see [Substitution templates](../../../iot/latest/developerguide/iot-substitution-templates.md "../../../iot/latest/developerguide/iot-substitution-templates.md")
in the _AWS IoT Developer Guide_.

## Troubleshoot a rule (AWS IoT SiteWise)

Follow the steps in this procedure to troubleshoot your rule if the CPU and memory usage
data isn't appearing in AWS IoT SiteWise as expected. In this procedure, you configure the republish
rule action as an error action to view error messages in the MQTT test client. You can also
configure logging to CloudWatch Logs to troubleshoot. For more information, see [Troubleshoot an AWS IoT SiteWise rule action](troubleshoot-rule.md "troubleshoot-rule.md").

###### To add a republish error action to a rule

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Message routing** and then
   choose **Rules**.
3. Choose the rule that you created earlier and choose **Edit**.
4. Under **Error action - _optional_**, choose
   **Add error action**.
5. Choose **Republish a message to an AWS IoT topic**.
6. In **Topic**, enter the path to your error (for example,
   `sitewise/rule/tutorial/error`). AWS IoT Core will republish error
   messages to this topic.
7. Choose the role that you created earlier (for example,
   **SiteWiseTutorialDeviceRuleRole**).
8. Choose **Update**.

After you set up the republish error action, you can view the error messages in the MQTT
test client in AWS IoT Core.

In the following procedure, you subscribe to the error topic in the MQTT test
client.

###### To subscribe to the error action topic

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation page, choose **MQTT test client** to open the
   MQTT test client.
3. In the **Topic filter** field, enter
   `sitewise/rule/tutorial/error` and choose
   **Subscribe**.

When error messages appear, view the `failures` array in any error message to
diagnose issues. For more information about possible issues and how to resolve them, see [Troubleshoot an AWS IoT SiteWise rule action](troubleshoot-rule.md "troubleshoot-rule.md").

If errors don't appear, check that your rule is enabled and that you subscribed to the
same topic that you configured in the republish error action. If errors still don't appear
after you do that, check that the device script is running and updating the device's shadow
successfully.

###### Note

You can also subscribe to your device's shadow update topic to view the payload that
your AWS IoT SiteWise action parses. To do so, subscribe to the following topic.

```
$aws/things/+/shadow/update/accepted
```

## Troubleshoot a rule (DynamoDB)

Follow the steps in this procedure to troubleshoot your rule if the demo asset data isn't
appearing in the DynamoDB table as expected. In this procedure, you configure the republish rule
action as an error action to view error messages in the MQTT test client. You can also
configure logging to CloudWatch Logs to troubleshoot. For more information, see [Monitoring with
CloudWatch Logs](../../../iot/latest/developerguide/cloud-watch-logs.md "../../../iot/latest/developerguide/cloud-watch-logs.md") in the _AWS IoT Developer Guide_.

###### To add a republish error action to a rule

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/").
2. In the left navigation pane, choose **Act** and then choose
   **Rules**.
3. Choose the rule that you created earlier.

![AWS IoT Core "Rules" page screenshot.](images/interact-dynamo-db/rule-choose-rule-console.png) 4. Under **Error action**, choose **Add
action**. 5. Choose **Republish a message to an AWS IoT topic**.

![AWS IoT Core "Select an action" page screenshot with the Republish action highlighted.](images/interact-dynamo-db/rule-choose-republish-action-console.png) 6. Choose **Configure action** at the bottom of the page. 7. In **Topic**, enter `windspeed/error`.
AWS IoT Core will republish error messages to this topic.

![AWS IoT Core "Configure Republish action" page screenshot with the "Topic" highlighted.](images/interact-dynamo-db/rule-configure-republish-action-console.png) 8. Choose **Select** to grant AWS IoT Core access to perform the error
action using the role that you created earlier. 9. Choose **Select** next to your role.

![AWS IoT Core "Configure Republish action" page screenshot with the role select button highlighted.](images/interact-dynamo-db/rule-select-role-console.png) 10. Choose **Update Role** to add the additional permissions to the
role.

![AWS IoT Core "Configure Republish action" page screenshot with the update role button highlighted.](images/interact-dynamo-db/rule-update-role-console.png) 11. Choose **Add action** to finish adding the error action. 12. Choose the back arrow in the upper left of the console to return to the AWS IoT Core
console home.

After you set up the republish error action, you can view the error messages in the MQTT
test client in AWS IoT Core.

In the following procedure, you subscribe to the error topic in the MQTT test
client.

###### To subscribe to the error action topic

1. In the AWS IoT Core console's left navigation page, choose
   **Test**.
2. In the **Subscription topic** field, enter
   `windspeed/error` and choose **Subscribe to
   topic**.

![AWS IoT Core "MQTT client" page screenshot with the "Subscribe to topic" button highlighted.](images/interact-dynamo-db/rule-subscribe-error-topic-console.png) 3. Watch for error messages to appear and explore the `failures` array in an
error message to diagnose the following common issues:

    * Typos in the rule query statement
    * Insufficient role permissions

If errors don't appear, check that your rule is enabled and that you subscribed to the
same topic that you configured in the republish error action. If errors still don't
appear, check that your demo wind farm assets still exist and that you enabled
notifications on the wind speed properties. If your demo assets expired and disappeared
from AWS IoT SiteWise, you can create a new demo and update the rule query statement to reflect the
updated asset model and property IDs.
