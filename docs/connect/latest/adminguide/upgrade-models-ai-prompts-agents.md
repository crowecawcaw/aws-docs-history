# Upgrade models for AI prompts and AI agents

When you customize AI prompts or AI agents in Amazon Connect, the model associated with each
AI prompt determines which large language model (LLM) processes the instructions. Over time, newer
and more capable models become available. This topic describes how to upgrade models across a few
common scenarios.

- You have a custom AI agent with one or more custom AI prompts using a deprecated model
- You have a custom AI agent with no prompt overrides
- You are using older versions of System AI Agents.

## Prerequisites

Before upgrading models, make sure you have the following:

- An Amazon Connect instance with AI agent designer enabled.
- An admin account, or an account with AI agent designer permissions in its security profile.
- Familiarity with [AI prompts](create-ai-prompts.md "create-ai-prompts.md"),
  [AI agents](create-ai-agents.md "create-ai-agents.md"), and
  [default system AI prompts and agents](default-ai-system.md "default-ai-system.md").

## When to upgrade

Amazon Connect notifies you when a model is scheduled for deprecation. Amazon Connect
automatically redirects LLM inference to a supported model after any model passes its
deprecation date, so there is no service disruption. However, upgrading manually before the
deprecation date lets you choose the replacement model and test it in your environment. Use
the following steps to determine which scenarios apply to you.

**Step 1: Check for custom AI agents.** In the admin website,
navigate to _AI agent designer_, _AI agents_. Look at
the _Type_ column. System agents display _- System_
after the type name (for example, "Answer Recommendation - System"). Agents without this
suffix are custom agents you created.

- If you have a custom AI agent with one or more custom AI prompts assigned to it
  → Scenario 1 (if you only overrode some prompt types, the unset prompts auto-upgrade;
  you only need to upgrade the custom prompts)
- If you have a custom AI agent with no prompt overrides → Scenario 2 (prompts
  auto-upgrade, no action needed)
- If you don't have any custom AI agents, skip to Step 2.

**Step 2: Check the Default AI Agent Configurations.** On the
same _AI agents_ page, scroll to the _Default AI Agent
Configurations_ section. If any use case is pinned to a specific version (not set
to _Latest_), you can update it → Scenario 3. This applies to all
customers, even if you have no custom agents.

## How model resolution works

When configuring an individual AI agent, you have the option to let Connect choose which
LLM to use for each prompt, choose the model you want each prompt to use, or pick a
combination of the two options.

- Each AI prompt has a model property that specifies which LLM to use.
- Each AI agent references one or more AI prompt versions. A version is an immutable
  snapshot of the prompt, including its model selection.
- When you create a custom AI agent and override only some of the prompts associated
  to the agent, the remaining types are filled from the system defaults at runtime.
  Prompts you explicitly set are pinned to the version you chose. Prompts filled by the
  system use the latest system default. This per-prompt-type resolution applies to
  non-agentic AI agent types such as Answer Recommendation, Manual Search, and
  Non-Agentic Self Service.
