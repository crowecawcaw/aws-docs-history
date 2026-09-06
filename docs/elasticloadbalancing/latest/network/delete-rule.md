

# Delete a listener rule
<a name="delete-rule"></a>

You can delete a non-default listener rule at any time. You cannot delete the default rule. When you delete a rule, traffic that was matched by the deleted rule is routed according to the remaining rules or the default action.

------
#### [ Console ]

**To delete a listener rule**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Choose the name of the load balancer to open its detail page.

1. On the **Listeners and rules** tab, choose the text in the **Protocol:Port** column to open the detail page for the listener.

1. On the **Rules** tab, select the check box for the rule to delete, and then choose **Actions**, **Delete rule**.

1. When prompted for confirmation, choose **Delete**.

------
#### [ AWS CLI ]

**To delete a listener rule**  
Use the following [delete-rule](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-rule.html) command to delete a rule.

```
aws elbv2 delete-rule \
    --rule-arn {{rule-arn}}
```

------