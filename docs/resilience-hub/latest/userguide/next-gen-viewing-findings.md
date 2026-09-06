

# Viewing failure mode findings and recommendations
<a name="next-gen-viewing-findings"></a>

After an assessment completes, review the findings and recommendations:

**To view findings (console)**

1. Navigate to your service and choose the **Assessment** tab.

1. Review findings sorted by severity.

1. Choose any finding to see detailed reasoning and recommendations.

**To list findings (CLI)**

```
aws resiliencehubv2 list-failure-mode-findings \
  --service-arn "arn:aws:resiliencehub:..."
```

Each finding includes the following information:


| Field | Description | Example | 
| --- | --- | --- | 
| Finding name | Brief description of the failure mode | "Single-AZ Amazon Relational Database Service database creates a critical single point of failure" | 
| Description | Detailed explanation of the issue | Paragraph explaining why this is a risk | 
| Reasoning | Why this matters for your specific architecture | Architecture-specific context for the finding | 
| Severity | Impact level | High, Medium, Low | 
| Failure category | Type of failure | Shared fate, Excessive load, Excessive latency, Misconfiguration and bugs, Single points of failure | 
| Policy component | Which policy requirements this relates to | Multi-AZ disaster recovery | 
| Recommendations | Suggested mitigations | See recommendations table below | 

Each recommendation includes a mitigation, observability, and testing recommendation:
+ **Mitigation** – An infrastructure or configuration change to address the failure mode.
+ **Observability** – Monitoring or alerting improvements to detect the failure mode.
+ **Testing** – A test to validate that the mitigation works as expected.

**Managing findings**

For each finding, you can reason about the failure mode in detail, implement the recommended fix, mark the finding as irrelevant if it does not apply to your use case, or use severity to prioritize what to address first.

Findings can have the following statuses:
+ **Open** – Requires attention.
+ **Resolved** – The issue has been fixed. The next assessment verifies the fix.
+ **Irrelevant** – Suppressed by the customer. The finding stays suppressed across future assessments.

**To mark a finding as resolved (CLI)**

```
aws resiliencehubv2 update-failure-mode-finding \
  --service-arn "arn:aws:resiliencehub:..." \
  --finding-id "finding-123" \
  --status "RESOLVED"
```

**To mark a finding as irrelevant (CLI)**

```
aws resiliencehubv2 update-failure-mode-finding \
  --service-arn "arn:aws:resiliencehub:..." \
  --finding-id "finding-123" \
  --status "IRRELEVANT"
```