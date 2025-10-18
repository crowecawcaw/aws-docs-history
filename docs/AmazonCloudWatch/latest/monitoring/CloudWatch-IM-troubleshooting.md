# Troubleshoot CloudWatch logs and metrics access errors

To support some features, Internet Monitor must interact with certain Amazon CloudWatch resources, including logs and 
 metrics. If Internet Monitor can't access the CloudWatch resources that it requires access to, 
 Internet Monitor sets a status code of `FAULT_ACCESS_CLOUDWATCH` for the monitor.

There are several reasons that your monitor might have the state `FAULT_ACCESS_CLOUDWATCH`. 
 The following sections list possible causes for these errors, and suggested troubleshooting steps. 


## Internet Monitor couldn't access CloudWatch logs in your account


Internet Monitor publishes diagnostic logs about your monitored application traffic. It publishes these logs to log groups 
 in CloudWatch Logs in the following location: 
 `/aws/internet-monitor/`monitor_name`/[byCity|byMetro|bySubdivision|byCountry]`. 
 Internet Monitor was unable to access these log groups.


**Error states and potential solutions:**



* **PutLogEvents throttling error:** The Internet Monitor service might have been throttled 
 when it tried to publish your monitor's logs to CloudWatch. Review the throttling limits for your account, and, 
 if necessary, request an increase in the limit.
* **Log group not found:** Disable, and then re-enable your monitor. Enabling a monitor restarts log group 
 creation, which might correct the problem.
* **PutLogEvents access denied error:** Contact AWS support for assistance.
* **PutLogEvents unknown or general error:** Contact AWS support for assistance.

## Internet Monitor couldn't access CloudWatch metrics in your account


Internet Monitor delivers specific CloudWatch metrics about the application traffic that is tracked by a monitor. An error 
 occurred when Internet Monitor tried to deliver these metrics to CloudWatch.


**Error states and potential solutions:**



* **PutMetricData throttling error:** The Internet Monitor service might have been throttled 
 when it tried to publish your monitor's metrics to CloudWatch. Review the throttling limits for your account, and, 
 if necessary, request an increase in the limit.
* **PutMetricData access denied error:** Contact AWS support for assistance.
* **PutMetricData unknown or general error:** Contact AWS support for assistance.
