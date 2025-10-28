# AWS IoT Device Defender in AWS GovCloud (US)

AWS IoT Device Defender is a fully managed service that helps you secure your fleet of IoT devices. You can use AWS IoT Device Defender to audit your IoT resources like policies, certificates, IAM roles and Amazon Cognito IDs against security best practices, monitor connected devices to detect abnormal behavior, and mitigate security risks. By using AWS IoT Device Defender, you can enforce consistent security policies across your AWS IoT device fleet and respond quickly when devices are compromised.

## How AWS IoT Device Defender differs for AWS GovCloud (US)

- Amazon Cognito related checks in Device Defender Audit are not available.
- Role alias related and key quality related checks in Device Defender Audit are not available.
- AWS IoT Device Defender ML Detect feature is not available in the
  AWS GovCloud (US) Regions.

## Documentation for AWS IoT Device Defender

[AWS IoT Device Defender documentation](../../../iot/latest/developerguide/device-defender.md "../../../iot/latest/developerguide/device-defender.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Security Profile Name
- Behavior Name
- Audit Schedule Name
- Mitigation Action Name
- Audit Mitigation Action Task Id
