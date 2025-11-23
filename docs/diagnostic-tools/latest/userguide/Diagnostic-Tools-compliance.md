# Compliance validation for AWS Diagnostic Tools

To learn whether an AWS service is within the scope of specific compliance programs, see
[AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/") and choose the compliance program that you are
interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more
information, see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS services is determined by the sensitivity
of your data, your company's compliance objectives, and applicable laws and
regulations. For more information about your compliance responsibility when using AWS services, see
[AWS Security Documentation](../../../security.md "../../../security.md").

## Compliance validation

To learn whether an AWS service is within the scope of specific compliance programs, see AWS services in [Scope by Compliance Program](../../../http:/aws.amazon.com/compliance/services-in-scope.md "../../../http:/aws.amazon.com/compliance/services-in-scope.md") and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](../../../http:/aws.amazon.com/compliance/programs.md "../../../http:/aws.amazon.com/compliance/programs.md").

You can download third-party audit reports using AWS Artifact. For more information, see Downloading Reports in AWS Artifact [https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:
[Security and Compliance Quick Start Guides](../../../http:/aws.amazon.com/quickstart.md "../../../http:/aws.amazon.com/quickstart.md") – These deployment guides discuss architectural considerations and provide steps for deploying baseline environments on AWS that are security and compliance focused.
[Architecting for HIPAA Security and Compliance on Amazon Web Services](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/welcome.md") – This whitepaper describes how companies can use AWS to create HIPAA-eligible applications.

When using Diagnostic Tools to diagnose AWS services in your account, you can select the Region to store the tool output. To meet data sovereignty requirements for a jurisdiction, specify where to store the output. The output saved in the destination Region will not replicate to other Regions. This facilitates data sovereignty for regulations like General Data Protection Regulation (GDPR) and regional requirements.

###### Note

Not all AWS services are HIPAA eligible. For more information, see the [HIPAA Eligible Services Reference](https://aws.amazon.com/compliance/hipaa-eligible-services-reference/ "https://aws.amazon.com/compliance/hipaa-eligible-services-reference/").

[AWS Compliance Resources](../../../http:/aws.amazon.com/compliance/resources.md "../../../http:/aws.amazon.com/compliance/resources.md") – This collection of workbooks and guides might apply to your industry and location.

[Evaluating Resources with Rules in the AWS Config Developer Guide](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md") – The AWS Config service assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.

[AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") – This AWS service provides a comprehensive view of your security state within AWS. Security Hub uses security controls to evaluate your AWS resources and to check your compliance against security industry standards and best practices. For a list of supported services and controls, see Security Hub controls reference.

[AWS Audit Manager](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md") – This AWS service helps you continuously audit your AWS usage to simplify how you manage risk and compliance with regulations and industry standards.
