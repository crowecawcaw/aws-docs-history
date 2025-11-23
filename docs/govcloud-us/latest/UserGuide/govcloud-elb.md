# Elastic Load Balancing

ELB automatically distributes your incoming application traffic across multiple targets, such as EC2 instances. It monitors the health of registered targets and routes traffic only to the healthy targets.

ELB supports the following types of load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and Classic Load Balancers. All four types of load balancers are supported in AWS GovCloud (US) Regions.

###### Note

Some features of ELB (ELB) TLS do not support FIPS 140-3 requirements by default. When using the Classic or Network Load Balancer, you can pass TCP traffic and terminate TLS on your target (for example, web server), that is configured to support FIPS 140-3 requirements. Application Load Balancer (ALB) supports selecting FIPS algorithms.

## How Elastic Load Balancing differs for AWS GovCloud (US)

- When using the legacy bucket policy, specify the following AWS account IDs in the policy to grant ELB permission to write logs to your S3 bucket:

| Region                 | ELB account ID |
| ---------------------- | -------------- |
| AWS GovCloud (US-East) | 190560391635   |
| AWS GovCloud (US-West) | 048591011584   |

- Export data must be encrypted in transit outside of the export boundary. Because ELB uses global DNS servers, export traffic across ELB must be encrypted.
- Cognito authentication is not available.

## Documentation for Elastic Load Balancing

[ELB documentation](https://aws.amazon.com/documentation/elastic-load-balancing/ "https://aws.amazon.com/documentation/elastic-load-balancing/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- All customer parameters provided as input to ELB (via console, APIs, or other mechanism) are not permitted to contain export-controlled data. Examples include the names of load balancers and the names of load balancer policies.
- Do not enter export-controlled data in the following fields:
  - Resource tags

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
