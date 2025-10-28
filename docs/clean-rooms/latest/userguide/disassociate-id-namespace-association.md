# Disassociating ID namespace

associations

As a collaboration member, you can disassociate an ID namespace from the collaboration. This
action prevents the member who can query from querying the table.

###### Warning

Disassociating an ID namespace association from a collaboration deletes any data from
derived ID mapping tables, rendering them not queryable.

For example, if your ID namespace association was used as a SOURCE in three different ID
mapping tables, then all the data from these ID mapping tables will be deleted when you
disassociate your ID namespace association.

###### To disassociate an ID namespace association

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration.
4. Choose the **Entity resolution** tab.
5. For **Associated ID namespaces**, select the option button next to the ID
   namespace that you want to disassociate.
6. Choose **Disassociate**.
7. In the dialog box, confirm your decision to disconnect the ID namespace by choosing
   **Disassociate**. This action prevents any member who can query from
   accessing the ID mapping table.

If a member of the collaboration removes one of the ID namespaces, you can’t repopulate
the ID mapping table if the source has left the collaboration.

Even though the ID mapping table was populated previously, disassociating the ID namespace
means you can no longer run queries on that table.
