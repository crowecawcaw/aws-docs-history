

# Actions, resources, and condition keys for Amazon SageMaker
<a name="list_sagemaker"></a>

Amazon SageMaker (service prefix: `sagemaker`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sagemaker/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sagemaker/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sagemaker/sagemaker.json) for this service.

**Topics**
+ [API operations defined by Amazon SageMaker](#list_sagemaker-operations)
+ [Actions defined by Amazon SageMaker](#list_sagemaker-actions-as-permissions)
+ [Permission-only actions for Amazon SageMaker](#list_sagemaker-permission-only-actions)
+ [Resource types defined by Amazon SageMaker](#list_sagemaker-resources-for-iam-policies)
+ [Condition keys for Amazon SageMaker](#list_sagemaker-policy-keys)

## API operations defined by Amazon SageMaker
<a name="list_sagemaker-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sagemaker-actions-as-permissions).




- **   AddAssociation  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddAssociation](#list_sagemaker-action-AddAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AddTags  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AssociateTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AssociateTrialComponent](#list_sagemaker-action-AssociateTrialComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachClusterNodeVolume  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AttachClusterNodeVolume](#list_sagemaker-action-AttachClusterNodeVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAddClusterNodes  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchAddClusterNodes](#list_sagemaker-action-BatchAddClusterNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteClusterNodes  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchDeleteClusterNodes](#list_sagemaker-action-BatchDeleteClusterNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDescribeModelPackage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchDescribeModelPackage](#list_sagemaker-action-BatchDescribeModelPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchRebootClusterNodes  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchRebootClusterNodes](#list_sagemaker-action-BatchRebootClusterNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchReplaceClusterNodes  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchReplaceClusterNodes](#list_sagemaker-action-BatchReplaceClusterNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAIBenchmarkJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAIBenchmarkJob](#list_sagemaker-action-CreateAIBenchmarkJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateAIRecommendationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAIRecommendationJob](#list_sagemaker-action-CreateAIRecommendationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateAIWorkloadConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAIWorkloadConfig](#list_sagemaker-action-CreateAIWorkloadConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAction  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAction](#list_sagemaker-action-CreateAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAlgorithm  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAlgorithm](#list_sagemaker-action-CreateAlgorithm)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateApp](#list_sagemaker-action-CreateApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAppImageConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAppImageConfig](#list_sagemaker-action-CreateAppImageConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateArtifact  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateArtifact](#list_sagemaker-action-CreateArtifact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateAutoMLJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAutoMLJob](#list_sagemaker-action-CreateAutoMLJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateAutoMLJobV2  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateAutoMLJobV2](#list_sagemaker-action-CreateAutoMLJobV2)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateCluster  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateCluster](#list_sagemaker-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:UpdateClusterSoftware](#list_sagemaker-action-UpdateClusterSoftware)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateClusterSchedulerConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateClusterSchedulerConfig](#list_sagemaker-action-CreateClusterSchedulerConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCodeRepository  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateCodeRepository](#list_sagemaker-action-CreateCodeRepository)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateCompilationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateCompilationJob](#list_sagemaker-action-CreateCompilationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateComputeQuota  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateComputeQuota](#list_sagemaker-action-CreateComputeQuota)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateContext  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateContext](#list_sagemaker-action-CreateContext)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDataQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateDataQualityJobDefinition](#list_sagemaker-action-CreateDataQualityJobDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateDomain  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateDomain](#list_sagemaker-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateEndpoint  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateEndpoint](#list_sagemaker-action-CreateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateEndpointConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateEndpointConfig](#list_sagemaker-action-CreateEndpointConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateExperiment](#list_sagemaker-action-CreateExperiment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateFeatureGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateFeatureGroup](#list_sagemaker-action-CreateFeatureGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateFlowDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateFlowDefinition](#list_sagemaker-action-CreateFlowDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateHub  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateHub](#list_sagemaker-action-CreateHub)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateHubContentPresignedUrls  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreateHubContentPresignedUrls](#list_sagemaker-action-CreateHubContentPresignedUrls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateHubContentReference  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateHubContentReference](#list_sagemaker-action-CreateHubContentReference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateHumanTaskUi  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateHumanTaskUi](#list_sagemaker-action-CreateHumanTaskUi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateHyperParameterTuningJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateHyperParameterTuningJob](#list_sagemaker-action-CreateHyperParameterTuningJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateImage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateImage](#list_sagemaker-action-CreateImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateImageVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreateImageVersion](#list_sagemaker-action-CreateImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateInferenceComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateInferenceComponent](#list_sagemaker-action-CreateInferenceComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateInferenceExperiment](#list_sagemaker-action-CreateInferenceExperiment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateInferenceRecommendationsJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateInferenceRecommendationsJob](#list_sagemaker-action-CreateInferenceRecommendationsJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateJob](#list_sagemaker-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:ImportHubContent](#list_sagemaker-action-ImportHubContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:UpdateHubContent](#list_sagemaker-action-UpdateHubContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** job.sagemaker.amazonaws.com, sagemaker.amazonaws.com / **Access level:** Write

- **   CreateLabelingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateLabelingJob](#list_sagemaker-action-CreateLabelingJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateMlflowApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateMlflowApp](#list_sagemaker-action-CreateMlflowApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateMlflowTrackingServer](#list_sagemaker-action-CreateMlflowTrackingServer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateModel  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModel](#list_sagemaker-action-CreateModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:DeployHubModel](#list_sagemaker-action-DeployHubModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateModelBiasJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelBiasJobDefinition](#list_sagemaker-action-CreateModelBiasJobDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateModelCard  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelCard](#list_sagemaker-action-CreateModelCard)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateModelCardExportJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreateModelCardExportJob](#list_sagemaker-action-CreateModelCardExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateModelExplainabilityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelExplainabilityJobDefinition](#list_sagemaker-action-CreateModelExplainabilityJobDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateModelPackage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelPackage](#list_sagemaker-action-CreateModelPackage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateModelPackageGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelPackageGroup](#list_sagemaker-action-CreateModelPackageGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateModelQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateModelQualityJobDefinition](#list_sagemaker-action-CreateModelQualityJobDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateMonitoringSchedule](#list_sagemaker-action-CreateMonitoringSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateNotebookInstance](#list_sagemaker-action-CreateNotebookInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateNotebookInstanceLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateNotebookInstanceLifecycleConfig](#list_sagemaker-action-CreateNotebookInstanceLifecycleConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateOptimizationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateOptimizationJob](#list_sagemaker-action-CreateOptimizationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreatePartnerApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreatePartnerApp](#list_sagemaker-action-CreatePartnerApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreatePartnerAppPresignedUrl  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreatePartnerAppPresignedUrl](#list_sagemaker-action-CreatePartnerAppPresignedUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePipeline  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreatePipeline](#list_sagemaker-action-CreatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreatePresignedDomainUrl  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreatePresignedDomainUrl](#list_sagemaker-action-CreatePresignedDomainUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePresignedMlflowAppUrl  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreatePresignedMlflowAppUrl](#list_sagemaker-action-CreatePresignedMlflowAppUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePresignedMlflowTrackingServerUrl  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreatePresignedMlflowTrackingServerUrl](#list_sagemaker-action-CreatePresignedMlflowTrackingServerUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePresignedNotebookInstanceUrl  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:CreatePresignedNotebookInstanceUrl](#list_sagemaker-action-CreatePresignedNotebookInstanceUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProcessingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateProcessingJob](#list_sagemaker-action-CreateProcessingJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateProject  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateProject](#list_sagemaker-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateSpace  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateSpace](#list_sagemaker-action-CreateSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateStudioLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateStudioLifecycleConfig](#list_sagemaker-action-CreateStudioLifecycleConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTrainingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateTrainingJob](#list_sagemaker-action-CreateTrainingJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateTrainingPlan  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateReservedCapacity](#list_sagemaker-action-CreateReservedCapacity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:CreateTrainingPlan](#list_sagemaker-action-CreateTrainingPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTransformJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateTransformJob](#list_sagemaker-action-CreateTransformJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTrial  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateTrial](#list_sagemaker-action-CreateTrial)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateTrialComponent](#list_sagemaker-action-CreateTrialComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateUserProfile  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateUserProfile](#list_sagemaker-action-CreateUserProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   CreateWorkforce  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateWorkforce](#list_sagemaker-action-CreateWorkforce)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:CreateWorkteam](#list_sagemaker-action-CreateWorkteam)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAIBenchmarkJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAIBenchmarkJob](#list_sagemaker-action-DeleteAIBenchmarkJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIRecommendationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAIRecommendationJob](#list_sagemaker-action-DeleteAIRecommendationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAIWorkloadConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAIWorkloadConfig](#list_sagemaker-action-DeleteAIWorkloadConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAction  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAction](#list_sagemaker-action-DeleteAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAlgorithm  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAlgorithm](#list_sagemaker-action-DeleteAlgorithm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteApp](#list_sagemaker-action-DeleteApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppImageConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAppImageConfig](#list_sagemaker-action-DeleteAppImageConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArtifact  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteArtifact](#list_sagemaker-action-DeleteArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssociation  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteAssociation](#list_sagemaker-action-DeleteAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCluster  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteCluster](#list_sagemaker-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteClusterSchedulerConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteClusterSchedulerConfig](#list_sagemaker-action-DeleteClusterSchedulerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCodeRepository  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteCodeRepository](#list_sagemaker-action-DeleteCodeRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCompilationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteCompilationJob](#list_sagemaker-action-DeleteCompilationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteComputeQuota  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteComputeQuota](#list_sagemaker-action-DeleteComputeQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContext  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteContext](#list_sagemaker-action-DeleteContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteDataQualityJobDefinition](#list_sagemaker-action-DeleteDataQualityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteDomain](#list_sagemaker-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteEndpoint](#list_sagemaker-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpointConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteEndpointConfig](#list_sagemaker-action-DeleteEndpointConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteExperiment](#list_sagemaker-action-DeleteExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFeatureGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteFeatureGroup](#list_sagemaker-action-DeleteFeatureGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlowDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteFlowDefinition](#list_sagemaker-action-DeleteFlowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHub  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteHub](#list_sagemaker-action-DeleteHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHubContent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteHubContent](#list_sagemaker-action-DeleteHubContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHubContentReference  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteHubContentReference](#list_sagemaker-action-DeleteHubContentReference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHumanTaskUi  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteHumanTaskUi](#list_sagemaker-action-DeleteHumanTaskUi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHyperParameterTuningJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteHyperParameterTuningJob](#list_sagemaker-action-DeleteHyperParameterTuningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteImage](#list_sagemaker-action-DeleteImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImageVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteImageVersion](#list_sagemaker-action-DeleteImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInferenceComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteInferenceComponent](#list_sagemaker-action-DeleteInferenceComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteInferenceExperiment](#list_sagemaker-action-DeleteInferenceExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteJob](#list_sagemaker-action-DeleteJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMlflowApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteMlflowApp](#list_sagemaker-action-DeleteMlflowApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteMlflowTrackingServer](#list_sagemaker-action-DeleteMlflowTrackingServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModel  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModel](#list_sagemaker-action-DeleteModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelBiasJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelBiasJobDefinition](#list_sagemaker-action-DeleteModelBiasJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelCard  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelCard](#list_sagemaker-action-DeleteModelCard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelExplainabilityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelExplainabilityJobDefinition](#list_sagemaker-action-DeleteModelExplainabilityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelPackage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelPackage](#list_sagemaker-action-DeleteModelPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelPackageGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelPackageGroup](#list_sagemaker-action-DeleteModelPackageGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelPackageGroupPolicy  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelPackageGroupPolicy](#list_sagemaker-action-DeleteModelPackageGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteModelQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteModelQualityJobDefinition](#list_sagemaker-action-DeleteModelQualityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteMonitoringSchedule](#list_sagemaker-action-DeleteMonitoringSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteNotebookInstance](#list_sagemaker-action-DeleteNotebookInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotebookInstanceLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteNotebookInstanceLifecycleConfig](#list_sagemaker-action-DeleteNotebookInstanceLifecycleConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOptimizationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteOptimizationJob](#list_sagemaker-action-DeleteOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartnerApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeletePartnerApp](#list_sagemaker-action-DeletePartnerApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipeline  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeletePipeline](#list_sagemaker-action-DeletePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProcessingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteProcessingJob](#list_sagemaker-action-DeleteProcessingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteProject](#list_sagemaker-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSpace  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteSpace](#list_sagemaker-action-DeleteSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStudioLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteStudioLifecycleConfig](#list_sagemaker-action-DeleteStudioLifecycleConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTags  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteTags](#list_sagemaker-action-DeleteTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   DeleteTrainingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteTrainingJob](#list_sagemaker-action-DeleteTrainingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrial  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteTrial](#list_sagemaker-action-DeleteTrial) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteTrialComponent](#list_sagemaker-action-DeleteTrialComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUserProfile  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteUserProfile](#list_sagemaker-action-DeleteUserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkforce  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteWorkforce](#list_sagemaker-action-DeleteWorkforce) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DeleteWorkteam](#list_sagemaker-action-DeleteWorkteam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAIBenchmarkJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAIBenchmarkJob](#list_sagemaker-action-DescribeAIBenchmarkJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAIRecommendationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAIRecommendationJob](#list_sagemaker-action-DescribeAIRecommendationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAIWorkloadConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAIWorkloadConfig](#list_sagemaker-action-DescribeAIWorkloadConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAction  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAction](#list_sagemaker-action-DescribeAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAlgorithm  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAlgorithm](#list_sagemaker-action-DescribeAlgorithm) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeApp](#list_sagemaker-action-DescribeApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAppImageConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAppImageConfig](#list_sagemaker-action-DescribeAppImageConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeArtifact  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeArtifact](#list_sagemaker-action-DescribeArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAutoMLJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAutoMLJob](#list_sagemaker-action-DescribeAutoMLJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAutoMLJobV2  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeAutoMLJobV2](#list_sagemaker-action-DescribeAutoMLJobV2) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCluster  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeCluster](#list_sagemaker-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterEvent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeClusterEvent](#list_sagemaker-action-DescribeClusterEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterNode  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeClusterNode](#list_sagemaker-action-DescribeClusterNode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClusterSchedulerConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeClusterSchedulerConfig](#list_sagemaker-action-DescribeClusterSchedulerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCodeRepository  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeCodeRepository](#list_sagemaker-action-DescribeCodeRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCompilationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeCompilationJob](#list_sagemaker-action-DescribeCompilationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeComputeQuota  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeComputeQuota](#list_sagemaker-action-DescribeComputeQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeContext  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeContext](#list_sagemaker-action-DescribeContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeDataQualityJobDefinition](#list_sagemaker-action-DescribeDataQualityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomain  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeDomain](#list_sagemaker-action-DescribeDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoint  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeEndpoint](#list_sagemaker-action-DescribeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpointConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeEndpointConfig](#list_sagemaker-action-DescribeEndpointConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeExperiment](#list_sagemaker-action-DescribeExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFeatureGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeFeatureGroup](#list_sagemaker-action-DescribeFeatureGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFeatureMetadata  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeFeatureMetadata](#list_sagemaker-action-DescribeFeatureMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlowDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeFlowDefinition](#list_sagemaker-action-DescribeFlowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHub  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeHub](#list_sagemaker-action-DescribeHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHubContent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeHubContent](#list_sagemaker-action-DescribeHubContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHumanTaskUi  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeHumanTaskUi](#list_sagemaker-action-DescribeHumanTaskUi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeHyperParameterTuningJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeHyperParameterTuningJob](#list_sagemaker-action-DescribeHyperParameterTuningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeImage](#list_sagemaker-action-DescribeImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeImageVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeImageVersion](#list_sagemaker-action-DescribeImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInferenceComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeInferenceComponent](#list_sagemaker-action-DescribeInferenceComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeInferenceExperiment](#list_sagemaker-action-DescribeInferenceExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInferenceRecommendationsJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeInferenceRecommendationsJob](#list_sagemaker-action-DescribeInferenceRecommendationsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeJob](#list_sagemaker-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobSchemaVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeJobSchemaVersion](#list_sagemaker-action-DescribeJobSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLabelingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeLabelingJob](#list_sagemaker-action-DescribeLabelingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLineageGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeLineageGroup](#list_sagemaker-action-DescribeLineageGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMlflowApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeMlflowApp](#list_sagemaker-action-DescribeMlflowApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeMlflowTrackingServer](#list_sagemaker-action-DescribeMlflowTrackingServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModel  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModel](#list_sagemaker-action-DescribeModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelBiasJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelBiasJobDefinition](#list_sagemaker-action-DescribeModelBiasJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelCard  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelCard](#list_sagemaker-action-DescribeModelCard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelCardExportJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelCardExportJob](#list_sagemaker-action-DescribeModelCardExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelExplainabilityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelExplainabilityJobDefinition](#list_sagemaker-action-DescribeModelExplainabilityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelPackage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelPackage](#list_sagemaker-action-DescribeModelPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelPackageGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelPackageGroup](#list_sagemaker-action-DescribeModelPackageGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeModelQualityJobDefinition  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeModelQualityJobDefinition](#list_sagemaker-action-DescribeModelQualityJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeMonitoringSchedule](#list_sagemaker-action-DescribeMonitoringSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeNotebookInstance](#list_sagemaker-action-DescribeNotebookInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeNotebookInstanceLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeNotebookInstanceLifecycleConfig](#list_sagemaker-action-DescribeNotebookInstanceLifecycleConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOptimizationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeOptimizationJob](#list_sagemaker-action-DescribeOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePartnerApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribePartnerApp](#list_sagemaker-action-DescribePartnerApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipeline  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribePipeline](#list_sagemaker-action-DescribePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipelineDefinitionForExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribePipelineDefinitionForExecution](#list_sagemaker-action-DescribePipelineDefinitionForExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipelineExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribePipelineExecution](#list_sagemaker-action-DescribePipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProcessingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeProcessingJob](#list_sagemaker-action-DescribeProcessingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProject  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeProject](#list_sagemaker-action-DescribeProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedCapacity  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeReservedCapacity](#list_sagemaker-action-DescribeReservedCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSpace  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeSpace](#list_sagemaker-action-DescribeSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStudioLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeStudioLifecycleConfig](#list_sagemaker-action-DescribeStudioLifecycleConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSubscribedWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeSubscribedWorkteam](#list_sagemaker-action-DescribeSubscribedWorkteam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrainingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTrainingJob](#list_sagemaker-action-DescribeTrainingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrainingPlan  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTrainingPlan](#list_sagemaker-action-DescribeTrainingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrainingPlanExtensionHistory  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTrainingPlanExtensionHistory](#list_sagemaker-action-DescribeTrainingPlanExtensionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTransformJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTransformJob](#list_sagemaker-action-DescribeTransformJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrial  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTrial](#list_sagemaker-action-DescribeTrial) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeTrialComponent](#list_sagemaker-action-DescribeTrialComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeUserProfile  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeUserProfile](#list_sagemaker-action-DescribeUserProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkforce  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeWorkforce](#list_sagemaker-action-DescribeWorkforce) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DescribeWorkteam](#list_sagemaker-action-DescribeWorkteam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetachClusterNodeVolume  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DetachClusterNodeVolume](#list_sagemaker-action-DetachClusterNodeVolume) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableSagemakerServicecatalogPortfolio  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DisableSagemakerServicecatalogPortfolio](#list_sagemaker-action-DisableSagemakerServicecatalogPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:DisassociateTrialComponent](#list_sagemaker-action-DisassociateTrialComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableSagemakerServicecatalogPortfolio  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:EnableSagemakerServicecatalogPortfolio](#list_sagemaker-action-EnableSagemakerServicecatalogPortfolio) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExtendTrainingPlan  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ExtendTrainingPlan](#list_sagemaker-action-ExtendTrainingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLineageGroupPolicy  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:GetLineageGroupPolicy](#list_sagemaker-action-GetLineageGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetModelPackageGroupPolicy  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:GetModelPackageGroupPolicy](#list_sagemaker-action-GetModelPackageGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSagemakerServicecatalogPortfolioStatus  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:GetSagemakerServicecatalogPortfolioStatus](#list_sagemaker-action-GetSagemakerServicecatalogPortfolioStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScalingConfigurationRecommendation  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:GetScalingConfigurationRecommendation](#list_sagemaker-action-GetScalingConfigurationRecommendation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSearchSuggestions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:GetSearchSuggestions](#list_sagemaker-action-GetSearchSuggestions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportHubContent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:ImportHubContent](#list_sagemaker-action-ImportHubContent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   ListAIBenchmarkJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAIBenchmarkJobs](#list_sagemaker-action-ListAIBenchmarkJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIRecommendationJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAIRecommendationJobs](#list_sagemaker-action-ListAIRecommendationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAIWorkloadConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAIWorkloadConfigs](#list_sagemaker-action-ListAIWorkloadConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListActions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListActions](#list_sagemaker-action-ListActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAlgorithms  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAlgorithms](#list_sagemaker-action-ListAlgorithms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAliases  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAliases](#list_sagemaker-action-ListAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppImageConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAppImageConfigs](#list_sagemaker-action-ListAppImageConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListApps  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListApps](#list_sagemaker-action-ListApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListArtifacts  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListArtifacts](#list_sagemaker-action-ListArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociations  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAssociations](#list_sagemaker-action-ListAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutoMLJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListAutoMLJobs](#list_sagemaker-action-ListAutoMLJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCandidatesForAutoMLJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListCandidatesForAutoMLJob](#list_sagemaker-action-ListCandidatesForAutoMLJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterEvents  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListClusterEvents](#list_sagemaker-action-ListClusterEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterNodes  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListClusterNodes](#list_sagemaker-action-ListClusterNodes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusterSchedulerConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListClusterSchedulerConfigs](#list_sagemaker-action-ListClusterSchedulerConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListClusters](#list_sagemaker-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeRepositories  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListCodeRepositories](#list_sagemaker-action-ListCodeRepositories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCompilationJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListCompilationJobs](#list_sagemaker-action-ListCompilationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComputeQuotas  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListComputeQuotas](#list_sagemaker-action-ListComputeQuotas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContexts  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListContexts](#list_sagemaker-action-ListContexts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataQualityJobDefinitions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListDataQualityJobDefinitions](#list_sagemaker-action-ListDataQualityJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListDomains](#list_sagemaker-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpointConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListEndpointConfigs](#list_sagemaker-action-ListEndpointConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEndpoints  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListEndpoints](#list_sagemaker-action-ListEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperiments  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListExperiments](#list_sagemaker-action-ListExperiments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFeatureGroups  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListFeatureGroups](#list_sagemaker-action-ListFeatureGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFlowDefinitions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListFlowDefinitions](#list_sagemaker-action-ListFlowDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHubContentVersions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListHubContentVersions](#list_sagemaker-action-ListHubContentVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHubContents  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListHubContents](#list_sagemaker-action-ListHubContents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHubs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListHubs](#list_sagemaker-action-ListHubs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHumanTaskUis  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListHumanTaskUis](#list_sagemaker-action-ListHumanTaskUis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHyperParameterTuningJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListHyperParameterTuningJobs](#list_sagemaker-action-ListHyperParameterTuningJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageVersions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListImageVersions](#list_sagemaker-action-ListImageVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImages  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListImages](#list_sagemaker-action-ListImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceComponents  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListInferenceComponents](#list_sagemaker-action-ListInferenceComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceExperiments  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListInferenceExperiments](#list_sagemaker-action-ListInferenceExperiments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceRecommendationsJobSteps  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListInferenceRecommendationsJobSteps](#list_sagemaker-action-ListInferenceRecommendationsJobSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInferenceRecommendationsJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListInferenceRecommendationsJobs](#list_sagemaker-action-ListInferenceRecommendationsJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobSchemaVersions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListJobSchemaVersions](#list_sagemaker-action-ListJobSchemaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListJobs](#list_sagemaker-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLabelingJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListLabelingJobs](#list_sagemaker-action-ListLabelingJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLabelingJobsForWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListLabelingJobsForWorkteam](#list_sagemaker-action-ListLabelingJobsForWorkteam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLineageGroups  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListLineageGroups](#list_sagemaker-action-ListLineageGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMlflowApps  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMlflowApps](#list_sagemaker-action-ListMlflowApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMlflowTrackingServers  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMlflowTrackingServers](#list_sagemaker-action-ListMlflowTrackingServers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelBiasJobDefinitions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelBiasJobDefinitions](#list_sagemaker-action-ListModelBiasJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelCardExportJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelCardExportJobs](#list_sagemaker-action-ListModelCardExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelCardVersions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelCardVersions](#list_sagemaker-action-ListModelCardVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelCards  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelCards](#list_sagemaker-action-ListModelCards) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelExplainabilityJobDefinitions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelExplainabilityJobDefinitions](#list_sagemaker-action-ListModelExplainabilityJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelMetadata  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelMetadata](#list_sagemaker-action-ListModelMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelPackageGroups  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelPackageGroups](#list_sagemaker-action-ListModelPackageGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelPackages  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelPackages](#list_sagemaker-action-ListModelPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModelQualityJobDefinitions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModelQualityJobDefinitions](#list_sagemaker-action-ListModelQualityJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListModels  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListModels](#list_sagemaker-action-ListModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitoringAlertHistory  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMonitoringAlertHistory](#list_sagemaker-action-ListMonitoringAlertHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitoringAlerts  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMonitoringAlerts](#list_sagemaker-action-ListMonitoringAlerts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitoringExecutions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMonitoringExecutions](#list_sagemaker-action-ListMonitoringExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMonitoringSchedules  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListMonitoringSchedules](#list_sagemaker-action-ListMonitoringSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebookInstanceLifecycleConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListNotebookInstanceLifecycleConfigs](#list_sagemaker-action-ListNotebookInstanceLifecycleConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotebookInstances  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListNotebookInstances](#list_sagemaker-action-ListNotebookInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOptimizationJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListOptimizationJobs](#list_sagemaker-action-ListOptimizationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerApps  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPartnerApps](#list_sagemaker-action-ListPartnerApps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineExecutionSteps  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPipelineExecutionSteps](#list_sagemaker-action-ListPipelineExecutionSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineExecutions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPipelineExecutions](#list_sagemaker-action-ListPipelineExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineParametersForExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPipelineParametersForExecution](#list_sagemaker-action-ListPipelineParametersForExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelineVersions  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPipelineVersions](#list_sagemaker-action-ListPipelineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelines  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListPipelines](#list_sagemaker-action-ListPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProcessingJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListProcessingJobs](#list_sagemaker-action-ListProcessingJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProjects  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListProjects](#list_sagemaker-action-ListProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceCatalogs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListResourceCatalogs](#list_sagemaker-action-ListResourceCatalogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpaces  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListSpaces](#list_sagemaker-action-ListSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStudioLifecycleConfigs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListStudioLifecycleConfigs](#list_sagemaker-action-ListStudioLifecycleConfigs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscribedWorkteams  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListSubscribedWorkteams](#list_sagemaker-action-ListSubscribedWorkteams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTags](#list_sagemaker-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainingJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTrainingJobs](#list_sagemaker-action-ListTrainingJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainingJobsForHyperParameterTuningJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTrainingJobsForHyperParameterTuningJob](#list_sagemaker-action-ListTrainingJobsForHyperParameterTuningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrainingPlans  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTrainingPlans](#list_sagemaker-action-ListTrainingPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTransformJobs  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTransformJobs](#list_sagemaker-action-ListTransformJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrialComponents  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTrialComponents](#list_sagemaker-action-ListTrialComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrials  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListTrials](#list_sagemaker-action-ListTrials) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUltraServersByReservedCapacity  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListUltraServersByReservedCapacity](#list_sagemaker-action-ListUltraServersByReservedCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUserProfiles  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListUserProfiles](#list_sagemaker-action-ListUserProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkforces  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListWorkforces](#list_sagemaker-action-ListWorkforces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkteams  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:ListWorkteams](#list_sagemaker-action-ListWorkteams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutModelPackageGroupPolicy  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:PutModelPackageGroupPolicy](#list_sagemaker-action-PutModelPackageGroupPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   QueryLineage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:QueryLineage](#list_sagemaker-action-QueryLineage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RenderUiTemplate  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:RenderUiTemplate](#list_sagemaker-action-RenderUiTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   RetryPipelineExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:RetryPipelineExecution](#list_sagemaker-action-RetryPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Search  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:Search](#list_sagemaker-action-Search) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchTrainingPlanOfferings  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:SearchTrainingPlanOfferings](#list_sagemaker-action-SearchTrainingPlanOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendPipelineExecutionStepFailure  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:SendPipelineExecutionStepFailure](#list_sagemaker-action-SendPipelineExecutionStepFailure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendPipelineExecutionStepSuccess  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:SendPipelineExecutionStepSuccess](#list_sagemaker-action-SendPipelineExecutionStepSuccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartClusterHealthCheck  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartClusterHealthCheck](#list_sagemaker-action-StartClusterHealthCheck) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartInferenceExperiment](#list_sagemaker-action-StartInferenceExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartMlflowTrackingServer](#list_sagemaker-action-StartMlflowTrackingServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartMonitoringSchedule](#list_sagemaker-action-StartMonitoringSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartNotebookInstance](#list_sagemaker-action-StartNotebookInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPipelineExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartPipelineExecution](#list_sagemaker-action-StartPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSession  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StartSession](#list_sagemaker-action-StartSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAIBenchmarkJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopAIBenchmarkJob](#list_sagemaker-action-StopAIBenchmarkJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAIRecommendationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopAIRecommendationJob](#list_sagemaker-action-StopAIRecommendationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAutoMLJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopAutoMLJob](#list_sagemaker-action-StopAutoMLJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCompilationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopCompilationJob](#list_sagemaker-action-StopCompilationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopHyperParameterTuningJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopHyperParameterTuningJob](#list_sagemaker-action-StopHyperParameterTuningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopInferenceExperiment](#list_sagemaker-action-StopInferenceExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopInferenceRecommendationsJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopInferenceRecommendationsJob](#list_sagemaker-action-StopInferenceRecommendationsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopJob](#list_sagemaker-action-StopJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopLabelingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopLabelingJob](#list_sagemaker-action-StopLabelingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopMlflowTrackingServer](#list_sagemaker-action-StopMlflowTrackingServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopMonitoringSchedule](#list_sagemaker-action-StopMonitoringSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopNotebookInstance](#list_sagemaker-action-StopNotebookInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopOptimizationJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopOptimizationJob](#list_sagemaker-action-StopOptimizationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPipelineExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopPipelineExecution](#list_sagemaker-action-StopPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopProcessingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopProcessingJob](#list_sagemaker-action-StopProcessingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTrainingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopTrainingJob](#list_sagemaker-action-StopTrainingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTransformJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:StopTransformJob](#list_sagemaker-action-StopTransformJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAction  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateAction](#list_sagemaker-action-UpdateAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAppImageConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateAppImageConfig](#list_sagemaker-action-UpdateAppImageConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateArtifact  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateArtifact](#list_sagemaker-action-UpdateArtifact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCluster  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:BatchAddClusterNodes](#list_sagemaker-action-BatchAddClusterNodes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:BatchDeleteClusterNodes](#list_sagemaker-action-BatchDeleteClusterNodes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:UpdateCluster](#list_sagemaker-action-UpdateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:UpdateClusterSoftware](#list_sagemaker-action-UpdateClusterSoftware)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateClusterSchedulerConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateClusterSchedulerConfig](#list_sagemaker-action-UpdateClusterSchedulerConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClusterSoftware  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateClusterSoftware](#list_sagemaker-action-UpdateClusterSoftware) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCodeRepository  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateCodeRepository](#list_sagemaker-action-UpdateCodeRepository) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateComputeQuota  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateComputeQuota](#list_sagemaker-action-UpdateComputeQuota) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateContext  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateContext](#list_sagemaker-action-UpdateContext) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDomain  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateDomain](#list_sagemaker-action-UpdateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateEndpoint  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateEndpoint](#list_sagemaker-action-UpdateEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEndpointWeightsAndCapacities  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateEndpointWeightsAndCapacities](#list_sagemaker-action-UpdateEndpointWeightsAndCapacities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateExperiment](#list_sagemaker-action-UpdateExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFeatureGroup  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateFeatureGroup](#list_sagemaker-action-UpdateFeatureGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFeatureMetadata  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateFeatureMetadata](#list_sagemaker-action-UpdateFeatureMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHub  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateHub](#list_sagemaker-action-UpdateHub) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHubContent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateHubContent](#list_sagemaker-action-UpdateHubContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateHubContentReference  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateHubContentReference](#list_sagemaker-action-UpdateHubContentReference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateImage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateImage](#list_sagemaker-action-UpdateImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateImageVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateImageVersion](#list_sagemaker-action-UpdateImageVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInferenceComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateInferenceComponent](#list_sagemaker-action-UpdateInferenceComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInferenceComponentRuntimeConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateInferenceComponentRuntimeConfig](#list_sagemaker-action-UpdateInferenceComponentRuntimeConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateInferenceExperiment  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateInferenceExperiment](#list_sagemaker-action-UpdateInferenceExperiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMlflowApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateMlflowApp](#list_sagemaker-action-UpdateMlflowApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMlflowTrackingServer  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateMlflowTrackingServer](#list_sagemaker-action-UpdateMlflowTrackingServer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModelCard  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateModelCard](#list_sagemaker-action-UpdateModelCard) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateModelPackage  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateModelPackage](#list_sagemaker-action-UpdateModelPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMonitoringAlert  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateMonitoringAlert](#list_sagemaker-action-UpdateMonitoringAlert) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMonitoringSchedule  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateMonitoringSchedule](#list_sagemaker-action-UpdateMonitoringSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateNotebookInstance  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateNotebookInstance](#list_sagemaker-action-UpdateNotebookInstance)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateNotebookInstanceLifecycleConfig  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateNotebookInstanceLifecycleConfig](#list_sagemaker-action-UpdateNotebookInstanceLifecycleConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePartnerApp  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:UpdatePartnerApp](#list_sagemaker-action-UpdatePartnerApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdatePipeline  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdatePipeline](#list_sagemaker-action-UpdatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdatePipelineExecution  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdatePipelineExecution](#list_sagemaker-action-UpdatePipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePipelineVersion  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdatePipelineVersion](#list_sagemaker-action-UpdatePipelineVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProject  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:AddTags](#list_sagemaker-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [sagemaker:UpdateProject](#list_sagemaker-action-UpdateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSpace  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateSpace](#list_sagemaker-action-UpdateSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrainingJob  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateTrainingJob](#list_sagemaker-action-UpdateTrainingJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrial  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateTrial](#list_sagemaker-action-UpdateTrial) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrialComponent  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateTrialComponent](#list_sagemaker-action-UpdateTrialComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUserProfile  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateUserProfile](#list_sagemaker-action-UpdateUserProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   UpdateWorkforce  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateWorkforce](#list_sagemaker-action-UpdateWorkforce) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkteam  **
  - **SDK client:** sagemaker
  - **IAM action:**  [sagemaker:UpdateWorkteam](#list_sagemaker-action-UpdateWorkteam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHumanLoop  **
  - **SDK client:** sagemaker-a2i-runtime
  - **IAM action:**  [sagemaker:DeleteHumanLoop](#list_sagemaker-action-DeleteHumanLoop) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeHumanLoop  **
  - **SDK client:** sagemaker-a2i-runtime
  - **IAM action:**  [sagemaker:DescribeHumanLoop](#list_sagemaker-action-DescribeHumanLoop) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListHumanLoops  **
  - **SDK client:** sagemaker-a2i-runtime
  - **IAM action:**  [sagemaker:ListHumanLoops](#list_sagemaker-action-ListHumanLoops) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartHumanLoop  **
  - **SDK client:** sagemaker-a2i-runtime
  - **IAM action:**  [sagemaker:StartHumanLoop](#list_sagemaker-action-StartHumanLoop) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopHumanLoop  **
  - **SDK client:** sagemaker-a2i-runtime
  - **IAM action:**  [sagemaker:StopHumanLoop](#list_sagemaker-action-StopHumanLoop) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetRecord  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:BatchGetRecord](#list_sagemaker-action-BatchGetRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchWriteRecord  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:BatchWriteRecord](#list_sagemaker-action-BatchWriteRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sagemaker:PutRecord](#list_sagemaker-action-PutRecord)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteRecord  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:DeleteRecord](#list_sagemaker-action-DeleteRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRecord  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:GetRecord](#list_sagemaker-action-GetRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRecords  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:ListRecords](#list_sagemaker-action-ListRecords) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutRecord  **
  - **SDK client:** sagemaker-featurestore-runtime
  - **IAM action:**  [sagemaker:PutRecord](#list_sagemaker-action-PutRecord) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetMetrics  **
  - **SDK client:** sagemaker-metrics
  - **IAM action:**  [sagemaker:BatchGetMetrics](#list_sagemaker-action-BatchGetMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutMetrics  **
  - **SDK client:** sagemaker-metrics
  - **IAM action:**  [sagemaker:BatchPutMetrics](#list_sagemaker-action-BatchPutMetrics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InvokeEndpoint  **
  - **SDK client:** sagemaker-runtime
  - **IAM action:**  [sagemaker:InvokeEndpoint](#list_sagemaker-action-InvokeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeEndpointAsync  **
  - **SDK client:** sagemaker-runtime
  - **IAM action:**  [sagemaker:InvokeEndpointAsync](#list_sagemaker-action-InvokeEndpointAsync) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeEndpointWithResponseStream  **
  - **SDK client:** sagemaker-runtime
  - **IAM action:**  [sagemaker:CallWithBearerToken](#list_sagemaker-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sagemaker:InvokeEndpoint](#list_sagemaker-action-InvokeEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CompleteRollout  **
  - **SDK client:** sagemakerjobruntime
  - **IAM action:**  [sagemaker:CallWithBearerToken](#list_sagemaker-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sagemaker:CompleteRollout](#list_sagemaker-action-CompleteRollout)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   Sample  **
  - **SDK client:** sagemakerjobruntime
  - **IAM action:**  [sagemaker:CallWithBearerToken](#list_sagemaker-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sagemaker:Sample](#list_sagemaker-action-Sample)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SampleWithResponseStream  **
  - **SDK client:** sagemakerjobruntime
  - **IAM action:**  [sagemaker:CallWithBearerToken](#list_sagemaker-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sagemaker:SampleWithResponseStream](#list_sagemaker-action-SampleWithResponseStream)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateReward  **
  - **SDK client:** sagemakerjobruntime
  - **IAM action:**  [sagemaker:CallWithBearerToken](#list_sagemaker-action-CallWithBearerToken)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sagemaker:UpdateReward](#list_sagemaker-action-UpdateReward)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by Amazon SageMaker
<a name="list_sagemaker-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddAssociation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddAssociation.html)  **
  - **Description:** Grants permission to associate a lineage entity (artifact, context, action, experiment, experiment-trial-component) to each other
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add or overwrite one or more tags for the specified Amazon SageMaker resource
  - **Resource types (\*required):** [action](#list_sagemaker-resource-action) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [ai-benchmark-job](#list_sagemaker-resource-ai-benchmark-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [ai-recommendation-job](#list_sagemaker-resource-ai-recommendation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [ai-workload-config](#list_sagemaker-resource-ai-workload-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [algorithm](#list_sagemaker-resource-algorithm) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [app](#list_sagemaker-resource-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [app-image-config](#list_sagemaker-resource-app-image-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [artifact](#list_sagemaker-resource-artifact) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [automl-job](#list_sagemaker-resource-automl-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [cluster](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [cluster-scheduler-config](#list_sagemaker-resource-cluster-scheduler-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [code-repository](#list_sagemaker-resource-code-repository) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [compilation-job](#list_sagemaker-resource-compilation-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [compute-quota](#list_sagemaker-resource-compute-quota) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [context](#list_sagemaker-resource-context) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [data-quality-job-definition](#list_sagemaker-resource-data-quality-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [device](#list_sagemaker-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [device-fleet](#list_sagemaker-resource-device-fleet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [domain](#list_sagemaker-resource-domain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [edge-deployment-plan](#list_sagemaker-resource-edge-deployment-plan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [edge-packaging-job](#list_sagemaker-resource-edge-packaging-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [endpoint](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [endpoint-config](#list_sagemaker-resource-endpoint-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [experiment](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [experiment-trial](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [experiment-trial-component](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [feature-group](#list_sagemaker-resource-feature-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [flow-definition](#list_sagemaker-resource-flow-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [hub](#list_sagemaker-resource-hub) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [hub-content](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [human-task-ui](#list_sagemaker-resource-human-task-ui) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [hyper-parameter-tuning-job](#list_sagemaker-resource-hyper-parameter-tuning-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [image](#list_sagemaker-resource-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [inference-component](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [inference-recommendations-job](#list_sagemaker-resource-inference-recommendations-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [job](#list_sagemaker-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [labeling-job](#list_sagemaker-resource-labeling-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [mlflow-app](#list_sagemaker-resource-mlflow-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [mlflow-tracking-server](#list_sagemaker-resource-mlflow-tracking-server) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model](#list_sagemaker-resource-model) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-bias-job-definition](#list_sagemaker-resource-model-bias-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-card](#list_sagemaker-resource-model-card) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-explainability-job-definition](#list_sagemaker-resource-model-explainability-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-package](#list_sagemaker-resource-model-package) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-package-group](#list_sagemaker-resource-model-package-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [model-quality-job-definition](#list_sagemaker-resource-model-quality-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [monitoring-schedule](#list_sagemaker-resource-monitoring-schedule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [notebook-instance](#list_sagemaker-resource-notebook-instance) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [notebook-instance-lifecycle-config](#list_sagemaker-resource-notebook-instance-lifecycle-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [optimization-job](#list_sagemaker-resource-optimization-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [partner-app](#list_sagemaker-resource-partner-app) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [pipeline](#list_sagemaker-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [processing-job](#list_sagemaker-resource-processing-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [project](#list_sagemaker-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [space](#list_sagemaker-resource-space) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [studio-lifecycle-config](#list_sagemaker-resource-studio-lifecycle-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [training-job](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [transform-job](#list_sagemaker-resource-transform-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [user-profile](#list_sagemaker-resource-user-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Resource types (\*required):** [workteam](#list_sagemaker-resource-workteam) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TaggingAction](#list_sagemaker-sagemaker_TaggingAction)
  - **Access level:** Tagging, Write

- **   [AssociateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AssociateTrialComponent.html)  **
  - **Description:** Grants permission to associate a trial component with a trial
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachClusterNodeVolume](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AttachClusterNodeVolume.html)  **
  - **Description:** Grants permission to attach an Amazon EBS volume to a SageMaker HyperPod cluster node
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAddClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchAddClusterNodes.html)  **
  - **Description:** Grants permission to add multiple nodes at a time to a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDeleteClusterNodes.html)  **
  - **Description:** Grants permission to batch delete SageMaker HyperPod cluster nodes
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDescribeModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchDescribeModelPackage.html)  **
  - **Description:** Grants permission to describe one or more ModelPackages
  - **Resource types (\*required):** [model-package\*](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetMetrics](https://docs.aws.amazon.com/sagemaker/latest/APIReference/)  **
  - **Description:** Grants permission to retrieve metrics associated with SageMaker Resources such as Training Jobs or Trial Components
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchGetRecord.html)  **
  - **Description:** Grants permission to get a batch of records from one or more feature groups
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchPutMetrics](https://docs.aws.amazon.com/sagemaker/latest/APIReference/)  **
  - **Description:** Grants permission to publish metrics associated with a SageMaker Resource such as a Training Job or Trial Component
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchRebootClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchRebootClusterNodes.html)  **
  - **Description:** Grants permission to reboot nodes in a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchReplaceClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_BatchReplaceClusterNodes.html)  **
  - **Description:** Grants permission to replace nodes in a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchWriteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_BatchWriteRecord.html)  **
  - **Description:** Grants permission to put a batch of records to one or more feature groups
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CallMlflowAppApi](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)  **
  - **Description:** Grants permission to invoke MLflow APIs
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CallPartnerAppApi](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-onboard.html)  **
  - **Description:** Grants permission for Partner App SDK to access the Partner App for reading or writing data use cases
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CompleteRollout](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompleteRollout.html)  **
  - **Description:** Grants permission to mark a rollout as complete for a job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAIBenchmarkJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIBenchmarkJob.html)  **
  - **Description:** Grants permission to create an AI benchmark job
  - **Resource types (\*required):** [ai-benchmark-job\*](#list_sagemaker-resource-ai-benchmark-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAIRecommendationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIRecommendationJob.html)  **
  - **Description:** Grants permission to create an AI recommendation job
  - **Resource types (\*required):** [ai-recommendation-job\*](#list_sagemaker-resource-ai-recommendation-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAIWorkloadConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIWorkloadConfig.html)  **
  - **Description:** Grants permission to create an AI workload configuration
  - **Resource types (\*required):** [ai-workload-config\*](#list_sagemaker-resource-ai-workload-config)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAction](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAction.html)  **
  - **Description:** Grants permission to create an action
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAlgorithm](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAlgorithm.html)  **
  - **Description:** Grants permission to create an algorithm
  - **Resource types (\*required):** [algorithm\*](#list_sagemaker-resource-algorithm)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateApp.html)  **
  - **Description:** Grants permission to create an App for a SageMaker UserProfile or Space
  - **Resource types (\*required):** [app\*](#list_sagemaker-resource-app)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:OwnerUserProfileArn](#list_sagemaker-sagemaker_OwnerUserProfileArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:SpaceSharingType](#list_sagemaker-sagemaker_SpaceSharingType)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)
  - **Access level:** Write

- **   [CreateAppImageConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAppImageConfig.html)  **
  - **Description:** Grants permission to create an AppImageConfig
  - **Resource types (\*required):** [app-image-config\*](#list_sagemaker-resource-app-image-config)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateArtifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateArtifact.html)  **
  - **Description:** Grants permission to create an artifact
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html)  **
  - **Description:** Grants permission to create an AutoML job
  - **Resource types (\*required):** [automl-job\*](#list_sagemaker-resource-automl-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)  **
  - **Description:** Grants permission to create a V2 AutoML job
  - **Resource types (\*required):** [automl-job\*](#list_sagemaker-resource-automl-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCluster.html)  **
  - **Description:** Grants permission to create a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateClusterSchedulerConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateClusterSchedulerConfig.html)  **
  - **Description:** Grants permission to create a cluster scheduler config
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-scheduler-config\*](#list_sagemaker-resource-cluster-scheduler-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCodeRepository](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCodeRepository.html)  **
  - **Description:** Grants permission to create a CodeRepository
  - **Resource types (\*required):** [code-repository\*](#list_sagemaker-resource-code-repository)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCompilationJob.html)  **
  - **Description:** Grants permission to create a compilation job
  - **Resource types (\*required):** [compilation-job\*](#list_sagemaker-resource-compilation-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComputeQuota](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateComputeQuota.html)  **
  - **Description:** Grants permission to create a compute quota
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [compute-quota\*](#list_sagemaker-resource-compute-quota) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateContext](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateContext.html)  **
  - **Description:** Grants permission to create a context
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDataQualityJobDefinition.html)  **
  - **Description:** Grants permission to create a data quality job definition
  - **Resource types (\*required):** [data-quality-job-definition\*](#list_sagemaker-resource-data-quality-job-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateDeviceFleet](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDeviceFleet.html)  **
  - **Description:** Grants permission to create a device fleet
  - **Resource types (\*required):** [device-fleet\*](#list_sagemaker-resource-device-fleet)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a Domain for SageMaker Studio
  - **Resource types (\*required):** [domain\*](#list_sagemaker-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:AppNetworkAccessType](#list_sagemaker-sagemaker_AppNetworkAccessType)<br />[sagemaker:AuthMode](#list_sagemaker-sagemaker_AuthMode)<br />[sagemaker:DomainSharingOutputKmsKeyArn](#list_sagemaker-sagemaker_DomainSharingOutputKmsKeyArn)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateEdgeDeploymentPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEdgeDeploymentPlan.html)  **
  - **Description:** Grants permission to create an edge deployment plan
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEdgeDeploymentStage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEdgeDeploymentStage.html)  **
  - **Description:** Grants permission to create an edge deployment stage
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEdgePackagingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEdgePackagingJob.html)  **
  - **Description:** Grants permission to create an edge packaging job
  - **Resource types (\*required):** [edge-packaging-job\*](#list_sagemaker-resource-edge-packaging-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html)  **
  - **Description:** Grants permission to create an endpoint using the endpoint configuration specified in the request
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint-config\*](#list_sagemaker-resource-endpoint-config) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html)  **
  - **Description:** Grants permission to create an endpoint configuration that can be deployed using Amazon SageMaker hosting services
  - **Resource types (\*required):** [endpoint-config\*](#list_sagemaker-resource-endpoint-config)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:AcceleratorTypes](#list_sagemaker-sagemaker_AcceleratorTypes)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ModelArn](#list_sagemaker-sagemaker_ModelArn)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:ServerlessMaxConcurrency](#list_sagemaker-sagemaker_ServerlessMaxConcurrency)<br />[sagemaker:ServerlessMemorySize](#list_sagemaker-sagemaker_ServerlessMemorySize)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateExperiment.html)  **
  - **Description:** Grants permission to create an experiment
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFeatureGroup.html)  **
  - **Description:** Grants permission to create a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:FeatureGroupDisableGlueTableCreation](#list_sagemaker-sagemaker_FeatureGroupDisableGlueTableCreation)<br />[sagemaker:FeatureGroupEnableOnlineStore](#list_sagemaker-sagemaker_FeatureGroupEnableOnlineStore)<br />[sagemaker:FeatureGroupOfflineStoreConfig](#list_sagemaker-sagemaker_FeatureGroupOfflineStoreConfig)<br />[sagemaker:FeatureGroupOfflineStoreKmsKeyArn](#list_sagemaker-sagemaker_FeatureGroupOfflineStoreKmsKeyArn)<br />[sagemaker:FeatureGroupOfflineStoreS3Uri](#list_sagemaker-sagemaker_FeatureGroupOfflineStoreS3Uri)<br />[sagemaker:FeatureGroupOnlineStoreKmsKeyArn](#list_sagemaker-sagemaker_FeatureGroupOnlineStoreKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFlowDefinition.html)  **
  - **Description:** Grants permission to create a flow definition, which defines settings for a human workflow
  - **Resource types (\*required):** [flow-definition\*](#list_sagemaker-resource-flow-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:WorkteamArn](#list_sagemaker-sagemaker_WorkteamArn)<br />[sagemaker:WorkteamType](#list_sagemaker-sagemaker_WorkteamType)
  - **Access level:** Write

- **   [CreateHub](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHub.html)  **
  - **Description:** Grants permission to create a hub
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateHubContentPresignedUrls](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHubContentPresignedUrls.html)  **
  - **Description:** Grants permission to generate S3 presigned URLs with GetObject permission for accessing model artifacts
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateHubContentReference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHubContentReference.html)  **
  - **Description:** Grants permission to create hub content reference
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateHumanTaskUi](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHumanTaskUi.html)  **
  - **Description:** Grants permission to define the settings you will use for the human review workflow user interface
  - **Resource types (\*required):** [human-task-ui\*](#list_sagemaker-resource-human-task-ui)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html)  **
  - **Description:** Grants permission to create a hyper parameter tuning job that can be deployed using Amazon SageMaker
  - **Resource types (\*required):** [hyper-parameter-tuning-job\*](#list_sagemaker-resource-hyper-parameter-tuning-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:FileSystemAccessMode](#list_sagemaker-sagemaker_FileSystemAccessMode)<br />[sagemaker:FileSystemDirectoryPath](#list_sagemaker-sagemaker_FileSystemDirectoryPath)<br />[sagemaker:FileSystemId](#list_sagemaker-sagemaker_FileSystemId)<br />[sagemaker:FileSystemType](#list_sagemaker-sagemaker_FileSystemType)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateImage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateImage.html)  **
  - **Description:** Grants permission to create a SageMaker Image
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateImageVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateImageVersion.html)  **
  - **Description:** Grants permission to create a SageMaker ImageVersion
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInferenceComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceComponent.html)  **
  - **Description:** Grants permission to create an inference component on an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ModelArn](#list_sagemaker-sagemaker_ModelArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-component\*](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ModelArn](#list_sagemaker-sagemaker_ModelArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html)  **
  - **Description:** Grants permission to create an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInferenceRecommendationsJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceRecommendationsJob.html)  **
  - **Description:** Grants permission to create an inference recommendations job
  - **Resource types (\*required):** [inference-recommendations-job\*](#list_sagemaker-resource-inference-recommendations-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateJob.html)  **
  - **Description:** Grants permission to create a SageMaker model customization job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateLabelingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html)  **
  - **Description:** Grants permission to start a labeling job. A labeling job takes unlabeled data in and produces labeled data as output, which can be used for training SageMaker models
  - **Resource types (\*required):** [labeling-job\*](#list_sagemaker-resource-labeling-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:WorkteamArn](#list_sagemaker-sagemaker_WorkteamArn)<br />[sagemaker:WorkteamType](#list_sagemaker-sagemaker_WorkteamType)
  - **Access level:** Write

- **   [CreateLineageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to create a lineage group policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMlflowApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMlflowApp.html)  **
  - **Description:** Grants permission to create an MLflow app
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMlflowTrackingServer.html)  **
  - **Description:** Grants permission to create an MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModel.html)  **
  - **Description:** Grants permission to create a model in Amazon SageMaker. In the request, you specify a name for the model and describe one or more containers
  - **Resource types (\*required):** [model\*](#list_sagemaker-resource-model)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:DirectGatedModelAccess](#list_sagemaker-sagemaker_DirectGatedModelAccess)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateModelBiasJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelBiasJobDefinition.html)  **
  - **Description:** Grants permission to create a model bias job definition
  - **Resource types (\*required):** [model-bias-job-definition\*](#list_sagemaker-resource-model-bias-job-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelCard.html)  **
  - **Description:** Grants permission to create a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModelCardExportJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelCardExportJob.html)  **
  - **Description:** Grants permission to create an export job for a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModelExplainabilityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelExplainabilityJobDefinition.html)  **
  - **Description:** Grants permission to create a model explainability job definition
  - **Resource types (\*required):** [model-explainability-job-definition\*](#list_sagemaker-resource-model-explainability-job-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackage.html)  **
  - **Description:** Grants permission to create a ModelPackage
  - **Resource types (\*required):** [model-package](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:CustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CustomerMetadataProperties___MetadataKey_)<br />[sagemaker:ModelApprovalStatus](#list_sagemaker-sagemaker_ModelApprovalStatus)<br />[sagemaker:ModelLifeCycle:Stage](#list_sagemaker-sagemaker_ModelLifeCycle_Stage)<br />[sagemaker:ModelLifeCycle:StageStatus](#list_sagemaker-sagemaker_ModelLifeCycle_StageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModelPackageGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackageGroup.html)  **
  - **Description:** Grants permission to create a ModelPackageGroup
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateModelQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelQualityJobDefinition.html)  **
  - **Description:** Grants permission to create a model quality job definition
  - **Resource types (\*required):** [model-quality-job-definition\*](#list_sagemaker-resource-model-quality-job-definition)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateMonitoringSchedule.html)  **
  - **Description:** Grants permission to create a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstance.html)  **
  - **Description:** Grants permission to create an Amazon SageMaker notebook instance. A notebook instance is an Amazon EC2 instance running on a Jupyter Notebook
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:AcceleratorTypes](#list_sagemaker-sagemaker_AcceleratorTypes)<br />[sagemaker:DirectInternetAccess](#list_sagemaker-sagemaker_DirectInternetAccess)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:MinimumInstanceMetadataServiceVersion](#list_sagemaker-sagemaker_MinimumInstanceMetadataServiceVersion)<br />[sagemaker:NotebookInstanceLifecycleConfigArns](#list_sagemaker-sagemaker_NotebookInstanceLifecycleConfigArns)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:RootAccess](#list_sagemaker-sagemaker_RootAccess)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html)  **
  - **Description:** Grants permission to create a notebook instance lifecycle configuration that can be deployed using Amazon SageMaker
  - **Resource types (\*required):** [notebook-instance-lifecycle-config\*](#list_sagemaker-resource-notebook-instance-lifecycle-config)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOptimizationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateOptimizationJob.html)  **
  - **Description:** Grants permission to create an optimization job
  - **Resource types (\*required):** [optimization-job\*](#list_sagemaker-resource-optimization-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePartnerApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePartnerApp.html)  **
  - **Description:** Grants permission to create an Amazon SageMaker Partner AI App
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePartnerAppPresignedUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePartnerAppPresignedUrl.html)  **
  - **Description:** Grants permission to return a URL that you can use from your browser to connect to the Amazon SageMaker Partner AI App
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePipeline.html)  **
  - **Description:** Grants permission to create a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePresignedDomainUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedDomainUrl.html)  **
  - **Description:** Grants permission to return a URL that you can use from your browser to connect to the Domain as a specified UserProfile when AuthMode is 'IAM'
  - **Resource types (\*required):** [user-profile\*](#list_sagemaker-resource-user-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePresignedMlflowAppUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowAppUrl.html)  **
  - **Description:** Grants permission to return a URL that you can use from your browser to connect to the MLflow app
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePresignedMlflowTrackingServerUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowTrackingServerUrl.html)  **
  - **Description:** Grants permission to return a URL that you can use from your browser to connect to the MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePresignedNotebookInstanceUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html)  **
  - **Description:** Grants permission to create a URL that you can use from your browser to connect to the Notebook Instance
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)  **
  - **Description:** Grants permission to start a processing job. After processing completes, Amazon SageMaker saves the resulting artifacts and other optional output to an Amazon S3 location that you specify
  - **Resource types (\*required):** [processing-job\*](#list_sagemaker-resource-processing-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a Project
  - **Resource types (\*required):** [project\*](#list_sagemaker-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateSpace.html)  **
  - **Description:** Grants permission to create a Space for a SageMaker Domain
  - **Resource types (\*required):** [space\*](#list_sagemaker-resource-space)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:OwnerUserProfileArn](#list_sagemaker-sagemaker_OwnerUserProfileArn)<br />[sagemaker:RemoteAccess](#list_sagemaker-sagemaker_RemoteAccess)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:SpaceSharingType](#list_sagemaker-sagemaker_SpaceSharingType)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)
  - **Access level:** Write

- **   [CreateStudioLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateStudioLifecycleConfig.html)  **
  - **Description:** Grants permission to create a Studio Lifecycle Configuration that can be deployed using Amazon SageMaker
  - **Resource types (\*required):** [studio-lifecycle-config\*](#list_sagemaker-resource-studio-lifecycle-config)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)  **
  - **Description:** Grants permission to start a model training job. After training completes, Amazon SageMaker saves the resulting model artifacts and other optional output to an Amazon S3 location that you specify
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:DirectGatedModelAccess](#list_sagemaker-sagemaker_DirectGatedModelAccess)<br />[sagemaker:EnableRemoteDebug](#list_sagemaker-sagemaker_EnableRemoteDebug)<br />[sagemaker:FileSystemAccessMode](#list_sagemaker-sagemaker_FileSystemAccessMode)<br />[sagemaker:FileSystemDirectoryPath](#list_sagemaker-sagemaker_FileSystemDirectoryPath)<br />[sagemaker:FileSystemId](#list_sagemaker-sagemaker_FileSystemId)<br />[sagemaker:FileSystemType](#list_sagemaker-sagemaker_FileSystemType)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:KeepAlivePeriod](#list_sagemaker-sagemaker_KeepAlivePeriod)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:DirectGatedModelAccess](#list_sagemaker-sagemaker_DirectGatedModelAccess)<br />[sagemaker:EnableRemoteDebug](#list_sagemaker-sagemaker_EnableRemoteDebug)<br />[sagemaker:FileSystemAccessMode](#list_sagemaker-sagemaker_FileSystemAccessMode)<br />[sagemaker:FileSystemDirectoryPath](#list_sagemaker-sagemaker_FileSystemDirectoryPath)<br />[sagemaker:FileSystemId](#list_sagemaker-sagemaker_FileSystemId)<br />[sagemaker:FileSystemType](#list_sagemaker-sagemaker_FileSystemType)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:KeepAlivePeriod](#list_sagemaker-sagemaker_KeepAlivePeriod)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:DirectGatedModelAccess](#list_sagemaker-sagemaker_DirectGatedModelAccess)<br />[sagemaker:EnableRemoteDebug](#list_sagemaker-sagemaker_EnableRemoteDebug)<br />[sagemaker:FileSystemAccessMode](#list_sagemaker-sagemaker_FileSystemAccessMode)<br />[sagemaker:FileSystemDirectoryPath](#list_sagemaker-sagemaker_FileSystemDirectoryPath)<br />[sagemaker:FileSystemId](#list_sagemaker-sagemaker_FileSystemId)<br />[sagemaker:FileSystemType](#list_sagemaker-sagemaker_FileSystemType)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:KeepAlivePeriod](#list_sagemaker-sagemaker_KeepAlivePeriod)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html)  **
  - **Description:** Grants permission to create a training plan that allocates resources for scheduling workloads within a specified time range
  - **Resource types (\*required):** [training-plan\*](#list_sagemaker-resource-training-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)  **
  - **Description:** Grants permission to start a transform job. After the results are obtained, Amazon SageMaker saves them to an Amazon S3 location that you specify
  - **Resource types (\*required):** [transform-job\*](#list_sagemaker-resource-transform-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ModelArn](#list_sagemaker-sagemaker_ModelArn)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)
  - **Access level:** Write

- **   [CreateTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrial.html)  **
  - **Description:** Grants permission to create a trial
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html)  **
  - **Description:** Grants permission to create a trial component
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateUserProfile.html)  **
  - **Description:** Grants permission to create a UserProfile for a SageMaker Domain
  - **Resource types (\*required):** [user-profile\*](#list_sagemaker-resource-user-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:DomainSharingOutputKmsKeyArn](#list_sagemaker-sagemaker_DomainSharingOutputKmsKeyArn)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)
  - **Access level:** Write

- **   [CreateWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkforce.html)  **
  - **Description:** Grants permission to create a workforce
  - **Resource types (\*required):** [workforce\*](#list_sagemaker-resource-workforce)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateWorkteam.html)  **
  - **Description:** Grants permission to create a workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIBenchmarkJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAIBenchmarkJob.html)  **
  - **Description:** Grants permission to delete an AI benchmark job
  - **Resource types (\*required):** [ai-benchmark-job\*](#list_sagemaker-resource-ai-benchmark-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIRecommendationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAIRecommendationJob.html)  **
  - **Description:** Grants permission to delete an AI recommendation job
  - **Resource types (\*required):** [ai-recommendation-job\*](#list_sagemaker-resource-ai-recommendation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAIWorkloadConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAIWorkloadConfig.html)  **
  - **Description:** Grants permission to delete an AI workload configuration
  - **Resource types (\*required):** [ai-workload-config\*](#list_sagemaker-resource-ai-workload-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAction](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAction.html)  **
  - **Description:** Grants permission to delete an action
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAlgorithm](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAlgorithm.html)  **
  - **Description:** Grants permission to delete an algorithm
  - **Resource types (\*required):** [algorithm\*](#list_sagemaker-resource-algorithm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to delete an App
  - **Resource types (\*required):** [app\*](#list_sagemaker-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:OwnerUserProfileArn](#list_sagemaker-sagemaker_OwnerUserProfileArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:SpaceSharingType](#list_sagemaker-sagemaker_SpaceSharingType)
  - **Access level:** Write

- **   [DeleteAppImageConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAppImageConfig.html)  **
  - **Description:** Grants permission to delete an AppImageConfig
  - **Resource types (\*required):** [app-image-config\*](#list_sagemaker-resource-app-image-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteArtifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteArtifact.html)  **
  - **Description:** Grants permission to delete an artifact
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssociation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteAssociation.html)  **
  - **Description:** Grants permission to delete the association from a lineage entity (artifact, context, action, experiment, experiment-trial-component) to another
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteCluster.html)  **
  - **Description:** Grants permission to delete a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteClusterSchedulerConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteClusterSchedulerConfig.html)  **
  - **Description:** Grants permission to delete a cluster scheduler config
  - **Resource types (\*required):** [cluster-scheduler-config\*](#list_sagemaker-resource-cluster-scheduler-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCodeRepository](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteCodeRepository.html)  **
  - **Description:** Grants permission to delete a CodeRepository
  - **Resource types (\*required):** [code-repository\*](#list_sagemaker-resource-code-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteCompilationJob.html)  **
  - **Description:** Grants permission to delete a compilation job
  - **Resource types (\*required):** [compilation-job\*](#list_sagemaker-resource-compilation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteComputeQuota](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteComputeQuota.html)  **
  - **Description:** Grants permission to delete a compute quota
  - **Resource types (\*required):** [compute-quota\*](#list_sagemaker-resource-compute-quota)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContext](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteContext.html)  **
  - **Description:** Grants permission to delete a context
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteDataQualityJobDefinition.html)  **
  - **Description:** Grants permission to delete the data quality job definition created using the CreateDataQualityJobDefinition API
  - **Resource types (\*required):** [data-quality-job-definition\*](#list_sagemaker-resource-data-quality-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeviceFleet](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteDeviceFleet.html)  **
  - **Description:** Grants permission to delete a device fleet
  - **Resource types (\*required):** [device-fleet\*](#list_sagemaker-resource-device-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete a Domain
  - **Resource types (\*required):** [domain\*](#list_sagemaker-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEdgeDeploymentPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEdgeDeploymentPlan.html)  **
  - **Description:** Grants permission to delete an edge deployment plan
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEdgeDeploymentStage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEdgeDeploymentStage.html)  **
  - **Description:** Grants permission to delete an edge deployment stage
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete an endpoint. Amazon SageMaker frees up all the resources that were deployed when the endpoint was created
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpointConfig.html)  **
  - **Description:** Grants permission to delete the endpoint configuration created using the CreateEndpointConfig API. The DeleteEndpointConfig API deletes only the specified configuration. It does not delete any endpoints created using the configuration
  - **Resource types (\*required):** [endpoint-config\*](#list_sagemaker-resource-endpoint-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteExperiment.html)  **
  - **Description:** Grants permission to delete an experiment
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFeatureGroup.html)  **
  - **Description:** Grants permission to delete a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFlowDefinition.html)  **
  - **Description:** Grants permission to delete the specified flow definition
  - **Resource types (\*required):** [flow-definition\*](#list_sagemaker-resource-flow-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHub](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHub.html)  **
  - **Description:** Grants permission to delete hubs
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHubContent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHubContent.html)  **
  - **Description:** Grants permission to delete hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHubContentReference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHubContentReference.html)  **
  - **Description:** Grants permission to delete hub content reference
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHumanLoop](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHumanLoop.html)  **
  - **Description:** Grants permission to delete a specified human loop
  - **Resource types (\*required):** [human-loop\*](#list_sagemaker-resource-human-loop)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteHumanTaskUi](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHumanTaskUi.html)  **
  - **Description:** Grants permission to delete the specified human task user interface (worker task template)
  - **Resource types (\*required):** [human-task-ui\*](#list_sagemaker-resource-human-task-ui)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteHyperParameterTuningJob.html)  **
  - **Description:** Grants permission to delete a hyper parameter tuning job
  - **Resource types (\*required):** [hyper-parameter-tuning-job\*](#list_sagemaker-resource-hyper-parameter-tuning-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteImage.html)  **
  - **Description:** Grants permission to delete a SageMaker Image
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImageVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteImageVersion.html)  **
  - **Description:** Grants permission to delete a SageMaker ImageVersion
  - **Resource types (\*required):** [image-version\*](#list_sagemaker-resource-image-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInferenceComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteInferenceComponent.html)  **
  - **Description:** Grants permission to delete an inference component. Amazon SageMaker frees up the resources that were reserved when the inference component was created
  - **Resource types (\*required):** [inference-component\*](#list_sagemaker-resource-inference-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteInferenceExperiment.html)  **
  - **Description:** Grants permission to delete an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteJob.html)  **
  - **Description:** Grants permission to delete a SageMaker model customization job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLineageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to delete a lineage group policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMlflowApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteMlflowApp.html)  **
  - **Description:** Grants permission to delete an MLflow app
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteMlflowTrackingServer.html)  **
  - **Description:** Grants permission to delete an MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModel.html)  **
  - **Description:** Grants permission to delete a model created using the CreateModel API. The DeleteModel API deletes only the model entry in Amazon SageMaker that you created by calling the CreateModel API. It does not delete model artifacts, inference code, or the IAM role that you specified when creating the model
  - **Resource types (\*required):** [model\*](#list_sagemaker-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelBiasJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelBiasJobDefinition.html)  **
  - **Description:** Grants permission to delete the model bias job definition created using the CreateModelBiasJobDefinition API
  - **Resource types (\*required):** [model-bias-job-definition\*](#list_sagemaker-resource-model-bias-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelCard.html)  **
  - **Description:** Grants permission to delete a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelExplainabilityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelExplainabilityJobDefinition.html)  **
  - **Description:** Grants permission to delete the model explainability job definition created using the CreateModelExplainabilityJobDefinition API
  - **Resource types (\*required):** [model-explainability-job-definition\*](#list_sagemaker-resource-model-explainability-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelPackage.html)  **
  - **Description:** Grants permission to delete a ModelPackage
  - **Resource types (\*required):** [model-package\*](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelPackageGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelPackageGroup.html)  **
  - **Description:** Grants permission to delete a ModelPackageGroup
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelPackageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelPackageGroupPolicy.html)  **
  - **Description:** Grants permission to delete a ModelPackageGroup policy
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteModelQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteModelQualityJobDefinition.html)  **
  - **Description:** Grants permission to delete the model quality job definition created using the CreateModelQualityJobDefinition API
  - **Resource types (\*required):** [model-quality-job-definition\*](#list_sagemaker-resource-model-quality-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteMonitoringSchedule.html)  **
  - **Description:** Grants permission to delete a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteNotebookInstance.html)  **
  - **Description:** Grants permission to delete a Amazon SageMaker notebook instance. Before you can delete a notebook instance, you must call the StopNotebookInstance API
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteNotebookInstanceLifecycleConfig.html)  **
  - **Description:** Grants permission to delete a notebook instance lifecycle configuration
  - **Resource types (\*required):** [notebook-instance-lifecycle-config\*](#list_sagemaker-resource-notebook-instance-lifecycle-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOptimizationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteOptimizationJob.html)  **
  - **Description:** Grants permission to delete an optimization job
  - **Resource types (\*required):** [optimization-job\*](#list_sagemaker-resource-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartnerApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeletePartnerApp.html)  **
  - **Description:** Grants permission to delete an Amazon SageMaker Partner AI App
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeletePipeline.html)  **
  - **Description:** Grants permission to delete a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteProcessingJob.html)  **
  - **Description:** Grants permission to delete a processing job
  - **Resource types (\*required):** [processing-job\*](#list_sagemaker-resource-processing-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [project\*](#list_sagemaker-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html)  **
  - **Description:** Grants permission to delete a record from a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteSpace.html)  **
  - **Description:** Grants permission to delete a Space
  - **Resource types (\*required):** [space\*](#list_sagemaker-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:OwnerUserProfileArn](#list_sagemaker-sagemaker_OwnerUserProfileArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:SpaceSharingType](#list_sagemaker-sagemaker_SpaceSharingType)
  - **Access level:** Write

- **   [DeleteStudioLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteStudioLifecycleConfig.html)  **
  - **Description:** Grants permission to delete a Studio Lifecycle Configuration
  - **Resource types (\*required):** [studio-lifecycle-config\*](#list_sagemaker-resource-studio-lifecycle-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTags.html)  **
  - **Description:** Grants permission to delete the specified set of tags from an Amazon SageMaker resource
  - **Resource types (\*required):** [action](#list_sagemaker-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-benchmark-job](#list_sagemaker-resource-ai-benchmark-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-recommendation-job](#list_sagemaker-resource-ai-recommendation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-workload-config](#list_sagemaker-resource-ai-workload-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [algorithm](#list_sagemaker-resource-algorithm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app](#list_sagemaker-resource-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app-image-config](#list_sagemaker-resource-app-image-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [artifact](#list_sagemaker-resource-artifact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automl-job](#list_sagemaker-resource-automl-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-scheduler-config](#list_sagemaker-resource-cluster-scheduler-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [code-repository](#list_sagemaker-resource-code-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [compilation-job](#list_sagemaker-resource-compilation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [compute-quota](#list_sagemaker-resource-compute-quota) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [context](#list_sagemaker-resource-context) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-quality-job-definition](#list_sagemaker-resource-data-quality-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device](#list_sagemaker-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device-fleet](#list_sagemaker-resource-device-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domain](#list_sagemaker-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [edge-deployment-plan](#list_sagemaker-resource-edge-deployment-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [edge-packaging-job](#list_sagemaker-resource-edge-packaging-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint-config](#list_sagemaker-resource-endpoint-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [feature-group](#list_sagemaker-resource-feature-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-definition](#list_sagemaker-resource-flow-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [human-task-ui](#list_sagemaker-resource-human-task-ui) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hyper-parameter-tuning-job](#list_sagemaker-resource-hyper-parameter-tuning-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image](#list_sagemaker-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-component](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-recommendations-job](#list_sagemaker-resource-inference-recommendations-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job](#list_sagemaker-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [labeling-job](#list_sagemaker-resource-labeling-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mlflow-app](#list_sagemaker-resource-mlflow-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mlflow-tracking-server](#list_sagemaker-resource-mlflow-tracking-server) / **Condition keys:** [aws:TagKeys](#list_sagemaker-aws_TagKeys)
  - **Resource types (\*required):** [model](#list_sagemaker-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-bias-job-definition](#list_sagemaker-resource-model-bias-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-card](#list_sagemaker-resource-model-card) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-explainability-job-definition](#list_sagemaker-resource-model-explainability-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-package](#list_sagemaker-resource-model-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-package-group](#list_sagemaker-resource-model-package-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-quality-job-definition](#list_sagemaker-resource-model-quality-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [monitoring-schedule](#list_sagemaker-resource-monitoring-schedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-instance](#list_sagemaker-resource-notebook-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-instance-lifecycle-config](#list_sagemaker-resource-notebook-instance-lifecycle-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [optimization-job](#list_sagemaker-resource-optimization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [partner-app](#list_sagemaker-resource-partner-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_sagemaker-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [processing-job](#list_sagemaker-resource-processing-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_sagemaker-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [space](#list_sagemaker-resource-space) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [studio-lifecycle-config](#list_sagemaker-resource-studio-lifecycle-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-job](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [transform-job](#list_sagemaker-resource-transform-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user-profile](#list_sagemaker-resource-user-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workteam](#list_sagemaker-resource-workteam) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [DeleteTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrainingJob.html)  **
  - **Description:** Grants permission to delete a training job
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrial.html)  **
  - **Description:** Grants permission to delete a trial
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrialComponent.html)  **
  - **Description:** Grants permission to delete a trial component
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteUserProfile.html)  **
  - **Description:** Grants permission to delete a UserProfile
  - **Resource types (\*required):** [user-profile\*](#list_sagemaker-resource-user-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkforce.html)  **
  - **Description:** Grants permission to delete a workforce
  - **Resource types (\*required):** [workforce\*](#list_sagemaker-resource-workforce)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteWorkteam.html)  **
  - **Description:** Grants permission to delete a workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeployHubModel](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.html)  **
  - **Description:** Grants permission to deploy a model in hub to an endpoint
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterDevices](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeregisterDevices.html)  **
  - **Description:** Grants permission to deregister a set of devices
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAIBenchmarkJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIBenchmarkJob.html)  **
  - **Description:** Grants permission to describe an AI benchmark job
  - **Resource types (\*required):** [ai-benchmark-job\*](#list_sagemaker-resource-ai-benchmark-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAIRecommendationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIRecommendationJob.html)  **
  - **Description:** Grants permission to describe an AI recommendation job
  - **Resource types (\*required):** [ai-recommendation-job\*](#list_sagemaker-resource-ai-recommendation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAIWorkloadConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIWorkloadConfig.html)  **
  - **Description:** Grants permission to describe an AI workload configuration
  - **Resource types (\*required):** [ai-workload-config\*](#list_sagemaker-resource-ai-workload-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAction](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAction.html)  **
  - **Description:** Grants permission to get information about an action
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAlgorithm](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAlgorithm.html)  **
  - **Description:** Grants permission to describe an algorithm
  - **Resource types (\*required):** [algorithm\*](#list_sagemaker-resource-algorithm)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeApp.html)  **
  - **Description:** Grants permission to describe an App
  - **Resource types (\*required):** [app\*](#list_sagemaker-resource-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAppImageConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAppImageConfig.html)  **
  - **Description:** Grants permission to describe an AppImageConfig
  - **Resource types (\*required):** [app-image-config\*](#list_sagemaker-resource-app-image-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeArtifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeArtifact.html)  **
  - **Description:** Grants permission to get information about an artifact
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html)  **
  - **Description:** Grants permission to describe an AutoML job that was created via the CreateAutoMLJob API
  - **Resource types (\*required):** [automl-job\*](#list_sagemaker-resource-automl-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html)  **
  - **Description:** Grants permission to describe an AutoML job that was created via the CreateAutoMLJobV2 API
  - **Resource types (\*required):** [automl-job\*](#list_sagemaker-resource-automl-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCluster.html)  **
  - **Description:** Grants permission to return information about a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterEvent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterEvent.html)  **
  - **Description:** Grants permission to return information about an Event within a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterNode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterNode.html)  **
  - **Description:** Grants permission to return information about a SageMaker HyperPod cluster node
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeClusterSchedulerConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterSchedulerConfig.html)  **
  - **Description:** Grants permission to get information about a cluster scheduler config
  - **Resource types (\*required):** [cluster-scheduler-config\*](#list_sagemaker-resource-cluster-scheduler-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCodeRepository](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCodeRepository.html)  **
  - **Description:** Grants permission to describe a CodeRepository
  - **Resource types (\*required):** [code-repository\*](#list_sagemaker-resource-code-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCompilationJob.html)  **
  - **Description:** Grants permission to return information about a compilation job
  - **Resource types (\*required):** [compilation-job\*](#list_sagemaker-resource-compilation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeComputeQuota](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeComputeQuota.html)  **
  - **Description:** Grants permission to get information about a compute quota
  - **Resource types (\*required):** [compute-quota\*](#list_sagemaker-resource-compute-quota)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeContext](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeContext.html)  **
  - **Description:** Grants permission to get information about a context
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDataQualityJobDefinition.html)  **
  - **Description:** Grants permission to return information about a data quality job definition
  - **Resource types (\*required):** [data-quality-job-definition\*](#list_sagemaker-resource-data-quality-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDevice](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDevice.html)  **
  - **Description:** Grants permission to access information about a device
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDeviceFleet](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDeviceFleet.html)  **
  - **Description:** Grants permission to access information about a device fleet
  - **Resource types (\*required):** [device-fleet\*](#list_sagemaker-resource-device-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to describe a Domain
  - **Resource types (\*required):** [domain\*](#list_sagemaker-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEdgeDeploymentPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEdgeDeploymentPlan.html)  **
  - **Description:** Grants permission to access information about an edge deployment plan
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEdgePackagingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEdgePackagingJob.html)  **
  - **Description:** Grants permission to access information about an edge packaging job
  - **Resource types (\*required):** [edge-packaging-job\*](#list_sagemaker-resource-edge-packaging-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html)  **
  - **Description:** Grants permission to return the description of an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpointConfig.html)  **
  - **Description:** Grants permission to return the description of an endpoint configuration, which was created using the CreateEndpointConfig API
  - **Resource types (\*required):** [endpoint-config\*](#list_sagemaker-resource-endpoint-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeExperiment.html)  **
  - **Description:** Grants permission to return information about an experiment
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html)  **
  - **Description:** Grants permission to return information about a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFeatureMetadata](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureMetadata.html)  **
  - **Description:** Grants permission to return information about a feature metadata
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFlowDefinition.html)  **
  - **Description:** Grants permission to return information about the specified flow definition
  - **Resource types (\*required):** [flow-definition\*](#list_sagemaker-resource-flow-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHub](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHub.html)  **
  - **Description:** Grants permission to describe hubs
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHubContent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHubContent.html)  **
  - **Description:** Grants permission to describe hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHumanLoop](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHumanLoop.html)  **
  - **Description:** Grants permission to return information about the specified human loop
  - **Resource types (\*required):** [human-loop\*](#list_sagemaker-resource-human-loop)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeHumanTaskUi](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHumanTaskUi.html)  **
  - **Description:** Grants permission to return detailed information about the specified human review workflow user interface
  - **Resource types (\*required):** [human-task-ui\*](#list_sagemaker-resource-human-task-ui)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHyperParameterTuningJob.html)  **
  - **Description:** Grants permission to describe a hyper parameter tuning job that was created via the CreateHyperParameterTuningJob API
  - **Resource types (\*required):** [hyper-parameter-tuning-job\*](#list_sagemaker-resource-hyper-parameter-tuning-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeImage.html)  **
  - **Description:** Grants permission to return information about a SageMaker Image
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeImageVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeImageVersion.html)  **
  - **Description:** Grants permission to return information about a SageMaker ImageVersion
  - **Resource types (\*required):** [image-version\*](#list_sagemaker-resource-image-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInferenceComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceComponent.html)  **
  - **Description:** Grants permission to return the description of an inference component
  - **Resource types (\*required):** [inference-component\*](#list_sagemaker-resource-inference-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html)  **
  - **Description:** Grants permission to get information about an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInferenceRecommendationsJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceRecommendationsJob.html)  **
  - **Description:** Grants permission to get information about an inference recommendations job
  - **Resource types (\*required):** [inference-recommendations-job\*](#list_sagemaker-resource-inference-recommendations-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeJob.html)  **
  - **Description:** Grants permission to return information about a SageMaker model customization job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobSchemaVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeJobSchemaVersion.html)  **
  - **Description:** Grants permission to return information about a job schema version for a particular JobCategory for the CreateJob API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeLabelingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeLabelingJob.html)  **
  - **Description:** Grants permission to return information about a labeling job
  - **Resource types (\*required):** [labeling-job\*](#list_sagemaker-resource-labeling-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLineageGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeLineageGroup.html)  **
  - **Description:** Grants permission to describe a lineage group
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMlflowApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMlflowApp.html)  **
  - **Description:** Grants permission to get information about an MLflow app
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMlflowTrackingServer.html)  **
  - **Description:** Grants permission to get information about an MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModel.html)  **
  - **Description:** Grants permission to describe a model that you created using the CreateModel API
  - **Resource types (\*required):** [model\*](#list_sagemaker-resource-model)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelBiasJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelBiasJobDefinition.html)  **
  - **Description:** Grants permission to return information about a model bias job definition
  - **Resource types (\*required):** [model-bias-job-definition\*](#list_sagemaker-resource-model-bias-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCard.html)  **
  - **Description:** Grants permission to get information about a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelCardExportJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelCardExportJob.html)  **
  - **Description:** Grants permission to get information about a model card export job
  - **Resource types (\*required):** [model-card-export-job\*](#list_sagemaker-resource-model-card-export-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelExplainabilityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelExplainabilityJobDefinition.html)  **
  - **Description:** Grants permission to return information about a model explainability job definition
  - **Resource types (\*required):** [model-explainability-job-definition\*](#list_sagemaker-resource-model-explainability-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackage.html)  **
  - **Description:** Grants permission to describe a ModelPackage
  - **Resource types (\*required):** [model-package\*](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelPackageGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelPackageGroup.html)  **
  - **Description:** Grants permission to describe a ModelPackageGroup
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeModelQualityJobDefinition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeModelQualityJobDefinition.html)  **
  - **Description:** Grants permission to return information about a model quality job definition
  - **Resource types (\*required):** [model-quality-job-definition\*](#list_sagemaker-resource-model-quality-job-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeMonitoringSchedule.html)  **
  - **Description:** Grants permission to return information about a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeNotebookInstance.html)  **
  - **Description:** Grants permission to return information about a notebook instance
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeNotebookInstanceLifecycleConfig.html)  **
  - **Description:** Grants permission to describe a notebook instance lifecycle configuration that was created via the CreateNotebookInstanceLifecycleConfig API
  - **Resource types (\*required):** [notebook-instance-lifecycle-config\*](#list_sagemaker-resource-notebook-instance-lifecycle-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOptimizationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeOptimizationJob.html)  **
  - **Description:** Grants permission to return information about an optimization job
  - **Resource types (\*required):** [optimization-job\*](#list_sagemaker-resource-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePartnerApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePartnerApp.html)  **
  - **Description:** Grants permission to describe an Amazon SageMaker Partner AI App
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipeline.html)  **
  - **Description:** Grants permission to get information about a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:PipelineVersionId](#list_sagemaker-sagemaker_PipelineVersionId)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePipelineDefinitionForExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipelineDefinitionForExecution.html)  **
  - **Description:** Grants permission to get the pipeline definition for a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipelineExecution.html)  **
  - **Description:** Grants permission to get information about a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProcessingJob.html)  **
  - **Description:** Grants permission to return information about a processing job
  - **Resource types (\*required):** [processing-job\*](#list_sagemaker-resource-processing-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProject.html)  **
  - **Description:** Grants permission to describe a project
  - **Resource types (\*required):** [project\*](#list_sagemaker-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeReservedCapacity](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeReservedCapacity.html)  **
  - **Description:** Grants permission to return information about a specified Reserved Capacity
  - **Resource types (\*required):** [reserved-capacity\*](#list_sagemaker-resource-reserved-capacity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeSpace.html)  **
  - **Description:** Grants permission to describe a Space
  - **Resource types (\*required):** [space\*](#list_sagemaker-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStudioLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeStudioLifecycleConfig.html)  **
  - **Description:** Grants permission to describe a Studio Lifecycle Configuration
  - **Resource types (\*required):** [studio-lifecycle-config\*](#list_sagemaker-resource-studio-lifecycle-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSubscribedWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeSubscribedWorkteam.html)  **
  - **Description:** Grants permission to return information about a subscribed workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html)  **
  - **Description:** Grants permission to return information about a training job
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlan.html)  **
  - **Description:** Grants permission to return information about a specified training plan
  - **Resource types (\*required):** [training-plan\*](#list_sagemaker-resource-training-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrainingPlanExtensionHistory](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingPlanExtensionHistory.html)  **
  - **Description:** Grants permission to retrieve the extension history for a specified training plan
  - **Resource types (\*required):** [training-plan\*](#list_sagemaker-resource-training-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTransformJob.html)  **
  - **Description:** Grants permission to return information about a transform job
  - **Resource types (\*required):** [transform-job\*](#list_sagemaker-resource-transform-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrial.html)  **
  - **Description:** Grants permission to return information about a trial
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html)  **
  - **Description:** Grants permission to return information about a trial component
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeUserProfile.html)  **
  - **Description:** Grants permission to describe a UserProfile
  - **Resource types (\*required):** [user-profile\*](#list_sagemaker-resource-user-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkforce.html)  **
  - **Description:** Grants permission to return information about a workforce
  - **Resource types (\*required):** [workforce\*](#list_sagemaker-resource-workforce)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeWorkteam.html)  **
  - **Description:** Grants permission to return information about a workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetachClusterNodeVolume](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DetachClusterNodeVolume.html)  **
  - **Description:** Grants permission to detach an Amazon EBS volume from a SageMaker HyperPod cluster node
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableSagemakerServicecatalogPortfolio](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisableSagemakerServicecatalogPortfolio.html)  **
  - **Description:** Grants permission to disable a SageMaker Service Catalog Portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DisassociateTrialComponent.html)  **
  - **Description:** Grants permission to disassociate a trial component from a trial
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [processing-job\*](#list_sagemaker-resource-processing-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableSagemakerServicecatalogPortfolio](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EnableSagemakerServicecatalogPortfolio.html)  **
  - **Description:** Grants permission to enable a SageMaker Service Catalog Portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ExtendTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ExtendTrainingPlan.html)  **
  - **Description:** Grants permission to extend an existing training plan by purchasing an extension offering
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetDeployments](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_GetDeployments.html)  **
  - **Description:** Grants permission to get deployment plan for device
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceFleetReport](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetDeviceFleetReport.html)  **
  - **Description:** Grants permission to access a summary of the devices in a device fleet
  - **Resource types (\*required):** [device-fleet\*](#list_sagemaker-resource-device-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeviceRegistration](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_GetDeviceRegistration.html)  **
  - **Description:** Grants permission to get device registration. After you deploy a model onto edge devices this api is used to get current device registration
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLineageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetLineageGroupPolicy.html)  **
  - **Description:** Grants permission to retreive a lineage group policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetModelPackageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetModelPackageGroupPolicy.html)  **
  - **Description:** Grants permission to get a ModelPackageGroup policy
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html)  **
  - **Description:** Grants permission to get a record from a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSagemakerServicecatalogPortfolioStatus](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetSagemakerServicecatalogPortfolioStatus.html)  **
  - **Description:** Grants permission to get a SageMaker Service Catalog Portfolio
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetScalingConfigurationRecommendation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetScalingConfigurationRecommendation.html)  **
  - **Description:** Grants permission to get a scaling policy configuration recommendation
  - **Resource types (\*required):** [inference-recommendations-job\*](#list_sagemaker-resource-inference-recommendations-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSearchSuggestions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetSearchSuggestions.html)  **
  - **Description:** Grants permission to get search suggestions when provided with a keyword
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportHubContent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImportHubContent.html)  **
  - **Description:** Grants permission to import hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html)  **
  - **Description:** Grants permission to invoke an endpoint. After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TargetModel](#list_sagemaker-sagemaker_TargetModel)
  - **Resource types (\*required):** [inference-component](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:TargetModel](#list_sagemaker-sagemaker_TargetModel)
  - **Access level:** Read

- **   [InvokeEndpointAsync](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointAsync.html)  **
  - **Description:** Grants permission to get inferences from the hosted model at the specified endpoint in an asynchronous manner
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeEndpointWithResponseStream](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.html)  **
  - **Description:** Grants permission to get the inference response as a stream from the specified endpoint
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-component](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAIBenchmarkJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAIBenchmarkJobs.html)  **
  - **Description:** Grants permission to list AI benchmark jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAIRecommendationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAIRecommendationJobs.html)  **
  - **Description:** Grants permission to list AI recommendation jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAIWorkloadConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAIWorkloadConfigs.html)  **
  - **Description:** Grants permission to list AI workload configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListActions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListActions.html)  **
  - **Description:** Grants permission to list actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAlgorithms](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAlgorithms.html)  **
  - **Description:** Grants permission to list Algorithms
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAliases](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAliases.html)  **
  - **Description:** Grants permission to list Aliases that belong to a SageMaker Image or Sagemaker ImageVersion
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image-version\*](#list_sagemaker-resource-image-version) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAppImageConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAppImageConfigs.html)  **
  - **Description:** Grants permission to list the AppImageConfigs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListApps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListApps.html)  **
  - **Description:** Grants permission to list the Apps in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListArtifacts](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListArtifacts.html)  **
  - **Description:** Grants permission to list artifacts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssociations](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAssociations.html)  **
  - **Description:** Grants permission to list associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutoMLJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAutoMLJobs.html)  **
  - **Description:** Grants permission to list AutoML jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCandidatesForAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCandidatesForAutoMLJob.html)  **
  - **Description:** Grants permission to lists candidates for an AutoML job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusterEvents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterEvents.html)  **
  - **Description:** Grants permission to list events within a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusterNodes](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterNodes.html)  **
  - **Description:** Grants permission to list nodes within a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClusterSchedulerConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterSchedulerConfigs.html)  **
  - **Description:** Grants permission to list cluster scheduler configs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusters.html)  **
  - **Description:** Grants permission to list SageMaker HyperPod clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeRepositories](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCodeRepositories.html)  **
  - **Description:** Grants permission to list code repositories
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCompilationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCompilationJobs.html)  **
  - **Description:** Grants permission to list compilation jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComputeQuotas](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListComputeQuotas.html)  **
  - **Description:** Grants permission to list compute quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContexts](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListContexts.html)  **
  - **Description:** Grants permission to list contexts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDataQualityJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDataQualityJobDefinitions.html)  **
  - **Description:** Grants permission to list data quality job definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeviceFleets](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDeviceFleets.html)  **
  - **Description:** Grants permission to list device fleets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDevices](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDevices.html)  **
  - **Description:** Grants permission to list devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list the Domains in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEdgeDeploymentPlans](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEdgeDeploymentPlans.html)  **
  - **Description:** Grants permission to list edge deployment plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEdgePackagingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEdgePackagingJobs.html)  **
  - **Description:** Grants permission to list edge packaging jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEndpointConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpointConfigs.html)  **
  - **Description:** Grants permission to list endpoint configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEndpoints](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListEndpoints.html)  **
  - **Description:** Grants permission to list endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExperiments](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListExperiments.html)  **
  - **Description:** Grants permission to list experiments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFeatureGroups](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFeatureGroups.html)  **
  - **Description:** Grants permission to list feature groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFlowDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFlowDefinitions.html)  **
  - **Description:** Grants permission to return summary information about flow definitions, given the specified parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHubContentVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubContentVersions.html)  **
  - **Description:** Grants permission to list all versions of hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListHubContents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubContents.html)  **
  - **Description:** Grants permission to list newest versions of hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListHubs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHubs.html)  **
  - **Description:** Grants permission to list hubs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHumanLoops](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanLoops.html)  **
  - **Description:** Grants permission to return summary information about human loops, given the specified parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHumanTaskUis](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHumanTaskUis.html)  **
  - **Description:** Grants permission to return summary information about human review workflow user interfaces, given the specified parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHyperParameterTuningJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListHyperParameterTuningJobs.html)  **
  - **Description:** Grants permission to list hyper parameter tuning jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImageVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListImageVersions.html)  **
  - **Description:** Grants permission to list ImageVersions that belong to a SageMaker Image
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImages](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListImages.html)  **
  - **Description:** Grants permission to list SageMaker Images in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceComponents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceComponents.html)  **
  - **Description:** Grants permission to list inference components
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceExperiments](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceExperiments.html)  **
  - **Description:** Grants permission to list inference experiments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceRecommendationsJobSteps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobSteps.html)  **
  - **Description:** Grants permission to list inference recommendations job steps
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInferenceRecommendationsJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListInferenceRecommendationsJobs.html)  **
  - **Description:** Grants permission to list inference recommendations jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobSchemaVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListJobSchemaVersions.html)  **
  - **Description:** Grants permission to list job schema versions for a particular JobCategory for the CreateJob API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListJobs.html)  **
  - **Description:** Grants permission to list SageMaker model customization jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLabelingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLabelingJobs.html)  **
  - **Description:** Grants permission to list labeling jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLabelingJobsForWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLabelingJobs.html)  **
  - **Description:** Grants permission to list labeling jobs for workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLineageGroups](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListLineageGroups.html)  **
  - **Description:** Grants permission to list lineage groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMlflowApps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMlflowApps.html)  **
  - **Description:** Grants permission to list SageMaker MLflow Apps in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMlflowTrackingServers](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMlflowTrackingServers.html)  **
  - **Description:** Grants permission to list MLflow tracking servers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelBiasJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelBiasJobDefinitions.html)  **
  - **Description:** Grants permission to list model bias job definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelCardExportJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCardExportJobs.html)  **
  - **Description:** Grants permission to list export jobs for a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModelCardVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCardVersions.html)  **
  - **Description:** Grants permission to list versions of a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModelCards](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelCards.html)  **
  - **Description:** Grants permission to list model cards
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelExplainabilityJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelExplainabilityJobDefinitions.html)  **
  - **Description:** Grants permission to list model explainability job definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelMetadata](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelMetadata.html)  **
  - **Description:** Grants permission to list model metadata for inference recommendations jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelPackageGroups](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelPackageGroups.html)  **
  - **Description:** Grants permission to list ModelPackageGroups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModelPackages](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelPackages.html)  **
  - **Description:** Grants permission to list ModelPackages
  - **Resource types (\*required):** [model-package](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModelQualityJobDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModelQualityJobDefinitions.html)  **
  - **Description:** Grants permission to list model quality job definitions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListModels.html)  **
  - **Description:** Grants permission to list the models created with the CreateModel API
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitoringAlertHistory](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringHistory.html)  **
  - **Description:** Grants permission to list the history of a monitoring alert
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitoringAlerts](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringAlerts.html)  **
  - **Description:** Grants permission to list monitoring alerts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitoringExecutions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringExecutions.html)  **
  - **Description:** Grants permission to list monitoring executions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMonitoringSchedules](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMonitoringSchedules.html)  **
  - **Description:** Grants permission to list monitoring schedules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotebookInstanceLifecycleConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListNotebookInstanceLifecycleConfigs.html)  **
  - **Description:** Grants permission to list the notebook instance lifecycle configurations that can be deployed using Amazon SageMaker
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotebookInstances](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListNotebookInstances.html)  **
  - **Description:** Grants permission to list the Amazon SageMaker notebook instances in the requester's account in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOptimizationJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListOptimizationJobs.html)  **
  - **Description:** Grants permission to list optimization jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPartnerApps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPartnerApps.html)  **
  - **Description:** Grants permission to list the Amazon SageMaker Partner AI Apps in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPipelineExecutionSteps](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineExecutionSteps.html)  **
  - **Description:** Grants permission to list steps for a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelineExecutions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineExecutions.html)  **
  - **Description:** Grants permission to list executions for a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelineParametersForExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineParametersForExecution.html)  **
  - **Description:** Grants permission to list parameters for a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelineVersions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineVersions.html)  **
  - **Description:** Grants permission to list versions of a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelines.html)  **
  - **Description:** Grants permission to list pipelines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProcessingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListProcessingJobs.html)  **
  - **Description:** Grants permission to list processing jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProjects](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list Projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecords](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_ListRecords.html)  **
  - **Description:** Grants permission to list record identifiers from a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourceCatalogs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListResourceCatalogs.html)  **
  - **Description:** Grants permission to list resource catalogs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSpaces](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListSpaces.html)  **
  - **Description:** Grants permission to list the Spaces in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStageDevices](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListStageDevices.html)  **
  - **Description:** Grants permission to list stage devices
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStudioLifecycleConfigs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListStudioLifecycleConfigs.html)  **
  - **Description:** Grants permission to list the Studio Lifecycle Configurations that can be deployed using Amazon SageMaker
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscribedWorkteams](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListSubscribedWorkteams.html)  **
  - **Description:** Grants permission to list subscribed workteams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to list the tag set associated with the specified resource
  - **Resource types (\*required):** [action](#list_sagemaker-resource-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-benchmark-job](#list_sagemaker-resource-ai-benchmark-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-recommendation-job](#list_sagemaker-resource-ai-recommendation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ai-workload-config](#list_sagemaker-resource-ai-workload-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [algorithm](#list_sagemaker-resource-algorithm) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app](#list_sagemaker-resource-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [app-image-config](#list_sagemaker-resource-app-image-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [artifact](#list_sagemaker-resource-artifact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [automl-job](#list_sagemaker-resource-automl-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [cluster-scheduler-config](#list_sagemaker-resource-cluster-scheduler-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [code-repository](#list_sagemaker-resource-code-repository) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [compilation-job](#list_sagemaker-resource-compilation-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [compute-quota](#list_sagemaker-resource-compute-quota) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [context](#list_sagemaker-resource-context) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [data-quality-job-definition](#list_sagemaker-resource-data-quality-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device](#list_sagemaker-resource-device) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [device-fleet](#list_sagemaker-resource-device-fleet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domain](#list_sagemaker-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [edge-deployment-plan](#list_sagemaker-resource-edge-deployment-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [edge-packaging-job](#list_sagemaker-resource-edge-packaging-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint-config](#list_sagemaker-resource-endpoint-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment](#list_sagemaker-resource-experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial](#list_sagemaker-resource-experiment-trial) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experiment-trial-component](#list_sagemaker-resource-experiment-trial-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [feature-group](#list_sagemaker-resource-feature-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flow-definition](#list_sagemaker-resource-flow-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [human-task-ui](#list_sagemaker-resource-human-task-ui) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hyper-parameter-tuning-job](#list_sagemaker-resource-hyper-parameter-tuning-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image](#list_sagemaker-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-component](#list_sagemaker-resource-inference-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [inference-recommendations-job](#list_sagemaker-resource-inference-recommendations-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job](#list_sagemaker-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [labeling-job](#list_sagemaker-resource-labeling-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mlflow-app](#list_sagemaker-resource-mlflow-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [mlflow-tracking-server](#list_sagemaker-resource-mlflow-tracking-server) / **Condition keys:**  
  - **Resource types (\*required):** [model](#list_sagemaker-resource-model) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-bias-job-definition](#list_sagemaker-resource-model-bias-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-card](#list_sagemaker-resource-model-card) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-explainability-job-definition](#list_sagemaker-resource-model-explainability-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-package](#list_sagemaker-resource-model-package) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-package-group](#list_sagemaker-resource-model-package-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [model-quality-job-definition](#list_sagemaker-resource-model-quality-job-definition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [monitoring-schedule](#list_sagemaker-resource-monitoring-schedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-instance](#list_sagemaker-resource-notebook-instance) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [notebook-instance-lifecycle-config](#list_sagemaker-resource-notebook-instance-lifecycle-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [optimization-job](#list_sagemaker-resource-optimization-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [partner-app](#list_sagemaker-resource-partner-app) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_sagemaker-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline-execution](#list_sagemaker-resource-pipeline-execution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [processing-job](#list_sagemaker-resource-processing-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_sagemaker-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [space](#list_sagemaker-resource-space) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [studio-lifecycle-config](#list_sagemaker-resource-studio-lifecycle-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-job](#list_sagemaker-resource-training-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [transform-job](#list_sagemaker-resource-transform-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user-profile](#list_sagemaker-resource-user-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workteam](#list_sagemaker-resource-workteam) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTrainingJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingJobs.html)  **
  - **Description:** Grants permission to list training jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrainingJobsForHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingJobsForHyperParameterTuningJob.html)  **
  - **Description:** Grants permission to list training jobs for a hyper parameter tuning job
  - **Resource types (\*required):** [hyper-parameter-tuning-job\*](#list_sagemaker-resource-hyper-parameter-tuning-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTrainingPlans](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingPlans.html)  **
  - **Description:** Grants permission to list all the training plans that have been created in a specified account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTransformJobs](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTransformJobs.html)  **
  - **Description:** Grants permission to list transform jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrialComponents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrialComponents.html)  **
  - **Description:** Grants permission to list trial components
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrials](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrials.html)  **
  - **Description:** Grants permission to list trials
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUltraServersByReservedCapacity](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListUltraServersByReservedCapacity.html)  **
  - **Description:** Grants permission to list all UltraServers in a specified Reserved Capacity
  - **Resource types (\*required):** [reserved-capacity\*](#list_sagemaker-resource-reserved-capacity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUserProfiles](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListUserProfiles.html)  **
  - **Description:** Grants permission to list the UserProfiles in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkforces](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListWorkforces.html)  **
  - **Description:** Grants permission to list workforces
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkteams](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListWorkteams.html)  **
  - **Description:** Grants permission to list workteams
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutLineageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to put a lineage group policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutModelPackageGroupPolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PutModelPackageGroupPolicy.html)  **
  - **Description:** Grants permission to put a ModelPackageGroup policy
  - **Resource types (\*required):** [model-package-group\*](#list_sagemaker-resource-model-package-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_PutRecord.html)  **
  - **Description:** Grants permission to put a record to a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:IsUpdateRecord](#list_sagemaker-sagemaker_IsUpdateRecord)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:UpdatableFeatures](#list_sagemaker-sagemaker_UpdatableFeatures)
  - **Access level:** Write

- **   [QueryLineage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_QueryLineage.html)  **
  - **Description:** Grants permission to explore the lineage graph
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RegisterDevices](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RegisterDevices.html)  **
  - **Description:** Grants permission to register a set of devices
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RenderUiTemplate](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RenderUiTemplate.html)  **
  - **Description:** Grants permission to render a UI template used for a human annotation task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RetryPipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RetryPipelineExecution.html)  **
  - **Description:** Grants permission to retry a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Sample](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Sample.html)  **
  - **Description:** Grants permission to invoke a sample request against a job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SampleWithResponseStream](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SampleWithResponseStream.html)  **
  - **Description:** Grants permission to invoke a streaming sample request against a job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html)  **
  - **Description:** Grants permission to search for SageMaker objects
  - **Resource types (\*required):** 
  - **Condition keys:** [sagemaker:SearchVisibilityCondition/${FilterKey}](#list_sagemaker-sagemaker_SearchVisibilityCondition___FilterKey_)
  - **Access level:** Read

- **   [SearchTrainingPlanOfferings](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchTrainingPlanOfferings.html)  **
  - **Description:** Grants permissions to search for the available training plan offerings that best match specified capacity requirements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendHeartbeat](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_edge_SendHeartbeat.html)  **
  - **Description:** Grants permission to publish heartbeat data from devices. After you deploy a model onto edge devices this api is used to report device status
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendPipelineExecutionStepFailure](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SendPipelineExecutionStepFailure.html)  **
  - **Description:** Grants permission to fail a pending callback step
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendPipelineExecutionStepSuccess](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SendPipelineExecutionStepSuccess.html)  **
  - **Description:** Grants permission to succeed a pending callback step
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartClusterHealthCheck](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartClusterHealthCheck.html)  **
  - **Description:** Grants permission to start deep health checks for a SageMaker Hyperpod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartEdgeDeploymentStage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartEdgeDeploymentStage.html)  **
  - **Description:** Grants permission to start an edge deployment stage
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartHumanLoop](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartHumanLoop.html)  **
  - **Description:** Grants permission to start a human loop
  - **Resource types (\*required):** [flow-definition\*](#list_sagemaker-resource-flow-definition)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartInferenceExperiment.html)  **
  - **Description:** Grants permission to start an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartMlflowTrackingServer.html)  **
  - **Description:** Grants permission to start an MLfLow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartMonitoringSchedule.html)  **
  - **Description:** Grants permission to start a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartNotebookInstance.html)  **
  - **Description:** Grants permission to start a notebook instance. This launches an EC2 instance with the latest version of the libraries and attaches your EBS volume
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html)  **
  - **Description:** Grants permission to start a pipeline execution
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:PipelineVersionId](#list_sagemaker-sagemaker_PipelineVersionId)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartSession.html)  **
  - **Description:** Grants permission to start a remote session for a SageMaker space
  - **Resource types (\*required):** [space\*](#list_sagemaker-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAIBenchmarkJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAIBenchmarkJob.html)  **
  - **Description:** Grants permission to stop an AI benchmark job
  - **Resource types (\*required):** [ai-benchmark-job\*](#list_sagemaker-resource-ai-benchmark-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAIRecommendationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAIRecommendationJob.html)  **
  - **Description:** Grants permission to stop an AI recommendation job
  - **Resource types (\*required):** [ai-recommendation-job\*](#list_sagemaker-resource-ai-recommendation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAutoMLJob.html)  **
  - **Description:** Grants permission to stop a running AutoML job
  - **Resource types (\*required):** [automl-job\*](#list_sagemaker-resource-automl-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopCompilationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopCompilationJob.html)  **
  - **Description:** Grants permission to stop a compilation job
  - **Resource types (\*required):** [compilation-job\*](#list_sagemaker-resource-compilation-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEdgeDeploymentStage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopEdgeDeploymentStage.html)  **
  - **Description:** Grants permission to stop an edge deployment stage
  - **Resource types (\*required):** [edge-deployment-plan\*](#list_sagemaker-resource-edge-deployment-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEdgePackagingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopEdgePackagingJob.html)  **
  - **Description:** Grants permission to stop an edge packaging job
  - **Resource types (\*required):** [edge-packaging-job\*](#list_sagemaker-resource-edge-packaging-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopHumanLoop](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopHumanLoop.html)  **
  - **Description:** Grants permission to stop a specified human loop
  - **Resource types (\*required):** [human-loop\*](#list_sagemaker-resource-human-loop)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopHyperParameterTuningJob.html)  **
  - **Description:** Grants permission to stop a running hyper parameter tuning job create via the CreateHyperParameterTuningJob
  - **Resource types (\*required):** [hyper-parameter-tuning-job\*](#list_sagemaker-resource-hyper-parameter-tuning-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html)  **
  - **Description:** Grants permission to stop an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopInferenceRecommendationsJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceRecommendationsJob.html)  **
  - **Description:** Grants permission to stop an inference recommendations job
  - **Resource types (\*required):** [inference-recommendations-job\*](#list_sagemaker-resource-inference-recommendations-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopJob.html)  **
  - **Description:** Grants permission to stop a SageMaker model customization job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopLabelingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopLabelingJob.html)  **
  - **Description:** Grants permission to stop a labeling job. Any labels already generated will be exported before stopping
  - **Resource types (\*required):** [labeling-job\*](#list_sagemaker-resource-labeling-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopMlflowTrackingServer.html)  **
  - **Description:** Grants permission to stop an MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopMonitoringSchedule.html)  **
  - **Description:** Grants permission to stop a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopNotebookInstance.html)  **
  - **Description:** Grants permission to stop a notebook instance. This terminates the EC2 instance. Before terminating the instance, Amazon SageMaker disconnects the EBS volume from it. Amazon SageMaker preserves the EBS volume
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopOptimizationJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopOptimizationJob.html)  **
  - **Description:** Grants permission to stop an optimization job
  - **Resource types (\*required):** [optimization-job\*](#list_sagemaker-resource-optimization-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopPipelineExecution.html)  **
  - **Description:** Grants permission to stop a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopProcessingJob.html)  **
  - **Description:** Grants permission to stop a processing job. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds
  - **Resource types (\*required):** [processing-job\*](#list_sagemaker-resource-processing-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopTrainingJob.html)  **
  - **Description:** Grants permission to stop a training job. To stop a job, Amazon SageMaker sends the algorithm the SIGTERM signal, which delays job termination for 120 seconds
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopTransformJob.html)  **
  - **Description:** Grants permission to stop a transform job. When Amazon SageMaker receives a StopTransformJob request, the status of the job changes to Stopping. After Amazon SageMaker stops the job, the status is set to Stopped
  - **Resource types (\*required):** [transform-job\*](#list_sagemaker-resource-transform-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TrainHubModel](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-admin-guide.html)  **
  - **Description:** Grants permission to train a model in hub
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAction](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateAction.html)  **
  - **Description:** Grants permission to update an action
  - **Resource types (\*required):** [action\*](#list_sagemaker-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAppImageConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateAppImageConfig.html)  **
  - **Description:** Grants permission to update an AppImageConfig
  - **Resource types (\*required):** [app-image-config\*](#list_sagemaker-resource-app-image-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateArtifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateArtifact.html)  **
  - **Description:** Grants permission to update an artifact
  - **Resource types (\*required):** [artifact\*](#list_sagemaker-resource-artifact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCluster](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCluster.html)  **
  - **Description:** Grants permission to update a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [reserved-capacity](#list_sagemaker-resource-reserved-capacity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Resource types (\*required):** [training-plan](#list_sagemaker-resource-training-plan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [UpdateClusterSchedulerConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSchedulerConfig.html)  **
  - **Description:** Grants permission to update a cluster scheduler config
  - **Resource types (\*required):** [cluster-scheduler-config\*](#list_sagemaker-resource-cluster-scheduler-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateClusterSoftware](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html)  **
  - **Description:** Grants permission to update platform software for a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCodeRepository](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCodeRepository.html)  **
  - **Description:** Grants permission to update a CodeRepository
  - **Resource types (\*required):** [code-repository\*](#list_sagemaker-resource-code-repository)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateComputeQuota](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateComputeQuota.html)  **
  - **Description:** Grants permission to update a compute quota
  - **Resource types (\*required):** [compute-quota\*](#list_sagemaker-resource-compute-quota)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContext](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateContext.html)  **
  - **Description:** Grants permission to update a context
  - **Resource types (\*required):** [context\*](#list_sagemaker-resource-context)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeviceFleet](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDeviceFleet.html)  **
  - **Description:** Grants permission to update a device fleet
  - **Resource types (\*required):** [device-fleet\*](#list_sagemaker-resource-device-fleet)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDevices](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDevices.html)  **
  - **Description:** Grants permission to update a set of devices
  - **Resource types (\*required):** [device\*](#list_sagemaker-resource-device)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateDomain.html)  **
  - **Description:** Grants permission to update a Domain
  - **Resource types (\*required):** [domain\*](#list_sagemaker-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:AppNetworkAccessType](#list_sagemaker-sagemaker_AppNetworkAccessType)<br />[sagemaker:DomainSharingOutputKmsKeyArn](#list_sagemaker-sagemaker_DomainSharingOutputKmsKeyArn)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [UpdateEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html)  **
  - **Description:** Grants permission to update an endpoint to use the endpoint configuration specified in the request
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [endpoint-config\*](#list_sagemaker-resource-endpoint-config) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEndpointWeightsAndCapacities](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpointWeightsAndCapacities.html)  **
  - **Description:** Grants permission to update variant weight, capacity, or both of one or more variants associated with an endpoint
  - **Resource types (\*required):** [endpoint\*](#list_sagemaker-resource-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateExperiment.html)  **
  - **Description:** Grants permission to update an experiment
  - **Resource types (\*required):** [experiment\*](#list_sagemaker-resource-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFeatureGroup](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureGroup.html)  **
  - **Description:** Grants permission to update a feature group
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFeatureMetadata](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureMetadata.html)  **
  - **Description:** Grants permission to update a feature metadata
  - **Resource types (\*required):** [feature-group\*](#list_sagemaker-resource-feature-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHub](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHub.html)  **
  - **Description:** Grants permission to update hubs
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHubContent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHubContent.html)  **
  - **Description:** Grants permission to update hub content
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateHubContentReference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateHubContentReference.html)  **
  - **Description:** Grants permission to update hub content reference
  - **Resource types (\*required):** [hub\*](#list_sagemaker-resource-hub) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hub-content\*](#list_sagemaker-resource-hub-content) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateImage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateImage.html)  **
  - **Description:** Grants permission to update the properties of a SageMaker Image
  - **Resource types (\*required):** [image\*](#list_sagemaker-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateImageVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateImageVersion.html)  **
  - **Description:** Grants permission to update the properties of a SageMaker ImageVersion
  - **Resource types (\*required):** [image-version\*](#list_sagemaker-resource-image-version)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInferenceComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceComponent.html)  **
  - **Description:** Grants permission to update an inference component to use the specification and configurations specified in the request
  - **Resource types (\*required):** [inference-component\*](#list_sagemaker-resource-inference-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInferenceComponentRuntimeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceComponentRuntimeConfig.html)  **
  - **Description:** Grants permission to update the runtime config of a given inference component
  - **Resource types (\*required):** [inference-component\*](#list_sagemaker-resource-inference-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInferenceExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateInferenceExperiment.html)  **
  - **Description:** Grants permission to update an inference experiment
  - **Resource types (\*required):** [inference-experiment\*](#list_sagemaker-resource-inference-experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMlflowApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowApp.html)  **
  - **Description:** Grants permission to update an MLflow app
  - **Resource types (\*required):** [mlflow-app\*](#list_sagemaker-resource-mlflow-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMlflowTrackingServer](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMlflowTrackingServer.html)  **
  - **Description:** Grants permission to update an MLflow tracking server
  - **Resource types (\*required):** [mlflow-tracking-server\*](#list_sagemaker-resource-mlflow-tracking-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModelCard](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelCard.html)  **
  - **Description:** Grants permission to update a model card
  - **Resource types (\*required):** [model-card\*](#list_sagemaker-resource-model-card)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateModelPackage.html)  **
  - **Description:** Grants permission to update a ModelPackage
  - **Resource types (\*required):** [model-package\*](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:CustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CustomerMetadataPropertiesToRemove](#list_sagemaker-sagemaker_CustomerMetadataPropertiesToRemove)<br />[sagemaker:ModelApprovalStatus](#list_sagemaker-sagemaker_ModelApprovalStatus)<br />[sagemaker:ModelLifeCycle:Stage](#list_sagemaker-sagemaker_ModelLifeCycle_Stage)<br />[sagemaker:ModelLifeCycle:StageStatus](#list_sagemaker-sagemaker_ModelLifeCycle_StageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMonitoringAlert](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMonitoringAlert.html)  **
  - **Description:** Grants permission to update a monitoring alert
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Resource types (\*required):** [monitoring-schedule-alert\*](#list_sagemaker-resource-monitoring-schedule-alert) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMonitoringSchedule](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateMonitoringSchedule.html)  **
  - **Description:** Grants permission to update a monitoring schedule
  - **Resource types (\*required):** [monitoring-schedule\*](#list_sagemaker-resource-monitoring-schedule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:InterContainerTrafficEncryption](#list_sagemaker-sagemaker_InterContainerTrafficEncryption)<br />[sagemaker:MaxRuntimeInSeconds](#list_sagemaker-sagemaker_MaxRuntimeInSeconds)<br />[sagemaker:NetworkIsolation](#list_sagemaker-sagemaker_NetworkIsolation)<br />[sagemaker:OutputKmsKeyArn](#list_sagemaker-sagemaker_OutputKmsKeyArn)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:VolumeKmsKeyArn](#list_sagemaker-sagemaker_VolumeKmsKeyArn)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)<br />[sagemaker:VpcSubnets](#list_sagemaker-sagemaker_VpcSubnets)
  - **Access level:** Write

- **   [UpdateNotebookInstance](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateNotebookInstance.html)  **
  - **Description:** Grants permission to update a notebook instance. Notebook instance updates include upgrading or downgrading the EC2 instance used for your notebook instance to accommodate changes in your workload requirements
  - **Resource types (\*required):** [notebook-instance\*](#list_sagemaker-resource-notebook-instance)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:AcceleratorTypes](#list_sagemaker-sagemaker_AcceleratorTypes)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:MinimumInstanceMetadataServiceVersion](#list_sagemaker-sagemaker_MinimumInstanceMetadataServiceVersion)<br />[sagemaker:NotebookInstanceLifecycleConfigArns](#list_sagemaker-sagemaker_NotebookInstanceLifecycleConfigArns)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:RootAccess](#list_sagemaker-sagemaker_RootAccess)
  - **Access level:** Write

- **   [UpdateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateNotebookInstanceLifecycleConfig.html)  **
  - **Description:** Grants permission to updates a notebook instance lifecycle configuration created with the CreateNotebookInstanceLifecycleConfig API
  - **Resource types (\*required):** [notebook-instance-lifecycle-config\*](#list_sagemaker-resource-notebook-instance-lifecycle-config)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePartnerApp](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePartnerApp.html)  **
  - **Description:** Grants permission to update an Amazon SageMaker Partner AI App
  - **Resource types (\*required):** [partner-app\*](#list_sagemaker-resource-partner-app)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipeline.html)  **
  - **Description:** Grants permission to update a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipelineExecution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipelineExecution.html)  **
  - **Description:** Grants permission to update a pipeline execution
  - **Resource types (\*required):** [pipeline-execution\*](#list_sagemaker-resource-pipeline-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipelineVersion](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipelineVersion.html)  **
  - **Description:** Grants permission to update a pipeline version
  - **Resource types (\*required):** [pipeline\*](#list_sagemaker-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:PipelineVersionId](#list_sagemaker-sagemaker_PipelineVersionId)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to update a Project
  - **Resource types (\*required):** [project\*](#list_sagemaker-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateReward](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateReward.html)  **
  - **Description:** Grants permission to submit reward scores for a trajectory in a job
  - **Resource types (\*required):** [job\*](#list_sagemaker-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html)  **
  - **Description:** Grants permission to update a Space
  - **Resource types (\*required):** [space\*](#list_sagemaker-resource-space)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:OwnerUserProfileArn](#list_sagemaker-sagemaker_OwnerUserProfileArn)<br />[sagemaker:RemoteAccess](#list_sagemaker-sagemaker_RemoteAccess)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:SpaceSharingType](#list_sagemaker-sagemaker_SpaceSharingType)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)
  - **Access level:** Write

- **   [UpdateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrainingJob.html)  **
  - **Description:** Grants permission to update a training job
  - **Resource types (\*required):** [training-job\*](#list_sagemaker-resource-training-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:EnableRemoteDebug](#list_sagemaker-sagemaker_EnableRemoteDebug)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:KeepAlivePeriod](#list_sagemaker-sagemaker_KeepAlivePeriod)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrial.html)  **
  - **Description:** Grants permission to update a trial
  - **Resource types (\*required):** [experiment-trial\*](#list_sagemaker-resource-experiment-trial)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrialComponent.html)  **
  - **Description:** Grants permission to update a trial component
  - **Resource types (\*required):** [experiment-trial-component\*](#list_sagemaker-resource-experiment-trial-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateUserProfile.html)  **
  - **Description:** Grants permission to update a UserProfile
  - **Resource types (\*required):** [user-profile\*](#list_sagemaker-resource-user-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:DomainSharingOutputKmsKeyArn](#list_sagemaker-sagemaker_DomainSharingOutputKmsKeyArn)<br />[sagemaker:ImageArns](#list_sagemaker-sagemaker_ImageArns)<br />[sagemaker:ImageVersionArns](#list_sagemaker-sagemaker_ImageVersionArns)<br />[sagemaker:InstanceTypes](#list_sagemaker-sagemaker_InstanceTypes)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)<br />[sagemaker:StudioLifecycleConfigArns](#list_sagemaker-sagemaker_StudioLifecycleConfigArns)<br />[sagemaker:VpcSecurityGroupIds](#list_sagemaker-sagemaker_VpcSecurityGroupIds)
  - **Access level:** Write

- **   [UpdateWorkforce](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkforce.html)  **
  - **Description:** Grants permission to update a workforce
  - **Resource types (\*required):** [workforce\*](#list_sagemaker-resource-workforce)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkteam](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateWorkteam.html)  **
  - **Description:** Grants permission to update a workteam
  - **Resource types (\*required):** [workteam\*](#list_sagemaker-resource-workteam)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon SageMaker
<a name="list_sagemaker-permission-only-actions"></a>

The following actions are defined by Amazon SageMaker but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AccessModelPackage](https://docs.aws.amazon.com/sagemaker/latest/APIReference/)  **
  - **Description:** Grants permission to access model package that can be used in Amazon SageMaker training or hosting services
  - **Resource types (\*required):** [model-package\*](#list_sagemaker-resource-model-package)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CallWithBearerToken](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CallWithBearerToken.html)  **
  - **Description:** Grants permission to use bearer token in SageMaker Job and Inference runtime endpoints APIs
  - **Resource types (\*required):** 
  - **Condition keys:** [sagemaker:BearerTokenType](#list_sagemaker-sagemaker_BearerTokenType)
  - **Access level:** Read

- **   [CreateReservedCapacity](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateReservedCapacity.html)  **
  - **Description:** Grants permission to create a reserved capacity
  - **Resource types (\*required):** [reserved-capacity\*](#list_sagemaker-resource-reserved-capacity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sagemaker-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sagemaker-aws_TagKeys)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSharedModel](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to create a shared model in a SageMaker Studio application
  - **Resource types (\*required):** [shared-model\*](#list_sagemaker-resource-shared-model)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants AWS Resource Access Manager permission to delete a resource policy on a SageMaker resource that supports cross-account sharing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeClusterInference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-inference.html)  **
  - **Description:** Grants permission to get information about the inference operator for a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSharedModel](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to describe a shared model in a SageMaker Studio application
  - **Resource types (\*required):** [shared-model\*](#list_sagemaker-resource-shared-model)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GetResourcePolicy.html)  **
  - **Description:** Grants AWS Resource Access Manager permission to retrieve a resource policy on a SageMaker resource that supports cross-account sharing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSharedModelEvents](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to list shared model events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSharedModelVersions](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to list shared model versions
  - **Resource types (\*required):** [shared-model\*](#list_sagemaker-resource-shared-model)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSharedModels](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to list shared models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutResourcePolicy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants AWS Resource Access Manager permission to create a resource policy on a SageMaker resource that supports cross-account sharing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendSharedModelEvent](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to send a shared model event
  - **Resource types (\*required):** [shared-model-event\*](#list_sagemaker-resource-shared-model-event)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateClusterInference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-inference.html)  **
  - **Description:** Grants permission to update the inference operator for a SageMaker HyperPod cluster
  - **Resource types (\*required):** [cluster\*](#list_sagemaker-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSharedModel](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  **
  - **Description:** Grants permission to update a shared model
  - **Resource types (\*required):** [shared-model\*](#list_sagemaker-resource-shared-model)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon SageMaker
<a name="list_sagemaker-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [action](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ActionSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:action/${ActionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [ai-benchmark-job](https://docs.aws.amazon.com/sagemaker/latest/dg/API_AIBenchmarkJob.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:ai-benchmark-job/${AIBenchmarkJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [ai-recommendation-job](https://docs.aws.amazon.com/sagemaker/latest/dg/API_AIRecommendationJob.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:ai-recommendation-job/${AIRecommendationJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [ai-workload-config](https://docs.aws.amazon.com/sagemaker/latest/dg/API_AIWorkloadConfig.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:ai-workload-config/${AIWorkloadConfigName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:algorithm/${AlgorithmName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [app](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:app/${DomainId}/${UserProfileName}/${AppType}/${AppName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [app-image-config](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi-create.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:app-image-config/${AppImageConfigName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [artifact](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ArtifactSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:artifact/${HashOfArtifactSource} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [automl-job](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:automl-job/${AutoMLJobJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-cluster.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:cluster/${ClusterId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [cluster-scheduler-config](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:cluster-scheduler-config/${ClusterSchedulerConfigId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [code-repository](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:code-repository/${CodeRepositoryName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [compilation-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:compilation-job/${CompilationJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [compute-quota](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-operate-console-ui-governance.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:compute-quota/${ComputeQuotaId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [context](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContextSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:context/${ContextName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [data-quality-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:data-quality-job-definition/${DataQualityJobDefinitionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [device](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-edge-devices.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:device-fleet/${DeviceFleetName}/device/${DeviceName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [device-fleet](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-device-fleet.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:device-fleet/${DeviceFleetName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [domain](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [edge-deployment-plan](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:edge-deployment/${EdgeDeploymentPlanName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [edge-packaging-job](https://docs.aws.amazon.com/sagemaker/latest/dg/edge-packaging-job.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:edge-packaging-job/${EdgePackagingJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:endpoint/${EndpointName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [endpoint-config](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:endpoint-config/${EndpointConfigName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [experiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Experiment.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:experiment/${ExperimentName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [experiment-trial](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Trial.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:experiment-trial/${TrialName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [experiment-trial-component](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponent.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:experiment-trial-component/${TrialComponentName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [feature-group](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:feature-group/${FeatureGroupName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [flow-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-create-flow-definition.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:flow-definition/${FlowDefinitionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [hub](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:hub/${HubName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [hub-content](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-content-sharing.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:hub-content/${HubName}/${HubContentType}/${HubContentName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [human-loop](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-start-human-loop.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:human-loop/${HumanLoopName} |   | 
|  [human-task-ui](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-instructions-overview.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:human-task-ui/${HumanTaskUiName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [hyper-parameter-tuning-job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:hyper-parameter-tuning-job/${HyperParameterTuningJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:image/${ImageName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [image-version](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:image-version/${ImageName}/${Version} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [inference-component](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:inference-component/${InferenceComponentName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [inference-experiment](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-experiment.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:inference-experiment/${InferenceExperimentName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [inference-recommendations-job](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender-recommendation-jobs.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:inference-recommendations-job/${InferenceRecommendationsJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [job](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:job/${JobCategory}/${JobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [labeling-job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:labeling-job/${LabelingJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [lineage-group](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LineageGroupSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:lineage-group/${LineageGroupName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [mlflow-app](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MlflowApp.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:mlflow-app/${MLflowAppId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [mlflow-tracking-server](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MlflowTrackingServer.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:mlflow-tracking-server/${MlflowTrackingServerName} |   | 
|  [model](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model/${ModelName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-bias-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-bias-job-definition/${ModelBiasJobDefinitionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-card](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCard.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-card/${ModelCardName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-card-export-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelCardExportJob.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-card/${ModelCardName}/export-job/${ExportJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-explainability-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-explainability-job-definition/${ModelExplainabilityJobDefinitionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-package](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelPackage.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-package/${ModelPackageName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](#list_sagemaker-sagemaker_CurrentCustomerMetadataProperties___MetadataKey_)<br />[sagemaker:CurrentModelLifeCycleStage](#list_sagemaker-sagemaker_CurrentModelLifeCycleStage)<br />[sagemaker:CurrentModelLifeCycleStageStatus](#list_sagemaker-sagemaker_CurrentModelLifeCycleStageStatus)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-package-group](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry-model-group.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-package-group/${ModelPackageGroupName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [model-quality-job-definition](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:model-quality-job-definition/${ModelQualityJobDefinitionName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [monitoring-schedule](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:monitoring-schedule/${MonitoringScheduleName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [monitoring-schedule-alert](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-scheduling.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:monitoring-schedule/${MonitoringScheduleName}/alert/${MonitoringScheduleAlertName} |   | 
|  [notebook-instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:notebook-instance/${NotebookInstanceName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [notebook-instance-lifecycle-config](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:notebook-instance-lifecycle-config/${NotebookInstanceLifecycleConfigName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [optimization-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationJobSummary.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:optimization-job/${OptimizationJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [partner-app](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:partner-app/${AppId} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [pipeline](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Pipeline.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:pipeline/${PipelineName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [pipeline-execution](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecution.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:pipeline/${PipelineName}/execution/${RandomString} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [processing-job](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:processing-job/${ProcessingJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:project/${ProjectName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [reserved-capacity](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:reserved-capacity/${RandomString} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [sagemaker-catalog](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceCatalog.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:sagemaker-catalog/${ResourceCatalogName} |   | 
|  [shared-model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:shared-model/${SharedModelId} |   | 
|  [shared-model-event](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-collaborate-permissions.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:shared-model-event/${EventId} |   | 
|  [space](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:space/${DomainId}/${SpaceName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [studio-lifecycle-config](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:studio-lifecycle-config/${StudioLifecycleConfigName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [training-job](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:training-job/${TrainingJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [training-plan](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:training-plan/${TrainingPlanName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [transform-job](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TransformJob.html.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:transform-job/${TransformJobName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [user-profile](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:user-profile/${DomainId}/${UserProfileName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:workforce/${WorkforceName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 
|  [workteam](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html)  | arn:${Partition}:sagemaker:${Region}:${Account}:workteam/${WorkteamName} | [aws:ResourceTag/${TagKey}](#list_sagemaker-aws_ResourceTag___TagKey_)<br />[sagemaker:ResourceTag/${TagKey}](#list_sagemaker-sagemaker_ResourceTag___TagKey_) | 

## Condition keys for Amazon SageMaker
<a name="list_sagemaker-policy-keys"></a>

Amazon SageMaker defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a key that is present in the request the user makes to the SageMaker service | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a tag key and value pair | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all the tag key names associated with the resource in the request | ArrayOfString | 
|   [sagemaker:AcceleratorTypes](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all accelerator types associated with the resource in the request | ArrayOfString | 
|   [sagemaker:AppNetworkAccessType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the app network access type associated with the resource in the request | String | 
|   [sagemaker:AuthMode](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the authentication mode specified in the request | String | 
|   [sagemaker:BearerTokenType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the type of bearer token used in the request | String | 
|   [sagemaker:CurrentCustomerMetadataProperties/${MetadataKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a current metadata key and value pair associated with the model-package resource | String | 
|   [sagemaker:CurrentModelLifeCycleStage](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the current value of the Stage field in the model life cycle object associated with the model-package resource | String | 
|   [sagemaker:CurrentModelLifeCycleStageStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the current value of the StageStatus field in the model life cycle object associated with the model-package resource | String | 
|   [sagemaker:CustomerMetadataProperties/${MetadataKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a metadata key and value pair | String | 
|   [sagemaker:CustomerMetadataPropertiesToRemove](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of metadata properties associated with the model-package resource in the request | ArrayOfString | 
|   [sagemaker:DirectGatedModelAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Used to deny direct access to SageMaker gated ModelReferences | String | 
|   [sagemaker:DirectInternetAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the direct internet access associated with the resource in the request | String | 
|   [sagemaker:DomainId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | You can use the domainId as a policy variable to filter requests from specific SageMaker Domains | String | 
|   [sagemaker:DomainSharingOutputKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the Domain sharing output KMS key associated with the resource in the request. This key has been deprecated. It has been replaced by sagemaker:DomainSharingOutputKmsKeyArn | ARN | 
|   [sagemaker:DomainSharingOutputKmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the Domain sharing output KMS key associated with the resource in the request. The ARN of the key-id must be used | ARN | 
|   [sagemaker:EnableRemoteDebug](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the remote debug config in the request | Bool | 
|   [sagemaker:FeatureGroupDisableGlueTableCreation](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the DisableGlueTableCreation flag associated with the feature group resource in the request | Bool | 
|   [sagemaker:FeatureGroupEnableOnlineStore](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the EnableOnlineStore flag associated with feature group in the request | Bool | 
|   [sagemaker:FeatureGroupOfflineStoreConfig](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the presence of an OfflineStoreConfig in the feature group resource in the request. This access filter only supports the null-conditional operator | Bool | 
|   [sagemaker:FeatureGroupOfflineStoreKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the offline store kms key associated with the feature group resource in the request. This key has been deprecated. It has been replaced by sagemaker:FeatureGroupOfflineStoreKmsKeyArn | ARN | 
|   [sagemaker:FeatureGroupOfflineStoreKmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the offline store kms key associated with the feature group resource in the request. The ARN of the key-id must be used | ARN | 
|   [sagemaker:FeatureGroupOfflineStoreS3Uri](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the offline store s3 uri associated with the feature group resource in the request | String | 
|   [sagemaker:FeatureGroupOnlineStoreKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the online store kms key associated with the feature group resource in the request. This key has been deprecated. It has been replaced by sagemaker:FeatureGroupOnlineStoreKmsKeyArn | ARN | 
|   [sagemaker:FeatureGroupOnlineStoreKmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the online store kms key associated with the feature group resource in the request. The ARN of the key-id must be used | ARN | 
|   [sagemaker:FileSystemAccessMode](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a file system access mode associated with the resource in the request | String | 
|   [sagemaker:FileSystemDirectoryPath](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a file system directory path associated with the resource in the request | String | 
|   [sagemaker:FileSystemId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a file system ID associated with the resource in the request | String | 
|   [sagemaker:FileSystemType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a file system type associated with the resource in the request | String | 
|   [sagemaker:HomeEfsFileSystemKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a key that is present in the request the user makes to the SageMaker service. This key has been deprecated. It has been replaced by sagemaker:VolumeKmsKeyArn | ARN | 
|   [sagemaker:ImageArns](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all image arns associated with the resource in the request | ArrayOfARN | 
|   [sagemaker:ImageVersionArns](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all image version arns associated with the resource in the request | ArrayOfARN | 
|   [sagemaker:InstanceTypes](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all instance types associated with the resource in the request | ArrayOfString | 
|   [sagemaker:InterContainerTrafficEncryption](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the inter container traffic encryption associated with the resource in the request | Bool | 
|   [sagemaker:IsUpdateRecord](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by whether the PutRecord authorization was triggered by an UpdateRecord API call. Set to true on UpdateRecord and false on direct PutRecord calls | Bool | 
|   [sagemaker:KeepAlivePeriod](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the keep-alive period associated with the resource in the request | Numeric | 
|   [sagemaker:MaxRuntimeInSeconds](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the max runtime in seconds associated with the resource in the request | Numeric | 
|   [sagemaker:MinimumInstanceMetadataServiceVersion](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the minimum instance metadata service version used by the resource in the request | String | 
|   [sagemaker:ModelApprovalStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the model approval status with the model-package in the request | String | 
|   [sagemaker:ModelArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the model arn associated with the resource in the request | ARN | 
|   [sagemaker:ModelLifeCycle:Stage](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by stage field in the model life cycle object associated with the model-package resource in the request | String | 
|   [sagemaker:ModelLifeCycle:StageStatus](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by stageStatus field in the model life cycle object associated with the model-package resource in the request | String | 
|   [sagemaker:NetworkIsolation](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the network isolation associated with the resource in the request | Bool | 
|   [sagemaker:NotebookInstanceLifecycleConfigArns](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of notebook instance lifecycle configuration ARNs associated with the resource in the request | ArrayOfARN | 
|   [sagemaker:OutputKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the output kms key associated with the resource in the request. This key has been deprecated. It has been replaced by sagemaker:OutputKmsKeyArn | ARN | 
|   [sagemaker:OutputKmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the output kms key associated with the resource in the request. The ARN of the key-id must be used | ARN | 
|   [sagemaker:OwnerUserProfileArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the OwnerUserProfile arn associated with the space in the request | ARN | 
|   [sagemaker:PipelineVersionId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access to specific version IDs of a Sagemaker pipeline | String | 
|   [sagemaker:RemoteAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the remote access flag associated with the space in the request | String | 
|   [sagemaker:ResourceTag/](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the preface string for a tag key and value pair attached to a resource | String | 
|   [sagemaker:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by a tag key and value pair | String | 
|   [sagemaker:RootAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the root access associated with the resource in the request | String | 
|   [sagemaker:SearchVisibilityCondition/${FilterKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Limits the results of your search request to the resources that you can access. ${FilterKey} is a key that the VisibilityConditions configuration presents in the Search request | String | 
|   [sagemaker:ServerlessMaxConcurrency](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by limiting maximum concurrency used for Serverless inference in the request | Numeric | 
|   [sagemaker:ServerlessMemorySize](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by limiting memory size used for Serverless inference in the request | Numeric | 
|   [sagemaker:SpaceSharingType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the sharing type associated with the space in the request | String | 
|   [sagemaker:StudioLifecycleConfigArns](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of lifecycle configuration ARNs associated with the resource in the request | ArrayOfARN | 
|   [sagemaker:TaggingAction](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the API actions to which a user can apply tags. Uses the name of the API operation that creates a taggable resource to filter access | String | 
|   [sagemaker:TargetModel](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the target model associated with the Multi-Model Endpoint in the request | String | 
|   [sagemaker:UpdatableFeatures](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of feature names being updated by an UpdateRecord API call. Absent on direct PutRecord calls | ArrayOfString | 
|   [sagemaker:UserProfileName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | You can use the UserProfileName as a policy variable to filter requests from specific user profiles within a SageMaker Domain. This context key is not applicable to user profiles within shared spaces | String | 
|   [sagemaker:VolumeKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the volume kms key associated with the resource in the request. This key has been deprecated. It has been replaced by sagemaker:VolumeKmsKeyArn | ARN | 
|   [sagemaker:VolumeKmsKeyArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the volume kms key associated with the resource in the request. The ARN of the key-id must be used | ARN | 
|   [sagemaker:VpcSecurityGroupIds](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all VPC security group ids associated with the resource in the request | ArrayOfString | 
|   [sagemaker:VpcSubnets](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the list of all VPC subnets associated with the resource in the request | ArrayOfString | 
|   [sagemaker:WorkteamArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the workteam arn associated to the request | ARN | 
|   [sagemaker:WorkteamType](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonsagemaker.html#amazonsagemaker-policy-keys)  | Filters access by the workteam type associated to the request. This can be public-crowd, private-crowd or vendor-crowd | String | 