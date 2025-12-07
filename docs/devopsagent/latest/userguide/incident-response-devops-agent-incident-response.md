# DevOps Agent incident response

AWS DevOps Agent is your always-on, autonomous on-call engineer. It begins investigating the moment an alert comes in, whether at 2 AM or during peak hours, to quickly restore your application to optimal performance. AWS DevOps Agent autonomously triages incidents 24/7, providing root cause analysis and actions for resolution. It uses its understanding of your application resources and relationships to quickly understand dependencies and interactions.

AWS DevOps Agent streamlines incident response by automatically routing observations, findings, and mitigation steps through your preferred communication channels such as Slack, ServiceNow, and PagerDuty.

## Automated investigations

AWS DevOps Agent integrates with ticketing and alarming systems like ServiceNow to automatically launch investigations from incident tickets, accelerating incident response within your existing workflows to reduce meant time to recover (MTTR).

## Incident coordination

You can also initiate and guide investigations using interactive chat. AWS DevOps Agent acts as a member of your operations team, working directly within your collaboration tools like ServiceNow and Slack to share findings and coordinate response. When needed, create an AWS Support case directly from an investigation, giving AWS Support experts immediate context for faster resolution.

## Root cause analysis

AWS DevOps Agent integrates with observability tools, code repositories, and CI/CD pipelines to correlate and analyze telemetry, code, and deployment data sharing its explored hypotheses, observations, findings, and root cause findings. Through systematic investigations, AWS DevOps Agent identifies root cause of issues stemming from system changes, input anomalies, resource limits, component failures, and dependency issues across your entire environment.

## Detailed mitigation plans

Once AWS DevOps Agent has identified the root cause, it provides detailed mitigations plans, which include actions to resolve the incident, validate success, and revert a change if needed. AWS DevOps Agent also provides agent-ready instructions that can be implemented by another frontier agent, for example, code improvements that can be implemented by Kiro autonomous agent.

### Example use cases

Through systematic investigation of alarms stemming from **system changes, input anomalies, resource limits, component failures**, and **dependency issues** across your entire stack, AWS DevOps Agent guides DevOps teams with targeted mitigation steps, reducing mean time to recovery (MTTR) from hours to minutes.

- **System changes:** If an incident is caused by Amazon DynamoDB getting throttled due to high latency from inefficient use, AWS DevOps Agent may recommend rolling back the change as an immediate mitigation.
- **System changes:** If an incident is caused by Amazon SNS subscription errors due to filter policy mismatch, AWS DevOps Agent may recommend changing the filter policy as an immediate mitigation.
- **Input anomalies:** If an incident is caused by AWS Lambda throttling on notifications due to high traffic exceeding limits, AWS DevOps Agent may recommend increasing concurrency limits as an immediate mitigation.
- **Input anomalies:** If an incident is caused by Amazon SNS
  message publish failures due to message size issues, AWS DevOps Agent may recommend adding
  validation to Amazon SNS message publishing as an immediate mitigation.
- **Resource limits**: If an incident is caused by API throttling
  due to exceeded rate limits, AWS DevOps Agent may recommend raising rate/burst limits as an
  immediate mitigation.
- **Resource limits:** If an incident is caused by Amazon DynamoDB
  throttling due to exceeded write capacity, AWS DevOps Agent may recommend increasing write
  capacity as an immediate mitigation.
- **Component failures:** If an incident is caused by cold start
  latency due to performance degradation, AWS DevOps Agent may recommend increasing
  provisioned concurrency as an immediate mitigation.
- **Dependency issues:** If an incident is caused by Amazon S3
  access denied due to restrictive bucket policy, AWS DevOps Agent may recommend updating the
  bucket policy as an immediate mitigation.
- **Dependency issues:** If an incident is caused by AWS SQS
  permission failure due to policy denies, AWS DevOps Agent may recommend restoring AWS SQS
  permissions as an immediate mitigation.
