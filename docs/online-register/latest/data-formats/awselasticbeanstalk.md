

# Data retrieval APIs for AWS Elastic Beanstalk
<a name="awselasticbeanstalk"></a>

AWS Elastic Beanstalk provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="elasticbeanstalk-CheckDNSAvailability"></a>[CheckDNSAvailability](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html) | Check CNAME availability | Read | 
| <a name="elasticbeanstalk-DescribeAccountAttributes"></a>[DescribeAccountAttributes](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeAccountAttributes.html) | Retrieve a list of account attributes, including resource quotas | Read | 
| <a name="elasticbeanstalk-DescribeApplicationVersions"></a>[DescribeApplicationVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html) | Retrieve a list of application versions stored in an AWS Elastic Beanstalk storage bucket | List | 
| <a name="elasticbeanstalk-DescribeApplications"></a>[DescribeApplications](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html) | Retrieve the descriptions of existing applications | List | 
| <a name="elasticbeanstalk-DescribeConfigurationOptions"></a>[DescribeConfigurationOptions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html) | Retrieve descriptions of environment configuration options | Read | 
| <a name="elasticbeanstalk-DescribeConfigurationSettings"></a>[DescribeConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html) | Retrieve a description of the settings for a configuration set | Read | 
| <a name="elasticbeanstalk-DescribeEnvironmentHealth"></a>[DescribeEnvironmentHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html) | Retrieve information about the overall health of an environment | Read | 
| <a name="elasticbeanstalk-DescribeEnvironmentManagedActionHistory"></a>[DescribeEnvironmentManagedActionHistory](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActionHistory.html) | Retrieve a list of an environment's completed and failed managed actions | Read | 
| <a name="elasticbeanstalk-DescribeEnvironmentManagedActions"></a>[DescribeEnvironmentManagedActions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActions.html) | Retrieve a list of an environment's upcoming and in-progress managed actions | Read | 
| <a name="elasticbeanstalk-DescribeEnvironmentResources"></a>[DescribeEnvironmentResources](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html) | Retrieve a list of AWS resources for an environment | Read | 
| <a name="elasticbeanstalk-DescribeEnvironments"></a>[DescribeEnvironments](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html) | Retrieve descriptions for existing environments | List | 
| <a name="elasticbeanstalk-DescribeEvents"></a>[DescribeEvents](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html) | Retrieve a list of event descriptions matching a set of criteria | Read | 
| <a name="elasticbeanstalk-DescribeInstancesHealth"></a>[DescribeInstancesHealth](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html) | Retrieve more detailed information about the health of environment instances | Read | 
| <a name="elasticbeanstalk-DescribePlatformVersion"></a>[DescribePlatformVersion](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html) | Retrieve a description of a managed platform version | Read | 
| <a name="elasticbeanstalk-ListAvailableSolutionStacks"></a>[ListAvailableSolutionStacks](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html) | Retrieve a list of the available solution stack names | List | 
| <a name="elasticbeanstalk-ListPlatformBranches"></a>[ListPlatformBranches](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformBranches.html) | Retrieve a list of the available platform branches | List | 
| <a name="elasticbeanstalk-ListPlatformVersions"></a>[ListPlatformVersions](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html) | Retrieve a list of the available platforms | List | 
| <a name="elasticbeanstalk-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListTagsForResource.html) | Retrieve a list of tags of an Elastic Beanstalk resource | Read | 
| <a name="elasticbeanstalk-RequestEnvironmentInfo"></a>[RequestEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html) | Initiate a request to compile information of the deployed environment | Read | 
| <a name="elasticbeanstalk-RetrieveEnvironmentInfo"></a>[RetrieveEnvironmentInfo](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html) | Retrieve the compiled information from a RequestEnvironmentInfo request | Read | 
| <a name="elasticbeanstalk-ValidateConfigurationSettings"></a>[ValidateConfigurationSettings](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidateConfigurationSettings.html) | Check the validity of a set of configuration settings for a configuration template or an environment | Read | 