• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Auditing and logging Distributor

activity

You can use AWS CloudTrail to audit activity related to Distributor, a tool in AWS Systems Manager. For
more information about auditing and logging options for Systems Manager, see [Logging and monitoring in AWS Systems Manager](monitoring.md "monitoring.md").

## Audit Distributor activity

using CloudTrail

CloudTrail captures API calls made in the AWS Systems Manager console, the AWS Command Line Interface (AWS CLI), and
the Systems Manager SDK. The information can be viewed in the CloudTrail console or stored in an
Amazon Simple Storage Service (Amazon S3) bucket. One bucket is used for all CloudTrail logs for your
account.

Logs of Run Command and State Manager actions show document creation, package
installation, and package uninstallation activity. Run Command and State Manager are tools
in AWS Systems Manager. For more information about viewing and using CloudTrail logs of Systems Manager
activity, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md "monitoring-cloudtrail-logs.md").
