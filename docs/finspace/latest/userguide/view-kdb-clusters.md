After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Viewing kdb cluster detail

###### To view and get details of a kdb cluster

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Clusters**
   tab. The table under this tab displays a list of clusters.
5. Choose a cluster name to view its details. The cluster details page opens
   where you can view the cluster details and the following tabs.
   - **Configuration** tab – Displays the cluster configuration
     details like the node details, code, availability zones, savedown
     database configuration etc.
   - **Monitoring** tab – Displays the
     dashboard of cluster metrics.
   - **Nodes** tab – Displays a list of
     nodes in this cluster along with their status. All the nodes that are
     active will have a **Running** status and nodes that are
     being prepared or stuck due to lack of resources have the status as
     **Provisioning**. From here you could also delete a
     node. For this, select a node and choose
     **Delete**.
   - **Logs** section – Displays the
     activity logs for your clusters.
   - **Tags** tab – Displays a list of key-value pairs
     associated with the clusters. If you did not provide tags during cluster
     creation, choose **Manage tags** to add new tags.
