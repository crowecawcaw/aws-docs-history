# Add a listener rule

You configure a listener rule with a priority, conditions, and actions. A rule
routes traffic to the specified target groups when the rule conditions are met.
For more information about rule concepts, see [Listener rules](load-balancer-listeners.md#listener-rules "load-balancer-listeners.md#listener-rules").

Console

###### To create a listener rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners and rules** tab, choose the text in the
   **Protocol:Port** column to open the detail page for
   the listener.
5. On the **Rules** tab, choose
   **Add rule**.
6. For **Name**, optionally enter a name
   for the rule.
7. For **Condition**, the source IP
   condition is selected. For
   **IP address type**, choose
   **IPv4** or **IPv6**.
8. For **Action**, choose
   **Forward to target groups**, and then
   choose one or more target groups. If you choose more than
   one target group, you must specify a weight for each target
   group.
9. Choose **Next**.
10. For **Priority**, enter a value from
    1-50,000. Rules are evaluated in priority order from the
    lowest value to the highest value.
11. Choose **Next**.
12. On the **Review and create** page, choose
    **Create**.

AWS CLI

###### To create a listener rule that routes IPv4 traffic

Use the following [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") command to create a rule that routes
IPv4 source traffic to an IPv4 target group.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `10` \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"IpAddressType":"ipv4"}}]' \
    --actions '[{"Type":"forward","TargetGroupArn":"`ipv4-target-group-arn`"}]'
```

###### To create a listener rule that routes IPv6 traffic

Use the following [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") command to create a rule that routes
IPv6 source traffic to an IPv6 target group.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `20` \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"IpAddressType":"ipv6"}}]' \
    --actions '[{"Type":"forward","TargetGroupArn":"`ipv6-target-group-arn`"}]'
```

###### To create a listener rule with weighted target groups

Use the following [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") command to create a rule that routes
traffic to multiple target groups with weights.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `10` \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"IpAddressType":"ipv4"}}]' \
    --actions '[{"Type":"forward","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"`ipv4-tg-1-arn`","Weight":70},{"TargetGroupArn":"`ipv4-tg-2-arn`","Weight":30}]}}]'
```
