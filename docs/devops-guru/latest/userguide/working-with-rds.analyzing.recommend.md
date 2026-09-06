

# Responding to recommendations
<a name="working-with-rds.analyzing.recommend"></a>

Recommendations are the most important part of the insight. In this stage of the analysis, you act to resolve the performance issue. Typically, you take the following steps:

1. Decide whether the reported performance issue indicates a real problem.

   In some cases, an issue might be expected and benign. For example, if you subject a test database to an extreme DB load, DevOps Guru for RDS reports the load as a performance anomaly. However, you don't need to remedy this anomaly because it's an expected result of your testing.

   If you determine that the issue needs a response, go to the next step.

1. Decide whether to implement the recommendation.

   In the table of recommendations, a column shows the recommended actions. For reactive insights, this is the **What we recommend** column on a reactive anomaly detail page. For proactive insights, this is the **Recommended custom change** column on a proactive insight page.

   DevOps Guru for RDS offers a list of recommendations that cover several potential problematic scenarios. After reviewing this list, determine which recommendation is more relevant to your current situation and consider applying it. If a recommendation works for your situation, go to the next step. If not, skip the remaining step and troubleshoot the issue using manual techniques.

1. Perform the recommended actions.

   DevOps Guru for RDS recommends that you do either of the following:
   + Perform a specific corrective action.

     For example, DevOps Guru for RDS might recommend that you upgrade CPU capacity, tune application pool settings, or enable the Performance Schema.
   + Investigate the cause of the issue.

     Typically, DevOps Guru for RDS recommends that you investigate specific SQL statements or wait events. For example, a recommendation might be to investigate the wait event `io/table/sql/handler`. Look up the listed wait event in [Tuning with wait events for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.html) or [Tuning with wait events for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.html) in the *Amazon Aurora User Guide*, or in [Tuning with wait events for RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.html) in the *Amazon RDS User Guide*. Then perform the recommended actions.
**Important**  
We recommend that you test any changes on a test instance before modifying a production instance. In this way, you understand the impact of the change.