

# Upgrade models for AI prompts and AI agents
<a name="upgrade-models-ai-prompts-agents"></a>

When you customize AI prompts or AI agents in Amazon Connect, the model associated with each AI prompt determines which large language model (LLM) processes the instructions. Over time, newer and more capable models become available. This topic describes how to upgrade models across a few common scenarios.
+ You have a custom AI agent with one or more custom AI prompts using a deprecated model
+ You have a custom AI agent with no prompt overrides
+ You are using older versions of System AI Agents.

## Prerequisites
<a name="upgrade-models-prerequisites"></a>

Before upgrading models, make sure you have the following:
+ An Amazon Connect instance with AI agent designer enabled.
+ An admin account, or an account with AI agent designer permissions in its security profile.
+ Familiarity with [AI prompts](create-ai-prompts.md), [AI agents](create-ai-agents.md), and [default system AI prompts and agents](default-ai-system.md).

## When to upgrade
<a name="upgrade-models-when-to-upgrade"></a>

Amazon Connect notifies you when a model is scheduled for deprecation. Amazon Connect automatically redirects LLM inference to a supported model after any model passes its deprecation date, so there is no service disruption. However, by upgrading manually before the deprecation date, you can choose the replacement model and test it in your environment. Use the following steps to determine which scenarios apply to you.

**Step 1: Check for custom AI agents.** In the admin website, navigate to *AI agent designer*, *AI agents*. Look at the *Type* column. System agents display *- System* after the type name (for example, "Answer Recommendation - System"). Agents without this suffix are custom agents you created.
+ If you have a custom AI agent with one or more custom AI prompts assigned to it → Scenario 1 (if you only overrode some prompt types, the unset prompts auto-upgrade; you only need to upgrade the custom prompts)
+ If you have a custom AI agent with no prompt overrides → Scenario 2 (prompts auto-upgrade, no action needed)
+ If you don't have any custom AI agents, skip to Step 2.

**Step 2: Check the Default AI Agent Configurations.** On the same *AI agents* page, scroll to the *Default AI Agent Configurations* section. If any use case is pinned to a specific version (not set to *Latest*), you can update it → Scenario 3. This applies to all customers, even if you have no custom agents.

## How model resolution works
<a name="upgrade-models-how-model-resolution-works"></a>

