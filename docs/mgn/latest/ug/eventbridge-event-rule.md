NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Registering event rules

You create CloudWatch Events event rules that capture events coming from your
Application Migration Service resources.

###### Note

When you use the AWS Management Console to create an event rule, the console automatically
adds the IAM permissions necessary to grant Amazon CloudWatch Events permissions
to call your desired target type. If you are creating an event rule using the AWS CLI, you
must grant permissions explicitly. For more information, see [Events and Event Patterns](../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.md "../../../AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.md") in the Amazon CloudWatch User Guide.

To create your CloudWatch Events rules:

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. On the navigation pane, choose **Events, Create
   rule**.
3. For **Event source**, select **Event Pattern** as the event source, and then select **Build custom event pattern**.
4. Paste one following event pattern into the text area, depending on the event rule
   you wish to create:
   1. To catch all MGN events:

   ```
   {
     "source": ["aws.mgn"]
   }
   ```

   2. To catch all Lifecycle state changes:

   ```
   {
     "detail-type": ["MGN Source Server Lifecycle State Change"],
     "source": ["aws.mgn"]
   }
   ```

   3. To catch all events relating to a given source server:

   ```
   {
     "source": ["aws.mgn"],
     "resources": [
       "arn:aws:mgn:us-west-2:111122223333:source-server/s-12345678901234567"
     ]
   }
   ```

5. For **Targets**, choose **Add
   target**. For **Target type**, choose your
   desired target.
6. Choose **Configure details.**
7. For **Rule definition**, type a name and description
   for your rule and choose **Create rule**.
