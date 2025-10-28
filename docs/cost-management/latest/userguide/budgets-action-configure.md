# Configuring a budget action

You can attach budget actions to an alert for either a cost budget or a usage budget.
To configure a budget action on a new budget, first follow the steps for [Creating a cost budget](create-cost-budget.md "create-cost-budget.md") or [Creating a usage budget](create-usage-budget.md "create-usage-budget.md"). To configure a
budget action on an existing cost or usage budget, first follow the steps for [Editing a budget](budgets-edit.md "budgets-edit.md"). Then, after you reach the
**Configure alerts** step of creating or editing the budget, use
the following procedure.

###### To configure a budget action

1. To configure a budget action on a new alert, choose **Add an alert
   threshold**. To configure a budget action on an existing alert,
   skip to step 7.
2. Under **Set alert threshold**, for
   **Threshold**, enter the amount that needs to be reached
   for you to be notified. This can be either an absolute value or a percentage.
   For example, say you have a budget of 200 dollars. To be notiﬁed at 160 dollars
   (80% of your budget), enter `160` for an absolute budget or
   `80` for a percentage budget.

Next to the amount, choose **Absolute value** to be notiﬁed
when your costs exceed the threshold amount. Or, choose **% of budgeted
amount** to be notiﬁed when your costs exceed the threshold
percentage.

Next to the threshold, choose **Actual** to create an alert
for actual spend. Or, choose **Forecasted** to create an alert
for forecasted spend. 3. (Optional) Under **Notification preferences - Optional**, for
**Email recipients**, enter the email addresses that you
want the alert to notify. Separate multiple email addresses with commas. A
notification can have up to 10 email addresses. 4. (Optional) Under **Notification preferences - Optional**, for
**Amazon SNS Alerts**, enter the Amazon Resource Name (ARN) for
your Amazon SNS topic. For instructions on how to create a topic, see [Creating an Amazon SNS topic for budget
notifications](budgets-sns-policy.md "budgets-sns-policy.md").

###### Important

After you create a budget with Amazon SNS notifications, Amazon SNS sends a confirmation email to the email addresses that you specified. The subject line is **AWS Notification - Subscription Confirmation**. The recipient must choose **Confirm subscription** in the confirmation email to receive future notifications. 5. (Optional) Under **Notification preferences - Optional**, for
**Amazon Q Developer in chat applications Alerts**, you can configure Amazon Q Developer in chat applications to send budget
alerts to an Amazon Chime or Slack chat room. You configure these alerts through the
Amazon Q Developer in chat applications console. 6. Choose **Next**. 7. For **Attach actions - Optional**, choose **Add
Action**.

    1. For **Select IAM role**, choose an IAM role to
     allow AWS Budgets to perform an action on your behalf.


    ###### Note

    If you didn't configure and assign the appropriate permissions for
     the IAM role and for AWS Budgets, then AWS Budgets can't run
     your configured actions. For simplified permissions management, we
     recommend that you use the managed policy. This ensures that your
     AWS Budgets actions work as intended and eliminates the need to
     update your existing IAM policy for AWS Budgets whenever any new
     functionality is added. This is because new functions and
     capabilities are added to the managed policy by default. For more
     information about managed policies, see [Managed policies](billing-permissions-ref.md#managed-policies "billing-permissions-ref.md#managed-policies").


     For more information and examples of IAM role permissions, see
     [Allow AWS Budgets to apply
     IAM policies and SCPs and target EC2 and RDS instances](billing-example-policies.md#example-budgets-applySCP "billing-example-policies.md#example-budgets-applySCP").
    2. For **Which action type should be applied when the budget
     threshold has been exceeded**, select the action that you
     want AWS Budgets to take on your behalf.


    You can choose from applying an IAM policy, attaching a service
     control policy (SCP), or targeting speciﬁc Amazon EC2 or Amazon RDS instances. You
     can apply multiple budget actions to a single alert. Only a
     management account can apply SCPs.
    3. Depending on the action that you chose, complete the fields related to
     the resources that you want to apply the action to.
    4. For **Do you want to automatically run this action when this
     threshold is exceeded**, choose **Yes** or
     **No**. If you choose **No**, then
     you run the action manually on the **Alert details**
     page. For instructions, see [Reviewing and approving your budget
     action](budgets-action-review.md "budgets-action-review.md").
    5. For **How do you want to be alerted when this action is
     run**, choose **Use the same alert settings when
     you defined this threshold** or **Use different
     alert settings**. To use different alert settings, complete
     the **Notification preferences** specific to this
     action.

8. Choose **Next**.

###### Note

To proceed, you must configure at least one of the following for each
alert:

    * An email recipient for notifications
    * An Amazon SNS topic for notifications
    * A budget action

9. Review your budget settings, and then choose **Create
   budget** or **Save**.
   After you create an action, you can view its status from the AWS Budgets page on the
   **Actions** column. This column shows your configured actions
   count, actions waiting for your approval (**Requires approval**), and
   your successfully completed actions.
