# Troubleshooting Amazon EventBridge Scheduler

You can use the topics in this section to troubleshoot common Amazon EventBridge Scheduler issues.

###### Topics

- [My schedule fails with target errors](#troubleshooting-target-errors "#troubleshooting-target-errors")
- [Schedule execution role permissions issues](#troubleshooting-perms "#troubleshooting-perms")
- [Understanding and managing service quotas](#troubleshooting-quotas "#troubleshooting-quotas")
- [Schedule pattern and trigger timing issues](#troubleshooting-timing "#troubleshooting-timing")
- [Creating schedule patterns and cron expressions](#troubleshooting-patterns "#troubleshooting-patterns")
- [Is my target being triggered?](#troubleshooting-trigger-target "#troubleshooting-trigger-target")
- [Templated vs universal
  targets](#troubleshooting-temp-universal-target "#troubleshooting-temp-universal-target")
- [Schedule updates triggering unexpected invocations](#troubleshooting-temp-universal-target-invoke "#troubleshooting-temp-universal-target-invoke")
- [Disabling or enabling
  one-time schedules](#troubleshooting-temp-universal-target-enable "#troubleshooting-temp-universal-target-enable")

## My schedule fails with target errors

Target invocation failures are one of the most common issues with EventBridge Scheduler. These failures can occur for several reasons:

### Common causes:

- Missing or incorrect target parameters.
- Network connectivity problems.
- API throttling.
- Incorrect target configuration.

### Troubleshooting steps

1. **Set up a Dead-Letter Queue (DLQ)**
   - A DLQ helps you capture and analyze failed invocations.
   - Failed invocations are sent to the DLQ with detailed error messages.
   - To [configure a DLQ](configuring-schedule-dlq.md "configuring-schedule-dlq.md"), add it to your schedule configuration:

```

{
    "DeadLetterConfig": {
        "Arn": "arn:aws:sqs:region:account-id:MyDLQ"
    }
}

```

Note: If your DLQ is encrypted with a KMS key, ensure the key policy allows EventBridge Scheduler to use it:

```

{
    "Sid": "Allow EventBridge Scheduler to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "scheduler.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
    ],
    "Resource": "*"
}

```

2. **Verify API parameters**
   - Ensure all required parameters for your target API calls are present and correctly formatted.
   - Check that parameter values are within allowed ranges.
   - Verify that the API endpoint is accessible from your VPC if using VPC endpoints.

3. **Review network configuration**
   - If calls fail due to transient network issues, implement [retry](../APIReference/API_RetryPolicy.md "../APIReference/API_RetryPolicy.md") logic.
   - Example retry policy:

```

{
    "RetryPolicy": {
        "MaximumRetryAttempts": 3,
        "MaximumEventAgeInSeconds": 3600
    }
}

```

4. **Check target-specific configurations**
   - For templated targets (like ECS tasks), ensure you provide overrides through the `Target.Input` parameter of the schedule creation API.
   - Verify that your target service is [supported](managing-targets-templated.md "managing-targets-templated.md") and correctly configured.

## Schedule execution role permissions issues

IAM role permission issues are a common reason for schedule execution failures. Here's how to troubleshoot and resolve these issues:

### Common causes

- Missing required permissions for the target service
- Incorrect role configuration in the schedule
- Missing trust relationship with EventBridge Scheduler service
- Insufficient permissions for accessing encrypted resources

### Symptoms

- Increased `TargetErrorCount` metric in CloudWatch
- Schedules fail to execute without apparent issues in the schedule configuration

### Troubleshooting steps

1. **Monitor CloudWatch metrics**
   - Check the `TargetErrorCount` metric in CloudWatch.

2. **Use Dead-Letter Queue (DLQ) to confirm permission issues**
   - Configure a DLQ for your schedule.
   - If there are permission issues with your target, and the DLQ is properly configured, you'll see the failed invocations in the DLQ with permission-related error messages.
   - If the DLQ remains empty despite failed executions showing in CloudWatch metrics, this likely indicates a permissions issue preventing EventBridge Scheduler from writing to the DLQ itself.

###### Note

Ensure the DLQ itself has the correct permissions. If it's encrypted, make sure EventBridge Scheduler has permission to use the KMS key. 3. **Verify trust relationship**

    * Ensure your IAM role has the correct trust relationship with EventBridge Scheduler:

```

{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "scheduler.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
    }]
}

```

4. **Check schedule execution role permissions**
   - The schedule's execution role needs specific permissions to invoke different target types.
   - Example permissions to include in your schedule's execution role policy:

```

// For Lambda function targets - add to schedule execution role
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "lambda:InvokeFunction"
        ],
        "Resource": "arn:aws:lambda:region:account-id:function:function-name"
    }]
}

// For SQS queue targets - add to schedule execution role
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "sqs:SendMessage"
        ],
        "Resource": "arn:aws:sqs:region:account-id:queue-name"
    }]
}

```

5. **Check for encrypted resource access**
   - If your target uses encrypted resources (e.g., KMS-encrypted SQS queues), ensure your role has permissions to use the KMS key:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:region:account-id:key/key-id"
        }
    ]
}

```

6. **Verify role ARN configuration**
   - Ensure the role ARN in your schedule configuration is correct.
   - Verify the role exists in the same AWS account and region as your schedule.

## Understanding and managing service quotas

If you're experiencing issues creating schedules or seeing throttled invocations, you might be reaching service quota limits. EventBridge Scheduler has quotas for the number of schedules, schedule groups, and invocation rates, which can vary by region.

### Identifying quota issues

To determine if you're hitting quota limits:

1. **Monitor CloudWatch metrics**
   - Check the `InvocationThrottleCount` metric. An increase in this metric indicates you're exceeding your invocation rate limit.
   - Review the `InvocationAttemptCount` metric to understand your current usage.

2. **Watch for specific error messages**
   - When creating or modifying schedules, a `LimitExceededException` indicates you've reached the maximum number of schedules or schedule groups.
   - API calls returning throttling errors suggest you're exceeding the API request quota.

### Resolving quota issues

If you determine you're hitting quota limits:

1. Review and optimize your current schedules. Consider consolidating similar schedules or removing unused ones.
2. For API throttling, implement [retry with backoff](../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md "../../../prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.md") in your API calls.
3. If you need higher quotas, request an increase through the Service Quotas console. Select EventBridge Scheduler, choose the quota you need to increase, and submit a request with your business justification.

## Schedule pattern and trigger timing issues

Users sometimes encounter issues where schedules don't trigger at the expected times. This can most commonly be due to misunderstandings about schedule patterns, daylight saving time changes, or flexible time windows.

### Common causes

- Misinterpretation of cron expressions.
- Unexpected behavior during daylight saving time changes.
- Confusion about flexible time windows.
- Misunderstanding of rate expressions.

### Troubleshooting steps

1.  **Verify cron expressions**
    - Ensure your cron expression is correctly formatted.
    - Note that you can't specify both day-of-month and day-of-week fields simultaneously in a cron expression.

2.  **Time zone considerations**

        * Select your preferred time zone when creating the schedule.
        * Understand how daylight saving time affects your schedule as this adjustment is based on UTC.

    Example of daylight saving impact: If you configure a schedule to run at 7:00 AM GMT:

        * During winter: The schedule runs at 7:00 AM GMT (as GMT = UTC)
        * During summer: The schedule still runs at 7:00 AM UTC, which is now 6:00 AM GMT/BST

    If you need the schedule to run at the same local time year-round, make sure to select the appropriate time zone when creating the schedule and how daylight savings can affect that time zone.

3.  **Understand flexible time windows**
    - [Flexible time windows](managing-schedule-flexible-time-windows.md "managing-schedule-flexible-time-windows.md") allow EventBridge Scheduler to optimize invocations.
    - The schedule might not trigger exactly at the start of the window.
    - Monitor the actual invocation times to understand the behavior.

4.  **Review rate and cron expressions**

        * Ensure rate expressions are correctly formatted (e.g., `rate(5 minutes)`, `rate(1 hour)`).
        * For both rate and cron expressions, be aware that schedule invocations are not clamped to the 0th second of a minute.
        * Schedules may trigger within the minute specified, but not necessarily at the exact start of the minute.

    For example:

        * A schedule with `rate(1 hour)` might run at 2:00:45 PM, 3:00:32 PM, 4:00:18 PM, etc.
        * A cron schedule set for `0 * * * ? *` (every hour) might run at 2:00:15 PM, 3:00:07 PM, 4:00:52 PM, etc.

5.  **Monitor CloudWatch metrics**
    - Use the `InvocationAttemptCount` metric to verify if your schedule is triggering.
    - Check `TargetErrorCount` if invocations are failing.
    - If you have configured a Dead-Letter Queue, monitor `InvocationsSentToDeadLetterCount` to track failed invocations.

## Creating schedule patterns and cron expressions

Users often encounter issues when creating schedule patterns, particularly with cron expressions. Here are some common problems and how to address them:

### Common issues

- Incorrect cron syntax
- Attempting to use unsupported cron features
- Confusion about which fields can be used together

### Troubleshooting steps

1. **Review cron expression syntax**
   - Ensure your cron expression follows the correct [format](schedule-types.md#cron-based "schedule-types.md#cron-based"): `Minutes Hours Day-of-month Month Day-of-week Year`.
   - Remember that EventBridge Scheduler uses the cron standard with an additional Year field.

2. **Understand limitations**
   - You can't specify both the day-of-month and day-of-week fields simultaneously as discussed
     [here](../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions "../../../eventbridge/latest/userguide/eb-scheduled-rule-pattern.md#eb-cron-expressions").
   - Cron expressions that lead to rates faster than 1 minute are not supported.

3. **Use the schedule preview feature**
   - When creating or editing a schedule, EventBridge Scheduler provides a preview of the next 10 execution times.
   - Use this preview to verify that your schedule will run at the intended times.
   - If the preview doesn't match your expectations, review and adjust your cron expression.

## Is my target being triggered?

To confirm if your target is being triggered:

1. Check CloudWatch metrics:
   - `InvocationAttemptCount` shows the number of attempted invocations
   - `TargetErrorCount` indicates if any invocations failed
   - `TargetErrorThrottledCount` shows if your target is being throttled
   - `InvocationDroppedCount` indicates if any invocations were dropped

2. [Configure a Dead-Letter Queue](configuring-schedule-dlq.md "configuring-schedule-dlq.md") (DLQ) to capture and analyze any failed invocations.

## Templated vs universal

targets

If you receive an error like "Invalid request provided: [service] is not a supported service for a target", you may be trying to use an unsupported service as a templated target.

To resolve this:

1. Check if your desired service is supported as a [templated target](managing-targets-templated.md "managing-targets-templated.md").
2. If not supported, use a [universal target](managing-targets-universal.md "managing-targets-universal.md") instead and configure it to make the appropriate API call to your service.

## Schedule updates triggering unexpected invocations

When you make a change to a schedule, invocations might not immediately reflect the updated schedule. Allow a short period of time for changes to take effect. For example, if you update a schedule close to its original trigger time, you might see an invocation based on the original schedule configuration.

## Disabling or enabling

one-time schedules

When re-enabling a one-time schedule after its original scheduled time has passed, the schedule may immediately invoke its target. This can occur even if the schedule was disabled before its original execution time.

For example:

- Current time: 13:15 UTC
- One-time schedule created for: 13:30 UTC
- Schedule disabled before 13:30 UTC
- Schedule re-enabled at 14:00 UTC
- Result: The target may be invoked immediately upon re-enabling
