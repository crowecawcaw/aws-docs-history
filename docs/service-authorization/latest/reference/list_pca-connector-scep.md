

# Actions, resources, and condition keys for AWS Private CA Connector for SCEP
<a name="list_pca-connector-scep"></a>

AWS Private CA Connector for SCEP (service prefix: `pca-connector-scep`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pca-connector-scep/pca-connector-scep.json) for this service.

**Topics**
+ [API operations defined by AWS Private CA Connector for SCEP](#list_pca-connector-scep-operations)
+ [Actions defined by AWS Private CA Connector for SCEP](#list_pca-connector-scep-actions-as-permissions)
+ [Resource types defined by AWS Private CA Connector for SCEP](#list_pca-connector-scep-resources-for-iam-policies)
+ [Condition keys for AWS Private CA Connector for SCEP](#list_pca-connector-scep-policy-keys)

## API operations defined by AWS Private CA Connector for SCEP
<a name="list_pca-connector-scep-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pca-connector-scep-actions-as-permissions).




- **   CreateChallenge  **
  - **IAM action:**  [pca-connector-scep:CreateChallenge](#list_pca-connector-scep-action-CreateChallenge)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pca-connector-scep:TagResource](#list_pca-connector-scep-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnector  **
  - **IAM action:**  [pca-connector-scep:CreateConnector](#list_pca-connector-scep-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pca-connector-scep:TagResource](#list_pca-connector-scep-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteChallenge  **
  - **IAM action:**  [pca-connector-scep:DeleteChallenge](#list_pca-connector-scep-action-DeleteChallenge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [pca-connector-scep:DeleteConnector](#list_pca-connector-scep-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetChallengeMetadata  **
  - **IAM action:**  [pca-connector-scep:GetChallengeMetadata](#list_pca-connector-scep-action-GetChallengeMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChallengePassword  **
  - **IAM action:**  [pca-connector-scep:GetChallengePassword](#list_pca-connector-scep-action-GetChallengePassword) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnector  **
  - **IAM action:**  [pca-connector-scep:GetConnector](#list_pca-connector-scep-action-GetConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListChallengeMetadata  **
  - **IAM action:**  [pca-connector-scep:ListChallengeMetadata](#list_pca-connector-scep-action-ListChallengeMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [pca-connector-scep:ListConnectors](#list_pca-connector-scep-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [pca-connector-scep:ListTagsForResource](#list_pca-connector-scep-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [pca-connector-scep:TagResource](#list_pca-connector-scep-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [pca-connector-scep:UntagResource](#list_pca-connector-scep-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Private CA Connector for SCEP
<a name="list_pca-connector-scep-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html)  **
  - **Description:** Grants permission to create a Challenge for a Connector
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-scep-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-scep-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateConnector.html)  **
  - **Description:** Grants permission to create a SCEP Connector in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-scep-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_DeleteChallenge.html)  **
  - **Description:** Grants permission to delete a Challenge for a Connector
  - **Resource types (\*required):** [Challenge\*](#list_pca-connector-scep-resource-Challenge)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete a SCEP Connector in your account
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-scep-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengeMetadata.html)  **
  - **Description:** Grants permission to get a Challenge for a Connector
  - **Resource types (\*required):** [Challenge\*](#list_pca-connector-scep-resource-Challenge)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChallengePassword](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengePassword.html)  **
  - **Description:** Grants permission to get a Challenge password for a Connector
  - **Resource types (\*required):** [Challenge\*](#list_pca-connector-scep-resource-Challenge)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetConnector.html)  **
  - **Description:** Grants permission to get a SCEP Connector in your account
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-scep-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListChallengeMetadata.html)  **
  - **Description:** Grants permission to list Challenges for a Connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list the SCEP Connectors in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a pca-connector-scep resource in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a pca-connector-scep resource in your account
  - **Resource types (\*required):** [Challenge](#list_pca-connector-scep-resource-Challenge) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-scep-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_pca-connector-scep-resource-Connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-scep-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a pca-connector-scep resource in your account
  - **Resource types (\*required):** [Challenge](#list_pca-connector-scep-resource-Challenge) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_pca-connector-scep-resource-Connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-scep-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Private CA Connector for SCEP
<a name="list_pca-connector-scep-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Challenge](${ActionsDocRoot}API_Challenge.html)  | arn:${Partition}:pca-connector-scep:${Region}:${Account}:connector/${ConnectorId}/challenge/${ChallengeId} | [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_) | 
|  [Connector](${ActionsDocRoot}API_Connector.html)  | arn:${Partition}:pca-connector-scep:${Region}:${Account}:connector/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_pca-connector-scep-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Private CA Connector for SCEP
<a name="list_pca-connector-scep-policy-keys"></a>

AWS Private CA Connector for SCEP defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.htmlreference_policies_iam-condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.htmlreference_policies_iam-condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-scep.htmlreference_policies_iam-condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 