After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Viewing a Managed kdb volume

###### To view and get details of a Managed kdb volume

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Volumes** tab. The table under this tab displays a list of volumes created in the environment.
5. Choose a volume name to view its details. The volume details page opens where you can view the following details.
   - **Volume details** section – Displays the metadata of the
     volume that you created.
   - **Configuration** tab – Displays the details about the
     network attached storage and availability zones.
   - **Monitoring** tab – Displays the dashboard of volume
     metrics. You can view activity logs for your volume here.
   - **Clusters** tab – Displays a list of clusters attached to
     this volume. For information on how to create clusters, see [Creating a Managed kdb Insights cluster](create-kdb-clusters.md "create-kdb-clusters.md").
   - **Tags** tab – Displays a list of key-value pairs
     associated with the volume. If you did not provide tags during volume creation,
     choose **Manage tags** to add new tags.
