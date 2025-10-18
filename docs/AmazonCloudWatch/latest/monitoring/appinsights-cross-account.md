# Application Insights cross-account observability

With CloudWatch Application Insights cross-account observability, you can monitor and troubleshoot your applications that span multiple AWS accounts within a single Region.

You can use Amazon CloudWatch Observability Access Manager to set up one or more of your AWS accounts as a monitoring account. You’ll provide the monitoring account with the ability to view data 
 in your source account by creating a sink in your monitoring account. You use the sink to create a link from your source account to your monitoring account. For more information, see 
 [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").


###### Required resources


For proper functionality of CloudWatch Application Insights cross-account observability, ensure that the following telemetry types are shared through the CloudWatch Observability Access Manager.



* Applications in CloudWatch Application Insights
* Metrics in Amazon CloudWatch
* Log groups in Amazon CloudWatch Logs
* Traces in [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html")
