# Compliance validation for AWS Wavelength

The existing compliance certifications for AWS services apply to services running entirely
in an AWS Region. The services running in a Wavelength Zone require a separate evaluation
for certifications.

Under the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"), AWS is responsible for the hardware and software that run AWS services.
This applies to AWS Wavelength, just as it does to an AWS Region. This includes patching the
infrastructure software and configuring infrastructure devices. As a customer, you are
responsible for implementing best practices for data encryption, patching the operating
system and applications, identity and access management, and operating system, network, and
firewall configurations.

AWS has responsibility for configuring and maintaining a network connection between the
Wavelength Zone and the AWS Region. Communication sent over this connection between the
Wavelength Zone and the Region is encrypted by AWS.

Third-party auditors assess the security and compliance of services in AWS Wavelength as part of
multiple AWS compliance programs.

AWS Wavelength currently supports these certifications and standards:

- HIPAA
- ISO (9001, 27001, 27017 and 27018)
- SOC (1, 2, 3)
- Payment Card Industry Data Security Standard (PCI DSS)
  For information about your compliance responsibility when using Amazon EC2, see [Compliance
  validation for Amazon EC2](../../../AWSEC2/latest/UserGuide/compliance-validation.md "../../../AWSEC2/latest/UserGuide/compliance-validation.md") in the _Amazon EC2 User Guide_.
  For more information about compliance, see [AWS Compliance](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/").
