

# Security best practices for CloudWatch Omni
<a name="omni-security-best-practices-for-cloudwatch-omni"></a>

CloudWatch Omni provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and do not represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

**Preventative controls**

**Use temporary credentials for telemetry ingestion.** Prefer Signature Version 4 with temporary role credentials over long-lived access keys. Never embed credentials in source code or in client applications. Store any secrets in a secrets manager and rotate them regularly.

**Prefer role credentials over bearer tokens.** For metrics and logs, telemetry ingestion supports both Signature Version 4 with an IAM role and a long-lived bearer token, which is an IAM user service-specific credential. Prefer the role path. If you use a bearer token, scope it so that it can only send telemetry, store it in a secrets manager, and rotate it regularly. Traces have no bearer-token path (the X-Ray OTLP endpoint accepts Signature Version 4 only), so a client that sends traces must sign, and long-lived credentials are not an option there. See [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md).

**Apply least privilege and keep the administrator group small.** Grant each member the lowest permission level that lets them do their job. Keep the set of space administrators small, and review access periodically.

**Restrict roles that call CloudWatch Omni outside the console.** When a member works in a space, CloudWatch Omni issues credentials for that space and the member's access is limited to what their grants allow. When a principal calls with its own IAM credentials (an automation role, a build pipeline, or an SDK client), a missing grant does not deny the request. The request is authorized by that principal's IAM policy instead. Grant each such role only the actions it needs, and do not rely on space grants to constrain it. See [Identity and access management for CloudWatch Omni](omni-identity-and-access-management-for-cloudwatch-omni.md).

**Require a grant on roles you create for programmatic access.** To make a role's CloudWatch Omni permissions effective only when the caller has a grant in the space, add the condition `"cloudwatch:HasAccessGrant": "true"` to the role's policy. Keep the setup and administration actions in a separate statement without the condition, because those operations are authorized by IAM alone.

**Use a Custom grant when you need an exact set of actions.** Adding action scopes to a grant on one of the tiered permission levels narrows only the actions you name; every other action that the level allows remains available. If your intent is to allow an exact set of actions and nothing else, use a Custom grant, which is an allowlist. See [Custom grant actions](omni-custom-grant-actions.md).

**Redact sensitive content at capture time.** CloudWatch Omni does not automatically detect or redact personally identifiable information. Redacting before content leaves your application process is the only layer that guarantees data never leaves your application. For the mechanisms available at each point in the pipeline, see [Protect sensitive data](omni-data-protection.md).

**Choose your judge model with your compliance constraints in mind.** Restrict which telemetry you evaluate and choose the judge model according to where trace content is allowed to flow. For what a judge model receives, see [Protect sensitive data](omni-data-protection.md). For cross-Region inference, see [Cross-Region inference in CloudWatch Omni](omni-cross-region-inference-in-cloudwatch-omni.md).

**Constrain access at the dataset and export layer, not only with query filters.** Data scopes do not extend to dataset creation and export, to AI-assisted summaries, or to prompt playground runs. A member who is restricted from a field in queries could still reach that content by building a dataset or running an AI-assisted summary over the underlying traces. Grant dataset, evaluation, export, and AI-feature permissions with this in mind.

**Do not rely on data scopes for metrics.** A data scope filters log and trace rows. It does not filter metrics. If a member should not see a metric, do not grant them the metric-read actions.

**Review member data scopes when you deploy new agents.** A data scope is an inclusion rule: it lists the values a member is allowed to see, so a newly deployed agent is not visible to a scoped member until you add it to their scope. Review data scopes whenever you deploy a new agent, so that members who need the new agent can see it.

**Verify data scope changes.** Saving an edit replaces the member's previous scope rather than adding to it. After you change a member's data scope, have the member run a query to confirm the result.

**Review AI-proposed instrumentation changes.** Treat AI-generated instrumentation diffs like any other code change, and review them before you apply them.

**Control local content exposure.** Local `.omni/` files are plaintext, and the local MCP server is unauthenticated. The tooling can share local trace content with third-party AI assistants, so restrict which assistants you connect, and keep raw trace files out of source control. See [Configuration and vulnerability analysis in CloudWatch Omni](omni-configuration-and-vulnerability-analysis-in-cloudwatch.md).

**Detective controls**

**Audit management activity with AWS CloudTrail.** Management operations are recorded in CloudTrail with the event source `cloudwatch.amazonaws.com`. Monitor critical operations and alarm on anomalies.