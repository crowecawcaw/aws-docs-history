# Adding a data access budget

to an existing associated table

As a collaboration member, you can add a data access budget to an existing associated
table.

###### To add a data access budget to an existing associated table

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. Choose the **Tables** tab.
5. Select the option button next to the table you want to add a data access budget
   to.
6. From the **Actions** dropdown list, under **Data access
   budget**, select **Add** (if there isn't already a
   budget).
7. Choose one of the following budget configurations:

| Per period budget only                                                                                                                                                                                                                                                                                                                             | Lifetime budget only                                                                                                                                | Both per period and lifetime budgets                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Leave **Add per period budget\*<br>• selected.<br>2. Enter a **Per period budget amount*<br>• between 1 and<br>1,000,000.<br>3. For **Period**, choose **Daily**,<br>**Weekly**, or **Monthly**.<br>4. (Optional) Leave \*\*Automatically refresh budget<br>weekly*<br>• selected to renew the allocation.<br>5. Clear **Add lifetime budget**. | 1. Clear **Add per period budget**.<br>2. Select **Add lifetime budget**.<br>3. Enter a \*_Lifetime budget amount_<br>• between 1 and<br>1,000,000. | 1. Leave **Add per period budget\*<br>• selected.<br>2. Enter a **Per period budget amount*<br>• between 1 and<br>1,000,000.<br>3. For **Period**, choose **Daily**,<br>**Weekly**, or **Monthly**.<br>4. Leave **Automatically refresh budget weekly**<br>selected.<br>5. Select **Add lifetime budget**.<br>6. Enter a \*\*Lifetime budget amount*<br>• between 1 and<br>1,000,000. |

8. Review your selections under **Data access budget summary**.
9. ###### Example

For example, if you've chosen a **Per period budget amount** of
1,000, set the **Period** to **Weekly**, left the
**Automatically refresh budget weekly** checkbox
selected, and set the **Lifetime budget** to 1,000,000, then the
**Access budget summary** will display the following message: Every
week, this table can be used up to 1,000 times for running queries or jobs. This budget
is set to automatically refresh every Sunday at 00:00 UTC, and will continue to refresh
until this table has reached its lifetime budget of 1,000,000 uses. 10. (Optional) If you want to enable **Data access budget tags** for the
access budget resource, choose **Add new tag** and enter a Key and Value
pair. 11. Choose **Add data access budget**.
