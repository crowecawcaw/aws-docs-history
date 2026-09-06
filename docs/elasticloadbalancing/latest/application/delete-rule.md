

# Delete a listener rule for your Application Load Balancer
<a name="delete-rule"></a>

You can delete the nondefault rules for a listener at any time. You can't delete the default rule for a listener. When you delete a listener, all its rules are deleted.

------
#### [ Console ]

**To delete a rule**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer.

1. On the **Listeners and rules** tab, select the text in the **Protocol:Port** column to open the detail page for the listener.

1. Select the rule.

1. Choose **Actions**, **Delete rule**.

1. When prompted for confirmation, enter **confirm** and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a rule**  
Use the [delete-rule](https://docs.aws.amazon.com/cli/latest/reference/elbv2/delete-rule.html) command.

```
aws elbv2 delete-rule \
    --rule-arn {{listener-rule-arn}}
```

------