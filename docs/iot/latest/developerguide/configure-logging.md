# Configure AWS IoT logging

You must enable logging by using the AWS IoT console, CLI, or API before you can monitor
and log AWS IoT activity. You can configure logging for AWS IoT at three levels: account-level,
event-level or resource-specific level. Event-level and resource-specific logging are
available exclusively with V2 logging. Customers using V1 logging must perform a migration
to V2 to access these features. See [details](configure-logging.md#migration-v1-v2 "configure-logging.md#migration-v1-v2").

When considering how to configure your AWS IoT logging, the account-level logging configuration
determines how AWS IoT activity will be logged unless specified otherwise. Starting out, you might
want to obtain detailed logs with a default [log level](configure-logging.md#log-level "configure-logging.md#log-level") of INFO
or DEBUG. After reviewing the initial logs, you can change the default log level to a less verbose
level such as WARN or ERROR at account or event level and set a more verbose resource-specific log
level on resources that might need more attention. Log levels can be changed whenever you want.

This topic covers cloud-side logging in AWS IoT. For information on device-side logging and
monitoring, see [Upload device-side
logs to CloudWatch](upload-device-logs-to-cloudwatch.md "upload-device-logs-to-cloudwatch.md").

For information on logging and monitoring AWS IoT Greengrass, see [Logging and monitoring in
AWS IoT Greengrass](../../../greengrass/v2/developerguide/logging-and-monitoring.md "../../../greengrass/v2/developerguide/logging-and-monitoring.md").

## Configuring V2 logging in AWS IoT

### Determing your logging version

The [GetV2LoggingOptions API](../apireference/API_GetV2LoggingOptions.md "../apireference/API_GetV2LoggingOptions.md") returns
a NotConfiguredException if V2 logging is not enabled. This error occurs when either V1 logging is in
use, or no logging has been configured.

### Understanding V2 logging features

V2 logging provides two key capabilities: event-level logging and resource-specific logging. Event-level
logging enables targeted logging configuration with customizable log levels and CloudWatch log group destinations.
Resource-specific logging allows you to filter logs by thing group, source IP, client ID, or principal ID.
Together, these features provide granular control and comprehensive visibility into IoT operations, improving
log searchability and reducing costs by eliminating unnecessary logging activity.

### Migrating from V1 to V2

You can migrate to V2 logging using the SetV2LoggingOptions API through either the AWS [CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-options.html")
or SDK. After migration, AWS IoT automatically routes all logs to the CloudWatch log group 'AWSIotLogsV2'. Important: If your
downstream applications or resources consume information from ‘AWSIotLogs’, update them to use the corresponding log
group path.

## Configure logging role and

policy

Before you can enable logging in AWS IoT, you must create an IAM role and a policy that gives AWS IoT permission
to write AWS IoT log activities to CloudWatch log groups on your behalf. You can also generate an IAM role with the policies
needed in the [Logs section of the AWS IoT console](https://console.aws.amazon.com/iot/home#/settings/logging "https://console.aws.amazon.com/iot/home#/settings/logging").

###### Note

Before enabling AWS IoT logging, ensure you understand the CloudWatch Logs access
permissions. Users with access to CloudWatch Logs can see debugging information from your devices.
For more information, see [Authentication and Access Control for Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").

If you expect high traffic patterns in AWS IoT Core due to load testing, consider disabling
IoT logging to prevent throttling. If high traffic is detected, our service may
disable logging in your account.

The following shows how to create a logging role and policy for AWS IoT Core resources.

### Create a logging role

To create a logging role, open the [Roles hub of the IAM console](https://console.aws.amazon.com/iam/home#/roles "https://console.aws.amazon.com/iam/home#/roles") and choose **Create
role**.

1. Under **Select trusted entity**, choose **AWS
   Service**. Then choose **IoT** under **Use
   case**. If you don't see **IoT**, enter and search
   **IoT** from the **Use cases for other AWS
   services:** drop-down menu. Select **Next**.
2. On the **Add permissions** page, you will see the policies that
   are automatically attached to the service role. Choose
   **Next**.
3. On the **Name, review, and create** page, enter a **Role
   name** and **Role description** for the role, then choose
   **Create role**.

### Logging role policy

The following policy documents provide the role policy and trust policy that allow
AWS IoT to submit log entries to CloudWatch on your behalf. If you configure event-level logging
with a custom CloudWatch log group, you must update the role policy to include the custom
resource ARN.

If you also allowed AWS IoT Core for LoRaWAN to submit log entries, you'll see a policy document
created for you that logs both activities.

###### Note

These documents were created for you when you created the logging role. The
documents have variables, ``${partition}`,` 
``${region}``, and
 ``${accountId}``, that you must replace with
your values.

- Replace partition with the partition of the region.
- Replace region with the AWS Region that you use. Make sure that you use the same
  AWS Region that you used to configure the AWS CLI on your device.
- Replace account-id with your AWS account ID.

Role policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:PutMetricFilter",
 "logs:PutRetentionPolicy",
 "iot:GetLoggingOptions",
 "iot:SetLoggingOptions",
 "iot:SetV2LoggingOptions",
 "iot:GetV2LoggingOptions",
 "iot:SetV2LoggingLevel",
 "iot:ListV2LoggingLevels",
 "iot:DeleteV2LoggingLevel"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:123456789012:log-group:AWSIotLogsV2:*"
 ]
 }
 ]
}`

```

Trust policy to log only AWS IoT Core activity:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "iot.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

AWS IoT Logging may fail to publish logging to CloudWatch Logs due to insufficient IAM role permissions. When this occurs, check [CloudWatch logging metrics](metrics_dimensions.md#logging-metrics "metrics_dimensions.md#logging-metrics") to investigate and troubleshoot the failures.

## Configure logging in the AWS IoT (console)

This section describes how to configure AWS IoT logging using the AWS IoT console. You can
set-up account-level, event-level and resource-specific logging.

###### To configure AWS IoT logging:

1. Sign in to the AWS IoT console. For more information, see [Open the AWS IoT console](setting-up.md#iot-console-signin "setting-up.md#iot-console-signin").
2. In the left navigation pane, choose **Logs** (previously a section
   under Settings).
3. Configure account-level logging: account level logging applies to all your AWS IoT fleet
   (devices or endpoints), unless overridden by event-level or resource-specific settings.
   1. Under Account-level logging, select **Manage account-level logging** to
      make updates.
   2. Select the "Enable logging" checkbox to start sending logs to CloudWatch. When “Enable logging”
      is unchecked, AWS IoT will not send any logs to CloudWatch log groups, regardless of event-level or
      resource-level logging configurations.
   3. Under **IAM log role**, select an existing role from the dropdown list.
      You can **View role details** to inspect role permissions. Alternatively, select
      **Create new role** to set up a new IAM role. The logging role provides policies
      that allow AWS IoT to submit log entries to CloudWatch on your behalf. If you configure event-level logging
      with a custom CloudWatch log group, you must update the role policy to include the ARN for this log group.
   4. Choose the **Default Log level** that corresponds to the [level of detail](configure-logging.md#log-level "configure-logging.md#log-level") of the log
      entries that you want to appear in the CloudWatch Logs. Note: Log level “DEBUG” provides the most detail but
      increases CloudWatch costs. CloudWatch log group destinations cannot be configured at the account level. However,
      you can specify custom log groups for individual event types as described in the following section.
   5. Choose **Update logging** to save your changes.

4. Event-level logging allows you to selectively capture logs for relevant events and direct them to
   dedicated CloudWatch log groups. This gives you the flexibility to organize logs by use cases for better
   discoverability, share them with different audiences, and reduce CloudWatch costs by enabling logs and setting
   log levels based on event criticality.

Configure **event-level logging**: event-level
logging captures specific AWS IoT events, such as client authentication attempts. These settings override
Account-Level Logging.

    1. Under **Event-level logging** section, select **Manage event-level logging**
     to make updates.
    2. By default, event types inherit the account-level logging configuration. Note: When resource-specific logging
     is configured, it overrides account and event-level settings.
    3. To modify settings for individual events, click the value in the corresponding event row. You can adjust both
     the log level and the CloudWatch log group destination. When specifying a custom CloudWatch log group destination, you must
     verify that the IAM role policy includes permissions for the new log group. Failure to update the role policy
     will prevent AWS IoT from writing logs to the custom log group. After making your selection, click the check mark
     to confirm your choice. The **'Is Modified'** column will display 'Yes' to indicate pending changes.
    4. Click on **Update Logging** to apply your changes or choose **Cancel** to discard.

5. Configure Resource-specific overrides: Resource-specific overrides apply a logging setting to selected resources.
   A resource can be a thing group, source IP, client ID, or principal ID. Resource-specific logging configuration
   overrides both account-level and event-level settings. When enabled, it generates logs for all event types at the
   configured logging level for the specified resources. For example, you can set debug-level logging for a specific
   Thing while keeping info-level logging for all other Things.
   1. Select **Add resource-specific overrides** in the Resource-specific overrides section.
   2. Choose a log target: Thing group, Source IP, Client ID or Principal ID.
   3. Enter the corresponding log target value for your selected target type.
   4. Select the desired log level from the dropdown menu in the Resource-specific log level section.
   5. Click **Submit** to add the override or **Cancel** to discard changes.
   6. To modify an existing resource-specific override, select the checkbox next to the resource and click “Remove”
      to delete the override or “Edit” to modify.

After you've enabled logging, visit [Viewing AWS IoT logs in the CloudWatch console](cloud-watch-logs.md#viewing-logs "cloud-watch-logs.md#viewing-logs") to learn more about viewing the log entries.

## Configure Account and Event-level logging in AWS IoT (CLI)

This section describes how to configure global logging for AWS IoT by using the
CLI.

You can optionally configure Event-level logging. Event-level logging captures logging information
at the event level, such as authentication and authorization or certificate creation events. You can
customize both the log level and the CloudWatch log group destinations at the event level. Event-level logging
operates at a more targeted level compared with account-level logging and therefore overrides the
account-level logging settings. This hierarchical approach allows you to maintain different logging
strategies for different types of events based on their operational importance and cost considerations.

###### Note

You need the Amazon Resource Name (ARN) of the role that you want to use. If you need
to create a role to use for logging, see [Create a logging role](#create-logging-role "#create-logging-role") before continuing. When specifying a custom CloudWatch
log group for any event type, ensure your logging role has the required permissions for
the target log group.

The principal used to call the API must have [Passing role permissions](pass-role.md "pass-role.md") for your logging role.

You can also perform this procedure with the API by using the methods in the AWS API that correspond
to the CLI commands shown here.

###### To use the CLI to configure default logging for AWS IoT

1. Use the [**set-v2-logging-options**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-options.html") command to set the logging options for your account.

```
aws iot set-v2-logging-options \
    --event-configurations `event-configuration-list` \
    --role-arn `logging-role-arn` \
    --default-log-level `log-level`
```

where:

**--role-arn**

The role ARN that grants AWS IoT permission to write to your logs in CloudWatch Logs.
Role-arn configuration is required for initial setup.

**--default-log-level**

The [log level](#log-level "#log-level") to
use. Valid values are: `ERROR`, `WARN`, `INFO`,
`DEBUG`, or `DISABLED`. Default-log-level configuration
is required for initial setup.

**--no-disable-all-logs**

An optional parameter that enables all AWS IoT logging. Use this parameter to
enable logging when it is currently disabled.

**--disable-all-logs**

An optional parameter that disables all AWS IoT logging. Use this parameter to
disable logging when it is currently enabled.

**--event-configurations**

This parameter is optional and allows you to customize logging settings for individual
event types:

    * eventType: The type of event that overrides the account-level setting
    * logLevel: Override the account-level setting with DEBUG, INFO, ERROR, WARN, or DISABLED
    * logDestination: Specify a custom CloudWatch log group for log delivery

You can configure logging level and log destination independently for each event type.
If not specified, events will inherit the account-level settings

```
aws iot set-v2-logging-options \
    --event-configurations "[{\"eventType\":\"Publish-In\",\"logLevel\":\"INFO\",\"logDestination\":\"examplePublishInLogGroup\"}]"
```

2. Use the [**get-v2-logging-options**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-v2-logging-options.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-v2-logging-options.html") command to get your current
   logging options.

```
aws iot get-v2-logging-options \
    --verbose
```

where:

**--verbose**

An optional parameter that enables you to retrieve all eventTypes and their configurations.

After you've enabled logging, visit [Viewing AWS IoT logs in the CloudWatch console](cloud-watch-logs.md#viewing-logs "cloud-watch-logs.md#viewing-logs") to learn more about viewing the log entries.

###### Note

AWS IoT continues to support older commands (**set-logging-options** and
**get-logging-options**) to set and get global logging on your account.
Be aware that when these commands are used, the resulting logs contain plain-text, rather
than JSON payloads and logging latency is generally higher. No further improvements will
be made to the implementation of these older commands. We recommend that you use the
["v2" versions](configure-logging.md#migration-v1-v2 "configure-logging.md#migration-v1-v2")
to configure your logging options and, when possible, change legacy applications that use
the older versions.

## Configure Resource-specific overrides in AWS IoT (CLI)

This section describes how to configure Resource-specific overrides for AWS IoT by using
the CLI. Resource-specific overrides allows you to specify a logging level for a specific
resource identified by Thing Group, Client ID, Source IP, or Principal ID. When resource-specific
logging is enabled, it overrides both account-level and event-level settings. All event types
will generate logs for the specified resource at the configured logging level, even if those
events are disabled in the event-level configurations.

Thing groups can contain other thing groups to create a hierarchical relationship. This
procedure describes how to configure the logging of a single thing group. You can apply this
procedure to the parent thing group in a hierarchy to configure the logging for all thing
groups in the hierarchy. You can also apply this procedure to a child thing group to
override the logging configuration of its parent.

A thing can be a member of a thing group. This membership allows the thing to inherit
configurations, policies, and settings applied to the thing group. Thing groups are used to
manage and apply settings to multiple things collectively, rather than dealing with each
thing individually. When your client ID matches the thing name, AWS IoT Core will automatically
associate the client session with the corresponding thing resource. This allows the client
session to inherit the configurations and settings applied to the thing groups to which the
thing belongs, including the logging levels. If your client ID doesn't match the thing
name, you can enable the exclusive thing attachment to establish the association. For more
information, see [Associating an AWS IoT thing to an MQTT client
connection](exclusive-thing.md "exclusive-thing.md")
.

In addition to thing groups, you can also log targets such as a device's client ID,
source IP, and principal ID.

###### Note

You need the Amazon Resource Name (ARN) of the role you want to use. If you need to
create a role to use for logging, see [Create a logging role](#create-logging-role "#create-logging-role")
before continuing.

The principal used to call the API must have [Passing role permissions](pass-role.md "pass-role.md")
for your logging role.

You can also perform this procedure with the API by using the methods in the AWS API
that correspond to the CLI commands shown here.

###### To use the CLI to configure Resource-specific overrides for AWS IoT

1. Enable account-level logging before configuring resource-specific logging using the
   following command: aws iot set-v2-logging-options command
2. Use the [**set-v2-logging-level**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-level.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-level.html") command to configure Resource-specific
   overrides. See the following example for thing group configuration:

```
aws iot set-v2-logging-level \
              --log-target targetType=THING_GROUP,targetName=`thing_group_name` \
              --log-level `log_level`
```

**--log-target**

The type and name of the resource for which you are configuring logging. The
`targetType` value must be one of: `THING_GROUP` |
`CLIENT_ID` | `SOURCE_IP` | `PRINCIPAL_ID`. The
log-target parameter value can be text, as shown in the preceding command example,
or a JSON string, such as the following example.

```
aws iot set-v2-logging-level \
              --log-target '{"targetType": "THING_GROUP","targetName": "`thing_group_name`"}' \
              --log-level `log_level`
```

**--log-level**

The logging level used when generating logs for the specified resource. Valid
values are: **DEBUG**, **INFO**,
**ERROR**, **WARN**, and
**DISABLED**. 3. Use the [**list-v2-logging-levels**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html") command to list the currently
configured logging levels.

```
aws iot list-v2-logging-levels
```

4. Use the [**delete-v2-logging-level**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html") command to delete a
   resource-specific logging level, such as the following examples.

```
aws iot delete-v2-logging-level \
              --target-type "THING_GROUP" \
              --target-name "`thing_group_name`"
```

```
aws iot delete-v2-logging-level \
              --target-type=CLIENT_ID
              --target-name=`ClientId1`
```

**--target-type**

The `target-type` value must be one of: `THING_GROUP` |
`CLIENT_ID` | `SOURCE_IP` |
`PRINCIPAL_ID`.

**--target-name**

The name of the thing group for which to remove the logging level.

## Log levels

These log levels determine the events that are logged and apply to default and
resource-specific log levels.

ERROR

Any error that causes an operation to fail.

Example: failed to authenticate device due to expired certificate.

Logs include ERROR information only.

WARN

Anything that can potentially cause inconsistencies in the system, but might not
cause the operation to fail.

Example: approaching message rate limit.

Logs include ERROR and WARN information.

INFO

High-level information about the flow of things.

Example: a client has successfully subscribed to an MQTT topic.

Logs include INFO, ERROR, and WARN information.

DEBUG

Information that might be helpful when debugging a problem.

Example: IoT Rules Engine detected a message published to the rules topic “rule/test”
and successfully started executing. The rule is configured with RepublishAction.

Logs include DEBUG, INFO, ERROR, and WARN information.

DISABLED

All logging is disabled.
