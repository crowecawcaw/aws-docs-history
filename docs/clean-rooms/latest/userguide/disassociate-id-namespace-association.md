

# Disassociating ID namespace associations
<a name="disassociate-id-namespace-association"></a>

As a collaboration member, you can disassociate an ID namespace from the collaboration. This action prevents the member who can query from querying the table.

**Warning**  
Disassociating an ID namespace association from a collaboration deletes any data from derived ID mapping tables, rendering them not queryable.   
For example, if your ID namespace association was used as a SOURCE in three different ID mapping tables, then all the data from these ID mapping tables will be deleted when you disassociate your ID namespace association.  
Disassociating an ID namespace association also causes all dependent intermediate tables (and their descendants) to become unusable with a status of `BASE_TABLE_REMOVED`. The stored data in those intermediate tables is removed and storage-based billing stops. For more information, see [Deleting an intermediate table](delete-intermediate-table.md).

**To disassociate an ID namespace association**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. Choose the **Entity resolution** tab.

1. For **Associated ID namespaces**, select the option button next to the ID namespace that you want to disassociate.

1. Choose **Disassociate**.

1. In the dialog box, confirm your decision to disconnect the ID namespace by choosing **Disassociate**. This action prevents any member who can query from accessing the ID mapping table.

   If a member of the collaboration removes one of the ID namespaces, you can’t repopulate the ID mapping table if the source has left the collaboration.

   Even though the ID mapping table was populated previously, disassociating the ID namespace means you can no longer run queries on that table.