

# Actions, resources, and condition keys for AWS Shield network security director
<a name="list_network-security-director"></a>

AWS Shield network security director (service prefix: `network-security-director`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-what-it-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/network-security-director/latest/APIReference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/network-security-director/network-security-director.json) for this service.

**Topics**
+ [Actions defined by AWS Shield network security director](#list_network-security-director-actions-as-permissions)
+ [Resource types defined by AWS Shield network security director](#list_network-security-director-resources-for-iam-policies)
+ [Condition keys for AWS Shield network security director](#list_network-security-director-policy-keys)

## Actions defined by AWS Shield network security director
<a name="list_network-security-director-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetFinding](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_GetFinding.html)  | Grants permission to get a finding |  |   | Read | 
|   [GetResource](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_GetResource.html)  | Grants permission to get a resource |  |   | Read | 
|   [ListAccountSummaries](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_ListAccountSummaries.html)  | Grants permission to list account summaries for an account |  |   | List | 
|   [ListFindings](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_ListFindings.html)  | Grants permission to list findings |  |   | List | 
|   [ListInsights](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_ListInsights.html)  | Grants permission to list insights about the latest network security scan |  |   | List | 
|   [ListRemediations](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_ListRemediations.html)  | Grants permission to list remediations for a finding |  |   | List | 
|   [ListResources](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_ListResources.html)  | Grants permission to list resources |  |   | List | 
|   [UpdateFinding](https://docs.aws.amazon.com/network-security-director/latest/APIReference/API_UpdateFinding.html)  | Grants permission to update the status of a finding |  |   | Write | 

## Resource types defined by AWS Shield network security director
<a name="list_network-security-director-resources-for-iam-policies"></a>

AWS Shield network security director does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Shield network security director
<a name="list_network-security-director-policy-keys"></a>

AWS Shield network security director has no service-specific condition keys that can be used in the `Condition` element of policy statements.