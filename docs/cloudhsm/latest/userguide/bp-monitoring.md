# AWS CloudHSM monitoring best practices

This section describes multiple mechanisms you can use to monitor your cluster and application. For additional details on monitoring, see [Monitoring AWS CloudHSM](get-logs.md "get-logs.md").


## Monitor client logs


Every Client SDK writes logs that you can monitor. For information on client logging, see [Working with AWS CloudHSM client SDK logs](hsm-client-logs.md "hsm-client-logs.md").


On platforms that are designed to be ephemeral, such as Amazon ECS and AWS Lambda, collecting client logs from a file can be difficult. 
 In these situations, it is a best practice to configure your Client SDK logging to write logs to the console. Most services will automatically collect this output and publish it to Amazon CloudWatch logs 
 for you to keep and view.


If you are using any third-party integration on top of the AWS CloudHSM Client SDK, you should ensure that you configure that software package to log its output to the console as well. 
 The output from the AWS CloudHSM Client SDK may be captured by this package and written to its own log file otherwise.


See the [AWS CloudHSM Client SDK 5 configure tool](configure-sdk-5.md "configure-sdk-5.md") for information on how to configure logging options in your application.


## Monitor audit logs


AWS CloudHSM publishes audit logs to your Amazon CloudWatch account. Audit logs come from the HSM and track certain operations for auditing purposes.


You can use audit logs to keep track of any management commands that are invoked on your HSM. For example, you can trigger an alarm when you notice an unexpected management operation being performed.


See [How HSM audit logging works](get-audit-logs-from-cloudwatch.md "get-audit-logs-from-cloudwatch.md") for more details. 


## Monitor AWS CloudTrail


AWS CloudHSM is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS CloudHSM. AWS CloudTrail captures all API calls for AWS CloudHSM as events. 
 The calls captured include calls from the AWS CloudHSM console and code calls to the AWS CloudHSM API operations.


You can use AWS CloudTrail to audit any API call that is made to the AWS CloudHSM control plane to ensure that no unwanted activity is taking place in your account.


See [Working with AWS CloudTrail and AWS CloudHSM](get-api-logs-using-cloudtrail.md "get-api-logs-using-cloudtrail.md") for details.


## Monitor Amazon CloudWatch metrics


You can use Amazon CloudWatch metrics to monitor your AWS CloudHSM cluster in real time. The metrics can be grouped by region, cluster ID, or HSM ID *and* cluster ID.


Using Amazon CloudWatch metrics, you can configure Amazon CloudWatch alarms to alert you of any potential issue that may arise that could impact your service. We recommend configuring alarms to monitor the following:



* Approaching your key limit on an HSM
* Approaching the HSM session count limit on an HSM
* Approaching the HSM user count limit on an HSM
* Differences in HSM user or key count to identify synchronization issues
* Unhealthy HSMs to scale your cluster up until AWS CloudHSM can resolve the issue

For more details, see [Working with Amazon CloudWatch Logs and AWS CloudHSM Audit Logs](get-hsm-audit-logs-using-cloudwatch.md "get-hsm-audit-logs-using-cloudwatch.md").
