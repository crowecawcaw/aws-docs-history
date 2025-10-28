# Troubleshoot monitoring and alerting issues

This section provides information about troubleshooting monitoring and alerting issues with AWS Transfer Family, including missing or incomplete CloudWatch metrics and missing EventBridge events.

###### Topics

- [Troubleshoot missing or incomplete CloudWatch metrics](#missing-cloudwatch-metrics "#missing-cloudwatch-metrics")
- [Troubleshoot missing EventBridge
  events](#eventbridge-event-issues "#eventbridge-event-issues")

## Troubleshoot missing or incomplete CloudWatch metrics

Description

CloudWatch metrics for your Transfer Family servers are missing, incomplete, or not updating as expected.

Cause

Missing or incomplete metrics can be caused by several factors:

- Logging configuration issues
- Low activity levels that don't generate metrics within the expected timeframe
- Viewing metrics with incorrect dimensions or time ranges

Solution

###### To resolve issues with missing or incomplete CloudWatch metrics:

1. Ensure that logging is properly configured for your Transfer Familyserver:
   - In the Transfer Family console, check that logging is enabled under **Server details > Additional details > Logging role**.
   - Very that the logging role has the necessary permissions and trust relationships.

2. When viewing metrics in the CloudWatch console:
   - Use the correct dimensions, for example **ServerId** for server-level metrics
   - Adjust the time range to ensure it covers periods of activity
   - Check that you're in the correct AWS Region

3. Generate test activity on your Transfer Family server to ensure metrics are being produced.

## Troubleshoot missing EventBridge

events

Description

You've configured Amazon EventBridge rules to capture Transfer Family events, but events are not being
delivered to your target destinations or triggering expected actions.

Cause

Missing EventBridge events can be caused by:

- Incorrectly configured event patterns
- Permission issues with event targets
- Service limits or throttling
- Events not being generated due to server configuration

Solution

To troubleshoot missing EventBridge events:

1. Verify your event pattern is correctly formatted to match Transfer Family
   events:

```
{
  "source": ["aws.transfer"],
  "detail-type": ["Transfer State Change"],
  "detail": {
    "serverId": ["s-1234567890abcdef0"]
  }
}
```

2. Check that your event target has the necessary permissions:
   - For Lambda targets, ensure the Lambda function's resource policy
     allows EventBridge to invoke it
   - For SQS targets, verify the queue policy allows EventBridge to send
     messages
   - For SNS targets, confirm the topic policy permits EventBridge to publish
     to it

3. Test your rule by generating sample events:
   - Use the EventBridge console to create a test event that matches your
     pattern
   - Perform actions on your Transfer Family server that should generate
     events

4. Enable EventBridge rule metrics to monitor rule invocations and failures:

```
aws events put-rule --name "TransferStateChangeRule" --event-pattern '{...}' --state ENABLED --metrics-enabled
```

5. Check CloudWatch Logs for any error messages related to event delivery
   failures
