# Using Internet Monitor with Amazon EventBridge

Overall (global) health events that Internet Monitor creates for networking issues are published with Amazon EventBridge, so that you can send notifications about
 a degradation in end users' experience for your application due to a global health event.

###### Note

Local health events are not published with EventBridge.

To use EventBridge to work with Internet Monitor health events, follow the guidance here.

###### To set up a rule for Internet Monitor in EventBridge

1. In the AWS Management Console, in EventBridge, choose **Rules**, then enter a name and a description. Create the 
 rule on the **Default** event bus.
2. In Step 2, select **Other** for the event source, and then, under **Event pattern**, match the following
 source.



```
{
  "source": ["aws.internetmonitor"]
}
```
3. In Step 3, for the target, select **AWS Service** and **CloudWatch Logs Group**, then 
 select an existing log group or create a new one.
4. Add any desired tags, and then create the rule. This should populate your selected CloudWatch Logs Group with events from EventBridge.
For more information about how EventBridge rules work with event patterns, see [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html")
 in the Amazon EventBridge User Guide.
