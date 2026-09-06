

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Compliance validation for Amazon Pinpoint
<a name="security-compliance-validation"></a>

Third-party auditors assess the security and compliance of Amazon Pinpoint as part of multiple AWS compliance programs. These include AWS System and Organization Controls (SOC), FedRAMP, HIPAA, ISO/IEC 27001:2013 for security management controls, ISO/IEC 27017:2015 for cloud-specific controls, ISO/IEC 27018:2014 for personal data protection, ISO/IEC 9001:2015 for quality management systems, and others.

For a list of AWS services that are in scope for specific compliance programs, see [AWS services in scope by compliance program](https://aws.amazon.com/compliance/services-in-scope/). For general information, see [AWS compliance programs](https://aws.amazon.com/compliance/programs/).

You can download third-party audit reports by using AWS Artifact. For more information, see [Downloading reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html).

Your compliance responsibility when using Amazon Pinpoint is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. AWS provides the following resources to help with compliance:
+ [Quick Starts](https://aws.amazon.com/quickstart/?awsf.quickstart-homepage-filter=categories%23security-identity-compliance) – These deployment guides discuss architectural considerations and provide steps for deploying security- and compliance-focused baseline environments on AWS.
+ [Architecting for HIPAA security and compliance on Amazon Web Services whitepaper ](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/introduction.html) – This whitepaper describes how companies can use AWS to create HIPAA-compliant applications.
+ [AWS compliance resources](https://aws.amazon.com/compliance/resources/) – This collection of workbooks and guides might apply to your industry and location.
+ [Evaluating resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *AWS Config Developer Guide* – The AWS Config service assesses how well your resource configurations comply with internal practices, industry guidelines, and regulations.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – This AWS service provides a comprehensive view of your security state within AWS and helps you check your compliance with security standards and best practices.

Amazon Pinpoint is an AWS HIPAA-eligible service when you use the proper communication channels. If you want to use Amazon Pinpoint to run workloads containing Protected Health Information (PHI), as defined by HIPAA and associated legislation and regulations, you should use the email channel, push notification channel, or SMS channel to send messages that contain PHI. If you use the SMS channel to send messages that contain PHI, you should send those messages from a dedicated [short code](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-awssupport-short-code.html) that you requested for your AWS account for the explicit purpose of sending messages that will or may contain PHI. The voice channel is not AWS HIPAA-eligible. Don't use the voice channel to send messages that contain PHI.