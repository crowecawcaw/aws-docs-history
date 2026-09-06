

# Configuring an analysis rule for an intermediate table
<a name="intermediate-table-analysis-rule"></a>

An intermediate table is not available for analysis until you attach an analysis rule to it. The only supported analysis rule type for intermediate tables is Custom.

You can view the inherited constraints from base tables on the **Analysis rule** tab of the intermediate table details page. Each constraint displays a "View sources" link that shows which data provider's table imposed the value.

For first-party intermediate tables (all base tables owned by the creator), you have full control over the analysis rule configuration. For multi-party intermediate tables (base tables from different providers), you can only make inherited controls more restrictive.

**Note**  
AWS Clean Rooms generates inherited constraints as a point-in-time snapshot of the base table analysis rules when you populate an intermediate table. Inherited constraints do not get updated when a base table analysis rule changes asynchronously. To refresh inherited constraints, populate the intermediate table again.

The following table describes the validation rules for multi-party intermediate tables.


| Deferred control | Validation | 
| --- | --- | 
| allowedResultReceivers | Must be a subset of the intersection of all base table values. | 
| disallowedOutputColumns | Must be a superset of the union of all base table values. | 
| allowedAdditionalAnalyses | Must be a subset of the intersection of all base table values. | 
| additionalAnalyses | Must be equal to or more restrictive (REQUIRED > ALLOWED > NOT\_ALLOWED). | 

**To configure an analysis rule for an intermediate table**

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration, and then choose the **Tables** tab.

1. Choose the intermediate table.

1. In the alert at the top of the intermediate table details page, choose **Configure analysis rule**.

1. In **Step 1 - Specify analysis controls**, choose the analysis control method:
   + **Review each new analysis** – Requires approval of each analysis template before use.
   + **Allow any analysis by specific collaborators** – Allows specified collaborators to run any analysis.

   (Optional) Add allowed analysis templates (up to 50).

1. In **Step 2 - Specify analysis results controls**, configure the following:
   + **Columns not allowed in output** – Choose **None** or **Custom list** and select the columns to disallow.
   + **Additional analyses applied to output** – Choose **Not allowed**, **Allowed**, or **Required**.
   + **Results delivery** – Select the members who can receive results.

1. In **Step 3 - Set differential privacy**, choose to turn differential privacy on or off.

1. In **Step 4 - Review and configure**, review all settings.

   Use the **Edit** buttons to modify any settings. You can preview what members see by choosing **Table view** or **JSON**.

   Review the **Columns available for analysis** table, which shows the column name, type, and whether each column is allowed in query output.

1. Choose **Configure analysis rule**.