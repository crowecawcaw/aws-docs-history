

AWS Well-Architected Agent is in preview release and is subject to change.

# View recommendations in AWS Well-Architected Agent
<a name="agent-view-rec"></a>

## Console
<a name="agent-view-rec-console"></a>

When you select a recommendation from the AWS WA Agent dashboard, the recommendation detail page displays the full context needed to evaluate and act on it.

The detail page includes the following sections:
+ **Overview:** A summary of what was detected and the recommended action.
+ **Details:** Metadata including priority, pillar, source (for example, Trusted Advisor), fix effort, detection date, and the number of affected resources.
+ **Insights:** Explains why this recommendation was generated. Includes a plain-language insight statement and the signals detected in your environment that triggered it. Signals reference specific resource ARNs and configuration states.
+ **Impact:** The pillar-specific impact of acting on this recommendation, including cross-pillar impacts and trade-offs. For example, a cost optimization recommendation may also improve performance while maintaining security. Impacts include quantified estimates where available (for example, "Up to 99% KMS cost reduction").
+ **Recommended fix:** A high-level summary of the remediation steps before you enter the guided workflow.
+ **Affected resources:** A table listing each resource targeted by this recommendation, including the ARN, service, account, and Region. You can search and filter by service, account, or Region. Choosing a resource ARN navigates you to that resource in the AWS console (for example, selecting an S3 bucket ARN opens that bucket in the Amazon S3 console).

### Cross-pillar impacts
<a name="agent-cross-pillar-impacts"></a>

Choose **Cross-pillar impacts** to view how this recommendation positively affects other optimization pillars beyond the primary pillar. The badge shows the total number of impacts (for example, "Cross-pillar impacts (4)").

Each cross-pillar impact includes:
+ **Impact description:** What the cross-pillar benefit is and why it occurs.
+ **Pillar:** The affected pillar (Cost Optimization, Security, Resilience, or Performance).
+ **Impact category:** The severity of the positive impact (High, Medium, or Low).

For example, enabling S3 Bucket Keys for cost optimization also reduces KMS API latency (Performance, High), improves resilience against KMS rate limiting (Resilience, Medium), and simplifies encryption audit trails (Security, Medium).

### Trade-offs
<a name="agent-trade-offs"></a>

Choose **Trade-offs** to view potential risks and considerations before implementing the recommendation. The badge shows the total number of trade-offs (for example, "Trade-offs (3)").

Each trade-off includes:
+ **Trade-off:** A title describing the potential risk.
+ **Description:** A detailed explanation of the trade-off and when it applies.
+ **Mitigation strategy:** Specific guidance for reducing or eliminating the risk.
+ **Pillar:** The pillar most affected by this trade-off.
+ **Risk:** The overall risk level of this trade-off.

Review all trade-offs and their mitigation strategies before beginning remediation. Trade-offs help you make informed decisions about whether to implement a recommendation as-is, implement with mitigations, or defer the recommendation.

### Recommendation actions
<a name="agent-rec-actions"></a>

The **Actions** dropdown on the recommendation detail page provides the following options:
+ **Share recommendation:** Share the recommendation with other AWS accounts. Enter a comma-separated list of account IDs (up to 100 accounts) and select an access level:
  + **Read only:** Recipients can view the recommendation but cannot take actions on it.
  + **Read/write:** Recipients can view the recommendation and take actions such as starting remediation or marking it complete.

  Choose **Share recommendation** to share.

  After sharing, choose **Accounts recommendation shared with** to view which accounts have access. You can switch between a JSON view and a list view. To revoke access, select the account and un-share the recommendation.
+ **Mark as complete:** Mark the recommendation as implemented. The recommendation moves to your archived recommendations.
+ **Suppress recommendation:** Suppress the recommendation if it is not relevant to your environment. Suppressed recommendations are hidden from the active list and moved to the archive.
+ **Recommendation feedback:** Provide feedback to help AWS WA Agent improve the relevance and accuracy of future recommendations.

**Console**  
In the **Actions** dropdown, choose **Recommendation feedback**. Select **Useful** or **Not Useful**. You can optionally add comments explaining your feedback. Choose **Submit** to send. If you select **Not Useful**, the recommendation is suppressed after submission.

**API**  
Use the `PutAgentRecommendationFeedback` API to submit feedback programmatically:

  ```
  aws wellarchitected put-agent-recommendation-feedback \
      --profile-arn "arn:aws:wellarchitected:{{us-east-1}}:{{111122223333}}:agent-profile/{{my-profile}}" \
      --recommendation-id "{{rec-id}}" \
      --feedback-type USEFUL
  ```

  Valid values for `--feedback-type` are `USEFUL` and `NOT_USEFUL`.

## CLI
<a name="agent-view-rec-cli"></a>

To list all active recommendations for a profile:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}"
```

To list suppressed recommendations for a profile:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile}}" \
    --state CLOSED
```

To get the full details of a specific recommendation:

```
aws wellarchitected get-agent-recommendation \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}"
```

To list the individual items (affected resources) for a recommendation:

```
aws wellarchitected list-agent-recommendation-items \
    --recommendation-arn "{{arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile/recommendation/rec-id}}"
```