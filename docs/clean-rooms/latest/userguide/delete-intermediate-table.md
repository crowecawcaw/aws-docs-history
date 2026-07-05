# Deleting an intermediate table

You can remove an intermediate table from a collaboration by deleting it as the owner.
Other collaboration actions can cause an intermediate table to reach an unusable state without
deleting the resource (such as `DISALLOWED_BY_DATA_PROVIDER` or
`BASE_TABLE_REMOVED`). In any of these deletion scenarios, the stored data in
AWS Clean Rooms is deleted, and storage-based billing stops.

###### To delete an intermediate table

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms/](https://console.aws.amazon.com/cleanrooms/ "https://console.aws.amazon.com/cleanrooms/").
2. In the left navigation pane, choose **Collaborations**.
3. Choose the collaboration, and then choose the **Tables** tab.
4. Choose the intermediate table that you want to delete.
5. Choose **Delete**.
6. To confirm deletion, choose **Delete**.

## Other deletion triggers

In addition to explicit owner deletion, an intermediate table can become unusable through
the following triggers which will delete the corresponding stored data in AWS Clean Rooms from the
intermediate table.

### Data provider disallowing

A data provider can disallow a specific intermediate table that references their base
table. This deletes the corresponding stored data in AWS Clean Rooms from the intermediate table.
The intermediate table status is changed to `DISALLOWED_BY_DATA_PROVIDER`. The
data provider can optionally cascade the disallow action to descendant intermediate tables
by using the `includeDescendants` flag, which will delete the corresponding
data stored in AWS Clean Rooms from descendant tables.

### Cascading behavior

When base tables (configured table associations or ID mapping tables) are removed from
a collaboration, dependent intermediate tables become unusable with a status of
`BASE_TABLE_REMOVED` and the corresponding data stored in AWS Clean Rooms is deleted
from the dependent intermediate tables. The owner must call `DeleteIntermediateTable` to
remove the resource.
