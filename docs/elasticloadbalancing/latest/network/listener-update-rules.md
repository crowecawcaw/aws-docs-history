# Update a listener for your Network Load Balancer

You can update the listener protocol, listener port or the target group which receives
traffic from the forwarding action. The default action, also known as the default rule,
forwards requests to the selected target group.

If you change the protocol from TCP or UDP to TLS, you must specify a security policy
and server certificate. If you change the protocol from TLS to TCP or UDP, the security
policy and server certificate are removed.

When the target group for the default action of a TCP or TLS listener is updated, new
connections are routed to the newly configured target group. However, this has no effect
on any active connections that were created prior to this change. These active
connections remain associated to the target in the original target group for up to one
hour if traffic is being sent, or up to when the idle-timeout period elapses if no
traffic is sent, whichever occurs first. The parameter `Connection termination on
 deregistration` is not applied when updating the listener, as it's applied
when deregistering targets.

Console

###### To update a listener

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose the name of the load balancer to open its detail page.
4. On the **Listeners** tab, choose the text in the
   **Protocol:Port** column to open the detail page for the
   listener.
5. Choose **Edit**.
6. (Optional) Change the specified values for **Protocol**
   and **Port** as needed.
7. (Optional) Choose a different target group for
   **Default action**.
8. (Optional) Add, update, or remove tags as needed.
9. Choose **Save changes**.

AWS CLI

###### To update the default action

Use the following [modify-listener](../../../cli/latest/reference/elbv2/modify-listener.md "../../../cli/latest/reference/elbv2/modify-listener.md") command to change the target group for
the default action.

```
aws elbv2 modify-listener \
    --listener-arn `listener-arn` \
    --default-actions Type=forward,TargetGroupArn=`new-target-group-arn`
```

###### To add tags

Use the [add-tags](../../../cli/latest/reference/elbv2/add-tags.md "../../../cli/latest/reference/elbv2/add-tags.md") command. The following example
adds two tags.

```
aws elbv2 add-tags \
    --resource-arns `listener-arn` \
    --tags "Key=`project`,Value=`lima`" "Key=`department`,Value=`digital-media`"
```

###### To remove tags

Use the [remove-tags](../../../cli/latest/reference/elbv2/remove-tags.md "../../../cli/latest/reference/elbv2/remove-tags.md") command. The following example
removes the tags with the specified keys.

```
aws elbv2 remove-tags \
    --resource-arns `listener-arn` \
    --tag-keys `project` `department`
```

CloudFormation

###### To update the default action

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource to include the
new target group.

```
Resources:
  myTCPListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TCP
      Port: 80
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref `newTargetGroup`
```

###### To add tags

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource
to include the Tags property.

```
Resources:
  myTCPListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TCP
      Port: 80
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
      Tags:
        - Key: '`project`'
          Value: '`lima`'
        - Key: '`department`'
          Value: '`digital-media`'
```
