# Actions, resources, and condition keys for Amazon RDS Data API

Amazon RDS Data API (service prefix: `rds-data`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md").
- View a list of the [API operations available for
  this service](../../../rdsdataservice/latest/APIReference/Welcome.md "../../../rdsdataservice/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/rds-data/rds-data.json "https://servicereference.us-east-1.amazonaws.com/v1/rds-data/rds-data.json") for this service.

###### Topics

- [API operations defined by Amazon RDS Data API](#list_rds-data-operations "#list_rds-data-operations")
- [Actions defined by Amazon RDS Data API](#list_rds-data-actions-as-permissions "#list_rds-data-actions-as-permissions")
- [Resource types defined by Amazon RDS Data API](#list_rds-data-resources-for-iam-policies "#list_rds-data-resources-for-iam-policies")
- [Condition keys for Amazon RDS Data API](#list_rds-data-policy-keys "#list_rds-data-policy-keys")

## API operations defined by Amazon RDS Data API

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rds-data-actions-as-permissions "#list_rds-data-actions-as-permissions").

| Operation             | IAM action                                                                                                                  | Condition key | Possible value(s) | Access level |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| BatchExecuteStatement | [rds-data:BatchExecuteStatement](#list_rds-data-action-BatchExecuteStatement "#list_rds-data-action-BatchExecuteStatement") |               |                   | Write        |
| BeginTransaction      | [rds-data:BeginTransaction](#list_rds-data-action-BeginTransaction "#list_rds-data-action-BeginTransaction")                |               |                   | Write        |
| CommitTransaction     | [rds-data:CommitTransaction](#list_rds-data-action-CommitTransaction "#list_rds-data-action-CommitTransaction")             |               |                   | Write        |
| ExecuteSql            | [rds-data:ExecuteSql](#list_rds-data-action-ExecuteSql "#list_rds-data-action-ExecuteSql")                                  |               |                   | Write        |
| ExecuteStatement      | [rds-data:ExecuteStatement](#list_rds-data-action-ExecuteStatement "#list_rds-data-action-ExecuteStatement")                |               |                   | Write        |
| RollbackTransaction   | [rds-data:RollbackTransaction](#list_rds-data-action-RollbackTransaction "#list_rds-data-action-RollbackTransaction")       |               |                   | Write        |

## Actions defined by Amazon RDS Data API

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                      | Description                                                                                                                                    | Resource types (\*required)                                                    | Condition keys                                                                                                                                                                             | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| [BatchExecuteStatement](../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md") | Grants permission to run a batch SQL statement over an array of data                                                                           | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |
| [BeginTransaction](../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md "../../../rdsdataservice/latest/APIReference/API_BeginTransaction.md")                | Grants permission to start a SQL transaction                                                                                                   | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |
| [CommitTransaction](../../../rdsdataservice/latest/APIReference/API_CommitTransaction.md "../../../rdsdataservice/latest/APIReference/API_CommitTransaction.md")             | Grants permission to end a SQL transaction started with the BeginTransaction operation and commits the changes                                 | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |
| [ExecuteSql](../../../rdsdataservice/latest/APIReference/API_ExecuteSql.md "../../../rdsdataservice/latest/APIReference/API_ExecuteSql.md")                                  | Grants permission to run one or more SQL statements. This operation is deprecated. Use the BatchExecuteStatement or ExecuteStatement operation | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |
| [ExecuteStatement](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md")                | Grants permission to run a SQL statement against a database                                                                                    | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |
| [RollbackTransaction](../../../rdsdataservice/latest/APIReference/API_RollbackTransaction.md "../../../rdsdataservice/latest/APIReference/API_RollbackTransaction.md")       | Grants permission to perform a rollback of a transaction. Rolling back a transaction cancels its changes                                       | [cluster\*](#list_rds-data-resource-cluster "#list_rds-data-resource-cluster") | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") | Write        |

## Resource types defined by Amazon RDS Data API

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                             | ARN                                                                        | Condition keys                                                                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cluster](../../../AmazonRDS/latest/UserGuide/Aurora.Managing.md "../../../AmazonRDS/latest/UserGuide/Aurora.Managing.md") | arn:${Partition}:rds:${Region}:${Account}:cluster:${DbClusterInstanceName} | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_ "#list_rds-data-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_rds-data-aws_TagKeys "#list_rds-data-aws_TagKeys") |

## Condition keys for Amazon RDS Data API

Amazon RDS Data API defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                             | Description                                                 | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------- |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters access by the tags associated with the resource     | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters access by the tag keys associated with the resource | ArrayOfString |
