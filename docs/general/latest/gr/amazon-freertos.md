# FreeRTOS endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

The following tables provide a list of Region-specific endpoints that FreeRTOS supports for Over-the-Air functionality.
The FreeRTOS console is also supported in these Regions.

### FreeRTOS OTA Control Plane

| Region Name               | Region         | Endpoint                                                              | Protocol       |
| ------------------------- | -------------- | --------------------------------------------------------------------- | -------------- |
| US East (Ohio)            | us-east-2      | iot.us-east-2.amazonaws.com<br>iot-fips.us-east-2.amazonaws.com       | https<br>https |
| US East (N. Virginia)     | us-east-1      | iot.us-east-1.amazonaws.com<br>iot-fips.us-east-1.amazonaws.com       | https<br>https |
| US West (N. California)   | us-west-1      | iot.us-west-1.amazonaws.com<br>iot-fips.us-west-1.amazonaws.com       | https<br>https |
| US West (Oregon)          | us-west-2      | iot.us-west-2.amazonaws.com<br>iot-fips.us-west-2.amazonaws.com       | https<br>https |
| Asia Pacific (Hong Kong)  | ap-east-1      | iot.ap-east-1.amazonaws.com                                           | HTTPS          |
| Asia Pacific (Mumbai)     | ap-south-1     | iot.ap-south-1.amazonaws.com                                          | HTTPS          |
| Asia Pacific (Seoul)      | ap-northeast-2 | iot.ap-northeast-2.amazonaws.com                                      | HTTPS          |
| Asia Pacific (Singapore)  | ap-southeast-1 | iot.ap-southeast-1.amazonaws.com                                      | HTTPS          |
| Asia Pacific (Sydney)     | ap-southeast-2 | iot.ap-southeast-2.amazonaws.com                                      | HTTPS          |
| Asia Pacific (Tokyo)      | ap-northeast-1 | iot.ap-northeast-1.amazonaws.com                                      | HTTPS          |
| Canada (Central)          | ca-central-1   | iot.ca-central-1.amazonaws.com<br>iot-fips.ca-central-1.amazonaws.com | https<br>https |
| Europe (Frankfurt)        | eu-central-1   | iot.eu-central-1.amazonaws.com                                        | HTTPS          |
| Europe (Ireland)          | eu-west-1      | iot.eu-west-1.amazonaws.com                                           | HTTPS          |
| Europe (London)           | eu-west-2      | iot.eu-west-2.amazonaws.com                                           | HTTPS          |
| Europe (Paris)            | eu-west-3      | iot.eu-west-3.amazonaws.com                                           | HTTPS          |
| Europe (Stockholm)        | eu-north-1     | iot.eu-north-1.amazonaws.com                                          | HTTPS          |
| Middle East (Bahrain)     | me-south-1     | iot.me-south-1.amazonaws.com                                          | HTTPS          |
| South America (São Paulo) | sa-east-1      | iot.sa-east-1.amazonaws.com                                           | HTTPS          |

### FreeRTOS OTA Data Plane

| Region Name               | Region         | Endpoint                                  | Protocol |
| ------------------------- | -------------- | ----------------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | _prefix_.iot.us-east-2.amazonaws.com      | MQTT     |
| US East (N. Virginia)     | us-east-1      | _prefix_.iot.us-east-1.amazonaws.com      | MQTT     |
| US West (N. California)   | us-west-1      | _prefix_.iot.us-west-1.amazonaws.com      | MQTT     |
| US West (Oregon)          | us-west-2      | _prefix_.iot.us-west-2.amazonaws.com      | MQTT     |
| Asia Pacific (Hong Kong)  | ap-east-1      | _prefix_.iot.ap-east-1.amazonaws.com      | MQTT     |
| Asia Pacific (Mumbai)     | ap-south-1     | _prefix_.iot.ap-south-1.amazonaws.com     | MQTT     |
| Asia Pacific (Seoul)      | ap-northeast-2 | _prefix_.iot.ap-northeast-2.amazonaws.com | MQTT     |
| Asia Pacific (Singapore)  | ap-southeast-1 | _prefix_.iot.ap-southeast-1.amazonaws.com | MQTT     |
| Asia Pacific (Sydney)     | ap-southeast-2 | _prefix_.iot.ap-southeast-2.amazonaws.com | MQTT     |
| Asia Pacific (Tokyo)      | ap-northeast-1 | _prefix_.iot.ap-northeast-1.amazonaws.com | MQTT     |
| Canada (Central)          | ca-central-1   | _prefix_.iot.ca-central-1.amazonaws.com   | MQTT     |
| Europe (Frankfurt)        | eu-central-1   | _prefix_.iot.eu-central-1.amazonaws.com   | MQTT     |
| Europe (Ireland)          | eu-west-1      | _prefix_.iot.eu-west-1.amazonaws.com      | MQTT     |
| Europe (London)           | eu-west-2      | _prefix_.iot.eu-west-2.amazonaws.com      | MQTT     |
| Europe (Paris)            | eu-west-3      | _prefix_.iot.eu-west-3.amazonaws.com      | MQTT     |
| Europe (Stockholm)        | eu-north-1     | _prefix_.iot.eu-north-1.amazonaws.com     | MQTT     |
| Middle East (Bahrain)     | me-south-1     | _prefix_.iot.me-south-1.amazonaws.com     | MQTT     |
| South America (São Paulo) | sa-east-1      | _prefix_.iot.sa-east-1.amazonaws.com      | MQTT     |

## Service quotas

| FreeRTOS OTA Resource Quotas | Resource | Default |
| ---------------------------- | -------- | ------- |
| File size                    | 16MB     |

| FreeRTOS OTA Throttling | API    | Transactions Per Second |
| ----------------------- | ------ | ----------------------- |
| CreateOTAUpdate         | 10 TPS |
| DeleteOTAUpdate         | 5 TPS  |
| GetOTAUpdate            | 15 TPS |
| ListOTAUpdates          | 15 TPS |
