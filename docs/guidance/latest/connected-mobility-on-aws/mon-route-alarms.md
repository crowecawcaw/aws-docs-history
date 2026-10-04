

# Route the alarms to a person
<a name="mon-route-alarms"></a>

The stream processing stack accepts an email address and subscribes it for you. Set it before deploying:

```
export FLINK_ALARM_EMAIL=oncall@example.com
```

The address is read at synthesis time and subscribed to the Flink alarms topic. Confirm the subscription from the email Amazon SNS sends; an unconfirmed subscription delivers nothing.

The simulation, manifest and security operators topics have no equivalent and must be subscribed after deploying. List the topics and subscribe each one:

```
aws sns list-topics \
  --query "Topics[?contains(TopicArn, 'cms-<stage>')].TopicArn" \
  --output text

aws sns subscribe \
  --topic-arn <topic-arn> \
  --protocol email \
  --notification-endpoint oncall@example.com
```

For anything beyond evaluation, prefer a destination that escalates — a chat channel or an on-call system — over a mailbox. The failures these alarms cover are the kind nobody notices from the application: telemetry keeps arriving, the console keeps reporting `RUNNING`, and the only symptom is that trips and alerts stop appearing.

## An alarm can go quiet while reporting OK
<a name="mon-alarm-goes-quiet"></a>

A CloudWatch alarm evaluates a metric. If the metric stops being published — because a log filter pattern no longer matches, a metric name was renamed, or the code path that emitted it was removed — the alarm does not fail. It sits in whatever state it last reached, usually `OK`, indefinitely.

This Guidance guards one instance of that directly: the sign-up denial alarm depends on a token appearing in the trigger’s log output, and that token’s value and shape are pinned by a unit test, because if it drifts the alarm goes quiet while continuing to report healthy. Apply the same caution to any alarm you add on a metric filter, and prefer metrics that emit an explicit zero over metrics that emit nothing, so the alarm always has data to evaluate.

When reviewing this platform’s health, treat "no alarms have fired" as a claim to verify rather than a conclusion. Check that the metric behind a critical alarm has recent datapoints.