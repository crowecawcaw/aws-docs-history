

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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/add-access-budget-to-existing-associated-table.html)

1. Review your selections under **Data access budget summary**.

1.   
**Example**  

   For example, if you've chosen a **Per period budget amount** of 1,000, set the **Period** to **Weekly**, left the **Automatically refresh budget weekly** checkbox selected, and set the **Lifetime budget** to 1,000,000, then the **Access budget summary** will display the following message: Every week, this table can be used up to 1,000 times for running queries or jobs. This budget is set to automatically refresh every Sunday at 00:00 UTC, and will continue to refresh until this table has reached its lifetime budget of 1,000,000 uses.

1. (Optional) If you want to enable **Data access budget tags** for the access budget resource, choose **Add new tag** and enter a Key and Value pair.

1. Choose **Add data access budget**.