After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Using Managed kdb Insights clusters

After you successfully create clusters in your kdb environment, you can use the
clusters to do the following:

- **Monitor cluster metrics** – You can view
  the available cluster metrics in CloudWatch for your clusters. Using the
  **Monitoring** tab you can adjust the date and time range and
  refresh frequency as you need. You can also add the graphs to CloudWatch dashboards from
  this tab. For more information, see the [Monitoring Managed kdb cluster
  metrics](kdb-cluster-logging-monitoring.md#kdb-cluster-monitoring-metrics "kdb-cluster-logging-monitoring.md#kdb-cluster-monitoring-metrics") section.
- **View logs** – You can view KDB
  application logs from Managed kdb Insights clusters using the
  **Logs** tab. You can view data directly in CloudWatch using CloudWatch
  reporting or CloudWatch Insights. For more information, see the [Logging](kdb-cluster-logging-monitoring.md#kdb-cluster-logging "kdb-cluster-logging-monitoring.md#kdb-cluster-logging") section.
- **Connect to clusters** – FinSpace provides you
  the ability to discover clusters in your dedicated account and connect to them.
  You can do this by using discovery API operations and q API operations. For more
  information on how to connect to a cluster, see the [Connecting to a cluster endpoint or node in
  a cluster](interacting-with-kdb-clusters.md#connect-kdb-clusters "interacting-with-kdb-clusters.md#connect-kdb-clusters") section.
- **Load code on to a cluster** – You can run
  your own KDB code on the cluster and perform analytics or query data in a
  database. For this, FinSpace provides a set of q API operations that you can use to
  perform required functions. For more information, see the [Running code on a Managed kdb
  Insights cluster](interacting-with-kdb-loading-code.md "interacting-with-kdb-loading-code.md") section.
