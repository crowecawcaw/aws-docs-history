

# Step 4: Review failure mode findings and recommendations
<a name="next-gen-tutorial-review-findings"></a>

Once the assessment completes, review the results to understand the potential failure modes in your service and the recommended improvements.

**Console:**

1. Navigate to your service and choose the **Failure modes** tab.

1. Review findings sorted by severity.

1. Choose any finding to see detailed reasoning and recommendations.

**AWS CLI:**

```
aws resiliencehubv2 list-failure-mode-findings \
  --service-arn "arn:aws:resiliencehub:us-east-1:123456789012:service/api-service:def456"
```

**Understanding your findings**

Each finding tells you:
+ **What** the failure mode is (for example, "Single-AZ RDS database").
+ **Why** it matters for your architecture.
+ **How** to fix it, with recommendations that include cost and complexity considerations.
+ **Which policy** requirement it relates to.

**Taking action**

For each finding, you can:
+ **Reason** – Think about the failure mode in detail and reason about the likelihood and impact of it occurring.
+ **Fix it** – Implement the recommendation if the likelihood and impact warrant it, then re-run the assessment to verify.
+ **Mark as irrelevant** – Suppress the finding if it does not apply to your use case. Suppressed findings remain suppressed across future assessments.
+ **Prioritize** – Use severity to decide what to address first.