

# Update a listener for your Network Load Balancer
<a name="listener-update-rules"></a>

You can update the listener protocol, listener port or the target group which receives traffic from the forwarding action. The default action, also known as the default rule, forwards requests to the selected target group.

To add, modify, or delete custom routing rules for the listener, see [Listener rules for your Network Load Balancer](create-rule.md).

If you change the protocol from TCP, UDP, or QUIC to TLS, you must specify a security policy and server certificate. If you change the protocol from TLS to TCP, UDP, or QUIC, the security policy and server certificate are removed.

When the target group for the default action of a TCP, TLS, or QUIC listener is updated, new connections are routed to the newly configured target group. However, this has no effect on any active connections that were created prior to this change. These active connections remain associated to the target in the original target group for up to one hour if traffic is being sent, or up to when the idle-timeout period elapses if no traffic is sent, whichever occurs first. The parameter `Connection termination on deregistration` is not applied when updating the listener, as it's applied when deregistering targets.

Port updates for QUIC or TCP\_QUIC listeners are not allowed. To update the port for listeners that handle QUIC traffic, the listener must be deleted and re-created with the new port.

------
#### [ Console ]

**To update a listener**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Choose the name of the load balancer to open its detail page.

1. On the **Listeners and rules** tab, choose the text in the **Protocol:Port** column to open the detail page for the listener.

1. Choose **Actions**, **Edit listener**.

1. Update the values as needed.
   + (Optional) Change the **Protocol**.
   + (Optional) Change the **Port**.
   + (Optional) Choose different target groups for the **Default action**.
   + (Optional) To add another target group, choose **Add target group** and update the weights as needed.
   + (Optional) To remove a target group, choose **Remove**.

1. (Optional) Add, update, or remove tags as needed.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To update the default action**  
Use the following [modify-listener](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-listener.html) command to change the target group.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --default-actions Type=forward,TargetGroupArn={{new-target-group-arn}}
```

The following example updates a listener with multiple target groups.

```
aws elbv2 modify-listener \
    --listener-arn {{listener-arn}} \
    --default-actions '[{
        "Type":"forward",
        "ForwardConfig":{
            "TargetGroups":[
                {"TargetGroupArn":"{{target-group-1-arn}}","Weight":{{10}}},
                {"TargetGroupArn":"{{target-group-2-arn}}","Weight":{{30}}}
            ]
        }
    }]'
```

**To add tags**  
Use the [add-tags](https://docs.aws.amazon.com/cli/latest/reference/elbv2/add-tags.html) command. The following example adds two tags.

```
aws elbv2 add-tags \
    --resource-arns {{listener-arn}} \
    --tags "Key={{project}},Value={{lima}}" "Key={{department}},Value={{digital-media}}"
```

**To remove tags**  
Use the [remove-tags](https://docs.aws.amazon.com/cli/latest/reference/elbv2/remove-tags.html) command. The following example removes the tags with the specified keys.

```
aws elbv2 remove-tags \
    --resource-arns {{listener-arn}} \
    --tag-keys {{project}} {{department}}
```

------
#### [ CloudFormation ]

**To update the default action**  
Update the [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html) resource to include the new target group.

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
          TargetGroupArn: !Ref {{newTargetGroup}}
```

Alternatively, to distribute traffic between multiple target groups, define `DefaultActions` as follows.

```
DefaultActions:
    - Type: forward
    ForwardConfig:
        TargetGroups:
        - TargetGroupArn: !Ref {{TargetGroup1}}
            Weight: {{10}}
        - TargetGroupArn: !Ref {{TargetGroup2}}
            Weight: {{30}}
```

**To add tags**  
Update the [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html) resource to include the Tags property.

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
        - Key: '{{project}}'
          Value: '{{lima}}'
        - Key: '{{department}}'
          Value: '{{digital-media}}'
```

------