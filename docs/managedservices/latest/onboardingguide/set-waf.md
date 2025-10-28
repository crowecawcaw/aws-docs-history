# Use AMS SSP to provision AWS WAF - Web Application Firewall in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access AWS WAF capabilities directly in your AMS managed account. AWS WAF is a web application firewall (AWS WAF) that helps protect your web applications from common web exploits that
could affect application availability,
compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow, or block, to
your web applications by defining customizable web security rules.
You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting;
and rules that are designed for your specific application.

To learn more, see [AWS WAF - Web Application Firewall](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/").

AMS doesn't support monitoring (CloudWatch alarms / events / MMS alerts) for AWS WAF.
Due to the nature of AWS WAF, you must create custom rules for your applications; AMS
can't quantify and create alarms for you, without context of your application. To learn more, see
[AWS WAF - Web Application Firewall](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/").

## AWS WAF in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request AWS WAF to be set up in my AMS account?**

Request access to AWS WAF by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account: `customer_waf_role`. After the AWS WAF IAM role is provisioned
in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using AWS WAF?**

After permissions are provisioned, you have the full functionality of AWS WAF.

**Q: What are the prerequisites or dependencies to using AWS WAF?**

There are no prerequisites or dependencies to use AWS WAF in your AMS account.
