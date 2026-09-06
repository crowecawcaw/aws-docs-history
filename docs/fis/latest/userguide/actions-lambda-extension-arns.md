

# Available versions of the AWS FIS extension for Lambda
<a name="actions-lambda-extension-arns"></a>

This section includes information about the AWS FIS Lambda extension versions. The extension supports Lambda functions developed for the x86-64 and ARM64 (Graviton2) platforms. Your Lambda function must be configured to use the specific Amazon Resource Name (ARN) for the AWS Region where it is currently hosted. You can view AWS Region and ARN details below.

**Topics**
+ [AWS FIS Lambda extension release notes](#extension-release-notes)
+ [Access Guide for Lambda Extension ARNs](#extension-arns-access-guide)
+ [Finding your Lambda extension version number](#extension-version-find)

## AWS FIS Lambda extension release notes
<a name="extension-release-notes"></a>

The following table describes changes made to recent versions of the AWS FIS Lambda extension


| Version | Launch date | Notes | 
| --- | --- | --- | 
| 1.0.6 | 2025-01-29 | Improved support for larger fault configuration responses. | 
| 1.0.0 | 2024-10-29 | Initial release | 

## Access Guide for Lambda Extension ARNs
<a name="extension-arns-access-guide"></a>

You must have at least one parameter in your AWS account and AWS Region before you can search for public parameters using the console. To discover public parameters, see [Discovering public parameters in Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html). 

### Console Access:
<a name="extension-arns-access-guide.console-access"></a>

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

1. Choose the **Public parameters** tab.

1. Choose the **Select a service** dropdown. From the dropdown options, choose `fis`.

1. (Optional) Filter the parameters you selected by entering more information into the search bar. For arm64 architectures, filter parameters by entering *"arm64"*. For x86\_64 architectures, filter parameters by entering *"x86\_64"*.

1. Choose the public parameter you want to use.

1. From the parameter details, locate the ARN value. Copy the ARN to use in configuring layer extensions on your target Lambda functions.

### AWS CLI Access:
<a name="extension-arns-access-guide.cli-access"></a>

#### SSM Parameter Names
<a name="extension-arns-access-guide.cli-access.ssm-parameter-names"></a>

The following SSM parameter names are available for different architectures:

1. arm64: `/aws/service/fis/lambda-extension/AWS-FIS-extension-arm64/1.x.x`

1. x86\_64: `/aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x`

#### AWS CLI Command Format
<a name="extension-arns-access-guide.cli-access.cli-command-format"></a>

To retrieve the extension ARNs, use the following AWS CLI command format where *parameterName* is the name for the architecture and *region* is the target AWS Region:

```
aws ssm get-parameter --name parameterName --region region
```

#### Example Usage
<a name="extension-arns-access-guide.cli-access.example-usage"></a>

```
aws ssm get-parameter --name /aws/service/fis/lambda-extension/AWS-FIS-extension-x86_64/1.x.x --region ap-southeast-2
```

#### Response Format
<a name="extension-arns-access-guide.cli-access.response-format"></a>

The command returns a JSON object containing the parameter details like the following. The ARN of the Lambda layer is included in the *Value* field of the *Parameter* object. Copy the ARN to use in configuring layer extensions on your target Lambda functions.

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
<a name="extension-arns-access-guide.programmatic-access"></a>

Retrieve these public parameters programmatically when building or configuring your Lambda functions using Infrastructure as Code (IaC). This approach helps maintain your Lambda functions with the latest layer version ARN without requiring manual code updates that would be necessary if the AWS FIS extension layer ARN were hardcoded. The following resources show how to retrieve public parameters using common IaC platforms:
+ [Get public parameters using the AWS SDK](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html)
+ [Get public parameters from AWS Systems Manager Parameter Store using the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/get-ssm-value.html)
+ [Get public parameters using Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ssm_parameter)

## Finding your Lambda extension version number
<a name="extension-version-find"></a>

Use the following procedure to locate the version number of your currently configured AWS FIS Lambda extension.

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. Choose the Lambda function where you want to add the `AWS-FIS-Extension` layer.

1. In the **Layers** section, choose **Edit**.

1. In the **Edit layers** section, choose **Add a layer**.

1. In the **Choose a layer** section, choose **Specify an ARN**.

1. Enter the ARN for the AWS FIS extension layer that corresponds to your AWS Region and architecture. You can find the ARN using the console, AWS CLI, or programmatic access methods described in the preceding sections.

1. Choose **Verify** to confirm the layer ARN is valid, then choose **Add**.

1. Use the **Test** tab to test the function.

1. After the test completes, view the log output. Locate the AWS FIS Lambda extension version in the **Details of the Execution** section.