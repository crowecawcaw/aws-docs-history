Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Connection fails

Your query connection can fail because for the following reasons. We suggest the following
troubleshooting approaches.

###### Client cannot connect to server

If you are using SSL or server certificates, first remove this complexity while
you troubleshoot the connection issue. Then add SSL or server certificates back when
you have found a solution. For more information, go to [Configure Security Options for
Connections](../mgmt/connecting-ssl-support.md "../mgmt/connecting-ssl-support.md") in the _Amazon Redshift Management Guide._

###### Connection is refused

Generally, when you receive an error message indicating that there is a failure to
establish a connection, it means that there is an issue with the permission to access
the cluster. For more information, go to [The connection is
refused or fails](../mgmt/connecting-refusal-failure-issues.md "../mgmt/connecting-refusal-failure-issues.md") in the _Amazon Redshift Management Guide._
