# Troubleshooting quotas in EventBridge Scheduler

Use the following information to help you diagnose and fix common issues that you might encounter concerning EventBridge Scheduler quotas.

## ServiceQuotaExceededException

I am receiving throttling errors on `CreateSchedule`, `DeleteSchedule`, `GetSchedule`, or
`UpdateSchedule` request rate, even though I am below the default rate limit.

### Common cause

On September 7, 2023, EventBridge Scheduler began supporting the ScheduleGroup ARN (Amazon Resource Name) instead of the Schedule ARN in execution role trust policies. Customers allowlisted to continue using Schedule ARNs in their trust policy may have limits of 50 TPS, instead of the default limits of 250 to 1000 TPS (dependent on region).

### Resolution

Contact [support](https://console.aws.amazon.com/support/home?#/case/create?issueType=technical "https://console.aws.amazon.com/support/home?#/case/create?issueType=technical") to request a higher maximum limit.

### Prevention

Modify your existing trust policies in one of the following way:

- Removing all scoping from the role.
- Scoping the role so that it may be assumed using the Schedule ARN or the ScheduleGroup ARN.

For example, suppose you had the following existing trust policy:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "scheduler.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
        "StringEquals": {
            "aws:SourceArn": "arn:aws:scheduler:`region`:`account`:schedule/`schedule_group`/`schedule`"
        }
    }
}
```

You could update the trust policy to the following:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "scheduler.amazonaws.com"
    },
    "Action": "sts:AssumeRole",
    "Condition": {
        "ForAnyValue:StringEquals": {
            "aws:SourceArn": [
                "arn:aws:scheduler:`region`:`account`:schedule/`schedule_group`/`schedule`",
                "arn:aws:scheduler:`region`:`account`:schedule-group/`schedule_group`"
            ]
        }
    }
}
```

## ThrottlingException on a single schedule

I am receiving `ThrottlingException` errors when calling `CreateSchedule`,
`UpdateSchedule`, `GetSchedule`, or `DeleteSchedule` on a single schedule.
My account is below the per-account request rate quota for that operation.

### Common cause

In addition to per-account request rate quotas, EventBridge Scheduler limits the rate at which a single schedule can be
read or written. This per-schedule limit is 10 TPS. The limit can be lower depending on the size of the
schedule's target `Input` parameter. This limit is not adjustable through the Service
Quotas console.

You are likely encountering this because your application repeatedly reads, creates, updates, or deletes
the same schedule at a high rate.

### Resolution

Distribute requests across multiple schedules instead of concentrating mutations on a single
schedule.

### Prevention

- Avoid concentrating rapid mutations on a single schedule. If you need to change an existing
  schedule, call `UpdateSchedule` rather than deleting and recreating it.
- To have EventBridge Scheduler delete a schedule automatically after its last invocation, set
  `ActionAfterCompletion` to `DELETE`. For recurring schedules, this requires an
  `EndDate`. For more information, see [Deleting a schedule in EventBridge Scheduler](managing-schedule-delete.md "managing-schedule-delete.md").
