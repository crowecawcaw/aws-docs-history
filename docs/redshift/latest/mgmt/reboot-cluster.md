Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Rebooting a cluster

Rebooting a cluster is a cluster operation that restarts the cluster with the same
configuration as before the reboot. You can reboot a cluster to apply pending
maintenance updates, reset configuration changes, recover from certain issues, or
troubleshoot cluster problems. Rebooting a cluster can help ensure optimal performance,
security, and stability of the Amazon Redshift environment. The following procedure provides
detailed steps for rebooting an Amazon Redshift cluster.

When you reboot a cluster, the cluster status is set to `rebooting` and a
cluster event is created when the reboot is completed. Any pending cluster modifications
are applied at this reboot.

###### To reboot a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose the cluster to reboot.
4. For **Actions**, choose **Reboot cluster**.
   The **Reboot cluster** page appears.
5. Choose **Reboot cluster**.
