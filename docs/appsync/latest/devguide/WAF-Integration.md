# Using AWS WAF to protect your AWS AppSync APIs

AWS WAF is a web application firewall that helps protect web applications and APIs from
attacks. It allows you to configure a set of rules, called a web access control list (web
ACL), that allow, block, or monitor (count) web requests based on customizable web security
rules and conditions that you define. When you integrate your AWS AppSync API with AWS WAF, you
gain more control and visibility into the HTTP traffic accepted by your API. To learn more
about AWS WAF, see [How AWS WAF Works](../../../waf/latest/developerguide/how-aws-waf-works.md "../../../waf/latest/developerguide/how-aws-waf-works.md") in
the AWS WAF Developer Guide.

You can use AWS WAF to protect your AppSync API from common web exploits, such as SQL
injection and cross-site scripting (XSS) attacks. These could affect API availability and
performance, compromise security, or consume excessive resources. For example, you can
create rules to allow or block requests from specified IP address ranges, requests from CIDR
blocks, requests that originate from a specific country or region, requests that contain
malicious SQL code, or requests that contain malicious script.

You can also create rules that match a specified string or a regular expression pattern in
HTTP headers, method, query string, URI, and the request body (limited to the first 8 KB).
Additionally, you can create rules to block attacks from specific user agents, bad bots, and
content scrapers. For example, you can use rate-based rules to specify the number of web
requests that are allowed by each client IP in a trailing, continuously updated, 5-minute
period.

To learn more about the types of rules that are supported and additional AWS WAF features,
see the [AWS WAF Developer Guide](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md") and the [AWS WAF API
Reference](../../../waf/latest/APIReference/API_Types_AWS_WAFV2.md "../../../waf/latest/APIReference/API_Types_AWS_WAFV2.md").

###### Important

AWS WAF is your first line of defense against web exploits. When AWS WAF is enabled on an
API, AWS WAF rules are evaluated before other access control features, such as API key
authorization, IAM policies, OIDC tokens, and Amazon Cognito user pools.

## Integrate an AppSync API with AWS WAF

You can integrate an Appsync API with AWS WAF using the AWS Management Console, the AWS CLI, AWS CloudFormation,
or any other compatible client.

###### To integrate an AWS AppSync API with AWS WAF

1. Create an AWS WAF web ACL. For detailed steps using the [AWS WAF Console](https://console.aws.amazon.com/waf/ "https://console.aws.amazon.com/waf/"), see [Creating a web
   ACL](../../../waf/latest/developerguide/web-acl-creating.md "../../../waf/latest/developerguide/web-acl-creating.md").
