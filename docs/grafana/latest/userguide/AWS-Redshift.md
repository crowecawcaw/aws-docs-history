# Connect to an Amazon Redshift data source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

###### Note

This guide assumes that users are familiar with the Amazon Redshift service before using the
Amazon Redshift data source.

With Amazon Managed Grafana, you can add Amazon Redshift as a data source by using the AWS data source
configuration option in the Grafana workspace console. This feature simplifies adding Amazon Redshift
as a data source by discovering your existing Amazon Redshift accounts and manages the configuration of
the authentication credentials that are required to access Amazon Redshift. You can use this method to
set up authentication and add Amazon Redshift as a data source, or you can manually set up the data
source and the necessary authentication credentials using the same method that you would on
a self-managed Grafana server.

There are prerequisites for Amazon Redshift to be accessible by Amazon Managed Grafana. For prerequisites
associated with using the Amazon Redshift data source, see [Prerequisites](Redshift-prereq.md "Redshift-prereq.md").
