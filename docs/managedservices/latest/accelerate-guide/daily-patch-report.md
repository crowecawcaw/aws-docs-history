

# Patch report (daily)
<a name="daily-patch-report"></a>

**Topics**
+ [Instance details summary for AMS patching](#instance-details-summary-po)
+ [Patch details](#patch-details)
+ [Instances that missed patches](#instances-that-missed-patches)

## Instance details summary for AMS patching
<a name="instance-details-summary-po"></a>

This is an informational report that helps identify all the instances onboarded to AMS Patching, account status, instance details, maintenance window coverage, maintenance window execution time, stack details, and platform type.

**This dataset provides:**
+ Data on the Production and Non-Production instances of an account. Production and Non-Production stage is derived from the account name and not from the instance tags.
+ Data on the distribution of instances by platform type. The 'N/A' platform type occurs when AWS Systems Manager (SSM) can't get the platform information.
+ Data on the distribution of state of instances, number of instances running, stopped, or terminating.


| **Console Field Name** | **Dataset Field Name** | **Definition** | 
| --- | --- | --- | 
| Access Restrictions | access\_restrictions | Regions to which access is restricted | 
| Account Id | aws\_account\_id | AWS Account ID to which the instance ID belongs | 
| Admin Account Id | aws\_admin\_account\_id | Trusted AWS Organizations account enabled by you. | 
|  Account Name | account\_name | AWS account name | 
| Account Status | account\_status | AMS account status | 
|   | account\_sla | AMS account service commitment | 
| Account Type | malz\_role | MALZ role | 
| Auto Scaling Group Name | instance\_asg\_name | Name of Auto Scaling Group (ASG) that contains the instance | 
| Instance Id | instance\_id | ID of EC2 instance | 
| Instance Name | instance\_name | Name of EC2 instance | 
| Instance Patch Group | instance\_patch\_group | Patch group name used to group instances together and apply the same maintenance window | 
| Instance Patch Group Type | instance\_patch\_group\_type | Patch group type | 
| Instance Platform Type | instance\_platform\_type | Operating System (OS) type | 
| Instance Platform Name | instance\_platform\_name | Operating System (OS) name | 
| Instance State | instance\_state | State within the EC2 instance lifecycle | 
| Instance Tags | ec2\_tags | The tags associated with the Amazon EC2 instance ID | 
| Landing Zone | malz\_flag | Flag for MALZ-related account | 
| Maintenance Window Coverage | mw\_covered\_flag | If an instance has at least one enabled maintenance window with a future execution date, then it’s considered covered, otherwise not covered | 
| Maintenance Window Execution Datetime | earliest\_window\_execution\_time | Next time the maintenance window is expected to execute | 
| Maintenance Window Execution Datetime | earliest\_window\_execution\_time | Next time the maintenance window is expected to execute | 
| Production Account | prod\_account | Identifier of AMS prod, non-prod accounts, depending on whether account name include value 'PROD', 'NONPROD'. | 
| Report Datetime | dataset\_datetime | The date and time the report was generated. | 
| Stack Name | instance\_stack\_name | Name of stack that contains instance | 
| Stack Type | instance\_stack\_type | AMS stack (AMS infrastructure within customer account) or Customer stack (AMS managed infrastructure that supports customer applications) | 

## Patch details
<a name="patch-details"></a>

This report provides patch details and maintenance window coverage of various instances.

**This report provides:**
+ Data on Patch groups and its types.
+ Data on Maintenance Windows, duration, cutoff, future dates of maintenance window executions (schedule) and instances impacted in each window.
+ Data on all the operating systems under the account and the number of instances that the operating system is installed.


| **Field Name** | **Dataset Field Name** | **Definition** | 
| --- | --- | --- | 
| Report Datetime | dataset\_datetime | The date and time the report was generated. | 
| Account Id | aws\_account\_id | AWS Account ID to which the instance ID belongs | 
| Account Name | account\_name | AWS account name | 
| Account Status | account\_status | AMS account status | 
| Compliant - Critical | compliant\_critical | Count of compliant patches with "critical" severity | 
| Compliant - High | compliant\_high | Count of compliant patches with "high" severity | 
| Compliant - Medium | compliant\_medium | Count of compliant patches with "medium" severity | 
| Compliant - Low  | compliant\_low | Count of compliant patches with "low" severity | 
| Compliant - Informational | compliant\_informational | Count of compliant patches with "informational" severity | 
| Compliant - Unspecified | compliant\_unspecified | Count of compliant patches with "unspecified" severity | 
| Compliant - Total | compliant\_total | Count of compliant patches (all severities) | 
| Instance Id | instance\_id | ID of EC2 instance | 
| Instance Name | instance\_name | Name of EC2 instance | 
|  | account\_sla | AMS account service tier | 
| Instance Platform Type | instance\_platform\_type | Operating System (OS) type | 
| Instance Platform Name | instance\_platform\_name | Operating System (OS) name | 
| Instance Patch Group Type | instance\_patch\_group\_type | DEFAULT: default patch group w/ default maintenance window, determined by AMSDefaultPatchGroup:True tag on the instance<br />CUSTOMER: customer created patch group<br />NOT\_ASSIGNED: no patch group assigned | 
| Instance Patch Group | instance\_patch\_group | Patch group name used to group instances together and apply the same maintenance window | 
| Instance State | instance\_state | State within the EC2 instance life cycle | 
| Instance Tags | ec2\_tags | The tags associated with the Amazon EC2 instance ID | 
| Last Execution Maintenance Window | last\_execution\_window | The latest time the maintenance window was executed | 
| Maintenance Window Id | window\_id | Maintenance window ID | 
| Maintenance Window State | window\_state | Maintenance window state | 
| Maintenance Window Type | window\_type | Maintenance window type | 
| Maintenance Window Next Execution Datetime | window\_next<br />execution\_time | Next time the maintenance window is expected to execute | 
| Maintenance Window Duration (hrs) | window\_duration | The duration of the maintenance window in hours | 
| Maintenance Window Coverage | mw\_covered\_flag | If an instance has at least one enabled maintenance window with a future execution date, then it’s considered covered, otherwise not covered | 
| Noncompliant - Critical | noncompliant\_critical | Count of noncompliant patches with "critical" severity | 
| Noncompliant - High | noncompliant\_high | Count of noncompliant patches with "high" severity | 
| Noncompliant - Medium | noncompliant\_medium | Count of noncompliant patches with "medium" severity | 
| Noncompliant - Low | noncompliant\_low | Count of noncompliant patches with "low" severity | 
| Noncompliant - Informational | noncompliant<br />\_informational | Count of noncompliant patches with "informational" severity | 
| Noncompliant - Unspecified | noncompliant<br />\_unspecified | Count of noncompliant patches with "unspecified" severity | 
| Noncompliant - Total | noncompliant\_total | Count of noncompliant patches (all severities) | 
| Patch Baseline Id | patch\_baseline\_id | Patch baseline currently attached to instance | 
| Patch Status | patch\_status | Overall patch compliance status. If there is at least one missing patch, instance is considered noncompliant, otherwise compliant. | 
| Production Account | prod\_account | Identifier of AMS prod, non-prod accounts, depending on whether account name include value 'PROD', 'NONPROD'. | 
| Stack Type | instance\_stack\_type | AMS stack (AMS infrastructure within customer account) or Customer stack (AMS managed infrastructure that supports customer applications) | 
|  | window\_next\_exec\_yyyy | Year part of window\_next\_execution\_time | 
|  | window\_next\_exec\_mm | Month part of window\_next\_execution\_time | 
|  | window\_next\_exec\_D | Day part of window\_next\_execution\_time | 
|  | window\_next<br />\_exec\_HHMI | Hour:Minute part of window\_next\_execution\_time | 

## Instances that missed patches
<a name="instances-that-missed-patches"></a>

This report provides details on instances that missed patches during the last maintenance window execution.

**This report provides:**
+ Data on missing patches at the patch ID level.
+ Data on all the instances that have at least one missing patch and attributes such as patch severity, unpatched days, range, and release date of the patch.


| **Field Name** | **Dataset Field Name** | **Definition** | 
| --- | --- | --- | 
| Report Datetime | dataset\_datetime | The date and time the report was generated | 
| Account Id | aws\_account\_id | AWS Account ID that the instance ID belongs to | 
| Account Name | account\_name | AWS account name | 
| Customer Name Parent | customer\_name\_parent |  | 
| Customer Name | customer\_name |  | 
| Production Account | prod\_account | Identifier of AMS prod or non-prod accounts, depending on whether the account name includes the value 'PROD' or 'NONPROD'. | 
| Account Status | account\_status | AMS account status | 
| Account Type | account\_type |  | 
|  | account\_sla | AMS account service tier | 
| Instance Id | instance\_id | ID of your EC2 instance | 
| Instance Name | instance\_name | Name of your EC2 instance | 
| Instance Platform Type | instance\_platform\_type | Operating System (OS) type | 
| Instance State | instance\_state | State within the EC2 instance life cycle | 
| Instance Tags | ec2\_tags | The tags associated with the Amazon EC2 instance ID | 
| Patch Id | patch\_id | ID of released patch | 
| Patch Severity | patch\_sev | Severity of patch per publisher | 
| Patch Classification | patch\_class | Classification of patch per the patch publisher | 
| Patch Release Datetime (UTC) | release\_dt\_utc | Release date of patch per publisher | 
| Patch Install State | install\_state | Install state of patch on instance per SSM | 
| Days Unpatched | days\_unpatched | Number of days instance unpatched since last SSM scanning | 
| Days Unpatched Range | days\_unpatched\_bucket | Bucketing of days unpatched | 