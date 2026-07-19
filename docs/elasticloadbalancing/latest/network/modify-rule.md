# Edit a listener rule

You can edit the conditions, actions, and priority of a listener rule.

Console

###### To edit a listener rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners and rules** tab, choose the text in the
   **Protocol:Port** column to open the detail page for
   the listener.
5. On the **Rules** tab, select the check box for
   the rule to modify, and then choose **Actions**,
   **Edit rule**.
6. Update the conditions or actions as needed.
7. Choose **Next**.
8. For **Priority**, enter a value from
   1-50,000. Rules are evaluated in priority order from the
   lowest value to the highest value.
9. Choose **Next**.
10. On the **Review and create** page, choose
    **Save changes**.

AWS CLI

###### To edit a listener rule

Use the following [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") command to update the conditions and
actions of a rule.

```
aws elbv2 modify-rule \
    --rule-arn `rule-arn` \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"IpAddressType":"ipv6"}}]' \
    --actions '[{"Type":"forward","TargetGroupArn":"`new-target-group-arn`"}]'
```
