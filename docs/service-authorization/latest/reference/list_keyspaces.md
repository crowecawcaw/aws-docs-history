

# Actions, resources, and condition keys for Amazon Keyspaces (for Apache Cassandra)
<a name="list_keyspaces"></a>

Amazon Keyspaces (for Apache Cassandra) (service prefix: `cassandra`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/keyspaces/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/keyspaces/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cassandra/cassandra.json) for this service.

**Topics**
+ [API operations defined by Amazon Keyspaces (for Apache Cassandra)](#list_keyspaces-operations)
+ [Actions defined by Amazon Keyspaces (for Apache Cassandra)](#list_keyspaces-actions-as-permissions)
+ [Resource types defined by Amazon Keyspaces (for Apache Cassandra)](#list_keyspaces-resources-for-iam-policies)
+ [Condition keys for Amazon Keyspaces (for Apache Cassandra)](#list_keyspaces-policy-keys)

## API operations defined by Amazon Keyspaces (for Apache Cassandra)
<a name="list_keyspaces-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_keyspaces-actions-as-permissions).




- **   CreateKeyspace  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Create](#list_keyspaces-action-Create)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:CreateMultiRegionResource](#list_keyspaces-action-CreateMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:TagResource](#list_keyspaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTable  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Create](#list_keyspaces-action-Create)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:CreateMultiRegionResource](#list_keyspaces-action-CreateMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:TagResource](#list_keyspaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateType  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Create](#list_keyspaces-action-Create)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:CreateMultiRegionResource](#list_keyspaces-action-CreateMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteKeyspace  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Drop](#list_keyspaces-action-Drop)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:DropMultiRegionResource](#list_keyspaces-action-DropMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteTable  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Drop](#list_keyspaces-action-Drop)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:DropMultiRegionResource](#list_keyspaces-action-DropMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteType  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Drop](#list_keyspaces-action-Drop)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:DropMultiRegionResource](#list_keyspaces-action-DropMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetKeyspace  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTable  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTableAutoScalingSettings  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cassandra:SelectMultiRegionResource](#list_keyspaces-action-SelectMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-autoscaling:DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-autoscaling:DescribeScalingPolicies](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingPolicies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetType  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListKeyspaces  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTables  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTypes  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RestoreTable  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Restore](#list_keyspaces-action-Restore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:RestoreMultiRegionTable](#list_keyspaces-action-RestoreMultiRegionTable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   TagResource  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Alter](#list_keyspaces-action-Alter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:AlterMultiRegionResource](#list_keyspaces-action-AlterMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:TagMultiRegionResource](#list_keyspaces-action-TagMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cassandra:TagResource](#list_keyspaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Alter](#list_keyspaces-action-Alter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:AlterMultiRegionResource](#list_keyspaces-action-AlterMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:UnTagMultiRegionResource](#list_keyspaces-action-UnTagMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cassandra:UntagResource](#list_keyspaces-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   UpdateKeyspace  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Alter](#list_keyspaces-action-Alter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:AlterMultiRegionResource](#list_keyspaces-action-AlterMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:Create](#list_keyspaces-action-Create)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:CreateMultiRegionResource](#list_keyspaces-action-CreateMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:Modify](#list_keyspaces-action-Modify)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:ModifyMultiRegionResource](#list_keyspaces-action-ModifyMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:Select](#list_keyspaces-action-Select)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cassandra:SelectMultiRegionResource](#list_keyspaces-action-SelectMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [cassandra:TagMultiRegionResource](#list_keyspaces-action-TagMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [cassandra:TagResource](#list_keyspaces-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [application-autoscaling:DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-autoscaling:DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-autoscaling:DescribeScalingPolicies](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingPolicies.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [application-autoscaling:PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [application-autoscaling:RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateTable  **
  - **SDK client:** keyspaces
  - **IAM action:**  [cassandra:Alter](#list_keyspaces-action-Alter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cassandra:AlterMultiRegionResource](#list_keyspaces-action-AlterMultiRegionResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetRecords  **
  - **SDK client:** keyspacesstreams
  - **IAM action:**  [cassandra:GetRecords](#list_keyspaces-action-GetRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetShardIterator  **
  - **SDK client:** keyspacesstreams
  - **IAM action:**  [cassandra:GetShardIterator](#list_keyspaces-action-GetShardIterator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetStream  **
  - **SDK client:** keyspacesstreams
  - **IAM action:**  [cassandra:GetStream](#list_keyspaces-action-GetStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStreams  **
  - **SDK client:** keyspacesstreams
  - **IAM action:**  [cassandra:ListStreams](#list_keyspaces-action-ListStreams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by Amazon Keyspaces (for Apache Cassandra)
<a name="list_keyspaces-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [Alter](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to alter a keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Write

- **   [AlterMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to alter a multiregion keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Write

- **   [Create](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to create a keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to create a multiregion keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Write

- **   [Drop](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to drop a keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DropMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to drop a multiregion keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetRecords](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to retrieve the CDC stream records from a given shard
  - **Resource types (\*required):** [stream\*](#list_keyspaces-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetShardIterator](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to return a shard iterator
  - **Resource types (\*required):** [stream\*](#list_keyspaces-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetStream](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to return information about a CDC stream, including the composition of its shards
  - **Resource types (\*required):** [stream\*](#list_keyspaces-resource-stream)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListStreams](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to return an array of CDC stream ARNs associated with the current account and endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [Modify](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to INSERT, UPDATE or DELETE data in a table
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ModifyMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to INSERT, UPDATE or DELETE data in a multiregion table
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Restore](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to restore table from a backup
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreMultiRegionTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to restore multiregion table from a backup
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Select](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to SELECT data from a table
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SelectMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to SELECT data from a multiregion table
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to tag a multiregion keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TagResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to tag a keyspace, table, or stream
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_keyspaces-resource-stream) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_keyspaces-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnTagMultiRegionResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to untag a multiregion keyspace or table
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to untag a keyspace, table or stream
  - **Resource types (\*required):** [keyspace](#list_keyspaces-resource-keyspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [stream](#list_keyspaces-resource-stream) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Resource types (\*required):** [table](#list_keyspaces-resource-table) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_keyspaces-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePartitioner](https://docs.aws.amazon.com/keyspaces/latest/devguide/)  **
  - **Description:** Grants permission to UPDATE the partitioner in a system table
  - **Resource types (\*required):** [table\*](#list_keyspaces-resource-table)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Keyspaces (for Apache Cassandra)
<a name="list_keyspaces-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html)  | arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/${KeyspaceName}/ | [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_) | 
|  [stream](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html)  | arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/${KeyspaceName}/table/${TableName}/stream/${StreamLabel} | [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_) | 
|  [table](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is.html)  | arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/${KeyspaceName}/table/${TableName} | [aws:ResourceTag/${TagKey}](#list_keyspaces-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Keyspaces (for Apache Cassandra)
<a name="list_keyspaces-policy-keys"></a>

Amazon Keyspaces (for Apache Cassandra) defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/keyspaces/latest/devguide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/keyspaces/latest/devguide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/keyspaces/latest/devguide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 