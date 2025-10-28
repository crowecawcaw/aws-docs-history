# Connect to an Amazon Athena data source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

###### Note

This guide assumes that you are familiar with the Amazon Athena service before
you use the Athena data source.

With Amazon Managed Grafana, you can add Athena as a data source by using the AWS data source
configuration option in the Grafana workspace console. This feature simplifies
adding Athena as a data source by discovering your existing Athena accounts and
manages the configuration of the authentication credentials that are required to
access Athena. You can use this method to set up authentication and add Athena as a
data source, or you can manually set up the data source and the necessary
authentication credentials using the same method that you would on a self-managed
Grafana server.

There are prerequisites for Athena to be accessible by Amazon Managed Grafana. For
prerequisites associated with using the Athena data source, see [Prerequisites](Athena-prereq.md "Athena-prereq.md").
