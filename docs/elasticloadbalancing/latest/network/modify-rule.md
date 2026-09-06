

# Edit a listener rule
<a name="modify-rule"></a>

You can edit the conditions, actions, and priority of a listener rule.

------
#### [ Console ]

**To edit a listener rule**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Choose the name of the load balancer to open its detail page.

1. On the **Listeners and rules** tab, choose the text in the **Protocol:Port** column to open the detail page for the listener.

1. On the **Rules** tab, select the check box for the rule to modify, and then choose **Actions**, **Edit rule**.

1. Update the conditions or actions as needed.

1. Choose **Next**.

1. For **Priority**, enter a value from 1-50,000. Rules are evaluated in priority order from the lowest value to the highest value.

1. Choose **Next**.

1. On the **Review and create** page, choose **Save changes**.

------
#### [ AWS CLI ]

**To edit a listener rule**  
Use the following [modify-rule](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-rule.html) command to update the conditions and actions of a rule.

```
aws elbv2 modify-rule \
    --rule-arn {{rule-arn}} \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"IpAddressType":"ipv6"}}]' \
    --actions '[{"Type":"forward","TargetGroupArn":"{{new-target-group-arn}}"}]'
```

------