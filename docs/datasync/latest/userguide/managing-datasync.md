

# Managing AWS DataSync resources
<a name="managing-datasync"></a>

Learn how to manage your AWS DataSync resources, such as agents, locations, and tasks.

## Managing your DataSync agent
<a name="managing-agent-overview"></a>

Once you activate a DataSync agent, AWS manages the agent for you (including software updates). [Learn more](managing-agent.md)

## Testing your DataSync agent's connectivity and system resources
<a name="local-console-overview"></a>

While AWS manages your DataSync agent once it's deployed and activated, there might be cases where you need to change your agent's settings or troubleshoot an issue. [Learn more](local-console-vm.md)

## Replacing your DataSync agent
<a name="replacing-agent-overview"></a>

To replace a DataSync agent, you must create a new agent and update any locations that are using the old agent. [Learn more](replacing-agent.md)

## Cleaning up DataSync resources
<a name="clean-up-overview"></a>

If you used DataSync for a test or just no longer need its resources, delete those resources so that you aren't charged for them. [Learn more](clean-up.md)

## Reusing a DataSync agent's infrastructure
<a name="reusing-agent-overview"></a>

After you delete an agent resource from DataSync, you can still use the agent's virtual machine or Amazon EC2 instance to activate a new agent. [Learn more](clean-up.md#reusing-agent)