- Available models depend on the AWS Region of your Amazon Connect instance. For a
  list of supported models per Region, see
  [Supported models for system/custom prompts](create-ai-prompts.md#cli-create-aiprompt "create-ai-prompts.md#cli-create-aiprompt").

## Scenario 1: Custom AI agent with custom AI prompts

In this scenario, you created a custom AI agent and assigned one or more custom AI prompts
to it. The custom prompts are pinned to the model you selected when you published them.

Custom prompts do not automatically receive model upgrades. You must manually update the
model, publish a new prompt version, and update the AI agent.

### If you only overrode some prompt types

Some AI agent types support multiple prompt types. For example, an Answer recommendation
AI agent supports three prompt types: intent labeling generation, query reformulation, and
answer generation. If you set only some of these to custom prompts and left the rest unset,
the following applies:

- Prompt types you explicitly set (through the admin website or CLI) are pinned to the
  specific prompt version you chose. They do not change unless you update them. Follow
  the upgrade steps below for each custom prompt.
- Prompt types you left unset are not stored in the AI agent configuration. At
  runtime, Amazon Connect resolves them from the current system defaults. These types
  always use the latest system prompt versions, including any model upgrades. No action
  is required for unset prompt types.

### Upgrade using the admin website

**Step 1: Create a new prompt version with the updated model**

1. Log in to the Amazon Connect admin website.
2. In the navigation menu, choose _AI agent designer_,
   _AI prompts_.
3. From the _Prompts_ list, select the custom AI prompt you
   want to upgrade.
4. Choose _Edit in AI Prompt Builder_ (top right).
5. The top-right dropdown shows _Latest: Draft_. This is the
   working copy you will modify.
6. In the _Models_ section, use the dropdown to select the
   new model.
7. Choose _Publish_. This creates a new version of the prompt
   with the new model.
8. Scroll down to the _Versions_ section on the same page. You
   can confirm the new version has been created.
9. To verify the new version, navigate back to _AI agent designer_,
   _AI prompts_. Select the prompt from the list, then use the
   version dropdown (top right) to select the new version. The
   _Overview_ section displays the updated model ID.

**Step 2: Update the AI agent to use the new prompt version**

1. Navigate to _AI agent designer_,
   _AI agents_.
2. Choose the custom AI agent that references this prompt.
3. Choose _Edit in AI Agent Builder_ to open the Agent Builder
   page.
4. Choose _Add prompt_. A popup appears with available
   prompts.
5. Select the new prompt version, then choose _Add_. The popup
   closes and the prompt is added to the agent.
6. Choose _Publish_. This creates a new AI agent version using
   the custom prompt with the updated model.
7. Scroll down to the _Versions_ section to confirm the new AI
   agent version appears.
8. Optionally, select the latest version from the top-right dropdown. The
   _Prompts_ section displays the new prompt version.

**Step 3: Set the new AI agent version as the default**

1. Navigate to _AI agent designer_,
   _AI agents_.
2. In the _Default AI Agent Configurations_ section, find the
   use case that is using the custom AI agent and update it to the new version.
3. Choose the check mark icon (✓) to save.
4. To avoid manually updating the version each time, select
   _Latest_ from the version dropdown. This automatically uses the
   most recently published version of the AI agent.

### Upgrade using the AWS CLI

Update the AI prompt with the new model:

```
aws qconnect update-ai-prompt \
  --assistant-id `assistant-id` \
  --ai-prompt-id `custom-prompt-id` \
  --model-id `new-model-id`
```

Publish a new version of the prompt:

```
aws qconnect create-ai-prompt-version \
  --assistant-id `assistant-id` \
  --ai-prompt-id `custom-prompt-id`
```

Update the AI agent to reference the new prompt version:

```
aws qconnect update-ai-agent \
  --assistant-id `assistant-id` \
  --ai-agent-id `custom-agent-id` \
  --configuration '{
    "`agentTypeConfiguration`": {
      "`promptTypeAIPromptId`": "`custom-prompt-id`:`new-version-number`"
    }
  }'
```

Publish a new version of the AI agent:

```
aws qconnect create-ai-agent-version \
  --assistant-id `assistant-id` \
  --ai-agent-id `custom-agent-id`
```

Set the new AI agent version as the default:

```
aws qconnect update-assistant-ai-agent \
  --assistant-id `assistant-id` \
  --ai-agent-type `AGENT_TYPE` \
  --configuration '{
    "aiAgentId": "`custom-agent-id`:`new-version-number`"
  }'
```

## Scenario 2: Custom AI agent with no prompt overrides

In this scenario, you created a custom AI agent to customize settings such as locale or
knowledge base configuration, but you did not override any prompt types. All prompts are
resolved from the system defaults.

### Automatic upgrades

When Amazon Connect publishes new system AI agent and prompt versions with upgraded
models, your custom AI agent automatically picks up the latest system prompt versions.
No action is required.

This is because the unset prompt types are resolved at runtime from the current system
defaults, which always point to the most recent system prompt versions.

### Force a specific model before a system upgrade

If you want to use a newer model before Amazon Connect rolls it out as a system
default:

1. Create a custom AI prompt by copying the system prompt you want to upgrade.
2. Change the model to the desired newer model.
3. Publish the custom prompt.
4. Edit your custom AI agent and add the custom prompt to the desired type.
5. Publish the AI agent.

This converts that prompt type into a Scenario 1 configuration.

## Scenario 3: Updating Default AI Agent Configurations

The _Default AI Agent Configurations_ section on the
_AI agents_ overview page controls which AI agent version is active for
each use case (Answer Recommendation, Manual Search, Self Service).

When an Amazon Connect instance is created, each use case is automatically configured with
a specific system AI agent version. These versions are pinned — they do not auto-update when
Amazon Connect publishes new system AI agent versions or when you publish new custom AI agent
versions. You must manually select the new version.

### Upgrade using the admin website

1. Navigate to _AI agent designer_,
   _AI agents_.
2. In the _Default AI Agent Configurations_ section, find the
   use case you want to update (for example, Answer Recommendation).
3. From the version dropdown, select the new AI agent version.
4. Choose _Save_.
5. To avoid manually updating the version each time, select
   _Latest_ from the version dropdown. This automatically uses the
   most recently published version of the AI agent.

### Upgrade using the AWS CLI

```
aws qconnect update-assistant-ai-agent \
  --assistant-id `assistant-id` \
  --ai-agent-type `AGENT_TYPE` \
  --configuration '{
    "aiAgentId": "`ai-agent-id`:`new-version-number`"
  }'
```

Replace `AGENT_TYPE` with the use case type (for example,
`ANSWER_RECOMMENDATION`, `MANUAL_SEARCH`,
`SELF_SERVICE`).

## Summary

| #   | Scenario                                 | Auto-upgrades?                           | Action required                                                                                        |
| --- | ---------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1   | Custom AI agent with custom AI prompts   | Custom prompts: No. Unset prompts: Yes   | Edit prompt, change model, publish prompt, update agent, publish<br>agent. Unset prompts auto-upgrade. |
| 2   | Custom AI agent with no prompt overrides | Yes                                      | No action needed                                                                                       |
| 3   | Updating Default AI Agent Configurations | Unset use cases: Yes. Explicitly set: No | Explicitly pinned versions: select new version and save                                                |

## Important considerations

- **Testing:** Test model upgrades in a non-production
  environment before rolling out changes broadly. Use the
  `update-session` API to set AI agent versions for specific sessions.
- **Infrastructure as code:** If you manage AI prompts
  and AI agents through CloudFormation or AWS CDK, update the resource properties in your template
  (for example, `ModelId` on `AWS::Wisdom::AIPrompt`) and deploy
  the stack. The prompt type behavior described in this topic applies the same way —
  unset prompt types in `AWS::Wisdom::AIAgent` resolve from system defaults
  at runtime.
- **Region availability:** Model availability varies by
  AWS Region. Check the supported models table before selecting a model. For more
  information, see
  [Supported models for system/custom prompts](create-ai-prompts.md#cli-create-aiprompt "create-ai-prompts.md#cli-create-aiprompt").
- **Session-level overrides:** AI agent versions set on
  sessions take precedence over assistant-level defaults, which take precedence over
  system defaults. If you set AI agent versions at the session level, you must also
  update those references.
- **Reverting to system defaults:** To switch a use case
  back to the system AI agent using the admin website, navigate to _AI agent
  designer_, _AI agents_. In the _Default AI Agent
  Configurations_ section, find the use case, select the system AI agent from
  the agent dropdown, choose the desired version or _Latest_, and
  choose _Save_. Using the CLI, run
  `list-ai-agents --origin SYSTEM` to find the system AI agent ID for the
  use case type, then set it using `update-assistant-ai-agent`.
