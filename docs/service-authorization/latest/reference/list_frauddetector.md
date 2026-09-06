

# Actions, resources, and condition keys for Amazon Fraud Detector
<a name="list_frauddetector"></a>

Amazon Fraud Detector (service prefix: `frauddetector`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/frauddetector/latest/ug/what-is-frauddetector.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/frauddetector/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/frauddetector/latest/ug/assets.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/frauddetector/frauddetector.json) for this service.

**Topics**
+ [API operations defined by Amazon Fraud Detector](#list_frauddetector-operations)
+ [Actions defined by Amazon Fraud Detector](#list_frauddetector-actions-as-permissions)
+ [Permission-only actions for Amazon Fraud Detector](#list_frauddetector-permission-only-actions)
+ [Resource types defined by Amazon Fraud Detector](#list_frauddetector-resources-for-iam-policies)
+ [Condition keys for Amazon Fraud Detector](#list_frauddetector-policy-keys)

## API operations defined by Amazon Fraud Detector
<a name="list_frauddetector-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_frauddetector-actions-as-permissions).




- **   BatchCreateVariable  **
  - **IAM action:**  [frauddetector:BatchCreateVariable](#list_frauddetector-action-BatchCreateVariable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   BatchGetVariable  **
  - **IAM action:**  [frauddetector:BatchGetVariable](#list_frauddetector-action-BatchGetVariable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   CancelBatchImportJob  **
  - **IAM action:**  [frauddetector:CancelBatchImportJob](#list_frauddetector-action-CancelBatchImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelBatchPredictionJob  **
  - **IAM action:**  [frauddetector:CancelBatchPredictionJob](#list_frauddetector-action-CancelBatchPredictionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBatchImportJob  **
  - **IAM action:**  [frauddetector:CreateBatchImportJob](#list_frauddetector-action-CreateBatchImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** frauddetector.amazonaws.com / **Access level:** Write

- **   CreateBatchPredictionJob  **
  - **IAM action:**  [frauddetector:CreateBatchPredictionJob](#list_frauddetector-action-CreateBatchPredictionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** frauddetector.amazonaws.com / **Access level:** Write

- **   CreateDetectorVersion  **
  - **IAM action:**  [frauddetector:CreateDetectorVersion](#list_frauddetector-action-CreateDetectorVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateList  **
  - **IAM action:**  [frauddetector:CreateList](#list_frauddetector-action-CreateList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateModel  **
  - **IAM action:**  [frauddetector:CreateModel](#list_frauddetector-action-CreateModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateModelVersion  **
  - **IAM action:**  [frauddetector:CreateModelVersion](#list_frauddetector-action-CreateModelVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** frauddetector.amazonaws.com / **Access level:** Write

- **   CreateRule  **
  - **IAM action:**  [frauddetector:CreateRule](#list_frauddetector-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVariable  **
  - **IAM action:**  [frauddetector:CreateVariable](#list_frauddetector-action-CreateVariable)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBatchImportJob  **
  - **IAM action:**  [frauddetector:DeleteBatchImportJob](#list_frauddetector-action-DeleteBatchImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBatchPredictionJob  **
  - **IAM action:**  [frauddetector:DeleteBatchPredictionJob](#list_frauddetector-action-DeleteBatchPredictionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDetector  **
  - **IAM action:**  [frauddetector:DeleteDetector](#list_frauddetector-action-DeleteDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDetectorVersion  **
  - **IAM action:**  [frauddetector:DeleteDetectorVersion](#list_frauddetector-action-DeleteDetectorVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntityType  **
  - **IAM action:**  [frauddetector:DeleteEntityType](#list_frauddetector-action-DeleteEntityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEvent  **
  - **IAM action:**  [frauddetector:DeleteEvent](#list_frauddetector-action-DeleteEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventType  **
  - **IAM action:**  [frauddetector:DeleteEventType](#list_frauddetector-action-DeleteEventType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEventsByEventType  **
  - **IAM action:**  [frauddetector:DeleteEventsByEventType](#list_frauddetector-action-DeleteEventsByEventType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExternalModel  **
  - **IAM action:**  [frauddetector:DeleteExternalModel](#list_frauddetector-action-DeleteExternalModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLabel  **
  - **IAM action:**  [frauddetector:DeleteLabel](#list_frauddetector-action-DeleteLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteList  **
  - **IAM action:**  [frauddetector:DeleteList](#list_frauddetector-action-DeleteList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModel  **
  - **IAM action:**  [frauddetector:DeleteModel](#list_frauddetector-action-DeleteModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelVersion  **
  - **IAM action:**  [frauddetector:DeleteModelVersion](#list_frauddetector-action-DeleteModelVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOutcome  **
  - **IAM action:**  [frauddetector:DeleteOutcome](#list_frauddetector-action-DeleteOutcome) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRule  **
  - **IAM action:**  [frauddetector:DeleteRule](#list_frauddetector-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVariable  **
  - **IAM action:**  [frauddetector:DeleteVariable](#list_frauddetector-action-DeleteVariable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDetector  **
  - **IAM action:**  [frauddetector:DescribeDetector](#list_frauddetector-action-DescribeDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelVersions  **
  - **IAM action:**  [frauddetector:DescribeModelVersions](#list_frauddetector-action-DescribeModelVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBatchImportJobs  **
  - **IAM action:**  [frauddetector:GetBatchImportJobs](#list_frauddetector-action-GetBatchImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBatchPredictionJobs  **
  - **IAM action:**  [frauddetector:GetBatchPredictionJobs](#list_frauddetector-action-GetBatchPredictionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetDeleteEventsByEventTypeStatus  **
  - **IAM action:**  [frauddetector:GetDeleteEventsByEventTypeStatus](#list_frauddetector-action-GetDeleteEventsByEventTypeStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDetectorVersion  **
  - **IAM action:**  [frauddetector:GetDetectorVersion](#list_frauddetector-action-GetDetectorVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDetectors  **
  - **IAM action:**  [frauddetector:GetDetectors](#list_frauddetector-action-GetDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetEntityTypes  **
  - **IAM action:**  [frauddetector:GetEntityTypes](#list_frauddetector-action-GetEntityTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetEvent  **
  - **IAM action:**  [frauddetector:GetEvent](#list_frauddetector-action-GetEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventPrediction  **
  - **IAM action:**  [frauddetector:GetEventPrediction](#list_frauddetector-action-GetEventPrediction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventPredictionMetadata  **
  - **IAM action:**  [frauddetector:GetEventPredictionMetadata](#list_frauddetector-action-GetEventPredictionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEventTypes  **
  - **IAM action:**  [frauddetector:GetEventTypes](#list_frauddetector-action-GetEventTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetExternalModels  **
  - **IAM action:**  [frauddetector:GetExternalModels](#list_frauddetector-action-GetExternalModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetKMSEncryptionKey  **
  - **IAM action:**  [frauddetector:GetKMSEncryptionKey](#list_frauddetector-action-GetKMSEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLabels  **
  - **IAM action:**  [frauddetector:GetLabels](#list_frauddetector-action-GetLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetListElements  **
  - **IAM action:**  [frauddetector:GetListElements](#list_frauddetector-action-GetListElements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetListsMetadata  **
  - **IAM action:**  [frauddetector:GetListsMetadata](#list_frauddetector-action-GetListsMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetModelVersion  **
  - **IAM action:**  [frauddetector:GetModelVersion](#list_frauddetector-action-GetModelVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModels  **
  - **IAM action:**  [frauddetector:GetModels](#list_frauddetector-action-GetModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetOutcomes  **
  - **IAM action:**  [frauddetector:GetOutcomes](#list_frauddetector-action-GetOutcomes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetRules  **
  - **IAM action:**  [frauddetector:GetRules](#list_frauddetector-action-GetRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetVariables  **
  - **IAM action:**  [frauddetector:GetVariables](#list_frauddetector-action-GetVariables) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventPredictions  **
  - **IAM action:**  [frauddetector:ListEventPredictions](#list_frauddetector-action-ListEventPredictions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [frauddetector:ListTagsForResource](#list_frauddetector-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutDetector  **
  - **IAM action:**  [frauddetector:PutDetector](#list_frauddetector-action-PutDetector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutEntityType  **
  - **IAM action:**  [frauddetector:PutEntityType](#list_frauddetector-action-PutEntityType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutEventType  **
  - **IAM action:**  [frauddetector:PutEventType](#list_frauddetector-action-PutEventType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutExternalModel  **
  - **IAM action:**  [frauddetector:PutExternalModel](#list_frauddetector-action-PutExternalModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** frauddetector.amazonaws.com / **Access level:** Write

- **   PutLabel  **
  - **IAM action:**  [frauddetector:PutLabel](#list_frauddetector-action-PutLabel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutOutcome  **
  - **IAM action:**  [frauddetector:PutOutcome](#list_frauddetector-action-PutOutcome)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   SendEvent  **
  - **IAM action:**  [frauddetector:SendEvent](#list_frauddetector-action-SendEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [frauddetector:UntagResource](#list_frauddetector-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDetectorVersion  **
  - **IAM action:**  [frauddetector:UpdateDetectorVersion](#list_frauddetector-action-UpdateDetectorVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDetectorVersionMetadata  **
  - **IAM action:**  [frauddetector:UpdateDetectorVersionMetadata](#list_frauddetector-action-UpdateDetectorVersionMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDetectorVersionStatus  **
  - **IAM action:**  [frauddetector:UpdateDetectorVersionStatus](#list_frauddetector-action-UpdateDetectorVersionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEventLabel  **
  - **IAM action:**  [frauddetector:UpdateEventLabel](#list_frauddetector-action-UpdateEventLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateList  **
  - **IAM action:**  [frauddetector:UpdateList](#list_frauddetector-action-UpdateList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModel  **
  - **IAM action:**  [frauddetector:UpdateModel](#list_frauddetector-action-UpdateModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModelVersionStatus  **
  - **IAM action:**  [frauddetector:UpdateModelVersionStatus](#list_frauddetector-action-UpdateModelVersionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleMetadata  **
  - **IAM action:**  [frauddetector:UpdateRuleMetadata](#list_frauddetector-action-UpdateRuleMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRuleVersion  **
  - **IAM action:**  [frauddetector:TagResource](#list_frauddetector-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [frauddetector:UpdateRuleVersion](#list_frauddetector-action-UpdateRuleVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateVariable  **
  - **IAM action:**  [frauddetector:UpdateVariable](#list_frauddetector-action-UpdateVariable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Fraud Detector
<a name="list_frauddetector-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_BatchCreateVariable.html)  **
  - **Description:** Grants permission to create a batch of variables
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [BatchGetVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_BatchGetVariable.html)  **
  - **Description:** Grants permission to get a batch of variables
  - **Resource types (\*required):** [variable\*](#list_frauddetector-resource-variable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [CancelBatchImportJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_CancelBatchImportJob.html)  **
  - **Description:** Grants permission to cancel the specified batch import job
  - **Resource types (\*required):** [batch-import\*](#list_frauddetector-resource-batch-import)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelBatchPredictionJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_CancelBatchPredictionJob.html)  **
  - **Description:** Grants permission to cancel the specified batch prediction job
  - **Resource types (\*required):** [batch-prediction\*](#list_frauddetector-resource-batch-prediction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBatchImportJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateBatchImportJob.html)  **
  - **Description:** Grants permission to create a batch import job
  - **Resource types (\*required):** [batch-import\*](#list_frauddetector-resource-batch-import) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateBatchPredictionJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateBatchPredictionJob.html)  **
  - **Description:** Grants permission to create a batch prediction job
  - **Resource types (\*required):** [batch-prediction\*](#list_frauddetector-resource-batch-prediction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDetectorVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateDetectorVersion.html)  **
  - **Description:** Grants permission to create a detector version. The detector version starts in a DRAFT status
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateList.html)  **
  - **Description:** Grants permission to create a list
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModel](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateModel.html)  **
  - **Description:** Grants permission to create a model using the specified model type
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model\*](#list_frauddetector-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModelVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateModelVersion.html)  **
  - **Description:** Grants permission to create a version of the model using the specified model type and model id
  - **Resource types (\*required):** [model\*](#list_frauddetector-resource-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRule](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateRule.html)  **
  - **Description:** Grants permission to create a rule for use with the specified detector
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateVariable.html)  **
  - **Description:** Grants permission to create a variable
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBatchImportJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteBatchImportJob.html)  **
  - **Description:** Grants permission to delete a batch import job
  - **Resource types (\*required):** [batch-import\*](#list_frauddetector-resource-batch-import)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBatchPredictionJob](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteBatchPredictionJob.html)  **
  - **Description:** Grants permission to delete a batch prediction job
  - **Resource types (\*required):** [batch-prediction\*](#list_frauddetector-resource-batch-prediction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDetector](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteDetector.html)  **
  - **Description:** Grants permission to delete the detector. Before deleting a detector, you must first delete all detector versions and rule versions associated with the detector
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDetectorVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteDetectorVersion.html)  **
  - **Description:** Grants permission to delete the detector version. You cannot delete detector versions that are in ACTIVE status
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEntityType](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEntityType.html)  **
  - **Description:** Grants permission to delete an entity type. You cannot delete an entity type that is included in an event type
  - **Resource types (\*required):** [entity-type\*](#list_frauddetector-resource-entity-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEvent](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEvent.html)  **
  - **Description:** Grants permission to deletes the specified event
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventType](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEventType.html)  **
  - **Description:** Grants permission to delete an event type. You cannot delete an event type that is used in a detector or a model
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEventsByEventType](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteEventsByEventType.html)  **
  - **Description:** Grants permission to delete events for the specified event type
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExternalModel](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteExternalModel.html)  **
  - **Description:** Grants permission to remove a SageMaker model from Amazon Fraud Detector. You can remove an Amazon SageMaker model if it is not associated with a detector version
  - **Resource types (\*required):** [external-model\*](#list_frauddetector-resource-external-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteLabel.html)  **
  - **Description:** Grants permission to delete a label. You cannot delete labels that are included in an event type in Amazon Fraud Detector. You cannot delete a label assigned to an event ID. You must first delete the relevant event ID
  - **Resource types (\*required):** [label\*](#list_frauddetector-resource-label)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteList](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteList.html)  **
  - **Description:** Grants permission to delete a list
  - **Resource types (\*required):** [list\*](#list_frauddetector-resource-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModel](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteModel.html)  **
  - **Description:** Grants permission to delete a model. You can delete models and model versions in Amazon Fraud Detector, provided that they are not associated with a detector version
  - **Resource types (\*required):** [model\*](#list_frauddetector-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteModelVersion.html)  **
  - **Description:** Grants permission to delete a model version. You can delete models and model versions in Amazon Fraud Detector, provided that they are not associated with a detector version
  - **Resource types (\*required):** [model-version\*](#list_frauddetector-resource-model-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOutcome](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteOutcome.html)  **
  - **Description:** Grants permission to delete an outcome. You cannot delete an outcome that is used in a rule version
  - **Resource types (\*required):** [outcome\*](#list_frauddetector-resource-outcome)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete the rule. You cannot delete a rule if it is used by an ACTIVE or INACTIVE detector version
  - **Resource types (\*required):** [rule\*](#list_frauddetector-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_DeleteVariable.html)  **
  - **Description:** Grants permission to delete a variable. You cannot delete variables that are included in an event type in Amazon Fraud Detector
  - **Resource types (\*required):** [variable\*](#list_frauddetector-resource-variable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDetector](https://docs.aws.amazon.com/frauddetector/latest/api/API_DescribeDetector.html)  **
  - **Description:** Grants permission to get all versions for a specified detector
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelVersions](https://docs.aws.amazon.com/frauddetector/latest/api/API_DescribeModelVersions.html)  **
  - **Description:** Grants permission to get all of the model versions for the specified model type or for the specified model type and model ID. You can also get details for a single, specified model version
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBatchImportJobs](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetBatchImportJobs.html)  **
  - **Description:** Grants permission to get all batch import jobs or a specific job if you specify a job ID
  - **Resource types (\*required):** [batch-import](#list_frauddetector-resource-batch-import)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetBatchPredictionJobs](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetBatchPredictionJobs.html)  **
  - **Description:** Grants permission to get all batch prediction jobs or a specific job if you specify a job ID. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 50 records per page. If you provide a maxResults, the value must be between 1 and 50. To get the next page results, provide the pagination token from the GetBatchPredictionJobsResponse as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [batch-prediction](#list_frauddetector-resource-batch-prediction)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDeleteEventsByEventTypeStatus](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetDeleteEventsByEventTypeStatus.html)  **
  - **Description:** Grants permission to get a specific event type DeleteEventsByEventType API execution status
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDetectorVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetDetectorVersion.html)  **
  - **Description:** Grants permission to get a particular detector version
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDetectors](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetDetectors.html)  **
  - **Description:** Grants permission to get all detectors or a single detector if a detectorId is specified. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 10 records per page. If you provide a maxResults, the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetDetectorsResponse as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [detector](#list_frauddetector-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetEntityTypes](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEntityTypes.html)  **
  - **Description:** Grants permission to get all entity types or a specific entity type if a name is specified. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 10 records per page. If you provide a maxResults, the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetEntityTypesResponse as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [entity-type](#list_frauddetector-resource-entity-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetEvent](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEvent.html)  **
  - **Description:** Grants permission to get the details of the specified event
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventPrediction](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPrediction.html)  **
  - **Description:** Grants permission to evaluate an event against a detector version. If a version ID is not provided, the detector's (ACTIVE) version is used
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventPredictionMetadata](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPredictionMetadata.html)  **
  - **Description:** Grants permission to get more details of a particular prediction
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEventTypes](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventTypes.html)  **
  - **Description:** Grants permission to get all event types or a specific event type if name is provided. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 10 records per page. If you provide a maxResults, the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetEventTypesResponse as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [event-type](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetExternalModels](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetExternalModels.html)  **
  - **Description:** Grants permission to get the details for one or more Amazon SageMaker models that have been imported into the service. This is a paginated API. If you provide a null maxResults, this actions retrieves a maximum of 10 records per page. If you provide a maxResults, the value must be between 5 and 10. To get the next page results, provide the pagination token from the GetExternalModelsResult as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetKMSEncryptionKey](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetKMSEncryptionKey.html)  **
  - **Description:** Grants permission to get the encryption key if a Key Management Service (KMS) customer master key (CMK) has been specified to be used to encrypt content in Amazon Fraud Detector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLabels](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetLabels.html)  **
  - **Description:** Grants permission to get all labels or a specific label if name is provided. This is a paginated API. If you provide a null maxResults, this action retrieves a maximum of 50 records per page. If you provide a maxResults, the value must be between 10 and 50. To get the next page results, provide the pagination token from the GetGetLabelsResponse as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [label](#list_frauddetector-resource-label)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetListElements](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetListElements.html)  **
  - **Description:** Grants permission to get elements of a list
  - **Resource types (\*required):** [list\*](#list_frauddetector-resource-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetListsMetadata](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetListsMetadata.html)  **
  - **Description:** Grants permission to get metadata about lists
  - **Resource types (\*required):** [list](#list_frauddetector-resource-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetModelVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetModelVersion.html)  **
  - **Description:** Grants permission to get the details of the specified model version
  - **Resource types (\*required):** [model-version\*](#list_frauddetector-resource-model-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModels](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetModels.html)  **
  - **Description:** Grants permission to get one or more models. Gets all models for the AWS account if no model type and no model id provided. Gets all models for the AWS account and model type, if the model type is specified but model id is not provided. Gets a specific model if (model type, model id) tuple is specified
  - **Resource types (\*required):** [model](#list_frauddetector-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetOutcomes](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetOutcomes.html)  **
  - **Description:** Grants permission to get one or more outcomes. This is a paginated API. If you provide a null maxResults, this actions retrieves a maximum of 100 records per page. If you provide a maxResults, the value must be between 50 and 100. To get the next page results, provide the pagination token from the GetOutcomesResult as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [outcome](#list_frauddetector-resource-outcome)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetRules](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetRules.html)  **
  - **Description:** Grants permission to get all rules for a detector (paginated) if ruleId and ruleVersion are not specified. Gets all rules for the detector and the ruleId if present (paginated). Gets a specific rule if both the ruleId and the ruleVersion are specified
  - **Resource types (\*required):** [rule](#list_frauddetector-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetVariables](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetVariables.html)  **
  - **Description:** Grants permission to get all of the variables or the specific variable. This is a paginated API. Providing null maxSizePerPage results in retrieving maximum of 100 records per page. If you provide maxSizePerPage the value must be between 50 and 100. To get the next page result, a provide a pagination token from GetVariablesResult as part of your request. Null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEventPredictions](https://docs.aws.amazon.com/frauddetector/latest/api/API_ListEventPredictions.html)  **
  - **Description:** Grants permission to get a list of past predictions
  - **Resource types (\*required):** [detector](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector-version](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-type](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/frauddetector/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags associated with the resource. This is a paginated API. To get the next page results, provide the pagination token from the response as part of your request. A null pagination token fetches the records from the beginning
  - **Resource types (\*required):** [batch-import](#list_frauddetector-resource-batch-import) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [batch-prediction](#list_frauddetector-resource-batch-prediction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector-version](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-type](#list_frauddetector-resource-entity-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [event-type](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [label](#list_frauddetector-resource-label) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [list](#list_frauddetector-resource-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model](#list_frauddetector-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [outcome](#list_frauddetector-resource-outcome) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rule](#list_frauddetector-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutDetector](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutDetector.html)  **
  - **Description:** Grants permission to create or update a detector
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [PutEntityType](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutEntityType.html)  **
  - **Description:** Grants permission to create or update an entity type. An entity represents who is performing the event. As part of a fraud prediction, you pass the entity ID to indicate the specific entity who performed the event. An entity type classifies the entity. Example classifications include customer, merchant, or account
  - **Resource types (\*required):** [entity-type\*](#list_frauddetector-resource-entity-type)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [PutEventType](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutEventType.html)  **
  - **Description:** Grants permission to create or update an event type. An event is a business activity that is evaluated for fraud risk. With Amazon Fraud Detector, you generate fraud predictions for events. An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the variables sent as part of the event, the entity performing the event (such as a customer), and the labels that classify the event. Example event types include online payment transactions, account registrations, and authentications
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [PutExternalModel](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutExternalModel.html)  **
  - **Description:** Grants permission to create or update an Amazon SageMaker model endpoint. You can also use this action to update the configuration of the model endpoint, including the IAM role and/or the mapped variables
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [external-model\*](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [PutKMSEncryptionKey](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutKMSEncryptionKey.html)  **
  - **Description:** Grants permission to specify the Key Management Service (KMS) customer master key (CMK) to be used to encrypt content in Amazon Fraud Detector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutLabel.html)  **
  - **Description:** Grants permission to create or update label. A label classifies an event as fraudulent or legitimate. Labels are associated with event types and used to train supervised machine learning models in Amazon Fraud Detector
  - **Resource types (\*required):** [label\*](#list_frauddetector-resource-label)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [PutOutcome](https://docs.aws.amazon.com/frauddetector/latest/api/API_PutOutcome.html)  **
  - **Description:** Grants permission to create or update an outcome
  - **Resource types (\*required):** [outcome\*](#list_frauddetector-resource-outcome)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [SendEvent](https://docs.aws.amazon.com/frauddetector/latest/api/API_SendEvent.html)  **
  - **Description:** Grants permission to send event
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/frauddetector/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to assign tags to a resource
  - **Resource types (\*required):** [batch-import](#list_frauddetector-resource-batch-import) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [batch-prediction](#list_frauddetector-resource-batch-prediction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector](#list_frauddetector-resource-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector-version](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [entity-type](#list_frauddetector-resource-entity-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [event-type](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [label](#list_frauddetector-resource-label) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [list](#list_frauddetector-resource-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model](#list_frauddetector-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [outcome](#list_frauddetector-resource-outcome) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_frauddetector-resource-rule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/frauddetector/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [batch-import](#list_frauddetector-resource-batch-import) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [batch-prediction](#list_frauddetector-resource-batch-prediction) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [detector-version](#list_frauddetector-resource-detector-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [entity-type](#list_frauddetector-resource-entity-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [event-type](#list_frauddetector-resource-event-type) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [label](#list_frauddetector-resource-label) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [list](#list_frauddetector-resource-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model](#list_frauddetector-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [outcome](#list_frauddetector-resource-outcome) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [rule](#list_frauddetector-resource-rule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Resource types (\*required):** [variable](#list_frauddetector-resource-variable) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDetectorVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateDetectorVersion.html)  **
  - **Description:** Grants permission to update a detector version. The detector version attributes that you can update include models, external model endpoints, rules, rule execution mode, and description. You can only update a DRAFT detector version
  - **Resource types (\*required):** [detector\*](#list_frauddetector-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [external-model](#list_frauddetector-resource-external-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_frauddetector-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDetectorVersionMetadata](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateDetectorVersionMetadata.html)  **
  - **Description:** Grants permission to update the detector version's description. You can update the metadata for any detector version (DRAFT, ACTIVE, or INACTIVE)
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDetectorVersionStatus](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateDetectorVersionStatus.html)  **
  - **Description:** Grants permission to update the detector version's status. You can perform the following promotions or demotions using UpdateDetectorVersionStatus: DRAFT to ACTIVE, ACTIVE to INACTIVE, and INACTIVE to ACTIVE
  - **Resource types (\*required):** [detector-version\*](#list_frauddetector-resource-detector-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEventLabel](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateEventLabel.html)  **
  - **Description:** Grants permission to update an existing event record's label value
  - **Resource types (\*required):** [event-type\*](#list_frauddetector-resource-event-type)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateList.html)  **
  - **Description:** Grants permission to update a list
  - **Resource types (\*required):** [list\*](#list_frauddetector-resource-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModel](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateModel.html)  **
  - **Description:** Grants permission to update a model. You can update the description attribute using this action
  - **Resource types (\*required):** [model\*](#list_frauddetector-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModelVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateModelVersion.html)  **
  - **Description:** Grants permission to update a model version. Updating a model version retrains an existing model version using updated training data and produces a new minor version of the model. You can update the training data set location and data access role attributes using this action. This action creates and trains a new minor version of the model, for example version 1.01, 1.02, 1.03
  - **Resource types (\*required):** [model\*](#list_frauddetector-resource-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateModelVersionStatus](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateModelVersionStatus.html)  **
  - **Description:** Grants permission to update the status of a model version
  - **Resource types (\*required):** [model-version\*](#list_frauddetector-resource-model-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleMetadata](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateRuleMetadata.html)  **
  - **Description:** Grants permission to update a rule's metadata. The description attribute can be updated
  - **Resource types (\*required):** [rule\*](#list_frauddetector-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRuleVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateRuleVersion.html)  **
  - **Description:** Grants permission to update a rule version resulting in a new rule version. Updates a rule version resulting in a new rule version (version 1, 2, 3 ...)
  - **Resource types (\*required):** [rule\*](#list_frauddetector-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_frauddetector-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_frauddetector-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateVariable](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateVariable.html)  **
  - **Description:** Grants permission to update a variable
  - **Resource types (\*required):** [variable\*](#list_frauddetector-resource-variable)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Fraud Detector
<a name="list_frauddetector-permission-only-actions"></a>

The following actions are defined by Amazon Fraud Detector but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [GetBatchImportJobValidationReport](https://docs.aws.amazon.com/frauddetector/latest/ug/prepare-storage-event-data.html#smart-data-validation)  **
  - **Description:** Grants permission to get the data validation report of a specific batch import job
  - **Resource types (\*required):** [batch-import\*](#list_frauddetector-resource-batch-import)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon Fraud Detector
<a name="list_frauddetector-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [batch-import](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:batch-import/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [batch-prediction](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:batch-prediction/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [detector](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:detector/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [detector-version](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:detector-version/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [entity-type](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:entity-type/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [event-type](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:event-type/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [external-model](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:external-model/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [label](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:label/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [list](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:list/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [model](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:model/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [model-version](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:model-version/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [outcome](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:outcome/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [rule](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:rule/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 
|  [variable](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonfrauddetector.html#amazonfrauddetector-resources-for-iam-policies)  | arn:${Partition}:frauddetector:${Region}:${Account}:variable/${ResourcePath} | [aws:ResourceTag/${TagKey}](#list_frauddetector-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Fraud Detector
<a name="list_frauddetector-policy-keys"></a>

Amazon Fraud Detector defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the tag keys that are passed in the request | ArrayOfString | 