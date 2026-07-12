# Actions, resources, and condition keys for AWS Action Recommendations

AWS Action Recommendations (service prefix: `action-recommendations`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md "../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md").
- View a list of the [API operations available for
  this service](../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md "../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.md "../../../awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/action-recommendations/action-recommendations.json "https://servicereference.us-east-1.amazonaws.com/v1/action-recommendations/action-recommendations.json") for this service.

###### Topics

- [Actions defined by AWS Action Recommendations](#list_action-recommendations-actions-as-permissions "#list_action-recommendations-actions-as-permissions")
- [Resource types defined by AWS Action Recommendations](#list_action-recommendations-resources-for-iam-policies "#list_action-recommendations-resources-for-iam-policies")
- [Condition keys for AWS Action Recommendations](#list_action-recommendations-policy-keys "#list_action-recommendations-policy-keys")

## Actions defined by AWS Action Recommendations

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                 | Description                                                                 | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ListRecommendedActions](../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md "../../../awsconsolehelpdocs/latest/gsg/recommended-actions.md") | Grants permission to list recommended actions in the AWS Management Console |                             |                | List         |

## Resource types defined by AWS Action Recommendations

AWS Action Recommendations does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Action Recommendations

AWS Action Recommendations has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
