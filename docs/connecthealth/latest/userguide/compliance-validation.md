# Compliance validation for Amazon Connect Health

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS Services in Scope by Compliance Program](http://aws.amazon.com/compliance/services-in-scope/ "http://aws.amazon.com/compliance/services-in-scope/") and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](http://aws.amazon.com/compliance/programs/ "http://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company’s compliance objectives, and applicable laws and regulations.

## HIPAA eligibility

Amazon Connect Health is a HIPAA-eligible AWS service. Customers subject to the Health Insurance Portability and Accountability Act of 1996 (HIPAA) must execute a Business Associate Addendum (BAA) with AWS prior to processing protected health information (PHI).

The zero-persistence architecture of Amazon Connect Health minimizes PHI exposure. However, customers remain responsible for ensuring their configuration meets HIPAA requirements.

## Customer responsibilities for compliance

When using Amazon Connect Health, you are responsible for the following:

### Data classification

- Identify which data constitutes PHI in your environment.
- Implement appropriate controls based on data sensitivity.
- Document data flows and storage locations.

### Access controls

- Implement least-privilege access for all users, including workforce users provisioned through AWS IAM Identity Center.
- Enforce multi-factor authentication (MFA) for administrative access.
- Conduct regular access reviews and remove unused accounts.

### Incident response

- Establish procedures for detecting and reporting security incidents.
- Amazon Connect Health provides audit logs through AWS CloudTrail to support incident investigations.
- Customers are responsible for notifying affected individuals per HIPAA breach notification rules.

### Risk assessment

- Conduct regular HIPAA Security Rule risk assessments.
- Document risks and mitigation strategies.
- Update security policies based on assessment findings.