2. Define the rules for the web ACL. A rule or rules are defined in the process
   of creating the web ACL. For information about how to structure rules, see
   [AWS WAF rules](../../../waf/latest/developerguide/waf-rules.md "../../../waf/latest/developerguide/waf-rules.md"). For examples of useful rules you can define for
   your AWS AppSync API, see [Creating rules for a web ACL](#Creating-web-acl-rules "#Creating-web-acl-rules").
3. Associate the web ACL with an AWS AppSync API. You can perform this step in the
   [AWS WAF Console](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/") or in the
   [AppSync Console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
   - To associate the web ACL with an AWS AppSync API in the AWS WAF Console,
     follow the instructions for [Associating or disassociating a Web ACL with an AWS
     resource](../../../waf/latest/developerguide/web-acl-associating-aws-resource.md "../../../waf/latest/developerguide/web-acl-associating-aws-resource.md") in the AWS WAF Developer Guide.
   - To associate the web ACL with an AWS AppSync API in the AWS AppSync
     Console
     1. Sign in to the AWS Management Console and open the [AppSync Console](https://console.aws.amazon.com/appsync/ "https://console.aws.amazon.com/appsync/").
     2. Choose the API that you want to associate with a web
        ACL.
     3. In the navigation pane, choose
        **Settings**.
     4. In the **Web application firewall** section,
        turn on **Enable AWS WAF**.
     5. In the **Web ACL** dropdown list, choose the
        name of the web ACL to associate with your API.
     6. Choose **Save** to associate the web ACL with
        your API.

###### Note

After you create a web ACL in the AWS WAF Console, it can take a few minutes for the
new web ACL to be available. If you do not see a newly created web ACL in the
**Web application firewall** menu, wait a few minutes and retry
the steps to associate the web ACL with your API.

###### Note

AWS WAF integration only supports the `Subscription registration message` event for real-time
endpoints. AWS AppSync will respond with an error message instead of a `start_ack` message for any
`Subscription registration message` blocked by AWS WAF.

After you associate a web ACL with an AWS AppSync API, you will manage the web ACL using
the AWS WAF APIs. You do not need to re-associate the web ACL with your AWS AppSync API unless
you want to associate the AWS AppSync API with a different web ACL.

## Creating rules for a web ACL

Rules define how to inspect web requests and what to do when a web request matches the
inspection criteria. Rules don't exist in AWS WAF on their own. You can access a rule
by name in a rule group or in the web ACL where it's defined. For more information, see
[AWS WAF
rules](../../../waf/latest/developerguide/waf-rules.md "../../../waf/latest/developerguide/waf-rules.md"). The following examples demonstrate how to define and associate rules
that are useful for protecting an AppSync API.

###### Example web ACL rule to limit request body size

The following is an example of a rule that limits the body size of requests. This
would be entered into the **Rule JSON editor** when creating a web
ACL in the AWS WAF Console.

```
{
    "Name": "BodySizeRule",
    "Priority": 1,
    "Action": {
        "Block": {}
    },
    "Statement": {
        "SizeConstraintStatement": {
            "ComparisonOperator": "GE",
            "FieldToMatch": {
                "Body": {}
            },
            "Size": 1024,
            "TextTransformations": [
                {
                    "Priority": 0,
                    "Type": "NONE"
                }
             ]
          }
       },
       "VisibilityConfig": {
           "CloudWatchMetricsEnabled": true,
           "MetricName": "BodySizeRule",
           "SampledRequestsEnabled": true
        }
}
```

After you have created your web ACL using the preceding example rule, you must
associate it with your AppSync API. As an alternative to using the AWS Management Console, you
can perform this step in the AWS CLI by running the following command.

```
`aws waf associate-web-acl --web-acl-id `waf-web-acl-arn` --resource-arn `appsync-api-arn``
```

It can take a few minutes for the changes to propagate, but after running this
command, requests that contain a body larger than 1024 bytes will be rejected by
AWS AppSync.

###### Note

After you create a new web ACL in the AWS WAF Console, it can take a few minutes
for the web ACL to be available to associate with an API. If you run the CLI
command and get a `WAFUnavailableEntityException`
error, wait a few minutes and retry running the command.

###### Example web ACL rule to limit requests from a single IP address

The following is an example of a rule that throttles an AppSync API to 100 requests from a single IP
address. This would be entered into the **Rule JSON editor** when creating a web ACL
with a rate-based rule in the AWS WAF Console.

```
{
  "Name": "Throttle",
  "Priority": 0,
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "Throttle"
  },
  "Statement": {
    "RateBasedStatement": {
      "Limit": 100,
      "AggregateKeyType": "IP"
    }
  }
}
```

After you have created your web ACL using the preceding example rule, you must
associate it with your AppSync API. You can perform this step in the AWS CLI by
running the following command.

```
`aws waf associate-web-acl --web-acl-id `waf-web-acl-arn` --resource-arn `appsync-api-arn``
```

###### Example web ACL rule to prevent GraphQL \_\_schema introspection queries to an API

The following is an example of a rule that prevents GraphQL \_\_schema introspection
queries to an API. Any HTTP body that includes the string "\_\_schema" will be
blocked. This would be entered into the **Rule JSON editor** when
creating a web ACL in the AWS WAF Console.

```
{
  "Name": "BodyRule",
  "Priority": 5,
  "Action": {
    "Block": {}
  },
  "VisibilityConfig": {
    "SampledRequestsEnabled": true,
    "CloudWatchMetricsEnabled": true,
    "MetricName": "BodyRule"
  },
  "Statement": {
    "ByteMatchStatement": {
      "FieldToMatch": {
        "Body": {}
      },
      "PositionalConstraint": "CONTAINS",
      "SearchString": "__schema",
      "TextTransformations": [
        {
          "Type": "NONE",
          "Priority": 0
        }
      ]
    }
  }
}
```

After you have created your web ACL using the preceding example rule, you must
associate it with your AppSync API. You can perform this step in the AWS CLI by
running the following command.

```
`aws waf associate-web-acl --web-acl-id `waf-web-acl-arn` --resource-arn `appsync-api-arn``
```
