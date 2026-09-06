

# Actions, resources, and condition keys for Amazon Managed Streaming for Kafka Connect
<a name="list_kafkaconnect"></a>

Amazon Managed Streaming for Kafka Connect (service prefix: `kafkaconnect`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/MSKC/latest/mskc/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/kafkaconnect/kafkaconnect.json) for this service.

**Topics**
+ [API operations defined by Amazon Managed Streaming for Kafka Connect](#list_kafkaconnect-operations)
+ [Actions defined by Amazon Managed Streaming for Kafka Connect](#list_kafkaconnect-actions-as-permissions)
+ [Resource types defined by Amazon Managed Streaming for Kafka Connect](#list_kafkaconnect-resources-for-iam-policies)
+ [Condition keys for Amazon Managed Streaming for Kafka Connect](#list_kafkaconnect-policy-keys)

## API operations defined by Amazon Managed Streaming for Kafka Connect
<a name="list_kafkaconnect-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_kafkaconnect-actions-as-permissions).




- **   CreateConnector  **
  - **IAM action:**  [kafkaconnect:CreateConnector](#list_kafkaconnect-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafkaconnect:TagResource](#list_kafkaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** kafkaconnect.amazonaws.com / **Access level:** Write

- **   CreateCustomPlugin  **
  - **IAM action:**  [kafkaconnect:CreateCustomPlugin](#list_kafkaconnect-action-CreateCustomPlugin)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafkaconnect:TagResource](#list_kafkaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWorkerConfiguration  **
  - **IAM action:**  [kafkaconnect:CreateWorkerConfiguration](#list_kafkaconnect-action-CreateWorkerConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [kafkaconnect:TagResource](#list_kafkaconnect-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteConnector  **
  - **IAM action:**  [kafkaconnect:DeleteConnector](#list_kafkaconnect-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomPlugin  **
  - **IAM action:**  [kafkaconnect:DeleteCustomPlugin](#list_kafkaconnect-action-DeleteCustomPlugin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkerConfiguration  **
  - **IAM action:**  [kafkaconnect:DeleteWorkerConfiguration](#list_kafkaconnect-action-DeleteWorkerConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeConnector  **
  - **IAM action:**  [kafkaconnect:DescribeConnector](#list_kafkaconnect-action-DescribeConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConnectorOperation  **
  - **IAM action:**  [kafkaconnect:DescribeConnector](#list_kafkaconnect-action-DescribeConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [kafkaconnect:DescribeConnectorOperation](#list_kafkaconnect-action-DescribeConnectorOperation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeCustomPlugin  **
  - **IAM action:**  [kafkaconnect:DescribeCustomPlugin](#list_kafkaconnect-action-DescribeCustomPlugin) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkerConfiguration  **
  - **IAM action:**  [kafkaconnect:DescribeWorkerConfiguration](#list_kafkaconnect-action-DescribeWorkerConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectorOperations  **
  - **IAM action:**  [kafkaconnect:ListConnectorOperations](#list_kafkaconnect-action-ListConnectorOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectors  **
  - **IAM action:**  [kafkaconnect:ListConnectors](#list_kafkaconnect-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCustomPlugins  **
  - **IAM action:**  [kafkaconnect:ListCustomPlugins](#list_kafkaconnect-action-ListCustomPlugins) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [kafkaconnect:ListTagsForResource](#list_kafkaconnect-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkerConfigurations  **
  - **IAM action:**  [kafkaconnect:ListWorkerConfigurations](#list_kafkaconnect-action-ListWorkerConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [kafkaconnect:TagResource](#list_kafkaconnect-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [kafkaconnect:UntagResource](#list_kafkaconnect-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConnector  **
  - **IAM action:**  [kafkaconnect:UpdateConnector](#list_kafkaconnect-action-UpdateConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Managed Streaming for Kafka Connect
<a name="list_kafkaconnect-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateConnector.html)  **
  - **Description:** Grants permission to create an MSK Connect connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateCustomPlugin.html)  **
  - **Description:** Grants permission to create an MSK Connect custom plugin
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CreateWorkerConfiguration.html)  **
  - **Description:** Grants permission to create an MSK Connect worker configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete an MSK Connect connector
  - **Resource types (\*required):** [connector\*](#list_kafkaconnect-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteCustomPlugin.html)  **
  - **Description:** Grants permission to delete an MSK Connect custom plugin
  - **Resource types (\*required):** [custom plugin\*](#list_kafkaconnect-resource-customplugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DeleteWorkerConfiguration.html)  **
  - **Description:** Grants permission to delete an MSK Connect worker configuration
  - **Resource types (\*required):** [worker configuration\*](#list_kafkaconnect-resource-workerconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeConnector.html)  **
  - **Description:** Grants permission to describe an MSK Connect connector
  - **Resource types (\*required):** [connector\*](#list_kafkaconnect-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeConnectorOperation](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeConnectorOperation.html)  **
  - **Description:** Grants permission to describe a MSK Connect connector operation
  - **Resource types (\*required):** [connector operation\*](#list_kafkaconnect-resource-connectoroperation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCustomPlugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeCustomPlugin.html)  **
  - **Description:** Grants permission to describe an MSK Connect custom plugin
  - **Resource types (\*required):** [custom plugin\*](#list_kafkaconnect-resource-customplugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkerConfiguration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_DescribeWorkerConfiguration.html)  **
  - **Description:** Grants permission to describe an MSK Connect worker configuration
  - **Resource types (\*required):** [worker configuration\*](#list_kafkaconnect-resource-workerconfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConnectorOperations](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListConnectorOperations.html)  **
  - **Description:** Grants permission to list all operations of a given MSK Connect connector
  - **Resource types (\*required):** [connector\*](#list_kafkaconnect-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConnectors](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListConnectors.html)  **
  - **Description:** Grants permission to list all MSK Connect connectors in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCustomPlugins](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListCustomPlugins.html)  **
  - **Description:** Grants permission to list all MSK Connect custom plugins in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags of an MSK Connect resource
  - **Resource types (\*required):** [connector](#list_kafkaconnect-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom plugin](#list_kafkaconnect-resource-customplugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [worker configuration](#list_kafkaconnect-resource-workerconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWorkerConfigurations](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ListWorkerConfigurations.html)  **
  - **Description:** Grants permission to list all MSK Connect worker configurations in this account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_TagResource.html)  **
  - **Description:** Grants permission to tag an MSK Connect resource
  - **Resource types (\*required):** [connector](#list_kafkaconnect-resource-connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafkaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Resource types (\*required):** [custom plugin](#list_kafkaconnect-resource-customplugin) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafkaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Resource types (\*required):** [worker configuration](#list_kafkaconnect-resource-workerconfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_kafkaconnect-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an MSK Connect resource
  - **Resource types (\*required):** [connector](#list_kafkaconnect-resource-connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Resource types (\*required):** [custom plugin](#list_kafkaconnect-resource-customplugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Resource types (\*required):** [worker configuration](#list_kafkaconnect-resource-workerconfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_kafkaconnect-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConnector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_UpdateConnector.html)  **
  - **Description:** Grants permission to update an MSK Connect connector
  - **Resource types (\*required):** [connector\*](#list_kafkaconnect-resource-connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Managed Streaming for Kafka Connect
<a name="list_kafkaconnect-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [connector](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorSummary.html)  | arn:${Partition}:kafkaconnect:${Region}:${Account}:connector/${ConnectorName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_) | 
|  [connector operation](https://docs.aws.amazon.com/MSKC/latest/mskc/API_ConnectorOperation.html)  | arn:${Partition}:kafkaconnect:${Region}:${Account}:connector-operation/${ConnectorName}/${ConnectorUUID}/${UUID} | [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_) | 
|  [custom plugin](https://docs.aws.amazon.com/MSKC/latest/mskc/API_CustomPlugin.html)  | arn:${Partition}:kafkaconnect:${Region}:${Account}:custom-plugin/${CustomPluginName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_) | 
|  [worker configuration](https://docs.aws.amazon.com/MSKC/latest/mskc/API_WorkerConfiguration.html)  | arn:${Partition}:kafkaconnect:${Region}:${Account}:worker-configuration/${WorkerConfigurationName}/${UUID} | [aws:ResourceTag/${TagKey}](#list_kafkaconnect-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Managed Streaming for Kafka Connect
<a name="list_kafkaconnect-policy-keys"></a>

Amazon Managed Streaming for Kafka Connect defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 