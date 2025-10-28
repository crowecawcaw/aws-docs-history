# Security management

AWS Managed Services (AMS) security management is the process by which AMS identifies an organization's assets and implements policies and
procedures to protect those assets.

###### Note

AMS now has a change type (CT), Deployment | Advanced stack components | ACM certificate with additional SANs | Create (ct-3l14e139i5p50),
that you can use to submit a request for an AWS Certificate Manager certificate. For information, see
[AWS::CertificateManager::Certificate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.md").
This CT provides for the creation of additional subject alternative name (SAN).

To better understand general AWS security, see
[Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/").

AMS categorizes security risks as follows:

- Known risks detected by anti-malware, which the malware mitigation process handles.
- Security events including access breaches, which the security event management process handles.

###### Topics

- [Data protection in AMS](sec-data-protect.md "sec-data-protect.md")
- [Identity and access management](sec-iam.md "sec-iam.md")
- [Security Incident Response in AMS](security-incident-response.md "security-incident-response.md")
- [Change request security reviews in AMS Advanced](ams-sec-change-request-review.md "ams-sec-change-request-review.md")