When configuring an individual AI agent, you have the option to let Connect choose which LLM to use for each prompt, choose the model you want each prompt to use, or pick a combination of the two options.
+ Each AI prompt has a model property that specifies which LLM to use.
+ Each AI agent references one or more AI prompt versions. A version is an immutable snapshot of the prompt, including its model selection.
+ When you create a custom AI agent and override only some of the prompts associated to the agent, the remaining types are filled from the system defaults at runtime. Prompts you explicitly set are pinned to the version you chose. Prompts filled by the system use the latest system default. This per-prompt-type resolution applies to non-agentic AI agent types such as Answer Recommendation, Manual Search, and Non-Agentic Self Service.
+ Available models depend on the AWS Region of your Amazon Connect instance. For a list of supported models per Region, see [Supported models for system/custom prompts](create-ai-prompts.md#cli-create-aiprompt).

## Scenario 1: Custom AI agent with custom AI prompts
<a name="upgrade-models-scenario-1"></a>

In this scenario, you created a custom AI agent and assigned one or more custom AI prompts to it. The custom prompts are pinned to the model you selected when you published them.

Custom prompts do not automatically receive model upgrades. You must manually update the model, publish a new prompt version, and update the AI agent.

### If you only overrode some prompt types
<a name="upgrade-models-scenario-1-partial-overrides"></a>

Some AI agent types support multiple prompt types. For example, an Answer recommendation AI agent supports three prompt types: intent labeling generation, query reformulation, and answer generation. If you set only some of these to custom prompts and left the rest unset, the following applies:
+ Prompt types you explicitly set (through the admin website or CLI) are pinned to the specific prompt version you chose. They do not change unless you update them. Follow the upgrade steps below for each custom prompt.
+ Prompt types you left unset are not stored in the AI agent configuration. At runtime, Amazon Connect resolves them from the current system defaults. These types always use the latest system prompt versions, including any model upgrades. No action is required for unset prompt types.

### Upgrade using the admin website
<a name="upgrade-models-scenario-1-admin-website"></a>

**Step 1: Create a new prompt version with the updated model**

1. Log in to the Amazon Connect admin website.

1. In the navigation menu, choose *AI agent designer*, *AI prompts*.

1. From the *Prompts* list, select the custom AI prompt you want to upgrade.

1. Choose *Edit in AI Prompt Builder* (top right).

1. The top-right dropdown shows *Latest: Draft*. This is the working copy you will modify.

1. In the *Models* section, use the dropdown to select the new model.

1. Choose *Publish*. This creates a new version of the prompt with the new model.

1. Scroll down to the *Versions* section on the same page. You can confirm the new version has been created.

1. To verify the new version, navigate back to *AI agent designer*, *AI prompts*. Select the prompt from the list, then use the version dropdown (top right) to select the new version. The *Overview* section displays the updated model ID.

**Step 2: Update the AI agent to use the new prompt version**

1. Navigate to *AI agent designer*, *AI agents*.

1. Choose the custom AI agent that references this prompt.

1. Choose *Edit in AI Agent Builder* to open the Agent Builder page.

1. Choose *Add prompt*. A popup appears with available prompts.

1. Select the new prompt version, then choose *Add*. The popup closes and the prompt is added to the agent.

1. Choose *Publish*. This creates a new AI agent version using the custom prompt with the updated model.

1. Scroll down to the *Versions* section to confirm the new AI agent version appears.

1. Optionally, select the latest version from the top-right dropdown. The *Prompts* section displays the new prompt version.

**Step 3: Set the new AI agent version as the default**

1. Navigate to *AI agent designer*, *AI agents*.

1. In the *Default AI Agent Configurations* section, find the use case that is using the custom AI agent and update it to the new version.

1. Choose the check mark icon (✓) to save.

1. To avoid manually updating the version each time, select *Latest* from the version dropdown. This automatically uses the most recently published version of the AI agent.

### Upgrade using the AWS CLI
<a name="upgrade-models-scenario-1-cli"></a>

Update the AI prompt with the new model:

```
aws qconnect update-ai-prompt \
  --assistant-id {{assistant-id}} \
  --ai-prompt-id {{custom-prompt-id}} \
  --model-id {{new-model-id}}
```

Publish a new version of the prompt:

```
aws qconnect create-ai-prompt-version \
  --assistant-id {{assistant-id}} \
  --ai-prompt-id {{custom-prompt-id}}
```

Update the AI agent to reference the new prompt version:

```
aws qconnect update-ai-agent \
  --assistant-id {{assistant-id}} \
  --ai-agent-id {{custom-agent-id}} \
  --configuration '{
    "{{agentTypeConfiguration}}": {
      "{{promptTypeAIPromptId}}": "{{custom-prompt-id}}:{{new-version-number}}"
    }
  }'
```

Publish a new version of the AI agent:

```
aws qconnect create-ai-agent-version \
  --assistant-id {{assistant-id}} \
  --ai-agent-id {{custom-agent-id}}
```

Set the new AI agent version as the default:

```
aws qconnect update-assistant-ai-agent \
  --assistant-id {{assistant-id}} \
  --ai-agent-type {{AGENT_TYPE}} \
  --configuration '{
    "aiAgentId": "{{custom-agent-id}}:{{new-version-number}}"
  }'
```

## Scenario 2: Custom AI agent with no prompt overrides
<a name="upgrade-models-scenario-2"></a>

In this scenario, you created a custom AI agent to customize settings such as locale or knowledge base configuration, but you did not override any prompt types. All prompts are resolved from the system defaults.

### Automatic upgrades
<a name="upgrade-models-scenario-2-automatic"></a>

When Amazon Connect publishes new system AI agent and prompt versions with upgraded models, your custom AI agent automatically picks up the latest system prompt versions. No action is required.

This is because the unset prompt types are resolved at runtime from the current system defaults, which always point to the most recent system prompt versions.

### Force a specific model before a system upgrade
<a name="upgrade-models-scenario-2-force-model"></a>

If you want to use a newer model before Amazon Connect rolls it out as a system default:

1. Create a custom AI prompt by copying the system prompt you want to upgrade.

1. Change the model to the desired newer model.

1. Publish the custom prompt.

1. Edit your custom AI agent and add the custom prompt to the desired type.

1. Publish the AI agent.

This converts that prompt type into a Scenario 1 configuration.

## Scenario 3: Updating Default AI Agent Configurations
<a name="upgrade-models-scenario-3"></a>

The *Default AI Agent Configurations* section on the *AI agents* overview page controls which AI agent version is active for each use case (Answer Recommendation, Manual Search, Self Service).

When an Amazon Connect instance is created, each use case is automatically configured with a specific system AI agent version. These versions are pinned — they do not auto-update when Amazon Connect publishes new system AI agent versions or when you publish new custom AI agent versions. You must manually select the new version.

### Upgrade using the admin website
<a name="upgrade-models-scenario-3-admin-website"></a>

1. Navigate to *AI agent designer*, *AI agents*.

1. In the *Default AI Agent Configurations* section, find the use case you want to update (for example, Answer Recommendation).

1. From the version dropdown, select the new AI agent version.

1. Choose *Save*.

1. To avoid manually updating the version each time, select *Latest* from the version dropdown. This automatically uses the most recently published version of the AI agent.

### Upgrade using the AWS CLI
<a name="upgrade-models-scenario-3-cli"></a>

```
aws qconnect update-assistant-ai-agent \
  --assistant-id {{assistant-id}} \
  --ai-agent-type {{AGENT_TYPE}} \
  --configuration '{
    "aiAgentId": "{{ai-agent-id}}:{{new-version-number}}"
  }'
```

Replace {{AGENT\_TYPE}} with the use case type (for example, `ANSWER_RECOMMENDATION`, `MANUAL_SEARCH`, `SELF_SERVICE`).

## Summary
<a name="upgrade-models-summary"></a>


| \# | Scenario | Auto-upgrades? | Action required | 
| --- | --- | --- | --- | 
| 1 | Custom AI agent with custom AI prompts | Custom prompts: No. Unset prompts: Yes | Edit prompt, change model, publish prompt, update agent, publish agent. Unset prompts auto-upgrade. | 
| 2 | Custom AI agent with no prompt overrides | Yes | No action needed | 
| 3 | Updating Default AI Agent Configurations | Unset use cases: Yes. Explicitly set: No | Explicitly pinned versions: select new version and save | 

## Important considerations
<a name="upgrade-models-important-considerations"></a>
+ **Testing:** Test model upgrades in a non-production environment before rolling out changes broadly. Use the `update-session` API to set AI agent versions for specific sessions.
+ **Infrastructure as code:** If you manage AI prompts and AI agents through CloudFormation or AWS CDK, update the resource properties in your template (for example, `ModelId` on `AWS::Wisdom::AIPrompt`) and deploy the stack. The prompt type behavior described in this topic applies the same way — unset prompt types in `AWS::Wisdom::AIAgent` resolve from system defaults at runtime.
+ **Region availability:** Model availability varies by AWS Region. Check the supported models table before selecting a model. For more information, see [Supported models for system/custom prompts](create-ai-prompts.md#cli-create-aiprompt).
+ **Session-level overrides:** AI agent versions set on sessions take precedence over assistant-level defaults, which take precedence over system defaults. If you set AI agent versions at the session level, you must also update those references.
+ **Reverting to system defaults:** To switch a use case back to the system AI agent using the admin website, navigate to *AI agent designer*, *AI agents*. In the *Default AI Agent Configurations* section, find the use case, select the system AI agent from the agent dropdown, choose the desired version or *Latest*, and choose *Save*. Using the CLI, run `list-ai-agents --origin SYSTEM` to find the system AI agent ID for the use case type, then set it using `update-assistant-ai-agent`.