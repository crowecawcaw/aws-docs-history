# Amazon Managed Workflows for Apache Airflow service endpoints and quotas

Amazon Managed Workflows for Apache Airflow has the following service quotas and endpoints. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

###### Contents

- [Service endpoints](mwaa-quotas.md#quotas-endpoints "mwaa-quotas.md#quotas-endpoints")
- [Service quotas](mwaa-quotas.md#quotas-list "mwaa-quotas.md#quotas-list")
- [Increasing quotas](mwaa-quotas.md#quotas-increase "mwaa-quotas.md#quotas-increase")

## Service endpoints

To access a list of endpoints for Amazon MWAA, refer to [Amazon Managed Workflows for Apache Airflow endpoints and quotas](../../../general/latest/gr/mwaa.md "../../../general/latest/gr/mwaa.md").

## Service quotas

| Quota name                 | Description                                                            | Default quota | Adjustable |
| -------------------------- | ---------------------------------------------------------------------- | ------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Environments               | The maximum number of Amazon MWAA environments per account per Region. | 10            | Yes        |
| Workers per environment    | The maximum number of workers per Amazon MWAA environment.             | 25            | Yes        |
| Webservers per environment | The maximum number of webservers per Amazon MWAA environment.          | 5             | Yes        | ## Increasing quotas You can request an increase to an adjustable quota by submitting a [quota increase request](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/ "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/"). |
