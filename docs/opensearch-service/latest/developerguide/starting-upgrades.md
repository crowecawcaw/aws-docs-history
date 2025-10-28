# Upgrading a domain (console)

The upgrade process is irreversible and can't be paused or cancelled. During an
upgrade, you can't make configuration changes to the domain. Before starting an upgrade,
double-check that you want to proceed. You can use these same steps to perform the
pre-upgrade check without actually starting an upgrade.

If the cluster has dedicated master nodes, OpenSearch upgrades complete without
downtime. Otherwise, the cluster might be unresponsive for several seconds post-upgrade
while it elects a master node.

###### To upgrade a domain to a later version of OpenSearch or Elasticsearch

1. [Take a manual snapshot](managedomains-snapshots.md "managedomains-snapshots.md") of your
   domain. This snapshot serves as a backup that you can [restore on a new domain](managedomains-snapshot-restore.md "managedomains-snapshot-restore.md") if
   you want to return to using the prior OpenSearch version.
2. Go to https://aws.amazon.com and
   choose **Sign In to the Console**.
3. Under **Analytics**, choose
   **Amazon OpenSearch Service**.
4. In the navigation pane, under **Domains**, choose the domain
   that you want to upgrade.
5. Choose **Actions** and **Upgrade**.
6. Select the version to upgrade to. If you're upgrading to an OpenSearch version,
   the **Enable compatibility mode** option appears. If you enable
   this setting, OpenSearch reports its version as 7.10 to allow Elasticsearch
   OSS clients and plugins like Logstash to continue working with Amazon OpenSearch Service. You can
   disable this setting later
7. Choose **Upgrade**.
8. Check the **Status** on the domain dashboard to monitor the
   status of the upgrade.
