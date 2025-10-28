# Clone an Amazon EMR cluster using the console

You can use the Amazon EMR console to clone a cluster, which makes a copy of the
configuration of the original cluster to use as the basis for a new cluster.

Console

###### To clone a cluster with the console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left navigation pane,
   choose **Clusters**.
3. _To clone a cluster from the cluster list_
   1. Use the search and filter options to find the cluster that
      you want to clone in the list view.
   2. Select the check box to the left of the row for the
      cluster that you want to clone.
   3. The **Clone** option will now be
      available at the top of the list view. Select
      **Clone** to initiate the cloning
      process. If the cluster has steps configured, choose
      **Include steps** and
      **Continue** if you want to clone the
      steps along with the other cluster configurations.
   4. Review the settings for the new cluster that have copied
      over from the cloned cluster. Adjust the settings if needed.
      When you are satisfied with the new cluster's configuration,
      select **Create cluster** to launch the new
      cluster.

4. _To clone a cluster from a cluster detail
   page_
   1. To navigate to the detail page of the cluster that you
      want to clone, select its **Cluster ID**
      from the cluster list view.
   2. At the top of the cluster detail page, select
      **Clone cluster** from the
      **Actions** menu to initiate the
      cloning process. If the cluster has steps configured, choose
      **Include steps** and
      **Continue** if you want to clone the
      steps along with the other cluster configurations.
   3. Review the settings for the new cluster that have copied
      over from the cloned cluster. Adjust the settings if needed.
      When you are satisfied with the new cluster's configuration,
      select **Create cluster** to launch the new
      cluster.
