# Available versions of the AWS FIS extension for Lambda

This section includes information about the AWS FIS Lambda extension versions. The extension supports Lambda functions developed for the x86-64 and ARM64 (Graviton2) platforms.
Your Lambda function must be configured to use the specific Amazon Resource Name (ARN) for the AWS Region where it is currently hosted.
You can view AWS Region and ARN details below.

###### Topics

- [AWS FIS Lambda extension release notes](#extension-release-notes "#extension-release-notes")
- [Access Guide for Lambda Extension ARNs](#extension-arns-access-guide "#extension-arns-access-guide")

## AWS FIS Lambda extension release notes

The following table describes changes made to recent versions of the AWS FIS Lambda extension

| Version | Launch date | Notes           |
| ------- | ----------- | --------------- |
| 1.0.0   | 2024-10-29  | Initial release |

## Access Guide for Lambda Extension ARNs

You must have at least one parameter in your AWS account and AWS Region
before you can search for public parameters using the console.
To discover public parameters, see
[Discovering public parameters in Parameter Store](../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md "../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md").

### Console Access:

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose the **Public parameters** tab.
4. Choose the **Select a service** dropdown. From the dropdown options, choose `fis`.
5. (Optional) Filter the parameters you selected by entering more information into the search bar. For arm64 architectures, filter parameters by entering _"arm64"_. For x86_64 architectures, filter parameters by entering _"x86_64"_.
6. Choose the public parameter you want to use.
7. From the parameter details, locate the ARN value. Copy the ARN to use in configuring layer extensions on your target Lambda functions.

### AWS CLI Access:

#### SSM Parameter Names

The following SSM parameter names are available for different architectures:

1. arm64: `/aws/service/fis/lambda-extension/AWS-FIS-extension-arm64/1.x.x`
2. x86_64: `/aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x`

#### AWS CLI Command Format

To retrieve the extension ARNs, use the following AWS CLI command format where
_parameterName_ is the name for the architecture and
_region_ is the target AWS Region:

```
aws ssm get-parameter --name parameterName --region region
```

#### Example Usage

```
aws ssm get-parameter --name /aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x --region ap-southeast-2
```

#### Response Format

The command returns a JSON object containing the parameter details like the following.
The ARN of the Lambda layer is included in the _Value_ field of the
_Parameter_ object. Copy the ARN to use in configuring layer extensions on your target Lambda functions.

```

 {
     "Parameter":
        {
             "Name": "/aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x",
             "Type": "String",
             "Value": "arn:aws:lambda:ap-southeast-2:211125361907:layer:aws-fis-extension-x86_64:9",
             "Version": 1,
             "LastModifiedDate": "2025-01-02T15:13:54.465000-05:00",
             "ARN": "arn:aws:ssm:ap-southeast-2::parameter/aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x",
             "DataType": "text"
        }
 }

```

### Programmatic Access:

Retrieve these public parameters programmatically when building or configuring your Lambda
functions using Infrastructure as Code (IaC). This approach helps maintain your Lambda functions with
the latest layer version ARN without requiring manual code updates that would be necessary if
the AWS FIS extension layer ARN were hardcoded. The following resources show how to retrieve
public parameters using common IaC platforms:

- [Get public parameters using the AWS SDK](../../../systems-manager/latest/APIReference/API_GetParameter.md "../../../systems-manager/latest/APIReference/API_GetParameter.md")
- [Get public parameters from AWS Systems Manager Parameter Store using the AWS CDK](../../../cdk/v2/guide/get-ssm-value.md "../../../cdk/v2/guide/get-ssm-value.md")
- [Get public parameters using Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ssm_parameter "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ssm_parameter")
