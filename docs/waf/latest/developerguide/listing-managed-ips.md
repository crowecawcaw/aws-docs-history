**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Listing IP addresses that are being rate limited by rate-based rules

This section explains how to access the list of IP addresses that are currently rate-limited by a
rate-based rule by using the CLI, the API, or any of the SDKs.

If your rate-based rule only aggregates on IP address or forwarded IP address, you
can retrieve the list of IP addresses that the rule is currently rate limiting. AWS WAF stores these IP addresses
in the rule's managed keys list.

###### Note

This option is only available if you aggregate on only the IP address or only an IP address in a header. If you use the custom keys request aggregation, you can't retrieve a list of rate limited IP addresses, even if you use one of the IP address specifications in your custom keys.

A rate-based rule applies its rule action to requests from the rule's managed keys list
that match the rule's scope-down statement. When a rule has no scope-down statement, it applies the action to
all requests from the IP addresses that are in the list. The rule action is Block by default, but it can be any valid rule action except for Allow. The maximum number of IP addresses that AWS WAF can rate limit using a single rate-based rule
instance is 10,000. If more than 10,000 addresses exceed the rate limit, AWS WAF limits those
with the highest rates.

You can access a rate-based rule's managed keys list using the CLI, the API, or any of the SDKs.
This topic covers access using the CLI and APIs. The console doesn't provide access to the list at this time.

For the AWS WAF API, the command is [GetRateBasedStatementManagedKeys](../APIReference/API_GetRateBasedStatementManagedKeys.md "../APIReference/API_GetRateBasedStatementManagedKeys.md").

For the AWS WAF CLI, the command is [get-rate-based-statement-managed-keys](../../../cli/latest/reference/wafv2/get-rate-based-statement-managed-keys.md "../../../cli/latest/reference/wafv2/get-rate-based-statement-managed-keys.md").

The following shows the syntax for retrieving the list of rate limited IP addresses for a
rate-based rule that's being used in a protection pack (web ACL) on an Amazon CloudFront distribution.

```
aws wafv2 get-rate-based-statement-managed-keys --scope=CLOUDFRONT --region=us-east-1 --web-acl-name=`WebACLName` --web-acl-id=`WebACLId` --rule-name=`RuleName`
```

The following shows the syntax for a regional application, an Amazon API Gateway REST API, an Application Load Balancer, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, AWS Amplify, or an AWS Verified Access instance.

```
aws wafv2 get-rate-based-statement-managed-keys --scope=REGIONAL --region=`region` --web-acl-name=`WebACLName` --web-acl-id=`WebACLId` --rule-name=`RuleName`
```

AWS WAF monitors web requests and manages keys independently for each unique combination of
protection pack (web ACL), optional rule group, and rate-based rule. For example, if you define a rate-based
rule inside a rule group, and then use the rule group in a protection pack (web ACL), AWS WAF monitors web
requests and manages keys for that protection pack (web ACL), rule group reference statement, and rate-based
rule instance. If you use the same rule group in a second protection pack (web ACL), AWS WAF monitors web
requests and manages keys for this second usage completely independent of your first.

For a rate-based rule that you've defined inside a rule group, you need to provide the name
of the rule group reference statement in your request, in addition to the protection pack (web ACL) name and
the name of the rate-based rule inside the rule group. The following shows the syntax
for a regional application where the rate-based rule is defined inside a rule group, and the
rule group is used in a protection pack (web ACL).

```
aws wafv2 get-rate-based-statement-managed-keys --scope=REGIONAL --region=`region` --web-acl-name=`WebACLName` --web-acl-id=`WebACLId` --rule-group-rule-name=`RuleGroupRuleName` --rule-name=`RuleName`
```
