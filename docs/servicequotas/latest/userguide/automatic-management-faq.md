# Service Quotas Automatic Management frequently asked questions

## Notifications and monitoring

Q1: When will I receive notifications about my quota usage?

Notifications are typically delivered within an hour of reaching a threshold. You'll also receive reminder notifications once every 24 hours if the quota threshold breach remains active.

Q2: Why didn't I receive a notification even though my quota usage reached the configured thresholds?

Notifications are typically delivered within an hour of reaching a threshold. If you consistently don't receive expected notifications, contact AWS Support with details about the specific quota, Region, and timeframe for further investigation.

Q3: Can I exclude specific resources from notifications?

No, you can't configure notification exclusions at the resource level. Automatic Management operates at the quota level, not the resource level. You can only exclude notifications on a quota basis. For instructions on excluding specific quotas from notifications, see [Excluding quotas from Automatic Management](excluding-quotas.md "excluding-quotas.md").

## Auto-adjustment process

Q4: What happens when the system automatically requests a quota increase on my behalf?

When you enable **Notify and Auto-Adjust** mode, the system automatically submits a quota increase request when your usage breaches the configured threshold.

###### How auto-adjustment works

Automatic processing

Auto-adjustment submits quota increase requests without creating a support case.

Notification of results

You receive notifications about the result of auto-adjustment requests.

Manual fallback

If the request can't be processed through auto-adjustment, the request result shows as `NOT_APPROVED` and you receive a Health notification. In these cases, submit a quota increase request manually through AWS Service Quotas.

Q5: Are auto-adjust requests evaluated differently than manual Service Quotas requests?

Yes, auto-adjust requests are processed differently than manual quota increase requests. Auto-adjust requests only work for quotas that support automated processing and are submitted without creating a support case. These requests use a streamlined approval process that may have different criteria than manual requests that go through AWS Support.

If an auto-adjust request isn't approved, you can submit a manual quota increase request through the Service Quotas console or API, which may be approved even if the auto-adjust request wasn't.

Q6: Why don't I see explicit rejection reasons for auto-adjust failures?

Auto-adjust requests use an automated approval process that doesn't provide detailed rejection reasons. When an auto-adjust request fails, you receive a notification that the request was `NOT_APPROVED`, but specific rejection details aren't available.

For more information about why a quota increase wasn't approved, submit a manual quota increase request through the Service Quotas console, which provides more detailed feedback through the support case process.

Q7: Which quotas support auto-adjust?

Not all service quotas support auto-adjustment. Only quotas that support automated processing can be auto-adjusted. Auto-adjustable status doesn't guarantee approval. If an auto-adjust request fails, submit a manual quota increase request through the Service Quotas console or API.

To view which quotas are supported in your account:

1. Open the Service Quotas console.
2. Navigate to **Automatic Management**.
3. View the list of monitored quotas, which shows only the quotas that support Automatic Management in your account and Region.

## Troubleshooting

Q8: My auto-adjust request failed, but a manual request for the same quota was approved. Why?

Auto-adjust requests and manual quota increase requests use different approval processes:

- **Auto-adjust requests** use automated processing with predefined criteria and may be more restrictive.
- **Manual requests** go through AWS Support and can be reviewed by support engineers who can consider additional context and factors.

If your auto-adjust requests consistently fail, consider submitting manual quota increase requests through the Service Quotas console for those specific quotas.

Q9: How can I track auto-adjust request results?

You can monitor auto-adjust request results through several methods:

- **AWS Health Dashboard:** View notifications about auto-adjust request results.
- **Request quota increase history:** Use the `ListRequestedServiceQuotaChangeHistoryByQuota` API to view the history of quota increase requests for a specific quota.
- **Configured notification channels:** Receive notifications through email, AWS Console Mobile Application, or other configured channels.

## Need more help?

If you have additional questions or need assistance with Automatic Management, contact AWS Support or refer to the [Service Quotas documentation](../../../servicequotas.md "../../../servicequotas.md").
