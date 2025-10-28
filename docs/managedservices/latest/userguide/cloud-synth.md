# Use AMS SSP to provision Amazon CloudWatch Synthetics in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon CloudWatch Synthetics capabilities directly in your AMS managed account. You can use Amazon CloudWatch Synthetics to create 'canaries' to monitor your endpoints and APIs.

Canaries are configurable scripts, written in Node.js or Python, that run on a schedule. They create Lambda functions in your account that use
Node.js or Python as a framework. Canaries work over both HTTP and HTTPS protocols. Canaries check the availability and latency of your endpoints
and can store load time data and UI screenshots. They monitor your REST APIs, URLs, and website content, and they can check for unauthorized changes
from phishing, code injection and cross-site scripting.

Canaries follow the same routes and perform the same actions as a customer, making it possible for you to continually verify your customer
experience even when you don't have any customer traffic on your applications. By using canaries, you can discover issues before your customers do.
To learn more, see [Amazon CloudWatch: Using synthetic monitoring](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md").

## Amazon CloudWatch Synthetics in AWS Managed Services FAQ

**Q: How do I request access to Amazon CloudWatch Synthetics in my AMS account?**

Request access to Amazon CloudWatch Synthetics by submitting an RFC with the
Management | AWS service | Self-provisioned
service | Add (ct-1w8z66n899dct) change type. This RFC provisions the following IAM role to your account: 'customer_cw_synthetics_console_role'
and 'customer_cw_synthetics_canary_lambda_role'. Once provisioned in your account, you must onboard the
'customer_cw_synthetics_console_role' role in your federation solution.

**Q: What are the restrictions to using Amazon CloudWatch Synthetics in my AMS account?**

There are no restrictions for the use of Amazon CloudWatch Synthetics in your AMS account.
Creating roles for canaries outside of
the AMS-provided service role 'customer_cw_synthetics_canary_lambda_role' is prohibited.

**Q: What are the prerequisites or dependencies to using Amazon CloudWatch Synthetics in
my AMS account?**

Canaries create and use a default Amazon CloudWatch Synthetics S3 bucket:
"cw-syn-results-`${accountnumber}`-`${default-region}`"
