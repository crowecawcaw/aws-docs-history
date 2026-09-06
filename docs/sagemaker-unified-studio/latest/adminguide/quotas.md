

# Quotas and limits for Amazon SageMaker Unified Studio
<a name="quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is account specific and region-specific.

## Resource quotas
<a name="resource-limits"></a>

The resource quotas are applied at the account level, meaning the depletion of resource quotas in one project can affect all other projects within the account. 

Amazon SageMaker Unified Studio has the following quotas and limits.


| Resource | Default | 
| --- | --- | 
| Maximum number of account pools for your Amazon SageMaker unified domain | 100 | 
| Maximum number of JupyterLab instances | 4000 | 
| Maximum number of user type project members per project | 100 | 
| Maximum number of group type project members per project | 20 | 
| Maximum number of spaces | 6000 | 
| Maximum number of projects | 1000 | 
| Maximum number of environments | 1000 | 
| Maximum number of Micro environments  | 200 | 

### Amazon DataZone quotas
<a name="amazon-datazone-quotas"></a>

The following table describes quotas for Amazon DataZone:


| Resource | Description | Value | 
| --- | --- | --- | 
| Data Asset Types | The maximum number of data asset types that can be created in a DataZone domain | 1000 | 
| Data assets | The maximum number of data assets that can be created in an Amazon DataZone domain | 1 million | 
| Glossaries | The maximum number of business glossaries you can create in a domain | 1000 | 
| Business glossary terms | The maximum number of total business glossary terms you can create in a domain | 10000 | 
| Number of asset filters | The maximum number of asset filters per Amazon DataZone domain | 100 | 

### Amazon DataZone API rate limits
<a name="datazone-api-quotas"></a>

The following table describes rate limits for the Amazon DataZone APIs. These limits apply per AWS account per Region.


| API | API rate limit | 
| --- | --- | 
| CreateGlossary | 5 transactions per second (TPS) | 
| UpdateGlossary | 20 TPS | 
| GetGlossary | 20 TPS | 
| DeleteGlossary | 20 TPS | 
| UpdateGlossaryTerm | 20 TPS | 
| DeleteGlossaryTerm | 20 TPS | 
| CreateAsset | 20 TPS | 
| UpdateAsset | 20 TPS | 

For more information about other AWS service quotas, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

For more quotas information, see the following:
+ [Amazon SageMaker Supported Regions and Quotas](https://docs.aws.amazon.com/sagemaker/latest/dg/regions-quotas.html)
+ [Amazon Managed Workflows for Apache Airflow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mwaa.html)
+ [Amazon Redshift endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/redshift-service.html)
+ [Amazon EMR endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/emr.html)
+ [Amazon Q Business endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/amazonq.html)
+ [Amazon Athena endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/athena.html)
+ [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html)
+ [AWS Glue endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/glue.html)