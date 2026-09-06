

# Actions, resources, and condition keys for Amazon EC2 Image Builder
<a name="list_imagebuilder"></a>

Amazon EC2 Image Builder (service prefix: `imagebuilder`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/imagebuilder/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/imagebuilder/imagebuilder.json) for this service.

**Topics**
+ [API operations defined by Amazon EC2 Image Builder](#list_imagebuilder-operations)
+ [Actions defined by Amazon EC2 Image Builder](#list_imagebuilder-actions-as-permissions)
+ [Resource types defined by Amazon EC2 Image Builder](#list_imagebuilder-resources-for-iam-policies)
+ [Condition keys for Amazon EC2 Image Builder](#list_imagebuilder-policy-keys)

## API operations defined by Amazon EC2 Image Builder
<a name="list_imagebuilder-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_imagebuilder-actions-as-permissions).




- **   CancelImageCreation  **
  - **IAM action:**  [imagebuilder:CancelImageCreation](#list_imagebuilder-action-CancelImageCreation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelLifecycleExecution  **
  - **IAM action:**  [imagebuilder:CancelLifecycleExecution](#list_imagebuilder-action-CancelLifecycleExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComponent  **
  - **IAM action:**  [imagebuilder:CreateComponent](#list_imagebuilder-action-CreateComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateContainerRecipe  **
  - **IAM action:**  [imagebuilder:CreateContainerRecipe](#list_imagebuilder-action-CreateContainerRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:GetComponent](#list_imagebuilder-action-GetComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImage](#list_imagebuilder-action-GetImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDistributionConfiguration  **
  - **IAM action:**  [imagebuilder:CreateDistributionConfiguration](#list_imagebuilder-action-CreateDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** vmie.amazonaws.com / **Access level:** Write

- **   CreateImage  **
  - **IAM action:**  [imagebuilder:CreateImage](#list_imagebuilder-action-CreateImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:GetContainerRecipe](#list_imagebuilder-action-GetContainerRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetDistributionConfiguration](#list_imagebuilder-action-GetDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImageRecipe](#list_imagebuilder-action-GetImageRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetInfrastructureConfiguration](#list_imagebuilder-action-GetInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetWorkflow](#list_imagebuilder-action-GetWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   CreateImagePipeline  **
  - **IAM action:**  [imagebuilder:CreateImagePipeline](#list_imagebuilder-action-CreateImagePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:GetContainerRecipe](#list_imagebuilder-action-GetContainerRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetDistributionConfiguration](#list_imagebuilder-action-GetDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImageRecipe](#list_imagebuilder-action-GetImageRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetInfrastructureConfiguration](#list_imagebuilder-action-GetInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetWorkflow](#list_imagebuilder-action-GetWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   CreateImageRecipe  **
  - **IAM action:**  [imagebuilder:CreateImageRecipe](#list_imagebuilder-action-CreateImageRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:GetComponent](#list_imagebuilder-action-GetComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImage](#list_imagebuilder-action-GetImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInfrastructureConfiguration  **
  - **IAM action:**  [imagebuilder:CreateInfrastructureConfiguration](#list_imagebuilder-action-CreateInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:GetInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetInstanceProfile.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   CreateLifecyclePolicy  **
  - **IAM action:**  [imagebuilder:CreateLifecyclePolicy](#list_imagebuilder-action-CreateLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   CreateWorkflow  **
  - **IAM action:**  [imagebuilder:CreateWorkflow](#list_imagebuilder-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteComponent  **
  - **IAM action:**  [imagebuilder:DeleteComponent](#list_imagebuilder-action-DeleteComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContainerRecipe  **
  - **IAM action:**  [imagebuilder:DeleteContainerRecipe](#list_imagebuilder-action-DeleteContainerRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDistributionConfiguration  **
  - **IAM action:**  [imagebuilder:DeleteDistributionConfiguration](#list_imagebuilder-action-DeleteDistributionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImage  **
  - **IAM action:**  [imagebuilder:DeleteImage](#list_imagebuilder-action-DeleteImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImagePipeline  **
  - **IAM action:**  [imagebuilder:DeleteImagePipeline](#list_imagebuilder-action-DeleteImagePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteImageRecipe  **
  - **IAM action:**  [imagebuilder:DeleteImageRecipe](#list_imagebuilder-action-DeleteImageRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInfrastructureConfiguration  **
  - **IAM action:**  [imagebuilder:DeleteInfrastructureConfiguration](#list_imagebuilder-action-DeleteInfrastructureConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLifecyclePolicy  **
  - **IAM action:**  [imagebuilder:DeleteLifecyclePolicy](#list_imagebuilder-action-DeleteLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [imagebuilder:DeleteWorkflow](#list_imagebuilder-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DistributeImage  **
  - **IAM action:**  [imagebuilder:DistributeImage](#list_imagebuilder-action-DistributeImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:GetDistributionConfiguration](#list_imagebuilder-action-GetDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImage](#list_imagebuilder-action-GetImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   GetComponent  **
  - **IAM action:**  [imagebuilder:GetComponent](#list_imagebuilder-action-GetComponent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComponentPolicy  **
  - **IAM action:**  [imagebuilder:GetComponentPolicy](#list_imagebuilder-action-GetComponentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContainerRecipe  **
  - **IAM action:**  [imagebuilder:GetContainerRecipe](#list_imagebuilder-action-GetContainerRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContainerRecipePolicy  **
  - **IAM action:**  [imagebuilder:GetContainerRecipePolicy](#list_imagebuilder-action-GetContainerRecipePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDistributionConfiguration  **
  - **IAM action:**  [imagebuilder:GetDistributionConfiguration](#list_imagebuilder-action-GetDistributionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImage  **
  - **IAM action:**  [imagebuilder:GetImage](#list_imagebuilder-action-GetImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImagePipeline  **
  - **IAM action:**  [imagebuilder:GetImagePipeline](#list_imagebuilder-action-GetImagePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImagePolicy  **
  - **IAM action:**  [imagebuilder:GetImagePolicy](#list_imagebuilder-action-GetImagePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImageRecipe  **
  - **IAM action:**  [imagebuilder:GetImageRecipe](#list_imagebuilder-action-GetImageRecipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetImageRecipePolicy  **
  - **IAM action:**  [imagebuilder:GetImageRecipePolicy](#list_imagebuilder-action-GetImageRecipePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInfrastructureConfiguration  **
  - **IAM action:**  [imagebuilder:GetInfrastructureConfiguration](#list_imagebuilder-action-GetInfrastructureConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLifecycleExecution  **
  - **IAM action:**  [imagebuilder:GetLifecycleExecution](#list_imagebuilder-action-GetLifecycleExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLifecyclePolicy  **
  - **IAM action:**  [imagebuilder:GetLifecyclePolicy](#list_imagebuilder-action-GetLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMarketplaceResource  **
  - **IAM action:**  [imagebuilder:GetMarketplaceResource](#list_imagebuilder-action-GetMarketplaceResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [imagebuilder:GetWorkflow](#list_imagebuilder-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowExecution  **
  - **IAM action:**  [imagebuilder:GetWorkflowExecution](#list_imagebuilder-action-GetWorkflowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowStepExecution  **
  - **IAM action:**  [imagebuilder:GetWorkflowStepExecution](#list_imagebuilder-action-GetWorkflowStepExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportComponent  **
  - **IAM action:**  [imagebuilder:ImportComponent](#list_imagebuilder-action-ImportComponent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ImportDiskImage  **
  - **IAM action:**  [imagebuilder:GetInfrastructureConfiguration](#list_imagebuilder-action-GetInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:ImportDiskImage](#list_imagebuilder-action-ImportDiskImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   ImportVmImage  **
  - **IAM action:**  [imagebuilder:ImportVmImage](#list_imagebuilder-action-ImportVmImage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListComponentBuildVersions  **
  - **IAM action:**  [imagebuilder:ListComponentBuildVersions](#list_imagebuilder-action-ListComponentBuildVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComponents  **
  - **IAM action:**  [imagebuilder:ListComponents](#list_imagebuilder-action-ListComponents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContainerRecipes  **
  - **IAM action:**  [imagebuilder:ListContainerRecipes](#list_imagebuilder-action-ListContainerRecipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributionConfigurations  **
  - **IAM action:**  [imagebuilder:ListDistributionConfigurations](#list_imagebuilder-action-ListDistributionConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageBuildVersions  **
  - **IAM action:**  [imagebuilder:ListImageBuildVersions](#list_imagebuilder-action-ListImageBuildVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImagePackages  **
  - **IAM action:**  [imagebuilder:ListImagePackages](#list_imagebuilder-action-ListImagePackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImagePipelineImages  **
  - **IAM action:**  [imagebuilder:ListImagePipelineImages](#list_imagebuilder-action-ListImagePipelineImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImagePipelines  **
  - **IAM action:**  [imagebuilder:ListImagePipelines](#list_imagebuilder-action-ListImagePipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageRecipes  **
  - **IAM action:**  [imagebuilder:ListImageRecipes](#list_imagebuilder-action-ListImageRecipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageScanFindingAggregations  **
  - **IAM action:**  [imagebuilder:ListImageScanFindingAggregations](#list_imagebuilder-action-ListImageScanFindingAggregations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImageScanFindings  **
  - **IAM action:**  [imagebuilder:ListImageScanFindings](#list_imagebuilder-action-ListImageScanFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListImages  **
  - **IAM action:**  [imagebuilder:ListImages](#list_imagebuilder-action-ListImages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInfrastructureConfigurations  **
  - **IAM action:**  [imagebuilder:ListInfrastructureConfigurations](#list_imagebuilder-action-ListInfrastructureConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLifecycleExecutionResources  **
  - **IAM action:**  [imagebuilder:ListLifecycleExecutionResources](#list_imagebuilder-action-ListLifecycleExecutionResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLifecycleExecutions  **
  - **IAM action:**  [imagebuilder:ListLifecycleExecutions](#list_imagebuilder-action-ListLifecycleExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLifecyclePolicies  **
  - **IAM action:**  [imagebuilder:ListLifecyclePolicies](#list_imagebuilder-action-ListLifecyclePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [imagebuilder:ListTagsForResource](#list_imagebuilder-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWaitingWorkflowSteps  **
  - **IAM action:**  [imagebuilder:ListWaitingWorkflowSteps](#list_imagebuilder-action-ListWaitingWorkflowSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowBuildVersions  **
  - **IAM action:**  [imagebuilder:ListWorkflowBuildVersions](#list_imagebuilder-action-ListWorkflowBuildVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowExecutions  **
  - **IAM action:**  [imagebuilder:ListWorkflowExecutions](#list_imagebuilder-action-ListWorkflowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowStepExecutions  **
  - **IAM action:**  [imagebuilder:ListWorkflowStepExecutions](#list_imagebuilder-action-ListWorkflowStepExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [imagebuilder:ListWorkflows](#list_imagebuilder-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutComponentPolicy  **
  - **IAM action:**  [imagebuilder:PutComponentPolicy](#list_imagebuilder-action-PutComponentPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutContainerRecipePolicy  **
  - **IAM action:**  [imagebuilder:PutContainerRecipePolicy](#list_imagebuilder-action-PutContainerRecipePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutImagePolicy  **
  - **IAM action:**  [imagebuilder:PutImagePolicy](#list_imagebuilder-action-PutImagePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   PutImageRecipePolicy  **
  - **IAM action:**  [imagebuilder:PutImageRecipePolicy](#list_imagebuilder-action-PutImageRecipePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RetryImage  **
  - **IAM action:**  [imagebuilder:RetryImage](#list_imagebuilder-action-RetryImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendWorkflowStepAction  **
  - **IAM action:**  [imagebuilder:SendWorkflowStepAction](#list_imagebuilder-action-SendWorkflowStepAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartImagePipelineExecution  **
  - **IAM action:**  [imagebuilder:StartImagePipelineExecution](#list_imagebuilder-action-StartImagePipelineExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartResourceStateUpdate  **
  - **IAM action:**  [imagebuilder:StartResourceStateUpdate](#list_imagebuilder-action-StartResourceStateUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [imagebuilder:UntagResource](#list_imagebuilder-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDistributionConfiguration  **
  - **IAM action:**  [imagebuilder:UpdateDistributionConfiguration](#list_imagebuilder-action-UpdateDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** vmie.amazonaws.com / **Access level:** Write

- **   UpdateImagePipeline  **
  - **IAM action:**  [imagebuilder:GetContainerRecipe](#list_imagebuilder-action-GetContainerRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetDistributionConfiguration](#list_imagebuilder-action-GetDistributionConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetImageRecipe](#list_imagebuilder-action-GetImageRecipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetInfrastructureConfiguration](#list_imagebuilder-action-GetInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:GetWorkflow](#list_imagebuilder-action-GetWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [imagebuilder:TagResource](#list_imagebuilder-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [imagebuilder:UpdateImagePipeline](#list_imagebuilder-action-UpdateImagePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write

- **   UpdateInfrastructureConfiguration  **
  - **IAM action:**  [imagebuilder:UpdateInfrastructureConfiguration](#list_imagebuilder-action-UpdateInfrastructureConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:GetInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetInstanceProfile.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ec2.amazonaws.com / **Access level:** Write

- **   UpdateLifecyclePolicy  **
  - **IAM action:**  [imagebuilder:UpdateLifecyclePolicy](#list_imagebuilder-action-UpdateLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** imagebuilder.amazonaws.com / **Access level:** Write



## Actions defined by Amazon EC2 Image Builder
<a name="list_imagebuilder-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelImageCreation](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CancelImageCreation.html)  **
  - **Description:** Grants permission to cancel an image creation
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelLifecycleExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CancelLifecycleExecution.html)  **
  - **Description:** Grants permission to cancel a lifecycle execution
  - **Resource types (\*required):** [lifecycleExecution\*](#list_imagebuilder-resource-lifecycleExecution)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html)  **
  - **Description:** Grants permission to create a new component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContainerRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateContainerRecipe.html)  **
  - **Description:** Grants permission to create a new Container Recipe
  - **Resource types (\*required):** [containerRecipe\*](#list_imagebuilder-resource-containerRecipe)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDistributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateDistributionConfiguration.html)  **
  - **Description:** Grants permission to create a new distribution configuration
  - **Resource types (\*required):** [distributionConfiguration\*](#list_imagebuilder-resource-distributionConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html)  **
  - **Description:** Grants permission to create a new image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateImagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImagePipeline.html)  **
  - **Description:** Grants permission to create a new image pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateImageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImageRecipe.html)  **
  - **Description:** Grants permission to create a new Image Recipe
  - **Resource types (\*required):** [imageRecipe\*](#list_imagebuilder-resource-imageRecipe)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInfrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateInfrastructureConfiguration.html)  **
  - **Description:** Grants permission to create a new infrastructure configuration
  - **Resource types (\*required):** [infrastructureConfiguration\*](#list_imagebuilder-resource-infrastructureConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)<br />[imagebuilder:CreatedResourceTag/${TagKey}](#list_imagebuilder-imagebuilder_CreatedResourceTag___TagKey_)<br />[imagebuilder:CreatedResourceTagKeys](#list_imagebuilder-imagebuilder_CreatedResourceTagKeys)<br />[imagebuilder:Ec2MetadataHttpTokens](#list_imagebuilder-imagebuilder_Ec2MetadataHttpTokens)<br />[imagebuilder:StatusTopicArn](#list_imagebuilder-imagebuilder_StatusTopicArn)
  - **Access level:** Write

- **   [CreateLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateLifecyclePolicy.html)  **
  - **Description:** Grants permission to create a new lifecycle policy
  - **Resource types (\*required):** [lifecyclePolicy\*](#list_imagebuilder-resource-lifecyclePolicy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)<br />[imagebuilder:LifecyclePolicyResourceType](#list_imagebuilder-imagebuilder_LifecyclePolicyResourceType)
  - **Access level:** Write

- **   [CreateWorkflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateWorkflow.html)  **
  - **Description:** Grants permission to create a new workflow
  - **Resource types (\*required):** [workflow\*](#list_imagebuilder-resource-workflow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteComponent.html)  **
  - **Description:** Grants permission to delete a component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContainerRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteContainerRecipe.html)  **
  - **Description:** Grants permission to delete a container recipe
  - **Resource types (\*required):** [containerRecipe\*](#list_imagebuilder-resource-containerRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDistributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteDistributionConfiguration.html)  **
  - **Description:** Grants permission to delete a distribution configuration
  - **Resource types (\*required):** [distributionConfiguration\*](#list_imagebuilder-resource-distributionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteImage.html)  **
  - **Description:** Grants permission to delete an image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteImagePipeline.html)  **
  - **Description:** Grants permission to delete an image pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteImageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteImageRecipe.html)  **
  - **Description:** Grants permission to delete an image recipe
  - **Resource types (\*required):** [imageRecipe\*](#list_imagebuilder-resource-imageRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInfrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteInfrastructureConfiguration.html)  **
  - **Description:** Grants permission to delete an infrastructure configuration
  - **Resource types (\*required):** [infrastructureConfiguration\*](#list_imagebuilder-resource-infrastructureConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteLifecyclePolicy.html)  **
  - **Description:** Grants permission to delete a lifecycle policy
  - **Resource types (\*required):** [lifecyclePolicy\*](#list_imagebuilder-resource-lifecyclePolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to delete a workflow
  - **Resource types (\*required):** [workflow\*](#list_imagebuilder-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DistributeImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributeImage.html)  **
  - **Description:** Grants permission to distribute an image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [GetComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetComponent.html)  **
  - **Description:** Grants permission to view details about a component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComponentPolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetComponentPolicy.html)  **
  - **Description:** Grants permission to view the resource policy associated with a component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContainerRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetContainerRecipe.html)  **
  - **Description:** Grants permission to view details about a container recipe
  - **Resource types (\*required):** [containerRecipe\*](#list_imagebuilder-resource-containerRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContainerRecipePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetContainerRecipePolicy.html)  **
  - **Description:** Grants permission to view the resource policy associated with a container recipe
  - **Resource types (\*required):** [containerRecipe\*](#list_imagebuilder-resource-containerRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDistributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetDistributionConfiguration.html)  **
  - **Description:** Grants permission to view details about a distribution configuration
  - **Resource types (\*required):** [distributionConfiguration\*](#list_imagebuilder-resource-distributionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html)  **
  - **Description:** Grants permission to view details about an image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImagePipeline.html)  **
  - **Description:** Grants permission to view details about an image pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImagePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImagePolicy.html)  **
  - **Description:** Grants permission to view the resource policy associated with an image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImageRecipe.html)  **
  - **Description:** Grants permission to view details about an image recipe
  - **Resource types (\*required):** [imageRecipe\*](#list_imagebuilder-resource-imageRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetImageRecipePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImageRecipePolicy.html)  **
  - **Description:** Grants permission to view the resource policy associated with an image recipe
  - **Resource types (\*required):** [imageRecipe\*](#list_imagebuilder-resource-imageRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInfrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetInfrastructureConfiguration.html)  **
  - **Description:** Grants permission to view details about an infrastructure configuration
  - **Resource types (\*required):** [infrastructureConfiguration\*](#list_imagebuilder-resource-infrastructureConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLifecycleExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetLifecycleExecution.html)  **
  - **Description:** Grants permission to view details about a lifecycle execution
  - **Resource types (\*required):** [lifecycleExecution\*](#list_imagebuilder-resource-lifecycleExecution)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetLifecyclePolicy.html)  **
  - **Description:** Grants permission to view details about a lifecycle policy
  - **Resource types (\*required):** [lifecyclePolicy\*](#list_imagebuilder-resource-lifecyclePolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMarketplaceResource](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetMarketplaceResource.html)  **
  - **Description:** Grants permission to retrieve Marketplace provided resource
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflow.html)  **
  - **Description:** Grants permission to view details about a workflow
  - **Resource types (\*required):** [workflow\*](#list_imagebuilder-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowExecution.html)  **
  - **Description:** Grants permission to view details about a workflow execution
  - **Resource types (\*required):** [workflowExecution\*](#list_imagebuilder-resource-workflowExecution)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkflowStepExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowStepExecution.html)  **
  - **Description:** Grants permission to view details about a workflow step execution
  - **Resource types (\*required):** [workflowStepExecution\*](#list_imagebuilder-resource-workflowStepExecution)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportComponent](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportComponent.html)  **
  - **Description:** Grants permission to import a new component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [ImportDiskImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportDiskImage.html)  **
  - **Description:** Grants permission to import a disk image
  - **Resource types (\*required):** [imageVersion\*](#list_imagebuilder-resource-imageVersion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [ImportVmImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportVmImage.html)  **
  - **Description:** Grants permission to import an image
  - **Resource types (\*required):** [imageVersion\*](#list_imagebuilder-resource-imageVersion)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [ListComponentBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListComponentBuildVersions.html)  **
  - **Description:** Grants permission to list the component build versions in your account
  - **Resource types (\*required):** [allComponentBuildVersions\*](#list_imagebuilder-resource-allComponentBuildVersions)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComponents](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListComponents.html)  **
  - **Description:** Grants permission to list the component versions owned by or shared with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListContainerRecipes](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListContainerRecipes.html)  **
  - **Description:** Grants permission to list the container recipes owned by or shared with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDistributionConfigurations](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListDistributionConfigurations.html)  **
  - **Description:** Grants permission to list the distribution configurations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImageBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageBuildVersions.html)  **
  - **Description:** Grants permission to list the image build versions in your account
  - **Resource types (\*required):** [allImageBuildVersions\*](#list_imagebuilder-resource-allImageBuildVersions)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImagePackages](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePackages.html)  **
  - **Description:** Grants permission to return a list of packages installed on the specified image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImagePipelineImages](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePipelineImages.html)  **
  - **Description:** Grants permission to return a list of images created by the specified pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImagePipelines](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePipelines.html)  **
  - **Description:** Grants permission to list the image pipelines in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImageRecipes](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageRecipes.html)  **
  - **Description:** Grants permission to list the image recipes owned by or shared with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListImageScanFindingAggregations](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageScanFindingAggregations.html)  **
  - **Description:** Grants permission to list aggregations on the image scan findings in your account
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imagePipeline](#list_imagebuilder-resource-imagePipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImageScanFindings](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageScanFindings.html)  **
  - **Description:** Grants permission to list the image scan findings for the images in your account
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imagePipeline](#list_imagebuilder-resource-imagePipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListImages](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImages.html)  **
  - **Description:** Grants permission to list the image versions owned by or shared with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInfrastructureConfigurations](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListInfrastructureConfigurations.html)  **
  - **Description:** Grants permission to list the infrastructure configurations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLifecycleExecutionResources](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecycleExecutionResources.html)  **
  - **Description:** Grants permission to list resources for the specified lifecycle execution
  - **Resource types (\*required):** [lifecycleExecution\*](#list_imagebuilder-resource-lifecycleExecution)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLifecycleExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecycleExecutions.html)  **
  - **Description:** Grants permission to list lifecycle executions for the specified resource
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [lifecyclePolicy](#list_imagebuilder-resource-lifecyclePolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLifecyclePolicies](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListLifecyclePolicies.html)  **
  - **Description:** Grants permission to list the lifecycle policies in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an Image Builder resource
  - **Resource types (\*required):** [component](#list_imagebuilder-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [containerRecipe](#list_imagebuilder-resource-containerRecipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [distributionConfiguration](#list_imagebuilder-resource-distributionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imagePipeline](#list_imagebuilder-resource-imagePipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [imageRecipe](#list_imagebuilder-resource-imageRecipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [infrastructureConfiguration](#list_imagebuilder-resource-infrastructureConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [lifecyclePolicy](#list_imagebuilder-resource-lifecyclePolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow](#list_imagebuilder-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWaitingWorkflowSteps](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWaitingWorkflowSteps.html)  **
  - **Description:** Grants permission to list waiting workflow steps for the caller account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflowBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowBuildVersions.html)  **
  - **Description:** Grants permission to list the workflow build versions in your account
  - **Resource types (\*required):** [allWorkflowBuildVersions\*](#list_imagebuilder-resource-allWorkflowBuildVersions)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflowExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowExecutions.html)  **
  - **Description:** Grants permission to list workflow executions for the specified image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflowStepExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html)  **
  - **Description:** Grants permission to list workflow step executions for the specified workflow
  - **Resource types (\*required):** [workflowExecution\*](#list_imagebuilder-resource-workflowExecution)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflows.html)  **
  - **Description:** Grants permission to list the workflow versions owned by or shared with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutComponentPolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutComponentPolicy.html)  **
  - **Description:** Grants permission to set the resource policy associated with a component
  - **Resource types (\*required):** [component\*](#list_imagebuilder-resource-component)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutContainerRecipePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutContainerRecipePolicy.html)  **
  - **Description:** Grants permission to set the resource policy associated with a container recipe
  - **Resource types (\*required):** [containerRecipe\*](#list_imagebuilder-resource-containerRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutImagePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutImagePolicy.html)  **
  - **Description:** Grants permission to set the resource policy associated with an image
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutImageRecipePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_PutImageRecipePolicy.html)  **
  - **Description:** Grants permission to set the resource policy associated with an image recipe
  - **Resource types (\*required):** [imageRecipe\*](#list_imagebuilder-resource-imageRecipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RetryImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_RetryImage.html)  **
  - **Description:** Grants permission to retry an image creation
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendWorkflowStepAction](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_SendWorkflowStepAction.html)  **
  - **Description:** Grants permission to send an action to a workflow step
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflowStepExecution\*](#list_imagebuilder-resource-workflowStepExecution) / **Condition keys:**  
  - **Access level:** Write

- **   [StartImagePipelineExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_StartImagePipelineExecution.html)  **
  - **Description:** Grants permission to create a new image from a pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Write

- **   [StartResourceStateUpdate](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_StartResourceStateUpdate.html)  **
  - **Description:** Grants permission to start a state update for the specified resource
  - **Resource types (\*required):** [image\*](#list_imagebuilder-resource-image)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Image Builder resource
  - **Resource types (\*required):** [component](#list_imagebuilder-resource-component) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [containerRecipe](#list_imagebuilder-resource-containerRecipe) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [distributionConfiguration](#list_imagebuilder-resource-distributionConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [imagePipeline](#list_imagebuilder-resource-imagePipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [imageRecipe](#list_imagebuilder-resource-imageRecipe) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [infrastructureConfiguration](#list_imagebuilder-resource-infrastructureConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [lifecyclePolicy](#list_imagebuilder-resource-lifecyclePolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_imagebuilder-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_imagebuilder-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Image Builder resource
  - **Resource types (\*required):** [component](#list_imagebuilder-resource-component) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [containerRecipe](#list_imagebuilder-resource-containerRecipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [distributionConfiguration](#list_imagebuilder-resource-distributionConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [image](#list_imagebuilder-resource-image) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [imagePipeline](#list_imagebuilder-resource-imagePipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [imageRecipe](#list_imagebuilder-resource-imageRecipe) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [infrastructureConfiguration](#list_imagebuilder-resource-infrastructureConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [lifecyclePolicy](#list_imagebuilder-resource-lifecyclePolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_imagebuilder-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_imagebuilder-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDistributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateDistributionConfiguration.html)  **
  - **Description:** Grants permission to update an existing distribution configuration
  - **Resource types (\*required):** [distributionConfiguration\*](#list_imagebuilder-resource-distributionConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateImagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateImagePipeline.html)  **
  - **Description:** Grants permission to update an existing image pipeline
  - **Resource types (\*required):** [imagePipeline\*](#list_imagebuilder-resource-imagePipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateInfrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateInfrastructureConfiguration.html)  **
  - **Description:** Grants permission to update an existing infrastructure configuration
  - **Resource types (\*required):** [infrastructureConfiguration\*](#list_imagebuilder-resource-infrastructureConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[imagebuilder:CreatedResourceTag/${TagKey}](#list_imagebuilder-imagebuilder_CreatedResourceTag___TagKey_)<br />[imagebuilder:CreatedResourceTagKeys](#list_imagebuilder-imagebuilder_CreatedResourceTagKeys)<br />[imagebuilder:Ec2MetadataHttpTokens](#list_imagebuilder-imagebuilder_Ec2MetadataHttpTokens)<br />[imagebuilder:StatusTopicArn](#list_imagebuilder-imagebuilder_StatusTopicArn)
  - **Access level:** Write

- **   [UpdateLifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateLifecyclePolicy.html)  **
  - **Description:** Grants permission to update an existing lifecycle policy
  - **Resource types (\*required):** [lifecyclePolicy\*](#list_imagebuilder-resource-lifecyclePolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_)<br />[imagebuilder:LifecyclePolicyResourceType](#list_imagebuilder-imagebuilder_LifecyclePolicyResourceType)
  - **Access level:** Write



## Resource types defined by Amazon EC2 Image Builder
<a name="list_imagebuilder-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [allComponentBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Component.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:component/${ComponentName}/${ComponentVersion}/\* |   | 
|  [allImageBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Image.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:image/${ImageName}/${ImageVersion}/\* |   | 
|  [allWorkflowBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Workflow.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:workflow/${WorkflowType}/${WorkflowName}/${WorkflowVersion}/\* |   | 
|  [component](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Component.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:component/${ComponentName}/${ComponentVersion}/${ComponentBuildVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [containerRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ContainerRecipe.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:container-recipe/${ContainerRecipeName}/${ContainerRecipeVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [distributionConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_DistributionConfiguration.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:distribution-configuration/${DistributionConfigurationName} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [image](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Image.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:image/${ImageName}/${ImageVersion}/${ImageBuildVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [imagePipeline](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImagePipeline.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:image-pipeline/${ImagePipelineName} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [imageRecipe](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageRecipe.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:image-recipe/${ImageRecipeName}/${ImageRecipeVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [imageVersion](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageVersion.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:image/${ImageName}/${ImageVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [infrastructureConfiguration](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InfrastructureConfiguration.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:infrastructure-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [lifecycleExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecution.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:lifecycle-execution/${LifecycleExecutionId} |   | 
|  [lifecyclePolicy](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecyclePolicy.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:lifecycle-policy/${LifecyclePolicyName} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [workflow](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Workflow.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:workflow/${WorkflowType}/${WorkflowName}/${WorkflowVersion}/${WorkflowBuildVersion} | [aws:ResourceTag/${TagKey}](#list_imagebuilder-aws_ResourceTag___TagKey_) | 
|  [workflowExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowExecutionMetadata.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:workflow-execution/${WorkflowExecutionId} |   | 
|  [workflowStepExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowStepMetadata.html)  | arn:${Partition}:imagebuilder:${Region}:${Account}:workflow-step-execution/${WorkflowStepExecutionId} |   | 

## Condition keys for Amazon EC2 Image Builder
<a name="list_imagebuilder-policy-keys"></a>

Amazon EC2 Image Builder defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [imagebuilder:CreatedResourceTag/${TagKey}](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html#image-builder-security-createdresourcetag)  | Filters access by the tag key-value pairs attached to the resource created by Image Builder | String | 
|   [imagebuilder:CreatedResourceTagKeys](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html#image-builder-security-createdresourcetagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [imagebuilder:Ec2MetadataHttpTokens](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html#image-builder-security-ec2metadatatokens)  | Filters access by the EC2 Instance Metadata HTTP Token Requirement specified in the request | String | 
|   [imagebuilder:LifecyclePolicyResourceType](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html#image-builder-security-lifecyclepolicyresourcetype)  | Filters access by the Lifecycle Policy Resource Type specified in the request | String | 
|   [imagebuilder:StatusTopicArn](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security_iam_service-with-iam.html#image-builder-security-statustopicarn)  | Filters access by the SNS Topic Arn in the request to which terminal state notifications will be published | ARN | 