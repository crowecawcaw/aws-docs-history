# Service Quotas Automatic Management frequently asked questions

## Notifications and monitoring

Q1: When will I receive notifications about my quota usage?

After you start Automatic Management, it can take up to 24 hours for the initial opt-in to take effect and begin monitoring your quotas. Once Automatic Management is active, notifications are typically delivered within an hour of reaching a configured threshold.

Q2: How often will I receive reminder notifications?

If the quota threshold breach remains active, you'll receive reminder notifications at different frequencies based on your utilization level:

- **At or above 95% utilization:** Once every 6 hours
- **Below 95% utilization:** Once every 24 hours

Q3: Why didn't I receive a notification even though my quota usage reached the configured thresholds?

Notifications are typically delivered within an hour of reaching a threshold. If you consistently don't receive expected notifications, contact AWS Support with details about the specific quota, Region, and timeframe for further investigation.

Q4: Can I exclude specific resources from notifications?

No, you can't configure notification exclusions at the resource level. Automatic Management operates at the quota level, not the resource level. You can only exclude notifications on a quota basis. For instructions on excluding specific quotas from notifications, see [Excluding quotas from Automatic Management](excluding-quotas.md "excluding-quotas.md").

Q5: Why did I receive an APPROACHING_THRESHOLD notification instead of THRESHOLD_BREACH even though my quota reached 100% utilization?

The notification type is determined by whether the quota supports automatic adjustment, not by the utilization level:

- **APPROACHING_THRESHOLD:** Sent for quotas that support automatic adjustment. This notification type indicates that you can optimize your quota utilization or request a quota increase.
- **THRESHOLD_BREACH:** Sent for quotas that cannot be automatically adjusted. This notification type indicates that you need to optimize your quota utilization to mitigate the threshold breach.

Even if your utilization reaches 100%, you'll receive an APPROACHING_THRESHOLD notification if the quota supports automatic adjustment. For more information about notification types, see [Integrating event-driven applications with Service Quotas using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md").

## Auto-adjustment process

Q6: What happens when the system automatically requests a quota increase on my behalf?

When you enable **Notify and Auto-Adjust** mode, the system automatically submits a quota increase request when your usage breaches the configured threshold.

###### How auto-adjustment works

Automatic processing

Auto-adjustment submits quota increase requests without creating a support case.

Notification of results

You receive notifications about the result of auto-adjustment requests.

Manual fallback

If the request can't be processed through auto-adjustment, the request result shows as `NOT_APPROVED` and you receive a Health notification. In these cases, submit a quota increase request manually through AWS Service Quotas.

Q7: Are auto-adjust requests evaluated differently than manual Service Quotas requests?

Yes, auto-adjust requests are processed differently than manual quota increase requests. Auto-adjust requests only work for quotas that support automated processing and are submitted without creating a support case. These requests use a streamlined approval process that may have different criteria than manual requests that go through AWS Support.

If an auto-adjust request isn't approved, you can submit a manual quota increase request through the Service Quotas console or API, which may be approved even if the auto-adjust request wasn't.

Q8: Why don't I see explicit rejection reasons for auto-adjust failures?

Auto-adjust requests use an automated approval process that doesn't provide detailed rejection reasons. When an auto-adjust request fails, you receive a notification that the request was `NOT_APPROVED`, but specific rejection details aren't available.

For more information about why a quota increase wasn't approved, submit a manual quota increase request through the Service Quotas console, which provides more detailed feedback through the support case process.

Q9: Which quotas support auto-adjust?

Not all service quotas support auto-adjustment. Only quotas that support automated processing can be auto-adjusted. Auto-adjustable status doesn't guarantee approval. If an auto-adjust request fails, submit a manual quota increase request through the Service Quotas console or API.

To view which quotas are supported in your account:

1. Open the Service Quotas console.
2. Navigate to **Automatic Management**.
3. View the list of monitored quotas, which shows only the quotas that support Automatic Management in your account and Region.

## Troubleshooting

Q10: My auto-adjust request failed, but a manual request for the same quota was approved. Why?

Auto-adjust requests and manual quota increase requests use different approval processes:

- **Auto-adjust requests** use automated processing with predefined criteria and may be more restrictive.
- **Manual requests** go through AWS Support and can be reviewed by support engineers who can consider additional context and factors.

If your auto-adjust requests consistently fail, consider submitting manual quota increase requests through the Service Quotas console for those specific quotas.

Q11: How can I track auto-adjust request results?

You can monitor auto-adjust request results through several methods:

- **AWS Health Dashboard:** View notifications about auto-adjust request results.
- **Request quota increase history:** Use the `ListRequestedServiceQuotaChangeHistoryByQuota` API to view the history of quota increase requests for a specific quota.
- **Configured notification channels:** Receive notifications through email, AWS Console Mobile Application, or other configured channels.

## Need more help?

If you have additional questions or need assistance with Automatic Management, contact AWS Support or refer to the [Service Quotas documentation](../../../servicequotas.md "../../../servicequotas.md").
