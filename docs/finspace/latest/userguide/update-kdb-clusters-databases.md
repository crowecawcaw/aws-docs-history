After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Updating a kdb cluster

database

You can update the databases mounted on a kdb cluster using the console. This
feature is only available for HDB clusters types. With this feature, you can update
the data in a cluster by selecting a changeset. You can also update the cache by
providing database paths. You can't change a database name or add a new database if
you created a cluster without one.

You can also choose how you want to update the databases on the cluster by
selecting a deployment mode.

###### To update a kdb cluster database

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the list of environments, choose a kdb environment.
4. On the environment details page, choose the **Clusters**
   tab.
5. From the list of clusters, choose the one where you want to update the
   database. The cluster details page opens.
6. On the cluster details page, choose the **Details**
   tab.
7. Under **Data management and storage** section, choose
   **Edit**.

###### Note

This button is not available for _RDB_
and _Gateway_ type clusters. 8. On the edit page, modify the changeset that you want to cache as
needed. 9. Choose a deployment mode from one of the following options.

    * **Rolling** – (Default) To update the
     database, this option stops the existing q process and starts a new q
     process with the updated database configuration. The initialization
     script re-runs when the new q process starts.
    * **No restart** – This option updates the
     database but doesn't stop the existing q process. **No
     restart** is often quicker than the other deployment modes
     because it reduces the turnaround time to update the changeset
     configuration for a kdb database on your cluster. This option doesn't
     re-run the initialization script.

###### Note

After the update completes, you must re-load the updated database. However, if you use a
historical database (HDB) cluster with a single database in a rolling
deployment, FinSpace autoloads the database after an update. 10. Choose **Save changes**. The cluster details page opens and
the updated information is displayed once the cluster updates
successfully.
