# Amazon OpenSearch Service endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

**OpenSearch Service API**

| Region Name                | Region         | Endpoint                                                                                           | Protocol                |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------- | ----------------------- |
| US East (Ohio)             | us-east-2      | es.us-east-2.amazonaws.com<br>es-fips.us-east-2.amazonaws.com<br>aos.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | es.us-east-1.amazonaws.com<br>es-fips.us-east-1.amazonaws.com<br>aos.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | es.us-west-1.amazonaws.com<br>es-fips.us-west-1.amazonaws.com<br>aos.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | es.us-west-2.amazonaws.com<br>es-fips.us-west-2.amazonaws.com<br>aos.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | es.af-south-1.amazonaws.com<br>aos.af-south-1.api.aws                                              | HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | es.ap-east-1.amazonaws.com<br>aos.ap-east-1.api.aws                                                | HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | es.ap-south-2.amazonaws.com<br>aos.ap-south-2.api.aws                                              | HTTPS<br>HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | es.ap-southeast-3.amazonaws.com<br>aos.ap-southeast-3.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | es.ap-southeast-5.amazonaws.com<br>aos.ap-southeast-5.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | es.ap-southeast-4.amazonaws.com<br>aos.ap-southeast-4.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | es.ap-south-1.amazonaws.com<br>aos.ap-south-1.api.aws                                              | HTTPS<br>HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | es.ap-southeast-6.amazonaws.com<br>aos.ap-southeast-6.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | es.ap-northeast-3.amazonaws.com<br>aos.ap-northeast-3.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | es.ap-northeast-2.amazonaws.com<br>aos.ap-northeast-2.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | es.ap-southeast-1.amazonaws.com<br>aos.ap-southeast-1.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | es.ap-southeast-2.amazonaws.com<br>aos.ap-southeast-2.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | es.ap-east-2.amazonaws.com<br>aos.ap-east-2.api.aws                                                | HTTPS<br>HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | es.ap-southeast-7.amazonaws.com<br>aos.ap-southeast-7.api.aws                                      | HTTPS<br>HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | es.ap-northeast-1.amazonaws.com<br>aos.ap-northeast-1.api.aws                                      | HTTPS<br>HTTPS          |
| Canada (Central)           | ca-central-1   | es.ca-central-1.amazonaws.com<br>aos.ca-central-1.api.aws                                          | HTTPS<br>HTTPS          |
| Canada West (Calgary)      | ca-west-1      | es.ca-west-1.amazonaws.com<br>aos.ca-west-1.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Frankfurt)         | eu-central-1   | es.eu-central-1.amazonaws.com<br>aos.eu-central-1.api.aws                                          | HTTPS<br>HTTPS          |
| Europe (Ireland)           | eu-west-1      | es.eu-west-1.amazonaws.com<br>aos.eu-west-1.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (London)            | eu-west-2      | es.eu-west-2.amazonaws.com<br>aos.eu-west-2.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Milan)             | eu-south-1     | es.eu-south-1.amazonaws.com<br>aos.eu-south-1.api.aws                                              | HTTPS<br>HTTPS          |
| Europe (Paris)             | eu-west-3      | es.eu-west-3.amazonaws.com<br>aos.eu-west-3.api.aws                                                | HTTPS<br>HTTPS          |
| Europe (Spain)             | eu-south-2     | es.eu-south-2.amazonaws.com<br>aos.eu-south-2.api.aws                                              | HTTPS<br>HTTPS          |
| Europe (Stockholm)         | eu-north-1     | es.eu-north-1.amazonaws.com<br>aos.eu-north-1.api.aws                                              | HTTPS<br>HTTPS          |
| Europe (Zurich)            | eu-central-2   | es.eu-central-2.amazonaws.com<br>aos.eu-central-2.api.aws                                          | HTTPS<br>HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | es.il-central-1.amazonaws.com<br>aos.il-central-1.api.aws                                          | HTTPS<br>HTTPS          |
| Mexico (Central)           | mx-central-1   | es.mx-central-1.amazonaws.com<br>aos.mx-central-1.api.aws                                          | HTTPS<br>HTTPS          |
| Middle East (Bahrain)      | me-south-1     | es.me-south-1.amazonaws.com<br>aos.me-south-1.api.aws                                              | HTTPS<br>HTTPS          |
| Middle East (UAE)          | me-central-1   | es.me-central-1.amazonaws.com<br>aos.me-central-1.api.aws                                          | HTTPS<br>HTTPS          |
| South America (São Paulo)  | sa-east-1      | es.sa-east-1.amazonaws.com<br>aos.sa-east-1.api.aws                                                | HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | es.us-gov-east-1.amazonaws.com<br>es-fips.us-gov-east-1.amazonaws.com<br>aos.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | es.us-gov-west-1.amazonaws.com<br>es-fips.us-gov-west-1.amazonaws.com<br>aos.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS |

