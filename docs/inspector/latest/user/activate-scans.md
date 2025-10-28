# Activating a scan type

You can activate a scan type at any time.
When you activate a scan type, Amazon Inspector begins scanning eligible resources for the scan type.

###### [Amazon EC2 scanning](scanning-ec2.md "scanning-ec2.md")

This scan type extracts metadata from an Amazon EC2 instance before comparing the metadata against rules collected from security advisories.
When you activate this scan type, Amazon Inspector scans all eligible Amazon EC2 instances in your account for package vulnerabilities and network reachability issues.
After you activate this scan type, you can view how many instances are being scanned in the **Instances** tab.

###### [Amazon ECR scanning](scanning-ecr.md "scanning-ecr.md")

This scan type scans container images and container repositories in Amazon ECR.
When you activate this scan type, you change the scanning configuration setting for your private registry from basic scanning to enhanced scanning.
After you activate Amazon ECR scanning, you can view how many images and repositories are being scanned in the **Container images** and **Container repositories** tabs.

###### [Lambda standard scanning](scanning-lambda.md#lambda-standard-scans "scanning-lambda.md#lambda-standard-scans") + [Lambda code scanning](scanning-lambda.md#lambda-code-scans "scanning-lambda.md#lambda-code-scans")

Lambda standard scanning is the default Lambda scan type.
When you activate Lambda standard scanning, all of your Lambda functions are scanned for software vulnerabilities, as long as they were invoked or updated in the last 90 days.
After you activate Lambda standard scanning, you view how many Lambda functions are being scanned in the **Lambda functions** tab.

Lambda code scanning scans custom application code in a Lambda function.
When you activate Lambda code scanning, all of your Lambda functions will be scanned for code vulnerabilities, as long as they were invoked or updated in the last 90 days.
After you activate Lambda standard scanning, you can view how many Lambda functions are being scanned for code vulnerabilities in the **Lambda functions** tab.

###### Note

If you want to activate Lambda code scanning, you must activate Lambda standard scanning first.

###### [Amazon Inspector Code Security](code-security-assessments.md "code-security-assessments.md")

This scan type scans first-party application code, third-party application dependencies, and Infrastructure as Code for vulnerabilities.
When you activate Code Security, Amazon Inspector begins scanning your code repositories for code vulnerabilities based on your scan configurations.
After you activate Amazon Inspector Code Security, you can view how many code repositories are being scanned in the **Code repositories** tab.

## Activating scans

The following procedure describes how to activate a scan type in Amazon Inspector.

###### Note

If you're the delegated administrator for an AWS organization, you can enable Amazon Inspector scan types for multiple accounts in multiple Regions using a shell script.
For more information, see [inspector2-enablement-with-cli](https://github.com/aws-samples/inspector2-enablement-with-cli "https://github.com/aws-samples/inspector2-enablement-with-cli") on GitHub.
Otherwise, complete the following steps while signed in as the Amazon Inspector delegated administrator.

Console

###### To activate scans

1. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Using the AWS Region selector in the upper-right corner of
   the page, select the Region where you want to activate a new
   scan type.
3. In the navigation pane, choose **Account
   management**.
4. On the **Account management** page, select
   the accounts for which you would like to activate a scan
   type.
5. Choose **Activate** and select the type of
   scanning you would like to activate.
6. (Recommended) Repeat these steps in each AWS Region for
   which you want to activate that scan type.

API
Run the [Enable](../../v2/APIReference/API_Enable.md "../../v2/APIReference/API_Enable.md") API
operation. In the request, provide the account IDs you are activating
scans for, and idempotency token, and one or more of `EC2`,
`ECR`, `LAMBDA`, or `LAMBDA_CODE`
for `resourceTypes` to activate scans of that type.
