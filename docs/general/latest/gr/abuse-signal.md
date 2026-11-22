

# AWS Abuse Signal API endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="abuse-signal_region"></a>


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | us-east-1 | abuse.us-east-1.amazonaws.com<br />abuse.us-east-1.api.aws | HTTPS | 
| US West (Oregon) | us-west-2 | abuse.us-west-2.amazonaws.com<br />abuse.us-west-2.api.aws | HTTPS | 
| Europe (London) | eu-west-2 | abuse.eu-west-2.amazonaws.com<br />abuse.eu-west-2.api.aws | HTTPS | 
| Global | aws-global | abuse.global.api.aws | HTTPS | 

## Service quotas
<a name="abuse-signal_quotas"></a>


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| CreateAbuseReport request rate | 10 transactions per second (burst 100) | Yes | Maximum sustained CreateAbuseReport requests per second per account. Exceeding it returns ThrottlingException (HTTP 429). | 
| GetAbuseReportStatus request rate | 50 transactions per second (burst 100) | Yes | Maximum sustained GetAbuseReportStatus requests per second per account. | 
| ListAbuseReportStatuses request rate | 10 transactions per second (burst 50) | Yes | Maximum sustained ListAbuseReportStatuses requests per second per account. | 
| Maximum decoded size per evidence item | 5 MB | No | Maximum decoded size of a single embedded evidence item in a CreateAbuseReport request. | 
| Maximum evidence items per report | 50 | No | Maximum number of embedded evidence items in a single report. | 
| Maximum total request payload size | 5 MB | No | Maximum total payload size of a single CreateAbuseReport request, including embedded evidence. | 