**OpenSearch Serverless API**

| Region Name               | Region         | Endpoint                                                                                                                                                                                                         | Protocol                                  |
| ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| US East (Ohio)            | us-east-2      | aoss.us-east-2.amazonaws.com<br>dashboards.us-east-2.aoss-fips.amazonaws.com<br>us-east-2.aoss.amazonaws.com<br>dashboards.us-east-2.aoss.amazonaws.com<br>us-east-2.aoss-fips.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | aoss.us-east-1.amazonaws.com<br>us-east-1.aoss.amazonaws.com<br>dashboards.us-east-1.aoss.amazonaws.com<br>dashboards.us-east-1.aoss-fips.amazonaws.com<br>us-east-1.aoss-fips.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | aoss.us-west-1.amazonaws.com<br>dashboards.us-west-1.aoss-fips.amazonaws.com<br>dashboards.us-west-1.aoss.amazonaws.com<br>us-west-1.aoss.amazonaws.com<br>us-west-1.aoss-fips.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | aoss.us-west-2.amazonaws.com<br>dashboards.us-west-2.aoss-fips.amazonaws.com<br>dashboards.us-west-2.aoss.amazonaws.com<br>us-west-2.aoss.amazonaws.com<br>us-west-2.aoss-fips.amazonaws.com                     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Asia Pacific (Hong Kong)  | ap-east-1      | aoss.ap-east-1.amazonaws.com<br>ap-east-1.aoss.amazonaws.com<br>dashboards.ap-east-1.aoss.amazonaws.com                                                                                                          | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)  | ap-south-2     | aoss.ap-south-2.amazonaws.com<br>dashboards.ap-south-2.aoss.amazonaws.com<br>ap-south-2.aoss.amazonaws.com                                                                                                       | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)     | ap-south-1     | aoss.ap-south-1.amazonaws.com<br>dashboards.ap-south-1.aoss.amazonaws.com<br>ap-south-1.aoss.amazonaws.com                                                                                                       | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)      | ap-northeast-3 | aoss.ap-northeast-3.amazonaws.com<br>ap-northeast-3.aoss.amazonaws.com<br>dashboards.ap-northeast-3.aoss.amazonaws.com                                                                                           | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)      | ap-northeast-2 | aoss.ap-northeast-2.amazonaws.com<br>dashboards.ap-northeast-2.aoss.amazonaws.com<br>ap-northeast-2.aoss.amazonaws.com                                                                                           | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)  | ap-southeast-1 | aoss.ap-southeast-1.amazonaws.com<br>dashboards.ap-southeast-1.aoss.amazonaws.com<br>ap-southeast-1.aoss.amazonaws.com                                                                                           | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)     | ap-southeast-2 | aoss.ap-southeast-2.amazonaws.com<br>dashboards.ap-southeast-2.aoss.amazonaws.com<br>ap-southeast-2.aoss.amazonaws.com                                                                                           | HTTPS<br>HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)      | ap-northeast-1 | aoss.ap-northeast-1.amazonaws.com<br>dashboards.ap-northeast-1.aoss.amazonaws.com<br>ap-northeast-1.aoss.amazonaws.com                                                                                           | HTTPS<br>HTTPS<br>HTTPS                   |
| Canada (Central)          | ca-central-1   | aoss.ca-central-1.amazonaws.com<br>ca-central-1.aoss-fips.amazonaws.com<br>dashboards.ca-central-1.aoss-fips.amazonaws.com<br>dashboards.ca-central-1.aoss.amazonaws.com<br>ca-central-1.aoss.amazonaws.com      | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | aoss.eu-central-1.amazonaws.com<br>dashboards.eu-central-1.aoss.amazonaws.com<br>eu-central-1.aoss.amazonaws.com                                                                                                 | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Ireland)          | eu-west-1      | aoss.eu-west-1.amazonaws.com<br>eu-west-1.aoss.amazonaws.com<br>dashboards.eu-west-1.aoss.amazonaws.com                                                                                                          | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (London)           | eu-west-2      | aoss.eu-west-2.amazonaws.com<br>eu-west-2.aoss.amazonaws.com<br>dashboards.eu-west-2.aoss.amazonaws.com                                                                                                          | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Milan)            | eu-south-1     | aoss.eu-south-1.amazonaws.com<br>eu-south-1.aoss.amazonaws.com<br>dashboards.eu-south-1.aoss.amazonaws.com                                                                                                       | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Paris)            | eu-west-3      | aoss.eu-west-3.amazonaws.com<br>eu-west-3.aoss.amazonaws.com<br>dashboards.eu-west-3.aoss.amazonaws.com                                                                                                          | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Spain)            | eu-south-2     | aoss.eu-south-2.amazonaws.com<br>dashboards.eu-south-2.aoss.amazonaws.com<br>eu-south-2.aoss.amazonaws.com                                                                                                       | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Stockholm)        | eu-north-1     | aoss.eu-north-1.amazonaws.com<br>eu-north-1.aoss.amazonaws.com<br>dashboards.eu-north-1.aoss.amazonaws.com                                                                                                       | HTTPS<br>HTTPS<br>HTTPS                   |
| Europe (Zurich)           | eu-central-2   | aoss.eu-central-2.amazonaws.com<br>eu-central-2.aoss.amazonaws.com<br>dashboards.eu-central-2.aoss.amazonaws.com                                                                                                 | HTTPS<br>HTTPS<br>HTTPS                   |
| South America (São Paulo) | sa-east-1      | aoss.sa-east-1.amazonaws.com<br>sa-east-1.aoss.amazonaws.com<br>dashboards.sa-east-1.aoss.amazonaws.com                                                                                                          | HTTPS<br>HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)    | us-gov-east-1  | aoss.us-gov-east-1.amazonaws.com<br>us-gov-east-1.aoss-fips.amazonaws.com<br>dashboards.us-gov-east-1.aoss-fips.amazonaws.com<br>us-gov-east-1.aoss.amazonaws.com<br>dashboards.us-gov-east-1.aoss.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | aoss.us-gov-west-1.amazonaws.com<br>dashboards.us-gov-west-1.aoss.amazonaws.com<br>us-gov-west-1.aoss-fips.amazonaws.com<br>us-gov-west-1.aoss.amazonaws.com<br>dashboards.us-gov-west-1.aoss-fips.amazonaws.com | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

