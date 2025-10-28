# Viewing inventory insights

When you create a watchlist for a specific product, site, risk type, and planning horizon, depending on the notifications settings, you will get notified when Insights detects an inventory risk. You will receive notifications through the web application or email. You can view the inventory risks
in _Card_ or _Table_ view. By using the _Card_ view, you can view the risks in a list format separated by when the risks will happen. For example, 0 to 7 days, 7 to 14 days, or 14+ days.

Using the _Table_ view, you can view the risks by name of the product, the impacted site name, type of risk, risk in days, the percentage deviation from the relevant threshold, start of the on-hand value,
the safety stock values you ingested under the _inv_policy_ data entity for this product/site combination, and the inventory projections.

Choose the _chat_ icon to collaborate with your peers on the inventory risk.

You can use the **Search** field to search the inventory insights page by product and site name.

Choose **Edit** on the top-right of the page to edit the inventory insights. For information on how to edit the insight watchlist page, see [Creating insight watchlist](creating-insights.md "creating-insights.md").

###### Note

AWS Supply Chain supports rebalance planning horizon for up to six weeks.

- **New Insights** – This section displays all new insights
  that AWS Supply Chain discovers after you created your Insight Watchlist. AWS Supply Chain scans for
  Inventory Risk Insights every 6 hours, and Lead Time Insights every 24 hours.
- **In Review** – This section displays all insights that
  are currently under review.
- **Resolved** – This section displays resolved
  insights.
