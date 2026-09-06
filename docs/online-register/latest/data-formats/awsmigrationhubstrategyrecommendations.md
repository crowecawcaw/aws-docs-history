

# Data retrieval APIs for AWS Migration Hub Strategy Recommendations
<a name="awsmigrationhubstrategyrecommendations"></a>

AWS Migration Hub Strategy Recommendations provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="migrationhub-strategy-GetAntiPattern"></a>[GetAntiPattern](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAntiPattern.html) | Get details of each anti pattern that collector should look at in a customer's environment | Read | 
| <a name="migrationhub-strategy-GetApplicationComponentDetails"></a>[GetApplicationComponentDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentDetails.html) | Get details of an application | Read | 
| <a name="migrationhub-strategy-GetApplicationComponentStrategies"></a>[GetApplicationComponentStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentStrategies.html) | Get a list of all recommended strategies and tools for an application running in a server | Read | 
| <a name="migrationhub-strategy-GetAssessment"></a>[GetAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAssessment.html) | Retrieve status of an on-going assessment | Read | 
| <a name="migrationhub-strategy-GetImportFileTask"></a>[GetImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetImportFileTask.html) | Get details of a specific import task | Read | 
| <a name="migrationhub-strategy-GetLatestAssessmentId"></a>[GetLatestAssessmentId](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetLatestAssessmentId.html) | Retrieve the latest assessment id | Read | 
| <a name="migrationhub-strategy-GetMessage"></a>[GetMessage](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetMessage.html) | The collector to receive information from the service | Read | 
| <a name="migrationhub-strategy-GetPortfolioPreferences"></a>[GetPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioPreferences.html) | Retrieve customer migration/Modernization preferences | Read | 
| <a name="migrationhub-strategy-GetPortfolioSummary"></a>[GetPortfolioSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioSummary.html) | Retrieve overall summary (number-of servers to rehost etc as well as overall number of anti patterns) | Read | 
| <a name="migrationhub-strategy-GetRecommendationReportDetails"></a>[GetRecommendationReportDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetRecommendationReportDetails.html) | Retrieve detailed information about a recommendation report | Read | 
| <a name="migrationhub-strategy-GetServerDetails"></a>[GetServerDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html) | Get info about a specific server | Read | 
| <a name="migrationhub-strategy-GetServerStrategies"></a>[GetServerStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerStrategies.html) | Get recommended strategies and tools for a specific server | Read | 
| <a name="migrationhub-strategy-ListAnalyzableServers"></a>[ListAnalyzableServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAnalyzableServers.html) | Get a list of all analyzable servers in a customer's vcenter environment | List | 
| <a name="migrationhub-strategy-ListAntiPatterns"></a>[ListAntiPatterns](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListAntiPatterns.html) | Get a list of all anti patterns that collector should look for in a customer's environment | List | 
| <a name="migrationhub-strategy-ListApplicationComponents"></a>[ListApplicationComponents](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListApplicationComponents.html) | Get a list of all applications running on servers on customer's servers | List | 
| <a name="migrationhub-strategy-ListCollectors"></a>[ListCollectors](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListCollectors.html) | Get a list of all collectors installed by the customer | List | 
| <a name="migrationhub-strategy-ListImportFileTask"></a>[ListImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListImportFileTask.html) | Get list of all imports performed by the customer | List | 
| <a name="migrationhub-strategy-ListJarArtifacts"></a>[ListJarArtifacts](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListJarArtifacts.html) | Get a list of binaries that collector should assess | List | 
| <a name="migrationhub-strategy-ListServers"></a>[ListServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListServers.html) | Get a list of all servers in a customer's environment | List | 