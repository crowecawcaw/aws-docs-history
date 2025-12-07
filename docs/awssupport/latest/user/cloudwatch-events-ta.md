# Monitoring AWS Trusted Advisor check results with

Amazon EventBridge

###### Important

End of Support Notice: Developer Support will be discontinued January 1, 2027. Customers with Developer Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information, see [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: Business Support will be discontinued January 1, 2027. Customers with Business Support can continue using their existing plan or choose to upgrade to Business Support+ anytime before January 1, 2027. Business Support+ delivers AI-powered assistance that understands the context of your operations, with 24/7 access to AWS experts at $29/month minimum per account. For more information see, [Business Support+ plan details](https://aws.amazon.com/premiumsupport/plans/business-plus/ "https://aws.amazon.com/premiumsupport/plans/business-plus/")

End of Support Notice: On January 1, 2027, AWS will discontinue Enterprise On-Ramp. Throughout 2026, Enterprise On-Ramp customers will be automatically upgraded to AWS Enterprise Support during contract renewal or in periodic batches. Customers will receive an email notification a month before their upgrade. No further action is required. Enterprise Support provides designated TAM assignment, 15-minute response times, and AWS Security Incident Response available at no additional cost, all at a lower $5,000 minimum (reduced from $15,000). For more information, see [AWS Enterprise Support plan details](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/").

For more information, see [Developer, Business, and Enterprise On-Ramp end of support](support-plans-eos.md "support-plans-eos.md").

Developer Support, Business Support, and Enterprise On-Ramp will remain available in the AWS GovCloud (US) Region.

You can use EventBridge to detect when your checks for Trusted Advisor change status. Then, based on the
rules that you create, EventBridge invokes one or more target actions when the status changes to a
value that you specify in a rule.

Depending on the status change, you can send notifications,
capture status information, take corrective action, initiate events, or take other actions.
For example, you can specify the following target types if a check changes status from no
problems detected (green) to recommended action (red).

- Use an AWS Lambda function to pass a notification to a Slack channel.
- Push data about the check to an Amazon Kinesis stream to support comprehensive and real-time
  status monitoring.
- Send an Amazon Simple Notification Service topic to your email.
- Get notified with an Amazon CloudWatch alarm action.
  For more information about on how to use EventBridge and Lambda functions to automate responses for
  Trusted Advisor, see [Trusted Advisor tools](https://github.com/aws/Trusted-Advisor-Tools "https://github.com/aws/Trusted-Advisor-Tools")
  in GitHub.

###### Notes

- Trusted Advisor delivers events on a best effort basis. Events are not always guaranteed to
  be delivered to EventBridge.
- You must have an AWS Business Support+, AWS Enterprise Support, or AWS Unified Operations plan to create a rule for Trusted Advisor checks. For more
  information, see [Change AWS Support Plans](changing-support-plans.md "changing-support-plans.md").
-
- As Trusted Advisor is a Global service, all Events are emitted to EventBridge in
  the US East (N. Virginia) Region.
  Follow this procedure to create an EventBridge rule for Trusted Advisor. Before you create event rules, do
  the following:

- Familiarize yourself with events, rules, and targets in EventBridge. For more information, see
  [What is
  Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _Amazon EventBridge User Guide_.
- Create the target that you will use in your event rule.

###### To create an EventBridge rule for Trusted Advisor

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. To change the Region, use the **Region selector** in the upper-right
   corner of the page and choose **US East (N. Virginia)**.
3. In the navigation pane, choose **Rules**.
4. Choose **Create rule**.
5. On the **Define rule detail** page, enter a name and description for
   your rule.
6. Keep the default values for **Event bus** and **Rule
   type**, and then choose **Next**.
7. On the **Build event pattern** page, for **Event
   source**, choose **AWS events or EventBridge partner events**.
8. Under **Event pattern**, keep the default value for
   **AWS services**.
9. For **AWS service**, choose **Trusted Advisor**.
10. For **Event type**, choose **Check Item Refresh
    Status**.
11. Choose one of the following options for check statuses:
    - Choose **Any status** to create a rule that monitors
      for any status change.
    - Choose **Specific status(es)**, and then choose the values that you
      want your rule to monitor.
      - **ERROR** – Trusted Advisor recommends an action for the
        check.
      - **INFO** – Trusted Advisor can't determine the status of the
        check.
      - **OK** – Trusted Advisor doesn't detect an issue for the check.
      - **WARN** – Trusted Advisor detects a possible issue for the
        check and recommends investigation.

12. Choose one of the following options for your checks:
    - Choose **Any check**.
    - Choose **Specific check(s)**, and then choose one or more check
      names from the list.

13. Choose one of the following options for AWS resources:
    - Choose **Any resource ID** to create a rule that monitors all
      resources.
    - Choose **Specific resource ID(s) by ARN**, and then enter the
      Amazon Resource Names (ARNs) that you want.

14. Choose **Next**.
15. In the **Select target(s)** page, choose the target type that you
    created for this rule, and then configure any additional options that are required for that
    type. For example, you might send the event to an Amazon SQS queue or an Amazon SNS topic.
16. Choose **Next**.
17. (Optional) On the **Configure tags** page, add any tags and then choose
    **Next**.
18. On the **Review and create** page, review your rule setup and ensure
    that it meets your event monitoring requirements.
19. Choose **Create rule**. Your rule will now monitor for Trusted Advisor checks
    and then send the event to the target that you specified.
