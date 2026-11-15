

# Traffic policies and policy statements
<a name="eb-filters"></a>

A traffic policy provides firewall-like filtering for incoming Simple Mail Transfer Protocol (SMTP) traffic at an ingress endpoint. With a traffic policy, you protect the ingress endpoint and downstream mail systems by allowing or rejecting recipients before accepted messages enter rule set processing.

Each policy statement checks information available while an email is being received, such as the recipient address, sender IPv4 or IPv6 address, Transport Layer Security (TLS) version, address list membership, or an Email Add On result. A matching statement applies an `ALLOW` or `DENY` action. You can also set a maximum message size in bytes when you create or update the traffic policy. Use this setting to prevent messages that are larger than your downstream mail systems can accept or process from entering rule set processing.

An ingress endpoint references one traffic policy and one rule set. The traffic policy checks each recipient before the rule set processes the message. If the recipient is accepted and the message is within the maximum message size, Mail Manager passes the message to the rule set. A traffic policy is reusable and can be assigned to multiple ingress endpoints.

You define policy statements when you create or update the traffic policy. Policy statements are not separate resources.

## How traffic policy evaluation works
<a name="eb-filters-how-it-works"></a>

A traffic policy contains one or more policy statements. Each statement has one action and one or more conditions. Each condition contains one expression. String and IP expressions contain one or more comparison values.

****How traffic policy elements combine****  
Any listed value can make an expression match. Every condition must match before its statement matches. Any statement with the same action can match. The following diagram shows how these levels connect:
+ Within one expression, any listed value can match. For example, a recipient that ends with `@example.com` or `@example.org` matches a `RECIPIENT` expression that uses `ENDS_WITH`.
+ Within one statement, every condition must match. For example, the sender IP must be in `192.0.2.0/24` and the recipient must end with `@example.com`.
+ Among statements with the same action, any statement can match. For example, separate `ALLOW` statements can match `mary_major@example.com` or `sofia_martinez@example.com`.

Read the following diagram from left to right. In the first panel, either recipient suffix makes the expression match. In the second panel, the sender IP and recipient conditions must both match. In the third panel, either `ALLOW` statement can match.

