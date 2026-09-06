

# Actions, resources, and condition keys for Amazon Redshift Data API
<a name="list_redshift-data"></a>

Amazon Redshift Data API (service prefix: `redshift-data`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/redshift-data/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-authentication-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/redshift-data/redshift-data.json) for this service.

**Topics**
+ [API operations defined by Amazon Redshift Data API](#list_redshift-data-operations)
+ [Actions defined by Amazon Redshift Data API](#list_redshift-data-actions-as-permissions)
+ [Resource types defined by Amazon Redshift Data API](#list_redshift-data-resources-for-iam-policies)
+ [Condition keys for Amazon Redshift Data API](#list_redshift-data-policy-keys)

## API operations defined by Amazon Redshift Data API
<a name="list_redshift-data-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_redshift-data-actions-as-permissions).




- **   BatchExecuteStatement  **
  - **IAM action:**  [redshift-data:BatchExecuteStatement](#list_redshift-data-action-BatchExecuteStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelStatement  **
  - **IAM action:**  [redshift-data:CancelStatement](#list_redshift-data-action-CancelStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeStatement  **
  - **IAM action:**  [redshift-data:DescribeStatement](#list_redshift-data-action-DescribeStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTable  **
  - **IAM action:**  [redshift-data:DescribeTable](#list_redshift-data-action-DescribeTable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExecuteStatement  **
  - **IAM action:**  [redshift-data:ExecuteStatement](#list_redshift-data-action-ExecuteStatement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetStatementResult  **
  - **IAM action:**  [redshift-data:GetStatementResult](#list_redshift-data-action-GetStatementResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStatementResultV2  **
  - **IAM action:**  [redshift-data:GetStatementResult](#list_redshift-data-action-GetStatementResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatabases  **
  - **IAM action:**  [redshift-data:ListDatabases](#list_redshift-data-action-ListDatabases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSchemas  **
  - **IAM action:**  [redshift-data:ListSchemas](#list_redshift-data-action-ListSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSessions  **
  - **IAM action:**  [redshift-data:ListSessions](#list_redshift-data-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStatements  **
  - **IAM action:**  [redshift-data:ListStatements](#list_redshift-data-action-ListStatements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTables  **
  - **IAM action:**  [redshift-data:ListTables](#list_redshift-data-action-ListTables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by Amazon Redshift Data API
<a name="list_redshift-data-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_BatchExecuteStatement.html)  **
  - **Description:** Grants permission to execute multiple queries under a single connection
  - **Resource types (\*required):** [cluster](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)<br />[redshift-data:glue-catalog-arn](#list_redshift-data-redshift-data_glue-catalog-arn)<br />[redshift-data:session-owner-iam-userid](#list_redshift-data-redshift-data_session-owner-iam-userid)
  - **Resource types (\*required):** [workgroup](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)<br />[redshift-data:glue-catalog-arn](#list_redshift-data-redshift-data_glue-catalog-arn)<br />[redshift-data:session-owner-iam-userid](#list_redshift-data-redshift-data_session-owner-iam-userid)
  - **Access level:** Write

- **   [CancelStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_CancelStatement.html)  **
  - **Description:** Grants permission to cancel a running query
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift-data:statement-owner-iam-userid](#list_redshift-data-redshift-data_statement-owner-iam-userid)
  - **Access level:** Write

- **   [DescribeStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeStatement.html)  **
  - **Description:** Grants permission to retrieve detailed information about a statement execution
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift-data:statement-owner-iam-userid](#list_redshift-data-redshift-data_statement-owner-iam-userid)
  - **Access level:** Read

- **   [DescribeTable](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeTable.html)  **
  - **Description:** Grants permission to retrieve metadata about a particular table
  - **Resource types (\*required):** [cluster\*](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ExecuteStatement.html)  **
  - **Description:** Grants permission to execute a query
  - **Resource types (\*required):** [cluster](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)<br />[redshift-data:glue-catalog-arn](#list_redshift-data-redshift-data_glue-catalog-arn)<br />[redshift-data:session-owner-iam-userid](#list_redshift-data-redshift-data_session-owner-iam-userid)
  - **Resource types (\*required):** [workgroup](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)<br />[redshift-data:glue-catalog-arn](#list_redshift-data-redshift-data_glue-catalog-arn)<br />[redshift-data:session-owner-iam-userid](#list_redshift-data-redshift-data_session-owner-iam-userid)
  - **Access level:** Write

- **   [GetStagingBucketLocation](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_GetStagingBucketLocation.html)  **
  - **Description:** Grants permission to get staging bucket location for a given managed workgroup
  - **Resource types (\*required):** [managed-workgroup\*](#list_redshift-data-resource-managed-workgroup)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetStatementResult](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_GetStatementResult.html)  **
  - **Description:** Grants permission to fetch the result of a query
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift-data:statement-owner-iam-userid](#list_redshift-data-redshift-data_statement-owner-iam-userid)
  - **Access level:** Read

- **   [ListDatabases](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListDatabases.html)  **
  - **Description:** Grants permission to list databases for a given cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSchemas](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListSchemas.html)  **
  - **Description:** Grants permission to list schemas for a given cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSessions](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list sessions for a given principal
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift-data:session-owner-iam-userid](#list_redshift-data-redshift-data_session-owner-iam-userid)
  - **Access level:** List

- **   [ListStatements](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListStatements.html)  **
  - **Description:** Grants permission to list queries for a given principal
  - **Resource types (\*required):** 
  - **Condition keys:** [redshift-data:statement-owner-iam-userid](#list_redshift-data-redshift-data_statement-owner-iam-userid)
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListTables.html)  **
  - **Description:** Grants permission to list tables for a given cluster
  - **Resource types (\*required):** [cluster\*](#list_redshift-data-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workgroup\*](#list_redshift-data-resource-workgroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_)
  - **Access level:** List



## Resource types defined by Amazon Redshift Data API
<a name="list_redshift-data-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)  | arn:${Partition}:redshift:${Region}:${Account}:cluster:${ClusterName} | [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_) | 
|  [managed-workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:managed-workgroup/${ManagedWorkgroupId} |   | 
|  [workgroup](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-serverless.html)  | arn:${Partition}:redshift-serverless:${Region}:${Account}:workgroup/${WorkgroupId} | [aws:ResourceTag/${TagKey}](#list_redshift-data-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Redshift Data API
<a name="list_redshift-data-policy-keys"></a>

Amazon Redshift Data API defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by tag-value associated with the resource | String | 
|   [redshift-data:glue-catalog-arn](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by glue catalog arn | ARN | 
|   [redshift-data:session-owner-iam-userid](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by session owner iam userid | String | 
|   [redshift-data:statement-owner-iam-userid](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-policy-resources.conditions)  | Filters access by statement owner iam userid | String | 