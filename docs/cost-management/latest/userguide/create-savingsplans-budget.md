# Creating a Savings Plans budget

Use this procedure to create a budget that's specifically for Savings Plans utilization or
coverage.

###### Note

It can take up to 48 hours for Savings Plans utilization and coverage metrics to
generate, which is longer than the time frame for cost and usage data.

###### To create a Savings Plans budget

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. In the navigation pane, choose **Budgets**.
3. At the top of the page, choose **Create budget**.
4. Under **Budget setup**, choose **Customize
   (advanced)**.
5. Under **Budget types**, choose **Savings Plans
   budget**. Then, choose **Next**.
6. Under **Details**, for **Budget name**,
   enter the name of your budget. Your budget name must be unique within your
   account. It can contain A-Z, a-z, spaces, and the following
   characters:

```
`_.:/=+-%@`
```

7.  Under **Utilization threshold**, for **Period**, choose
    how often you want the budget to reset the tracked utilization or coverage.

        * **Daily** for every day
        * **Monthly** for every month
        * **Quarterly** for every three months
        * **Annually** for every 12 months
        * **Custom** to specify your own start and end
         dates

    All budget times are in the UTC format.

###### Note

**Custom** period budgets align with time periods
outside of standard reset options. For example, you can create a budget
period that matches your fiscal year or project timeline. 8. For **Monitor my spend against**, choose
**Utilization of Savings Plans** to track how much of your
Savings Plans you used. Or, choose **Coverage of Savings Plans** to track
how much of your instance usage is covered by Savings Plans.

For **Utilization threshold**, enter the utilization
percentage that you want AWS to notify you at. For example, for a
utilization budget where you want to stay above 90% Savings Plans utilization, enter
`90`. The budget notiﬁes you when your overall
Savings Plans utilization is below 90%.

For **Coverage threshold**, enter the coverage percentage
that you want AWS to notify you at. For example, for a coverage budget
where you want to stay above 80%, enter `80`. The
budget notiﬁes you when your overall coverage is below 80%. 9. (Optional) Under **Budget scope**, for
**Filters**, choose **Add filter** to
apply one or more of the [available filters](budgets-create-filters.md "budgets-create-filters.md"). Your
choice of budget type determines the set of filters that's displayed on the
console.

###### Note

You can't use the **Linked account** filter within a
linked account. 10. Choose **Next**. 11. Under **Notification preferences**, for **Email
recipients**, enter the email addresses that you want the alert
to notify. Separate multiple email addresses with commas. A notification can
be sent to a maximum of 10 email addresses. 12. (Optional) For **Amazon SNS Alerts**, enter the Amazon
Resource Name (ARN) for your Amazon SNS topic. For instructions on how to create
a topic, see [Creating an Amazon SNS topic for budget
notifications](budgets-sns-policy.md "budgets-sns-policy.md").

###### Important

After you create a budget with Amazon SNS notifications, Amazon SNS sends a confirmation email to the email addresses that you specified. The subject line is **AWS Notification - Subscription Confirmation**. The recipient must choose **Confirm subscription** in the confirmation email to receive future notifications. 13. (Optional) For **AWS Chatbot Alerts**, you can choose to configure
AWS Chatbot to send budget alerts to an Amazon Chime or Slack chat room. You
configure these alerts through the AWS Chatbot console. 14. Choose **Next**.

###### Note

To proceed, you must configure at least one email recipient or an
Amazon SNS topic for notifications. 15. Review your budget settings, and then choose **Create
budget**.
