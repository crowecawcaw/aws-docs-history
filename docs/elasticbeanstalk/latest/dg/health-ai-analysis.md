# AI-powered environment analysis

AWS Elastic Beanstalk's AI-powered analysis identifies root causes and recommends solutions for environment health issues. When your environment experiences problems, you can request
an AI analysis using the `RequestEnvironmentInfo` and `RetrieveEnvironmentInfo` API operations with the `analyze` info type
to get AI-generated insights and recommended solutions.

###### Note

AI analysis is available only on supported Amazon Linux 2 and AL2023 platform versions released on or after February 16, 2026.

## How it works

When you request an AI analysis, Elastic Beanstalk runs a script on an instance in your environment that collects recent events, instance health,
and logs (up to 170,000 [tokens](../../../bedrock/latest/userguide/key-definitions.md "../../../bedrock/latest/userguide/key-definitions.md") of data). It then sends
this data to Amazon Bedrock in your account and returns insights and recommended next steps.

## Prerequisites

Before using AI analysis, ensure that your environment meets the following requirements:

- Environment running a [supported platform version](#health-ai-analysis-supported-platforms "#health-ai-analysis-supported-platforms")
- [Instance profile](iam-instanceprofile.md "iam-instanceprofile.md") with required permissions (see [Required permissions](#health-ai-analysis-permissions "#health-ai-analysis-permissions") below)
- **Anthropic use case details** – AI analysis uses Anthropic Claude models through Amazon Bedrock. Anthropic
  requires a one-time use case details form submission before you can invoke their models. Submit this form by selecting any Anthropic model from the
  model catalog in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/ "https://console.aws.amazon.com/bedrock/"), or by calling the
  [`PutUseCaseForModelAccess`](../../../bedrock/latest/APIReference/API_PutUseCaseForModelAccess.md "../../../bedrock/latest/APIReference/API_PutUseCaseForModelAccess.md")
  API. This only needs to be done once per AWS account. If submitted from the AWS Organizations management account, it automatically applies to all
  member accounts in the organization. For more information, see
  [Access Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md").
- **GovCloud regions** – If you are using AWS GovCloud (US) regions, you must enable access to the latest
  Anthropic Claude Sonnet and/or Opus model in Amazon Bedrock before using AI analysis. For instructions on enabling model access in GovCloud regions, see
  [Manage access to Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access.md#model-access-govcloud "../../../bedrock/latest/userguide/model-access.md#model-access-govcloud").
  For information about the latest available Anthropic Claude Sonnet and/or Opus model, see
  [Supported Regions and models for inference profiles](../../../bedrock/latest/userguide/inference-profiles-support.md "../../../bedrock/latest/userguide/inference-profiles-support.md").

## Required permissions

To use AI analysis, the Amazon EC2 instance profile for your environment must have permissions to invoke Amazon Bedrock. Add the following permissions to your
instance profile:

- `bedrock:InvokeModel`
- `bedrock:ListFoundationModels`
- `elasticbeanstalk:DescribeEvents`
- `elasticbeanstalk:DescribeEnvironmentHealth`

For more information about configuring instance profiles, see [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md "iam-instanceprofile.md").

## Using AI analysis in the console

###### From the environment overview

When your environment's health status is **Warning**, **Degraded**,
or **Severe**, an **AI Analysis** button appears in the environment overview section. Click on this button to
initiate an AI analysis of your environment.

###### From the Logs page

You can also access AI analysis from the **Logs** page in the navigation pane. Click on the **AI Analysis** button to
request an AI-powered analysis of your environment's current state.

## Using AI analysis with the AWS CLI

You can use the Elastic Beanstalk API through the AWS CLI to request and retrieve AI analysis programmatically.

###### Request AI analysis

Use the [`RequestEnvironmentInfo`](../api/API_RequestEnvironmentInfo.md "../api/API_RequestEnvironmentInfo.md") operation
with the `InfoType` parameter set to `analyze`.

###### Example AWS CLI - Request AI analysis

```
aws elasticbeanstalk request-environment-info \
    --environment-name `my-env` \
    --info-type analyze \
    --region `us-east-1`
```

###### Retrieve AI analysis

Use the [`RetrieveEnvironmentInfo`](../api/API_RetrieveEnvironmentInfo.md "../api/API_RetrieveEnvironmentInfo.md") operation
with the `InfoType` parameter set to `analyze` to retrieve the analysis results.

###### Example AWS CLI - Retrieve AI analysis

```
aws elasticbeanstalk retrieve-environment-info \
    --environment-name `my-env` \
    --info-type analyze \
    --region `us-east-1`
```

The response includes an AI-generated analysis of the current state of the environment. If any issues are identified, recommended solutions
are presented.

## Using AI analysis with the EB CLI

If you use the EB CLI, you can request AI analysis with the `--analyze` (`-ai`) option of the
**eb logs** command. The command requests the analysis, waits for it to complete, and displays the results.

###### Example EB CLI - Request AI analysis

```
$ `eb logs --analyze`
```

The `--analyze` option is not compatible with `--instance`, `--all`, `--zip`, or
`--log-group`. For the full command reference, see [eb logs](eb3-logs.md "eb3-logs.md").

###### Note

The `--analyze` option requires EB CLI version 3.27 or later.

## Important considerations

- **Pricing** – AI analysis uses Amazon Bedrock to process your environment data, and standard Amazon Bedrock
  pricing applies for model invocations. For pricing details, see [Amazon Bedrock
  Pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
- **Platform requirement** – AI analysis is available only on Amazon Linux 2 and AL2023 based platform versions
  released on or after February 16, 2026. To use this feature, update your environment to a supported platform version. For more information, see
  [Updating your Elastic Beanstalk environment's platform version](using-features.platform.upgrade.md "using-features.platform.upgrade.md").
- **Permissions** – Before using AI analysis, ensure that your instance profile has the required Amazon Bedrock
  permissions (`bedrock:InvokeModel` and `bedrock:ListFoundationModels`) and Elastic Beanstalk permissions
  (`elasticbeanstalk:DescribeEvents` and `elasticbeanstalk:DescribeEnvironmentHealth`).
- **Data privacy** – The analysis sends environment events and logs to Amazon Bedrock in your account for
  processing. For information about how Amazon Bedrock handles your data, see [Amazon Bedrock
  Security and Compliance](https://aws.amazon.com/bedrock/security-compliance/ "https://aws.amazon.com/bedrock/security-compliance/").
- **Service quotas** – AI analysis uses an Anthropic Claude model in Amazon Bedrock, which has default
  quotas for requests per minute and tokens per minute. If you encounter throttling errors, you can request a quota increase. For more information,
  see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

## Supported platform versions

AI analysis is supported on Amazon Linux 2 and AL2023 based platform versions released on or after
[February 16, 2026](RELEASE_NOTES_URL.md "RELEASE_NOTES_URL.md"). To verify your platform version, see
[Elastic Beanstalk release notes](../relnotes/welcome.md "../relnotes/welcome.md").
