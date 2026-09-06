

# Understanding recommended action types
<a name="recommended-action-types"></a>

Recommended actions automatically identify and prioritize the most important actions you should take related to Billing and Cost Management, regarding budgets, payments, cost optimization, cost anomalies, IAM permissions, and tax settings.

Recommended actions are categorized into three levels based on urgency, financial impact, and account relevance.

1. **Critical alerts**: These are high-priority items that could impact your account standing, such as past due payments or expired payment methods.

1. **Advisory warnings**: These are important notifications about your configured resources like budgets, tax settings, and credits that help you identify opportunities to save costs.

1. **Informational**: These are best practices and optimization opportunities to improve your cloud financial management.

The following table provides an overview of the different recommended actions, organized by severity and feature.

**Note**  
\* These action types are always visible. Additional action types require the `bcm-recommended-actions:ListRecommendedActions` permission. For more information, see [Billing and Cost Management recommended actions policies](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#allows-recommended-actions-access).




- ****Critical alerts****
  - **Feature:** PAYMENTS / **Action type:** Payments past due / **Recommended action:** Make a payment / **Example:** You have USD $603.23, EUR €50.02 past due. To avoid potential disruption in using AWS services, please make a payment.
  - **Feature:** PAYMENTS / **Action type:** Invalid payment method / **Recommended action:** Verify payment method / **Example:** Your default payment method is invalid. To avoid payment failures and potential disruption in using AWS services, please contact your bank to determine the reason and visit the payments page to verify your payment method.
  - **Feature:** PAYMENTS / **Action type:** Expired payment method / **Recommended action:** Review your payment configurations and update your default payment method. / **Example:** Your default payment method expired. To avoid failed payments for invoices and potential disruption to your AWS services, update the card information or switch to a different payment method.
  - **Feature:** IAM / **Action type:** Update permissions for recommended actions\* / **Recommended action:** Contact your administrator to add new IAM permissions for your role. / **Example:** You need a new IAM permission to view the full list of recommended actions: bcm-recommended-actions:ListRecommendedActions.

- ****Advisory warnings****
  - **Feature:** TAX\_SETTINGS / **Action type:** Fix tax registration information / **Recommended action:** Review your tax settings and update your tax registration number. / **Example:** Your tax registration ID is invalid.
  - **Feature:** TAX\_SETTINGS / **Action type:** Update tax exemption certificate / **Recommended action:** Review your tax settings and update your tax exemption certificate. / **Example:** You have 2 tax exemption certificates that are expired or expiring within 30 days.
  - **Feature:** IAM / **Action type:** Migrate to granular permissions\* / **Recommended action:** Migrate to Billing and Cost Management granular permissions. / **Example:** Migrate to the new IAM permissions to avoid losing access to future Billing and Cost Management launches.
  - **Feature:** BUDGETS / **Action type:** Review budget alerts\* / **Recommended action:** Review your budgets and alert thresholds. You can also identify cost savings opportunities by visiting Cost Optimization Hub. / **Example:** 5 of your budget alerts have exceeded their threshold.
  - **Feature:** BUDGETS / **Action type:** Review budgets exceeded\* / **Recommended action:** Review your budgets values. You can also identify cost savings opportunities by visiting Cost Optimization Hub. / **Example:** 7 of your budgets have exceeded their threshold and 2 of your budgets are forecasted to exceed their threshold.
  - **Feature:** FREE\_TIER / **Action type:** Review Free Tier usage alerts\* / **Recommended action:** Review your Free Tier usage to prevent any cost surprises. / **Example:** You have exceeded 85% of the Free Tier usage limit for 3 services.
  - **Feature:** COST\_ANOMALY\_DETECTION / **Action type:** Review anomalies\* / **Recommended action:** Review your cost anomaly monitors and associated thresholds. You can also identify cost savings opportunities by visiting Cost Optimization Hub. / **Example:** 2 cost anomalies detected in the last 90 days with a total cost impact of $1,000.
  - **Feature:** RESERVATIONS / **Action type:** Review expiring reservations\* / **Recommended action:** Review your expiring reserved instances and plan to make new purchases to optimize your workloads. / **Example:** 2 reservations expiring within 30 days.
  - **Feature:** SAVINGS\_PLANS / **Action type:** Review expiring Savings Plans\* / **Recommended action:** Review your expiring Savings Plans and add any future purchases to the queue. / **Example:** 2 Savings Plans expiring within 30 days.

- ****Informational****
  - **Feature:** PAYMENTS / **Action type:** Payments due / **Recommended action:** Make a payment. / **Example:** You have USD $603.23, EUR €50.02 due. To avoid potential disruption in using AWS services, please make a payment.
  - **Feature:** COST\_OPTIMIZATION\_HUB / **Action type:** Review savings opportunity recommendations\* / **Recommended action:** Review your savings opportunities by visiting Cost Optimization Hub. / **Example:** Save $1000.00 by following savings opportunity recommendations.
  - **Feature:** COST\_OPTIMIZATION\_HUB / **Action type:** Enable Cost Optimization Hub\* / **Recommended action:** Opt in to Cost Optimization Hub to start generating savings opportunity recommendations. / **Example:** Opt in to start generating savings opportunity recommendations.
  - **Feature:** BUDGETS / **Action type:** Create a budget\* / **Recommended action:** Create a budget to monitor your cost and usage as well as commitment coverage and utilization. / **Example:** Create a cost budget to receive alerts when your costs and usage exceed your budgeted amounts.
  - **Feature:** BUDGETS / **Action type:** Create a Savings Plans budget\* / **Recommended action:** Create a Savings Plans budget to monitor your commitment coverage and utilization. / **Example:** Create a Savings Plans budget to monitor your Savings Plans commitment coverage and utilization.
  - **Feature:** BUDGETS / **Action type:** Create a reservation budget\* / **Recommended action:** Create a reservation budget to monitor your commitment coverage and utilization. / **Example:** Create a reservation budget to monitor your reserved instance commitment coverage and utilization.
  - **Feature:** ACCOUNT / **Action type:** Add an alternate billing contact\* / **Recommended action:** Add an additional billing contact. / **Example:** Add an additional billing contact.
  - **Feature:** COST\_ANOMALY\_DETECTION / **Action type:** Create an anomaly monitor\* / **Recommended action:** Create a cost anomaly monitor to proactively identify any cost anomalies. / **Example:** Create a cost anomaly monitor to automatically detect cost anomalies.

