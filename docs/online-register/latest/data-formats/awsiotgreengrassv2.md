

# Data retrieval APIs for AWS IoT Greengrass V2
<a name="awsiotgreengrassv2"></a>

AWS IoT Greengrass V2 provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="greengrass-DescribeComponent"></a>[DescribeComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_DescribeComponent.html) | Retrieve metadata for a version of a component | Read | 
| <a name="greengrass-GetComponent"></a>[GetComponent](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponent.html) | Get the recipe for a version of a component | Read | 
| <a name="greengrass-GetComponentVersionArtifact"></a>[GetComponentVersionArtifact](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetComponentVersionArtifact.html) | Get the pre-signed URL to download a public component artifact | Read | 
| <a name="greengrass-GetConnectivityInfo"></a>[GetConnectivityInfo](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetConnectivityInfo.html) | Retrieve the connectivity information for a Greengrass core device | Read | 
| <a name="greengrass-GetCoreDevice"></a>[GetCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetCoreDevice.html) | Retrieves metadata for a AWS IoT Greengrass core device | Read | 
| <a name="greengrass-GetDeployment"></a>[GetDeployment](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetDeployment.html) | Get a deployment | Read | 
| <a name="greengrass-GetServiceRoleForAccount"></a>[GetServiceRoleForAccount](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetServiceRoleForAccount.html) | Retrieve the service role that is attached to an account | Read | 
| <a name="greengrass-ListClientDevicesAssociatedWithCoreDevice"></a>[ListClientDevicesAssociatedWithCoreDevice](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListClientDevicesAssociatedWithCoreDevice.html) | Retrieve a paginated list of client devices associated to a AWS IoT Greengrass core device | List | 
| <a name="greengrass-ListComponentVersions"></a>[ListComponentVersions](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponentVersions.html) | Retrieve a paginated list of all versions for a component | List | 
| <a name="greengrass-ListComponents"></a>[ListComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListComponents.html) | Retrieve a paginated list of component summaries | List | 
| <a name="greengrass-ListCoreDevices"></a>[ListCoreDevices](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListCoreDevices.html) | Retrieve a paginated list of AWS IoT Greengrass core devices | List | 
| <a name="greengrass-ListDeployments"></a>[ListDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListDeployments.html) | Retrieves a paginated list of deployments | List | 
| <a name="greengrass-ListEffectiveDeployments"></a>[ListEffectiveDeployments](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListEffectiveDeployments.html) | Retrieves a paginated list of deployment jobs that AWS IoT Greengrass sends to AWS IoT Greengrass core devices | List | 
| <a name="greengrass-ListInstalledComponents"></a>[ListInstalledComponents](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListInstalledComponents.html) | Retrieve a paginated list of the components that a AWS IoT Greengrass core device runs | List | 
| <a name="greengrass-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ListTagsForResource.html) | List the tags for a resource | Read | 
| <a name="greengrass-ResolveComponentCandidates"></a>[ResolveComponentCandidates](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html) | List components that meet the component, version, and platform requirements of a deployment | List | 