

# Actions, resources, and condition keys for AWS Transform custom
<a name="list_transform-custom"></a>

AWS Transform custom (service prefix: `transform-custom`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/transform/latest/userguide/custom.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/transform/latest/userguide/custom.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/transform/latest/userguide/security-iam.html#security_iam_access-manage) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/transform-custom/transform-custom.json) for this service.

**Topics**
+ [Actions defined by AWS Transform custom](#list_transform-custom-actions-as-permissions)
+ [Resource types defined by AWS Transform custom](#list_transform-custom-resources-for-iam-policies)
+ [Condition keys for AWS Transform custom](#list_transform-custom-policy-keys)

## Actions defined by AWS Transform custom
<a name="list_transform-custom-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateFindings](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke BatchCreateFindings on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [BatchUpdateFindings](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke BatchUpdateFindings on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CompleteTransformationPackageUpload](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CompleteTransformationPackageUpload on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ConverseStream](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ConverseStream on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAnalysis](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateAnalysis on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCampaign](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateCampaign on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRemediation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateRemediation on AWS Transform custom
  - **Resource types (\*required):** [remediation\*](#list_transform-custom-resource-remediation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRepository](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateRepository on AWS Transform custom
  - **Resource types (\*required):** [repository\*](#list_transform-custom-resource-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateSource on AWS Transform custom
  - **Resource types (\*required):** [source\*](#list_transform-custom-resource-source)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTransformationPackageUrl](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke CreateTransformationPackageUrl on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnalysis](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteAnalysis on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCampaign](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteCampaign on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFinding](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteFinding on AWS Transform custom
  - **Resource types (\*required):** [finding\*](#list_transform-custom-resource-finding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKnowledgeItem](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteKnowledgeItem on AWS Transform custom
  - **Resource types (\*required):** [knowledge-item\*](#list_transform-custom-resource-knowledge-item)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRemediation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteRemediation on AWS Transform custom
  - **Resource types (\*required):** [remediation\*](#list_transform-custom-resource-remediation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRepository](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteRepository on AWS Transform custom
  - **Resource types (\*required):** [repository\*](#list_transform-custom-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteSource on AWS Transform custom
  - **Resource types (\*required):** [source\*](#list_transform-custom-resource-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTransformationPackage](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke DeleteTransformationPackage on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExecuteTransformation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ExecuteTransformation on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnalysis](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetAnalysis on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnalysisArtifactDownloadUrl](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetAnalysisArtifactDownloadUrl on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCampaign](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetCampaign on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFinding](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetFinding on AWS Transform custom
  - **Resource types (\*required):** [finding\*](#list_transform-custom-resource-finding)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingGroups](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetFindingGroups on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetKnowledgeItem](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetKnowledgeItem on AWS Transform custom
  - **Resource types (\*required):** [knowledge-item\*](#list_transform-custom-resource-knowledge-item)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRemediation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetRemediation on AWS Transform custom
  - **Resource types (\*required):** [remediation\*](#list_transform-custom-resource-remediation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRepository](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetRepository on AWS Transform custom
  - **Resource types (\*required):** [repository\*](#list_transform-custom-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetSource on AWS Transform custom
  - **Resource types (\*required):** [source\*](#list_transform-custom-resource-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTransformationPackageUrl](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke GetTransformationPackageUrl on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnalyses](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListAnalyses on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAnalysisArtifacts](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListAnalysisArtifacts on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCampaignRepositories](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListCampaignRepositories on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCampaigns](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListCampaign on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListFindings on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKnowledgeItems](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListKnowledgeItems on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRemediations](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListRemediations on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRepositories](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListRepositories on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSources](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListSources on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListTagsForResource on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTransformationPackageMetadata](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke ListTransformationPackageMetadata on AWS Transform custom
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTransformationPackageShares](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to list active shares of a Transformation Package
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SendTelemetryEvent](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to send a CLI telemetry event
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ShareTransformationPackage](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to share a Transformation Package with another AWS account or AWS Organization
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke TagResource on AWS Transform custom
  - **Resource types (\*required):** [analysis](#list_transform-custom-resource-analysis) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_transform-custom-resource-campaign) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [finding](#list_transform-custom-resource-finding) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [knowledge-item](#list_transform-custom-resource-knowledge-item) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_transform-custom-resource-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [remediation](#list_transform-custom-resource-remediation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_transform-custom-resource-repository) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [source](#list_transform-custom-resource-source) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_transform-custom-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnshareTransformationPackage](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to revoke an existing share of a Transformation Package
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UntagResource on AWS Transform custom
  - **Resource types (\*required):** [analysis](#list_transform-custom-resource-analysis) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [campaign](#list_transform-custom-resource-campaign) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [finding](#list_transform-custom-resource-finding) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [knowledge-item](#list_transform-custom-resource-knowledge-item) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [package](#list_transform-custom-resource-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [remediation](#list_transform-custom-resource-remediation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [repository](#list_transform-custom-resource-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Resource types (\*required):** [source](#list_transform-custom-resource-source) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transform-custom-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnalysis](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateAnalysis on AWS Transform custom
  - **Resource types (\*required):** [analysis\*](#list_transform-custom-resource-analysis)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaign](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateCampaign on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCampaignRepositoryStatus](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateCampaignRepositories on AWS Transform custom
  - **Resource types (\*required):** [campaign\*](#list_transform-custom-resource-campaign)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKnowledgeItemConfiguration](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateKnowledgeItemConfiguration on AWS Transform custom
  - **Resource types (\*required):** [package\*](#list_transform-custom-resource-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKnowledgeItemStatus](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateKnowledgeItemStatus on AWS Transform custom
  - **Resource types (\*required):** [knowledge-item\*](#list_transform-custom-resource-knowledge-item)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRemediation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateRemediation on AWS Transform custom
  - **Resource types (\*required):** [remediation\*](#list_transform-custom-resource-remediation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRepository](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateRepository on AWS Transform custom
  - **Resource types (\*required):** [repository\*](#list_transform-custom-resource-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSource](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  **
  - **Description:** Grants permission to invoke UpdateSource on AWS Transform custom
  - **Resource types (\*required):** [source\*](#list_transform-custom-resource-source)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Transform custom
<a name="list_transform-custom-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [analysis](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:analysis/${AnalysisId} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [campaign](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:campaign/${Name} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [finding](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:finding/${FindingId} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [knowledge-item](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:package/${TransformationPackageName}/knowledge-item/${Id} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [package](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:package/${Name} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [remediation](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:remediation/${RemediationId} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [repository](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:repository/${RepositoryId} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 
|  [source](https://docs.aws.amazon.com/transform/latest/userguide/custom.html)  | arn:${Partition}:transform-custom:${Region}:${Account}:source/${Name} | [aws:ResourceTag/${TagKey}](#list_transform-custom-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Transform custom
<a name="list_transform-custom-policy-keys"></a>

AWS Transform custom defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 