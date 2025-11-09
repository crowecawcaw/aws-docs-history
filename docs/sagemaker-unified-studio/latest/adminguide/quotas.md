# Quotas and limits for Amazon SageMaker Unified Studio

Your AWS account has default quotas, formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is account specific and region-specific.

## Resource quotas

The resource quotas are applied at the account level, meaning the depletion of
resource quotas in one project can affect all other projects within the account.

Amazon SageMaker Unified Studio has the following quotas and limits.

| Resource                                                                                                                                                              | Default |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Maximum number of account pools for your Amazon SageMaker unified<br>domain                                                                                           | 100     |
| Maximum number of JupyterLab instances                                                                                                                                | 4000    |
| Maximum number of project members for your Amazon SageMaker unified<br>domain. The total number of project members is the product of project<br>members and projects. | 6000    |
| Maximum number of spaces                                                                                                                                              | 6000    |
| Maximum number of projects                                                                                                                                            | 500     |
| Maximum number of Micro environments                                                                                                                                  | 200     |

### Amazon DataZone quotas

The following table describes quotas for Amazon DataZone:

| Resource                | Description                                                                        | Value     |
| ----------------------- | ---------------------------------------------------------------------------------- | --------- |
| Data Asset Types        | The maximum number of data asset types that can be created in a DataZone domain    | 1000      |
| Data assets             | The maximum number of data assets that can be created in an Amazon DataZone domain | 1 million |
| Glossaries              | The maximum number of business glossaries you can create in a domain               | 1000      |
| Business glossary terms | The maximum number of total business glossary terms you can create in a domain     | 10000     |
| Number of asset filters | The maximum number of asset filters per Amazon DataZone domain                     | 100       |

### Amazon DataZone API rate limits

The following table describes rate limits for the Amazon DataZone APIs. These limits
apply per AWS account per Region.

| API                | API rate limit                  |
| ------------------ | ------------------------------- |
| CreateGlossary     | 5 transactions per second (TPS) |
| UpdateGlossary     | 20 TPS                          |
| GetGlossary        | 20 TPS                          |
| DeleteGlossary     | 20 TPS                          |
| UpdateGlossaryTerm | 20 TPS                          |
| DeleteGlossaryTerm | 20 TPS                          |
| CreateAsset        | 20 TPS                          |
| UpdateAsset        | 20 TPS                          |

For more information about other AWS service quotas, see [AWS
service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

For more quotas information, see the following:

- [Amazon SageMaker Supported Regions and Quotas](../../../sagemaker/latest/dg/regions-quotas.md "../../../sagemaker/latest/dg/regions-quotas.md")
- [Amazon
  Managed Workflows for Apache Airflow endpoints and quotas](../../../general/latest/gr/mwaa.md "../../../general/latest/gr/mwaa.md")
- [Amazon Redshift endpoints and quotas](../../../general/latest/gr/redshift-service.md "../../../general/latest/gr/redshift-service.md")
- [Amazon EMR
  endpoints and quotas](../../../general/latest/gr/emr.md "../../../general/latest/gr/emr.md")
- [Amazon Q
  Business endpoints and quotas](../../../general/latest/gr/amazonq.md "../../../general/latest/gr/amazonq.md")
- [Amazon
  Athena endpoints and quotas](../../../general/latest/gr/athena.md "../../../general/latest/gr/athena.md")
- [Amazon
  Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md")
- [AWS Glue
  endpoints and quotas](../../../general/latest/gr/glue.md "../../../general/latest/gr/glue.md")
