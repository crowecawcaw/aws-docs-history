

# AWS Proton endpoints and quotas
<a name="proton"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="proton_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  proton.us-east-2.amazonaws.com  | HTTPS | 
| US East (N. Virginia) | us-east-1 |  proton.us-east-1.amazonaws.com  | HTTPS | 
| US West (Oregon) | us-west-2 |  proton.us-west-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  proton.ap-northeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  proton.ap-southeast-1.amazonaws.com  | HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  proton.ap-southeast-2.amazonaws.com  | HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  proton.ap-northeast-1.amazonaws.com  | HTTPS | 
| Canada (Central) | ca-central-1 |  proton.ca-central-1.amazonaws.com  | HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  proton.eu-central-1.amazonaws.com  | HTTPS | 
| Europe (Ireland) | eu-west-1 |  proton.eu-west-1.amazonaws.com  | HTTPS | 
| Europe (London) | eu-west-2 |  proton.eu-west-2.amazonaws.com  | HTTPS | 

## Service quotas
<a name="limits_proton"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Components per account | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-8FBB60E3)  | Maximum number of components per account | 
| Environment account connections per environment account | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-6CC8209C)  | Maximum number of environment account connections per environment account | 
| Environments per account | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-37A692EA)  | Maximum number of environments per account | 
| Service instances per service | Each supported Region: 20 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-E8182F7E)  | Maximum number of service instances per service | 
| Services per account | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-1C8983C3)  | Maximum number of services per account | 
| Template versions per template | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-A1B6A95A)  | Maximum number of template versions registered per template | 
| Templates per account | Each supported Region: 1,000 |  [Yes](https://console.aws.amazon.com/servicequotas/home/services/proton/quotas/L-405DC02B)  | Maximum number of registered templates per account, service and environment templates combined | 

For more information, see [AWS Proton quotas](https://docs.aws.amazon.com/proton/latest/adminguide/ag-limits.html) in the *AWS Proton Administrator Guide*.