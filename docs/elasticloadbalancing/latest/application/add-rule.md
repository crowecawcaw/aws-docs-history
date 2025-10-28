# Add a listener rule for your Application Load Balancer

You define a default rule when you create a listener. You can define additional rules
at any time. Each rule must specify an action and a condition, and can optionally
specify transforms. For more information, see the following:

- [Action types](rule-action-types.md "rule-action-types.md")
- [Condition types](rule-condition-types.md "rule-condition-types.md")
- [Transforms](rule-transforms.md "rule-transforms.md")

Console

###### To add a rule

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load
   Balancers**.
3. Select the load balancer.
4. On the **Listeners and rules** tab, select the
   text in the **Protocol:Port** column to open the
   detail page for the listener.
5. On the **Rules** tab, choose **Add
   rule**.
6. (Optional) To specify a name for your rule, expand **Name
   and tags** and enter the name. To add additional tags,
   choose **Add additional tags** and enter the tag
   key and tag value.
7. For each condition, choose **Add condition**,
   choose the condition type, and provide the required condition
   values:
   - **Host header** – Select the match
     pattern type and enter the host header.

   Value matching –
   Maximum 128 characters. Not case sensitive. Allowed
   characters are a-z, A-Z, 0-9; the following special
   characters: -\_.; and wildcards (\* and ?). You must include
   at least one "." character. You can include only
   alphabetical characters after the final "."
   character.

   Regex matching –
   Maximum 128 characters.
   - **Path** – Select the match
     pattern type and enter the path.

   Value matching –
   Maximum 128 characters. Case sensitive. Allowed characters
   are a-z, A-Z, 0-9; the following special characters:
   \_-.$/~"'@:+; &; and wildcards (\* and ?).

   Regex matching –
   Maximum 128 characters.
   - **Query string** – Enter key:value
     pairs, or values without keys.

   Maximum 128 characters. Not case sensitive. Allowed
   characters are a-z, A-Z, 0-9; the following special
   characters: \_-.$/~"'@:+&()!,;=; and wildcards (\* and
   ?).
   - **HTTP request method** – Enter
     the HTTP request method.

   Maximum 40 characters. Case sensitive. Allowed characters
   are A-Z, and the following special characters: -\_. Wildcards
   are not supported.
   - **HTTP header** – Select the match
     pattern type and enter the name of the header and the
     comparison strings.
     - **HTTP header name** –
       Rule will assess requests containing this header to
       confirm matching values.

     Value matching –
     Maximum 40 characters. Not case sensitive. Allowed
     characters are a-z, A-Z, 0-9, and the following
     special characters: \*?-!#$%&'+.^\_`|~. Wildcards
     are not supported.

     Regex matching –
     Maximum 128 characters.
     - **HTTP header value** –
       Enter strings to compare against the HTTP header
       value.

     Value matching
     Maximum 128 characters. Not case sensitive.
     Allowed characters are a-z, A-Z, 0-9; spaces; the
     following special characters:
     !"#$%&'()+,./:;<=>@[]^\_`{|}~-;
     and wildcards (\* and ?).

     Regex matching –
     Maximum 128 characters.

   - **Source IP** – Define the source
     IP address in CIDR format. Both IPv4 and IPv6 CIDRs are allowed.
     Wildcards are not supported.

8. (Optional) To add a transform, choose **Add transform**,
   choose the transform type, and enter a regular expression to match and a
   replacement string.
9. (Optional) To add an authentication rule to an HTTPS listener,
   choose **Actions**, **Authenticate
   users**, chose an identity provider, and provide the
   required information. For more information, see [Authenticate users using an Application Load Balancer](listener-authenticate-users.md "listener-authenticate-users.md").
10. For **Actions**, **Routing
    action**, select one of the following routing actions
    and provide the required information:
    - **Forward to target groups** –
      Choose a target group. To add another target group, choose
      **Add target group**, choose a target
      group, review the relative weights, and update the
      weights as needed. You must enable group-level stickiness if
      you enabled stickiness on any of the target groups.
    - **Redirect to URL** – Enter the
      URL by entering each part separately on the **URI
      parts** tab, or by entering the full address on
      the **Full URL** tab. For **Status
      code**, select either temporary (HTTP 302) or
      permanent (HTTP 301) based on your needs.
    - **Return fixed response** – Enter
      the **Response code** to return for dropped
      client requests. Optionally, you can specify the
      **Content type** and a
      **Response body**.

