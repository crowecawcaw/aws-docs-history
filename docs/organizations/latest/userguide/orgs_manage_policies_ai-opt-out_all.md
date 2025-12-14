# Opt out from all supported AWS AI services

###### In this topic:

- You can opt out with a one button selection in the AWS Organizations console.
- You can opt out by attaching the provided example policy using the AWS CLI & AWS SDKs.
- You can view a list of AWS services supported by the AI services opt-out policy.

## Opt out from all supported AI services

You can opt your organization out of having its content used for service
improvement by creating and attaching an AI services opt-out policy.
This policy applies to all current and future supported AWS AI services.
Member accounts cannot update the policy.

AWS Management Console

###### To opt out from all AI services

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose **Opt out from all services**.
3. On the **Opt out from all services** confirmation page, choose **Opt out from all services**.

AWS CLI & AWS SDKs

###### To opt out from all AI services

1. Copy "Example 1: Opt out of all AI services for all accounts in the organization" in [AI services opt-out examples](orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples "orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples").
2. Follow the instruction in [Attaching and detaching AI services opt-out](orgs_manage_policies_ai-opt-out_attach.md "orgs_manage_policies_ai-opt-out_attach.md").

###### Note

Additional steps are required to opt out from Amazon Monitron. For more information,
see [AWS Service Terms](https://aws.amazon.com/service-terms/#81._Industrial_AI_Services "https://aws.amazon.com/service-terms/#81._Industrial_AI_Services").

## List of services supported by the AI services opt-out policy

The following is a list of AWS services supported by the AI services opt-out policy:

- [Amazon AI Operations](https://aws.amazon.com/what-is/aiops "https://aws.amazon.com/what-is/aiops")
- [Amazon Chime SDK voice analytics](../../../chime-sdk/latest/dg/voice-analytics.md "../../../chime-sdk/latest/dg/voice-analytics.md")
- [Amazon CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md")
- [Amazon CodeGuru Profiler](../../../codeguru.md "../../../codeguru.md")
- [Amazon CodeWhisperer](../../../codewhisperer.md "../../../codewhisperer.md") (now part of [Amazon Q Developer](../../../amazonq.md "../../../amazonq.md"))
- [Amazon Comprehend](../../../comprehend.md "../../../comprehend.md")
- [Amazon Connect](../../../connect.md "../../../connect.md")
- [Amazon Connect Optimization](../../../connect.md "../../../connect.md")
- [Amazon Connect Contact Lens](../../../connect/latest/adminguide/contact-lens.md "../../../connect/latest/adminguide/contact-lens.md")
- [AWS Database Migration Service](../../../dms.md "../../../dms.md")
- [Amazon DataZone](../../../datazone.md "../../../datazone.md")
- [AWS Entity Resolution](../../../entityresolution.md "../../../entityresolution.md")
- [Amazon Fraud Detector](../../../frauddetector.md "../../../frauddetector.md")
- [AWS Glue](../../../glue.md "../../../glue.md")
- [Amazon GuardDuty](../../../guardduty.md "../../../guardduty.md")
- [Amazon Lex](../../../lex.md "../../../lex.md")
- [Amazon Polly](../../../polly.md "../../../polly.md")
- [Amazon Q](../../../amazonq.md "../../../amazonq.md")
- [Amazon Quick Suite](../../../quicksight.md "../../../quicksight.md")
- [Amazon Rekognition](../../../rekognition.md "../../../rekognition.md")
- [Amazon Security Lake](../../../security-lake.md "../../../security-lake.md")
- [AWS Supply Chain](../../../aws-supply-chain.md "../../../aws-supply-chain.md")
- [Amazon Textract](../../../textract.md "../../../textract.md")
- [Amazon Transcribe](../../../transcribe.md "../../../transcribe.md")
- [AWS Transform](../../../transform/latest/userguide/what-is.md "../../../transform/latest/userguide/what-is.md")
- [Amazon Translate](../../../translate.md "../../../translate.md")
- [AWS Security Hub CSPM](../../../securityhub.md "../../../securityhub.md")
