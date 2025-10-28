# Security in AWS RTB Fabric

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data
centers and network architectures that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security
_of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the
  infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use
  securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to RTB Fabric, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.

###### Important

**Security Risk:** RTB Fabric supports creating links without TLS encryption or authentication. Disabling TLS encryption allows any actor with access to the data in transit to view, tamper with, or spoof the data in transit. Disabling authentication allows anyone with network access to the endpoint to submit RTB requests. Always enable TLS and authentication for production environments.

This documentation helps you understand how to apply the shared responsibility model when
using RTB Fabric. The following topics show you how to configure RTB Fabric to meet your
security and compliance objectives. You also learn how to use other AWS services that help you
to monitor and secure your RTB Fabric resources.

###### Topics

- [Identity and access management for AWS RTB Fabric](security-iam.md "security-iam.md")
- [Data protection in AWS RTB Fabric](data-protection.md "data-protection.md")
- [Incident response for AWS RTB Fabric](incident-response.md "incident-response.md")
- [Compliance validation for AWS RTB Fabric](compliance-validation.md "compliance-validation.md")
