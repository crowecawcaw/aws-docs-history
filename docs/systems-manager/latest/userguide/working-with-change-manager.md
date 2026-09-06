

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with Change Manager
<a name="working-with-change-manager"></a>

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 

With Change Manager, users across your organization or in a single AWS account can perform change-related tasks for which they have been granted the necessary permissions. Change Manager tasks include the following:
+ Create, review, and approve or reject change templates. 

  A change template is a collection of configuration settings in Change Manager that define such things as required approvals, available runbooks, and notification options for change requests.
+ Create, review, and approve or reject change requests.

  A change request is a request in Change Manager to run an Automation runbook that updates one or more resources in your AWS or on-premises environments. A change request is created using a change template.
+ Specify which users in your organization or account can be made reviewers for change templates and change requests.
+ Edit configuration settings, such as how user identities are managed in Change Manager and which of the available *best practice* options are enforced in your Change Manager operations. For information about configuring these settings, see [Configuring Change Manager options and best practices](change-manager-account-setup.md).

**Topics**
+ [Working with change templates](change-templates.md)
+ [Working with change requests](change-requests.md)
+ [Reviewing change request details, tasks, and timelines (console)](reviewing-changes.md)
+ [Viewing aggregated counts of change requests (command line)](change-requests-review-aggregate-command-line.md)