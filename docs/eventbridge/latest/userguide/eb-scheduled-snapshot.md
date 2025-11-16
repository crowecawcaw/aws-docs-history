# Tutorial: Create a scheduled rule in EventBridge

You can run EventBridge [rules](eb-rules.md "eb-rules.md") on a schedule. In this tutorial,
you create a snapshot of an existing [Amazon Elastic Block Store](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") (Amazon EBS) volume on a schedule. You can choose
a fixed rate to create a snapshot every few minutes or use a cron expression to create the
snapshot at a specific time of day.

###### Important

To create rules with built-in [targets](eb-targets.md "eb-targets.md"), you must use
the AWS Management Console.

###### Steps:

- [Step 1: Create the rule](#eb-ebs-create-rule "#eb-ebs-create-rule")
- [Step 2: Test the rule](#eb-ebs-test-rule "#eb-ebs-test-rule")
- [Step 3: Confirm success](#success "#success")
- [Step 4: Clean up your resources](#cleanup "#cleanup")

## Step 1: Create the rule

Create a rule that takes snapshots on a schedule. You can use a rate expression or
a cron expression to specify the schedule. For more information, see [Creating a scheduled rule (legacy) in Amazon EventBridge](eb-create-rule-schedule.md "eb-create-rule-schedule.md").

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus. 5. For **Event bus**, choose the event bus that you want
to associate with this rule. If you want this rule to match events that come
from your account, select **AWS default event bus**. When an
AWS service in your account emits an event, it always goes to your account’s
default event bus. 6. For **Rule type**, choose **Schedule**. 7. Choose **Next**. 8. For **Schedule pattern**, choose **A schedule that runs at a regular rate, such as every 10 minutes.** and
enter `5` and choose **Minutes** from the drop-down list. 9. Choose **Next**. 10. For **Target types**, choose **AWS service**. 11. For **Select a target**, choose **EBS
Create Snapshot** from the drop-down list. 12. For **Volume ID**, enter the volume ID of the Amazon EBS
volume. 13. For **Execution role**, choose **Create a new for role for this specific resource**. 14. Choose **Next**. 15. Choose **Next**. 16. Review the details of the rule and choose **Create rule**.

## Step 2: Test the rule

You can verify your rule works by viewing your first snapshot after it's taken.

###### To test your rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic Block Store**,
   **Snapshots**.
3. Verify that the first snapshot appears in the list.

## Step 3: Confirm success

If you see the a snapshot in the list, you've successfully completed this tutorial. If the snapshot isn't in the list,
start troubleshooting by verifying the rule was created successfully.

## Step 4: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
