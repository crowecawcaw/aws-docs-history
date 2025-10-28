# Delete a listener rule for your Application Load Balancer

You can delete the nondefault rules for a listener at any time. You can't delete the
default rule for a listener. When you delete a listener, all its rules are
deleted.

Console

###### To delete a rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load
   Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select the
   text in the **Protocol:Port** column to open the
   detail page for the listener.
5. Select the rule.
6. Choose **Actions**, **Delete
   rule**.
7. When prompted for confirmation, enter
   `confirm` and then choose
   **Delete**.

AWS CLI

###### To delete a rule

Use the [delete-rule](../../../cli/latest/reference/elbv2/delete-rule.md "../../../cli/latest/reference/elbv2/delete-rule.md") command.

```
aws elbv2 delete-rule \
    --rule-arn `listener-rule-arn`
```
