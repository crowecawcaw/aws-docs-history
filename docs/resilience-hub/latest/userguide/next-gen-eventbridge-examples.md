# Example event patterns and events

Event patterns have the same structure as the events that they match. The pattern quotes
the fields that you want to match and provides the values that you're looking for.

You can copy and paste event patterns from this section into EventBridge to create rules that
monitor events from the next generation of Resilience Hub.

###### Select all failure mode assessment completion events

The following pattern matches all completed assessments.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Completed"]
}
```

###### Select all failure mode assessment failure events

The following pattern matches all failed assessments.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Failed"]
}
```

###### Select all new dependency discovered events

The following pattern matches all new dependency events.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["New Dependency Discovered"]
}
```

###### Select all events from the next generation of Resilience Hub

The following pattern matches all events regardless of type.

```
{
  "source": ["aws.resiliencehub"]
}
```

###### Select assessment events with high-severity findings

The following pattern matches assessments that identified at least one high-severity finding.

```
{
  "source": ["aws.resiliencehub"],
  "detail-type": ["Failure Mode Assessment Completed"],
  "detail": {
    "highSeverityCount": [{"numeric": [">", 0]}]
  }
}
```

The following sections provide example events for each event type.