11. Choose **Next**.
12. For **Priority**, enter a value from 1-50,000.
    Rules are evaluated in priority order from the lowest value to the
    highest value.
13. Choose **Next**.
14. On the **Review and create** page, choose
    **Create**.

AWS CLI

###### To add a rule

Use the [create-rule](../../../cli/latest/reference/elbv2/create-rule.md "../../../cli/latest/reference/elbv2/create-rule.md") command.

The following example creates a rule with a `forward` action
and a `host-header` condition.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `10` \
    --conditions "Field=host-header,Values=`example.com`,`www.example.com`" \
    --actions "Type=forward,TargetGroupArn=`target-group-arn`"
```

To create a forward action that distributes traffic between two target groups,
use the following `--actions` option instead.

```
    --actions '[{
        "Type":"forward",
        "ForwardConfig":{
          "TargetGroups":[
            {"TargetGroupArn":"`target-group-1-arn`","Weight":`50`},
            {"TargetGroupArn":"`target-group-2-arn`","Weight":`50`}
          ]
        }
    }]'
```

The following example creates a rule with a `fixed-response` action
and a `source-ip` condition.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `20` \
    --conditions '[{"Field":"source-ip","SourceIpConfig":{"Values":["`192.168.1.0/24`","`10.0.0.0/16`"]}}]' \
    --actions "Type=fixed-response,FixedResponseConfig={StatusCode=403,ContentType=text/plain,MessageBody='`Access denied`'}"
```

The following example creates a rule with a `redirect` action
and an `http-header` condition.

```
aws elbv2 create-rule \
    --listener-arn `listener-arn` \
    --priority `30` \
    --conditions '[{"Field":"http-header","HttpHeaderConfig":{"HttpHeaderName":"User-Agent","Values":["*Mobile*","*Android*","*iPhone*"]}}]' \
    --actions "Type=redirect,RedirectConfig={Host=`m.example.com`,StatusCode=HTTP_302}"
```

CloudFormation

###### To add a rule

Define a resource of type [AWS::ElasticLoadBalancingV2::ListenerRule](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.md").

The following example creates a rule with a `forward` action
and a `host-header` condition. The rule sends traffic to the
specified target group when the condition is met.

```
Resources:
    myForwardListenerRule:
     Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
     Properties:
       ListenerArn: !Ref myListener
       Priority: `10`
       Conditions:
         - Field: host-header
           Values:
             - `example.com`
             - `www.example.com`
       Actions:
         - Type: forward
           TargetGroupArn: !Ref myTargetGroup

```

Alternatively, to create a forward action that distributes traffic between
two target groups when the condition is met, define `Actions` as
follows.

```
       Actions:
         - Type: forward
           ForwardConfig:
             TargetGroups:
               - TargetGroupArn: !Ref TargetGroup1
                 Weight: `50`
               - TargetGroupArn: !Ref TargetGroup2
                 Weight: `50`
```

The following example creates a rule with a `fixed-response` action
and a `source-ip` condition.

```
Resources:
    myFixedResponseListenerRule:
     Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
     Properties:
       ListenerArn: !Ref myListener
       Priority: `20`
       Conditions:
         - Field: source-ip
           SourceIpConfig:
             Values:
                - `192.168.1.0/24`
                - `10.0.0.0/16`
       Actions:
         - Type: fixed-response
           FixedResponseConfig:
             StatusCode: 403
             ContentType: text/plain
             MessageBody: "`Access denied`"
```

The following example creates a rule with a `redirect` action
and an `http-header` condition.

```
Resources:
    myRedirectListenerRule:
     Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
     Properties:
       ListenerArn: !Ref myListener
       Priority: `30`
       Conditions:
         - Field: http-header
           HttpHeaderConfig:
             HttpHeaderName: User-Agent
             Values:
               - "*Mobile*"
               - "*Android*"
               - "*iPhone*"
       Actions:
         - Type: redirect
           RedirectConfig:
             Host: `m.example.com`
             StatusCode: HTTP_302
```
