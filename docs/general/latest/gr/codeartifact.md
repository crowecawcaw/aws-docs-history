# AWS CodeArtifact endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                  | Protocol |
| ------------------------ | -------------- | ----------------------------------------- | -------- |
| US East (Ohio)           | us-east-2      | codeartifact.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)    | us-east-1      | codeartifact.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | codeartifact.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Mumbai)    | ap-south-1     | codeartifact.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | codeartifact.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | codeartifact.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | codeartifact.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | codeartifact.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | codeartifact.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)          | eu-west-2      | codeartifact.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)           | eu-south-1     | codeartifact.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)           | eu-west-3      | codeartifact.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Stockholm)       | eu-north-1     | codeartifact.eu-north-1.amazonaws.com     | HTTPS    |

## Service quotas

| Name                                                    | Default                            | Adjustable                                                                                                                                                                                   | Description                                                                                         |
| ------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Asset file size                                         | Each supported Region: 5 Gigabytes | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-AA0DC56D "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-AA0DC56D") | The maximum file size per asset.                                                                    |
| Assets per package version                              | Each supported Region: 150         | No                                                                                                                                                                                           | The maximum number of assets per package version.                                                   |
| CopyPackageVersions requests per second                 | Each supported Region: 5           | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-308A4050 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-308A4050") | The maximum number of calls that can be made to CopyPackageVersions per second.                     |
| Direct upstreams per repository                         | Each supported Region: 10          | No                                                                                                                                                                                           | The maximum number of direct upstream repositories per repository.                                  |
| Domains per AWS account                                 | Each supported Region: 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-DD7208D3 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-DD7208D3") | The maximum number of domains that can be created per AWS account.                                  |
| GetAuthorizationToken requests per second               | Each supported Region: 40          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-0B362111 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-0B362111") | The maximum number of authorization tokens retrieved per second.                                    |
| GetPackageVersionAsset requests per second              | Each supported Region: 50          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-6C12FB34 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-6C12FB34") | The maximum number of calls that can be made to GetPackageVersionAsset per second.                  |
| ListPackageVersionAssets requests per second            | Each supported Region: 200         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-3072382D "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-3072382D") | The maximum number of calls that can be made to ListPackageVersionAssets per second.                |
| ListPackageVersions requests per second                 | Each supported Region: 200         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-CBBCDF5C "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-CBBCDF5C") | The maximum number of calls that can be made to ListPackageVersions per second.                     |
| ListPackages requests per second                        | Each supported Region: 200         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-6010CAF9 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-6010CAF9") | The maximum number of calls that can be made to ListPackages per second.                            |
| PublishPackageVersion requests per second               | Each supported Region: 10          | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-3E27C79F "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-3E27C79F") | The maximum number of calls that can be made to PublishPackageVersion per second.                   |
| Read requests per second from a single AWS account      | Each supported Region: 800         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-F39CF68A "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-F39CF68A") | The maximum number of read requests from one AWS account per second.                                |
| Repositories per domain                                 | Each supported Region: 1,000       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-86608C96 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-86608C96") | The maximum number of repositories that can be created per domain.                                  |
| Requests per second using a single authentication token | Each supported Region: 1,200       | No                                                                                                                                                                                           | The maximum number of requests per second using a single authentication token.                      |
| Requests without authentication token per IP address    | Each supported Region: 600         | No                                                                                                                                                                                           | The maximum number of requests per second without an authentication token from a single IP address. |
| Upstream repositories searched                          | Each supported Region: 25          | No                                                                                                                                                                                           | The maximum number of upstream repositories searched when resolving a package.                      |
| Write requests per second from a single AWS account     | Each supported Region: 100         | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-A649E766 "https://console.aws.amazon.com/servicequotas/home/services/codeartifact/quotas/L-A649E766") | The maximum number of write requests from one AWS account per second.                               |
