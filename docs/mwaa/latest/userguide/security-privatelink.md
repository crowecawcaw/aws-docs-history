# AWS PrivateLink for Amazon MWAA

With AWS PrivateLink, you can access Amazon MWAA from within your VPC without crossing the public internet. Interface VPC endpoints are elastic network interfaces with private IP addresses in your subnets. For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User Guide_.

## Creating a VPC endpoint

Amazon MWAA uses prefixes for service endpoints, where each prefix corresponds to a set of API operations:

Environment management

`api.airflow.`region`.amazonaws.com` (use `api.airflow.`region`.api.aws` for IPv6)

- `CreateEnvironment`
- `DeleteEnvironment`
- `GetEnvironment`
- `ListEnvironments`
- `ListTagsForResource`
- `TagResource`
- `UntagResource`
- `UpdateEnvironment`

Airflow environment

`env.airflow.`region`.amazonaws.com` (use `env.airflow.`region`.api.aws` for IPv6)

- `CreateCliToken`
- `CreateWebLoginToken`

## FIPS endpoints

FIPS-compliant endpoints are available in US and Canada Regions:

- `com.amazonaws.`region`.airflow-fips.api`
- `com.amazonaws.`region`.airflow-fips.env`

For more information about supported Regions, see [Amazon MWAA endpoints and quotas](../../../general/latest/gr/mwaa.md#mwaa_region "../../../general/latest/gr/mwaa.md#mwaa_region") in the _AWS General Reference_.
