

# Failure analysis evaluator
<a name="builtin-failure-analysis"></a>

The failure analysis evaluator (`Builtin.FailureAnalysis`) tells you what went wrong in your agent sessions, where it happened, and why. It finds each failure, locates it at a span, determines the root cause, and recommends what to change. It then groups similar failures across sessions into *failure insights*, so that you can fix patterns instead of individual sessions.

**Note**  
The failure analysis evaluator is one of the [Insight evaluators](insight-evaluators.md). Currently, only the batch evaluation APIs support it. For how to run it, see [Insights in batch evaluation](batch-evaluations-insights.md).

## How it works
<a name="builtin-failure-analysis-how-it-works"></a>

The evaluator works in three steps:

1.  **Detect:** The evaluator analyzes every span in each session and records a finding for each span where a failure occurred.

1.  **Find the cause:** For each session with failures, the evaluator analyzes the full session to determine why each failure occurred. It considers the system prompt, the tool definitions, and the tool inputs and outputs. The cause can be in an earlier span than the failure.

1.  **Group:** The service groups similar failures from all sessions into insights, and similar causes within each insight into root causes.

The evaluator reads the spans of your sessions from your CloudWatch Logs data source. It supports the same agent frameworks and instrumentation as the other built-in evaluators. For more information, see [Supported agent frameworks](supported-frameworks.md). You specify only the evaluator ID. As with other built-in evaluators, you cannot modify its model or prompt.

## Failure insights
<a name="builtin-failure-analysis-results"></a>

When you run the evaluator in a batch evaluation, the service returns failure insights in the `insightResults` field of the `GetBatchEvaluation` response. The following example shows one failure insight in a readable form.

```
Failure insight: Tool calls fail because of permission and quota errors
  Affects 3 sessions
  Tool calls that change the state of a service fail because the caller
  lacks permissions or because a quota is exceeded.

  Root cause: Constraints are not visible to the agent before it acts
    Affects 2 sessions
    Explanation: The agent calls tools without checking quotas or
      permissions first, so the call fails and the request is not completed.
    Suggested fix: Update the tools to return current limits and permissions,
      and update the system prompt to check them before it changes a resource.

    Sample session: session-0001
      Finding at span 1a2b3c4d5e6f7a8b
        Category: execution-error-rate-limiting (confidence 0.9)
        The scale_service tool call returned an error because the requested
        replica count exceeded the quota.
```

A failure insight has the following parts:
+  **Failure insight:** A failure pattern that affects one or more sessions, with a name, a description, and the number of sessions that it affects. An insight groups failures by what happened, not by category, so it can include failures of several categories. In the response, the `type` of the insight is `FAILURE`.
+  **Root cause:** The reason behind the pattern. The explanation describes what fails, why, and the impact. The suggested fix describes what to change. Most suggested fixes target the system prompt or the tool descriptions of your agent. Some point to the tool implementation, an API, or the infrastructure. The explanation and the suggested fix cover all of the failures in the group, so they are general and are not tied to one session.
+  **Sample session and finding:** Examples that show the root cause. A finding locates one failure at a span. It includes the span ID, so that you can find the span in your traces, the failure category, a description of what happened, and a confidence value between 0 and 1. The findings of a sample session are ordered with the highest confidence first. The service does not filter findings by confidence.

