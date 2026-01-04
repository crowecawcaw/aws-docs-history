# TELCOSEC02-BP02 Implement features such as concealed or

spoofed subscriber identities for signaling over the interfaces with access network

The 3rd Generation Partnership Project (3GPP) recommends that telco organizations use the
Subscription Concealed Identifier (SUCI) instead of the Subscription Permanent Identifier (SUPI)
on the air interface between the user equipment (UE) and the access network. This best practice
is aimed at enhancing the privacy and security of subscriber identities, as the air interface is
considered the most exposed and vulnerable part of the network.

The SUPI, which includes sensitive subscriber information such as the International Mobile
Subscriber Identity (IMSI), is a unique and permanent identifier associated with each
subscriber. By using the SUCI, a privacy-preserving temporary identifier derived from the SUPI,
telco organizations can block the disclosure of the actual subscriber identity over the air
interface, mitigating the risk of subscriber tracking, profiling, and other privacy-related
attacks.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement a secure mechanism for generating and processing the Subscription Concealed
Identifier (SUCI) instead of the Subscription Permanent Identifier (SUPI) for signaling over
the air interface, maintaining adherence with 3GPP privacy protection schemes. Establish a
secure system for mapping and managing the SUPI-SUCI relationship, with robust encryption and
integrity protection for the air interface communications. Monitor the air interface signaling
for anomalies and develop incident response procedures to address security incidents related
to subscriber identity, prioritizing privacy protection. Verify comprehensive security
governance and adherence with industry standards and regulations for the air interface
security controls.

### Implementation steps

Implement SUCI generation and conversion:

- Configure the UE and the Access and Mobility Management Function (AMF) to generate
  and process the SUCI instead of the SUPI for signaling over the air interface.
- Verify that the SUCI is generated using the appropriate privacy protection scheme,
  as defined in 3GPP TS 33.501.

Incident response and subscriber identity protection:

- Develop and test incident response procedures to address security incidents or
  breaches related to the SUCI signaling over the air interface.
- Use AWS Lambda, AWS Step Functions, and Amazon SNS to automate the incident response workflows
  and facilitate rapid remediation.
- Verify that the incident response plan includes steps for investigating,
  mitigating, and reporting subscriber identity-related security incidents, while
  preserving the privacy of the affected subscribers.

Air interface security governance:

- Establish security governance policies and controls for the management of SUCI
  signaling over the air interface.
- Use AWS Config, AWS Security Hub CSPM, and AWS Trusted Advisor to continuously assess the security
  posture and verify adherence with industry standards and regulations, such as GDPR.

## Resources

**Key AWS services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/")
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/")
- [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/")
