After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Example: Detecting Data

Anomalies and Getting an Explanation (RANDOM_CUT_FOREST_WITH_EXPLANATION
Function)

Amazon Kinesis Data Analytics provides the `RANDOM_CUT_FOREST_WITH_EXPLANATION` function, which
assigns an anomaly score to each record based on values in the numeric columns. The
function also provides an explanation of the anomaly. For more information, see [RANDOM_CUT_FOREST_WITH_EXPLANATION](../sqlref/sqlrf-random-cut-forest-with-explanation.md "../sqlref/sqlrf-random-cut-forest-with-explanation.md") in the
_Amazon Managed Service for Apache Flink SQL Reference_.

In this exercise, you write application code to obtain anomaly scores for records in
your application's streaming source. You also obtain an explanation for each
anomaly.

###### Topics

- [Step 1: Prepare the Data](app-anomaly-with-ex-prepare.md "app-anomaly-with-ex-prepare.md")
- [Step 2: Create an Analytics
  Application](app-anom-with-exp-create-app.md "app-anom-with-exp-create-app.md")
- [Step 3: Examine the Results](examine-results-with-exp.md "examine-results-with-exp.md")

###### First Step

[Step 1: Prepare the Data](app-anomaly-with-ex-prepare.md "app-anomaly-with-ex-prepare.md")
