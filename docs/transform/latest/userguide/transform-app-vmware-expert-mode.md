

# Use expert mode
<a name="transform-app-vmware-expert-mode"></a>

Expert mode minimizes interaction during a migration job. You provide inputs and preferences before execution, and the agent applies them automatically as the job progresses. The agent pauses only when it can't resolve a question or when an error requires action.

**To use expert mode**

1. Create the migration job and define its job plan. Before starting any step, enable expert mode by entering "Run this job in expert mode" in chat or by entering the /expert-mode-on command in the web application.

1. Start the job. The agent adds **Data collection** as the first step and displays the inputs that are available for your job plan.

1. Provide your inputs and preferences. You can include multiple values in one message or attach a UTF-8 text file (maximum 256 KB). For example, enter "Use multi-account migration, average Amazon EC2 sizing, shared tenancy, and a maximum of 20 servers per wave."

1. Optionally, specify review checkpoints or mode switches. For example, enter "Pause for my review after migration planning" or "Switch to standard mode after network migration."

1. Review the collected values and correct any values that the agent marks as invalid, and tell the agent to proceed.

The agent processes steps and waves sequentially, presenting intermediate results without waiting for confirmation unless you set a review checkpoint. You can send instructions in chat at any time and switch to standard mode on demand.

## Limitations
<a name="transform-app-vmware-expert-mode-limitations"></a>
+ You must enable expert mode before any step starts. You can't enable it mid-job.
+ The agent pauses when it can't resolve a question from collected inputs, when an input is invalid, or when an error requires action.
+ Expert mode doesn't bypass approval requirements. Operations that require approval still wait for authorization in the **Approvals** tab.
+ Collected settings apply globally to all relevant steps and waves. Wave-specific instructions are evaluated when that wave runs.
+ Input text files must use UTF-8 encoding and can't exceed 256 KB. This limit doesn't apply to inventory or other migration artifacts.