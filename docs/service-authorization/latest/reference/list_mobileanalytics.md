# Actions, resources, and condition keys for Amazon Mobile Analytics

Amazon Mobile Analytics (service prefix: `mobileanalytics`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../mobileanalytics/latest/ug.md "../../../mobileanalytics/latest/ug.md").
- View a list of the [API operations available for this
  service](../../../mobileanalytics/latest/ug.md "../../../mobileanalytics/latest/ug.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../mobileanalytics/latest/ug/access_permissions.md "../../../mobileanalytics/latest/ug/access_permissions.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/mobileanalytics/mobileanalytics.json "https://servicereference.us-east-1.amazonaws.com/v1/mobileanalytics/mobileanalytics.json") for this service.

###### Topics

- [Actions defined by Amazon Mobile Analytics](#list_mobileanalytics-actions-as-permissions "#list_mobileanalytics-actions-as-permissions")
- [Resource types defined by Amazon Mobile Analytics](#list_mobileanalytics-resources-for-iam-policies "#list_mobileanalytics-resources-for-iam-policies")
- [Condition keys for Amazon Mobile Analytics](#list_mobileanalytics-policy-keys "#list_mobileanalytics-policy-keys")

## Actions defined by Amazon Mobile Analytics

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                        | Description                                        | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------- | -------------- | ------------ |
| GetFinancialReports                                                                                            | Grant access to financial metrics for an app       |                             |                | Read         |
| GetReports                                                                                                     | Grant access to standard metrics for an app        |                             |                | Read         |
| [PutEvents](../../../mobileanalytics/latest/ug/PutEvents.md "../../../mobileanalytics/latest/ug/PutEvents.md") | The PutEvents operation records one or more events |                             |                | Write        |

## Resource types defined by Amazon Mobile Analytics

Amazon Mobile Analytics does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon Mobile Analytics

Amazon Mobile Analytics has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
