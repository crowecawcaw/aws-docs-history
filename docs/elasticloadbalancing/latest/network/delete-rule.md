# Delete a listener rule

You can delete a non-default listener rule at any time. You cannot delete
the default rule. When you delete a rule, traffic that was matched by the
deleted rule is routed according to the remaining rules or the default
action.

Console

###### To delete a listener rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners and rules** tab, choose the text in the
   **Protocol:Port** column to open the detail page for
   the listener.
5. On the **Rules** tab, select the check box for
   the rule to delete, and then choose **Actions**,
   **Delete rule**.
6. When prompted for confirmation, choose
   **Delete**.

AWS CLI

###### To delete a listener rule

Use the following
[delete-rule](../../../cli/latest/reference/elbv2/delete-rule.md "../../../cli/latest/reference/elbv2/delete-rule.md") command to delete a rule.

```
aws elbv2 delete-rule \
    --rule-arn `rule-arn`
```
