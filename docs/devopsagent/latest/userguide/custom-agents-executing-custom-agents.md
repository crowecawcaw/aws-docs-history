

# Executing custom agents
<a name="custom-agents-executing-custom-agents"></a>

You can execute a custom agent on demand or configure triggers to run it automatically.

## Running a custom agent on demand
<a name="running-a-custom-agent-on-demand"></a>

You can run a custom agent immediately from the agent detail page or through Chat.

**To run a custom agent from the detail page:**

1. Navigate to the **Agents** page in your DevOps Agent web app.

1. Choose the custom agent you want to run.

1. Choose **Run Now** to execute the agent with its configured instructions.

To provide additional context for a specific run, choose the dropdown arrow next to **Run Now**, enter a prompt describing what the agent should focus on in this invocation, and choose **Run with prompt**. The prompt is passed to the agent as additional context alongside its system prompt.

After the run starts, the new invocation appears in the **History** tab with a status of "Pending start". Choose the invocation to view its trajectory in real time.

**To run a custom agent using Chat:**

Ask Chat to run the agent by name. For example:

```
Run my weekly-investigation-report agent.
```

```
Run certificate-checker and focus on certificates expiring in the next 7 days.
```

When you provide additional context in the chat message, Chat passes it as the prompt for that run. If you don't provide additional context, the agent runs with its configured system prompt only.

A custom agent can only run one invocation at a time. If the agent is already running, you must wait for the current invocation to complete, time out, or be canceled before starting another.

## Configuring triggers
<a name="configuring-triggers"></a>

Triggers run a custom agent automatically based on defined conditions. AWS DevOps Agent supports two types of triggers:
+ **Schedule triggers** – Execute the agent at recurring intervals using EventBridge-compatible cron or rate expressions.
+ **Event triggers** – Execute the agent when a webhook event arrives from a connected integration, passing the event payload as context.

Both kinds of trigger are created from the **Triggers** tab of the custom agent. To open it, navigate to the **Agents** page in your DevOps Agent web app, choose the custom agent, and then choose the **Triggers** tab.

### Creating a schedule trigger
<a name="creating-a-schedule-trigger"></a>

Schedule expressions use EventBridge-compatible cron or rate syntax. The expression must be one of the following formats:
+ **Rate expression** – Runs at a fixed interval. Format: `rate(value unit)`. Examples:
  + `rate(1 hour)` – Every hour
  + `rate(30 minutes)` – Every 30 minutes
  + `rate(7 days)` – Every 7 days
+ **Cron expression** – Runs on a specific schedule. Format: `cron(minutes hours day-of-month month day-of-week year)`. Examples:
  + `cron(0 9 ? * MON-FRI *)` – Every weekday at 9:00 AM UTC
  + `cron(0 0 1 * ? *)` – First day of every month at midnight UTC
  + `cron(0 */6 ? * * *)` – Every 6 hours

For cron expressions, exactly one of day-of-month or day-of-week must be `?` (question mark). For more information about schedule expression syntax, see [Schedule types](https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html) in the *Amazon EventBridge Scheduler User Guide*.

**To create a schedule trigger:**

1. Choose the **\+** (create) button.

1. For **Trigger type**, choose **Schedule**.

1. Enter a schedule expression. A green confirmation message appears when the expression is valid.

1. (Optional) To provide additional context for each scheduled run, enter a prompt in the **User prompt (optional)** field. The prompt is passed to the agent alongside its system prompt.

1. Choose **Create**.

After creation, the trigger appears in the list showing its expression, creation date, and next scheduled run time.

### Creating an event trigger
<a name="creating-an-event-trigger"></a>

An event trigger runs the custom agent when a webhook event arrives from a connected integration. The event payload is passed to the agent as context for that run.

**Prerequisites:**

Before creating an event trigger, you must have a connected integration with an active webhook in your agent space. Any integration with an active webhook can serve as an event source. For more information about setting up integrations, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).

**To create an event trigger:**

1. Choose the **\+** (create) button.

1. For **Trigger type**, choose **Event**.

1. For **Event source**, choose the integration whose webhook events should run the agent. Only integrations with an active webhook are listed.

1. (Optional) For **Filter expression**, enter a JMESPath expression to filter and optionally transform the event payload.

1. Choose **Create**.

If no event sources are listed, either no webhook-enabled integration exists in the agent space, or your role is missing the `ListAssociations` and `ListWebhooks` permissions.

**Filter expressions:**

