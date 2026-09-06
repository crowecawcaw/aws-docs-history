

# AWS PrivateLink for Amazon MWAA
<a name="security-privatelink"></a>

With AWS PrivateLink, you can access Amazon MWAA from within your VPC without crossing the public internet. Interface VPC endpoints are elastic network interfaces with private IP addresses in your subnets. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint
<a name="security-privatelink-create"></a>

Amazon MWAA uses prefixes for service endpoints, where each prefix corresponds to a set of API operations:

Environment management  
`api.airflow.{{region}}.amazonaws.com` (use `api.airflow.{{region}}.api.aws` for IPv6)  
+ `CreateEnvironment`
+ `DeleteEnvironment`
+ `GetEnvironment`
+ `ListEnvironments`
+ `ListTagsForResource`
+ `TagResource`
+ `UntagResource`
+ `UpdateEnvironment`

Airflow environment  
`env.airflow.{{region}}.amazonaws.com` (use `env.airflow.{{region}}.api.aws` for IPv6)  
+ `CreateCliToken`
+ `CreateWebLoginToken`

## FIPS endpoints
<a name="security-privatelink-fips"></a>

FIPS-compliant endpoints are available in US and Canada Regions:
+ `com.amazonaws.{{region}}.airflow-fips.api`
+ `com.amazonaws.{{region}}.airflow-fips.env`

For more information about supported Regions, see [Amazon MWAA endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/mwaa.html#mwaa_region) in the *AWS General Reference*.