**OpenSearch Ingestion API**

| Region Name               | Region         | Endpoint                          | Protocol |
| ------------------------- | -------------- | --------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | osis.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | osis.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)   | us-west-1      | osis.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | osis.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | osis.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | osis.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | osis.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | osis.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | osis.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | osis.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | osis.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | osis.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | osis.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | osis.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | osis.eu-north-1.amazonaws.com     | HTTPS    |
| South America (São Paulo) | sa-east-1      | osis.sa-east-1.amazonaws.com      | HTTPS    |

## Service quotas

For more information, see [Amazon OpenSearch Service
quotas](../../../opensearch-service/latest/developerguide/limits.md "../../../opensearch-service/latest/developerguide/limits.md").

### OpenSearch Service domain and instance quotas

Your AWS account has the following quotas related to OpenSearch Service domains:

| Name                                    | Default                    | Adjustable                                                                                                                                                               | Description                                                                                                                                |
| --------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Dedicated master instances per domain   | Each supported Region: 5   | No                                                                                                                                                                       | The maximum number of dedicated master instances in a single Amazon OpenSearch Service domain.                                             |
| Domains per Region                      | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/es/quotas/L-076D529E "https://console.aws.amazon.com/servicequotas/home/services/es/quotas/L-076D529E") | The maximum number of Amazon OpenSearch Service domains you can create in each AWS Region.                                                 |
| Instances per domain                    | Each supported Region: 80  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/es/quotas/L-6408ABDE "https://console.aws.amazon.com/servicequotas/home/services/es/quotas/L-6408ABDE") | The maximum number of instances in a single Amazon OpenSearch Service domain. You can request an increase up to 1002 instances per domain. |
| Instances per domain (T2 instance type) | Each supported Region: 10  | No                                                                                                                                                                       | The maximum number of T2 instances in a single Amazon OpenSearch Service domain.                                                           |
| Warm instances per domain               | Each supported Region: 150 | No                                                                                                                                                                       | The maximum number of warm nodes in a single Amazon OpenSearch Service cluster.                                                            |

Your AWS account has the following additional OpenSearch Service limits:

| Name                       | Default | Adjustable | Notes                                                                                                                                                                                                                      |
| -------------------------- | ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total storage per domain   | 3 PiB   | No         | This maximum is the sum of all data nodes and warm nodes. For<br>example, your domain might have 45 `r6gd.16xlarge.search`<br>instances and 140 `ultrawarm1.large.search` instances for<br>a total of 2.88 PiB of storage. |
| Custom packages per Region | 25      | No         |                                                                                                                                                                                                                            |
| Custom packages per domain | 20      | No         |                                                                                                                                                                                                                            |

