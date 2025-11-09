# Adding a collaboration analysis rule to a

configured table

The _collaboration analysis rule_ allows you to specify
controls that are specific to this collaboration. These controls work together with the
configured table analysis rule to determine how this table can be analyzed within this
collaboration.

You add a collaboration analysis rule to a configured table after you've [created a configured
table](create-configured-table.md "create-configured-table.md"), [added an
analysis rule](add-analysis-rule.md "add-analysis-rule.md"), and [associated it to a collaboration](associate-configured-table.md "associate-configured-table.md"). You need
to add a collaboration analysis rule if the table is configured to support direct analysis or to
allow additional analysis.

- **Direct analysis** – The table can be used in queries that
  analyze it directly. For example, in a query that outputs an aggregate measurement analysis
  or a list of identifiers for activation.
- **Additional analysis** – The table can also be used as input
  into additional analyses, in addition to queries that analyze it directly. For example, the
  table can be used in a query that is a seed for a lookalike ML model, or an ML input channel for a custom ML model.

###### To add the collaboration analysis rule to a table

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you haven't yet done so).
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. On the **Tables** tab, under **Tables associated by
   you**, view the configured table you've associated to the collaboration.
   - If **Direct analysis status** or **Additional analysis
     status** has a status of **Ready**, then the table is ready
     to be queried.
   - If **Direct analysis status** or **Additional analysis
     status** has a status of **Not ready**, then select the
     status, and then choose **Configure** in the dialog box.

5. On the **Configure collaboration analysis rule** page, expand
   **View configured table analysis rule** to view the details.
6. For **Allowed additional analyses**, choose the option based on your
   goal.

| Your goal                                                         | Recommended option          |
| ----------------------------------------------------------------- | --------------------------- |
| Allow any additional analyses on the table.                       | **Any**                     |
| Allow only additional analyses on the table by a specific member. | **Any by specific members** |
| Allow only specific analyses on the table.                        | **Custom list**             |

7. For **Results delivery**, specify who can receive results from the
   **Members allowed to receive results for query output** dropdown.
8. Choose **Configure analysis rule**.
