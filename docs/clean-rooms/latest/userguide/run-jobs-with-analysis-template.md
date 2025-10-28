# Running a PySpark job on a configured

table using a PySpark analysis template

This procedure demonstrates how to use a PySpark analysis template in the AWS Clean Rooms
console to analyze configured tables with the **Custom** analysis rule.

###### To run a PySpark job on a configured table using a PySpark analysis template

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").

1. In the left navigation pane, choose **Collaborations**.
2. Choose the collaboration that has **Your member abilities** status
   of **Run jobs**.
3. On the **Analysis** tab, under the **Tables**
   section, view the tables and their associated analysis rule type (**Custom
   analysis rule**).

###### Note

If you don’t see the tables that you expect in the list, it might be for the
following reasons:

    * The tables haven't been [associated](associate-configured-table.md "associate-configured-table.md").
    * The tables don't have an [analysis rule
     configured](add-analysis-rule.md "add-analysis-rule.md").

4. Under the **Analysis** section, for **Analysis
   mode**, select **Run analysis templates**.
5. Choose the PySpark analysis template from the **Analysis template**
   dropdown list.

The parameters from the PySpark analysis template will automatically populate in the
**Definition**. 6. (Spark analytics engine only) Specify the supported **Worker type**
and the **Number of workers**.

Use the following table to determine the type and number or workers you need for
your use case.

| Worker type         | vCPU | Memory (GB)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Storage (GB) | Number of workers | Total Clean Rooms Processing Units (CRPU) |
| ------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ----------------- | ----------------------------------------- |
| **CR.1X** (default) | 4    | 30                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 100          | 4                 | 8                                         |
| 128                 | 256  |
| **CR.4X**           | 16   | 120                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 400          | 4                 | 32                                        |
| 32                  | 256  | ###### Note Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/ "https://aws.amazon.com/clean-rooms/pricing/"). 7. Choose **Run**. ###### Note You can't run the job if the member who can receive results hasn’t configured the job results settings. 8. Continue to adjust parameters and run your job again, or choose the **+** button to start a new job in a new tab. |
