

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Choosing between State Manager and Maintenance Windows
<a name="state-manager-vs-maintenance-windows"></a>

State Manager and Maintenance Windows, both tools in AWS Systems Manager, can perform some similar types of updates on your managed nodes. Which one you choose depends on whether you need to automate system compliance or perform high-priority, time-sensitive tasks during periods you specify.

## State Manager and Maintenance Windows: Key use cases
<a name="sm-mw-use-cases"></a>

State Manager sets and maintains the targeted state configuration for managed nodes and AWS resources within your AWS account. You can define combinations of configurations and targets as association objects. Use State Manager if you want to maintain a consistent state across all managed nodes, use Amazon EC2 Auto Scaling to generate new nodes, or have strict compliance reporting requirements.

The main use cases for State Manager are as follows:
+ **Auto Scaling scenarios: **State Manager can monitor all new nodes launched within an account either manually or through Auto Scaling groups. If there are any associations in the account targeting that new node (through tags or all nodes), then that particular association is automatically applied to the new node.
+ **Compliance reporting:** State Manager can drive compliance reporting of required states for resources in your account. 
+ **Supporting all nodes:** State Manager can target all nodes within a given account.

A **maintenance window** takes one or more actions on AWS resources within a given time window. You can define a single maintenance window with start and end times. You can specify multiple tasks to run within this maintenance window. Use Maintenance Windows if your priorities include patching managed nodes, running multiple task types during an update period, or controlling when updates run.

The main use cases for Maintenance Windows are as follows:
+ **Running multiple documents:** Maintenance windows can run multiple tasks. Each task can use a different document type. As a result, you can build complex workflows using different tasks within a single maintenance window.
+ **Patching:** A maintenance window can provide patching support for all managed nodes in a single Region that are tagged with a specific tag or resource group. Patching usually involves removing nodes from a load balancer, applying patches, and putting nodes back into production. You can achieve this as a series of tasks within a patch time window.
**Note**  
Using a maintenance window, your patching operation is limited to a single Region in a single account. Using a patch policy created in Quick Setup, a tool in Systems Manager, you can instead configure patching for some or all accounts and Regions in an organization created in AWS Organizations. For more information, see [Patch policy configurations in Quick Setup](patch-manager-policies.md).
+ **Window actions:** Maintenance windows can make one or more sets of actions start within a specific time window. Maintenance windows won't start outside of that window. Actions already started continue until finished, even if they finish outside of the time window.

The following table compares the main features of State Manager and Maintenance Windows.


| Feature | State Manager | Maintenance Windows | 
| --- | --- | --- | 
| **CloudFormation integration** | AWS CloudFormation templates support State Manager associations. | CloudFormation templates support maintenance windows, window targets, and window tasks. | 
| **Compliance** | Every State Manager association reports compliance against the required state of the targeted resource. You can use the Compliance Dashboard to aggregate and view the reported compliance. | Not applicable. | 
| **Configuration Management integration** | State Manager supports external targeted state solutions such as Microsoft PowerShell Desired State Configuration (DSC), Ansible playbooks, and Chef recipes. You can use State Manager associations to test that the Configuration Management solutions work and to apply their configuration changes to your nodes when you're ready. | Not applicable. | 
| **Documents** | State Manager configurations can be defined as Policy documents (for gathering inventory information), Automation runbooks, for AWS resources such as Amazon Simple Storage Service (Amazon S3) buckets, or Systems Manager Command documents (SSM documents) for managed nodes. | Maintenance Windows configurations can be defined as automation documents (multi-step actions with optional approval workflows) or SSM documents (required state for managed nodes). | 
|  Monitoring  | State Manager monitors changes in the configuration, association, or state of a node (for example, new nodes coming online). When State Manager detects these changes, the given association is re-applied to the nodes originally targeted with that association. | Not applicable. | 
| **Priorities within tasks** | Not applicable. | Tasks within a maintenance window can be assigned a priority. All tasks with the same priority are run in parallel. Tasks with lower priorities are run after tasks with higher priorities reach a final state. There is no way to conditionally run tasks. After a higher priority task reaches its final state, the next priority task runs, regardless of the state of the previous task. | 
| **Safety controls** | State Manager supports two safety controls when deploying configurations across a large fleet. You can use maximum concurrency to define how many concurrent nodes or resources should have the configuration applied. You can define a maximum error rate which can be used to pause the State Manager association if a certain number or percentage of errors occur across the fleet. | Maintenance windows support two safety controls when deploying configurations across a large fleet. You can use maximum concurrency to define how many concurrent nodes or resources should have the configuration applied. You can define a maximum error rate which can be used to pause the actions in a maintenance window if a certain number or percentage of errors occur across the fleet. | 
|  Scheduling  | You can run State Manager associations on demand, at a particular cron interval, at a given rate, or after they're created. This is useful if you want to maintain the required state of your resources in a consistent and timely manner. Cron expressions for State Manager associations do not support the months field, such as `03` or `MAR` for the month of March. If you require monthly or quarterly configuration updates, a maintenance window can best meet your needs. For more information, see [Reference: Cron and rate expressions for Systems Manager](reference-cron-and-rate-expressions.md).  | Maintenance windows support several scheduling options including `at` expressions (for example, `"at(2021-07-07T13:15:30)"`), cron and rate expressions, cron with offsets, and start and end times for when maintenance windows should run, and cutoff times to specify when to stop scheduling within a given time window. | 
| **Targeting** | State Manager associations can target one or more nodes by using node ID, tag, or resource group. State Manager can target all managed nodes within a given account. | Maintenance windows can target one or more nodes using node IDs, tags, or resource groups. | 
| **Tasks within maintenance windows** | Not applicable. | Maintenance windows can support one or more tasks where each task targets a specific Automation runbook or Command document action. All tasks within a maintenance window run in parallel unless different priorities are set for different tasks.<br />Overall, maintenance windows support four task types:+  AWS Systems Manager Run Command commands <br />+  AWS Systems Manager Automation workflows <br />+  AWS Lambda functions <br />+  AWS Step Functions tasks  | 