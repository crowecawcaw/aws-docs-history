

# Adding a data access budget to an existing associated table
<a name="add-access-budget-to-existing-associated-table"></a>

As a collaboration member, you can add a data access budget to an existing associated table.

**To add a data access budget to an existing associated table**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Tables** tab.

1. Select the option button next to the table you want to add a data access budget to.

1. From the **Actions** dropdown list, under **Data access budget**, select **Add** (if there isn't already a budget).

1. Choose one of the following budget configurations:


<table>
<thead>
  <tr><th>Per period budget only</th><th>Lifetime budget only</th><th>Both per period and lifetime budgets</th></tr>
</thead>
<tbody>
  <tr><td> <ol><li> Leave <b>Add per period budget</b> selected. </li><li> Enter a <b>Per period budget amount</b> between 1 and 1,000,000. </li><li> For <b>Period</b>, choose <b>Daily</b>, <b>Weekly</b>, or <b>Monthly</b>. </li><li> (Optional) Leave <b>Automatically refresh budget weekly</b> selected to renew the allocation. </li><li> Clear <b>Add lifetime budget</b>. </li></ol> </td><td> <ol><li> Clear <b>Add per period budget</b>. </li><li> Select <b>Add lifetime budget</b>. </li><li> Enter a <b>Lifetime budget amount</b> between 1 and 1,000,000. </li></ol> </td><td> <ol><li> Leave <b>Add per period budget </b>selected. </li><li> Enter a <b>Per period budget amount</b> between 1 and 1,000,000. </li><li> For <b>Period</b>, choose <b>Daily</b>, <b>Weekly</b>, or <b>Monthly</b>. </li><li> Leave <b>Automatically refresh budget weekly</b> selected. </li><li> Select <b>Add lifetime budget</b>. </li><li> Enter a <b>Lifetime budget amount</b> between 1 and 1,000,000. </li></ol> </td></tr>
</tbody>
</table>


1. Review your selections under **Data access budget summary**.

1.   
**Example**  

   For example, if you've chosen a **Per period budget amount** of 1,000, set the **Period** to **Weekly**, left the **Automatically refresh budget weekly** checkbox selected, and set the **Lifetime budget** to 1,000,000, then the **Access budget summary** will display the following message: Every week, this table can be used up to 1,000 times for running queries or jobs. This budget is set to automatically refresh every Sunday at 00:00 UTC, and will continue to refresh until this table has reached its lifetime budget of 1,000,000 uses.

1. (Optional) If you want to enable **Data access budget tags** for the access budget resource, choose **Add new tag** and enter a Key and Value pair.

1. Choose **Add data access budget**.