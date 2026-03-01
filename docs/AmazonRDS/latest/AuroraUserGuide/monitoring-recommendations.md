# Recommendations from Amazon Aurora

Amazon Aurora provides automated
recommendations for database resources, such as DB instances, DB clusters,
and DB parameter groups. These recommendations provide best practice guidance by analyzing DB cluster configuration, DB instance configuration, usage, and performance
data.

Amazon RDS Performance Insights monitors specific metrics and automatically creates thresholds by analyzing what levels are
considered potentially problematic for a specified resource. When new metric values cross a
predefined threshold over a given period of time, Performance Insights generates a proactive
recommendation. This recommendation helps to prevent future database performance
impact. For example, the "Idle In Transaction" recommendation is generated for Aurora PostgreSQL instances when the sessions
connected to the database are not performing active work, but can keep database resources blocked.
To receive proactive recommendations, you must turn on Performance Insights with a paid tier retention period. For information about turning on
Performance Insights, see [Turning Performance Insights on and off for Aurora](USER_PerfInsights.md "USER_PerfInsights.md"). For information about pricing and data
retention for Performance Insights see [Pricing and data retention for Performance Insights](USER_PerfInsights.Overview.md "USER_PerfInsights.Overview.md").

DevOps Guru for RDS monitors certain metrics to detect when the metric's behavior becomes highly
unusual or anomalous. These anomalies are reported as reactive insights with
recommendations. For example, DevOps Guru for RDS might recommend you to consider increasing CPU
capacity or investigate wait events that are contributing to DB load. DevOps Guru for RDS also
provides threshold based proactive recommendations. For these recommendations, you must turn
on DevOps Guru for RDS. For information about turning on DevOps Guru for RDS, see [Turning on DevOps Guru and specifying resource coverage](devops-guru-for-rds.md#devops-guru-for-rds.configuring.coverage "devops-guru-for-rds.md#devops-guru-for-rds.configuring.coverage").

Recommendations will be in any of the following status: active, dismissed, pending, or
resolved. Resolved recommendations are available for 365 days.

You can view or dismiss the recommendations. You can apply a configuration based active
recommendation immediately, schedule it in the next maintenance window, or dismiss it. For
threshold based proactive and machine learning based reactive recommendations, you need to
review the suggested cause of the issue and then perform the recommended actions to fix the
issue.

Recommendations are supported in the following AWS Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)
  Learn to view, apply, dismiss, and modify recommendations from Amazon Aurora in the following sections.

###### Topics

- [Viewing Amazon Aurora recommendations](UserRecommendationsView.md "UserRecommendationsView.md")
- [Applying Amazon Aurora recommendations](USERRecommendationsManage.md "USERRecommendationsManage.md")
- [Dismissing Amazon Aurora recommendations](USERRecommendationsManage.md "USERRecommendationsManage.md")
- [Modifying dismissed Amazon Aurora recommendations to active recommendations](USERRecommendationsManage.md "USERRecommendationsManage.md")
- [Recommendations from Amazon Aurora reference](USERRecommendationsManage.md "USERRecommendationsManage.md")
