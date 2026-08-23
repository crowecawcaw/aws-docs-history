# Skill evaluators

A _skill_ is a reusable `SKILL.md` instruction file that an agent loads at runtime to help with a task. Skills follow the open [Agent Skills](https://agentskills.io "https://agentskills.io") standard for skill file structure. For terminology, see [Skill](evaluations-terminology.md#skill "evaluations-terminology.md#skill").

AgentCore Evaluations provides two built-in evaluators for agents that use skills. Both are tool-level evaluators. AgentCore Evaluations emits one result per skill invocation and anchors each result to the tool call span that loaded the skill. A session with three skill invocations produces three results per evaluator.

You can use these evaluators with on-demand, batch, and online evaluations. For the exact prompt bodies, see [Skill selection accuracy](prompt-templates-builtin.md#skill-selection-accuracy "prompt-templates-builtin.md#skill-selection-accuracy") and [Skill instruction following](prompt-templates-builtin.md#skill-instruction-following "prompt-templates-builtin.md#skill-instruction-following") on the [Prompt templates](prompt-templates-builtin.md "prompt-templates-builtin.md") page.

## Builtin.SkillSelectionAccuracy

The Skill selection accuracy evaluator (`Builtin.SkillSelectionAccuracy`) judges whether the skill the agent loaded fits the task, given the catalog of available skills. It returns `Yes` (1.0) or `No` (0.0).

Placeholders the evaluator uses:

- `invoked_skill` – The name of the skill the agent loaded in this tool call.
- `available_skills` – The catalog of skills the agent could choose from at runtime. Not every framework exposes a catalog. When the catalog is not in the trace, this placeholder is empty and the evaluator judges the invoked skill against the user request and the conversation context alone.
- `user_message` – The user request in the turn that triggered the skill invocation.
- `context` – Previous turns up to the tool call being evaluated.

The evaluator runs whenever AgentCore Evaluations detects a skill invocation. It focuses on the selection decision, not on how well the agent then executed the skill.

## Builtin.SkillInstructionFollowing

The Skill instruction following evaluator (`Builtin.SkillInstructionFollowing`) judges how fully the agent followed the loaded skill’s prescribed steps. It returns `Fully Followed` (1.0), `Mostly Followed` (0.75), `Partially Followed` (0.5), `Minimally Followed` (0.25), or `Not Followed` (0.0).

Placeholders the evaluator uses:

- `invoked_skill` – The name of the skill the agent loaded in this tool call.
- `skill_content` – The full body of the loaded skill’s `SKILL.md` instructions.
- `context` – The **full session context** — every turn from session start through session end. Because the agent may carry out prescribed steps at any point after loading the skill, the judge needs the entire session, not just the turns up to the tool call.

The evaluator runs only when both the invoked skill and its `SKILL.md` body are present in the trace. The judge identifies the prescribed steps in the skill body, then, for each step, determines from the conversation record whether the step was fully carried out, partially carried out, or skipped, and produces an overall rating consistent with that per-step breakdown.

## Framework support

AgentCore Evaluations detects skill invocations from two kinds of trace signals: a filesystem read of a `SKILL.md` file, and a framework’s native skill-loading tool. The filesystem-read signal works for any framework. The native-tool signal applies to the specific frameworks in the second row of the following table.

|                                                      |                                                                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Detection method                                     | Frameworks                                                                                       |
| `SKILL.md` file read (universal)                     | LlamaIndex, OpenAI Agents, and any agent that reads `SKILL.md` through a generic file-read tool. |
| Native skill-loading tool (in addition to file read) | Strands Agents, LangGraph Deep Agents, Google ADK, Claude Agent SDK.                             |

For the file-read path, AgentCore Evaluations matches a tool call as a skill load when its parameters contain a path ending in `/SKILL.md` and the tool result body is a well-formed `SKILL.md` file (frontmatter with `name` and `description` fields, followed by an instructions body).

An available-skills catalog is emitted natively by Strands Agents, LangGraph Deep Agents, and Google ADK. Claude Agent SDK and file-read agents do not emit a catalog. `Builtin.SkillSelectionAccuracy` still runs on those agents, with an empty `available_skills` placeholder.

For general instrumentation setup and per-framework scope names, see [Supported agent frameworks](supported-frameworks.md "supported-frameworks.md").

## Skipping behavior

AgentCore Evaluations classifies a tool call as a skill invocation when the trace exposes `invoked_skill` or `skill_content` for that call. If neither signal is present, AgentCore Evaluations skips both skill evaluators for that call and emits no result. If your agent doesn’t load any skills, both evaluators produce zero results for the session — this is expected, not an error.

If your agent does load skills but the evaluators still return no results, run the diagnostic skill in [Diagnostic skill source](diagnose-evaluation-skill-source.md "diagnose-evaluation-skill-source.md") to confirm the traces carry the expected signals.

## Skill placeholders for custom evaluators

You can write a custom TOOL\_CALL evaluator that reasons about the skills an agent loaded. The skill placeholders described above (`invoked_skill`, `skill_content`, `available_skills`, `user_message`) are available to any custom TOOL\_CALL evaluator alongside the standard tool-level placeholders (`context`, `available_tools`, `tool_turn`). Session-level and trace-level custom evaluators cannot use these placeholders.

How AgentCore Evaluations behaves depends on which skill placeholders the custom evaluator references:

- An evaluator that references `invoked_skill` behaves like `Builtin.SkillSelectionAccuracy`: it runs only on skill-invocation tool calls, and `{context}` renders the standard pre-call snapshot.
- An evaluator that references `skill_content` behaves like `Builtin.SkillInstructionFollowing`: it runs only on skill-invocation tool calls whose `SKILL.md` body is available, and `{context}` renders the **full session context** — every turn from session start through session end. This differs from the standard tool-level `context`.

In either case, AgentCore Evaluations emits one result per skill invocation. For custom-evaluator authoring, see [Create evaluator](create-evaluator.md "create-evaluator.md").
