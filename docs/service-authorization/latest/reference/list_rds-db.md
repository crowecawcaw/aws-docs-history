# Actions, resources, and condition keys for Amazon RDS IAM Authentication

Amazon RDS IAM Authentication (service prefix: `rds-db`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AmazonRDS/latest/UserGuide.md "../../../AmazonRDS/latest/UserGuide.md").
- View a list of the [API operations available for this
  service](../../../AmazonRDS/latest/APIReference.md "../../../AmazonRDS/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/rds-db/rds-db.json "https://servicereference.us-east-1.amazonaws.com/v1/rds-db/rds-db.json") for this service.

###### Topics

- [Actions defined by Amazon RDS IAM Authentication](#list_rds-db-actions-as-permissions "#list_rds-db-actions-as-permissions")
- [Resource types defined by Amazon RDS IAM Authentication](#list_rds-db-resources-for-iam-policies "#list_rds-db-resources-for-iam-policies")
- [Condition keys for Amazon RDS IAM Authentication](#list_rds-db-policy-keys "#list_rds-db-policy-keys")

## Actions defined by Amazon RDS IAM Authentication

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                      | Description                                        | Resource types (\*required)                                                | Condition keys | Access level                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------------- | -------------- | ----------------------------- |
| [connect](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.md") | Allows IAM role or user to connect to RDS database | [db-user\*](#list_rds-db-resource-db-user "#list_rds-db-resource-db-user") |                | Permissions management, Write |

## Resource types defined by Amazon RDS IAM Authentication

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                 | ARN                                                                                | Condition keys |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------- |
| [db-user](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.md") | arn:${Partition}:rds-db:${Region}:${Account}:dbuser:${DbiResourceId}/${DbUserName} |                |

## Condition keys for Amazon RDS IAM Authentication

Amazon RDS IAM Authentication has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
