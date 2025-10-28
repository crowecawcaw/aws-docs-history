# AWS Direct Connect Classic connection

A Classic connection offers a straightforward approach to establishing dedicated
network connectivity between your on-premises infrastructure and AWS. This connection type
is ideal for organizations that prefer to manage their own network configurations and have
existing Direct Connect infrastructure in place. The Classic connection does not rely on the
AWS Direct Connect Resiliency Toolkit.

Select Classic when you have existing connections and you want to add additional
connections. A Classic connection has a 95% SLA. However, it does not provide resiliency or
redundancy, which are found only in the AWS Direct Connect Resiliency Toolkit when creating a connection.

###### Note

Before you configure a Classic connection, familiarize yourself with the [Connection prerequisites](connection_options.md#connect-prereqs.title "connection_options.md#connect-prereqs.title").

###### Tasks

- [Configure a Classic connection](toolkit-classic.md "toolkit-classic.md")
