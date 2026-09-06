

# AI-powered environment analysis
<a name="health-ai-analysis"></a>

AWS Elastic Beanstalk's AI-powered analysis identifies root causes and recommends solutions for environment health issues. When your environment experiences problems, you can request an AI analysis using the `RequestEnvironmentInfo` and `RetrieveEnvironmentInfo` API operations with the `analyze` info type to get AI-generated insights and recommended solutions.

**Note**  
AI analysis is available on supported Amazon Linux 2 and AL2023 platform versions released on or after February 26, 2026. For Windows Server platforms, AI analysis is available on platform versions released on or after April 22, 2026.

## How it works
<a name="health-ai-analysis-how-it-works"></a>

When you request an AI analysis, Elastic Beanstalk runs a script on an instance in your environment that collects recent events, instance health, and logs (up to 170,000 [tokens](https://docs.aws.amazon.com/bedrock/latest/userguide/key-definitions.html) of data). It then sends this data to Amazon Bedrock in your account and returns insights and recommended next steps.

## Prerequisites
<a name="health-ai-analysis-prereqs"></a>

Before you use AI analysis, verify that your environment meets the following requirements:
+ Environment running a [supported platform version](#health-ai-analysis-supported-platforms)
+ [Instance profile](iam-instanceprofile.md) with required permissions (see [Required permissions](#health-ai-analysis-permissions) below)
+ **Anthropic use case details (commercial regions)** – In commercial regions, AI analysis uses Anthropic Claude models through Amazon Bedrock. Anthropic requires you to submit a one-time use case details form before you can invoke their models. To submit this form, select any Anthropic model from the model catalog in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/), or call the [`PutUseCaseForModelAccess`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutUseCaseForModelAccess.html) API. You only need to do this once per AWS account. If you submit the form from the AWS Organizations management account, it automatically covers all member accounts in the organization. For more information, see [Access Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
  + Even after submitting the use case details form, the first invocation of an Anthropic Claude model in your account requires AWS Marketplace permissions to complete an automatic model subscription. If your instance profile doesn't have these permissions, AI analysis fails with the following error:

    `AccessDeniedException: Model access is denied due to IAM user or service role is not authorized to perform the required AWS Marketplace actions (aws-marketplace:ViewSubscriptions, aws-marketplace:Subscribe) to enable access to this model.`

    To resolve this, add `aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`, and `aws-marketplace:ViewSubscriptions` permissions to your instance profile. These permissions are only needed for the first invocation in an account. After the model is enabled, you can remove them. For more information, see [Grant IAM permissions to request access to Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-permissions).
+ **GovCloud regions** – If you are using AWS GovCloud (US) regions, AI analysis uses the NVIDIA Nemotron model instead of Anthropic Claude. You must request access to the NVIDIA Nemotron 3 Super 120B model in Amazon Bedrock before using AI analysis. To request access, open the [Amazon Bedrock Model access](https://console.amazonaws-us-gov.com/bedrock/home#/modelaccess) page in the GovCloud console and request access to NVIDIA Nemotron 3 Super 120B. The Anthropic use case details form and AWS Marketplace permissions are not required for GovCloud regions. For more information about enabling model access in GovCloud, see [Access Amazon Bedrock foundation models in AWS GovCloud (US)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-govcloud).

## Required permissions
<a name="health-ai-analysis-permissions"></a>

To use AI analysis, the Amazon EC2 instance profile for your environment must have permissions to invoke Amazon Bedrock. Add the following permissions to your instance profile:
+ `bedrock:InvokeModel`
+ `bedrock:ListFoundationModels`
+ `elasticbeanstalk:DescribeEvents`
+ `elasticbeanstalk:DescribeEnvironmentHealth`

For more information about configuring instance profiles, see [Managing Elastic Beanstalk instance profiles](iam-instanceprofile.md).

**Note**  
In commercial regions, if this is the first time an Anthropic Claude model is being invoked in your account, you also need AWS Marketplace permissions (`aws-marketplace:Subscribe`, `aws-marketplace:Unsubscribe`, and `aws-marketplace:ViewSubscriptions`). These permissions are not required in GovCloud regions. See [Prerequisites](#health-ai-analysis-prereqs) for details.

## Using AI analysis in the console
<a name="health-ai-analysis-console"></a>

**From the environment overview**  
When your environment's health status is **Warning**, **Degraded**, or **Severe**, an **AI Analysis** button appears in the environment overview section. Click on this button to initiate an AI analysis of your environment.

**From the Logs page**  
You can also access AI analysis from the **Logs** page in the navigation pane. Click on the **AI Analysis** button to request an AI-powered analysis of your environment's current state.

## Using AI analysis with the AWS CLI
<a name="health-ai-analysis-api"></a>

You can use the Elastic Beanstalk API through the AWS CLI to request and retrieve AI analysis programmatically.

**Request AI analysis**  
Use the [`RequestEnvironmentInfo`](http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html) operation with the `InfoType` parameter set to `analyze`.

**Example AWS CLI - Request AI analysis**  

```
aws elasticbeanstalk request-environment-info \
    --environment-name {{my-env}} \
    --info-type analyze \
    --region {{us-east-1}}
```

**Retrieve AI analysis**  
Use the [`RetrieveEnvironmentInfo`](http://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html) operation with the `InfoType` parameter set to `analyze` to retrieve the analysis results.

**Example AWS CLI - Retrieve AI analysis**  

```
aws elasticbeanstalk retrieve-environment-info \
    --environment-name {{my-env}} \
    --info-type analyze \
    --region {{us-east-1}}
```

The response includes an AI-generated analysis of the current state of the environment, along with recommended solutions for any identified issues.

## Using AI analysis with the EB CLI
<a name="health-ai-analysis-ebcli"></a>

If you use the EB CLI, you can request AI analysis with the `--analyze` (`-ai`) option of the **eb logs** command. The command requests the analysis, waits for it to complete, and displays the results.

**Example EB CLI - Request AI analysis**  

```
$ eb logs --analyze
```

The `--analyze` option is not compatible with `--instance`, `--all`, `--zip`, or `--log-group`. For the full command reference, see [**eb logs**](eb3-logs.md).

**Note**  
The `--analyze` option requires EB CLI version 3.27 or later.

## Important considerations
<a name="health-ai-analysis-considerations"></a>
+ **Pricing** – AI analysis uses Amazon Bedrock to process your environment data, and standard Amazon Bedrock pricing applies for model invocations. For pricing details, see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/).
+ **Platform requirement** – AI analysis is available on Amazon Linux 2 and AL2023 based platform versions released on or after February 26, 2026. For Windows Server platforms, AI analysis is available on platform versions released on or after April 22, 2026. To use this feature, update your environment to a supported platform version. For more information, see [Updating your Elastic Beanstalk environment's platform version](using-features.platform.upgrade.md).
+ **Permissions** – Before using AI analysis, ensure that your instance profile has the required Amazon Bedrock permissions (`bedrock:InvokeModel` and `bedrock:ListFoundationModels`) and Elastic Beanstalk permissions (`elasticbeanstalk:DescribeEvents` and `elasticbeanstalk:DescribeEnvironmentHealth`).
+ **Data privacy** – The analysis sends environment events and logs to Amazon Bedrock in your account for processing. For information about how Amazon Bedrock handles your data, see [Amazon Bedrock Security and Compliance](https://aws.amazon.com/bedrock/security-compliance/).
+ **Service quotas** – AI analysis uses Amazon Bedrock foundation models, which have default quotas for requests per minute and tokens per minute. In commercial regions, Anthropic Claude models are used. In GovCloud regions, the NVIDIA Nemotron model is used. If you encounter throttling errors, you can request a quota increase. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

## Supported platform versions
<a name="health-ai-analysis-supported-platforms"></a>

AI analysis is supported on Amazon Linux 2 and AL2023 based platform versions released on or after [February 26, 2026](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-02-26-al2023.html). For Windows Server platforms, AI analysis is supported on platform versions released on or after [April 22, 2026](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-04-22-windows.html). To verify your platform version, see [Elastic Beanstalk release notes](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/welcome.html).