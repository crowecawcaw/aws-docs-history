

# Manage hybrid Wait and Save plus Spot fleet capacity with CloudFormation
<a name="examples-cfn-capacity-manager"></a>

The smf\_capacity\_manager CloudFormation template implements automated capacity management for hybrid fleet setups that combine Wait and Save and Spot fleets. The template uses Lambda and EventBridge Scheduler to dynamically balance fleet sizes while maintaining a constant total capacity. The capacity manager monitors the Wait and Save fleet's active worker count and automatically adjusts the Spot fleet's maximum worker count to cover any deficit. For the template source, see [smf\_capacity\_manager](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/smf_capacity_manager) on the GitHub website.

For example, with a target maximum worker count of 20 workers:
+ Wait and Save has 15 workers. Spot fleet maximum is set to 5.
+ Wait and Save scales down to 8. Spot fleet maximum increases to 12.
+ Wait and Save scales up to 18. Spot fleet maximum decreases to 2.

Workers are only terminated when their tasks complete, so fleets rebalance for cost-effectiveness without losing work in progress.

To deploy the template, you need an existing Deadline Cloud farm with two service-managed fleets (Wait and Save and Spot) that have the same worker capabilities. Set the Spot fleet's `minWorkerCount` to 0 so that the capacity manager can scale it down to zero when the Wait and Save fleet is at full capacity.