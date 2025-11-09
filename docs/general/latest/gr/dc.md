# AWS Direct Connect endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                    | Protocol       |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------- | -------------- |
| US East (Ohio)             | us-east-2      | directconnect.us-east-2.amazonaws.com<br>directconnect-fips.us-east-2.amazonaws.com         | HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | directconnect.us-east-1.amazonaws.com<br>directconnect-fips.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | directconnect.us-west-1.amazonaws.com<br>directconnect-fips.us-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | directconnect.us-west-2.amazonaws.com<br>directconnect-fips.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | directconnect.af-south-1.amazonaws.com                                                      | HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | directconnect.ap-east-1.amazonaws.com                                                       | HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | directconnect.ap-south-2.amazonaws.com                                                      | HTTPS          |
| Asia Pacific (Jakarta)     | ap-southeast-3 | directconnect.ap-southeast-3.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Malaysia)    | ap-southeast-5 | directconnect.ap-southeast-5.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Melbourne)   | ap-southeast-4 | directconnect.ap-southeast-4.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Mumbai)      | ap-south-1     | directconnect.ap-south-1.amazonaws.com                                                      | HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | directconnect.ap-southeast-6.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Osaka)       | ap-northeast-3 | directconnect.ap-northeast-3.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Seoul)       | ap-northeast-2 | directconnect.ap-northeast-2.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | directconnect.ap-southeast-1.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | directconnect.ap-southeast-2.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | directconnect.ap-east-2.amazonaws.com                                                       | HTTPS          |
| Asia Pacific (Thailand)    | ap-southeast-7 | directconnect.ap-southeast-7.amazonaws.com                                                  | HTTPS          |
| Asia Pacific (Tokyo)       | ap-northeast-1 | directconnect.ap-northeast-1.amazonaws.com                                                  | HTTPS          |
| Canada (Central)           | ca-central-1   | directconnect.ca-central-1.amazonaws.com<br>directconnect-fips.ca-central-1.amazonaws.com   | HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | directconnect.ca-west-1.amazonaws.com<br>directconnect-fips.ca-west-1.amazonaws.com         | HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | directconnect.eu-central-1.amazonaws.com                                                    | HTTPS          |
| Europe (Ireland)           | eu-west-1      | directconnect.eu-west-1.amazonaws.com                                                       | HTTPS          |
| Europe (London)            | eu-west-2      | directconnect.eu-west-2.amazonaws.com                                                       | HTTPS          |
| Europe (Milan)             | eu-south-1     | directconnect.eu-south-1.amazonaws.com                                                      | HTTPS          |
| Europe (Paris)             | eu-west-3      | directconnect.eu-west-3.amazonaws.com                                                       | HTTPS          |
| Europe (Spain)             | eu-south-2     | directconnect.eu-south-2.amazonaws.com                                                      | HTTPS          |
| Europe (Stockholm)         | eu-north-1     | directconnect.eu-north-1.amazonaws.com                                                      | HTTPS          |
| Europe (Zurich)            | eu-central-2   | directconnect.eu-central-2.amazonaws.com                                                    | HTTPS          |
| Israel (Tel Aviv)          | il-central-1   | directconnect.il-central-1.amazonaws.com                                                    | HTTPS          |
| Mexico (Central)           | mx-central-1   | directconnect.mx-central-1.amazonaws.com                                                    | HTTPS          |
| Middle East (Bahrain)      | me-south-1     | directconnect.me-south-1.amazonaws.com                                                      | HTTPS          |
| Middle East (UAE)          | me-central-1   | directconnect.me-central-1.amazonaws.com                                                    | HTTPS          |
| South America (São Paulo)  | sa-east-1      | directconnect.sa-east-1.amazonaws.com                                                       | HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | directconnect.us-gov-east-1.amazonaws.com<br>directconnect-fips.us-gov-east-1.amazonaws.com | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | directconnect.us-gov-west-1.amazonaws.com<br>directconnect-fips.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                                  | Default                      | Adjustable | Description                                                                                                          |
| --------------------------------------------------------------------- | ---------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| Dedicated connections per location                                    | Each supported Region: 10    | No         | The maximum number of active AWS Direct Connect dedicated connections per location.                                  |
| Direct Connect gateways per account                                   | Each supported Region: 200   | No         | The maximum number of AWS Direct Connect gateways per account.                                                       |
| Direct Connect gateways per transit gateway                           | Each supported Region: 20    | No         | The maximum number of Direct Connect gateways associated to a transit gateway.                                       |
| LAGs per Region                                                       | Each supported Region: 10    | No         | The maximum number of link aggregation groups (LAGs) per AWS Region.                                                 |
| Members per LAG                                                       | Each supported Region: 4     | No         | The maximum number of dedicated connections or interconnects per link aggregation group (LAG).                       |
| Prefixes per transit gateway                                          | Each supported Region: 200   | No         | The maximum number of prefixes per AWS Transit Gateway from AWS to on-premises on a transit virtual interface.       |
| Private or public or transit virtual interfaces per hosted connection | Each supported Region: 1     | No         | The maximum number of private, public, or transit virtual interfaces per AWS Direct Connect hosted connection.       |
| Public or private virtual interfaces per dedicated connection         | Each supported Region: 50    | No         | The maximum number of private, or public interfaces per AWS Direct Connect dedicated connection.                     |
| Routes per BGP session on private or transit virtual interfaces       | Each supported Region: 100   | No         | The maximum Routes per Border Gateway Protocol (BGP) on a private virtual interface or a transit virtual interface.  |
| Routes per BGP session on public virtual interfaces                   | Each supported Region: 1,000 | No         | The maximum routes per Border Gateway Protocol (BGP) on a public virtual interface                                   |
| Total number of virtual interfaces per dedicated connection           | Each supported Region: 54    | No         | The maximum number of private, or public and transit virtual interfaces per AWS Direct Connect dedicated connection. |
| Transit gateways per AWS Direct Connect gateway                       | Each supported Region: 6     | No         | The maximum number of transit gateways per AWS Direct Connect gateway.                                               |
| Transit virtual interfaces per dedicated connection                   | Each supported Region: 4     | No         | The maximum number of transit virtual interfaces per AWS Direct Connect dedicated connection.                        |
| Virtual interfaces per Direct Connect gateway                         | Each supported Region: 30    | No         | The maximum number of virtual interfaces per AWS Direct Connect gateway.                                             |
| Virtual interfaces per LAG                                            | Each supported Region: 54    | No         | The maximum number of virtual interfaces for each Link Aggregation Group (LAG)                                       |
| Virtual private gateways per Direct Connect gateway                   | Each supported Region: 20    | No         | The maximum number of virtual private gateways per AWS Direct Connect gateway.                                       |

For more information, see [AWS Direct Connect
Quotas](../../../directconnect/latest/UserGuide/limits.md "../../../directconnect/latest/UserGuide/limits.md") in the _AWS Direct Connect User Guide_.