### OpenSearch Serverless quotas

Your AWS account has the following quotas related to OpenSearch Serverless
resources.

To view the quotas for OpenSearch Serverless, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home"). In the navigation pane, choose
**AWS services** and select **Amazon OpenSearch
Serverless**.

| Name                             | Default      | Adjustable | Notes |
| -------------------------------- | ------------ | ---------- | ----- |
| Default indexing capacity (OCUs) | 10           | No         |       |
| Default search capacity (OCUs)   | 10           | No         |       |
| Maximum indexing capacity (OCUs) | 1,700        | No         |       |
| Maximum search capacity (OCUs)   | 1,700        | No         |       |
| Data access policies             | 500          | No         |       |
| Encryption policies              | 150          | No         |       |
| Network policies                 | 500          | No         |       |
| SAML providers                   | 50           | No         |       |
| Data access policy size          | 10,240 bytes | No         |       |
| Network policy size              | 10,240 bytes | No         |       |
| SAML provider size               | 51,200 bytes | No         |       |
| Encryption policy size           | 10,240 bytes | No         |       |

Your AWS account has the following additional OpenSearch Serverless
limits:

| Name                                                           | Default       | Adjustable | Notes                                                                                                                                   |
| -------------------------------------------------------------- | ------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Collection tags                                                | 50            | No         |                                                                                                                                         |
| Collections with unique KMS keys                               | Maximum OCU/2 | No         | This limit depends on the maximum number of OCUs you set and how<br>many OCUs are already in use.                                       |
| OpenSearch Serverless-managed VPC endpoints                    | 50            | No         | This limit only applies to OpenSearch Serverless-managed VPC<br>endpoints. It doesn't include OpenSearch Service-managed VPC endpoints. |
| Indexes per Amazon OpenSearch Serverless collection            | 1000          | No         | The maximum number of indexes per Amazon OpenSearch Serverless<br>collection is 1000.                                                   |
| Index templates per Amazon OpenSearch Serverless<br>collection | 500           | No         | The maximum number of index templates per Amazon OpenSearch<br>Serverless collection is 500.                                            |

### OpenSearch Ingestion quotas

Your AWS account has the following quotas related to OpenSearch Ingestion
resources. Unless otherwise noted, each quota is
Region-specific.

| Name                                          | Default                       | Adjustable | Notes                                                                                                                                                                                                                                                                                     |
| --------------------------------------------- | ----------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connected VPCs per pipeline                   | Each supported Region: 1      | No         |                                                                                                                                                                                                                                                                                           |
| Pipelines connected to a single VPC domain    | Each supported Region: 50     | No         |                                                                                                                                                                                                                                                                                           |
| Pipelines                                     | Each supported Region: 50     | No         |                                                                                                                                                                                                                                                                                           |
| Characters per pipeline configuration         | Each supported Region: 24000  | No         |                                                                                                                                                                                                                                                                                           |
| Sources per pipeline                          | Each supported Region: 100000 | No         | This limit only applies to _plugin_<br>sources, such as HTTP, OTel, or S3. You can still chain<br>sub-pipelines together within a single OpenSearch Ingestion<br>pipeline configuration.                                                                                                  |
| Unique OpenSearch sinks per pipeline          | Each supported Region: 1      | No         | This limit only applies to OpenSearch<br>*domain<br>• and<br>*collection<br>• sinks. You can still chain<br>sub-pipelines together within a single OpenSearch Ingestion<br>pipeline configuration.                                                                                        |
| Total OpenSearch sinks per pipeline           | Each supported Region: 50     | No         | This limit refers to the number of times that you can specify<br>the same OpenSearch sink within a pipeline configuration file.<br>The number of non "pipeline" sinks within the<br>`pipelineConfigurationBody` must be between 1 and<br>20, inclusive of OpenSearch Ingestion pipelines. |
| Minimum Ingestion OCUs per pipeline           | Each supported Region: 1      | No         |                                                                                                                                                                                                                                                                                           |
| Maximum Ingestion OCUs per stateless pipeline | Each supported Region: 96     | No         | See [Stateless versus stateful processors](../../../opensearch-service/latest/developerguide/pipeline-config-reference.md#processor-stateful-stateless "../../../opensearch-service/latest/developerguide/pipeline-config-reference.md#processor-stateful-stateless").                    |
| Maximum Ingestion OCUs per stateful pipeline  | Each supported Region: 48     | No         | See [Stateless versus stateful processors](../../../opensearch-service/latest/developerguide/pipeline-config-reference.md#processor-stateful-stateless "../../../opensearch-service/latest/developerguide/pipeline-config-reference.md#processor-stateful-stateless").                    |
