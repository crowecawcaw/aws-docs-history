# Update the TCP idle timeout for your Network Load Balancer listener

For each TCP request made through a Network Load Balancer, the state of that connection is tracked.
If no data is sent through the connection by either the client or target for longer
than the idle timeout, the connection is closed.

###### Considerations

- The default idle timeout value for TCP flows is 350 seconds.
- The connection idle timeout for TLS listeners is 350 seconds and can't be modified.

Console

###### To update the TCP idle timeout

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the check box for the Network Load Balancer.
4. On the listeners tab, select the check box for the TCP listener and then choose
   **Actions**, **View listener details**.
5. On the listener details page, in the **Attributes** tab, select
   **Edit**. If the listener uses a protocol other than TCP, this tab
   is not present.
6. Enter a value for **TCP idle timeout** from 60-6000 seconds.
7. Choose **Save changes**.

AWS CLI

###### To update the TCP idle timeout

Use the [modify-listener-attributes](../../../cli/latest/reference/elbv2/modify-listener-attributes.md "../../../cli/latest/reference/elbv2/modify-listener-attributes.md") command with the
`tcp.idle_timeout.seconds` attribute.

```
aws elbv2 modify-listener-attributes \
    --listener-arn `listener-arn` \
    --attributes Key=tcp.idle_timeout.seconds,Value=`500`
```

The following is example output.

```
{
    "Attributes": [
        {
            "Key": "tcp.idle_timeout.seconds",
            "Value": "500"
        }
    ]
}
```

CloudFormation

###### To update the TCP idle timeout

Update the [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md") resource to include
the `tcp.idle_timeout.seconds` listener attribute.

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
      ListenerAttributes:
        - Key: "tcp.idle_timeout.seconds"
          Value: "`500`"
```
