# Quotas for Amazon DataZone

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is region-specific.

Amazon DataZone has the following quotas and limits.

## Amazon DataZone quotas

| Resource                           | Description                                                                        | Value     |
| ---------------------------------- | ---------------------------------------------------------------------------------- | --------- |
| Data Asset Types                   | The maximum number of data asset types that can be created in a DataZone domain    | 1000      |
| Data assets                        | The maximum number of data assets that can be created in an Amazon DataZone domain | 1 million |
| Glossaries                         | The maximum number of business glossaries you can create in a domain               | 1000      |
| Business glossary terms            | The maximum number of total business glossary terms you can create in a domain     | 10000     |
| Environments in a domain           | The maximum number of environments in an Amazon DataZone domain                    | 500       |
| Number of asset filters per asset  | The maximum number of asset filters per Amazon DataZone asset                      | 100       |
| Number of filters per subscription | The maximum number of filters per Amazon DataZone subscription                     | 5         |
| Domain units in a domain           | The maximum number of domain units in an Amazon DataZone domain                    | 500       |
| Hierarchy levels in a domain unit  | The maximum number of hierarchy levels for a domain unit                           | 5         |
| Grants per policy per domain unit  | The maximum number of grants per policy per domain unit                            | 20        |
| Data products                      | The maximum number of data products that can be created in a DataZone domain       | 500,000   |
| Data source runs                   | The maximum number of data source runs per data source per day                     | 25        |

## Amazon DataZone API rate limits

The following table describes rate limits for the Amazon DataZone APIs. These limits apply per AWS
account per Region.

| Amazon DataZone API rate limits          | API                             | API rate limit |
| ---------------------------------------- | ------------------------------- | -------------- |
| **CreateGlossary**                       | 5 transactions per second (TPS) |
| **UpdateGlossary**                       | 20 TPS                          |
| **GetGlossary**                          | 20 TPS                          |
| **DeleteGlossary**                       | 20 TPS                          |
| **UpdateGlossaryTerm**                   | 20 TPS                          |
| **DeleteGlossaryTerm**                   | 20 TPS                          |
| **CreateAsset**                          | 20 TPS                          |
| **ListAssetRevisions**                   | 20 TPS                          |
| **CreateAssetRevision**                  | 20 TPS                          |
| **DeleteAsset**                          | 20 TPS                          |
| **CreateDataProduct**                    | 20 TPS                          |
| **ListDataProductRevisions**             | 20 TPS                          |
| **CreateDataProductRevision**            | 20 TPS                          |
| **DeleteDataProduct**                    | 20 TPS                          |
| **CreateAssetType**                      | 20 TPS                          |
| **DeleteAssetType**                      | 20 TPS                          |
| **CreateFormType**                       | 20 TPS                          |
| **DeleteFormType**                       | 20 TPS                          |
| **Search**                               | 20 TPS                          |
| **SearchTypes**                          | 20 TPS                          |
| **AcceptPredictions**                    | 20 TPS                          |
| **RejectPredictions**                    | 20 TPS                          |
| **AcceptSubscriptionRequest**            | 3 TPS                           |
| **CancelSubscription**                   | 3 TPS                           |
| **CreateSubscriptionGrant**              | 3 TPS                           |
| **CreateSubscriptionRequest**            | 3 TPS                           |
| **GetSubscriptionEligibility**           | 30 TPS                          |
| **DeleteSubscriptionGrant**              | 3 TPS                           |
| **DeleteSubscriptionRequest**            | 3 TPS                           |
| **DeleteSubscriptionTarget**             | 3 TPS                           |
| **GetSubscription**                      | 8 TPS                           |
| **GetSubscriptionGrant**                 | 8 TPS                           |
| **GetSubscriptionRequestDetails**        | 8 TPS                           |
| **ListSubscriptionGrants**               | 8 TPS                           |
| **ListSubscriptionRequests**             | 8 TPS                           |
| **ListSubscriptions**                    | 8 TPS                           |
| **ListSubscriptionTargets**              | 8 TPS                           |
| **RejectSubscriptionRequest**            | 3 TPS                           |
| **RevokeSubscription**                   | 3 TPS                           |
| **UpdateSubscriptionRequest**            | 3 TPS                           |
| **UpdateSubscriptionTarget**             | 3 TPS                           |
| **CreateProjectProfile**                 | 3 TPS                           |
| **UpdateProjectProfile**                 | 3 TPS                           |
| **CreateDomain**                         | 8 TPS                           |
| **UpdateDomain**                         | 8 TPS                           |
| **CreateProject**                        | 3 TPS                           |
| **UpdateProject**                        | 3 TPS                           |
| **DeleteProject**                        | 3 TPS                           |
| **ListProjects**                         | 8 TPS                           |
| **CreateProjectMembership**              | 3 TPS                           |
| **ListProjectMemberships**               | 8 TPS                           |
| **DeleteProjectMembership**              | 3 TPS                           |
| **CreateEnvironment**                    | 3 TPS                           |
| **DeleteEnvironment**                    | 3 TPS                           |
| **UpdateEnvironment**                    | 3 TPS                           |
| **ListEnvironments**                     | 8 TPS                           |
| **GetEnvironment**                       | 8 TPS                           |
| **GetEnvironmentCredentials**            | 8 TPS                           |
| **CreateEnvironmentProfile**             | 8 TPS                           |
| **ListEnvironmentProfiles**              | 8 TPS                           |
| **ListEnvironmentBlueprints**            | 8 TPS                           |
| **PutEnvironmentBlueprintConfiguration** | 10 TPS                          |
| **StartMetadataGenerationRun**           | 10 TPS                          |
| **CancelMetadataGenerationRun**          | 20 TPS                          |
| **CreateDomainUnit**                     | 20 TPS                          |
| **AddPolicyGrant**                       | 20 TPS                          |
| **AddEntityOwner**                       | 20 TPS                          |
| **CreateRule**                           | 20 TPS                          |
| **UpdateRule**                           | 20 TPS                          |
| **CreateDataSource**                     | 20 TPS                          |
| **UpdateDataSource**                     | 20 TPS                          |
| **DeleteDataSource**                     | 20 TPS                          |
| **ListDataSources**                      | 20 TPS                          |
| **SearchListings**                       | 16 TPS                          |
| **StartDataSourceRun**                   | 20 TPS                          |
| **UpdateDataSourceRunActivities**        | 20 TPS                          |
| **PostLineageEvent**                     | 20 TPS                          |
| **CreateConnection**                     | 20 TPS                          |
| **UpdateConnection**                     | 20 TPS                          |
| **GetConnection**                        | 20 TPS                          |
| **ListConnections**                      | 20 TPS                          |
| **DeleteConnection**                     | 20 TPS                          |
| **CreateListingChangeSet**               | 20 TPS                          |
