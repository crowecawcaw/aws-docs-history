# Deleting a Neptune Analytics graph

You can delete a Neptune Analytics graph when you no longer need it. Before deleting the graph, you can save a snapshot of your data.
You can then restore that snapshot at a later date to create a new graph containing the same data. For more information
about creating snapshots, see [Graph snapshots](graph-snapshots.md "graph-snapshots.md").

Neptune Analytics doesn't provide a single-step method to delete a graph and its snapshot. Also, the graph cannot be deleted if
delete-protection is enabled. This design choice is intended to prevent you from accidentally losing data or taking
your application offline. Neptune Analytics graph applications are typically mission critical and require high availability.

**Deleting a Neptune Analytics graph**

AWS Console

Choose the graph you want to delete, then choose **Delete graph** from the drop-down
**Actions** menu. You can choose the following options to preserve the data from the
graph in case it is needed later.

- Create a final snapshot of the graph. The default setting is to create a final snapshot.

If you graph has private graph endpoints configured then you need to delete all of the private graph
endpoints first. To delete the private graph endpoints:

In the navigation pane, choose **graphs**, and then choose the graph that you want to
delete. On the graph page, go to the graph private endpoints section and choose the private graph
endpoint you want to delete. Select the delete button and enter "confirm" in the text box.

CLI/API

You can call the [delete-graph](../../../cli/latest/reference/neptune-graph/delete-graph.md "../../../cli/latest/reference/neptune-graph/delete-graph.md") CLI command, or the
[DeleteGraph](../apiref/API_DeleteGraph.md "../apiref/API_DeleteGraph.md")
API operation. You can choose the following options to preserve the data from the graph in case it is
needed later.

- Create a final snapshot of the graph
- Retain automated backups

```
aws neptune-graph delete-graph --graph-id g-sample
```

If your graph has private graph endpoints configured, you will need to delete the private graph endpoints first.

```
aws neptune-graph delete-private-graph-endpoint --graph-identifier g-sample --vpc-id your-vpc-id
```
