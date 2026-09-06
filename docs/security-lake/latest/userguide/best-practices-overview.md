

# Security best practices for Security Lake
<a name="best-practices-overview"></a>

See the following best practices for working with Amazon Security Lake.

## Grant Security Lake users minimum possible permissions
<a name="minimum-permissions"></a>

Follow the principle of least privilege by granting the minimum set of access policy permissions for your AWS Identity and Access Management (IAM) users, user groups, and roles. For example, you might allow an IAM user to view a list of log sources in Security Lake but not to create sources or subscribers. For more information, see [Identity-based policy examples for Security Lake](security_iam_id-based-policy-examples.md)

You can also use AWS CloudTrail to track API usage in Security Lake. CloudTrail provides a record of API actions taken by a user, group, or role in Security Lake. For more information, see [Logging Security Lake API calls using CloudTrail](securitylake-cloudtrail.md).

## View the Summary page
<a name="summary-page"></a>

The **Summary** page of the Security Lake console provides an overview of issue from the last 14 days that are impacting the Security Lake service and the Amazon S3 buckets in which your data is stored. You can further investigate these issues to help you mitigate possible security-related impact.

## Integrate with Security Hub CSPM
<a name="integrate-security-hub"></a>

Integrate Security Lake and AWS Security Hub CSPM to receive Security Hub CSPM findings in Security Lake. Security Hub CSPM generates findings from many different AWS services and third-party integrations. Receiving Security Hub CSPM findings helps you get an overview of your compliance posture and whether you're meeting AWS security best practices.

For more information, see [Integration with AWS Security Hub CSPM](securityhub-integration.md).

## Delete AWS Lambda
<a name="Lambda"></a>

When deleting a AWS Lambda function, we recommend against disabling it first. Disabling a Lambda function before deletion could interfere with data querying capabilities and potentially impact other functionalities. It's best to delete the Lambda function directly without disabling it. For more information on deleting Lambda function, see [AWS Lambda developer guide](https://docs.aws.amazon.com/lambda/latest/dg/example_lambda_DeleteFunction_section.html).

## Monitor for Security Lake events
<a name="monitor-cloudwatch-metrics"></a>

You can monitor Security Lake using Amazon CloudWatch metrics. CloudWatch collects raw data from Security Lake every minute and processes it into metrics. You can set alarms that trigger notifications when metrics match specified thresholds.

For more information, see [CloudWatch metrics for Amazon Security Lake](cloudwatch-metrics.md).