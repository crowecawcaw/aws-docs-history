After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing kdb dataviews

The following sections provide a detailed overview of the operations that you can perform by using a Managed kdb dataview.

## Creating a kdb dataview

###### To create a kdb dataview

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Databases** tab.
5. On database details page, choose the **Dataviews** tab.
6. Choose **Create dataview**.
7. On the **Create dataview** page, enter a unique name for the dataview.
8. (Optional) Enter a description for your dataview.
9. Choose the availability zone that you want to associate with the dataview.
   Currently, you can only choose single availability zone.
10. Choose a how you want to update data in the dataview from one of the following options.
    - **Auto-update** – Adds the most recent version of the
      data in a database. The dataview is automatically updated as new data is added to
      the database.
    - **Static** – Add data based on the changeset ID that you
      specify. The dataview is not automatically updated as new data is added to the
      database. To refresh the contents of a static dataview, you need to update it and
      specify a new changeset ID. When you choose this, the **Read
      Write** option enables.
    1. If you choose **Static**, specify the **Changeset
       ID** to indicate which version of data you want.
    2. If you choose **Static**, you get the option to make dataviews
       writable. Select **True** if you want to make the dataview writable
       to perform database maintenance operations. By default, this value is set to
       **False**. For more information, read [this](finspace-managed-kdb-databases-dbmaint.md "finspace-managed-kdb-databases-dbmaint.md") section.

11. (Optional) For **segment configuration**, specify the database path of the
    data that you want to place on each selected volume. You can also enable **On
    demand caching** on the selected database path when a particular file or a
    column of a database is accessed.

###### Note

    * Each [segment](finspace-managed-kdb-dataviews.md#segment "finspace-managed-kdb-dataviews.md#segment") must have a unique database path for
     each volume.
    * Every data view has a default segment associated with it. The default segment
     is S3/object store segment. All database paths not explicitly specified to be on a
     volume are accessible from the cluster through this default segment.
    * The **Segment configuration** is required if **Read
     Write** is **True**. You can only add one segment for
     a writeable dataview.
    * The **Database path** is disabled and defaults to
     **\\*** when **Read Write** is
     **True** as you cannot have partial writeable dataviews on
     cache.

12. Choose **Create dataview**. The database details page opens and the table
    under **Dataviews** lists the newly created database along with its
    status.

You can choose the dataview name from the list to view its details.

## Viewing kdb dataview details

###### To view and get details of a kdb dataview

1.  Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2.  In the left pane, under **Managed kdb Insights**, choose **Kdb
    environments**.
3.  From the kdb environments table, choose the name of the environment.
4.  On the environment details page, choose **Databases** tab.
5.  From the list of databases, choose a database name. The database details page
    opens.
6.  On the database details page, choose the **Dataviews** tab that
    shows a list of dataviews along with its status, availability zones where they were
    created, and their creation time.
7.  From the list of dataviews, choose a name to view its details. The dataviews details page
    opens where you can view the following details.
    - **Dataview details** section – Displays the metadata of
      the dataview that you created.
    - **Configuration** tab – Displays the details
      about the dataview update mode and ID, and the availability zones ID.
    - **Active versions** tab – Displays a list of active versions of the dataview. Each update of the dataview creates a new version,
      including changeset details and the cache configurations. Each version triggers a
      workflow to cache database based on the cache configuration. A dataview version
      becomes active once the workflow finishes.

    The dataview version is deactivated under the following conditions

        + It's not the latest active version.
        + No cluster is currently mounting this version.

    You can choose the **Version ID** to see details of each active
    version.
    - **Clusters** tab – Displays a list of
      clusters that mounts the dataview.

## Updating a kdb dataview

###### To update a kdb dataview

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Databases** tab.
5. From the list of databases, choose a database name. The database details page opens.
6. On the database details page, choose the **Dataviews** tab.
7. From the list of dataviews, choose a name and then choose **Edit**.
8. On the edit page, you can update the description for the dataview. If the dataview is
   **Static**, you can also update the **Changeset
   ID**.
9. Choose **Save changes**.

## Deleting a kdb dataview

Before deleting a dataview, make sure that it is not in use by any cluster. You can check
this from the **Clusters** tab in the dataview details page.

###### Note

This action is irreversible. Deleting a kdb dataview will delete all of its metadata.

###### To delete a kdb dataview

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Databases** tab.
5. From the list of databases, choose the one whose dataview you want to delete. The database details page opens.
6. On the database details page, choose the **Dataviews** tab.
7. From the list of dataviews, choose a name and then choose **Delete**.
8. On the confirmation dialog box, enter **confirm** to provide a written
   consent to delete the resource permanently.
9. Choose **Delete**.
