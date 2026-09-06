

# Deleting an ID mapping table
<a name="delete-id-mapping-table"></a>

As a collaboration member, you can delete an ID mapping table that you have created. This action prevents the member who can query from querying the table.

**Warning**  
Deleting a mapping table permanently removes any populated data.  
Deleting an ID mapping table also causes all dependent intermediate tables (and their descendants) to become unusable with a status of `BASE_TABLE_REMOVED`. The stored data in those intermediate tables is removed and storage-based billing stops. For more information, see [Deleting an intermediate table](delete-intermediate-table.md).

**To delete an ID mapping table**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Entity resolution** tab.

1. For ID mapping tables, choose a table.

1. On the ID mapping table details page, scroll down to view the **ID mapping tables**.

1. Choose and ID mapping table, and then choose **Delete**.

1. If you’re certain that you want to delete the ID mapping table, choose **Delete**.