# Deleting a graph snapshot

Deleting a graph snapshot is an important task in managing and maintaining your Neptune graph database. The
AWS Neptune Console and Command Line Interface (CLI) or Software Development Kit (SDK) provide the
necessary tools to accomplish this.

CLI/SDK
**Delete a snapshot**

```
aws neptune-graph delete-graph-snapshot \
--snapshot-id <SNAPSHOT_ID>
```

Neptune Console

1. Expand **Analytics** and choose **Snapshots**.
2. Select the snapshot you want to delete, and choose the **Delete** button.
3. Type "confirm" in the text box to confirm you want to delete the snapshot, then choose the
   **Delete** button.
