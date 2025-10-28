# Best practices for Amazon EventBridge event patterns

Below are some best practices to consider when defining event patterns in your event bus rules.

## Avoid writing infinite loops

In EventBridge, it is possible to create rules that lead to infinite loops, where a rule
is fired repeatedly. For example, a rule might detect that ACLs have changed on an S3 bucket,
and trigger software to change them to the desired state. If the rule is not written
carefully, the subsequent change to the ACLs fires the rule again, creating an infinite
loop.

To prevent these issues, write the event patterns for your rules to be as precise as possible,
so they only match the events you actually want sent to the target.
In the above example, you would create an event pattern to match events so that the triggered actions do not re-fire the same
rule. For example, create an event pattern in your rule that would match events only if ACLs are found to be in a bad state, instead
of after any change. For more information, see [Make event patterns precise as possible](#eb-patterns-best-practices-precision "#eb-patterns-best-practices-precision") and [Scope your event patterns
to account for event source updates](#eb-patterns-best-practices-future-proof "#eb-patterns-best-practices-future-proof").

An infinite loop can quickly cause higher than expected charges. It can also lead to throttling and delayed event delivery.
You can monitor the upper bound of your invocation rates to be warned about unexpected spikes in volume.

Use budgeting to alert you when charges exceed your specified limit. For more
information, see [Managing Your
Costs with Budgets](../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md "../../../awsaccountbilling/latest/aboutv2/budgets-managing-costs.md").

## Make event patterns precise as possible

The more precise your event pattern, the more likely it will match only the events
you actually want it to, and avoid unexpected matches when new events are added to an event source, or existing events are updated to include new properties.

Event patterns can include filters that match on:

- Event metadata about the event, such as `source`, `detail-type`. `account`, or `region`.
- Event data, this is, the fields inside the `detail` object.
- Event content, or the actual values of the fields inside the `detail` object.

Most patterns are simple, such as specifying only `source` and
`detail-type` filters. However, EventBridge patterns include the flexibility to
filter on any key or value of the event. In addition, you can apply content filters such
as `prefix` and `suffix` filters to improve the precision of your
patterns. For more information, see [Using comparison operators in Amazon EventBridge event patterns](eb-create-pattern.md#eb-event-patterns-content-based-filtering "eb-create-pattern.md#eb-event-patterns-content-based-filtering").

### Specify event source and detail type as filters

You can reduce generating infinite loops and matching undesired events by making your event patterns more precise using the `source` and `detail-type` metadata fields.

When you need to match specific values within two or more fields,
use the `$or` comparison operator, rather than listing all possible values within a single array of values.

For events that are delivered through AWS CloudTrail, we recommend you use the `eventName` field as a filter.

The following event pattern example matches `CreateQueue` or `SetQueueAttributes` from the Amazon Simple Queue Service service, or `CreateKey` or `DisableKeyRotation` events from the AWS Key Management Service service.

```
{
  "detail-type": ["AWS API Call via CloudTrail"],
  "$or": [{
      "source": [
        "aws.sqs"
        ],
      "detail": {
        "eventName": [
          "CreateQueue",
          "SetQueueAttributes"
        ]
      }
    },
    {
      "source": [
        "aws.kms"
        ],
      "detail": {
        "eventName": [
          "CreateKey",
          "DisableKeyRotation"
        ]
      }
    }
  ]
}
```

### Specify account and region as filters

Including `account` and `region` fields in your event
pattern helps limit cross-account or cross-region event matching.

### Specify content filters

Content-based filtering can help improve event pattern precision, while still keeping the length of the event pattern to a minimum.
For example, matching based on a numeric range can be helpful instead of listing all possible numeric values.

For more information, see [Using comparison operators in Amazon EventBridge event patterns](eb-create-pattern.md#eb-event-patterns-content-based-filtering "eb-create-pattern.md#eb-event-patterns-content-based-filtering").

## Scope your event patterns

to account for event source updates

When creating event patterns, you should take into account that event schemas and
event domains may evolve and expand over time. Here again, making your event patterns as
precise as possible helps you limit unexpected matches if the event source changes or
expands.

For example, suppose you are matching against events from a new micro-service that publishes payment-related events.
Initially, the service uses the domain `acme.payments`, and publishes a single event, `Payment accepted`:

```
{
  "detail-type": "Payment accepted",
  "source": "acme.payments",
  "detail": {
    "type": "`credit`",
    "amount": "`100`",
    "date": "`2023-06-10`",
    "currency": "`USD`"
    }
  }
}
```

At this point, you could create a simple event pattern that matches Payment accepted events:

```
{ “source” : “acme.payments” }
```

However, suppose the service later introduces a new event for rejected payments:

```
{
  "detail-type": "Payment rejected",
  "source": "acme.payments",
  "detail": {
  }
}
```

In this case, the simple event pattern you created will now match against both `Payment accepted` and `Payment rejected` events.
EventBridge routes both types of events to the specified target for processing,
possibly introducing processing failures and additional processing cost.

To scope your event pattern to only `Payment accepted` events, you'd want to specify both `source` and `detail-type`,
at a minimum:

```
{
  "detail-type": "Payment accepted",
  "source": "acme.payments"
  }
}
```

You can also specify account and Region in your event pattern, to further limit
when cross-account or cross-Region events match this rule.

```
{
  "account": "`012345678910`",
  "source": "acme.payments",
  "region": "`AWS-Region`",
  "detail-type": "Payment accepted"
}
```

## Validate event patterns

To ensure rules match the desired events, we strongly recommend you validate your event patterns. You can validate your event patterns using the EventBridge console or API:

- In the EventBridge console, you can create and test event patterns [as part of creating a rule](eb-create-rule.md "eb-create-rule.md"), or separately by [using the Sandbox](eb-event-pattern-sandbox.md "eb-event-pattern-sandbox.md").
- You can test your event patterns in the AWS CLI using the [test-event-pattern](../../../cli/latest/reference/events/test-event-pattern.md "../../../cli/latest/reference/events/test-event-pattern.md") command.
