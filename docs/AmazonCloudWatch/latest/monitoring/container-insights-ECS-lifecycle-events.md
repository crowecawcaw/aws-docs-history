# Viewing Amazon ECS lifecycle events
 within Container Insights

You can view Amazon ECS lifecycle events within the Container Insights console. This helps
 you correlate your container metrics, logs, and events in a single view to give you a more
 complete operational visibility.

The events include container instance state change events, task state change events, and
 service action events. They are automatically sent by Amazon ECS to Amazon EventBridge and are also
 collected in CloudWatch in event log format. For more information about these events, see [Amazon ECS
 events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html").

Standard Container Insights pricing applies for Amazon ECS Lifecycle events. For more
 information, see [Amazon CloudWatch
 Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To configure the table of lifecycle events and create rules for a cluster, you must have
 the `events:PutRule`, `events:PutTargets`, and
 `logs:CreateLogGroup` permissions. You must also make sure that there is a
 resource policy that enables EventBridge to create the log stream and send logs to CloudWatch Logs. If this
 resource policy doesn't exist, you can enter the following command to create it:


```
{
    "policyName": 'EventBridgeCloudWatchLogs',
    "policyDocument": {
       "Statement": [
           {
               "Action": [
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Effect": "Allow",
               "Principal": {
                   "Service": ["events.amazonaws.com", "delivery.logs.amazonaws.com"]
               },
               "Resource": "arn:aws:logs:region:account-id:log-group:/aws/events/ecs/containerinsights/*:*",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": "account-id"
                   },
                   "ArnLike": {
                       "aws:SourceArn": "arn:aws:events:region:account-id:rule/eventsToLog*"
                   }
               },
               "Sid": "TrustEventBridgeToStoreECSLifecycleLogEvents"
           }
       ],
       "Version": "2012-10-17"		 	 	 
    }
}
```
You can use the following command to check whether you already have this policy, and to
 confirm that attaching it worked correctly.


```
aws logs describe-resource-policies --region `region` --output json
```
To view the table of lifecycle events, you must have the
 `events:DescribeRule`, `events:ListTargetsByRule`, and
 `logs:DescribeLogGroups` permissions.

###### To view Amazon ECS lifecycle events in the CloudWatch Container Insights console

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Insights**, **Container
 Insights**.
3. Choose **View performance dashboards**.
4. In the next drop-down, choose either **ECS Clusters**,
 **ECS Services**, or **ECS Tasks**.
5. If you chose **ECS Services** or **ECS Tasks** in
 the previous step, choose the **Lifecycle events** tab.
6. At the bottom of the page, if you see **Configure lifecycle
 events**, choose it to create EventBridge rules for your cluster.


The events are displayed below the container insights panes and above the
 Application Insights section. To run extra analytics and create additional
 visualizations on these events, choose **View in Logs Insights** in the
 Lifecycle Events table.
