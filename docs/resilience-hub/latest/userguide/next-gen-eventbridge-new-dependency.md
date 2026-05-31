# Alert on new dependencies

The following command creates an EventBridge rule that fires whenever Next generation Resilience Hub discovers
a new dependency. This is particularly useful for critical services where unexpected new
dependencies should be reviewed immediately.

```

aws events put-rule \
  --name "ResilienceHub-NewDependency" \
  --event-pattern '{
    "source": ["aws.resiliencehub"],
    "detail-type": ["New Dependency Discovered"]
  }'
```
