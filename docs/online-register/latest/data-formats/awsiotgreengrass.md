

# Data retrieval APIs for AWS IoT Greengrass
<a name="awsiotgreengrass"></a>

AWS IoT Greengrass provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="greengrass-Discover"></a>[Discover](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-discover-api.html) | Retrieve information required to connect to a Greengrass core | Read | 
| <a name="greengrass-GetAssociatedRole"></a>[GetAssociatedRole](https://docs.aws.amazon.com/greengrass/v1/apireference/getassociatedrole-get.html) | Retrieve the role associated with a group | Read | 
| <a name="greengrass-GetBulkDeploymentStatus"></a>[GetBulkDeploymentStatus](https://docs.aws.amazon.com/greengrass/v1/apireference/getbulkdeploymentstatus-get.html) | Return the status of a bulk deployment | Read | 
| <a name="greengrass-GetConnectivityInfo"></a>[GetConnectivityInfo](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectivityinfo-get.html) | Retrieve the connectivity information for a core | Read | 
| <a name="greengrass-GetConnectorDefinition"></a>[GetConnectorDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinition-get.html) | Retrieve information about a connector definition | Read | 
| <a name="greengrass-GetConnectorDefinitionVersion"></a>[GetConnectorDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getconnectordefinitionversion-get.html) | Retrieve information about a connector definition version | Read | 
| <a name="greengrass-GetCoreDefinition"></a>[GetCoreDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinition-get.html) | Retrieve information about a core definition | Read | 
| <a name="greengrass-GetCoreDefinitionVersion"></a>[GetCoreDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getcoredefinitionversion-get.html) | Retrieve information about a core definition version | Read | 
| <a name="greengrass-GetDeploymentStatus"></a>[GetDeploymentStatus](https://docs.aws.amazon.com/greengrass/v1/apireference/getdeploymentstatus-get.html) | Return the status of a deployment | Read | 
| <a name="greengrass-GetDeviceDefinition"></a>[GetDeviceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getdevicedefinition-get.html) | Retrieve information about a device definition | Read | 
| <a name="greengrass-GetDeviceDefinitionVersion"></a>[GetDeviceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getdevicedefinitionversion-get.html) | Retrieve information about a device definition version | Read | 
| <a name="greengrass-GetFunctionDefinition"></a>[GetFunctionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinition-get.html) | Retrieve information about a Lambda function definition, such as its creation time and latest version | Read | 
| <a name="greengrass-GetFunctionDefinitionVersion"></a>[GetFunctionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getfunctiondefinitionversion-get.html) | Retrieve information about a Lambda function definition version, such as which Lambda functions are included in the version and their configurations | Read | 
| <a name="greengrass-GetGroup"></a>[GetGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html) | Retrieve information about a group | Read | 
| <a name="greengrass-GetGroupCertificateAuthority"></a>[GetGroupCertificateAuthority](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupcertificateauthority-get.html) | Return the public key of the CA associated with a group | Read | 
| <a name="greengrass-GetGroupCertificateConfiguration"></a>[GetGroupCertificateConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupcertificateconfiguration-get.html) | Retrieve the current configuration for the CA used by a group | Read | 
| <a name="greengrass-GetGroupVersion"></a>[GetGroupVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroupversion-get.html) | Retrieve information about a group version | Read | 
| <a name="greengrass-GetLoggerDefinition"></a>[GetLoggerDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getloggerdefinition-get.html) | Retrieve information about a logger definition | Read | 
| <a name="greengrass-GetLoggerDefinitionVersion"></a>[GetLoggerDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getloggerdefinitionversion-get.html) | Retrieve information about a logger definition version | Read | 
| <a name="greengrass-GetResourceDefinition"></a>[GetResourceDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getresourcedefinition-get.html) | Retrieve information about a resource definition, such as its creation time and latest version | Read | 
| <a name="greengrass-GetResourceDefinitionVersion"></a>[GetResourceDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getresourcedefinitionversion-get.html) | Retrieve information about a resource definition version, such as which resources are included in the version | Read | 
| <a name="greengrass-GetServiceRoleForAccount"></a>[GetServiceRoleForAccount](https://docs.aws.amazon.com/greengrass/v1/apireference/getserviceroleforaccount-get.html) | Retrieve the service role that is attached to an account | Read | 
| <a name="greengrass-GetSubscriptionDefinition"></a>[GetSubscriptionDefinition](https://docs.aws.amazon.com/greengrass/v1/apireference/getsubscriptiondefinition-get.html) | Retrieve information about a subscription definition | Read | 
| <a name="greengrass-GetSubscriptionDefinitionVersion"></a>[GetSubscriptionDefinitionVersion](https://docs.aws.amazon.com/greengrass/v1/apireference/getsubscriptiondefinitionversion-get.html) | Retrieve information about a subscription definition version | Read | 
| <a name="greengrass-GetThingRuntimeConfiguration"></a>[GetThingRuntimeConfiguration](https://docs.aws.amazon.com/greengrass/v1/apireference/getthingruntimeconfiguration-get.html) | Retrieve runtime configuration of a thing | Read | 
| <a name="greengrass-ListBulkDeploymentDetailedReports"></a>[ListBulkDeploymentDetailedReports](https://docs.aws.amazon.com/greengrass/v1/apireference/listbulkdeploymentdetailedreports-get.html) | Retrieve a paginated list of the deployments that have been started in a bulk deployment operation and their current deployment status | Read | 
| <a name="greengrass-ListBulkDeployments"></a>[ListBulkDeployments](https://docs.aws.amazon.com/greengrass/v1/apireference/listbulkdeployments-get.html) | Retrieve a list of bulk deployments | List | 
| <a name="greengrass-ListConnectorDefinitionVersions"></a>[ListConnectorDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listconnectordefinitionversions-get.html) | List the versions of a connector definition | List | 
| <a name="greengrass-ListConnectorDefinitions"></a>[ListConnectorDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listconnectordefinitions-get.html) | Retrieve a list of connector definitions | List | 
| <a name="greengrass-ListCoreDefinitionVersions"></a>[ListCoreDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listcoredefinitionversions-get.html) | List the versions of a core definition | List | 
| <a name="greengrass-ListCoreDefinitions"></a>[ListCoreDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listcoredefinitions-get.html) | Retrieve a list of core definitions | List | 
| <a name="greengrass-ListDeployments"></a>[ListDeployments](https://docs.aws.amazon.com/greengrass/v1/apireference/listdeployments-get.html) | Retrieve a list of all deployments for a group | List | 
| <a name="greengrass-ListDeviceDefinitionVersions"></a>[ListDeviceDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listdevicedefinitionversions-get.html) | List the versions of a device definition | List | 
| <a name="greengrass-ListDeviceDefinitions"></a>[ListDeviceDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listdevicedefinitions-get.html) | Retrieve a list of device definitions | List | 
| <a name="greengrass-ListFunctionDefinitionVersions"></a>[ListFunctionDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listfunctiondefinitionversions-get.html) | List the versions of a Lambda function definition | List | 
| <a name="greengrass-ListFunctionDefinitions"></a>[ListFunctionDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listfunctiondefinitions-get.html) | Retrieve a list of Lambda function definitions | List | 
| <a name="greengrass-ListGroupCertificateAuthorities"></a>[ListGroupCertificateAuthorities](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroupcertificateauthorities-get.html) | Retrieve a list of current CAs for a group | List | 
| <a name="greengrass-ListGroupVersions"></a>[ListGroupVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroupversions-get.html) | List the versions of a group | List | 
| <a name="greengrass-ListGroups"></a>[ListGroups](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html) | Retrieve a list of groups | List | 
| <a name="greengrass-ListLoggerDefinitionVersions"></a>[ListLoggerDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listloggerdefinitionversions-get.html) | List the versions of a logger definition | List | 
| <a name="greengrass-ListLoggerDefinitions"></a>[ListLoggerDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listloggerdefinitions-get.html) | Retrieve a list of logger definitions | List | 
| <a name="greengrass-ListResourceDefinitionVersions"></a>[ListResourceDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listresourcedefinitionversions-get.html) | List the versions of a resource definition | List | 
| <a name="greengrass-ListResourceDefinitions"></a>[ListResourceDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listresourcedefinitions-get.html) | Retrieve a list of resource definitions | List | 
| <a name="greengrass-ListSubscriptionDefinitionVersions"></a>[ListSubscriptionDefinitionVersions](https://docs.aws.amazon.com/greengrass/v1/apireference/listsubscriptiondefinitionversions-get.html) | List the versions of a subscription definition | List | 
| <a name="greengrass-ListSubscriptionDefinitions"></a>[ListSubscriptionDefinitions](https://docs.aws.amazon.com/greengrass/v1/apireference/listsubscriptiondefinitions-get.html) | Retrieve a list of subscription definitions | List | 
| <a name="greengrass-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/greengrass/v1/apireference/listtagsforresource-get.html) | List the tags for a resource | Read | 