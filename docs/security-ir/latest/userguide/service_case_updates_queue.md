# Alternate rule: Security Incident Response Case Updates

To create an event rule that monitors for all case updates, repeat these tutorials with the following alterations:

1. **In [Tutorial: Create and subscribe to an Amazon SNS topic](service_sns_create_topic.md "service_sns_create_topic.md")**, use `CaseUpdates` as the topic name.
2. **In [Tutorial: Register an event rule](service_sns_reg_rule.md "service_sns_reg_rule.md")**, use the following pattern in the JSON editor:

```

                           {
                             "source": ["aws.security-ir"],
                             "detail-type": [
                               "Case Created",
                               "Case Updated",
                               "Case Closed",
                               "Case Comment Created",
                               "Case Comment Updated"
                             ]
                           }

```
