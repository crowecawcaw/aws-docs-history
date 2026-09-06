

# Actions, resources, and condition keys for AWS Elastic Beanstalk
<a name="list_elasticbeanstalk"></a>

AWS Elastic Beanstalk (service prefix: `elasticbeanstalk`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elasticbeanstalk/elasticbeanstalk.json) for this service.

**Topics**
+ [API operations defined by AWS Elastic Beanstalk](#list_elasticbeanstalk-operations)
+ [Actions defined by AWS Elastic Beanstalk](#list_elasticbeanstalk-actions-as-permissions)
+ [Resource types defined by AWS Elastic Beanstalk](#list_elasticbeanstalk-resources-for-iam-policies)
+ [Condition keys for AWS Elastic Beanstalk](#list_elasticbeanstalk-policy-keys)

## API operations defined by AWS Elastic Beanstalk
<a name="list_elasticbeanstalk-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_elasticbeanstalk-actions-as-permissions).




- **   DescribeEnvironments  **
  - **IAM action:**  [elasticbeanstalk:DescribeEnvironments](#list_elasticbeanstalk-action-DescribeEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by AWS Elastic Beanstalk
<a name="list_elasticbeanstalk-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortEnvironmentUpdate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AbortEnvironmentUpdate.html)  **
  - **Description:** Grants permission to cancel in-progress environment configuration update or application version deployment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html)  **
  - **Description:** Grants permission to add tags to an Elastic Beanstalk resource and to update tag values
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ApplyEnvironmentManagedAction](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplyEnvironmentManagedAction.html)  **
  - **Description:** Grants permission to apply a scheduled managed action immediately
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [AssociateEnvironmentOperationsRole](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_AssociateEnvironmentOperationsRole.html)  **
  - **Description:** Grants permission to associate an operations role with an environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [CheckDNSAvailability](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html)  **
  - **Description:** Grants permission to check CNAME availability
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ComposeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ComposeEnvironments.html)  **
  - **Description:** Grants permission to create or update a group of environments, each running a separate component of a single application
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [applicationversion\*](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html)  **
  - **Description:** Grants permission to create a new application
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Access level:** Write

- **   [CreateApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html)  **
  - **Description:** Grants permission to create an application version for an application
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [applicationversion\*](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [CreateConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateConfigurationTemplate.html)  **
  - **Description:** Grants permission to create a configuration template
  - **Resource types (\*required):** [configurationtemplate\*](#list_elasticbeanstalk-resource-configurationtemplate)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:FromApplication](#list_elasticbeanstalk-elasticbeanstalk_FromApplication)<br />[elasticbeanstalk:FromApplicationVersion](#list_elasticbeanstalk-elasticbeanstalk_FromApplicationVersion)<br />[elasticbeanstalk:FromConfigurationTemplate](#list_elasticbeanstalk-elasticbeanstalk_FromConfigurationTemplate)<br />[elasticbeanstalk:FromEnvironment](#list_elasticbeanstalk-elasticbeanstalk_FromEnvironment)<br />[elasticbeanstalk:FromPlatform](#list_elasticbeanstalk-elasticbeanstalk_FromPlatform)<br />[elasticbeanstalk:FromSolutionStack](#list_elasticbeanstalk-elasticbeanstalk_FromSolutionStack)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to launch an environment for an application
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:FromApplicationVersion](#list_elasticbeanstalk-elasticbeanstalk_FromApplicationVersion)<br />[elasticbeanstalk:FromConfigurationTemplate](#list_elasticbeanstalk-elasticbeanstalk_FromConfigurationTemplate)<br />[elasticbeanstalk:FromPlatform](#list_elasticbeanstalk-elasticbeanstalk_FromPlatform)<br />[elasticbeanstalk:FromSolutionStack](#list_elasticbeanstalk-elasticbeanstalk_FromSolutionStack)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [CreatePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreatePlatformVersion.html)  **
  - **Description:** Grants permission to create a new version of a custom platform
  - **Resource types (\*required):** [platform\*](#list_elasticbeanstalk-resource-platform)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStorageLocation](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateStorageLocation.html)  **
  - **Description:** Grants permission to create the Amazon S3 storage location for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an application along with all associated versions and configurations
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplicationVersion.html)  **
  - **Description:** Grants permission to delete an application version from an application
  - **Resource types (\*required):** [applicationversion\*](#list_elasticbeanstalk-resource-applicationversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [DeleteConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteConfigurationTemplate.html)  **
  - **Description:** Grants permission to delete a configuration template
  - **Resource types (\*required):** [configurationtemplate\*](#list_elasticbeanstalk-resource-configurationtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [DeleteEnvironmentConfiguration](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteEnvironmentConfiguration.html)  **
  - **Description:** Grants permission to delete the draft configuration associated with the running environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [DeletePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeletePlatformVersion.html)  **
  - **Description:** Grants permission to delete a version of a custom platform
  - **Resource types (\*required):** [platform\*](#list_elasticbeanstalk-resource-platform)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeAccountAttributes](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeAccountAttributes.html)  **
  - **Description:** Grants permission to retrieve a list of account attributes, including resource quotas
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeApplicationVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html)  **
  - **Description:** Grants permission to retrieve a list of application versions stored in an AWS Elastic Beanstalk storage bucket
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** List

- **   [DescribeApplications](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html)  **
  - **Description:** Grants permission to retrieve the descriptions of existing applications
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeConfigurationOptions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html)  **
  - **Description:** Grants permission to retrieve descriptions of environment configuration options
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [solutionstack](#list_elasticbeanstalk-resource-solutionstack) / **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html)  **
  - **Description:** Grants permission to retrieve a description of the settings for a configuration set
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeEnvironmentHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html)  **
  - **Description:** Grants permission to retrieve information about the overall health of an environment
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeEnvironmentManagedActionHistory](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActionHistory.html)  **
  - **Description:** Grants permission to retrieve a list of an environment's completed and failed managed actions
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeEnvironmentManagedActions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActions.html)  **
  - **Description:** Grants permission to retrieve a list of an environment's upcoming and in-progress managed actions
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeEnvironmentResources](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html)  **
  - **Description:** Grants permission to retrieve a list of AWS resources for an environment
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html)  **
  - **Description:** Grants permission to retrieve descriptions for existing environments
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** List

- **   [DescribeEvents](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html)  **
  - **Description:** Grants permission to retrieve a list of event descriptions matching a set of criteria
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribeInstancesHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html)  **
  - **Description:** Grants permission to retrieve more detailed information about the health of environment instances
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [DescribePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html)  **
  - **Description:** Grants permission to retrieve a description of a managed platform version
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateEnvironmentOperationsRole](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DisassociateEnvironmentOperationsRole.html)  **
  - **Description:** Grants permission to disassociate an operations role with an environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [ListAvailableSolutionStacks](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html)  **
  - **Description:** Grants permission to retrieve a list of the available solution stack names
  - **Resource types (\*required):** [solutionstack](#list_elasticbeanstalk-resource-solutionstack)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPlatformBranches](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformBranches.html)  **
  - **Description:** Grants permission to retrieve a list of the available platform branches
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPlatformVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html)  **
  - **Description:** Grants permission to retrieve a list of the available platforms
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags of an Elastic Beanstalk resource
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform) / **Condition keys:**  
  - **Access level:** Read

