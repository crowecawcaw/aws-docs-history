# Querying configured tables using a SQL analysis

template

This procedure demonstrates how to use an analysis template in the AWS Clean Rooms console to
query configured tables with the **Custom** analysis rule.

###### To use a SQL analysis template to query configured tables with the

**Custom** analysis rule

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration that has **Your member abilities** status
   of **Run queries**.
4. On the **Analysis** tab, under the **Tables**
   section, view the tables and their associated analysis rule type (**Custom
   analysis rule**).

###### Note

If you don’t see the tables that you expect in the list, it might be for the
following reasons:

    * The tables haven't been [associated](associate-configured-table.md "associate-configured-table.md").
    * The tables don't have an [analysis rule
     configured](add-analysis-rule.md "add-analysis-rule.md").

5. Under the **Analysis** section, for **Analysis
   mode**, select **Run analysis templates** and then choose
   the analysis template from the dropdown list.
6. The parameters form the SQL analysis template will automatically populate in the
   **Definition**.
7. (Spark analytics engine only) Specify the supported **Worker type**
   and the **Number of workers**.

Use the following table to determine the type and number or workers you need for
your use case.

| Worker type         | vCPU | Memory (GB)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Storage (GB) | Number of workers | Total Clean Rooms Processing Units (CRPU) |
| ------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------- | ----------------------------------------- |
| **CR.1X** (default) | 4    | 30                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 100          | 4                 | 8                                         |
| 128                 | 256  |
| **CR.4X**           | 16   | 120                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 400          | 4                 | 32                                        |
| 32                  | 256  | ###### Note Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/ "https://aws.amazon.com/clean-rooms/pricing/"). 8. Choose **Run**. ###### Note You can't run the query if the member who can receive results hasn’t configured the query results settings. 9. Continue to adjust parameters and run your query again, or choose the **+** button to start a new query in a new tab. |
