

# Actions, resources, and condition keys for AWS Edge Analytics Platform

AWS Edge Analytics Platform (service prefix: `apex`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/waf/latest/developerguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/apex/apex.json) for this service.

**Topics**
+ [Actions defined by AWS Edge Analytics Platform](#list_apex-actions-as-permissions)
+ [Permission-only actions for AWS Edge Analytics Platform](#list_apex-permission-only-actions)
+ [Resource types defined by AWS Edge Analytics Platform](#list_apex-resources-for-iam-policies)
+ [Condition keys for AWS Edge Analytics Platform](#list_apex-policy-keys)

## Actions defined by AWS Edge Analytics Platform
<a name="list_apex-actions-as-permissions"></a>

AWS Edge Analytics Platform has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Edge Analytics Platform
<a name="list_apex-permission-only-actions"></a>

The following actions are defined by AWS Edge Analytics Platform but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetStatistics](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to retrieve aggregate statistics over AWS WAFv2 request logs within a specified time window |  |   | Read | 
|   [GetStatisticsTimeSeries](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to retrieve time-bucketed statistics over AWS WAFv2 request logs within a specified time window |  |   | Read | 
|   [Search](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-console)  | Grants permission to search individual AWS WAFv2 request log records within a specified time window |  |   | Read | 

## Resource types defined by AWS Edge Analytics Platform
<a name="list_apex-resources-for-iam-policies"></a>

AWS Edge Analytics Platform does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Edge Analytics Platform
<a name="list_apex-policy-keys"></a>

AWS Edge Analytics Platform has no service-specific condition keys that can be used in the `Condition` element of policy statements.