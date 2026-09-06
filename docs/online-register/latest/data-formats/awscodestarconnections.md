

# Data retrieval APIs for AWS CodeStar Connections
<a name="awscodestarconnections"></a>

AWS CodeStar Connections provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="codestar-connections-GetConnection"></a>[GetConnection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetConnection.html) | Get details about a Connection resource | Read | 
| <a name="codestar-connections-GetConnectionToken"></a>[GetConnectionToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-getconnectiontoken) | Get a Connection token to call provider actions | Read | 
| <a name="codestar-connections-GetHost"></a>[GetHost](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetHost.html) | Get details about a host resource | Read | 
| <a name="codestar-connections-GetIndividualAccessToken"></a>[GetIndividualAccessToken](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codestar-connections-GetInstallationUrl"></a>[GetInstallationUrl](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codestar-connections-GetRepositoryLink"></a>[GetRepositoryLink](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositoryLink.html) | Describe a repository link | Read | 
| <a name="codestar-connections-GetRepositorySyncStatus"></a>[GetRepositorySyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetRepositorySyncStatus.html) | Get the latest sync status for a repository | Read | 
| <a name="codestar-connections-GetResourceSyncStatus"></a>[GetResourceSyncStatus](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetResourceSyncStatus.html) | Get the latest sync status for a resource (cfn stack or other resources) | Read | 
| <a name="codestar-connections-GetSyncBlockerSummary"></a>[GetSyncBlockerSummary](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncBlockerSummary.html) | Describe service sync blockers on a resource (cfn stack or other resources) | Read | 
| <a name="codestar-connections-GetSyncConfiguration"></a>[GetSyncConfiguration](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_GetSyncConfiguration.html) | Describe a sync configuration | Read | 
| <a name="codestar-connections-ListConnections"></a>[ListConnections](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListConnections.html) | List Connection resources | List | 
| <a name="codestar-connections-ListHosts"></a>[ListHosts](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListHosts.html) | List host resources | List | 
| <a name="codestar-connections-ListInstallationTargets"></a>[ListInstallationTargets](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | List | 
| <a name="codestar-connections-ListRepositoryLinks"></a>[ListRepositoryLinks](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListRepositoryLinks.html) | List repository links | List | 
| <a name="codestar-connections-ListRepositorySyncDefinitions"></a>[ListRepositorySyncDefinitions](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListRepositorySyncDefinitions.html) | List repository sync definitions | List | 
| <a name="codestar-connections-ListSyncConfigurations"></a>[ListSyncConfigurations](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListSyncConfigurations.html) | List sync configurations for a repository link | List | 
| <a name="codestar-connections-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_ListTagsForResource.html) | The set of key-value pairs that are used to manage the resource | List | 
| <a name="codestar-connections-PassConnection"></a>[PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection) | Pass a Connection resource to an AWS service that accepts a Connection ARN as input, such as codepipeline:CreatePipeline | Read | 
| <a name="codestar-connections-PassRepository"></a>[PassRepository](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passrepository) | Pass a repository link resource to an AWS service that accepts a RepositoryLinkId as input, such as codestar-connections:CreateSyncConfiguration | Read | 
| <a name="codestar-connections-RegisterAppCode"></a>[RegisterAppCode](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration) | Associate a third party server, such as a GitHub Enterprise Server instance, with a Host | Read | 
| <a name="codestar-connections-StartAppRegistrationHandshake"></a>[StartAppRegistrationHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#connections-permissions-actions-host-registration) | Associate a third party server, such as a GitHub Enterprise Server instance, with a Host | Read | 
| <a name="codestar-connections-StartOAuthHandshake"></a>[StartOAuthHandshake](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-handshake) | Associate a third party, such as a Bitbucket App installation, with a Connection | Read | 
| <a name="codestar-connections-UseConnection"></a>[UseConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-use) | Use a Connection resource to call provider actions | Read | 