![The first panel shows that either recipient suffix can make an expression match. The second panel shows that the sender IP and recipient conditions must both match. The third panel shows that either allow statement can match.](https://docs.aws.amazon.com/ses/latest/dg/images/traffic-policy-elements.png)


Any listed value can make an expression match. Every condition must match before its statement matches. Any statement with the same action can match. The policy evaluates `DENY` statements before `ALLOW` statements, and then applies the default action if needed.

The traffic policy evaluates `DENY` statements first. A match rejects the recipient. If none match and the default action is `ALLOW`, the default action accepts the recipient without evaluating `ALLOW` statements. If the default action is `DENY`, the policy evaluates `ALLOW` statements. The first match accepts the recipient. If none match, the default `DENY` action rejects the recipient. The following diagram shows these branches:

![A left-to-right flow shows deny statements, allow statements when the default action is deny, and the default action when no statement matches.](https://docs.aws.amazon.com/ses/latest/dg/images/traffic-policy-evaluation-order.png)


### Combining policy elements
<a name="eb-filters-combination-semantics"></a>

*Any listed value can match.* With `EQUALS`, `STARTS_WITH`, `ENDS_WITH`, `CONTAINS`, or `CIDR_MATCHES`, an expression matches when the value being checked matches at least one entry in the `Values` list. In the following example, `mary_major@example.com` and `mary_major@example.org` both match:

```
{
  "StringExpression": {
    "Evaluate": {"Attribute": "RECIPIENT"},
    "Operator": "ENDS_WITH",
    "Values": ["@example.com", "@example.org"]
  }
}
```

With `NOT_EQUALS` or `NOT_CIDR_MATCHES`, an expression matches only when the value being checked matches none of the listed values.

*Every condition in a statement must match.* The statement's action applies only after all its conditions match. The following statement allows a recipient only when the sender is in `192.0.2.0/24` and the recipient address ends with `@example.com`:

```
{
  "Action": "ALLOW",
  "Conditions": [
    {
      "IpExpression": {
        "Evaluate": {"Attribute": "SENDER_IP"},
        "Operator": "CIDR_MATCHES",
        "Values": ["192.0.2.0/24"]
      }
    },
    {
      "StringExpression": {
        "Evaluate": {"Attribute": "RECIPIENT"},
        "Operator": "ENDS_WITH",
        "Values": ["@example.com"]
      }
    }
  ]
}
```

*A match on any statement with the same action is enough.* Statements are checked in their policy order. The first matching statement applies its action, and later statements with that action are not checked. In the following example, either `mary_major@example.com` or `sofia_martinez@example.com` matches an `ALLOW` statement:

```
{
  "DefaultAction": "DENY",
  "PolicyStatements": [
    {
      "Action": "ALLOW",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "EQUALS",
          "Values": ["mary_major@example.com"]
        }
      }]
    },
    {
      "Action": "ALLOW",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "EQUALS",
          "Values": ["sofia_martinez@example.com"]
        }
      }]
    }
  ]
}
```

**Use an address list for a large recipient set**  
To allow a large number of recipients, store them in an address list instead of creating one statement for each recipient. One address-list membership condition can allow every matching recipient.  
In the following example, replace the AWS Region, account ID, and address list ID with your own values. The policy statement allows every recipient in the address list:  

```
{
  "Action": "ALLOW",
  "Conditions": [{
    "BooleanExpression": {
      "Evaluate": {
        "IsInAddressList": {
          "Attribute": "RECIPIENT",
          "AddressLists": ["arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"]
        }
      },
      "Operator": "IS_TRUE"
    }
  }]
}
```
For instructions on creating and maintaining address lists, see [Address Lists](eb-addlist.md).

### Evaluating policy statements in order
<a name="eb-filters-evaluation-order"></a>

The traffic policy applies the value and condition logic described in [Combining policy elements](#eb-filters-combination-semantics). For each SMTP recipient, it evaluates statements in the following order:

1. The traffic policy evaluates `DENY` statements first, in the order in which they appear in the policy. The first matching `DENY` statement stops evaluation and rejects the recipient.

1. If no `DENY` statement matches and the default action is `ALLOW`, the default action accepts the recipient. The `ALLOW` statements are not evaluated.

1. If no `DENY` statement matches and the default action is `DENY`, the traffic policy evaluates `ALLOW` statements in the order in which they appear in the policy. The first matching `ALLOW` statement stops evaluation and accepts the recipient.

1. If no `ALLOW` statement matches, the default `DENY` action rejects the recipient.

**Note**  
A matching `DENY` statement always takes precedence over a matching `ALLOW` statement because all `DENY` statements are evaluated first.

### Reviewing evaluation examples
<a name="eb-filters-evaluation-examples"></a>

The following JSON fragments include only the fields needed to show evaluation behavior.

The following policy uses a default `DENY` action with a `DENY` statement and an `ALLOW` statement:

```
{
  "DefaultAction": "DENY",
  "PolicyStatements": [
    {
      "Action": "DENY",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "EQUALS",
          "Values": ["mary_major@example.com"]
        }
      }]
    },
    {
      "Action": "ALLOW",
      "Conditions": [{
        "StringExpression": {
          "Evaluate": {"Attribute": "RECIPIENT"},
          "Operator": "ENDS_WITH",
          "Values": ["@example.com"]
        }
      }]
    }
  ]
}
```
+ `mary_major@example.com` matches both statements. The `DENY` statement is evaluated first and rejects the recipient.
+ `sofia_martinez@example.com` does not match the `DENY` statement. It matches the `ALLOW` statement and is accepted.
+ `mary_major@other.example` matches neither statement. The default `DENY` action rejects the recipient.

The following policy uses a default `ALLOW` action with a `DENY` statement:

```
{
  "DefaultAction": "ALLOW",
  "PolicyStatements": [{
    "Action": "DENY",
    "Conditions": [{
      "IpExpression": {
        "Evaluate": {"Attribute": "SENDER_IP"},
        "Operator": "CIDR_MATCHES",
        "Values": ["192.0.2.0/24"]
      }
    }]
  }]
}
```

A sender in `192.0.2.0/24` matches the `DENY` statement and is rejected. If the sender is outside that range, no `DENY` statement matches and the default `ALLOW` action accepts the recipient.

**Default ALLOW is not recommended**  
This example shows how `DefaultAction` works. Using `ALLOW` as the default action is not recommended. It accepts all traffic that does not match a `DENY` statement. This includes traffic that you did not explicitly approve. Use `DENY` as the default action and add explicit `ALLOW` statements for the traffic that the ingress point must accept.

### Setting the maximum message size
<a name="eb-filters-max-message-size"></a>

Specify the maximum message size in bytes when you create or update the traffic policy. This setting is separate from policy statement matching. A message that is larger than this limit is rejected before it passes to the rule set. Set the limit to match what your downstream mail systems can store and process.

For example, `31457280` bytes is 30 mebibytes (MiB), calculated as 30 multiplied by 1,024 multiplied by 1,024. If you set the maximum message size to `31457280`, the traffic policy rejects messages larger than 30 MiB.

### Understanding charges for received messages
<a name="eb-filters-charges"></a>

**Note**  
Mail Manager message-processing charges apply only after the traffic policy accepts at least one recipient and Mail Manager receives the message. If the traffic policy rejects every recipient, the message is not counted as a received message for this charge.

Email Add On usage is metered separately when the add-on is invoked during traffic policy evaluation. This usage can be metered even when the traffic policy rejects the recipient. For current prices, see [SES pricing](https://aws.amazon.com/ses/pricing/).

## Traffic policy examples
<a name="eb-filters-examples"></a>

The following examples use example IP address ranges. In each example, replace the IP address ranges, recipient domain, traffic policy name, and AWS Region with your own values. Both `create-traffic-policy` commands set the maximum message size to `31457280` bytes (30 MiB).

### Example: Allowing only an approved IPv4 sender range
<a name="eb-filters-example-ipv4-allowlist"></a>

This policy uses `DENY` as its default action. Its `ALLOW` statement accepts recipients when the connecting sender's IPv4 address is in `192.0.2.0/24`. The default action rejects all other recipients. In the following AWS CLI command, replace the AWS Region, traffic policy name, and IPv4 range with your own values. The command creates this traffic policy:

```
PROMPT> aws mailmanager create-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-name {{allow-ipv4-partner}} \
  --policy-statements '[{
    "Action": "ALLOW",
    "Conditions": [{
      "IpExpression": {
        "Evaluate": {"Attribute": "SENDER_IP"},
        "Operator": "CIDR_MATCHES",
        "Values": ["192.0.2.0/24"]
      }
    }]
  }]' \
  --default-action DENY \
  --max-message-size-bytes 31457280
```

### Example: Allowing only approved IPv4 and IPv6 partner traffic
<a name="eb-filters-example-default-deny-allowlist"></a>

This policy uses `DENY` as its default action. One `ALLOW` statement accepts mail from the partner's IPv4 range, and a second `ALLOW` statement accepts mail from its IPv6 range. In both cases, the recipient must end with `@example.com`. The two statements are alternatives, but both conditions within a statement must match. The default action rejects all other recipients. In the following AWS CLI command, replace the AWS Region, traffic policy name, IPv4 and IPv6 ranges, and recipient domain with your own values. The command creates this traffic policy:

```
PROMPT> aws mailmanager create-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-name {{allow-partner-dual-stack}} \
  --policy-statements '[
    {
      "Action": "ALLOW",
      "Conditions": [
        {
          "IpExpression": {
            "Evaluate": {"Attribute": "SENDER_IP"},
            "Operator": "CIDR_MATCHES",
            "Values": ["192.0.2.0/24"]
          }
        },
        {
          "StringExpression": {
            "Evaluate": {"Attribute": "RECIPIENT"},
            "Operator": "ENDS_WITH",
            "Values": ["@example.com"]
          }
        }
      ]
    },
    {
      "Action": "ALLOW",
      "Conditions": [
        {
          "Ipv6Expression": {
            "Evaluate": {"Attribute": "SENDER_IPV6"},
            "Operator": "CIDR_MATCHES",
            "Values": ["2001:db8:1234::/48"]
          }
        },
        {
          "StringExpression": {
            "Evaluate": {"Attribute": "RECIPIENT"},
            "Operator": "ENDS_WITH",
            "Values": ["@example.com"]
          }
        }
      ]
    }
  ]' \
  --default-action DENY \
  --max-message-size-bytes 31457280
```

### Understanding overlapping policy statements
<a name="eb-filters-example-deny-precedence"></a>

Suppose one statement allows `mary_major@example.com` and another statement denies the sender range `192.0.2.0/24`. A message for `mary_major@example.com` from that sender range is rejected. The matching `DENY` statement stops evaluation before the `ALLOW` statements are evaluated.

## Using Email Add Ons in a traffic policy
<a name="eb-filters-addons"></a>

An Email Add On can add sender reputation information to traffic policy evaluation. The traffic policy evaluates this information during the SMTP transaction. This happens before an accepted message passes to the rule set. You can combine an Email Add On condition with recipient, sender IP, TLS, or address list conditions in the same policy statement.

Using an Email Add On in a traffic policy provides the following benefits.
+ Managed reputation data can block listed senders before message content is accepted.
+ Provider-specific result categories let you create narrower conditions than a single listed or not-listed result.
+ The same add-on instance can be referenced by policy statements without operating a separate reputation service.

Before you use an Email Add On condition, subscribe to the Email Add On, create an add-on instance, and copy its `AddonInstanceArn`. For information about subscribing to an add-on and creating an add-on instance, see [Email Add Ons](eb-addons.md). The add-on instance must belong to the same AWS account as the traffic policy.

The following table lists the Email Add On results available to traffic policies.


**Email Add On results available to traffic policies**  

| Email Add On | Result field | Use | 
| --- | --- | --- | 
| Abusix Mail Intelligence | isListed | Use a boolean expression with IS\_TRUE or IS\_FALSE. | 
| Abusix Mail Intelligence | listedOn | Use a string expression with EQUALS or NOT\_EQUALS and a value such as Spam, Exploit, or Policy. | 
| Spamhaus Domain Block List | isListed | Use a boolean expression with IS\_TRUE or IS\_FALSE. | 
| Spamhaus Domain Block List | listedOn | Use a string expression with EQUALS or NOT\_EQUALS and a value such as SBL or XBL. | 

The following example allows a recipient when the add-on result field `isListed` is false. The default `DENY` action rejects traffic that does not match this explicit `ALLOW` statement. In the following AWS CLI command, replace the Region, account ID, add-on instance ID, and traffic policy name with your own values. The command sets the maximum message size to `31457280` bytes (30 MiB):

```
PROMPT> aws mailmanager create-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-name {{allow-unlisted-senders}} \
  --policy-statements '[{
    "Action": "ALLOW",
    "Conditions": [{
      "BooleanExpression": {
        "Evaluate": {
          "Analysis": {
            "Analyzer": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:addon-instance/{{ai-0123456789abcdef}}",
            "ResultField": "isListed"
          }
        },
        "Operator": "IS_FALSE"
      }
    }]
  }]' \
  --default-action DENY \
  --max-message-size-bytes 31457280
```

**Note**  
Email Add Ons can add charges and processing time. Review the provider terms and [SES pricing](https://aws.amazon.com/ses/pricing/) before enabling an add-on condition. Test the condition against representative legitimate and unwanted traffic before using it to reject mail.

**Note**  
Email Add On conditions are not applied to messages received through IPv6 connections. On a dual-stack ingress endpoint, these conditions apply only to messages received through IPv4 connections. Native `Ipv6Expression` conditions can still filter IPv6 sender ranges.

You cannot delete an add-on instance while a traffic policy or rule set references it. Remove the reference before deleting the add-on instance.

## Managing traffic policies and ingress point associations with the AWS CLI
<a name="eb-filters-cli"></a>

The `create-traffic-policy` commands in the preceding examples return a `TrafficPolicyId`. The following commands use `tp-0123456789abcdef01234567` as that ID and `rs-0123456789abcdef01234567` as the ID of an existing rule set. Replace these IDs and the AWS Region with your own values.

### Updating and inspecting a traffic policy
<a name="eb-filters-cli-update-policy"></a>

Traffic policy properties that you omit from an update request remain unchanged. In the following AWS CLI command, replace the AWS Region and traffic policy ID with your own values. The command sets the maximum message size to `31457280` bytes (30 MiB):

```
PROMPT> aws mailmanager update-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --max-message-size-bytes 31457280
```

In the following command, replace the AWS Region and traffic policy ID with your own values. Use `get-traffic-policy` to inspect the complete policy:

```
PROMPT> aws mailmanager get-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}}
```

In the following command, replace the AWS Region with your own value. Use `list-traffic-policies` to list the traffic policies in the Region:

```
PROMPT> aws mailmanager list-traffic-policies \
  --region {{us-east-1}}
```

**Note**  
When you supply `--policy-statements` in an update, supply the complete list of policy statements that the policy must contain.

### Assigning a traffic policy when creating an ingress point
<a name="eb-filters-cli-create-ingress"></a>

An ingress point requires an existing traffic policy and rule set. In the following AWS CLI command, replace the AWS Region, ingress point name, rule set ID, and traffic policy ID with your own values. The command creates an open ingress point and assigns both resources:

```
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-name {{partner-ingress}} \
  --type OPEN \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --tls-policy REQUIRED
```

The command returns an `IngressPointId`. For all request options, see [CreateIngressPoint](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateIngressPoint.html) in the *SES Mail Manager API Reference*.

### Changing the traffic policy assigned to an ingress point
<a name="eb-filters-cli-update-ingress"></a>

Other ingress point properties remain unchanged. In the following AWS CLI command, replace the AWS Region, ingress point ID, and traffic policy ID with your own values. The command changes the traffic policy assigned to the ingress point:

```
PROMPT> aws mailmanager update-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-fedcba9876543210fedcba98}}
```

In the following command, replace the AWS Region and ingress point ID with your own values. Run `get-ingress-point` and check that the response contains the expected `TrafficPolicyId` and `RuleSetId`:

```
PROMPT> aws mailmanager get-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}}
```

### Deleting a traffic policy
<a name="eb-filters-cli-delete-policy"></a>

You cannot delete a traffic policy while an ingress point references it. First, update every ingress point that references the policy to use another traffic policy. In the following AWS CLI command, replace the AWS Region and traffic policy ID with your own values. Then run the command to delete the unused policy:

```
PROMPT> aws mailmanager delete-traffic-policy \
  --region {{us-east-1}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}}
```

## Permissions for traffic policies and ingress points
<a name="eb-filters-permissions"></a>

The principal that manages traffic policies needs permission for the traffic policy API operations that it uses. The principal that creates or updates an ingress endpoint also needs permission for the corresponding ingress point API operation.

In the following IAM policy, replace the AWS Region, account ID, traffic policy IDs, rule set ID, and ingress point ID with your own values. The policy allows a principal to manage traffic policies in one account, create an open ingress point only with an approved traffic policy and rule set, and update one ingress point only when assigning an approved traffic policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageTrafficPolicies",
      "Effect": "Allow",
      "Action": [
        "ses:CreateTrafficPolicy",
        "ses:GetTrafficPolicy",
        "ses:UpdateTrafficPolicy",
        "ses:DeleteTrafficPolicy"
      ],
      "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-traffic-policy/*"
    },
    {
      "Sid": "ListTrafficPolicies",
      "Effect": "Allow",
      "Action": "ses:ListTrafficPolicies",
      "Resource": "*"
    },
    {
      "Sid": "CreateIngressPointWithApprovedResources",
      "Effect": "Allow",
      "Action": "ses:CreateIngressPoint",
      "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-ingress-point/*",
      "Condition": {
        "StringEquals": {
          "ses:MailManagerIngressPointType": "OPEN",
          "ses:MailManagerTrafficPolicyArn": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-traffic-policy/{{tp-0123456789abcdef01234567}}",
          "ses:MailManagerRuleSetArn": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-rule-set/{{rs-0123456789abcdef01234567}}"
        }
      }
    },
    {
      "Sid": "GetOneIngressPoint",
      "Effect": "Allow",
      "Action": "ses:GetIngressPoint",
      "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-ingress-point/{{inp-0123456789abcdef01234567}}"
    },
    {
      "Sid": "UpdateOneIngressPointToApprovedPolicy",
      "Effect": "Allow",
      "Action": "ses:UpdateIngressPoint",
      "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-ingress-point/{{inp-0123456789abcdef01234567}}",
      "Condition": {
        "StringEquals": {
          "ses:MailManagerTrafficPolicyArn": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-traffic-policy/{{tp-fedcba9876543210fedcba98}}"
        }
      }
    }
  ]
}
```

The `ses:MailManagerTrafficPolicyArn`, `ses:MailManagerRuleSetArn`, and `ses:MailManagerIngressPointType` condition keys restrict the resources that can be assigned when an ingress point is created or updated.

**Note**  
Condition keys are included in the request context only when the corresponding value is supplied. The conditional `UpdateIngressPoint` statement in this example authorizes an update that supplies `TrafficPolicyId`. Use a separate statement to authorize updates that do not change the traffic policy.

If the SES service-linked role does not exist in the account, the principal that creates the first ingress endpoint also needs `iam:CreateServiceLinkedRole` permission with the `iam:AWSServiceName` condition set to `ses.amazonaws.com`. A request that adds tags also requires `ses:TagResource`.

## Creating traffic policies and policy statements in the SES console
<a name="eb-filters-create-console"></a>

The following procedure shows you how to use the **Traffic policies** page in the SES console to create traffic policies and their policy statements, and manage the ones you've already created.

**To create and manage traffic policies and policy statements using the console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Traffic policies** under **Mail Manager**.

1. On the **Traffic policies** page, select **Create traffic policy**.

1. On the **Create a traffic policy** page, enter a unique name for your traffic policy.

1. (Optional) To reject messages above a maximum size, enter the size in bytes in the **Maximum message size** field.

1. In **Default action**, choose **Allow** or **Deny**. This action applies as described in [How traffic policy evaluation works](#eb-filters-how-it-works).

1. Select **Add new policy statement** to create a statement for your traffic policy.

1. Choose either **Allow** or **Deny** (block) for the action to be taken when the statement's conditions are met.

1. Build a condition by selecting an email property and a conditional operator for the value you enter. Select **Add new condition** if you want to add more conditions to this policy statement. *To learn more about a condition property and its operators and valid values, see the [Policy statement conditions](#filter-conditions) reference.*

   If you subscribed to an [Email Add On](eb-addons.md), you can select its supported result fields as condition properties. For more information about using Email Add On results, see [Using Email Add Ons in a traffic policy](#eb-filters-addons).

1. To add more policy statements and conditions, repeat steps 7–9.

1. When you're done creating policy statements and their conditions, select **Create traffic policy**.

1. You can view and manage existing traffic policies from the **Traffic policies** page. To delete a traffic policy, select its radio button, and then choose **Delete**.

1. To edit a traffic policy's properties or policy statements, choose its name to open its overview page. Then choose **Edit**.

1. In **Traffic policy details**, you can change the maximum message size and default action.

1. In each **Policy statement** container, you can change the action and edit its conditions. You can also add or remove policy statements and conditions.

1. When you're done with all your edits, save your changes by selecting **Save changes**.

## Reference for policy statement conditions
<a name="eb-filters-reference"></a>

**Policy statement conditions**  
Each item in the following list describes a supported condition, its operators, and a small JSON fragment. Place one of these condition objects in a policy statement's `Conditions` list. Follow the expression link for complete API field constraints.

Recipient address  
Use a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressStringExpression.html) with `EQUALS`, `NOT_EQUALS`, `STARTS_WITH`, `ENDS_WITH`, or `CONTAINS`. The following example matches recipients in a domain:  

```
{
  "StringExpression": {
    "Evaluate": {"Attribute": "RECIPIENT"},
    "Operator": "ENDS_WITH",
    "Values": ["@example.com"]
  }
}
```

Sender IPv4 range  
Use an [IPv4 expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIpv4Expression.html) with `CIDR_MATCHES` or `NOT_CIDR_MATCHES`. The following example matches a sender in an IPv4 range:  

```
{
  "IpExpression": {
    "Evaluate": {"Attribute": "SENDER_IP"},
    "Operator": "CIDR_MATCHES",
    "Values": ["192.0.2.0/24"]
  }
}
```

Sender IPv6 range  
Use an [IPv6 expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressIpv6Expression.html) with `CIDR_MATCHES` or `NOT_CIDR_MATCHES`. The following example matches a sender in an IPv6 range:  

```
{
  "Ipv6Expression": {
    "Evaluate": {"Attribute": "SENDER_IPV6"},
    "Operator": "CIDR_MATCHES",
    "Values": ["2001:db8:1234::/48"]
  }
}
```

TLS protocol version  
Use a [TLS expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressTlsProtocolExpression.html) with `IS` or `MINIMUM_TLS_VERSION`. Supported values are `TLS1_2` and `TLS1_3`. The following example requires TLS 1.2 or later:  

```
{
  "TlsExpression": {
    "Evaluate": {"Attribute": "TLS_PROTOCOL"},
    "Operator": "MINIMUM_TLS_VERSION",
    "Value": "TLS1_2"
  }
}
```

Recipient address list membership  
Use `IsInAddressList` in a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressBooleanExpression.html) with `IS_TRUE` or `IS_FALSE`. For instructions on creating and maintaining address lists, see [Address Lists](eb-addlist.md). In the following example, replace the AWS Region, account ID, and address list ID with your own values. The condition matches recipients in the address list:  

```
{
  "BooleanExpression": {
    "Evaluate": {
      "IsInAddressList": {
        "Attribute": "RECIPIENT",
        "AddressLists": ["arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/{{al-0123456789abcdef}}"]
      }
    },
    "Operator": "IS_TRUE"
  }
}
```

Email Add On list category  
Use an `Analysis` operand for the `listedOn` result in a [string expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressStringExpression.html) with `EQUALS` or `NOT_EQUALS`. For information about provider-specific values, see [Using Email Add Ons in a traffic policy](#eb-filters-addons). In the following example, replace the AWS Region, account ID, and add-on instance ID with your own values. The condition matches the `Spam` category:  

```
{
  "StringExpression": {
    "Evaluate": {
      "Analysis": {
        "Analyzer": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:addon-instance/{{ai-0123456789abcdef}}",
        "ResultField": "listedOn"
      }
    },
    "Operator": "EQUALS",
    "Values": ["Spam"]
  }
}
```

Email Add On listed status  
Use an `Analysis` operand for the `isListed` result in a [boolean expression](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressBooleanExpression.html) with `IS_TRUE` or `IS_FALSE`. For information about Email Add On results, see [Using Email Add Ons in a traffic policy](#eb-filters-addons). In the following example, replace the AWS Region, account ID, and add-on instance ID with your own values. The condition matches a listed sender:  

```
{
  "BooleanExpression": {
    "Evaluate": {
      "Analysis": {
        "Analyzer": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:addon-instance/{{ai-0123456789abcdef}}",
        "ResultField": "isListed"
      }
    },
    "Operator": "IS_TRUE"
  }
}
```

**Recipient address matching and subaddressing**  
The *Recipient address* property evaluates the SMTP envelope recipient mailbox without its display name. The comparison ignores letter case. A subaddress extension, also known as plus addressing, remains part of the mailbox. For example, the value evaluated for `mary_major+tag@example.com` is `mary_major+tag@example.com`, not `mary_major@example.com`.  
An `EQUALS` condition for `mary_major@example.com` does not match `mary_major+tag@example.com`. To match recipients in the domain, use `ENDS_WITH` and the value `@example.com`. You can also use an address list when you need to manage a set of recipient patterns.

## Recommendations for traffic policies
<a name="eb-filters-recommendations"></a>
+ Use `DENY` as the default action. It rejects traffic that does not match an explicit `ALLOW` statement. Using `ALLOW` as the default action is not recommended. It accepts all traffic that does not match a `DENY` statement. This includes traffic that you did not explicitly approve.
+ Define separate IPv4 and IPv6 conditions for a dual-stack ingress point when the policy must filter both address families. An `IpExpression` does not evaluate an IPv6 sender address, and an `Ipv6Expression` does not evaluate an IPv4 sender address.
+ Use multiple conditions in one statement to narrow a match. For example, combine a sender range, recipient domain, and minimum TLS version for a partner integration.
+ Use `MINIMUM_TLS_VERSION` with `TLS1_2` or `TLS1_3` when the sender must use a minimum TLS version. The traffic policy condition evaluates the negotiated version. The ingress point TLS policy separately controls whether TLS is required.
+ Treat an Email Add On result as one signal. Test it against representative legitimate and unwanted traffic before using the result to reject mail.
+ Set the maximum message size according to your application requirements. Account for message headers and MIME encoding when calculating the expected message size.

### Monitoring traffic policy evaluation
<a name="eb-filters-monitoring"></a>

Enable `TRAFFIC_POLICY_DEBUG_LOGS` before changing which traffic is accepted. These logs include evaluations for accepted and rejected recipients. For setup instructions and the log record format, see [Ingress endpoint logs – `TRAFFIC_POLICY_DEBUG_LOGS`](eb-logging.md#ingress-endpoint-logs-traffic).

The following CloudWatch Logs Logs Insights query returns rejected traffic policy evaluations:

```
fields @timestamp, traffic_policy_id, sender_ip_address, recipient, traffic_policy_verdict
| filter traffic_policy_verdict = "REJECT"
| sort @timestamp desc
| limit 100
```

Review rejected recipients, sender ranges, add-on result categories, and known legitimate traffic before completing a rollout.

## Traffic policy limitations
<a name="eb-filters-limitations"></a>
+ A traffic policy evaluates connection and SMTP envelope information. It does not inspect the message body.
+ Traffic policy conditions do not provide native SPF, DKIM, or DMARC result fields. Use rule set conditions to process supported authentication results after the message is accepted.
+ Malware and content analysis that requires the message body belongs in the rule set. A traffic policy can use only the Email Add On results that are supported for traffic policy evaluation.
+ You can't configure rate limits, quarantine actions, or a custom SMTP response in a traffic policy. With a traffic policy, you can allow or deny a recipient and apply the optional maximum message size.
+ Email Add On conditions do not apply to IPv6 connections. Use native IPv6 conditions to filter IPv6 sender ranges.