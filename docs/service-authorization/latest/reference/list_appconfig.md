

# Actions, resources, and condition keys for AWS AppConfig
<a name="list_appconfig"></a>

AWS AppConfig (service prefix: `appconfig`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appconfig/appconfig.json) for this service.

**Topics**
+ [API operations defined by AWS AppConfig](#list_appconfig-operations)
+ [Actions defined by AWS AppConfig](#list_appconfig-actions-as-permissions)
+ [Resource types defined by AWS AppConfig](#list_appconfig-resources-for-iam-policies)
+ [Condition keys for AWS AppConfig](#list_appconfig-policy-keys)

## API operations defined by AWS AppConfig
<a name="list_appconfig-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_appconfig-actions-as-permissions).




- **   CreateApplication  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateApplication](#list_appconfig-action-CreateApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfigurationProfile  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateConfigurationProfile](#list_appconfig-action-CreateConfigurationProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   CreateDeploymentStrategy  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateDeploymentStrategy](#list_appconfig-action-CreateDeploymentStrategy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateEnvironment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateEnvironment](#list_appconfig-action-CreateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   CreateExperimentDefinition  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateExperimentDefinition](#list_appconfig-action-CreateExperimentDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateExtension  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateExtension](#list_appconfig-action-CreateExtension)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   CreateExtensionAssociation  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateExtensionAssociation](#list_appconfig-action-CreateExtensionAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateHostedConfigurationVersion  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:CreateHostedConfigurationVersion](#list_appconfig-action-CreateHostedConfigurationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteApplication](#list_appconfig-action-DeleteApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfigurationProfile  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteConfigurationProfile](#list_appconfig-action-DeleteConfigurationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDeploymentStrategy  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteDeploymentStrategy](#list_appconfig-action-DeleteDeploymentStrategy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEnvironment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteEnvironment](#list_appconfig-action-DeleteEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExperimentDefinition  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteExperimentDefinition](#list_appconfig-action-DeleteExperimentDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExtension  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteExtension](#list_appconfig-action-DeleteExtension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteExtensionAssociation  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteExtensionAssociation](#list_appconfig-action-DeleteExtensionAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteHostedConfigurationVersion  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:DeleteHostedConfigurationVersion](#list_appconfig-action-DeleteHostedConfigurationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountSettings  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetAccountSettings](#list_appconfig-action-GetAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetApplication  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetApplication](#list_appconfig-action-GetApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguration  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetConfiguration](#list_appconfig-action-GetConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfigurationProfile  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetConfigurationProfile](#list_appconfig-action-GetConfigurationProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeployment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetDeployment](#list_appconfig-action-GetDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDeploymentStrategy  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetDeploymentStrategy](#list_appconfig-action-GetDeploymentStrategy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnvironment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetEnvironment](#list_appconfig-action-GetEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExperimentDefinition  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetExperimentDefinition](#list_appconfig-action-GetExperimentDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExperimentRun  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetExperimentRun](#list_appconfig-action-GetExperimentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExtension  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetExtension](#list_appconfig-action-GetExtension) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExtensionAssociation  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetExtensionAssociation](#list_appconfig-action-GetExtensionAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetHostedConfigurationVersion  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:GetHostedConfigurationVersion](#list_appconfig-action-GetHostedConfigurationVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApplications  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListApplications](#list_appconfig-action-ListApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurationProfiles  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListConfigurationProfiles](#list_appconfig-action-ListConfigurationProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeploymentStrategies  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListDeploymentStrategies](#list_appconfig-action-ListDeploymentStrategies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDeployments  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListDeployments](#list_appconfig-action-ListDeployments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEnvironments  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListEnvironments](#list_appconfig-action-ListEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentDefinitions  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListExperimentDefinitions](#list_appconfig-action-ListExperimentDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentRunEvents  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListExperimentRunEvents](#list_appconfig-action-ListExperimentRunEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExperimentRuns  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListExperimentRuns](#list_appconfig-action-ListExperimentRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExtensionAssociations  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListExtensionAssociations](#list_appconfig-action-ListExtensionAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExtensions  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListExtensions](#list_appconfig-action-ListExtensions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListHostedConfigurationVersions  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListHostedConfigurationVersions](#list_appconfig-action-ListHostedConfigurationVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ListTagsForResource](#list_appconfig-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDeployment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:StartDeployment](#list_appconfig-action-StartDeployment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartExperimentRun  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:StartExperimentRun](#list_appconfig-action-StartExperimentRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StopDeployment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:StopDeployment](#list_appconfig-action-StopDeployment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopExperimentRun  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:StopExperimentRun](#list_appconfig-action-StopExperimentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:TagResource](#list_appconfig-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UntagResource](#list_appconfig-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountSettings  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateAccountSettings](#list_appconfig-action-UpdateAccountSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateApplication  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateApplication](#list_appconfig-action-UpdateApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfigurationProfile  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateConfigurationProfile](#list_appconfig-action-UpdateConfigurationProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   UpdateDeploymentStrategy  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateDeploymentStrategy](#list_appconfig-action-UpdateDeploymentStrategy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnvironment  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateEnvironment](#list_appconfig-action-UpdateEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   UpdateExperimentDefinition  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateExperimentDefinition](#list_appconfig-action-UpdateExperimentDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExperimentRun  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateExperimentRun](#list_appconfig-action-UpdateExperimentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateExtension  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateExtension](#list_appconfig-action-UpdateExtension)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** appconfig.amazonaws.com / **Access level:** Write

- **   UpdateExtensionAssociation  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:UpdateExtensionAssociation](#list_appconfig-action-UpdateExtensionAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateConfiguration  **
  - **SDK client:** appconfig
  - **IAM action:**  [appconfig:ValidateConfiguration](#list_appconfig-action-ValidateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLatestConfiguration  **
  - **SDK client:** appconfigdata
  - **IAM action:**  [appconfig:GetLatestConfiguration](#list_appconfig-action-GetLatestConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartConfigurationSession  **
  - **SDK client:** appconfigdata
  - **IAM action:**  [appconfig:StartConfigurationSession](#list_appconfig-action-StartConfigurationSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS AppConfig
<a name="list_appconfig-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateConfigurationProfile.html)  **
  - **Description:** Grants permission to create a configuration profile
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateDeploymentStrategy.html)  **
  - **Description:** Grants permission to create a deployment strategy
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create an environment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExperimentDefinition](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExperimentDefinition.html)  **
  - **Description:** Grants permission to create an experiment definition
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtension.html)  **
  - **Description:** Grants permission to create an extension
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateExtensionAssociation.html)  **
  - **Description:** Grants permission to create an extension association
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [CreateHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateHostedConfigurationVersion.html)  **
  - **Description:** Grants permission to create a hosted configuration version
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteConfigurationProfile.html)  **
  - **Description:** Grants permission to delete a configuration profile
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteDeploymentStrategy.html)  **
  - **Description:** Grants permission to delete a deployment strategy
  - **Resource types (\*required):** [deploymentstrategy\*](#list_appconfig-resource-deploymentstrategy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an environment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExperimentDefinition](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExperimentDefinition.html)  **
  - **Description:** Grants permission to delete an experiment definition
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtension.html)  **
  - **Description:** Grants permission to delete an extension
  - **Resource types (\*required):** [extension\*](#list_appconfig-resource-extension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtensionAssociation.html)  **
  - **Description:** Grants permission to delete an extension association
  - **Resource types (\*required):** [extensionassociation\*](#list_appconfig-resource-extensionassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteHostedConfigurationVersion.html)  **
  - **Description:** Grants permission to delete a hosted configuration version
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hostedconfigurationversion\*](#list_appconfig-resource-hostedconfigurationversion) / **Condition keys:**  
  - **Access level:** Write

- **   [GetAccountSettings](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetAccountSettings.html)  **
  - **Description:** Grants permission to view account-wide AppConfig settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to view details about an application
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfiguration.html)  **
  - **Description:** Grants permission to view details about a configuration
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetConfigurationProfile.html)  **
  - **Description:** Grants permission to view details about a configuration profile
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to view details about a deployment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deployment\*](#list_appconfig-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetDeploymentStrategy.html)  **
  - **Description:** Grants permission to view details about a deployment strategy
  - **Resource types (\*required):** [deploymentstrategy\*](#list_appconfig-resource-deploymentstrategy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to view details about an environment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentDefinition](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExperimentDefinition.html)  **
  - **Description:** Grants permission to view details about an experiment definition
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentRun](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExperimentRun.html)  **
  - **Description:** Grants permission to view details about an experiment run
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentrun\*](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExtension.html)  **
  - **Description:** Grants permission to view details about an extension
  - **Resource types (\*required):** [extension\*](#list_appconfig-resource-extension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetExtensionAssociation.html)  **
  - **Description:** Grants permission to view details about an extension association
  - **Resource types (\*required):** [extensionassociation\*](#list_appconfig-resource-extensionassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetHostedConfigurationVersion](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_GetHostedConfigurationVersion.html)  **
  - **Description:** Grants permission to view details about a hosted configuration version
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [hostedconfigurationversion\*](#list_appconfig-resource-hostedconfigurationversion) / **Condition keys:**  
  - **Access level:** Read

- **   [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html)  **
  - **Description:** Grants permission to retrieve a deployed configuration
  - **Resource types (\*required):** [configuration\*](#list_appconfig-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApplications](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list the applications in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurationProfiles](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListConfigurationProfiles.html)  **
  - **Description:** Grants permission to list the configuration profiles for an application
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeploymentStrategies](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListDeploymentStrategies.html)  **
  - **Description:** Grants permission to list the deployment strategies for your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDeployments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListDeployments.html)  **
  - **Description:** Grants permission to list the deployments for an environment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list the environments for an application
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperimentDefinitions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExperimentDefinitions.html)  **
  - **Description:** Grants permission to list the experiment definitions in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExperimentRunEvents](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExperimentRunEvents.html)  **
  - **Description:** Grants permission to list the events for an experiment run
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentrun\*](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExperimentRuns](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExperimentRuns.html)  **
  - **Description:** Grants permission to list the experiment runs for an experiment definition
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExtensionAssociations](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensionAssociations.html)  **
  - **Description:** Grants permission to list the extension associations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExtensions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensions.html)  **
  - **Description:** Grants permission to list the extensions in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListHostedConfigurationVersions](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListHostedConfigurationVersions.html)  **
  - **Description:** Grants permission to list the hosted configuration versions for a configuration profile
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to view a list of resource tags for a specified resource
  - **Resource types (\*required):** [application](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deployment](#list_appconfig-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deploymentstrategy](#list_appconfig-resource-deploymentstrategy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentrun](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [extension](#list_appconfig-resource-extension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [extensionassociation](#list_appconfig-resource-extensionassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html)  **
  - **Description:** Grants permission to start a configuration session
  - **Resource types (\*required):** [configuration\*](#list_appconfig-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StartDeployment.html)  **
  - **Description:** Grants permission to initiate a deployment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [deploymentstrategy\*](#list_appconfig-resource-deploymentstrategy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [StartExperimentRun](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StartExperimentRun.html)  **
  - **Description:** Grants permission to start an experiment run
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Write

- **   [StopDeployment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html)  **
  - **Description:** Grants permission to stop a deployment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [deployment\*](#list_appconfig-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopExperimentRun](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopExperimentRun.html)  **
  - **Description:** Grants permission to stop an experiment run
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentrun\*](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an appconfig resource
  - **Resource types (\*required):** [application](#list_appconfig-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [configuration](#list_appconfig-resource-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [configurationprofile](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_appconfig-resource-deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [deploymentstrategy](#list_appconfig-resource-deploymentstrategy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_appconfig-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [experimentdefinition](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [experimentrun](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [extension](#list_appconfig-resource-extension) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [extensionassociation](#list_appconfig-resource-extensionassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_appconfig-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an appconfig resource
  - **Resource types (\*required):** [application](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [configuration](#list_appconfig-resource-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [configurationprofile](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [deployment](#list_appconfig-resource-deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [deploymentstrategy](#list_appconfig-resource-deploymentstrategy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [environment](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [experimentdefinition](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [experimentrun](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [extension](#list_appconfig-resource-extension) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Resource types (\*required):** [extensionassociation](#list_appconfig-resource-extensionassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_appconfig-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountSettings](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateAccountSettings.html)  **
  - **Description:** Grants permission to modify account-wide AppConfig settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to modify an application
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfigurationProfile](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateConfigurationProfile.html)  **
  - **Description:** Grants permission to modify a configuration profile
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDeploymentStrategy](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateDeploymentStrategy.html)  **
  - **Description:** Grants permission to modify a deployment strategy
  - **Resource types (\*required):** [deploymentstrategy\*](#list_appconfig-resource-deploymentstrategy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to modify an environment
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_appconfig-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExperimentDefinition](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExperimentDefinition.html)  **
  - **Description:** Grants permission to modify an experiment definition
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExperimentRun](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExperimentRun.html)  **
  - **Description:** Grants permission to modify an experiment run
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentdefinition\*](#list_appconfig-resource-experimentdefinition) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [experimentrun\*](#list_appconfig-resource-experimentrun) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExtension](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExtension.html)  **
  - **Description:** Grants permission to modify an extension
  - **Resource types (\*required):** [extension\*](#list_appconfig-resource-extension)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateExtensionAssociation](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateExtensionAssociation.html)  **
  - **Description:** Grants permission to modify an extension association
  - **Resource types (\*required):** [extensionassociation\*](#list_appconfig-resource-extensionassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ValidateConfiguration.html)  **
  - **Description:** Grants permission to validate a configuration
  - **Resource types (\*required):** [application\*](#list_appconfig-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [configurationprofile\*](#list_appconfig-resource-configurationprofile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS AppConfig
<a name="list_appconfig-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-namespace.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/retrieving-feature-flags.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/environment/${EnvironmentId}/configuration/${ConfigurationProfileId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [configurationprofile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/configurationprofile/${ConfigurationProfileId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [deployment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/environment/${EnvironmentId}/deployment/${DeploymentNumber} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [deploymentstrategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)  | arn:${Partition}:appconfig:${Region}:${Account}:deploymentstrategy/${DeploymentStrategyId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/environment/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [experimentdefinition](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-experiment-definition.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/experimentdefinition/${ExperimentDefinitionId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [experimentrun](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-experimentation-creating-starting.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/experimentdefinition/${ExperimentDefinitionId}/experimentrun/${ExperimentRunNumber} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [extension](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)  | arn:${Partition}:appconfig:${Region}:${Account}:extension/${ExtensionId}/${ExtensionVersionNumber} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [extensionassociation](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)  | arn:${Partition}:appconfig:${Region}:${Account}:extensionassociation/${ExtensionAssociationId} | [aws:ResourceTag/${TagKey}](#list_appconfig-aws_ResourceTag___TagKey_) | 
|  [hostedconfigurationversion](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile.html)  | arn:${Partition}:appconfig:${Region}:${Account}:application/${ApplicationId}/configurationprofile/${ConfigurationProfileId} |   | 

## Condition keys for AWS AppConfig
<a name="list_appconfig-policy-keys"></a>

AWS AppConfig defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by the allowed set of values for a specified tag | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a tag key-value pair assigned to the AWS resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 