- **   [PutInstanceStatistics](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html#health-enhanced-authz)  **
  - **Description:** Grants permission to submit instance statistics for enhanced health
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [RebuildEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RebuildEnvironment.html)  **
  - **Description:** Grants permission to delete and recreate all of the AWS resources for an environment and to force a restart
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html)  **
  - **Description:** Grants permission to remove tags from an Elastic Beanstalk resource
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform) / **Condition keys:** [aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [RequestEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html)  **
  - **Description:** Grants permission to initiate a request to compile information of the deployed environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [RestartAppServer](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html)  **
  - **Description:** Grants permission to request an environment to restart the application container server running on each Amazon EC2 instance
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [RetrieveEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html)  **
  - **Description:** Grants permission to retrieve the compiled information from a RequestEnvironmentInfo request
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read

- **   [SwapEnvironmentCNAMEs](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SwapEnvironmentCNAMEs.html)  **
  - **Description:** Grants permission to swap the CNAMEs of two environments
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:FromEnvironment](#list_elasticbeanstalk-elasticbeanstalk_FromEnvironment)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [TerminateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_TerminateEnvironment.html)  **
  - **Description:** Grants permission to terminate an environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an application with specified properties
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplicationResourceLifecycle](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationResourceLifecycle.html)  **
  - **Description:** Grants permission to update the application version lifecycle policy associated with the application
  - **Resource types (\*required):** [application\*](#list_elasticbeanstalk-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationVersion.html)  **
  - **Description:** Grants permission to update an application version with specified properties
  - **Resource types (\*required):** [applicationversion\*](#list_elasticbeanstalk-resource-applicationversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [UpdateConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateConfigurationTemplate.html)  **
  - **Description:** Grants permission to update a configuration template with specified properties or configuration option values
  - **Resource types (\*required):** [configurationtemplate\*](#list_elasticbeanstalk-resource-configurationtemplate)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:FromApplication](#list_elasticbeanstalk-elasticbeanstalk_FromApplication)<br />[elasticbeanstalk:FromApplicationVersion](#list_elasticbeanstalk-elasticbeanstalk_FromApplicationVersion)<br />[elasticbeanstalk:FromConfigurationTemplate](#list_elasticbeanstalk-elasticbeanstalk_FromConfigurationTemplate)<br />[elasticbeanstalk:FromEnvironment](#list_elasticbeanstalk-elasticbeanstalk_FromEnvironment)<br />[elasticbeanstalk:FromPlatform](#list_elasticbeanstalk-elasticbeanstalk_FromPlatform)<br />[elasticbeanstalk:FromSolutionStack](#list_elasticbeanstalk-elasticbeanstalk_FromSolutionStack)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update an environment
  - **Resource types (\*required):** [environment\*](#list_elasticbeanstalk-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:FromApplicationVersion](#list_elasticbeanstalk-elasticbeanstalk_FromApplicationVersion)<br />[elasticbeanstalk:FromConfigurationTemplate](#list_elasticbeanstalk-elasticbeanstalk_FromConfigurationTemplate)<br />[elasticbeanstalk:FromPlatform](#list_elasticbeanstalk-elasticbeanstalk_FromPlatform)<br />[elasticbeanstalk:FromSolutionStack](#list_elasticbeanstalk-elasticbeanstalk_FromSolutionStack)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Write

- **   [UpdateTagsForResource](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html)  **
  - **Description:** Doesn't grant permission to update tags. To grant permission to add tags to an Elastic Beanstalk resource, remove tags, and to update tag values, specify elasticbeanstalk:AddTags and elasticbeanstalk:RemoveTags
  - **Resource types (\*required):** [application](#list_elasticbeanstalk-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Resource types (\*required):** [applicationversion](#list_elasticbeanstalk-resource-applicationversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [platform](#list_elasticbeanstalk-resource-platform) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elasticbeanstalk-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elasticbeanstalk-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [ValidateConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html)  **
  - **Description:** Grants permission to check the validity of a set of configuration settings for a configuration template or an environment
  - **Resource types (\*required):** [configurationtemplate](#list_elasticbeanstalk-resource-configurationtemplate) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Resource types (\*required):** [environment](#list_elasticbeanstalk-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication)
  - **Access level:** Read



## Resource types defined by AWS Elastic Beanstalk
<a name="list_elasticbeanstalk-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}:${Account}:application/${ApplicationName} | [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_) | 
|  [applicationversion](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}:${Account}:applicationversion/${ApplicationName}/${VersionLabel} | [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication) | 
|  [configurationtemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}:${Account}:configurationtemplate/${ApplicationName}/${TemplateName} | [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication) | 
|  [environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}:${Account}:environment/${ApplicationName}/${EnvironmentName} | [aws:ResourceTag/${TagKey}](#list_elasticbeanstalk-aws_ResourceTag___TagKey_)<br />[elasticbeanstalk:InApplication](#list_elasticbeanstalk-elasticbeanstalk_InApplication) | 
|  [platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}::platform/${PlatformNameWithVersion} |   | 
|  [solutionstack](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.arn.html)  | arn:${Partition}:elasticbeanstalk:${Region}::solutionstack/${SolutionStackName} |   | 

## Condition keys for AWS Elastic Beanstalk
<a name="list_elasticbeanstalk-policy-keys"></a>

AWS Elastic Beanstalk defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 
|   [elasticbeanstalk:FromApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by an application as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:FromApplicationVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by an application version as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:FromConfigurationTemplate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by a configuration template as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:FromEnvironment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by an environment as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:FromPlatform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by a platform as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:FromSolutionStack](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by a solution stack as a dependency or a constraint on an input parameter | ARN | 
|   [elasticbeanstalk:InApplication](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.actions.html#AWSHowTo.iam.policies.conditions)  | Filters access by the application that contains the resource that the action operates on | ARN | 