You can optionally specify a JMESPath filter expression to control which events start the agent and what context the agent receives. Filter expressions are evaluated against the raw event payload root.
+ **Syntax** – [JMESPath specification](https://jmespath.org/specification.html)
+ **Maximum length** – 4,096 characters
+ **Validation** – Invalid expressions are rejected when you create the trigger

The filter expression acts as both a condition and, optionally, a projection:
+ When the result is not `null`, `false`, an empty string, an empty array, or an empty object, the trigger runs.
+ When the result is the boolean `true` (for example, a predicate like `severity == 'critical'`), the agent receives the raw event payload as context.
+ When the result is any other truthy value (for example, a projection like `{sev: severity}`), the agent receives the projected result as context.

AWS DevOps Agent truncates this context at 10,000 characters.

If you leave the filter expression empty, the agent runs on every event from that source and receives the raw event payload as context.

**Note**  
** A projection that evaluates to an empty object or empty array counts as no match, and the agent does not run. To pass a possibly-empty value through, wrap it in an object literal. For example, `{payload: details}`.

**Example filter expressions:**
+ `severity == 'critical'` – Predicate: runs the agent only when severity equals critical, passing the raw event payload as context.
+ `{sev: severity}` – Projection: runs the agent on every event, passing an object containing only the severity field as context. Because a multiselect hash always includes its keys, the result is never empty and does not filter.

Because payload shape differs for each source, the available fields depend on the integration. When an event arrives but a trigger does not run, AWS DevOps Agent emits a notice describing why. For example, the notice might state that the filter expression matched nothing. The notice also lists the top-level fields present in that payload. For more information, see [Vended Logs and Metrics](configuring-integrations-and-knowledge-vended-logs-and-metrics.md).

### Creating triggers programmatically
<a name="creating-triggers-programmatically"></a>

You can also create triggers programmatically using the AWS SDKs. Call the `devops-agent` client's `CreateTrigger` operation, which requires the `aidevops:CreateTrigger` permission. Set the trigger type to `TIME_BASED` and supply a schedule condition containing the schedule expression and optional user prompt.

Alternatively, you can model schedule-based triggers as `AWS::DevOpsAgent::Trigger` resources in AWS CloudFormation. A trigger references the custom agent it runs, so create the agent first. For more information about the `AWS::DevOpsAgent::Trigger` resource type, see [Managing assets](about-aws-devops-agent-managing-assets.md).

## Managing triggers
<a name="managing-triggers"></a>

The **Triggers** tab displays all triggers configured for the custom agent. A schedule trigger shows its schedule expression. An event trigger shows its event source and, if set, its filter expression. Both types show the creation date.

If the source integration or its webhook is removed, an event trigger remains listed but shows that the source is no longer available, and it does not run.

**Pausing a trigger:**

To temporarily stop a trigger from invoking the agent without deleting it, turn off the toggle switch next to the trigger. The trigger status changes to Paused and no longer runs until re-enabled. Turn the toggle back on to resume.

**Deleting a trigger:**

To permanently remove a trigger, choose the delete icon (trash can) next to the trigger you want to remove. Confirm the deletion in the dialog that appears. Deleted triggers cannot be recovered.

## Canceling an invocation
<a name="canceling-an-invocation"></a>

You can cancel a running invocation from the invocation trajectory view or through Chat.

**To cancel a running invocation from the trajectory view:**

1. From the **History** tab, choose the running invocation.

1. Choose **Cancel** at the top of the trajectory view.

**To cancel a running invocation using Chat:**

```
Cancel the running invocation of weekly-health-report.
```

The invocation status changes to "Canceled". Any work completed before cancellation is preserved in the trajectory. Tool calls that were in progress when the cancellation occurred may still complete.

## Tool call results
<a name="tool-call-results"></a>

During invocation, the custom agent invokes MCP tools to gather data, perform actions, and produce outputs. Each tool call and its result are recorded in the invocation trajectory.

Tool call results provide transparency into what the agent did during invocation:
+ **Successful tool calls** – The tool returned data that the agent uses to continue its work. For example, `query_cloudwatch_logs` returns log entries, or `use_aws` returns API responses.
+ **Failed tool calls** – The tool returned an error. The agent may retry, try an alternative approach, or report the failure in its output.

You can inspect individual tool calls and their results in the invocation trajectory to understand the agent's behavior, verify it accessed the correct resources, and troubleshoot unexpected results. For more information about viewing trajectories, see [Viewing an invocation trajectory](custom-agents-managing-custom-agents.md).