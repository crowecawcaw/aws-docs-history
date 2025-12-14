# DevOps Agent Incident Response

All investigations that AWS DevOps Agent performs are listed in the Incident Prevention tab of your DevOps Agent web apps. Click on an investigation from the list to view an agent activity timeline, root cause analyses, and generated mitigation plans. You can also chat with your DevOps Agent to understand what it has done and steer its investigation plan. And, if you ever want to bring in an AWS support expert to help with investigation, you can do that too!

## Investigation timeline

AWS DevOps Agent will summarize and share its actions and findings in the **Investigation Timeline** tab. Use this view to understand which hypotheses the agent investigated and view its findings. The following is a list of the types of updates you will find in the investigation timeline:

- **Planning:** Agent defines approach, creates plans, or sets up analysis tasks.
- **Fetching data**: Agent gathers data, discovers resources, or fetches information (for example, tool use, results, and activities).
- **Observations:** Agent analyzes data and identifies patterns or insights from signals.
- **Findings:** Agent draws conclusions from the analysis.
- **Root cause:** The main finding that explains why issues occurred.
- **User request:** User expands or modifies the investigation.
- **Update:** Agent response that shows thinking.

## Root cause

Once your DevOps Agent completes its investigation and determines a likely root cause, it will publish a root cause summary under the Root Cause tab, containing an overview of the investigated incident, root cause, key observations supporting the root cause analysis, and any investigation gaps it encountered. Investigation gaps are a list of things the agent wanted to introspect during its investigation but was unable to do so because it lacked necessary connectivity or permissions. Use reported investigations gaps, which will be consolidated and displayed in the Investigation Gaps table in AWS console view of the related DevOps Agent Space.

###### Note

If you use chat to restart and refocus and investigation, your agent will create a new root cause version. You can switch between versions from the version picker in the Root Cause tab.

## Mitigation plans

Once your DevOps Agent has determined a likely root cause it will offer to generate a mitigation plan. Click on the “Generate mitigation plan” and the agent will generate a plan to mitigate the investigated incident. Mitigation plans will include the following steps:

1. Prepare
2. Pre-Validate
3. Apply
4. Post-Validate steps.

Each step may contain one or more suggested actions, and each suggested action may contain commands that you can use to inform changes in infrastructure-as-code templates that you may use to make configuration changes. Where appropriate, your DevOps Agent will also provide “agent-ready specs” that you can use with coding agents you may use (e.g. Kiro).

### Example mitigation scenarios:

- **System changes:** If an incident is caused by Amazon DynamoDB getting throttled due to high latency from inefficient use, AWS DevOps Agent may recommend rolling back the change as an immediate mitigation.
- **System changes:** If an incident is caused by Amazon SNS subscription errors due to filter policy mismatch, AWS DevOps Agent may recommend changing the filter policy as an immediate mitigation.
- **Input anomalies:** If an incident is caused by AWS Lambda throttling on notifications due to high traffic exceeding limits, AWS DevOps Agent may recommend increasing concurrency limits as an immediate mitigation.
- **Input Anomalies:** If an incident is caused by Amazon SNS message publish failures due to message size issues, AWS DevOps Agent may recommend adding validation to Amazon SNS message publishing as an immediate mitigation.
- **Resource Limits**: If an incident is caused by API throttling due to exceeded rate limits, AWS DevOps Agent may recommend raising rate/burst limits as an immediate mitigation.
- **Resource Limits:** If an incident is caused by Amazon DynamoDB throttling due to exceeded write capacity, AWS DevOps Agent may recommend increasing write capacity as an immediate mitigation.
- **Component Failures:** If an incident is caused by cold start latency due to performance degradation, AWS DevOps Agent may recommend increasing provisioned concurrency as an immediate mitigation.
- **Dependency Issues:** If an incident is caused by Amazon S3 access denied due to restrictive bucket policy, AWS DevOps Agent may recommend updating the bucket policy as an immediate mitigation.
- **Dependency Issues:** If an incident is caused by AWS SQS permission failure due to policy denies, AWS DevOps Agent may recommend restoring AWS SQS permissions as an immediate mitigation.

## Chat and investigation steering

The investigation details page includes a chat component. You can use chat to ask your DevOps Agent follow up questions about the investigation. You can also steer the agent’s investigation plan by asking it to restart and refocus its investigation.

### Example chat scenarios:

- Steering investigation - “Actually, the errors in the application logs are a red herring. Can the investigation focus on the service logs and the faults logged instead”
- Resume Stopped Investigation - "Can we investigate this issue further? I see that the logs you checked earlier are not related to the problem"
- User defined time limits - "Only check the logs for last 2 hours, not the full day"
- User defined resource boundaries - "Check only the ECS cluster and its configuration to know if that caused the alarm"
- Recommendations - Next steps suggestion - "The metrics show a spike in errors at 3 PM"
- Context Preservation - "Check the logs again for the 2nd alarm you were looking at"
- Investigation History - "I have fixed the bug that caused the faults in the earlier investigation. Can you re-check if the faults are still happening?"

## Asking for human support

If needed, you can create an AWS Support case directly from an investigation, giving AWS Support experts immediate context for faster resolution. Creating a support case from the investigation details page will automatically open a “chat with AWS support” component in your DevOps Agent Space web app.
