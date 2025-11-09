# Region availability for AWS Directory Service

The following table provides a list describing which Region-specific endpoints are supported
by directory type.

| Region name               | Region         | Endpoint                           | Protocol | AWS Managed Microsoft AD (Standard and Enterprise Editions) | AWS Managed Microsoft AD (Hybrid Edition) | AD Connector | Simple AD |
| ------------------------- | -------------- | ---------------------------------- | -------- | ----------------------------------------------------------- | ----------------------------------------- | ------------ | --------- |
| US East (N. Virginia)     | us-east-1      | ds.us-east-1.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| US East (Ohio)            | us-east-2      | ds.us-east-2.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| US West (N. California)   | us-west-1      | ds.us-west-1.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| US West (Oregon)          | us-west-2      | ds.us-west-2.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| Africa (Cape Town)        | af-south-1     | ds.af-south-1.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Hong Kong)  | ap-east-1      | ds.ap-east-1.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Taipei)     | ap-east-2      | ds.ap-east-2.amazonaws.com         | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Asia Pacific (Hyderabad)  | ap-south-2     | ds.ap-south-2.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Jakarta)    | ap-southeast-3 | ds.ap-southeast-3.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Malaysia)   | ap-southeast-5 | ds.ap-southeast-5.amazonaws.com    | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Asia Pacific (Melbourne)  | ap-southeast-4 | ds.ap-southeast-4.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Thailand)   | ap-southeast-7 | ds.ap-southeast-7.amazonaws.com    | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Asia Pacific (Mumbai)     | ap-south-1     | ds.ap-south-1.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Osaka)      | ap-northeast-3 | ds.ap-northeast-3.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Seoul)      | ap-northeast-2 | ds.ap-northeast-2.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Asia Pacific (Singapore)  | ap-southeast-1 | ds.ap-southeast-1.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| Asia Pacific (Sydney)     | ap-southeast-2 | ds.ap-southeast-2.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| Asia Pacific (Tokyo)      | ap-northeast-1 | ds.ap-northeast-1.amazonaws.com    | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| Canada (Central)          | ca-central-1   | ds.ca-central-1.amazonaws.com      | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Canada West (Calgary)     | ca-west-1      | ds.ca-west-1.amazonaws.com         | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| China (Beijing)           | cn-north-1     | ds.cn-north-1.amazonaws.com.cn     | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| China (Ningxia)           | cn-northwest-1 | ds.cn-northwest-1.amazonaws.com.cn | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Europe (Frankfurt)        | eu-central-1   | ds.eu-central-1.amazonaws.com      | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Ireland)          | eu-west-1      | ds.eu-west-1.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | Yes       |
| Europe (London)           | eu-west-2      | ds.eu-west-2.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Milan)            | eu-south-1     | ds.eu-south-1.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Paris)            | eu-west-3      | ds.eu-west-3.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Spain)            | eu-south-2     | ds.eu-south-2.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Stockholm)        | eu-north-1     | ds.eu-north-1.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Europe (Zurich)           | eu-central-2   | ds.eu-central-2.amazonaws.com      | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Israel (Tel Aviv)         | il-central-1   | ds.il-central-1.amazonaws.com      | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Mexico (Central)          | mx-central-1   | ds.mx-central-1.amazonaws.com      | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| Middle East (Bahrain)     | me-south-1     | ds.me-south-1.amazonaws.com        | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| Middle East (UAE)         | me-central-1   | ds.me-central-1.amazonaws.com      | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| South America (São Paulo) | sa-east-1      | ds.sa-east-1.amazonaws.com         | HTTPS    | Yes                                                         | Yes                                       | Yes          | No        |
| AWS GovCloud (US-West)    | us-gov-west-1  | ds.us-gov-west-1.amazonaws.com     | HTTPS    | Yes                                                         | No                                        | Yes          | No        |
| AWS GovCloud (US-East)    | us-gov-east-1  | ds.us-gov-east-1.amazonaws.com     | HTTPS    | Yes                                                         | No                                        | Yes          | No        |

For information about using AWS Directory Service in the AWS GovCloud (US-West) Region and
AWS GovCloud (US-East) Region, see [Service
endpoints](../../../govcloud-us/latest/UserGuide/using-govcloud-endpoints.md "../../../govcloud-us/latest/UserGuide/using-govcloud-endpoints.md") in the _AWS GovCloud (US) User Guide_.

For information about using AWS Directory Service in the Beijing and Ningxia Regions, see [Endpoints and ARNs for
Amazon Web Services in China](http://docs.amazonaws.cn/en_us/general/latest/gr/rande.html "http://docs.amazonaws.cn/en_us/general/latest/gr/rande.html") in _Getting started with AWS in
China_.

For information about the FIPS endpoints that Directory Service Data supports, see [Directory Service Data endpoints and
quotas](../../../general/latest/gr/ds-data_region.md "../../../general/latest/gr/ds-data_region.md") in the _AWS General Reference Reference Guide_.

## Supported AWS Regions for Directory Service Data

The following table provides a list of the Region-specific endpoints that Directory Service Data supports
by directory type.

| Region name               | Region         | Endpoint                             | Protocol | AWS Managed Microsoft AD | AD Connector | Simple AD |
| ------------------------- | -------------- | ------------------------------------ | -------- | ------------------------ | ------------ | --------- |
| US East (Ohio)            | us-east-2      | ds-data.us-east-2.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| US East (N. Virginia)     | us-east-1      | ds-data.us-east-1.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| US West (N. California)   | us-west-1      | ds-data.us-west-1.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| US West (Oregon)          | us-west-2      | ds-data.us-west-2.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Hong Kong)  | ap-east-1      | ds-data.ap-east-1.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Mumbai)     | ap-south-1     | ds-data.ap-south-1.amazonaws.com     | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Osaka)      | ap-northeast-3 | ds-data.ap-northeast-3.amazonaws.com | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Seoul)      | ap-northeast-2 | ds-data.ap-northeast-2.amazonaws.com | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Singapore)  | ap-southeast-1 | ds-data.ap-southeast-1.amazonaws.com | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Sydney)     | ap-southeast-2 | ds-data.ap-southeast-2.amazonaws.com | HTTPS    | Yes                      | No           | No        |
| Asia Pacific (Tokyo)      | ap-northeast-1 | ds-data.ap-northeast-1.amazonaws.com | HTTPS    | Yes                      | No           | No        |
| Canada (Central)          | ca-central-1   | ds-data.ca-central-1.amazonaws.com   | HTTPS    | Yes                      | No           | No        |
| Europe (Frankfurt)        | eu-central-1   | ds-data.eu-central-1.amazonaws.com   | HTTPS    | Yes                      | No           | No        |
| Europe (Ireland)          | eu-west-1      | ds-data.eu-west-1.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| Europe (London)           | eu-west-2      | ds-data.eu-west-2.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| Europe (Paris)            | eu-west-3      | ds-data.eu-west-3.amazonaws.com      | HTTPS    | Yes                      | No           | No        |
| Europe (Stockholm)        | eu-north-1     | ds-data.eu-north-1.amazonaws.com     | HTTPS    | Yes                      | No           | No        |
| South America (São Paulo) | sa-east-1      | ds-data.sa-east-1.amazonaws.com      | HTTPS    | Yes                      | No           | No        |

For information about the FIPS endpoints that Directory Service Data supports, see [Directory Service Data endpoints and
quotas](../../../general/latest/gr/ds_region.md "../../../general/latest/gr/ds_region.md") in the _AWS General Reference Reference Guide_.
