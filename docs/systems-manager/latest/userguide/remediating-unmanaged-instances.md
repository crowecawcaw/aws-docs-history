

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Diagnosing and remediating unmanaged Amazon EC2 instances in Systems Manager
<a name="remediating-unmanaged-instances"></a>

To help you manage your Amazon Elastic Compute Cloud (Amazon EC2) instances with Systems Manager, you can use the unified Systems Manager console to do the following:

1. Run a manual or scheduled diagnosis process to identify which EC2 instances in your account or organization aren't currently managed by Systems Manager.

1. Identify network or other issues that are preventing Systems Manager from taking over management of the instances.

1. Run an Automation execution to automatically remediate the problem, or access information to help you manually address the issue.

Use the information in the following topics to help you diagnose and remediate issues that are preventing Systems Manager from managing your EC2 instances.

## How Systems Manager counts impacted nodes for the 'Unmanaged EC2 instance issues' list
<a name="unmanaged-instance-scan-count"></a>

The number of nodes reported as unmanaged on the **Unmanaged EC2 instances issues** tab represents to the total number of instances with any of the follow status values at the diagnosis scan time: 
+ `Running`
+ `Stopped`
+ `Stopping`

This number is reported as **Impacted nodes** in the **Issue summary** area. In the following image, this number of impacted nodes not currently managed by Systems Manager is `40`.

![The "Issue summary" area showing 40 impacted nodes in the Diagnose and remedidate page](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/2-unmanaged-EC2-instance-count.png)


Unlike the report of unmanaged EC2 instances on the **Review node insights** page, this count of EC2 instances is not dynamic. It represents findings made during the last reported diagnostic scan, shown as the **Scan time** value. We therefore recommend running a diagnostic scan for unmanaged EC2 instances on a regular schedule to keep this reported number of impacted nodes up to date.

For information about unmanaged instance counts on the **Review node insights** page, see [What is an unmanaged instance?](review-node-insights.md#unmanaged-instance-definition) in the topic [Reviewing node insights](review-node-insights.md).

**Topics**
+ [How Systems Manager counts impacted nodes for the 'Unmanaged EC2 instance issues' list](#unmanaged-instance-scan-count)
+ [Categories of diagnosable unmanaged EC2 instance issues](diagnosing-ec2-category-types.md)
+ [Running a diagnosis and optional remediation for unmanaged EC2 instances](running-diagnosis-execution-ec2.md)
+ [Scheduling a recurring scan for unmanaged EC2 instances](schedule-recurring-ec2-diagnosis.md)