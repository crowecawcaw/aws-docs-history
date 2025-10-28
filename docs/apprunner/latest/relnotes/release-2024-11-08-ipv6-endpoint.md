# App Runner introduces dual-stack endpoints for APIs on November 8, 2024

**Release date:** November 8, 2024

## Changes

AWS App Runner now offers dual-stack support for API endpoints, enabling both IPv4 and IPv6 traffic to enhance accessibility and compatibility across
network configurations. This update extends IPv6 support to AWS PrivateLink connections, offering developers developers more flexibility for applications
hosted within VPCs.

With this release App Runner has introduced new dual-stack public API endpoints in the format of `apprunner.`region`.api.aws`, along with FIPS
compliant endpoints in the format of `apprunner-fips.`region`.api.aws`. These endpoints accept both IPv4 and IPv6 traffic, allowing developers to make API
calls directly over IPv6 networks.

| **Region**     | **Dual-stack endpoint**                                      |
| -------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| us-east-1      | apprunner.us-east-1.api.aws apprunner-fips.us-east-1.api.aws |
| us-east-2      | apprunner.us-east-2.api.aws apprunner-fips.us-east-2.api.aws |
| us-west-2      | apprunner.us-west-2.api.aws apprunner-fips.us-west-2.api.aws |
| ap-south-1     | apprunner.ap-south-1.api.aws                                 |
| ap-southeast-1 | apprunner.ap-southeast-1.api.aws                             |
| ap-southeast-2 | apprunner.ap-southeast-2.api.aws                             |
| ap-northeast-1 | apprunner.ap-northeast-1.api.aws                             |
| eu-central-1   | apprunner.eu-central-1.api.aws                               |
| eu-west-1      | apprunner.eu-west-1.api.aws                                  |
| eu-west-2      | apprunner.eu-west-2.api.aws                                  |
| eu-west-3      | apprunner.eu-west-3.api.aws                                  | In addition to public endpoint support, App Runner now extends IPv6 compatibility to AWS PrivateLink endpoints, enabling developers to make IPv6 based API calls from their VPCs. ###### Note The previous set of endpoints (apprunner.`region`.amazonaws.com) will remain active and continue to receive traffic; however, they support only IPv4. |
