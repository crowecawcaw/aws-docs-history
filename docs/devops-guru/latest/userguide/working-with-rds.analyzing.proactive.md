# Viewing proactive anomalies

Within insights, you can view anomalies for Amazon RDS resources. Each proactive insight provides details about one proactive anomaly.
On a proactive insight page, you can view an insight overview, detailed metrics about the anomaly, and recommendations to prevent future issues.
To view a proactive anomaly, [go to the proactive insight page](working-with-rds.analyzing.md "working-with-rds.analyzing.md").

## Insight overview

The **Insight overview** section provides details about why the insight was created.
It displays the severity of the insight as well as a description of the anomaly and a timeframe for when the anomaly occurred.
It also lists the number of affected services and applications detected by DevOps Guru.

## Metrics

The **Metrics** section provides graphs of the anomaly. Each graph displays a threshold determined by the resource's baseline behavior,
as well as data of the metric reported from the time of the anomaly.

## Recommendations for aggregated resources

This section suggests actions that you can take to mitigate the reported issues before they become a bigger problem.
Actions that you can take are presented in the **Recommended custom change** column.
The rationale behind the recommendations is presented in the **Why is DevOps Guru recommending this?** column.
For more information about how to respond to recommendations, see [Responding to recommendations](working-with-rds.analyzing.md "working-with-rds.analyzing.md").
