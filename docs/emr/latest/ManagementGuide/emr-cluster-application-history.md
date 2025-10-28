# View Amazon EMR application history

You can view Spark History Server and YARN timeline service application details with the
cluster's detail page in the console. Amazon EMR application history makes it easier for you to
troubleshoot and analyze active jobs and job history.

###### Note

To augment the security for the off-console applications that you might use with
Amazon EMR, the application hosting domains are registered in the Public Suffix List (PSL).
Examples of these hosting domains include the following:
`emrstudio-prod.us-east-1.amazonaws.com`,
`emrnotebooks-prod.us-east-1.amazonaws.com`,
`emrappui-prod.us-east-1.amazonaws.com`. For further security, if you
ever need to set sensitive cookies in the default domain name, we recommend that you use
cookies with a `__Host-` prefix. This helps to defend your domain against
cross-site request forgery attempts (CSRF). For more information, see the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#cookie_prefixes") page in the _Mozilla Developer
Network_.

The **Application user interfaces** section of the
**Applications** tab provides several viewing options, depending on the
cluster status and the applications you installed on the cluster.

- [Off-cluster
  access to persistent application user interfaces](app-history-spark-UI.md "app-history-spark-UI.md") – Starting with
  Amazon EMR version 5.25.0, persistent application user interface links are available for
  Spark UI and Spark History Service. With Amazon EMR version 5.30.1 and later, Tez UI and
  the YARN timeline server also have persistent application user interfaces. The YARN
  timeline server and Tez UI are open-source applications that provide metrics for
  active and terminated clusters. The Spark user interface provides details about
  scheduler stages and tasks, RDD sizes and memory usage, environmental information,
  and information about the running executors. Persistent application UIs are run
  off-cluster, so cluster information and logs are available for 30 days after an
  application terminates. Unlike on-cluster application user interfaces, persistent
  application UIs don't require you to set up a web proxy through a SSH
  connection.
- [On-cluster
  application user interfaces](emr-web-interfaces.md "emr-web-interfaces.md") – There are a variety of application
  history user interfaces that can be run on a cluster. On-cluster user interfaces are
  hosted on the master node and require you to set up a SSH connection to the web
  server. On-cluster application user interfaces keep application history for one week
  after an application terminates. For more information and instructions on setting up
  an SSH tunnel, see [View web interfaces hosted on Amazon EMR
  clusters](emr-web-interfaces.md "emr-web-interfaces.md").

With the exception of the Spark History Server, YARN timeline server, and Hive
applications, on-cluster application history can only be viewed while the cluster is
running.
