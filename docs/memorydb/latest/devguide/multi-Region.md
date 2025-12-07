# Using MemoryDB Multi-Region with the console

Here are ways to use MemoryDB Multi-Region with the console.

###### Topics

- [Create a new cluster in MemoryDB Multi-Region](#multi-Region.console.create "#multi-Region.console.create")
- [Restore a snapshot to a new or existing cluster within a Multi-Region cluster](#multi-Region.console.restore "#multi-Region.console.restore")
- [Modify clusters in MemoryDB Multi-Region](#multi-Region.console.modify "#multi-Region.console.modify")
- [Delete clusters in MemoryDB Multi-Region](#multi-Region.console.delete "#multi-Region.console.delete")

## Create a new cluster in MemoryDB Multi-Region

1. Navigate to the create cluster section from the cluster list or dashboard.

![Create a cluster, console view.](images/create-multi-region1.png) 2. In the **Cluster type** field, select **Multi-Region cluster**. 3. In the **Cluster creation method** field, select **Easy create**. 4. Fill in the **Name** and **Description**, verify the default values and select **Create**.

###### Create and configure a cluster

1. Navigate to the create cluster section from the cluster list or dashboard.

![Create and configure a cluster, console view.](images/create-multi-region2-configure.png) 2. In the **Cluster type** field, select **Multi-Region cluster**. 3. In the **Cluster creation method** field, select **Create new cluster**. 4. Fill in the **Name** and **Description**, verify the values and select **Create**.

## Restore a snapshot to a new or existing cluster within a Multi-Region cluster

1. Navigate to the create cluster section from the cluster list or dashboard.

![Restore a cluster, console view.](images/restore-multi-region-from-snapshot1.png) 2. In the **Cluster type** field, select **Multi-Region cluster**. 3. In the **Cluster creation method** field, select **Restore from snapshot**. 4. Select the source snapshot, then fill in the required fields. Review your selection, and then select **Restore**.

![Console view of selecting the source snapshot to restore to Multi-Region cluster.](images/restore-multi-region-from-snapshot2-confirm.png) 5. To see your Multi-Region clusters, navigate to the cluster section:

![Console view of the cluster section for modifying Multi-Region clusters.](images/restore-multi-region-from-snapshot3-confirm.png) 6. Now select the target multi regional cluster name.

![Console view of selecting the multi regional cluster to modify.](images/restore-multi-region-from-snapshot4-confirm.png) 7. Now select the target regional cluster name.

![Console view of selecting theregional cluster to modify.](images/restore-multi-region-from-snapshot5-confirm.png)

## Modify clusters in MemoryDB Multi-Region

1. Navigate to the cluster section. You should see all your current clusters.

![This is my image.](images/modify-multi-region1.png)

Then depending on the type of cluster you want to modify, select from the following steps. 2. To modify a single cluster with a Muti-Region cluster, first select the Multi-Region it beloongs to. Then select the edit button on the actions (Top right). Then select the target single cluster. You can also modify this cluster from the **Details** page.

###### Modify a regional cluster

1. To modify a multi regional cluster, select the target Multi-Region cluster name.

![Console view of selecting a target Multi-Region cluster to modify.](images/modify-multi-region2.png)

Then select the cluster, and select the **Edit** button on the actions (Top right) or from the details page. 2. To add a regional cluster, select the target Multi Region cluster selected, then go to the **Actions** dropdown and select **Add AWS Region**. You can also go to the details page for AWS Regions, select the target Multi Region cluster, and add from there.

![Console view of selecting a target Multi-Region cluster to add a regional cluster to.](images/modify-multi-region3-add-regional-cluster.png) 3. To add a Region, select the target Region. Then fill in the required information and select **Add AWS Region**.

![Console view of selecting a target Multi-Region cluster to add a Region to.](images/modify-multi-region4-add-region.png) 4. To add a new regional cluster to an empty Multi Region cluster, you will see the same options as in create Multi Region cluster. The only difference is that the multi regional cluster information is already present.

![Console view of selecting an empty Multi-Region cluster to add a new regional cluster to.](images/modify-multi-region5-add-regional-cluster-to-empty.png)

## Delete clusters in MemoryDB Multi-Region

1. To delete a single cluster in a Region, select the target regional cluster. Then go to the action menu dropdown, select the individual cluster, and select **Delete**.

![Console view of selecting a single cluster to delete.](images/delete-multi-region1-select.png)

You will be presented with a confirmation window, including the option to create a snapshot before deleting. If you still want to delete, enter "delete" into the text field and then select **Delete**.

![Consolve view of a confirmation window for deletion.](images/delete-multi-region2-snapshot.png) 2. To delete all associated regional clusters with a Multi Region cluster, select the target multi regional cluster with one or more clusters in it. Then with the target multi regional cluster selected, go to the action menu dropdown and select **Delete**.

![Console view of selecting to delete all associated clusters with a Multi Region cluster.](images/delete-multi-region3-associated-clusters.png) 3. To delete an entire multi regional cluster, select the target empty multi regional cluster. Then go to the action menu dropdown and select **Delete**.

![Console view of deleting an entire multi regional cluster.](images/delete-multi-region4-entire-mrc.png)
