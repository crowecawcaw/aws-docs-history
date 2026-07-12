# Actions, resources, and condition keys for AWS Shield network security director

AWS Shield network security director (service prefix: `network-security-director`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../waf/latest/developerguide/nsd-what-it-is.md "../../../waf/latest/developerguide/nsd-what-it-is.md").
- View a list of the [API operations available for
  this service](../../../network-security-director/latest/APIReference/welcome.md "../../../network-security-director/latest/APIReference/welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../waf/latest/developerguide/nsd-security.md "../../../waf/latest/developerguide/nsd-security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/network-security-director/network-security-director.json "https://servicereference.us-east-1.amazonaws.com/v1/network-security-director/network-security-director.json") for this service.

###### Topics

- [Actions defined by AWS Shield network security director](#list_network-security-director-actions-as-permissions "#list_network-security-director-actions-as-permissions")
- [Resource types defined by AWS Shield network security director](#list_network-security-director-resources-for-iam-policies "#list_network-security-director-resources-for-iam-policies")
- [Condition keys for AWS Shield network security director](#list_network-security-director-policy-keys "#list_network-security-director-policy-keys")

## Actions defined by AWS Shield network security director

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                         | Description                                                               | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetFinding](../../../network-security-director/latest/APIReference/API_GetFinding.md "../../../network-security-director/latest/APIReference/API_GetFinding.md")                               | Grants permission to get a finding                                        |                             |                | Read         |
| [GetResource](../../../network-security-director/latest/APIReference/API_GetResource.md "../../../network-security-director/latest/APIReference/API_GetResource.md")                            | Grants permission to get a resource                                       |                             |                | Read         |
| [ListAccountSummaries](../../../network-security-director/latest/APIReference/API_ListAccountSummaries.md "../../../network-security-director/latest/APIReference/API_ListAccountSummaries.md") | Grants permission to list account summaries for an account                |                             |                | List         |
| [ListFindings](../../../network-security-director/latest/APIReference/API_ListFindings.md "../../../network-security-director/latest/APIReference/API_ListFindings.md")                         | Grants permission to list findings                                        |                             |                | List         |
| [ListInsights](../../../network-security-director/latest/APIReference/API_ListInsights.md "../../../network-security-director/latest/APIReference/API_ListInsights.md")                         | Grants permission to list insights about the latest network security scan |                             |                | List         |
| [ListRemediations](../../../network-security-director/latest/APIReference/API_ListRemediations.md "../../../network-security-director/latest/APIReference/API_ListRemediations.md")             | Grants permission to list remediations for a finding                      |                             |                | List         |
| [ListResources](../../../network-security-director/latest/APIReference/API_ListResources.md "../../../network-security-director/latest/APIReference/API_ListResources.md")                      | Grants permission to list resources                                       |                             |                | List         |
| [UpdateFinding](../../../network-security-director/latest/APIReference/API_UpdateFinding.md "../../../network-security-director/latest/APIReference/API_UpdateFinding.md")                      | Grants permission to update the status of a finding                       |                             |                | Write        |

## Resource types defined by AWS Shield network security director

AWS Shield network security director does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Shield network security director

AWS Shield network security director has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
