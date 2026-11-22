

# Security best practices for Performance Monitor

The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

## Preventative best practices
<a name="CloudWatch-PerformanceMonitor-security-best-practices-preventative"></a>
+ **Apply least privilege** – Grant permissions to create, edit, or delete monitors only to the users who manage them. Give users who only need to view network path data read-only permissions.
+ **Restrict who can change the scope** – The scope is shared with Network Flow Monitor, so changes to it affect both features. Limit scope-modification permissions to administrators.
+ **Use a delegated administrator account** – For multi-account monitoring, register a delegated administrator account instead of using your AWS Organizations management account for day-to-day monitoring tasks.
+ **Use temporary credentials** – Use IAM roles with temporary credentials instead of long-term access keys.

## Detective best practices
<a name="CloudWatch-PerformanceMonitor-security-best-practices-detective"></a>
+ **Log API activity with CloudTrail** – Review CloudTrail management events for changes to monitors and the scope. To also record query activity, turn on data events. For more information, see [Log Performance Monitor API calls with AWS CloudTrail](CloudWatch-PerformanceMonitor-monitoring-overview.md).
+ **Review IAM permissions regularly** – Periodically review which users and roles have permissions for Performance Monitor, and remove permissions that are no longer needed.