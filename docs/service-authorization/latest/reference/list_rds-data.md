

# Actions, resources, and condition keys for Amazon RDS Data API
<a name="list_rds-data"></a>

Amazon RDS Data API (service prefix: `rds-data`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rds-data/rds-data.json) for this service.

**Topics**
+ [API operations defined by Amazon RDS Data API](#list_rds-data-operations)
+ [Actions defined by Amazon RDS Data API](#list_rds-data-actions-as-permissions)
+ [Resource types defined by Amazon RDS Data API](#list_rds-data-resources-for-iam-policies)
+ [Condition keys for Amazon RDS Data API](#list_rds-data-policy-keys)

## API operations defined by Amazon RDS Data API
<a name="list_rds-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rds-data-actions-as-permissions).




- **   BatchExecuteStatement  **
  - **IAM action:**  [rds-data:BatchExecuteStatement](#list_rds-data-action-BatchExecuteStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BeginTransaction  **
  - **IAM action:**  [rds-data:BeginTransaction](#list_rds-data-action-BeginTransaction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CommitTransaction  **
  - **IAM action:**  [rds-data:CommitTransaction](#list_rds-data-action-CommitTransaction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteSql  **
  - **IAM action:**  [rds-data:ExecuteSql](#list_rds-data-action-ExecuteSql) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExecuteStatement  **
  - **IAM action:**  [rds-data:ExecuteStatement](#list_rds-data-action-ExecuteStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RollbackTransaction  **
  - **IAM action:**  [rds-data:RollbackTransaction](#list_rds-data-action-RollbackTransaction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon RDS Data API
<a name="list_rds-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BatchExecuteStatement.html)  **
  - **Description:** Grants permission to run a batch SQL statement over an array of data
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write

- **   [BeginTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BeginTransaction.html)  **
  - **Description:** Grants permission to start a SQL transaction
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write

- **   [CommitTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_CommitTransaction.html)  **
  - **Description:** Grants permission to end a SQL transaction started with the BeginTransaction operation and commits the changes
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write

- **   [ExecuteSql](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteSql.html)  **
  - **Description:** Grants permission to run one or more SQL statements. This operation is deprecated. Use the BatchExecuteStatement or ExecuteStatement operation
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write

- **   [ExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to run a SQL statement against a database
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write

- **   [RollbackTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_RollbackTransaction.html)  **
  - **Description:** Grants permission to perform a rollback of a transaction. Rolling back a transaction cancels its changes
  - **Resource types (\*required):** [cluster\*](#list_rds-data-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by Amazon RDS Data API
<a name="list_rds-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Managing.html)  | arn:${Partition}:rds:${Region}:${Account}:cluster:${DbClusterInstanceName} | [aws:ResourceTag/${TagKey}](#list_rds-data-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rds-data-aws_TagKeys) | 

## Condition keys for Amazon RDS Data API
<a name="list_rds-data-policy-keys"></a>

Amazon RDS Data API defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys associated with the resource | ArrayOfString | 