When no session has failures, the evaluator returns no insights. For the response format and a full example in JSON, see [insightResults fields](batch-evaluations-insights.md#batch-evaluations-insights-fields).

**Note**  
The service generates the insights, root causes, and their names, so the grouping can vary between runs over the same sessions. The number of insights, their names, and their boundaries can change. Names are display labels, not stable identifiers, so do not use them to track an insight across runs. An insight can come from a single session.

### Act on the results
<a name="builtin-failure-analysis-results-act"></a>

To work through the failure insights, follow these steps:

1.  **Start with the largest insights:** Sort the insights by the number of affected sessions to find the patterns that matter most.

1.  **Read the root causes:** The explanation tells you why the failures occur, and the suggested fix tells you what to change.

1.  **Check the findings:** Open the sample sessions and use the span IDs to confirm the failures in your traces.

1.  **Apply the fix and run again:** Update your system prompt or tools, then run the evaluator on new sessions to check whether the pattern is gone.

## Session results
<a name="builtin-failure-analysis-results-session"></a>

Each session also receives one result, which the service writes to CloudWatch Logs and metrics like the result of any session-level evaluator. The result has the following values:
+  **Score:** `1.0` when the evaluator found failures in the session, and `0.0` when it found none.
+  **Label:** `Failures Found` or `No Failures Found`.
+  **Explanation:** A summary of the failures in the session, or `No failures detected in this session.` for a session with no failures.

**Note**  
A higher score is worse for this evaluator. The average score is the share of evaluated sessions that had failures. For example, an average score of `0.2` means that 20 percent of the sessions had failures.

## Failure categories
<a name="builtin-failure-analysis-categories"></a>

The evaluator assigns each finding to one of the following groups of failure categories. If a failure does not fit a category, the evaluator reports the category `other`.
+  **Execution errors:** Authentication errors, resource not found, service errors, rate limiting, timeouts, resource exhaustion, and tool schema or formatting errors.
+  **Task and instruction errors:** The agent does not follow its instructions or does not identify the problem correctly.
+  **Incorrect actions:** The agent chooses the wrong tool, retrieves poor information, or asks for clarification or information that it does not need.
+  **Context handling errors:** The agent loses or misuses the context of the conversation.
+  **Hallucination:** The agent invents capabilities, parameters, history, or tool outputs, or misunderstands how to use a tool.
+  **Repetitive behavior:** The agent repeats tool calls, requests, or steps without making progress.
+  **Orchestration and reasoning errors:** The reasoning and the actions of the agent do not match, the agent deviates from the goal, or it ends the task too early.
+  **Nonsensical model output:** The model returns output that is malformed or has no meaning.
+  **Configuration mismatch:** A tool definition does not match the behavior of the tool.
+  **Coding-specific failures:** Unhandled edge cases and dependency issues in coding tasks.

## Use with other evaluators
<a name="builtin-failure-analysis-pairing"></a>

You can run the failure analysis evaluator alone or together with other evaluators. Because it reports failures rather than quality scores, it works best next to an evaluator that measures outcomes. For example, run `Builtin.GoalSuccessRate` and `Builtin.FailureAnalysis` together:
+  `Builtin.GoalSuccessRate` tells you how often the agent achieved the goal of the user. A higher score is better.
+  `Builtin.FailureAnalysis` tells you which sessions had failures, why they happened, and what to change. A higher score is worse.

Compare the two to separate sessions that missed the goal because of a failure from sessions that reached the goal despite a failure, such as an error that the agent recovered from.

## Considerations
<a name="builtin-failure-analysis-considerations"></a>

Keep the following in mind when you use the failure analysis evaluator:
+  **Evaluator judgment:** Every result is the judgment of the evaluator, not a comparison with ground truth or expected answers. Review the findings and the suggested fixes before you act on them.
+  **Advice only:** The evaluator does not change your agent. A suggested fix is a recommendation that you apply yourself.
+  **Failures only:** The evaluator does not score quality or goal success. A session without failures receives the label `No Failures Found` and adds nothing to the insights.
+  **No history:** Each run stands alone. The evaluator does not compare runs.
+  **Sessions without spans:** A session that has no spans from supported instrumentation in the selected time range fails with the message `No spans were found for the session`.
+  **Large sessions:** The evaluator analyzes very large sessions in parts, so coverage of an extremely large session can be partial. For multi-agent sessions, it analyzes the spans of all agents in the session together.
+  **Insight generation errors:** If the service cannot generate the insights, the evaluation ends with the status `COMPLETED_WITH_ERRORS`, the `insightResults` field is not present, and the `errorDetails` field contains the message `Insight generation failed for the Builtin.FailureAnalysis evaluator.` The session results and the results of the other evaluators are still returned.