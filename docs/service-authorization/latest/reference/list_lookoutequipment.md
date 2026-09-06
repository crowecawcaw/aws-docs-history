

# Actions, resources, and condition keys for Amazon Lookout for Equipment
<a name="list_lookoutequipment"></a>

Amazon Lookout for Equipment (service prefix: `lookoutequipment`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lookoutequipment/lookoutequipment.json) for this service.

**Topics**
+ [API operations defined by Amazon Lookout for Equipment](#list_lookoutequipment-operations)
+ [Actions defined by Amazon Lookout for Equipment](#list_lookoutequipment-actions-as-permissions)
+ [Resource types defined by Amazon Lookout for Equipment](#list_lookoutequipment-resources-for-iam-policies)
+ [Condition keys for Amazon Lookout for Equipment](#list_lookoutequipment-policy-keys)

## API operations defined by Amazon Lookout for Equipment
<a name="list_lookoutequipment-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_lookoutequipment-actions-as-permissions).




- **   CreateDataset  **
  - **IAM action:**  [lookoutequipment:CreateDataset](#list_lookoutequipment-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:CreateInferenceScheduler](#list_lookoutequipment-action-CreateInferenceScheduler)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   CreateLabel  **
  - **IAM action:**  [lookoutequipment:CreateLabel](#list_lookoutequipment-action-CreateLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLabelGroup  **
  - **IAM action:**  [lookoutequipment:CreateLabelGroup](#list_lookoutequipment-action-CreateLabelGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateModel  **
  - **IAM action:**  [lookoutequipment:CreateModel](#list_lookoutequipment-action-CreateModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   CreateRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:CreateRetrainingScheduler](#list_lookoutequipment-action-CreateRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **IAM action:**  [lookoutequipment:DeleteDataset](#list_lookoutequipment-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:DeleteInferenceScheduler](#list_lookoutequipment-action-DeleteInferenceScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLabel  **
  - **IAM action:**  [lookoutequipment:DeleteLabel](#list_lookoutequipment-action-DeleteLabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLabelGroup  **
  - **IAM action:**  [lookoutequipment:DeleteLabelGroup](#list_lookoutequipment-action-DeleteLabelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModel  **
  - **IAM action:**  [lookoutequipment:DeleteModel](#list_lookoutequipment-action-DeleteModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [lookoutequipment:DeleteResourcePolicy](#list_lookoutequipment-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:DeleteRetrainingScheduler](#list_lookoutequipment-action-DeleteRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataIngestionJob  **
  - **IAM action:**  [lookoutequipment:DescribeDataIngestionJob](#list_lookoutequipment-action-DescribeDataIngestionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataset  **
  - **IAM action:**  [lookoutequipment:DescribeDataset](#list_lookoutequipment-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:DescribeInferenceScheduler](#list_lookoutequipment-action-DescribeInferenceScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLabel  **
  - **IAM action:**  [lookoutequipment:Describelabel](#list_lookoutequipment-action-Describelabel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLabelGroup  **
  - **IAM action:**  [lookoutequipment:DescribeLabelGroup](#list_lookoutequipment-action-DescribeLabelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModel  **
  - **IAM action:**  [lookoutequipment:DescribeModel](#list_lookoutequipment-action-DescribeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelVersion  **
  - **IAM action:**  [lookoutequipment:DescribeModelVersion](#list_lookoutequipment-action-DescribeModelVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **IAM action:**  [lookoutequipment:DescribeResourcePolicy](#list_lookoutequipment-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:DescribeRetrainingScheduler](#list_lookoutequipment-action-DescribeRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportDataset  **
  - **IAM action:**  [lookoutequipment:ImportDataset](#list_lookoutequipment-action-ImportDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ImportModelVersion  **
  - **IAM action:**  [lookoutequipment:ImportModelVersion](#list_lookoutequipment-action-ImportModelVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   ListDataIngestionJobs  **
  - **IAM action:**  [lookoutequipment:ListDataIngestionJobs](#list_lookoutequipment-action-ListDataIngestionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDatasets  **
  - **IAM action:**  [lookoutequipment:ListDatasets](#list_lookoutequipment-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceEvents  **
  - **IAM action:**  [lookoutequipment:ListInferenceEvents](#list_lookoutequipment-action-ListInferenceEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInferenceExecutions  **
  - **IAM action:**  [lookoutequipment:ListInferenceExecutions](#list_lookoutequipment-action-ListInferenceExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInferenceSchedulers  **
  - **IAM action:**  [lookoutequipment:ListInferenceSchedulers](#list_lookoutequipment-action-ListInferenceSchedulers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLabelGroups  **
  - **IAM action:**  [lookoutequipment:ListLabelGroups](#list_lookoutequipment-action-ListLabelGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLabels  **
  - **IAM action:**  [lookoutequipment:ListLabels](#list_lookoutequipment-action-ListLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelVersions  **
  - **IAM action:**  [lookoutequipment:ListModelVersions](#list_lookoutequipment-action-ListModelVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModels  **
  - **IAM action:**  [lookoutequipment:ListModels](#list_lookoutequipment-action-ListModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRetrainingSchedulers  **
  - **IAM action:**  [lookoutequipment:ListRetrainingSchedulers](#list_lookoutequipment-action-ListRetrainingSchedulers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSensorStatistics  **
  - **IAM action:**  [lookoutequipment:ListSensorStatistics](#list_lookoutequipment-action-ListSensorStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [lookoutequipment:ListTagsForResource](#list_lookoutequipment-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [lookoutequipment:PutResourcePolicy](#list_lookoutequipment-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDataIngestionJob  **
  - **IAM action:**  [lookoutequipment:StartDataIngestionJob](#list_lookoutequipment-action-StartDataIngestionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   StartInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:StartInferenceScheduler](#list_lookoutequipment-action-StartInferenceScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:StartRetrainingScheduler](#list_lookoutequipment-action-StartRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:StopInferenceScheduler](#list_lookoutequipment-action-StopInferenceScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:StopRetrainingScheduler](#list_lookoutequipment-action-StopRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [lookoutequipment:TagResource](#list_lookoutequipment-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [lookoutequipment:UntagResource](#list_lookoutequipment-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateActiveModelVersion  **
  - **IAM action:**  [lookoutequipment:UpdateActiveModelVersion](#list_lookoutequipment-action-UpdateActiveModelVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInferenceScheduler  **
  - **IAM action:**  [lookoutequipment:UpdateInferenceScheduler](#list_lookoutequipment-action-UpdateInferenceScheduler)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   UpdateLabelGroup  **
  - **IAM action:**  [lookoutequipment:UpdateLabelGroup](#list_lookoutequipment-action-UpdateLabelGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModel  **
  - **IAM action:**  [lookoutequipment:UpdateModel](#list_lookoutequipment-action-UpdateModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** lookoutequipment.amazonaws.com / **Access level:** Write

- **   UpdateRetrainingScheduler  **
  - **IAM action:**  [lookoutequipment:UpdateRetrainingScheduler](#list_lookoutequipment-action-UpdateRetrainingScheduler) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Lookout for Equipment
<a name="list_lookoutequipment-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateInferenceScheduler.html)  **
  - **Description:** Grants permission to create an inference scheduler for a trained model
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateLabel.html)  **
  - **Description:** Grants permission to create a label
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateLabelGroup.html)  **
  - **Description:** Grants permission to create a label group
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Write

- **   [CreateModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateModel.html)  **
  - **Description:** Grants permission to create a model that is trained on a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [label-group](#list_lookoutequipment-resource-label-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_CreateRetrainingScheduler.html)  **
  - **Description:** Grants permission to create a retraining scheduler for a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteInferenceScheduler.html)  **
  - **Description:** Grants permission to delete an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteLabel.html)  **
  - **Description:** Grants permission to delete a label
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteLabelGroup.html)  **
  - **Description:** Grants permission to delete a label group
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteModel.html)  **
  - **Description:** Grants permission to delete a model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a resource policy
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DeleteRetrainingScheduler.html)  **
  - **Description:** Grants permission to delete a retraining scheduler of a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDataIngestionJob](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeDataIngestionJob.html)  **
  - **Description:** Grants permission to describe a data ingestion job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeDataset.html)  **
  - **Description:** Grants permission to describe a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeInferenceScheduler.html)  **
  - **Description:** Grants permission to describe an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeLabelGroup.html)  **
  - **Description:** Grants permission to describe a label group
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeModel.html)  **
  - **Description:** Grants permission to describe a model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeModelVersion.html)  **
  - **Description:** Grants permission to describe a model version
  - **Resource types (\*required):** [model-version\*](#list_lookoutequipment-resource-model-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to describe a resource policy
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeRetrainingScheduler.html)  **
  - **Description:** Grants permission to describe a retraining scheduler of a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [Describelabel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_DescribeLabel.html)  **
  - **Description:** Grants permission to describe a label
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportDataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ImportDataset.html)  **
  - **Description:** Grants permission to import a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Write

- **   [ImportModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ImportModelVersion.html)  **
  - **Description:** Grants permission to import a model version
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)<br />[lookoutequipment:IsImportingData](#list_lookoutequipment-lookoutequipment_IsImportingData)
  - **Resource types (\*required):** [label-group](#list_lookoutequipment-resource-label-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)<br />[lookoutequipment:IsImportingData](#list_lookoutequipment-lookoutequipment_IsImportingData)
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)<br />[lookoutequipment:IsImportingData](#list_lookoutequipment-lookoutequipment_IsImportingData)
  - **Access level:** Write

- **   [ListDataIngestionJobs](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListDataIngestionJobs.html)  **
  - **Description:** Grants permission to list the data ingestion jobs in your account or for a particular dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDatasets](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListDatasets.html)  **
  - **Description:** Grants permission to list the datasets in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceEvents](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceEvents.html)  **
  - **Description:** Grants permission to list the inference events for an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInferenceExecutions](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceExecutions.html)  **
  - **Description:** Grants permission to list the inference executions for an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInferenceSchedulers](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListInferenceSchedulers.html)  **
  - **Description:** Grants permission to list the inference schedulers in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLabelGroups](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListLabelGroups.html)  **
  - **Description:** Grants permission to list the label groups in your account
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLabels](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListLabels.html)  **
  - **Description:** Grants permission to list the labels in your account
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModelVersions](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListModelVersions.html)  **
  - **Description:** Grants permission to list the model versions in your account
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListModels.html)  **
  - **Description:** Grants permission to list the models in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRetrainingSchedulers](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListRetrainingSchedulers.html)  **
  - **Description:** Grants permission to list the retraining schedulers in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSensorStatistics](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListSensorStatistics.html)  **
  - **Description:** Grants permission to list the sensor statistics for a particular dataset or an ingestion job
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-scheduler](#list_lookoutequipment-resource-inference-scheduler) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [label-group](#list_lookoutequipment-resource-label-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put a resource policy
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDataIngestionJob](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartDataIngestionJob.html)  **
  - **Description:** Grants permission to start a data ingestion job for a dataset
  - **Resource types (\*required):** [dataset\*](#list_lookoutequipment-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartInferenceScheduler.html)  **
  - **Description:** Grants permission to start an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StartRetrainingScheduler.html)  **
  - **Description:** Grants permission to start a retraining scheduler of a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StopInferenceScheduler.html)  **
  - **Description:** Grants permission to stop an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_StopRetrainingScheduler.html)  **
  - **Description:** Grants permission to stop a retraining scheduler of a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [inference-scheduler](#list_lookoutequipment-resource-inference-scheduler) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [label-group](#list_lookoutequipment-resource-label-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_lookoutequipment-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [dataset](#list_lookoutequipment-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [inference-scheduler](#list_lookoutequipment-resource-inference-scheduler) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [label-group](#list_lookoutequipment-resource-label-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Resource types (\*required):** [model-version](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_lookoutequipment-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateActiveModelVersion](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateActiveModelVersion.html)  **
  - **Description:** Grants permission to set the active model version for a given machine learning model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-version\*](#list_lookoutequipment-resource-model-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInferenceScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateInferenceScheduler.html)  **
  - **Description:** Grants permission to update an inference scheduler
  - **Resource types (\*required):** [inference-scheduler\*](#list_lookoutequipment-resource-inference-scheduler)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLabelGroup](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateLabelGroup.html)  **
  - **Description:** Grants permission to update a label group
  - **Resource types (\*required):** [label-group\*](#list_lookoutequipment-resource-label-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModel](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateModel.html)  **
  - **Description:** Grants permission to update a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRetrainingScheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_UpdateRetrainingScheduler.html)  **
  - **Description:** Grants permission to update a retraining scheduler of a trained model
  - **Resource types (\*required):** [model\*](#list_lookoutequipment-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Lookout for Equipment
<a name="list_lookoutequipment-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dataset](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/dataset.html)  | arn:${Partition}:lookoutequipment:${Region}:${Account}:dataset/${DatasetName}/${DatasetId} | [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_) | 
|  [inference-scheduler](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/inference-scheduler.html)  | arn:${Partition}:lookoutequipment:${Region}:${Account}:inference-scheduler/${InferenceSchedulerName}/${InferenceSchedulerId} | [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_) | 
|  [label-group](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/label-group.html)  | arn:${Partition}:lookoutequipment:${Region}:${Account}:label-group/${LabelGroupName}/${LabelGroupId} | [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_) | 
|  [model](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model.html)  | arn:${Partition}:lookoutequipment:${Region}:${Account}:model/${ModelName}/${ModelId} | [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_) | 
|  [model-version](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/model-version.html)  | arn:${Partition}:lookoutequipment:${Region}:${Account}:model/${ModelName}/${ModelId}/model-version/${ModelVersionNumber} | [aws:ResourceTag/${TagKey}](#list_lookoutequipment-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Lookout for Equipment
<a name="list_lookoutequipment-policy-keys"></a>

Amazon Lookout for Equipment defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [lookoutequipment:IsImportingData](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-isimportingdata)  | Filters access by the import strategy of underlying data | Bool | 