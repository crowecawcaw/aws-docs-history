

# Actions, resources, and condition keys for AWS Clean Rooms ML
<a name="list_cleanroomsml"></a>

AWS Clean Rooms ML (service prefix: `cleanrooms-ml`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/clean-rooms/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/clean-rooms/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cleanrooms-ml/cleanrooms-ml.json) for this service.

**Topics**
+ [API operations defined by AWS Clean Rooms ML](#list_cleanroomsml-operations)
+ [Actions defined by AWS Clean Rooms ML](#list_cleanroomsml-actions-as-permissions)
+ [Resource types defined by AWS Clean Rooms ML](#list_cleanroomsml-resources-for-iam-policies)
+ [Condition keys for AWS Clean Rooms ML](#list_cleanroomsml-policy-keys)

## API operations defined by AWS Clean Rooms ML
<a name="list_cleanroomsml-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cleanroomsml-actions-as-permissions).




- **   CancelTrainedModel  **
  - **IAM action:**  [cleanrooms-ml:CancelTrainedModel](#list_cleanroomsml-action-CancelTrainedModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelTrainedModelInferenceJob  **
  - **IAM action:**  [cleanrooms-ml:CancelTrainedModelInferenceJob](#list_cleanroomsml-action-CancelTrainedModelInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:CreateAudienceModel](#list_cleanroomsml-action-CreateAudienceModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfiguredAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:CreateConfiguredAudienceModel](#list_cleanroomsml-action-CreateConfiguredAudienceModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   CreateConfiguredModelAlgorithm  **
  - **IAM action:**  [cleanrooms-ml:CreateConfiguredModelAlgorithm](#list_cleanroomsml-action-CreateConfiguredModelAlgorithm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   CreateConfiguredModelAlgorithmAssociation  **
  - **IAM action:**  [cleanrooms-ml:CreateConfiguredModelAlgorithmAssociation](#list_cleanroomsml-action-CreateConfiguredModelAlgorithmAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMLInputChannel  **
  - **IAM action:**  [cleanrooms-ml:CreateMLInputChannel](#list_cleanroomsml-action-CreateMLInputChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   CreateTrainedModel  **
  - **IAM action:**  [cleanrooms-ml:CreateTrainedModel](#list_cleanroomsml-action-CreateTrainedModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTrainingDataset  **
  - **IAM action:**  [cleanrooms-ml:CreateTrainingDataset](#list_cleanroomsml-action-CreateTrainingDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   DeleteAudienceGenerationJob  **
  - **IAM action:**  [cleanrooms-ml:DeleteAudienceGenerationJob](#list_cleanroomsml-action-DeleteAudienceGenerationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:DeleteAudienceModel](#list_cleanroomsml-action-DeleteAudienceModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:DeleteConfiguredAudienceModel](#list_cleanroomsml-action-DeleteConfiguredAudienceModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredAudienceModelPolicy  **
  - **IAM action:**  [cleanrooms-ml:DeleteConfiguredAudienceModelPolicy](#list_cleanroomsml-action-DeleteConfiguredAudienceModelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredModelAlgorithm  **
  - **IAM action:**  [cleanrooms-ml:DeleteConfiguredModelAlgorithm](#list_cleanroomsml-action-DeleteConfiguredModelAlgorithm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguredModelAlgorithmAssociation  **
  - **IAM action:**  [cleanrooms-ml:DeleteConfiguredModelAlgorithmAssociation](#list_cleanroomsml-action-DeleteConfiguredModelAlgorithmAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMLConfiguration  **
  - **IAM action:**  [cleanrooms-ml:DeleteMLConfiguration](#list_cleanroomsml-action-DeleteMLConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMLInputChannelData  **
  - **IAM action:**  [cleanrooms-ml:DeleteMLInputChannelData](#list_cleanroomsml-action-DeleteMLInputChannelData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrainedModelOutput  **
  - **IAM action:**  [cleanrooms-ml:DeleteTrainedModelOutput](#list_cleanroomsml-action-DeleteTrainedModelOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrainingDataset  **
  - **IAM action:**  [cleanrooms-ml:DeleteTrainingDataset](#list_cleanroomsml-action-DeleteTrainingDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAudienceGenerationJob  **
  - **IAM action:**  [cleanrooms-ml:GetAudienceGenerationJob](#list_cleanroomsml-action-GetAudienceGenerationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:GetAudienceModel](#list_cleanroomsml-action-GetAudienceModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationConfiguredModelAlgorithmAssociation  **
  - **IAM action:**  [cleanrooms-ml:GetCollaborationConfiguredModelAlgorithmAssociation](#list_cleanroomsml-action-GetCollaborationConfiguredModelAlgorithmAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationMLInputChannel  **
  - **IAM action:**  [cleanrooms-ml:GetCollaborationMLInputChannel](#list_cleanroomsml-action-GetCollaborationMLInputChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCollaborationTrainedModel  **
  - **IAM action:**  [cleanrooms-ml:GetCollaborationTrainedModel](#list_cleanroomsml-action-GetCollaborationTrainedModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:GetConfiguredAudienceModel](#list_cleanroomsml-action-GetConfiguredAudienceModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredAudienceModelPolicy  **
  - **IAM action:**  [cleanrooms-ml:GetConfiguredAudienceModelPolicy](#list_cleanroomsml-action-GetConfiguredAudienceModelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredModelAlgorithm  **
  - **IAM action:**  [cleanrooms-ml:GetConfiguredModelAlgorithm](#list_cleanroomsml-action-GetConfiguredModelAlgorithm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguredModelAlgorithmAssociation  **
  - **IAM action:**  [cleanrooms-ml:GetConfiguredModelAlgorithmAssociation](#list_cleanroomsml-action-GetConfiguredModelAlgorithmAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMLConfiguration  **
  - **IAM action:**  [cleanrooms-ml:GetMLConfiguration](#list_cleanroomsml-action-GetMLConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMLInputChannel  **
  - **IAM action:**  [cleanrooms-ml:GetMLInputChannel](#list_cleanroomsml-action-GetMLInputChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrainedModel  **
  - **IAM action:**  [cleanrooms-ml:GetTrainedModel](#list_cleanroomsml-action-GetTrainedModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrainedModelInferenceJob  **
  - **IAM action:**  [cleanrooms-ml:GetTrainedModelInferenceJob](#list_cleanroomsml-action-GetTrainedModelInferenceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrainingDataset  **
  - **IAM action:**  [cleanrooms-ml:GetTrainingDataset](#list_cleanroomsml-action-GetTrainingDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAudienceExportJobs  **
  - **IAM action:**  [cleanrooms-ml:ListAudienceExportJobs](#list_cleanroomsml-action-ListAudienceExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAudienceGenerationJobs  **
  - **IAM action:**  [cleanrooms-ml:ListAudienceGenerationJobs](#list_cleanroomsml-action-ListAudienceGenerationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAudienceModels  **
  - **IAM action:**  [cleanrooms-ml:ListAudienceModels](#list_cleanroomsml-action-ListAudienceModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationConfiguredModelAlgorithmAssociations  **
  - **IAM action:**  [cleanrooms-ml:ListCollaborationConfiguredModelAlgorithmAssociations](#list_cleanroomsml-action-ListCollaborationConfiguredModelAlgorithmAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationMLInputChannels  **
  - **IAM action:**  [cleanrooms-ml:ListCollaborationMLInputChannels](#list_cleanroomsml-action-ListCollaborationMLInputChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationTrainedModelExportJobs  **
  - **IAM action:**  [cleanrooms-ml:ListCollaborationTrainedModelExportJobs](#list_cleanroomsml-action-ListCollaborationTrainedModelExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationTrainedModelInferenceJobs  **
  - **IAM action:**  [cleanrooms-ml:ListCollaborationTrainedModelInferenceJobs](#list_cleanroomsml-action-ListCollaborationTrainedModelInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCollaborationTrainedModels  **
  - **IAM action:**  [cleanrooms-ml:ListCollaborationTrainedModels](#list_cleanroomsml-action-ListCollaborationTrainedModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredAudienceModels  **
  - **IAM action:**  [cleanrooms-ml:ListConfiguredAudienceModels](#list_cleanroomsml-action-ListConfiguredAudienceModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredModelAlgorithmAssociations  **
  - **IAM action:**  [cleanrooms-ml:ListConfiguredModelAlgorithmAssociations](#list_cleanroomsml-action-ListConfiguredModelAlgorithmAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfiguredModelAlgorithms  **
  - **IAM action:**  [cleanrooms-ml:ListConfiguredModelAlgorithms](#list_cleanroomsml-action-ListConfiguredModelAlgorithms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMLInputChannels  **
  - **IAM action:**  [cleanrooms-ml:ListMLInputChannels](#list_cleanroomsml-action-ListMLInputChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cleanrooms-ml:ListTagsForResource](#list_cleanroomsml-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainedModelInferenceJobs  **
  - **IAM action:**  [cleanrooms-ml:ListTrainedModelInferenceJobs](#list_cleanroomsml-action-ListTrainedModelInferenceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainedModelVersions  **
  - **IAM action:**  [cleanrooms-ml:ListTrainedModelVersions](#list_cleanroomsml-action-ListTrainedModelVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainedModels  **
  - **IAM action:**  [cleanrooms-ml:ListTrainedModels](#list_cleanroomsml-action-ListTrainedModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainingDatasets  **
  - **IAM action:**  [cleanrooms-ml:ListTrainingDatasets](#list_cleanroomsml-action-ListTrainingDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutConfiguredAudienceModelPolicy  **
  - **IAM action:**  [cleanrooms-ml:PutConfiguredAudienceModelPolicy](#list_cleanroomsml-action-PutConfiguredAudienceModelPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutMLConfiguration  **
  - **IAM action:**  [cleanrooms-ml:PutMLConfiguration](#list_cleanroomsml-action-PutMLConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   StartAudienceExportJob  **
  - **IAM action:**  [cleanrooms-ml:StartAudienceExportJob](#list_cleanroomsml-action-StartAudienceExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAudienceGenerationJob  **
  - **IAM action:**  [cleanrooms-ml:StartAudienceGenerationJob](#list_cleanroomsml-action-StartAudienceGenerationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write

- **   StartTrainedModelExportJob  **
  - **IAM action:**  [cleanrooms-ml:StartTrainedModelExportJob](#list_cleanroomsml-action-StartTrainedModelExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTrainedModelInferenceJob  **
  - **IAM action:**  [cleanrooms-ml:StartTrainedModelInferenceJob](#list_cleanroomsml-action-StartTrainedModelInferenceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [cleanrooms-ml:TagResource](#list_cleanroomsml-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cleanrooms-ml:UnTagResource](#list_cleanroomsml-action-UnTagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateConfiguredAudienceModel  **
  - **IAM action:**  [cleanrooms-ml:UpdateConfiguredAudienceModel](#list_cleanroomsml-action-UpdateConfiguredAudienceModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cleanrooms-ml.amazonaws.com / **Access level:** Write



## Actions defined by AWS Clean Rooms ML
<a name="list_cleanroomsml-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelTrainedModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CancelTrainedModel.html)  **
  - **Description:** Grants permission to cancel a trained model
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CancelTrainedModelInferenceJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CancelTrainedModelInferenceJob.html)  **
  - **Description:** Grants permission to cancel a trained model inference job
  - **Resource types (\*required):** [TrainedModelInferenceJob\*](#list_cleanroomsml-resource-TrainedModelInferenceJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateAudienceModel.html)  **
  - **Description:** Grants permission to create an audience model
  - **Resource types (\*required):** [trainingdataset\*](#list_cleanroomsml-resource-trainingdataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateConfiguredAudienceModel.html)  **
  - **Description:** Grants permission to create a configured audience model
  - **Resource types (\*required):** [audiencemodel\*](#list_cleanroomsml-resource-audiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredModelAlgorithm](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateConfiguredModelAlgorithm.html)  **
  - **Description:** Grants permission to create a configured model algorithm
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguredModelAlgorithmAssociation](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateConfiguredModelAlgorithmAssociation.html)  **
  - **Description:** Grants permission to create a configured model algorithm association
  - **Resource types (\*required):** [ConfiguredModelAlgorithm\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMLInputChannel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateMLInputChannel.html)  **
  - **Description:** Grants permission to create an ML input channel
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrainedModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainedModel.html)  **
  - **Description:** Grants permission to create a trained model
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrainingDataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.html)  **
  - **Description:** Grants permission to create a training dataset, or seed audience. In Clean Rooms ML, the TrainingDataset is metadata that points to a Glue table, which is read only during AudienceModel creation
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAudienceGenerationJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteAudienceGenerationJob.html)  **
  - **Description:** Grants permission to delete the specified audience generation job, and removes all data associated with the job
  - **Resource types (\*required):** [audiencegenerationjob\*](#list_cleanroomsml-resource-audiencegenerationjob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteAudienceModel.html)  **
  - **Description:** Grants permission to delete the specified audience generation job, and removes all data associated with the job
  - **Resource types (\*required):** [audiencemodel\*](#list_cleanroomsml-resource-audiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfiguredAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteConfiguredAudienceModel.html)  **
  - **Description:** Grants permission to delete the specified configured audience model
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfiguredAudienceModelPolicy](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteConfiguredAudienceModelPolicy.html)  **
  - **Description:** Grants permission to delete the specified configured audience model policy
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfiguredModelAlgorithm](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteConfiguredModelAlgorithm.html)  **
  - **Description:** Grants permission to delete a configured model algorithm
  - **Resource types (\*required):** [ConfiguredModelAlgorithm\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteConfiguredModelAlgorithmAssociation](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteConfiguredModelAlgorithmAssociation.html)  **
  - **Description:** Grants permission to delete a configured model algorithm association
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMLConfiguration](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteMLConfiguration.html)  **
  - **Description:** Grants permission to delete an ML configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMLInputChannelData](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteMLInputChannelData.html)  **
  - **Description:** Grants permission to delete all data associated with the ML input channel
  - **Resource types (\*required):** [MLInputChannel\*](#list_cleanroomsml-resource-MLInputChannel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteTrainedModelOutput](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteTrainedModelOutput.html)  **
  - **Description:** Grants permission to delete all output associated with the trained model
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteTrainingDataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_DeleteTrainingDataset.html)  **
  - **Description:** Grants permission to delete a training dataset
  - **Resource types (\*required):** [trainingdataset\*](#list_cleanroomsml-resource-trainingdataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [GetAudienceGenerationJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetAudienceGenerationJob.html)  **
  - **Description:** Grants permission to return information about an audience generation job
  - **Resource types (\*required):** [audiencegenerationjob\*](#list_cleanroomsml-resource-audiencegenerationjob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetAudienceModel.html)  **
  - **Description:** Grants permission to return information about an audience model
  - **Resource types (\*required):** [audiencemodel\*](#list_cleanroomsml-resource-audiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetCollaborationConfiguredModelAlgorithmAssociation](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationConfiguredModelAlgorithmAssociation.html)  **
  - **Description:** Grants permission to return information about a configured model algorithm association created by any member in the collaboration
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** Read

- **   [GetCollaborationMLInputChannel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationMLInputChannel.html)  **
  - **Description:** Grants permission to return information about an ML input channel created by any member in the collaboration
  - **Resource types (\*required):** [MLInputChannel\*](#list_cleanroomsml-resource-MLInputChannel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** Read

- **   [GetCollaborationTrainedModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationTrainedModel.html)  **
  - **Description:** Grants permission to return information about a trained model created by any member in the collaboration
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** Read

- **   [GetConfiguredAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredAudienceModel.html)  **
  - **Description:** Grants permission to return information about a configured audience model
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetConfiguredAudienceModelPolicy](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredAudienceModelPolicy.html)  **
  - **Description:** Grants permission to return information about a configured audience model policy
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetConfiguredModelAlgorithm](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredModelAlgorithm.html)  **
  - **Description:** Grants permission to return information about a configured model algorithm
  - **Resource types (\*required):** [ConfiguredModelAlgorithm\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetConfiguredModelAlgorithmAssociation](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredModelAlgorithmAssociation.html)  **
  - **Description:** Grants permission to return information about a configured model algorithm association
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetMLConfiguration](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetMLConfiguration.html)  **
  - **Description:** Grants permission to return information about an ML configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetMLInputChannel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetMLInputChannel.html)  **
  - **Description:** Grants permission to return information about an ML input channel
  - **Resource types (\*required):** [MLInputChannel\*](#list_cleanroomsml-resource-MLInputChannel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetTrainedModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetTrainedModel.html)  **
  - **Description:** Grants permission to return information about a trained model
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetTrainedModelInferenceJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetTrainedModelInferenceJob.html)  **
  - **Description:** Grants permission to return information about a trained model inference job
  - **Resource types (\*required):** [TrainedModelInferenceJob\*](#list_cleanroomsml-resource-TrainedModelInferenceJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [GetTrainingDataset](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetTrainingDataset.html)  **
  - **Description:** Grants permission to return information about a training dataset
  - **Resource types (\*required):** [trainingdataset\*](#list_cleanroomsml-resource-trainingdataset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Read

- **   [ListAudienceExportJobs](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceExportJobs.html)  **
  - **Description:** Grants permission to return a list of the audience export jobs
  - **Resource types (\*required):** [audiencegenerationjob](#list_cleanroomsml-resource-audiencegenerationjob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListAudienceGenerationJobs](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceGenerationJobs.html)  **
  - **Description:** Grants permission to return a list of audience generation jobs
  - **Resource types (\*required):** [configuredaudiencemodel](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListAudienceModels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceModels.html)  **
  - **Description:** Grants permission to return a list of audience models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCollaborationConfiguredModelAlgorithmAssociations](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationConfiguredModelAlgorithmAssociations.html)  **
  - **Description:** Grants permission to return a list of configured model algorithms created by any member in the collaboration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** List

- **   [ListCollaborationMLInputChannels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationMLInputChannels.html)  **
  - **Description:** Grants permission to return a list of ML input channels created by any member in the collaboration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** List

- **   [ListCollaborationTrainedModelExportJobs](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationTrainedModelExportJobs.html)  **
  - **Description:** Grants permission to return a list of trained model export jobs started by any member in the collaboration
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** List

- **   [ListCollaborationTrainedModelInferenceJobs](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationTrainedModelInferenceJobs.html)  **
  - **Description:** Grants permission to return a list of trained model inference jobs started by any member in the collaboration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** List

- **   [ListCollaborationTrainedModels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationTrainedModels.html)  **
  - **Description:** Grants permission to return a list of trained models created by any member in the collaboration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** List

- **   [ListConfiguredAudienceModels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListConfiguredAudienceModels.html)  **
  - **Description:** Grants permission to return a list of configured audience models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfiguredModelAlgorithmAssociations](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListConfiguredModelAlgorithmAssociations.html)  **
  - **Description:** Grants permission to return a list of configured model algorithm associations
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListConfiguredModelAlgorithms](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListConfiguredModelAlgorithms.html)  **
  - **Description:** Grants permission to return a list of configured model algorithms
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListMLInputChannels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListMLInputChannels.html)  **
  - **Description:** Grants permission to return a list of ML input channels
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for a provided resource
  - **Resource types (\*required):** [audiencegenerationjob](#list_cleanroomsml-resource-audiencegenerationjob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [audiencemodel](#list_cleanroomsml-resource-audiencemodel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodel](#list_cleanroomsml-resource-configuredaudiencemodel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [trainingdataset](#list_cleanroomsml-resource-trainingdataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListTrainedModelInferenceJobs](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainedModelInferenceJobs.html)  **
  - **Description:** Grants permission to return a list of trained model inference jobs
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListTrainedModelVersions](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainedModelVersions.html)  **
  - **Description:** Grants permission to return a list of trained model versions
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListTrainedModels](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainedModels.html)  **
  - **Description:** Grants permission to return a list of trained models
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** List

- **   [ListTrainingDatasets](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListTrainingDatasets.html)  **
  - **Description:** Grants permission to return a list of training datasets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutConfiguredAudienceModelPolicy](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PutConfiguredAudienceModelPolicy.html)  **
  - **Description:** Grants permission to create or update the resource policy for a configured audience model
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutMLConfiguration](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PutMLConfiguration.html)  **
  - **Description:** Grants permission to put an ML configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [StartAudienceExportJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceExportJob.html)  **
  - **Description:** Grants permission to export an audience of a specified size after you have generated an audience
  - **Resource types (\*required):** [audiencegenerationjob\*](#list_cleanroomsml-resource-audiencegenerationjob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [StartAudienceGenerationJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartAudienceGenerationJob.html)  **
  - **Description:** Grants permission to start the audience generation job
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)<br />[cleanrooms-ml:CollaborationId](#list_cleanroomsml-cleanrooms-ml_CollaborationId)
  - **Access level:** Write

- **   [StartTrainedModelExportJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartTrainedModelExportJob.html)  **
  - **Description:** Grants permission to start a trained model export job
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [StartTrainedModelInferenceJob](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_StartTrainedModelInferenceJob.html)  **
  - **Description:** Grants permission to start a trained model inference job
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation\*](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [MLInputChannel\*](#list_cleanroomsml-resource-MLInputChannel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [TrainedModel\*](#list_cleanroomsml-resource-TrainedModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a specific resource
  - **Resource types (\*required):** [ConfiguredModelAlgorithm](#list_cleanroomsml-resource-ConfiguredModelAlgorithm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [MLInputChannel](#list_cleanroomsml-resource-MLInputChannel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [TrainedModel](#list_cleanroomsml-resource-TrainedModel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [TrainedModelInferenceJob](#list_cleanroomsml-resource-TrainedModelInferenceJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [audiencegenerationjob](#list_cleanroomsml-resource-audiencegenerationjob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [audiencemodel](#list_cleanroomsml-resource-audiencemodel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodel](#list_cleanroomsml-resource-configuredaudiencemodel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [trainingdataset](#list_cleanroomsml-resource-trainingdataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnTagResource](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a specific resource
  - **Resource types (\*required):** [ConfiguredModelAlgorithm](#list_cleanroomsml-resource-ConfiguredModelAlgorithm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [ConfiguredModelAlgorithmAssociation](#list_cleanroomsml-resource-ConfiguredModelAlgorithmAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [MLInputChannel](#list_cleanroomsml-resource-MLInputChannel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [TrainedModel](#list_cleanroomsml-resource-TrainedModel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [TrainedModelInferenceJob](#list_cleanroomsml-resource-TrainedModelInferenceJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [audiencegenerationjob](#list_cleanroomsml-resource-audiencegenerationjob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [audiencemodel](#list_cleanroomsml-resource-audiencemodel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodel](#list_cleanroomsml-resource-configuredaudiencemodel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [trainingdataset](#list_cleanroomsml-resource-trainingdataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateConfiguredAudienceModel](https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_UpdateConfiguredAudienceModel.html)  **
  - **Description:** Grants permission to update a configured audience model. 
  - **Resource types (\*required):** [audiencemodel](#list_cleanroomsml-resource-audiencemodel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Resource types (\*required):** [configuredaudiencemodel\*](#list_cleanroomsml-resource-configuredaudiencemodel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_cleanroomsml-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_cleanroomsml-aws_TagKeys)
  - **Access level:** Write



## Resource types defined by AWS Clean Rooms ML
<a name="list_cleanroomsml-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ConfiguredModelAlgorithm](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:configured-model-algorithm/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [ConfiguredModelAlgorithmAssociation](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:membership/${MembershipId}/configured-model-algorithm-association/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [MLInputChannel](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:membership/${MembershipId}/ml-input-channel/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [TrainedModel](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:membership/${MembershipId}/trained-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [TrainedModelInferenceJob](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:membership/${MembershipId}/trained-model-inference-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [audiencegenerationjob](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:audience-generation-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [audiencemodel](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:audience-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [configuredaudiencemodel](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:configured-audience-model/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 
|  [trainingdataset](${AuthZDocPage})  | arn:${Partition}:cleanrooms-ml:${Region}:${Account}:training-dataset/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_cleanroomsml-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Clean Rooms ML
<a name="list_cleanroomsml-policy-keys"></a>

AWS Clean Rooms ML defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [cleanrooms-ml:CollaborationId](https://docs.aws.amazon.com/TBD)  | Filters access by Clean rooms collaboration id | String | 