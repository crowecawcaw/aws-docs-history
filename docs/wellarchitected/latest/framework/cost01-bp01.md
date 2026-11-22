

# COST01-BP01 Establish cloud budgets and forecasts

 Because cloud spending changes with usage, adapt your budgeting, forecasting, and financial planning for variable, usage-based costs. Combine historical usage trends with business events to project future spend. 

 **Desired outcome:** 
+  Your forecasts combine trend-based analysis with business-driver inputs, so planned events such as launches and campaigns are reflected in expected spend. 
+  Your budgets carry defined thresholds and automated alerts that notify the right stakeholders before spend exceeds plan. 
+  You forecast at a granularity that matches your organization, such as account, environment, team, or product, not organization-wide totals alone. 
+  Your finance and technology teams share a common cost vocabulary and review forecast accuracy on a regular cadence. 

 **Common anti-patterns:** 
+  Applying fixed annual IT budgeting processes to the cloud without accounting for elastic, usage-based spend. 
+  Forecasting from historical data alone, ignoring business drivers such as marketing events, regional expansion, or product launches. 
+  Setting budgets without monitoring or alerts, so overruns are discovered only after the invoice arrives. 
+  Producing forecasts only at the organization level, with no breakdown by account, environment, or team. 
+  Leaving finance and engineering teams without a shared process or vocabulary for discussing cloud cost. 

 **Benefits of establishing this best practice:** 
+  Financial predictability improves despite the variability of cloud spend, because forecasts reflect both usage trends and planned business change. 
+  Cost overruns are caught early through threshold-based alerts rather than after the fact. 
+  Spend aligns with business objectives because forecasts are broken down to the units that own the cost. 
+  Teams that provision resources become more accountable, because cost is visible at their level of ownership. 
+  Finance and technology stakeholders make faster, data-driven decisions from a shared set of metrics. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Traditional IT budgeting sets a fixed figure tied to capital purchases and refresh cycles. Cloud spend moves with workload demand, so a flat monthly figure won't match actual usage. Budget in ranges anchored to expected usage, and revise as trends and business events change. 

 *Trend-based forecasting* extrapolates future spend from historical usage patterns. It works well for stable workloads but cannot anticipate new events. *Business driver-based forecasting* ties expected spend to the events that cause demand, such as a marketing campaign, a new region, or a feature launch. It captures planned change but requires input from business teams. Use trend-based forecasting for the baseline and driver-based forecasting to adjust for known events. 

 An organization-wide forecast hides which team, environment, or product drives changes in spend. Choose a level of granularity for your forecasting, such as organization, individual accounts, environments, products, or custom groupings tied to business units or cost centers, where someone can act on a variance. This depends on your account structure and tags, so establish a consistent cost allocation strategy first. 

 Configure alerts that fire when actual or forecasted spend approaches a threshold, so teams can investigate before the period closes. Pair budgets with anomaly detection to catch unexpected spend changes, such as a misconfigured resource or an unplanned usage spike. 

 [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) produces trend-based forecasts from historical usage and breaks down spend by service, account, tag, and cost category. [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) tracks actual and forecasted spend against thresholds and sends alerts when either approaches a limit. [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) uses machine learning to identify unusual spend and attribute it to a service or account. [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) provide the granular data for custom forecasting models and dashboards. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a shared cost vocabulary and forecast granularity:** Agree with finance and technology stakeholders on consistent cost terminology, pricing-model definitions, and the level at which you forecast (account, environment, team, or product). Confirm this granularity maps to your account structure and tagging strategy so that variances can be traced to an owner. 

1.  **Produce trend-based forecasts:** Use [AWS Cost Explorer forecasting](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) to project future spend from historical usage across the dimensions you defined. Set forecast horizons that match your planning cycles. Cost Explorer forecasts up to 18 months ahead from up to 36 months of historical usage, which covers a full fiscal year plus a planning horizon, in the console or through the GetCostForecast API. For advanced modeling, feed [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) data into a machine learning workflow. 

1.  **Add business driver-based forecasts:** Work with application, marketing, and business teams to identify the drivers that change demand, such as campaigns, launches, or resiliency and security requirements. Estimate the cost impact of each driver and combine them into a forecast that layers planned change on top of the trend baseline. 

1.  **Configure budgets with thresholds and alerts:** Create budgets in [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) at the granularity you chose, and set alerts that notify the relevant stakeholders when actual or forecasted spend approaches each threshold. 

1.  **Enable anomaly detection:** Turn on [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) to surface unexpected spend changes early, and route findings to the teams that own the affected accounts or services. 

1.  **Review forecast accuracy on a cadence:** Set a recurring review with finance, technology, and business teams to compare actuals against forecast, adjust for changing business direction, and improve the models based on where they were wrong. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST01-BP02 Implement goals and targets](cost01-bp02.md) 
+  [COST01-BP04 Keep up-to-date with new service releases](cost01-bp04.md) 

 **Related documents:** 
+  [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) 
+  [Forecasting with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html) 
+  [AWS Data Exports and Cost and Usage Report 2.0](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html) 
+  [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) 
+  [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) 
+  [Forecasting and creating what-if scenarios with AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/forecasts-and-whatifs.html) 

 **Related videos:** 
+  [AWS Budgets Tutorial: Setup Billing Alerts](https://aws.amazon.com/video/watch/3d4c8571417/) 

 **Related examples:** 
+  [Understand and build driver-based forecasting](https://aws.amazon.com/blogs/aws-cloud-financial-management/understand-and-build-driver-based-forecasting/) 
+  [How to establish and drive a forecasting culture](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-establish-and-drive-a-forecasting-culture/) 
+  [How to improve your cloud cost forecasting](https://aws.amazon.com/blogs/aws-cloud-financial-management/forecasting-blog-series-1-3-ways-to-more-effectively-forecast-cloud-spend/) 
+  [AWS Budgets dashboard from the Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/advanced/aws-budgets) 

 **Related services:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) 
+  [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) 