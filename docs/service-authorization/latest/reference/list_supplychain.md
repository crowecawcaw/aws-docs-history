

# Actions, resources, and condition keys for AWS Supply Chain
<a name="list_supplychain"></a>

AWS Supply Chain (service prefix: `scn`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/scn/scn.json) for this service.

**Topics**
+ [API operations defined by AWS Supply Chain](#list_supplychain-operations)
+ [Actions defined by AWS Supply Chain](#list_supplychain-actions-as-permissions)
+ [Resource types defined by AWS Supply Chain](#list_supplychain-resources-for-iam-policies)
+ [Condition keys for AWS Supply Chain](#list_supplychain-policy-keys)

## API operations defined by AWS Supply Chain
<a name="list_supplychain-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_supplychain-actions-as-permissions).




- **   CreateBillOfMaterialsImportJob  **
  - **IAM action:**  [scn:CreateBillOfMaterialsImportJob](#list_supplychain-action-CreateBillOfMaterialsImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataIntegrationFlow  **
  - **IAM action:**  [scn:CreateDataIntegrationFlow](#list_supplychain-action-CreateDataIntegrationFlow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scn:TagResource](#list_supplychain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataLakeDataset  **
  - **IAM action:**  [scn:CreateDataLakeDataset](#list_supplychain-action-CreateDataLakeDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scn:TagResource](#list_supplychain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataLakeNamespace  **
  - **IAM action:**  [scn:CreateDataLakeNamespace](#list_supplychain-action-CreateDataLakeNamespace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scn:TagResource](#list_supplychain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInstance  **
  - **IAM action:**  [scn:CreateInstance](#list_supplychain-action-CreateInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scn:TagResource](#list_supplychain-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDataIntegrationFlow  **
  - **IAM action:**  [scn:DeleteDataIntegrationFlow](#list_supplychain-action-DeleteDataIntegrationFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataLakeDataset  **
  - **IAM action:**  [scn:DeleteDataLakeDataset](#list_supplychain-action-DeleteDataLakeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataLakeNamespace  **
  - **IAM action:**  [scn:DeleteDataLakeNamespace](#list_supplychain-action-DeleteDataLakeNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInstance  **
  - **IAM action:**  [scn:DeleteInstance](#list_supplychain-action-DeleteInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBillOfMaterialsImportJob  **
  - **IAM action:**  [scn:GetBillOfMaterialsImportJob](#list_supplychain-action-GetBillOfMaterialsImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataIntegrationEvent  **
  - **IAM action:**  [scn:GetDataIntegrationEvent](#list_supplychain-action-GetDataIntegrationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataIntegrationFlow  **
  - **IAM action:**  [scn:GetDataIntegrationFlow](#list_supplychain-action-GetDataIntegrationFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataIntegrationFlowExecution  **
  - **IAM action:**  [scn:GetDataIntegrationFlowExecution](#list_supplychain-action-GetDataIntegrationFlowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakeDataset  **
  - **IAM action:**  [scn:GetDataLakeDataset](#list_supplychain-action-GetDataLakeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakeNamespace  **
  - **IAM action:**  [scn:GetDataLakeNamespace](#list_supplychain-action-GetDataLakeNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInstance  **
  - **IAM action:**  [scn:GetInstance](#list_supplychain-action-GetInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataIntegrationEvents  **
  - **IAM action:**  [scn:ListDataIntegrationEvents](#list_supplychain-action-ListDataIntegrationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataIntegrationFlowExecutions  **
  - **IAM action:**  [scn:ListDataIntegrationFlowExecutions](#list_supplychain-action-ListDataIntegrationFlowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataIntegrationFlows  **
  - **IAM action:**  [scn:ListDataIntegrationFlows](#list_supplychain-action-ListDataIntegrationFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataLakeDatasets  **
  - **IAM action:**  [scn:ListDataLakeDatasets](#list_supplychain-action-ListDataLakeDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataLakeNamespaces  **
  - **IAM action:**  [scn:ListDataLakeNamespaces](#list_supplychain-action-ListDataLakeNamespaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstances  **
  - **IAM action:**  [scn:ListInstances](#list_supplychain-action-ListInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [scn:ListTagsForResource](#list_supplychain-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SendDataIntegrationEvent  **
  - **IAM action:**  [scn:SendDataIntegrationEvent](#list_supplychain-action-SendDataIntegrationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [scn:TagResource](#list_supplychain-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [scn:UntagResource](#list_supplychain-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDataIntegrationFlow  **
  - **IAM action:**  [scn:UpdateDataIntegrationFlow](#list_supplychain-action-UpdateDataIntegrationFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataLakeDataset  **
  - **IAM action:**  [scn:UpdateDataLakeDataset](#list_supplychain-action-UpdateDataLakeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataLakeNamespace  **
  - **IAM action:**  [scn:UpdateDataLakeNamespace](#list_supplychain-action-UpdateDataLakeNamespace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInstance  **
  - **IAM action:**  [scn:UpdateInstance](#list_supplychain-action-UpdateInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Supply Chain
<a name="list_supplychain-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssignAdminPermissionsToUser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to add AWS Supply Chain administrator permission to federated user
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBillOfMaterialsImportJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create a BillOfMaterialsImportJob which will import a CSV file of BillOfMaterials records
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataIntegrationFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create DataIntegrationFlow that can transform from multiple sources to one target
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supplychain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataLakeDataset](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create the data lake dataset
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supplychain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataLakeNamespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create the data lake namespace
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supplychain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInstance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create a new AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supplychain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSSOApplication](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create IAM Identity Center application for a AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataIntegrationFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to delete the DataIntegrationFlow
  - **Resource types (\*required):** [data-integration-flow\*](#list_supplychain-resource-data-integration-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataLakeDataset](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to delete the data lake dataset
  - **Resource types (\*required):** [dataset\*](#list_supplychain-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataLakeNamespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to delete the data lake namespace
  - **Resource types (\*required):** [namespace\*](#list_supplychain-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInstance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to delete an AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSSOApplication](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to delete IAM Identity Center application of the AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeInstance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to view details of an AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBillOfMaterialsImportJob](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to view status and details of a BillOfMaterialsImportJob
  - **Resource types (\*required):** [bill-of-materials-import-job\*](#list_supplychain-resource-bill-of-materials-import-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataIntegrationEvent](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to get a DataIntegrationEvent
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataIntegrationFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to get the DataIntegrationFlow details
  - **Resource types (\*required):** [data-integration-flow\*](#list_supplychain-resource-data-integration-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataIntegrationFlowExecution](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to get a particular execution of one specified DataIntegrationFlow
  - **Resource types (\*required):** [data-integration-flow\*](#list_supplychain-resource-data-integration-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataLakeDataset](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to get the dataset details
  - **Resource types (\*required):** [dataset\*](#list_supplychain-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataLakeNamespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to get the namespace details
  - **Resource types (\*required):** [namespace\*](#list_supplychain-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInstance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to view details of an AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAdminUsers](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list AWS Supply Chain administrators of an instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataIntegrationEvents](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list all DataIntegrationEvents under an instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataIntegrationFlowExecutions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list all executions of one specified DataIntegrationFlow
  - **Resource types (\*required):** [data-integration-flow\*](#list_supplychain-resource-data-integration-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataIntegrationFlows](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list all the DataIntegrationFlows in a paginated way
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataLakeDatasets](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list the data lake datasets under specific instance or namespace
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataLakeNamespaces](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list the data lake namespaces under specific instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInstances](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to view the AWS Supply Chain instances associated with an AWS account
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to list tags for an AWS Supply Chain resource
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RemoveAdminPermissionsForUser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to remove AWS Supply Chain administrator permission from federated user
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendDataIntegrationEvent](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to create a DataIntegrationEvent which will ingest data in real-time
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to tag an AWS Supply Chain resource
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_supplychain-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to remove tag from an AWS Supply Chain resource
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_supplychain-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDataIntegrationFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to update the DataIntegrationFlow
  - **Resource types (\*required):** [data-integration-flow\*](#list_supplychain-resource-data-integration-flow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataLakeDataset](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to update the data lake dataset
  - **Resource types (\*required):** [dataset\*](#list_supplychain-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataLakeNamespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to update the data lake namespace
  - **Resource types (\*required):** [namespace\*](#list_supplychain-resource-namespace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInstance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  **
  - **Description:** Grants permission to update an AWS Supply Chain instance
  - **Resource types (\*required):** [instance\*](#list_supplychain-resource-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Supply Chain
<a name="list_supplychain-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [bill-of-materials-import-job](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  | arn:${Partition}:scn:${Region}:${Account}:instance/${InstanceId}/bill-of-materials-import-job/${JobId} |   | 
|  [data-integration-flow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  | arn:${Partition}:scn:${Region}:${Account}:instance/${InstanceId}/data-integration-flows/${FlowName} | [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  | arn:${Partition}:scn:${Region}:${Account}:instance/${InstanceId}/namespaces/${Namespace}/datasets/${DatasetName} | [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_) | 
|  [instance](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  | arn:${Partition}:scn:${Region}:${Account}:instance/${InstanceId} | [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_) | 
|  [namespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssupplychain.html)  | arn:${Partition}:scn:${Region}:${Account}:instance/${InstanceId}/namespaces/${Namespace} | [aws:ResourceTag/${TagKey}](#list_supplychain-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Supply Chain
<a name="list_supplychain-policy-keys"></a>

AWS Supply Chain defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by using tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by using tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by using tag keys in the request | ArrayOfString | 