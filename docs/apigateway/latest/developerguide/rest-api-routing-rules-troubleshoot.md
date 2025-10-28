# Troubleshooting issues with routing rules

The following troubleshooting guidance might help resolve issues with your routing rules.

## I can't tell how API Gateway sent traffic to my APIs

You can use access logs for your REST API stage to log and troubleshoot your routing rules. You can view the
routing rule ID that API Gateway used to send traffic to your API using the
`$context.customDomain.routingRuleIdMatched` variable. To view the API mapping that API Gateway used to
send traffic to your API, use the `$context.customDomain.basePathMatched` variable.

To log your routing rules, you need to configure [an appropriate CloudWatch Logs
role](set-up-logging.md#set-up-access-logging-permissions "set-up-logging.md#set-up-access-logging-permissions") ARN
for your account and create a log group.

The following example access log group can retrieve the relevant information for troubleshooting routing rules
and API mappings. API Gateway only populates the context variable for the routing mechanism it used, otherwise the context
variable is `-`.

CLF

```
$context.path $context.customDomain.routingRuleIdMatched $context.customDomain.basePathMatched $context.requestId $context.extendedRequestId
```

JSON

```
{"requestPath": "$context.path", "routingRuleId" : "$context.customDomain.routingRuleIdMatched", "API mapping" : "$context.customDomain.basePathMatched", "requestId":"$context.requestId", "extendedRequestId":"$context.extendedRequestId"}
```

XML

```
<request id="$context.requestId"> <requestPath>$context.path</requestPath> <ruleId>$context.customDomain.routingRuleIdMatched</ruleId> <ApiMapping>$context.customDomain.basePathMatched</ApiMapping> <extendedRequestId>$context.extendedRequestId</extendedRequestId> </request>
```

CSV

```
$context.path,$context.customDomain.routingRuleIdMatched,$context.customDomain.basePathMatched,$context.requestId,$context.extendedRequestId
```

We also recommend that you confirm the routing mode for your custom domain name. For more information, see
[Set the routing mode for your custom domain name](set-routing-mode.md "set-routing-mode.md").

## I can't enable routing rules on my custom domain name

You might receive the following error from API Gateway:

```
Your account doesn’t have permission to use RoutingRules.
This might be caused by an IAM policy in your account with a deny statement on BasePathMapping or ApiMapping.
To grant permission for this account to use RoutingRules, use the UpdateAccount API.
This will impact any existing IAM policies that deny access to BasePathMapping or ApiMapping.
See API Gateway documentation for further details.
```

You'll receive this error if have or had an IAM policy that denies access to [BasePathMapping](../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md#amazonapigatewaymanagement-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonapigatewaymanagement.md#amazonapigatewaymanagement-resources-for-iam-policies") or [ApiMapping](../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md#amazonapigatewaymanagementv2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonapigatewaymanagementv2.md#amazonapigatewaymanagementv2-resources-for-iam-policies"). When you enable routing rules for a custom domain name, although your policy will
continue to deny access to `BasePathMapping` or `ApiMapping`, the same policy can be used
to access `RoutingRule`. This might allow a user to change the routing behavior of your custom domain
name.

For example, if you had a policy like the following:

```
{
    "Sid": "DenyCreatingApiMappings",
    "Effect": "Deny",
    "Action": "apigateway:POST",
    "Resource": [
        "arn:aws:apigateway:us-west-2::/domainnames/example.com/apimappings"
    ]
}
```

When you enable routing rules for `example.com`, this policy will continue to deny access to
creating an `ApiMapping` but will not deny access to creating a `RoutingRule`.

We recommend that you audit the IAM policies in your account. The following example policy will deny
access to creating `ApiMapping`, `BasePathMapping`, and `RoutingRule`:

```
{
    "Sid": "DenyCreatingBasePathMappingsApiMappings",
    "Effect": "Deny",
    "Action": "apigateway:POST",
    "Resource": [
        "arn:aws:apigateway:us-west-2::/domainnames/example.com/basepathmappings",
        "arn:aws:apigateway:us-west-2::/domainnames/example.com/apimappings"
    ]
},
{
    "Sid": "DenyCreatingRoutingRules",
    "Effect": "Deny",
    "Action": "apigateway:CreateRoutingRule",
    "Resource": [
        "arn:aws:apigateway:us-west-2:111122223333:/domainnames/example.com/routingrules/*"
    ]
}
```

After you have confirmed all your policies have been updated, you can update your API's account-level
settings to enable routing rules for a Region.

Use the following [update-account](../../../cli/latest/reference/apigateway/update-account.md "../../../cli/latest/reference/apigateway/update-account.md") command to update the settings for your API's account-level settings for a Region:

```
aws apigateway update-account --patch-operations 'op=remove,path=/features,value=BlockedForRoutingRules' --region `us-west-2`
```

After you update your API's account-level settings, you can change the routing mode of your custom domain
name. You can also continue to use IAM policies to deny access to `RoutingRules`,
`ApiMapping` or `BasePathMapping`.
