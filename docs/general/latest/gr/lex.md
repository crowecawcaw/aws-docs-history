# Amazon Lex endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## V2 service endpoints

### Model building endpoints

| Region Name              | Region         | Endpoint                                   | Protocol |
| ------------------------ | -------------- | ------------------------------------------ | -------- |
| US East (N. Virginia)    | us-east-1      | models-v2-lex.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | models-v2-lex.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)       | af-south-1     | models-v2-lex.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Seoul)     | ap-northeast-2 | models-v2-lex.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | models-v2-lex.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | models-v2-lex.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | models-v2-lex.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)         | ca-central-1   | models-v2-lex.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | models-v2-lex.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | models-v2-lex.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)          | eu-west-2      | models-v2-lex.eu-west-2.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | models-v2-lex.us-gov-west-1.amazonaws.com  | HTTPS    |

### Runtime endpoints

| Region Name              | Region         | Endpoint                                    | Protocol |
| ------------------------ | -------------- | ------------------------------------------- | -------- |
| US East (N. Virginia)    | us-east-1      | runtime-v2-lex.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | runtime-v2-lex.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)       | af-south-1     | runtime-v2-lex.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Seoul)     | ap-northeast-2 | runtime-v2-lex.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | runtime-v2-lex.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | runtime-v2-lex.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | runtime-v2-lex.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)         | ca-central-1   | runtime-v2-lex.ca-central-1.amazonaws.com   | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | runtime-v2-lex.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | runtime-v2-lex.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)          | eu-west-2      | runtime-v2-lex.eu-west-2.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | runtime-v2-lex.us-gov-west-1.amazonaws.com  | HTTPS    |

## V1 service endpoints

### Model building endpoints

| Region Name           | Region    | Endpoint                                                                      | Protocol       |
| --------------------- | --------- | ----------------------------------------------------------------------------- | -------------- |
| US East (N. Virginia) | us-east-1 | models.lex.us-east-1.amazonaws.com<br>models-fips.lex.us-east-1.amazonaws.com | HTTPS<br>HTTPS |

### Runtime endpoints

| Region Name              | Region         | Endpoint                                                                                | Protocol       |
| ------------------------ | -------------- | --------------------------------------------------------------------------------------- | -------------- |
| US East (N. Virginia)    | us-east-1      | runtime.lex.us-east-1.amazonaws.com<br>runtime-fips.lex.us-east-1.amazonaws.com         | HTTPS<br>HTTPS |
| US West (Oregon)         | us-west-2      | runtime.lex.us-west-2.amazonaws.com<br>runtime-fips.lex.us-west-2.amazonaws.com         | HTTPS<br>HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 | runtime.lex.ap-southeast-1.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Sydney)    | ap-southeast-2 | runtime.lex.ap-southeast-2.amazonaws.com                                                | HTTPS          |
| Asia Pacific (Tokyo)     | ap-northeast-1 | runtime.lex.ap-northeast-1.amazonaws.com                                                | HTTPS          |
| Europe (Frankfurt)       | eu-central-1   | runtime.lex.eu-central-1.amazonaws.com                                                  | HTTPS          |
| Europe (Ireland)         | eu-west-1      | runtime.lex.eu-west-1.amazonaws.com                                                     | HTTPS          |
| Europe (London)          | eu-west-2      | runtime.lex.eu-west-2.amazonaws.com                                                     | HTTPS          |
| AWS GovCloud (US-West)   | us-gov-west-1  | runtime.lex.us-gov-west-1.amazonaws.com<br>runtime-fips.lex.us-gov-west-1.amazonaws.com | HTTPS<br>HTTPS |

## Service quotas

| Name                                                      | Default                        | Adjustable                                                                                                                                                                 | Description                                                                                                                                           |
| --------------------------------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bot channel associations per bot alias (V2)               | Each supported Region: 10      | No                                                                                                                                                                         | The maximum number of bot channel associations that you can create per bot alias in this account in the current Region.                               |
| Bots per account (V2)                                     | Each supported Region: 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-36FA8BD2 "https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-36FA8BD2") | The maximum number of bots that you can create in this account in the current Region.                                                                 |
| Characters per custom slot type value (V2)                | Each supported Region: 500     | No                                                                                                                                                                         | The maximum number of characters that you can have per custom slot type value in this account in the current Region.                                  |
| Characters per sample utterance (V2)                      | Each supported Region: 500     | No                                                                                                                                                                         | The maximum number of characters that you can have per intent or slot sample utterance in this account in the current Region.                         |
| Custom slot type values and synonyms per bot locale (V2)  | Each supported Region: 50,000  | No                                                                                                                                                                         | The maximum number of custom slot type values and synonyms that you can have per locale per bot in this account in the current Region.                |
| Custom slot types per bot locale (V2)                     | Each supported Region: 100     | No                                                                                                                                                                         | The maximum number of custom slot types that you can create per locale per bot in this account in the current Region.                                 |
| Sample utterances per intent (V2)                         | Each supported Region: 1,500   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-ED50DA7C "https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-ED50DA7C") | The maximum number of sample utterances that you can create per intent in this account in the current Region.                                         |
| Sample utterances per slot (V2)                           | Each supported Region: 10      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-77D6C60C "https://console.aws.amazon.com/servicequotas/home/services/lex/quotas/L-77D6C60C") | The maximum number of sample utterances that you can create per slot in this account in the current Region.                                           |
| Slots per bot locale (V2)                                 | Each supported Region: 2,000   | No                                                                                                                                                                         | The maximum number of slots that you can create per locale per bot in this account in the current Region.                                             |
| Slots per intent (V2)                                     | Each supported Region: 100     | No                                                                                                                                                                         | The maximum number of slots that you can create per intent in this account in the current Region.                                                     |
| Total characters in sample utterances per bot locale (V2) | Each supported Region: 200,000 | No                                                                                                                                                                         | The maximum number of characters that you can use per locale per bot for all intent and slot sample utterances in this account in the current Region. |
| Values and synonyms per custom slot type (V2)             | Each supported Region: 10,000  | No                                                                                                                                                                         | The maximum number of values and synonyms that you can have per custom slot type in this account in the current Region.                               |
| Versions per bot (V2)                                     | Each supported Region: 100     | No                                                                                                                                                                         | The maximum number of versions that you can create per bot in this account in the current Region.                                                     |
