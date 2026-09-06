

# Data retrieval APIs for AWS CodeConnections
<a name="awscodeconnections"></a>

AWS CodeConnections provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="codeconnections-GetConnection"></a>[GetConnection](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetConnection.html) | Get details about a Connection resource | Read | 
| <a name="codeconnections-GetConnectionToken"></a>[GetConnectionToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-getconnectiontoken) | Get a Connection token to call provider actions | Read | 
| <a name="codeconnections-GetHost"></a>[GetHost](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetHost.html) | Get details about a host resource | Read | 
| <a name="codeconnections-GetIndividualAccessToken"></a>[GetIndividualAccessToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codeconnections-GetInstallationUrl"></a>[GetInstallationUrl](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codeconnections-GetRepositoryLink"></a>[GetRepositoryLink](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositoryLink.html) | Describe a repository link | Read | 
| <a name="codeconnections-GetRepositorySyncStatus"></a>[GetRepositorySyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetRepositorySyncStatus.html) | Get the latest sync status for a repository | Read | 
| <a name="codeconnections-GetResourceSyncStatus"></a>[GetResourceSyncStatus](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetResourceSyncStatus.html) | Get the latest sync status for a resource (cfn stack or other resources) | Read | 
| <a name="codeconnections-GetSyncBlockerSummary"></a>[GetSyncBlockerSummary](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncBlockerSummary.html) | Describe service sync blockers on a resource (cfn stack or other resources) | Read | 
| <a name="codeconnections-GetSyncConfiguration"></a>[GetSyncConfiguration](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_GetSyncConfiguration.html) | Describe a sync configuration | Read | 
| <a name="codeconnections-ListConnections"></a>[ListConnections](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListConnections.html) | List Connection resources | List | 
| <a name="codeconnections-ListHosts"></a>[ListHosts](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListHosts.html) | List host resources | List | 
| <a name="codeconnections-ListInstallationTargets"></a>[ListInstallationTargets](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | List | 
| <a name="codeconnections-ListRepositoryLinks"></a>[ListRepositoryLinks](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositoryLinks.html) | List repository links | List | 
| <a name="codeconnections-ListRepositorySyncDefinitions"></a>[ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListRepositorySyncDefinitions.html) | List repository sync definitions | List | 
| <a name="codeconnections-ListSyncConfigurations"></a>[ListSyncConfigurations](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListSyncConfigurations.html) | List sync configurations for a repository link | List | 
| <a name="codeconnections-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_ListTagsForResource.html) | The set of key-value pairs that are used to manage the resource | List | 
| <a name="codeconnections-PassConnection"></a>[PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection) | Pass a Connection resource to an AWS service that accepts a Connection ARN as input, such as codepipeline:CreatePipeline | Read | 
| <a name="codeconnections-PassRepository"></a>[PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository) | Pass a repository link resource to an AWS service that accepts a RepositoryLinkId as input, such as codeconnections:CreateSyncConfiguration | Read | 
| <a name="codeconnections-RegisterAppCode"></a>[RegisterAppCode](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration) | Associate a third party server, such as a GitHub Enterprise Server instance, with a Host | Read | 
| <a name="codeconnections-StartAppRegistrationHandshake"></a>[StartAppRegistrationHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration) | Associate a third party server, such as a GitHub Enterprise Server instance, with a Host | Read | 
| <a name="codeconnections-StartOAuthHandshake"></a>[StartOAuthHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codeconnections-UseConnection"></a>[UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use) | Use a Connection resource to call provider actions | Read | 