# Actions, resources, and condition keys for Amazon RHEL Knowledgebase Portal

Amazon RHEL Knowledgebase Portal (service prefix: `rhelkb`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../systems-manager/latest/userguide/fleet-rhel.md "../../../systems-manager/latest/userguide/fleet-rhel.md").
- View a list of the [API operations available for
  this service](../../../systems-manager/latest/userguide/fleet-rhel.md "../../../systems-manager/latest/userguide/fleet-rhel.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../systems-manager/latest/userguide/security-iam.md "../../../systems-manager/latest/userguide/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/rhelkb/rhelkb.json "https://servicereference.us-east-1.amazonaws.com/v1/rhelkb/rhelkb.json") for this service.

###### Topics

- [Actions defined by Amazon RHEL Knowledgebase Portal](#list_rhelkb-actions-as-permissions "#list_rhelkb-actions-as-permissions")
- [Resource types defined by Amazon RHEL Knowledgebase Portal](#list_rhelkb-resources-for-iam-policies "#list_rhelkb-resources-for-iam-policies")
- [Condition keys for Amazon RHEL Knowledgebase Portal](#list_rhelkb-policy-keys "#list_rhelkb-policy-keys")

## Actions defined by Amazon RHEL Knowledgebase Portal

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                         | Description                                                  | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------- | -------------- | ------------ |
| [GetRhelURL](../../../systems-manager/latest/userguide/fleet-rhel.md "../../../systems-manager/latest/userguide/fleet-rhel.md") | Grants permission to access the Red Hat Knowledgebase portal |                             |                | Read         |

## Resource types defined by Amazon RHEL Knowledgebase Portal

Amazon RHEL Knowledgebase Portal does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon RHEL Knowledgebase Portal

Amazon RHEL Knowledgebase Portal has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
