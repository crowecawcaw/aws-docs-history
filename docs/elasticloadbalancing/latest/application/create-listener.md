# Create an HTTP listener for your Application Load Balancer

A listener checks for connection requests. You define a listener
when you create your load balancer, and you can add listeners to your load balancer at
any time.

The information on this page helps you create an HTTP listener for your load balancer.
To add an HTTPS listener to your load balancer, see [Create an HTTPS listener for your Application Load Balancer](create-https-listener.md "create-https-listener.md").

## Prerequisites

- To add a forward action to the default listener rule, you must specify an
  available target group. For more information, see [Create a target group for your Application Load Balancer](create-target-group.md "create-target-group.md").
- You can specify the same target group in multiple listeners, but these
  listeners must belong to the same load balancer. To use a target group with
  a load balancer, you must verify that it is not used by a listener for any
  other load balancer.

## Add an HTTP listener

You configure a listener with a protocol and a port for connections from clients
to the load balancer, and a target group for the default listener rule. For more
information, see [Listener configuration](load-balancer-listeners.md#listener-configuration "load-balancer-listeners.md#listener-configuration").

To add another listener rule, see [Listener rules](listener-rules.md "listener-rules.md").

Console

###### To add an HTTP listener

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, choose **Add listener**.
5. For **Protocol**, choose **HTTP**.
   Keep the default port or enter a different port.
6. For **Default action**, select one of the following routing
   actions and provide the required information:
   - **Forward to target groups** –
     Choose a target group. To add another target group,
     choose **Add target group**, choose a
     target group, review the relative weights, and update
     the weights as needed. You must enable group-level
     stickiness if you enabled stickiness on any of the
     target groups.

   If you don't have a target group that meets your needs, choose
   **Create target group** to create one now.
   For more information, see [Create a target group](create-target-group.md "create-target-group.md").
   - **Redirect to URL** – Enter the URL by entering each part separately
     on the **URI parts** tab, or by entering the full address on the
     **Full URL** tab. For **Status code**, select either temporary
     (HTTP 302) or permanent (HTTP 301) based on your needs.
   - **Return fixed response** – Enter the
     **Response code** to return for dropped client
     requests. Optionally, you can specify the **Content
     type** and a **Response body**.

7. (Optional) To add tags, expand **Listener tags**. Choose
   **Add new tag** and enter the tag key and tag value.
8. Choose **Add listener**.

AWS CLI

###### To create a target group

If you don't have a target group that you can use for the default action,
use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command to create one now. For
examples, see [Create a target group](create-target-group.md "create-target-group.md").

###### To create an HTTP listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command. The following example
creates an HTTP listener with a default rule that forwards
traffic to the specified target group.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol HTTP \
    --port `80` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

To create a forward action that distributes traffic between two target groups,
use the following `--default-actions` option instead. When specifying
multiple target groups, you must provide a weight for each target group.

```
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

###### To create an HTTP listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md"). The
following example creates an HTTP listener with a default
rule that forwards traffic to the specified target group.

```
Resources:
  myHTTPlistener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTP
    Port: `80`
    DefaultActions:
      - Type: "forward"
        TargetGroupArn: !Ref myTargetGroup
```

To create a forward action that distributes traffic between multiple target
groups, use the `ForwardConfig` property. When specifying
multiple target groups, you must provide a weight for each target group.

```
Resources:
  myHTTPlistener:
  Type: 'AWS::ElasticLoadBalancingV2::Listener'
  Properties:
    LoadBalancerArn: !Ref myLoadBalancer
    Protocol: HTTP
    Port: `80`
    DefaultActions:
      - Type: "forward"
        ForwardConfig:
          TargetGroups:
            - TargetGroupArn: !Ref TargetGroup1
              Weight: `50`
            - TargetGroupArn: !Ref TargetGroup2
              Weight: `50`
```
