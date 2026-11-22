

# Data protection in AWS Abuse Signal API

You’re responsible for the information you choose to include in a report. Include only the information that AWS needs to process your report. AWS handles personal information as described in the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

## Encryption in transit
<a name="encryption-transit"></a>

TLS on port 443 protects all API traffic. The service requires TLS 1.2 or later, and we recommend TLS 1.3. This applies equally whether you use a Regional endpoint or an AWS PrivateLink endpoint. Do not disable certificate verification.

## Handling sensitive data
<a name="data-protection-sensitive"></a>

Include only the evidence necessary to substantiate a report. Avoid embedding secrets, credentials, or personal data beyond what the report type requires; prefer referencing large or sensitive artifacts (by URL or hash). Never put confidential data into free-form fields such as `description`.