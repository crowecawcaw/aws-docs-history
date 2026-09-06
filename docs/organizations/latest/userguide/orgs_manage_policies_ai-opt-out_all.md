

# Opt out from all supported AWS AI services
<a name="orgs_manage_policies_ai-opt-out_all"></a>

**In this topic:**
+ You can opt out with a one button selection in the AWS Organizations console.
+ You can opt out by attaching the provided example policy using the AWS CLI & AWS SDKs.
+ You can view a list of AWS services supported by the AI services opt-out policy.

## Opt out from all supported AI services
<a name="ai-opt-out-all-procedure"></a>

You can opt your organization out of having its content used for service improvement by creating and attaching an AI services opt-out policy. This policy applies to all current and future supported AWS AI services. Member accounts cannot update the policy.

------
#### [ AWS Management Console ]

**To opt out from all AI services**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy)** page, choose **Opt out from all services**. If the policy is disabled, choose **Enable AI services opt-out policies**, and then choose **Opt out from all services**.

1. On the **Opt out from all services** confirmation page, choose **Opt out from all services**.

------
#### [ AWS CLI & AWS SDKs ]

**To opt out from all AI services**

1. Copy "Example 1: Opt out of all AI services for all accounts in the organization" in [AI services opt-out examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html#ai-opt-out-policy-examples).

1. Follow the instruction in [Attaching and detaching AI services opt-out](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_attach.html).

------

**Note**  
Additional steps are required to opt out from Amazon Monitron. For more information, see [AWS Service Terms](https://aws.amazon.com/service-terms/#81._Industrial_AI_Services).

## List of services supported by the AI services opt-out policy
<a name="ai-opt-out-all-list"></a>

The following is a list of AWS services supported by the AI services opt-out policy:
+ [Amazon AI Operations](https://aws.amazon.com/what-is/aiops)
+ [Amazon Bio Discovery](https://aws.amazon.com/biodiscovery/)
+ [Amazon Chime SDK voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/dg/voice-analytics.html)
+ [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch)
+ [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru)
+ [Amazon CodeWhisperer](https://docs.aws.amazon.com/codewhisperer) (now part of [Amazon Q Developer](https://docs.aws.amazon.com/amazonq))
+ [Amazon Comprehend](https://docs.aws.amazon.com/comprehend)
+ [AWS Config](https://docs.aws.amazon.com/config)
+ [Amazon Connect Customer](https://docs.aws.amazon.com/connect)
+ [Amazon Connect Decisions](https://docs.aws.amazon.com/connect-decisions/)
+ [Amazon Connect Health Operational Support](https://docs.aws.amazon.com/connecthealth/latest/userguide/)
+ [Amazon Connect Health Model Training](https://docs.aws.amazon.com/connecthealth/latest/userguide/)
+ [AWS Database Migration Service](https://docs.aws.amazon.com/dms)
+ [Amazon DataZone](https://docs.aws.amazon.com/datazone) (and [Amazon SageMaker Data Agent](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sagemaker-data-agent.html))
+ [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html)
+ [AWS Entity Resolution](https://docs.aws.amazon.com/entityresolution)
+ [AWS FinOps Agent](https://docs.aws.amazon.com/finops-agent/latest/userguide/what-is.html)
+ [Amazon Fraud Detector](https://docs.aws.amazon.com/frauddetector)
+ [AWS Glue](https://docs.aws.amazon.com/glue)
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty)
+ [Amazon Lex](https://docs.aws.amazon.com/lex)
+ [Amazon Polly](https://docs.aws.amazon.com/polly)
+ [Amazon Q](https://docs.aws.amazon.com/amazonq)
+ [Amazon Quick](https://docs.aws.amazon.com/quicksight)
+ [Amazon Rekognition](https://docs.aws.amazon.com/rekognition)
+ [Scenario Discovery](https://docs.aws.amazon.com/iot-sitewise)
+ [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/)
+ [AWS Supply Chain](https://aws.amazon.com/products/connect/decisions/)
+ [Amazon Textract](https://docs.aws.amazon.com/textract)
+ [Amazon Transcribe](https://docs.aws.amazon.com/transcribe)
+ [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is.html)
+ [Amazon Translate](https://docs.aws.amazon.com/translate)
+ [Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces)
+ [AWS Security Hub](https://docs.aws.amazon.com/securityhub)