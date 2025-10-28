# Edit a listener rule for your Application Load Balancer

You can edit the action and conditions for a listener rule at any time. Rule updates
do not take effect immediately, so requests could be routed using the previous rule
configuration for a short time after you update a rule. Any in-flight requests are
completed.

###### Tasks

- [Modify the default action](#modify-default-action "#modify-default-action")
- [Update rule priorities](#update-rule-priority "#update-rule-priority")
- [Update actions, conditions, and transforms](#update-rule-actions-conditions-transforms "#update-rule-actions-conditions-transforms")
- [Manage the rule tags](#manage-rule-tags "#manage-rule-tags")

## Modify the default action

The default action is assigned to a rule named **Default**. You
can keep the current rule type and change the required information, or you can
change the rule type and provide the new required information.

Console

###### To modify the default action

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load
   Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select
   the text in the **Protocol:Port** column
   to open the detail page for the listener.
5. On the **Rules** tab, in the
   **Listener rules** section, select
   the default rule. Choose **Actions**,
   **Edit rule**.
6. Under **Default action**, update the
   actions as needed.

AWS CLI

###### To modify the default action

Use the [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command. The following example updates
the target group for the `forward` action.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --default-actions Type=forward,TargetGroupArn=`new-target-group-arn`
```

The following example updates the default action to distribute
traffic equally between two target groups.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --default-actions '[{
      "Type":"forward",
      "ForwardConfig":{
        "TargetGroups":[
          {"TargetGroupArn":"`target-group-1-arn`","Weight":`50`},
          {"TargetGroupArn":"`target-group-2-arn`","Weight":`50`}
        ]
      }
    }]'
```

CloudFormation

###### To modify the default action

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource.

```
Resources:
    myHTTPlistener:
      Type: 'AWS::ElasticLoadBalancingV2::Listener'
      Properties:
        LoadBalancerArn: !Ref myLoadBalancer
        Protocol: HTTP
        Port: 80
        DefaultActions:
          - Type: "forward"
            TargetGroupArn: !Ref `myNewTargetGroup`
```

## Update rule priorities

Rules are evaluated in priority order, from the lowest value to the highest value.
The default rule is evaluated last. You can change the priority of a nondefault rule
at any time. You can't change the priority of the default rule.

Console

###### To update rule priorities

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load
   Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select
   the text in the **Protocol:Port** column to
   open the detail page for the listener.
5. On the **Rules** tab, select the listener
   rule and then choose **Actions**,
   **Reprioritize rules**.
6. In the **Listener rules** section, the
   **Priority** column displays the current
   rule priorities. To update a rule priority, enter a value from
   1-50,000.
7. Choose **Save changes**.

AWS CLI

###### To update rule priorities

Use the [set-rule-priorities](../../../cli/latest/reference/elbv2/set-rule-priorities.md "../../../cli/latest/reference/elbv2/set-rule-priorities.md") command.

```
aws elbv2 set-rule-priorities \
    --rule-priorities "RuleArn=`listener-rule-arn`,Priority=`5`"
```

CloudFormation

###### To update rule priorities

Update the [AWS::ElasticLoadBalancingV2::ListenerRule](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md")
resource.

```
Resources:
    myListenerRule:
     Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
     Properties:
       ListenerArn: !Ref myListener
       Priority: `5`
       Conditions:
         - Field: host-header
           Values:
             - example.com
             - www.example.com
       Actions:
         - Type: forward
           TargetGroupArn: !Ref myTargetGroup

```

## Update actions, conditions, and transforms

You can update the actions, conditions, and transforms for a rule.

Console

###### To update rule actions, conditions, and transforms

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load
   Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select
   the text in the **Protocol:Port** column to
   open the detail page for the listener.
5. On the **Rules** tab, select the listener
   rule and then choose **Actions**,
   **Edit rule**.
6. Update the actions, conditions, and transforms as needed.
   For detailed steps, see [Add a rule](add-rule.md "add-rule.md").
7. Choose **Next**.
8. (Optional) Update the priority.
9. Choose **Next**.
10. Choose **Save changes**.

AWS CLI

###### To update rule actions, conditions, and transforms

Use the [modify-rule](../../../cli/latest/reference/elbv2/modify-rule.md "../../../cli/latest/reference/elbv2/modify-rule.md") command. Include at least one of
the following options: `--actions`, `--conditions`,
and `--transforms`.

For examples of these options, see [Add a rule](add-rule.md "add-rule.md").

CloudFormation

###### To update rule actions, conditions, and transforms

Update the [AWS::ElasticLoadBalancingV2::ListenerRule](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md")
resource.

For example rules, see [Add a rule](add-rule.md "add-rule.md").

## Manage the rule tags

Tags help you to categorize your listeners and rules in different ways. For
example, you can tag a resource by purpose, owner, or environment. Tag keys must be
unique for each rule. If you add a tag with a key that is already associated with
the rule, it updates the value of that tag.

When you are finished with a tag, you can remove it.

Console

###### To manage the tags for a rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load
   Balancers**.
3. Choose the name of the load balancer to open its details
   page.
4. On the **Listeners and rules** tab, select
   the text in the **Protocol:Port** column to
   open the detail page for the listener.
5. On the **Rules** tab, select the text in the
   **Name tag** column to open the detail page
   for the rule.
6. On the rule details page, choose **Manage
   tags**.
7. On the **Manage tags** page, do one or more
   of the following:
   1. To add a tag, choose **Add new tag**
      and enter values for **Key** and
      **Value**.
   2. To delete a tag, choose **Remove**
      next to the tag.
   3. To update a tag, enter new values for
      **Key** or
      **Value**.

8. Choose **Save changes**.

AWS CLI

###### To add tags to a rule

Use the [add-tags](../../../cli/latest/reference/elbv2/add-tags.md "../../../cli/latest/reference/elbv2/add-tags.md") command.

```
aws elbv2 add-tags \
    --resource-arns `listener-rule-arn` \
    --tags "Key=`project`,Value=`lima`" "Key=`department`,Value=`digital-media`"
```

###### To remove tags from a rule

Use the [remove-tags](../../../cli/latest/reference/elbv2/remove-tags.md "../../../cli/latest/reference/elbv2/remove-tags.md") command.

```
aws elbv2 remove-tags \
    --resource-arns `listener-rule-arn` \
    --tag-keys `project` `department`
```

CloudFormation

###### To add tags to a rule

Update the [AWS::ElasticLoadBalancingV2::ListenerRule](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md")
resource.

```
Resources:
    myListenerRule:
     Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
     Properties:
       ListenerArn: !Ref myListener
       Priority: 10
       Conditions:
         - Field: host-header
           Values:
             - example.com
             - www.example.com
       Actions:
         - Type: forward
           TargetGroupArn: !Ref myTargetGroup
       Tags:
        - Key: '`project`'
          Value: '`lima`'
        - Key: '`department`'
          Value: '`digital-media`'
```
