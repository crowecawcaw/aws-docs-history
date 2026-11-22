

# Decommission an AWS Control Tower landing zone

AWS Control Tower allows you to set up and govern secure multi-account AWS environments, known as landing zones. The process of cleaning up all of the resources allocated by AWS Control Tower is referred to as *decommissioning* a landing zone. 

If you no longer want to use AWS Control Tower, the automated decommissioning tool cleans up the resources allocated by AWS Control Tower. To begin the automated decommissioning process, navigate to the **Landing Zone Settings** page, select the decommission tab, and choose **Decommission landing zone**.

For a list of actions performed during decommissioning, see [Overview of the decommissioning process](decommissioning-process-overview.md).

**Warning**  
Manually deleting the AWS Control Tower resources of a fully deployed landing zone is not the same as decommissioning it through the AWS Control Tower console or APIs. Manual deletion does not fully clean up the landing zone and can leave it in a state where you cannot set up a new one. To decommission a completed landing zone, always use the AWS Control Tower console or APIs.

 Your data and your existing AWS Organizations are not changed by the decommissioning process, in the following ways.
+ AWS Control Tower does not remove your data, it only removes parts of the landing zone that it created.
+ After the decommissioning process is complete, a few resource artifacts remain, such as Amazon S3 buckets and Amazon CloudWatch Logs log groups. These resources must be deleted manually before you set up another landing zone, and to avoid possible costs associated with maintaining certain resources.
+ You can't use automated decommissioning to remove a landing zone that is only partially set up. If your landing zone setup fails, first try to resolve the failure and complete setup, which then makes automated decommissioning possible. If setup cannot be completed, contact AWS Support for troubleshooting assistance.

*Decommissioning a landing zone is a process with significant consequences, and it cannot be undone.* The decommissioning actions taken by AWS Control Tower and the artifacts that remain after decommissioning are described in the following sections.

**Important**  
 We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone. It is not possible to re-create your existing landing zone after you've decommissioned it.